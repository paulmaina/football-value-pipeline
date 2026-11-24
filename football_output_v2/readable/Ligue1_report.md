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
| Training as of utc | 2026-11-24T15:18:59.800617+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 99, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 99, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 361, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-24T15:18:59.800617+00:00', 'observations': 1098, 'observations_sha256': '9dc5b59457cb166942eab82dd775b1f2ea483d9ab552a10718155387f4c80092', 'eligible_training_matches': 415, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 360, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 41, 'retrospective_eligible_training_matches': 415, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'a4dbb89e42d6bf57ff095f91c0c405c7535d75f7f653eeae0ddb96bfcd786b53', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 354, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-10-05T00:00:00+00:00', 'audit_origin_utc': '2026-10-17T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 39, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1777, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1489, 'tuning_matches': 189, 'audit_matches': 95, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8570382866976696, 'audit_candidate_poisson_score': 0.8512580175470882, 'audit_gain': 0.005780269150581385, 'audit_gain_lower95': -0.001752721712168081, 'audit_baseline_briers': [0.5856032374357698, 0.1628927417464559, 0.22821981475151296, 0.24145157511779713], 'audit_candidate_briers': [0.5842467140794457, 0.16219801987764715, 0.22431110130082776, 0.24020901700559263], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1602.686 |
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
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261124T151859800617Z_833aacc5f956a81d36416c1f53871297dbe3e1f73026c81398491b17abb164de.json |
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

The model's most likely 1X2 outcome is **Paris FC win** at **38.4%**. Expected goals are 1.39 for Stade Brestois 29 and 1.46 for Paris FC (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.2%; Double Chance 1X: 61.6%; Double Chance X2: 64.6%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| Stade Brestois 29 win | 35.4% | 2.82 |
| Draw | 26.2% | 3.82 |
| Paris FC win | 38.4% | 2.60 |

| Measure | Benchmark estimate |
| --- | --- |
| Stade Brestois 29 expected goals | 1.39 |
| Paris FC expected goals | 1.46 |
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
| 4 | 0-1 | 7.91% |
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
| Bbs statistics cutoff utc | 2026-11-24T15:18:59.800617+00:00 |
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
| Score matrix json | [[0.06389483624702608,0.07914412411555213,0.06167610974123747,0.029913800700914074,0.010881467834080678,0.003166601085779499,0.0007679235458974771,0.00015962312984877302,2.903231806601614e-05,4.6936973389751364e-06,6.8295322453502e-07,9.033876576065267e-08,1.0953900326514469e-08,1.2260306024729635e-09,1.274233894133246e-10,1.2360435479919986e-11],[0.07522278402856476,0.12327801880344308,0.08559036830355488,0.04151256021322144,0.015100641780257074,0.004394417130707734,0.0010656777705029448,0.00022151530845318404,4.0289292019253986e-05,6.5136287880960785e-06,9.47761106647255e-07,1.253666657313996e-07,1.520115920476006e-08,1.7014109881014163e-09,1.7683045957552842e-10,1.7153063472343647e-11],[0.05610235109545681,0.08163134266557576,0.059388563716755494,0.02880430796284066,0.010477877876983616,0.003049152923836627,0.0007394415216275619,0.0001537027620169999,2.7955519220368343e-05,4.519609694132724e-06,6.57622720710333e-07,8.698813153065003e-08,1.0547623872801369e-08,1.1805575426067204e-09,1.2269729905027472e-10,1.1901991113672096e-11],[0.02595181458483447,0.03776101050673551,0.027471950175750773,0.013324291137535707,0.004846854696755088,0.0014104765624808567,0.00034205071429101576,7.109979355865425e-05,1.2931658607236631e-05,2.090680167367375e-06,3.0420298938293505e-07,4.0238952851076436e-08,4.879117785844122e-09,5.461020769045537e-10,5.67572925704102e-11,5.50562071893951e-12],[0.009003588981944203,0.013100610634918793,0.009530976999945586,0.004622660989117824,0.0016815428224541229,0.0004893434790746512,0.00011866931433212447,2.4666996437208475e-05,4.486443079876925e-06,7.253298168474959e-07,1.0553861944910906e-07,1.3960295198264837e-08,1.6927360125293652e-09,1.8946184385534158e-10,1.9691082963060105e-11,1.9100917156203423e-12],[0.002498927057013086,0.0036360467414320754,0.002645302484675442,0.001283009769134416,0.0004667086497377386,0.00013581624644181707,3.293641691290327e-05,6.846272629259349e-06,1.2452027768633928e-06,2.0131375479416417e-07,2.9292020352114797e-08,3.874650371623334e-09,4.698152959417586e-10,5.258473358026015e-11,5.465218380910011e-12,5.30141911088162e-13],[0.0005779765943702255,0.0008409808948548521,0.0006118317527040171,0.0002967472038957381,0.00010794499790680844,3.1412926343042756e-05,7.617860643292097e-06,1.583473726167545e-06,2.880028283546984e-07,4.656183863761509e-08,6.774948519535753e-09,8.961675051223618e-10,1.0866353380319389e-10,1.2162317881704075e-11,1.2640498242727957e-12,1.2261647071439678e-13],[0.0001145829856522831,0.00016672319043298928,0.00012129471958649803,5.882968434628381e-05,2.1399932569706726e-05,6.22756513589111e-06,1.5102293506236775e-06,3.13921271230581e-07,5.7096125121019906e-08,9.230814085769514e-09,1.3431232969819247e-09,1.776638524495375e-10,2.1542381224389523e-11,2.411161124710062e-12,2.5059596580418563e-13,2.430852986341118e-14],[1.9876415650334505e-05,2.892104279471565e-05,2.104068286375611e-05,1.0205033949745187e-05,3.7121912317367394e-06,1.0802796979486564e-06,2.6197559899010077e-07,5.4455115067392185e-08,9.904317892124019e-09,1.6012455646468973e-09,2.329881418998308e-10,3.0818891279748615e-11,3.736901433283576e-12,4.182579153601441e-13,4.3470237298025584e-14,4.216738119217461e-15],[3.064809486569242e-06,4.459430104402544e-06,3.2443316531091643e-06,1.5735475354387588e-06,5.723948977085539e-07,1.6657185705237946e-07,4.039487376191029e-08,8.396612155167652e-09,1.5271791437541367e-09,2.4690128658957404e-10,3.5925203020229906e-11,4.7520655646044535e-12,5.762050444396376e-13,6.44925548639788e-14,6.70281795260016e-15,6.501926311818866e-16],[4.25315691661241e-07,6.18852691359965e-07,4.5022869025546094e-07,2.1836739325227765e-07,7.943349591194197e-08,2.3115833106101147e-08,5.605755838627146e-09,1.1652309620014715e-09,2.1193266878833052e-10,3.4263464642118624e-11,4.985482013671124e-12,6.594628675245216e-13,7.996224499059212e-14,8.949886020379873e-15,9.301764648283998e-16,9.022979400710576e-17],[5.365703164673933e-08,7.807329730834263e-08,5.6800008922663455e-08,2.7548821640199075e-08,1.0021181177940116e-08,2.9162502414858463e-09,7.072116649688175e-10,1.470033573406743e-10,2.6737028844942742e-11,4.322614572361975e-12,6.289590801057647e-13,8.319660112798357e-14,1.0087887172105296e-14,1.1291008698844946e-15,1.1734932190111314e-16,1.1383221939467525e-17],[6.20516479826076e-09,9.028782645513973e-09,6.5686342514854055e-09,3.1858821300584498e-09,1.1588990067833185e-09,3.3724961642538185e-10,8.1785458377114e-11,1.7000196063807633e-11,3.0920023919885113e-12,4.998885506276321e-13,7.273594203111174e-14,9.621266864949225e-15,1.166613218213274e-15,1.3057481482799523e-16,1.357085658697275e-17,1.3164121439778874e-18],[6.623962886310887e-10,9.638151942268391e-10,7.011963567476131e-10,3.4009032275151233e-10,1.237115251486454e-10,3.6001121892048025e-11,8.730531074400666e-12,1.8147570845859432e-12,3.300687371696731e-13,5.33626956624469e-14,7.764502574532552e-15,1.0270624021231388e-15,1.2453501093621873e-16,1.393875514071738e-17,1.448677888341517e-18,1.4052592426300351e-19],[6.565953117793873e-11,9.55374522491521e-11,6.950555858770568e-11,3.3711196051786164e-11,1.2262811374373086e-11,3.5685839819494977e-12,8.654072903461449e-13,1.798864236120714e-13,3.271781395974123e-14,5.2895368523700436e-15,7.696504458490986e-16,1.0180678390160868e-16,1.2344438780310855e-17,1.3816685622363138e-18,1.435991001292062e-19,1.3929525970810645e-20],[6.074554615216521e-12,8.838739191014949e-12,6.430373536447243e-12,3.1188236937892092e-12,1.1345057768971145e-12,3.3015097592750743e-13,8.006398698412443e-14,1.6642365322502547e-14,3.026919995062641e-15,4.893665842944424e-16,7.120495050849475e-17,9.418752432665219e-18,1.1420576147883059e-18,1.2782639459741051e-19,1.3285208724181348e-20,1.288703479232222e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.19890957718238206, "-10": 8.194338374409996e-07, "-11": 1.0677914989230549e-07, "-12": 1.2783514234385099e-08, "-13": 1.414763053162164e-09, "-14": 1.4457645288566825e-10, "-15": 1.2360435479919986e-11, "-2": 0.11520283745234851, "-3": 0.04843160625487896, "-4": 0.016091120993224007, "-5": 0.004399668816878818, "-6": 0.0010195945781270325, "-7": 0.00020475067707916746, "-8": 3.6245555136778095e-05, "-9": 5.733520744617592e-06, "0": 0.2617110109118599, "1": 0.1894484256816369, "10": 5.103103065061708e-07, "11": 6.34218563508296e-08, "12": 7.241604374769094e-09, "13": 7.643641144166881e-10, "14": 7.449827036895367e-11, "15": 6.074554615216521e-12, "2": 0.10479179152285523, "3": 0.04201699670794161, "4": 0.013314181679420709, "5": 0.0034720039406822864, "6": 0.0007673964485819857, "7": 0.00014697709483759897, "8": 2.4814819048811036e-05, "9": 3.743775429155046e-06} |
| Raw goal margin distribution | {"-1": 0.19890957718238206, "-10": 8.194338374409996e-07, "-11": 1.0677914989230549e-07, "-12": 1.2783514234385099e-08, "-13": 1.414763053162164e-09, "-14": 1.4457645288566825e-10, "-15": 1.2360435479919986e-11, "-2": 0.11520283745234851, "-3": 0.04843160625487896, "-4": 0.016091120993224007, "-5": 0.004399668816878818, "-6": 0.0010195945781270325, "-7": 0.00020475067707916746, "-8": 3.6245555136778095e-05, "-9": 5.733520744617592e-06, "0": 0.2617110109118599, "1": 0.1894484256816369, "10": 5.103103065061708e-07, "11": 6.34218563508296e-08, "12": 7.241604374769094e-09, "13": 7.643641144166881e-10, "14": 7.449827036895367e-11, "15": 6.074554615216521e-12, "2": 0.10479179152285523, "3": 0.04201699670794161, "4": 0.013314181679420709, "5": 0.0034720039406822864, "6": 0.0007673964485819857, "7": 0.00014697709483759897, "8": 2.4814819048811036e-05, "9": 3.743775429155046e-06} |
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
| Count model | {"corners": {"alpha": 0.015563401279930092, "mu": 8.88300535333006, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-22 |
| Elo home rating | 1,519.1581 |
| Elo away rating | 1,513.5245 |
| Elo rating diff | 65.6336 |
| Elo home expectancy | 0.5933 |
| Research p home | 0.3873 |
| Research p draw | 0.2666 |
| Research p away | 0.3462 |
| Research p over 1 5 | 0.7727 |
| Research v4 p home | 0.3921 |
| Research v4 p draw | 0.2520 |
| Research v4 p away | 0.3559 |
| Research v4 p over 1 5 | 0.7709 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.3877394125967062, 1.4550431679179001], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "team_news": "dated news leads; absences and tactics require confirmation", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [{"headline": "Paris Saint-Germain drop one of this season's best kits in latest Jordan collab", "published_at_utc": "2026-11-24T13:21:57+00:00", "source": "ESPN league news; unconfirmed context lead", "url": "https://www.espn.com/soccer/story/_/id/50581189/psg-kit-nike-jordan-champions-league"}], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:19:59.955875+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 4.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-22", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:19:59.724999+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:19:59.805327+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:19:59.955332+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Stade+Brestois+29_vs_Paris+FC&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 0.9312494032006584, "goals_for": 2.213236948620373, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 2.2686762445488604, "results": "WWWLWLWDWW", "xg_against": 0.9528064296311309, "xg_for": 1.9202236507517008, "xg_matches": 10}, "venue": {"goals_against": 1.1612768438259973, "goals_for": 1.1708095557758593, "last_match": "2026-11-07T00:00:00+00:00", "matches": 4, "points_per_game": 1.514299067924793, "results": "WLLW", "xg_against": 0.9386567683674618, "xg_for": 1.226017240444295, "xg_matches": 4}}, "home": {"all": {"goals_against": 0.7849059493921307, "goals_for": 1.667360393435035, "last_match": "2026-11-21T00:00:00+00:00", "matches": 10, "points_per_game": 1.9393909626348576, "results": "WWWLDWLLWD", "xg_against": 1.3513413427138565, "xg_for": 1.7558598510679808, "xg_matches": 10}, "venue": {"goals_against": 1.1151840416711334, "goals_for": 2.021622295578943, "last_match": "2026-11-08T00:00:00+00:00", "matches": 5, "points_per_game": 1.5140209424328015, "results": "WLWLD", "xg_against": 0.909037295991237, "xg_for": 2.399795463650609, "xg_matches": 5}}}, "goal_rates": [1.4459423146269244, 1.3658870624337847], "h2h": [{"away": "Brest", "away_goals": 0.0, "away_xg": null, "date": "2026-05-03T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 2.0, "away_xg": null, "date": "2025-09-14T00:00:00+00:00", "home": "Brest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.18848647043842556, "-10": 4.374973041855451e-07, "-11": 5.3532782882488235e-08, "-12": 6.015524476355475e-09, "-13": 6.203158610465356e-10, "-14": 5.3037980139414315e-11, "-2": 0.10110601684354655, "-3": 0.04000818867568046, "-4": 0.012500384096190384, "-5": 0.0032125285163666357, "-6": 0.0006995232938227457, "-7": 0.00013196333860111733, "-8": 2.194170980436925e-05, "-9": 3.2597000850286688e-06, "0": 0.26657450821570994, "1": 0.20260102682507636, "10": 7.847271840598482e-07, "11": 1.0164811108331488e-07, "12": 1.209175018325699e-08, "13": 1.3199720326894761e-09, "14": 1.1947443786636977e-10, "2": 0.11498227861883445, "3": 0.048165821848622205, "4": 0.015931241417980423, "5": 0.004334204796723481, "6": 0.000999081215942494, "7": 0.0001995207566378382, "8": 3.511894261442515e-05, "9": 5.523123878316854e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:19:59.955875+00:00", "p_over_1_5": 0.7726844104141903, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.1946754343500756, "-10": 4.47327039455996e-07, "-11": 5.473556305733981e-08, "-12": 6.150681910583719e-09, "-13": 6.342531828078675e-10, "-14": 5.422964303439016e-11, "-2": 0.10337767742365452, "-3": 0.04090709685081611, "-4": 0.012781244035826476, "-5": 0.003284707943674068, "-6": 0.0007152402564828751, "-7": 0.00013492830471963704, "-8": 2.2434698439258166e-05, "-9": 3.332939368083334e-06, "0": 0.2519634324023579, "1": 0.206085448707291, "10": 7.906547946823385e-07, "11": 1.0241593260811064e-07, "12": 1.2183087896906663e-08, "13": 1.3299427338468907e-09, "14": 1.2037691449952123e-10, "2": 0.1158508227319783, "3": 0.048529653053951134, "4": 0.016051581579219792, "5": 0.0043669441727958, "6": 0.0010066279972298611, "7": 0.00020102788087219317, "8": 3.538422132723195e-05, "9": 5.564844018048808e-06}, "p_over_1_5": 0.7709282834217628, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
