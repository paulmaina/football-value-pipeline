# Ligue 1 — football model report

Fixtures in this report: **2**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,752 |
| Training data through | 2026-10-26 |
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
| Training sha256 | ed606a506424ef7ecb06a191d932b6a5dbe577e0d070ca7f9c54a36f28d8a21f |
| Training as of utc | 2026-10-27T11:27:31.296367+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 71, 'bbs_added_results': 8, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 71, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 93, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-27T11:27:31.296367+00:00', 'observations': 305, 'observations_sha256': 'bdb5ae3123e606d9b4647db4cd909db1f138cc75659c329dee54df99786e17cc', 'eligible_training_matches': 131, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 131, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 15, 'retrospective_eligible_training_matches': 131, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'd15b2d7e53c0dbe7a26607a8e495f3f81d7c4a2ef77ffeda9d6178db16e7a8b8', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 70, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-08-24T00:00:00+00:00', 'audit_origin_utc': '2025-09-27T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 28, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-27', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1750, 'tune_start_date': '2025-10-28', 'audit_start_date': '2026-04-28', 'training_shot_matches': 1453, 'tuning_matches': 196, 'audit_matches': 97, 'audit_matchdays': 32, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8794267693315355, 'audit_candidate_poisson_score': 0.8748035361069939, 'audit_gain': 0.004623233224541612, 'audit_gain_lower95': -0.0027891338597886314, 'audit_baseline_briers': [0.6035169394663551, 0.16831616921012935, 0.2150058083521931, 0.24570292417472075], 'audit_candidate_briers': [0.6021996013104772, 0.16740657079202217, 0.21307578129089047, 0.24370977187987214], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1588.433 |
| Base scoring parameter | 0.208 |
| Home-advantage parameter | 0.192 |
| Dixon-Coles low-score adjustment | -0.056 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1752, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 8.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261027T112731296367Z_6b3b55e6f0c47441914a04782a51477e49585e5d93856ee7500bcafcbbe53c58.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 2} |
| Legacy comparison status | {'AVAILABLE': 2} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Le Havre AC vs Paris Saint-Germain FC

The model's most likely 1X2 outcome is **Paris Saint-Germain FC win** at **70.0%**. Expected goals are 0.80 for Le Havre AC and 2.26 for Paris Saint-Germain FC (3.06 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 59.0%; Under 3.5 goals: 63.4%; Double Chance 1X: 30.0%; Double Chance X2: 88.8%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre AC win | 11.2% | 8.95 |
| Draw | 18.8% | 5.32 |
| Paris Saint-Germain FC win | 70.0% | 1.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre AC expected goals | 0.80 |
| Paris Saint-Germain FC expected goals | 2.26 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 59.0% |
| Under 2.5 | 41.0% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.5% |
| Under 4.5 | 80.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.00% |
| 2 | 0-1 | 10.14% |
| 3 | 1-2 | 9.57% |
| 4 | 0-3 | 9.05% |
| 5 | 1-1 | 8.94% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T18:00:00+00:00 |
| Fixture id | fdorg:559644 |
| Matched home-team name | Le Havre |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7974 |
| Dc lambda away | 2.2620 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-27T11:27:31.296367+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.35 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.39 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.13 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.2305828774629504, "-10": 5.3360247499710855e-05, "-11": 1.0826516266176095e-05, "-12": 2.0176911048047894e-06, "-13": 3.476609263525418e-07, "-14": 5.569678689178531e-08, "-15": 8.335329408392977e-09, "-16": 1.1651197111992665e-09, "-17": 1.4015864372126743e-10, "-2": 0.2105740790658163, "-3": 0.13945809851551874, "-4": 0.07266760896485072, "-5": 0.03108079803838089, "-6": 0.011249070678299247, "-7": 0.0035242587265579433, "-8": 0.0009725884896000711, "-9": 0.00023971565178627563, "0": 0.18779501524934666, "1": 0.07819897018868092, "10": 1.5808667539485075e-09, "11": 1.1306648908271104e-10, "12": 7.427926479161526e-12, "13": 4.511661865605792e-13, "14": 2.5478775084479012e-14, "15": 1.3441226948967343e-15, "16": 6.622995181720784e-17, "17": 2.8084811859179502e-18, "2": 0.026166184311754038, "3": 0.006108674278439622, "4": 0.0011220490513444298, "5": 0.0001691729321935852, "6": 2.15835612470239e-05, "7": 2.383647248757589e-06, "8": 2.3188415316927814e-07, "9": 2.014680018968109e-08} |
| Raw goal margin distribution | {"-1": 0.2305828774629504, "-10": 5.3360247499710855e-05, "-11": 1.0826516266176095e-05, "-12": 2.0176911048047894e-06, "-13": 3.476609263525418e-07, "-14": 5.569678689178531e-08, "-15": 8.335329408392977e-09, "-16": 1.1651197111992665e-09, "-17": 1.4015864372126743e-10, "-2": 0.2105740790658163, "-3": 0.13945809851551874, "-4": 0.07266760896485072, "-5": 0.03108079803838089, "-6": 0.011249070678299247, "-7": 0.0035242587265579433, "-8": 0.0009725884896000711, "-9": 0.00023971565178627563, "0": 0.18779501524934666, "1": 0.07819897018868092, "10": 1.5808667539485075e-09, "11": 1.1306648908271104e-10, "12": 7.427926479161526e-12, "13": 4.511661865605792e-13, "14": 2.5478775084479012e-14, "15": 1.3441226948967343e-15, "16": 6.622995181720784e-17, "17": 2.8084811859179502e-18, "2": 0.026166184311754038, "3": 0.006108674278439622, "4": 0.0011220490513444298, "5": 0.0001691729321935852, "6": 2.15835612470239e-05, "7": 2.383647248757589e-06, "8": 2.3188415316927814e-07, "9": 2.014680018968109e-08} |
| Unadjusted home-win probability | 11.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 70.0% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 49.7% |
| P home draw | 30.0% |
| P draw away | 88.8% |
| P home away | 81.2% |
| Raw p home draw | 30.0% |
| Raw p draw away | 88.8% |
| Raw p home away | 81.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5900 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04724312196656944, 0.09337827073628803, 0.1148011849995984, 0.08926611459758298, 0.052058081208242915, 0.02428732408754257, 0.00944256392159539, 0.003146686009966156, 0.0009175398558687544, 0.00023781757398560138, 5.547604098196055e-05, 1.1764522129120778e-05, 2.286938894767442e-06, 4.103672786573015e-07, 6.837639572370682e-08, 1.0633505527775619e-08, 1.5503080222229996e-09, 2.127309055427817e-10, 2.7568910246434597e-11], [0.030088699301905223, 0.08701475968623625, 0.09560149847041967, 0.07433698805627302, 0.04335173518479123, 0.02022544084901136, 0.007863361866085264, 0.0026204250223525374, 0.000764087802122362, 0.00019804426614327127, 4.6198065351854984e-05, 9.796988980003064e-06, 1.9044645336267014e-06, 3.417362526615342e-07, 5.694092697053289e-08, 8.855126908771856e-09, 1.2910299664219487e-09, 1.7715316563091559e-10, 2.2958204924146683e-11], [0.014630527892536688, 0.034128838813368076, 0.039806411884257244, 0.030952326188890187, 0.018050731989279367, 0.00842143943199318, 0.0032741350945791055, 0.0010910887320856573, 0.0003181497597177367, 8.246138141708891e-05, 1.9235882774586183e-05, 4.079255919656918e-06, 7.929781526171466e-07, 1.42291640265834e-07, 2.370897975790373e-08, 3.6870847701932976e-09, 5.375571661589804e-10, 7.376277558961272e-11, 9.559303734308444e-12], [0.004061225180862816, 0.009473677272654232, 0.011049690311352995, 0.008591922823832258, 0.005010624895173002, 0.0023376710759540342, 0.0009088530495495227, 0.0003028706186030631, 8.83138205908647e-05, 2.2890099463236085e-05, 5.339605793727091e-06, 1.132343069353322e-06, 2.2011938768973968e-07, 3.9498123151705636e-08, 6.5812735065071385e-09, 1.0234819702112987e-09, 1.4921817691019678e-10, 2.04754909621329e-11, 2.6535259234968205e-12], [0.0008455034957122708, 0.0019723179322889204, 0.0023004269324465583, 0.0017887461194399615, 0.0010431583268356594, 0.00048667802904853646, 0.00018921345068574177, 6.305441224586896e-05, 1.8385989622328374e-05, 4.7654730411318766e-06, 1.1116486191397545e-06, 2.3574167421083365e-07, 4.5826494094124486e-08, 8.223085328094484e-09, 1.3701505107894935e-09, 2.1307796171703242e-10, 3.106562295434687e-11, 4.26277746589525e-12, 5.524356184069171e-13], [0.00014081980277878478, 0.00032849234054084053, 0.00038313935847329673, 0.0002979181955346661, 0.00017373949439238585, 8.10569139157114e-05, 3.15137677653398e-05, 1.0501801520424623e-05, 3.062212569952702e-06, 7.936962735257293e-07, 1.8514664942300935e-07, 3.926310918578068e-08, 7.632467391446293e-09, 1.3695664890892993e-09, 2.2820050500688604e-10, 3.5488435822752676e-11, 5.174023430791271e-12, 7.099716146430892e-13, 9.200893340660028e-14], [1.954478106360991e-05, 4.559238651277794e-05, 5.3177001603787926e-05, 4.134891394314608e-05, 2.4113798720026625e-05, 1.1250119691355855e-05, 4.373885485627215e-06, 1.4575749109137913e-06, 4.2501319465685643e-07, 1.1015936388884417e-07, 2.5697030220374826e-08, 5.4494386284448434e-09, 1.059331863823868e-09, 1.9008602947241137e-10, 3.167259732618192e-11, 4.925540973347879e-12, 7.181174321885801e-13, 9.853898028372558e-14, 1.2770181635272026e-14], [2.325150659332014e-06, 5.4239117448126494e-06, 6.326217722160045e-06, 4.919085775617861e-06, 2.868705196051637e-06, 1.3383738161500149e-06, 5.203405803139993e-07, 1.7340083033455287e-07, 5.056182039414832e-08, 1.3105141303150158e-08, 3.057054799709459e-09, 6.482940780293188e-10, 1.26023728462607e-10, 2.261364071150914e-11, 3.767939907643425e-12, 5.859684385551965e-13, 8.543105269364894e-14, 1.172271893099891e-14, 1.519208434845375e-15], [2.420357063413617e-07, 5.646001066726928e-07, 6.58525316932423e-07, 5.120504322921838e-07, 2.986168167747738e-07, 1.3931753223841193e-07, 5.4164662143034676e-08, 1.8050095928949107e-08, 5.263214176632541e-09, 1.3641748844449293e-09, 3.182229997881073e-10, 6.748393462719802e-11, 1.3118393860543193e-11, 2.353958648052638e-12, 3.92222324750466e-13, 6.099617001170856e-14, 8.892914142661943e-15, 1.2202721339015075e-15, 1.5814144564429695e-16], [2.2395216187263807e-08, 5.224163673790292e-08, 6.093240150561933e-08, 4.737929086294345e-08, 2.7630585048437355e-08, 1.2890851107542319e-08, 5.011778372454418e-09, 1.6701494446424385e-09, 4.869976463692306e-10, 1.2622514221637772e-10, 2.944471699544598e-11, 6.244191520286473e-12, 1.2138261373806775e-12, 2.1780841189054401e-13, 3.629176822311192e-14, 5.6438879810597185e-15, 8.228485696189016e-16, 1.129100274464249e-16, 1.4632600771621065e-17], [1.8649774617560798e-09, 4.350459234988124e-09, 5.074188815523833e-09, 3.945543944497688e-09, 2.3009565051564727e-09, 1.0734947400102376e-09, 4.173593873703987e-10, 1.3908287582389886e-10, 4.0555073316210726e-11, 1.0511487961182384e-11, 2.452029625662756e-12, 5.199894635911303e-13, 1.0108222978409137e-13, 1.8138149494076353e-14, 3.0222226576169797e-15, 4.699987619382033e-16, 6.852329640158625e-17, 9.402662364723988e-18, 1.2185401747301493e-18], [1.411884697231249e-10, 3.293523351228282e-10, 3.841424192201341e-10, 2.9869814685290243e-10, 1.741943452531661e-10, 8.126912131965081e-11, 3.159627096614987e-11, 1.0529295289058026e-11, 3.070229457697232e-12, 7.957741743189475e-13, 1.8563136427241742e-13, 3.9365900200987206e-14, 7.652449229053326e-15, 1.373152020972172e-15, 2.2879793506443215e-16, 3.558134472431347e-17, 5.187569049877036e-18, 7.118303238627709e-19, 9.224981325205989e-20], [9.797974698840916e-12, 2.285587380375938e-11, 2.6658109629287586e-11, 2.072858280279285e-11, 1.2088464382528371e-11, 5.63978628034207e-12, 2.192668169795688e-12, 7.306954246414508e-13, 2.1306294065758602e-13, 5.522388082580812e-14, 1.2882152586675205e-14, 2.731852642944223e-15, 5.310525999570956e-16, 9.529183782168295e-17, 1.5877758171786325e-17, 2.4692180320618606e-18, 3.5999873359956444e-19, 4.9398477912200426e-20, 6.401807017166367e-21], [6.2764097720348e-13, 1.4641069618936637e-12, 1.7076714823628697e-12, 1.3278364525606734e-12, 7.743657062961311e-13, 3.6127476146998253e-13, 1.404584554536903e-13, 4.680706007684683e-14, 1.3648436170792931e-14, 3.537544399923694e-15, 8.25207972719265e-16, 1.7499766177149429e-16, 3.401829286443761e-17, 6.104227051840819e-18, 1.0171011827494731e-18, 1.5817375184231662e-19, 2.306088389625821e-20, 3.1643793643237087e-21, 4.100884657926011e-22], [3.733374723459074e-14, 8.70889588555684e-14, 1.0157682145980313e-13, 7.898322813410622e-14, 4.6061322628752677e-14, 2.1489579420154227e-14, 8.354840845850405e-15, 2.7842078722925264e-15, 8.118451226976448e-16, 2.1042250785846384e-16, 4.908555525921655e-17, 1.0409324292896324e-17, 2.0234981355295648e-18, 3.6309558823163563e-19, 6.049987149972462e-20, 9.408593582814256e-21, 1.3717224363284843e-21, 1.8822566344917934e-22, 2.439314780551456e-23], [2.0726627976620304e-15, 4.8349297479523316e-15, 5.639254415624964e-15, 4.384922776815107e-15, 2.5571928053144557e-15, 1.1930399464506233e-15, 4.638368522926315e-16, 1.5457125269524895e-16, 4.5071317719741897e-17, 1.1682055409238248e-17, 2.725089545634977e-18, 5.778958933620245e-19, 1.123388252536495e-19, 2.0158027882763432e-20, 3.3587797156517377e-21, 5.223381884193172e-22, 7.615410380938523e-23, 1.044975013477627e-23, 1.3542377532228302e-24], [1.0787653742482933e-16, 2.516451207064357e-16, 2.935080615628907e-16, 2.2822346527937924e-16, 1.330950242732109e-16, 6.209452814889725e-17, 2.4141463634028222e-17, 8.045018970278611e-18, 2.345841155765721e-18, 6.080196397480338e-19, 1.4183359912056385e-19, 3.007793068812008e-20, 5.84693443641997e-21, 1.0491712649827138e-21, 1.7481547220607983e-22, 2.71863012135861e-23, 3.9636167730295055e-24, 5.438814566295521e-25, 7.048444147907219e-26], [5.28440877907115e-18, 1.2327014908113247e-17, 1.43777007890328e-17, 1.1179688487432e-17, 6.519754262692551e-18, 3.041744549049539e-18, 1.1825867367700922e-18, 3.9409096629522723e-19, 1.1491269458359148e-19, 2.978427375249314e-20, 6.9478195560572e-21, 1.473388790360007e-21, 2.8641623474429013e-22, 5.1394399336252214e-23, 8.563460026578976e-24, 1.3317402674669167e-24, 1.9416058183055757e-25, 2.664241931374501e-26, 3.452730410442399e-27], [2.4447937624182936e-19, 5.703004899232988e-19, 6.651739991455098e-19, 5.172202572235064e-19, 3.016317476622718e-19, 1.407241266012217e-19, 5.47115258952831e-20, 1.8232335470332798e-20, 5.3163532702711125e-21, 1.377948030376507e-21, 3.214358809698696e-22, 6.816527401429253e-23, 1.3250841360559064e-23, 2.377724967419909e-24, 3.9618232678393613e-25, 6.161200685229107e-26, 8.98269984802897e-27, 1.232592391639797e-27, 1.5973809225722428e-28]] |
| Legacy trial inputs | {"lambda_home": 0.8327570701535364, "lambda_away": 2.33271410738213, "rho": -0.06159715442825365, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1119 |
| Legacy p draw | 0.1838 |
| Legacy p away | 0.7043 |
| Legacy p over 1 5 | 0.8293 |
| Legacy p under 3 5 | 0.6102 |
| Legacy p btts yes | 0.5154 |
| Legacy p over 2 5 | 0.6128 |
| Legacy goal margin distribution | {"-1": 0.2254624216184634, "-10": 6.610691260667737e-05, "-11": 1.3818077928563158e-05, "-12": 2.653439397521842e-06, "-13": 4.7114886336133725e-07, "-14": 7.77901077252182e-08, "-15": 1.2000951795710677e-08, "-16": 1.7370204915882236e-09, "-17": 2.3568911046692837e-10, "-18": 2.7568910246434597e-11, "-2": 0.2097267298162166, "-3": 0.14201437217386753, "-4": 0.07587973381499588, "-5": 0.033335044703847995, "-6": 0.012405180797200665, "-7": 0.003998818367356736, "-8": 0.0011359995761841212, "-9": 0.00028832347094284304, "0": 0.1837849842798938, "1": 0.07724150304852376, "10": 2.222363021864202e-09, "11": 1.658336187255338e-10, "12": 1.1368179596451545e-11, "13": 7.206040744183421e-13, "14": 4.2473666364341055e-14, "15": 2.3392028394147225e-15, "16": 1.208687263320881e-16, "17": 5.8547092689944485e-18, "18": 2.4447937624182936e-19, "2": 0.026728058341883812, "3": 0.006461044562284007, "4": 0.001232403859405732, "5": 0.0001932791938666314, "6": 2.56769818821433e-05, "7": 2.9548086888747075e-06, "8": 2.996626882925734e-07, "9": 2.7151342751558734e-08} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.1119 |
| Legacy raw p draw | 0.1838 |
| Legacy raw p away | 0.7043 |
| Legacy market weight | 0 |
| Legacy lambda home | 0.8328 |
| Legacy lambda away | 2.3327 |
| Legacy model home team | Le Havre |
| Legacy model away team | Paris SG |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.295393234483514, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,379.4397 |
| Elo away rating | 1,704.9432 |
| Elo rating diff | -265.5035 |
| Elo home expectancy | 0.1782 |

</details>


---

## 2026-10-30 — Lille OSC vs Racing Club de Lens

The model's most likely 1X2 outcome is **Lille OSC win** at **40.1%**. Expected goals are 1.28 for Lille OSC and 1.09 for Racing Club de Lens (2.37 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 42.3%; Under 3.5 goals: 78.5%; Double Chance 1X: 69.3%; Double Chance X2: 59.9%; Double Chance 12 (either team wins): 70.8%; Under 4.5 goals: 90.8%; BTTS Yes (both teams score): 48.7%; BTTS No (at least one team does not score): 51.3%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille OSC win | 40.1% | 2.49 |
| Draw | 29.2% | 3.43 |
| Racing Club de Lens win | 30.7% | 3.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille OSC expected goals | 1.28 |
| Racing Club de Lens expected goals | 1.09 |
| Expected total goals | 2.37 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 69.3% |
| Under 1.5 | 30.7% |
| Over 2.5 | 42.3% |
| Under 2.5 | 57.7% |
| Over 3.5 | 21.5% |
| Under 3.5 | 78.5% |
| Over 4.5 | 9.2% |
| Under 4.5 | 90.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.77% |
| 2 | 1-0 | 11.23% |
| 3 | 0-0 | 10.07% |
| 4 | 0-1 | 9.44% |
| 5 | 2-1 | 8.36% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:05:00+00:00 |
| Fixture id | fdorg:559639 |
| Matched home-team name | Lille |
| Matched away-team name | Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.2816 |
| Dc lambda away | 1.0894 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-27T11:27:31.296367+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.7% |
| P btts no | 51.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.93 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.25 |
| Fair Over 2.5 odds | 2.37 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.65 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.84 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.1840119202485526, "-10": 6.875481318961116e-08, "-11": 6.738667178049575e-09, "-12": 6.062933692143798e-10, "-13": 5.021346693617426e-11, "-14": 3.5530532687325312e-12, "-2": 0.08615307001261745, "-3": 0.02820900155803668, "-4": 0.007201785512257976, "-5": 0.001501470341440841, "-6": 0.00026405346757751895, "-7": 4.011360755881096e-05, "-8": 5.3601913543651565e-06, "-9": 6.390420189863324e-07, "0": 0.2916667099118157, "1": 0.21776652466149685, "10": 3.4903363586204777e-07, "11": 4.0243393900208016e-08, "12": 4.259511826817941e-09, "13": 4.150052924410839e-10, "14": 3.454550641117944e-11, "2": 0.11922946435313432, "3": 0.04592582507169915, "4": 0.0137932260208775, "5": 0.0033829754444392964, "6": 0.0006998909534333057, "7": 0.0001250796461067115, "8": 1.9662178471797588e-05, "9": 2.7576374775798266e-06} |
| Raw goal margin distribution | {"-1": 0.1840119202485526, "-10": 6.875481318961116e-08, "-11": 6.738667178049575e-09, "-12": 6.062933692143798e-10, "-13": 5.021346693617426e-11, "-14": 3.5530532687325312e-12, "-2": 0.08615307001261745, "-3": 0.02820900155803668, "-4": 0.007201785512257976, "-5": 0.001501470341440841, "-6": 0.00026405346757751895, "-7": 4.011360755881096e-05, "-8": 5.3601913543651565e-06, "-9": 6.390420189863324e-07, "0": 0.2916667099118157, "1": 0.21776652466149685, "10": 3.4903363586204777e-07, "11": 4.0243393900208016e-08, "12": 4.259511826817941e-09, "13": 4.150052924410839e-10, "14": 3.454550641117944e-11, "2": 0.11922946435313432, "3": 0.04592582507169915, "4": 0.0137932260208775, "5": 0.0033829754444392964, "6": 0.0006998909534333057, "7": 0.0001250796461067115, "8": 1.9662178471797588e-05, "9": 2.7576374775798266e-06} |
| Unadjusted home-win probability | 40.1% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.5% |
| Raw p btts yes | 48.7% |
| P home draw | 69.3% |
| P draw away | 59.9% |
| P home away | 70.8% |
| Raw p home draw | 69.3% |
| Raw p draw away | 59.9% |
| Raw p home away | 70.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4227 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10171900396672721, 0.09703768630165349, 0.05897722669856359, 0.022062739416505765, 0.006190073242785579, 0.0013893834678529167, 0.0002598766262570512, 4.1664437564699276e-05, 5.844829947817103e-06, 7.288291164292097e-07, 8.179411499183674e-08, 8.344987991992418e-09, 7.804423241288263e-10, 6.737422844533767e-11, 5.4008499628472845e-12], [0.10861545552532667, 0.13901381848355512, 0.0734792263380022, 0.027487779842677366, 0.007712159732097585, 0.0017310210740568664, 0.0003237780836711223, 5.190936925043073e-05, 7.28202404019188e-06, 9.080420122421995e-07, 1.0190659386749581e-07, 1.0396949734268458e-08, 9.723464697911132e-10, 8.394097956803056e-11, 6.72887314396748e-12], [0.07268622534103324, 0.08157338036925826, 0.04577357232162678, 0.017123395839825552, 0.004804257187320633, 0.0010783322344620695, 0.00020169618363840807, 3.233672135611142e-05, 4.536305982840191e-06, 5.656609192814469e-07, 6.348228032488145e-08, 6.476735729316265e-09, 6.057191083086207e-10, 5.2290677113706655e-11, 4.191722978704703e-12], [0.03018638380984261, 0.03387719415803286, 0.019009635126398396, 0.007111297863159734, 0.0019951944222887895, 0.00044782832718679333, 8.376385461926556e-05, 1.3429348923095942e-05, 1.883915044899108e-06, 2.3491737995120155e-07, 2.636401147562537e-08, 2.689770030604296e-09, 2.5155343255990485e-10, 2.171617031459491e-11, 1.7408106978460166e-12], [0.009402239866355279, 0.010551827190677182, 0.005920985778098161, 0.0022149764175703086, 0.0006214489505118088, 0.00013948637828509802, 2.6090168939151008e-05, 4.18287796972745e-06, 5.867884424831755e-07, 7.317039261777126e-08, 8.211674551502541e-09, 8.377904147905694e-10, 7.835207181597098e-11, 6.763998084787815e-12, 5.422153195351858e-13], [0.0023428341748084735, 0.002629286393495809, 0.0014753811885955068, 0.0005519240650355979, 0.0001548515949234463, 3.4756979040279434e-05, 6.501104022659254e-06, 1.0422824343801579e-06, 1.4621494834986935e-07, 1.8232474266317607e-08, 2.0461711299780868e-09, 2.0875919387272355e-10, 1.9523636295897097e-11, 1.6854415646303778e-12, 1.351082932118559e-13], [0.00048648620334711633, 0.0005459676014793387, 0.0003063608174437955, 0.00011460625161702923, 3.2154714706904706e-05, 7.2172375471273515e-06, 1.349945056955094e-06, 2.1642847358518013e-07, 3.0361327259167906e-08, 3.785947498469439e-09, 4.248845416056367e-10, 4.334855139683468e-11, 4.054055468051808e-12, 3.4997955747657055e-13, 2.8055046025917746e-14], [8.658700472099519e-05, 9.717377175662951e-05, 5.452747758070847e-05, 2.039813664096605e-05, 5.723040889902587e-06, 1.2845564319524377e-06, 2.402692989347808e-07, 3.852091412900057e-08, 5.403845717798268e-09, 6.738399808010843e-10, 7.56228636223733e-11, 7.71537034066287e-12, 7.215590442981449e-13, 6.229093731123434e-14, 4.993363400607271e-15], [1.3484751814335959e-05, 1.5133497217317961e-05, 8.491915208372282e-06, 3.1767331710418152e-06, 8.912860107854044e-07, 2.0005224493217078e-07, 3.7418685115393556e-08, 5.999110009229451e-09, 8.415756912053425e-10, 1.049414393413734e-10, 1.177723551845897e-11, 1.201564305576451e-12, 1.1237303638233643e-13, 9.700968784299348e-15, 7.77648636685671e-16], [1.8667264301141451e-06, 2.0949661977162205e-06, 1.1755561229465183e-06, 4.397627671203897e-07, 1.2338285316866595e-07, 2.769371050800771e-08, 5.179958033099597e-09, 8.304711399645732e-10, 1.1650133479241601e-10, 1.4527294319536487e-11, 1.6303508673117574e-12, 1.6633541926346265e-13, 1.5556068063787034e-14, 1.3429282998083597e-15, 1.0765175981215193e-16], [2.3257386206128382e-07, 2.610100610515872e-07, 1.4646153993048854e-07, 5.478967002877439e-08, 1.5372164989286777e-08, 3.450335894832041e-09, 6.453665762902812e-10, 1.0346769469599646e-10, 1.4514802453571097e-11, 1.8099432732566784e-12, 2.0312403124997458e-13, 2.0723588754952634e-14, 1.9381173211662947e-15, 1.673142974349625e-16, 1.3412241415403827e-17], [2.6341981946922615e-08, 2.9562747314977136e-08, 1.6588653628458033e-08, 6.20563500121745e-09, 1.7410954483191544e-09, 3.9079492874627206e-10, 7.309606742182505e-11, 1.1719047538770508e-11, 1.643988111159147e-12, 2.0499936066125227e-13, 2.3006409734740766e-14, 2.3472130359797893e-15, 2.195167205493098e-16, 1.895049668708027e-17, 1.5191088891117037e-18], [2.734937650259498e-09, 3.069331337321198e-09, 1.7223052337898937e-09, 6.442956662408803e-10, 1.8076800386159965e-10, 4.0574007161352534e-11, 7.589147516715642e-12, 1.2167218246350931e-12, 1.7068590324174198e-13, 2.1283913673666587e-14, 2.388624223781683e-15, 2.4369773383854965e-16, 2.2791168299389763e-17, 1.9675219193849815e-18, 1.577204063098542e-19], [2.6211043178890193e-10, 2.941579900558733e-10, 1.650619598066967e-10, 6.174788491506999e-11, 1.7324409403368345e-11, 3.8885239433005155e-12, 7.273272691709334e-13, 1.166079536737612e-13, 1.635816297118394e-14, 2.0398036505999097e-15, 2.289205118140237e-16, 2.335545683695512e-17, 2.1842556313339625e-18, 1.885629896517732e-19, 1.5115578154359193e-20], [2.3325797359287255e-11, 2.6177781711429997e-11, 1.46892353726642e-11, 5.495083278690389e-12, 1.5417381916251188e-12, 3.4604849913495474e-13, 6.472649096327691e-14, 1.0377204292524755e-14, 1.4557497465165325e-15, 1.815267186502055e-16, 2.037215166719791e-17, 2.0784546791756576e-18, 1.9438182559025997e-19, 1.6780644921530643e-20, 1.3451693264959959e-21]] |
| Legacy trial inputs | {"lambda_home": 1.245891515271806, "lambda_away": 1.1222673895435868, "rho": -0.06159715442825365, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3830 |
| Legacy p draw | 0.2943 |
| Legacy p away | 0.3227 |
| Legacy p over 1 5 | 0.6926 |
| Legacy p under 3 5 | 0.7854 |
| Legacy p btts yes | 0.4885 |
| Legacy p over 2 5 | 0.4220 |
| Legacy goal margin distribution | {"-1": 0.18978171232298985, "-10": 9.281904222004795e-08, "-11": 9.371365949595084e-09, "-12": 8.685750266755614e-10, "-13": 7.410310158930515e-11, "-14": 5.4008499628472845e-12, "-2": 0.09174425555423468, "-3": 0.030941328193390412, "-4": 0.00813682530303434, "-5": 0.0017474574485687165, "-6": 0.00031656564342114274, "-7": 4.953934420467223e-05, "-8": 6.8191240759832145e-06, "-9": 8.374708985649597e-07, "0": 0.2942752878869004, "1": 0.2115757626577677, "10": 2.639222042331575e-07, "11": 2.95818703273292e-08, "12": 3.0437848756880355e-09, "13": 2.8828821350033194e-10, "14": 2.3325797359287255e-11, "2": 0.11306980687721718, "3": 0.04233412681895839, "4": 0.012359204850915512, "5": 0.002946632894557955, "6": 0.0005926074237463678, "7": 0.00010295263013844839, "8": 1.573256990823818e-05, "9": 2.144987110918334e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3830 |
| Legacy raw p draw | 0.2943 |
| Legacy raw p away | 0.3227 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.2459 |
| Legacy lambda away | 1.1223 |
| Legacy model home team | Lille |
| Legacy model away team | Lens |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 90/100 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 8.924167775994395, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,569.6537 |
| Elo away rating | 1,580.6843 |
| Elo rating diff | 48.9694 |
| Elo home expectancy | 0.5700 |

</details>


---
