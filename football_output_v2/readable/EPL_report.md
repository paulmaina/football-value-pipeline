# Premier League — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,980 |
| Training data through | 2026-10-25 |
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
| Training sha256 | bbff5504c9b6ad4698c983f48234324fa4a7f11bd2e959dc15c9c793366d40fe |
| Training as of utc | 2026-10-26T10:32:17.000888+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 80, 'bbs_added_results': 10, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 80, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 119, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-26T10:32:17.000888+00:00', 'observations': 348, 'observations_sha256': '7ca0f5f7384002c4ccd320aa6b69d6a2a66bfbbae3f82d69733caa599b57c0b1', 'eligible_training_matches': 179, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 166, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 18, 'retrospective_eligible_training_matches': 179, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '225649214bca033d026dcd3cf885df7a03af2e521b4933744f23380d822ec47a', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 118, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-21T00:00:00+00:00', 'audit_origin_utc': '2025-10-19T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 31, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1969, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1609, 'tuning_matches': 248, 'audit_matches': 105, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9094261757751134, 'audit_candidate_poisson_score': 0.8955631912992509, 'audit_gain': 0.013862984475862539, 'audit_gain_lower95': 0.003252758122502132, 'audit_baseline_briers': [0.625786200280283, 0.15863361164873582, 0.2306533668033659, 0.2523682911503458], 'audit_candidate_briers': [0.6238183660512071, 0.15613922359773086, 0.22796688126399844, 0.24779469717444716], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1877.963 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.175 |
| Dixon-Coles low-score adjustment | -0.076 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1980, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261026T103217000888Z_9e17d30be9d92859b980fe5dd93cf7e4879ab9d90c5a6b5253428f627895846a.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE': 6} |
| Shot features applied fixtures | 6 |
| Goal rate features used | {'shot_features': 6} |
| Legacy comparison status | {'AVAILABLE': 6} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **50.8%**. Expected goals are 1.89 for Chelsea and 1.29 for Tottenham Hotspur (3.18 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.6%; Double Chance 1X: 74.8%; Double Chance X2: 49.2%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 78.4%; BTTS Yes (both teams score): 62.3%; BTTS No (at least one team does not score): 37.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 50.8% | 1.97 |
| Draw | 23.9% | 4.18 |
| Tottenham Hotspur win | 25.2% | 3.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.89 |
| Tottenham Hotspur expected goals | 1.29 |
| Expected total goals | 3.18 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.4% |
| Under 3.5 | 60.6% |
| Over 4.5 | 21.6% |
| Under 4.5 | 78.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.89% |
| 2 | 2-1 | 9.59% |
| 3 | 2-0 | 7.44% |
| 4 | 1-0 | 7.09% |
| 5 | 1-2 | 6.52% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0382a9faef0bb8df1bcc436536cffb05 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9634 |
| Dc lambda away | 1.3074 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:32:17.000888+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7336 |
| Shot lambda away | 1.2448 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 62.3% |
| P btts no | 37.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.35 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.03 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.62 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.14360933319987068, "-10": 1.797497144803111e-07, "-11": 2.0680859524624967e-08, "-12": 2.187069805725577e-09, "-13": 2.1395399763649746e-10, "-14": 1.9459732794795668e-11, "-15": 1.639639777427851e-12, "-16": 1.1457489360803415e-13, "-2": 0.07252367048379665, "-3": 0.02633931889427498, "-4": 0.007621721089684497, "-5": 0.0018237618679467188, "-6": 0.00037100399746353393, "-7": 6.553316974556659e-05, "-8": 1.0218571122872662e-05, "-9": 1.4252819413414586e-06, "0": 0.2393554217136307, "1": 0.21472869767779343, "10": 8.475899735637618e-06, "11": 1.4336328581637324e-06, "12": 2.2288650105046277e-07, "13": 3.205481593096391e-08, "14": 4.286092254337441e-09, "15": 5.309148192805203e-10, "16": 5.4540312870478366e-11, "2": 0.1567412465219722, "3": 0.08368735094287771, "4": 0.03560082749245554, "5": 0.01252353493966285, "6": 0.003745321898811405, "7": 0.0009725758819350464, "8": 0.0002229483451877486, "9": 4.5715831556578816e-05} |
| Raw goal margin distribution | {"-1": 0.14360933319987068, "-10": 1.797497144803111e-07, "-11": 2.0680859524624967e-08, "-12": 2.187069805725577e-09, "-13": 2.1395399763649746e-10, "-14": 1.9459732794795668e-11, "-15": 1.639639777427851e-12, "-16": 1.1457489360803415e-13, "-2": 0.07252367048379665, "-3": 0.02633931889427498, "-4": 0.007621721089684497, "-5": 0.0018237618679467188, "-6": 0.00037100399746353393, "-7": 6.553316974556659e-05, "-8": 1.0218571122872662e-05, "-9": 1.4252819413414586e-06, "0": 0.2393554217136307, "1": 0.21472869767779343, "10": 8.475899735637618e-06, "11": 1.4336328581637324e-06, "12": 2.2288650105046277e-07, "13": 3.205481593096391e-08, "14": 4.286092254337441e-09, "15": 5.309148192805203e-10, "16": 5.4540312870478366e-11, "2": 0.1567412465219722, "3": 0.08368735094287771, "4": 0.03560082749245554, "5": 0.01252353493966285, "6": 0.003745321898811405, "7": 0.0009725758819350464, "8": 0.0002229483451877486, "9": 4.5715831556578816e-05} |
| Unadjusted home-win probability | 50.8% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 25.2% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 60.6% |
| Raw p btts yes | 62.3% |
| P home draw | 74.8% |
| P draw away | 49.2% |
| P home away | 76.1% |
| Raw p home draw | 74.8% |
| Raw p draw away | 49.2% |
| Raw p home away | 76.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6166 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.04939070633130037, 0.03892866250465719, 0.03044322205493623, 0.01262070837798551, 0.003924082337803828, 0.0009760734014406766, 0.00020232315969809984, 3.5946940251891074e-05, 5.588384943058589e-06, 7.722504595932072e-07, 9.604451027920167e-08, 1.0859109997258492e-08, 1.125452984843015e-09, 1.0767090812685205e-10, 9.564994207974362e-12, 7.930632461841608e-13, 6.164561813624148e-14, 4.509907779883023e-15], [0.06835384677294412, 0.10750981222150402, 0.060619278565109576, 0.02513065914880929, 0.007813727466774046, 0.0019435809164730787, 0.00040287075907340114, 7.157841508236175e-05, 1.112772698569873e-05, 1.5377237549835485e-06, 1.9124614709829706e-07, 2.1622921933332058e-08, 2.2410291485250503e-09, 2.1439691111938828e-10, 1.904604733758271e-11, 1.5791666780025535e-12, 1.227502427757403e-13, 8.98023722713527e-15], [0.0780372882417429, 0.09705469306736599, 0.06035328532445071, 0.025020387538438577, 0.007779441366053132, 0.001935052616587422, 0.0004011029897876361, 7.126433390159458e-05, 1.1078899282166858e-05, 1.5309763285128278e-06, 1.9040697210917934e-07, 2.1528042033509705e-08, 2.231195666178557e-09, 2.1345615216405619e-10, 1.8962474586916855e-11, 1.5722374028253302e-12, 1.22211623121392e-13, 8.94083256151614e-15], [0.05179657731207993, 0.06441921581630468, 0.04005897282927051, 0.01660706652822552, 0.005163537140261914, 0.0012843744921981987, 0.0002662286515682454, 4.7301087258351694e-05, 7.353523887501579e-06, 1.0161723395247478e-06, 1.2638098624160863e-07, 1.4289052306791017e-08, 1.4809368883192011e-09, 1.4167968079637234e-10, 1.2586179031836301e-11, 1.0435590218885233e-12, 8.111691126212021e-14, 5.934400533913136e-15], [0.025784648739990153, 0.03206827435568125, 0.01994159840068538, 0.008267097929115034, 0.002570439946550213, 0.0006393693724664358, 0.00013253022924368944, 2.35467666642865e-05, 3.6606285642764843e-06, 5.058567224639555e-07, 6.291321756685686e-08, 7.113176462183452e-09, 7.372193193641593e-10, 7.052900003252539e-11, 6.2654758703301774e-12, 5.194899782030165e-13, 4.0380487906851085e-14, 2.954180395500263e-15], [0.010268602987242102, 0.01277102438606164, 0.007941638413327418, 0.0032923289879482785, 0.0010236644128773975, 0.0002546255453880757, 5.27794782715411e-05, 9.377378026243279e-06, 1.4578263907863355e-06, 2.014548231310076e-07, 2.5054863471616385e-08, 2.83278573250733e-09, 2.93593780602275e-10, 2.8087809445236022e-11, 2.4951933566107736e-12, 2.068841967098237e-13, 1.6081320437128554e-14, 1.1764870617391098e-15], [0.0034078483536491826, 0.004238328668712373, 0.0026355970160458664, 0.0010926274913141203, 0.00033972421452535106, 8.450275531402436e-05, 1.7515961845793534e-05, 3.112076911336697e-06, 4.838098494916923e-07, 6.685695105698854e-08, 8.314974815827873e-09, 9.401185542726633e-10, 9.743517040342978e-11, 9.321520687330356e-12, 8.280815397115832e-13, 6.865880101018107e-14, 5.33691890165209e-15, 3.904415723753663e-16], [0.0009693985567377296, 0.0012056374779794196, 0.000749723484837948, 0.0003108094619285726, 9.663815084291642e-05, 2.403770371825928e-05, 4.98260085869225e-06, 8.852632374548351e-07, 1.376248357209107e-07, 1.9018167810527408e-08, 2.3652826503100587e-09, 2.674266795640693e-10, 2.771646615772592e-11, 2.6516052837922626e-12, 2.3555656418748116e-13, 1.9530723113116616e-14, 1.5181431049148252e-15, 1.1106524043119247e-16], [0.00024128622557369558, 0.00030008680583433917, 0.0001866084373895433, 7.736141282664001e-05, 2.4053527314686607e-05, 5.983056980356891e-06, 1.2401843868840948e-06, 2.203446907569693e-07, 3.425523684298468e-08, 4.733679348328983e-09, 5.887259880279218e-10, 6.65633074046117e-11, 6.8987120508454446e-12, 6.599925553743107e-13, 5.863073953109091e-14, 4.861255909589527e-15, 3.7787039924873063e-16, 2.7644473441616405e-17], [5.3383884033114894e-05, 6.639334344278734e-05, 4.12865805228551e-05, 1.7115990277339332e-05, 5.321773796666234e-06, 1.3237341636202834e-06, 2.7438723172732085e-07, 4.87506296338077e-08, 7.57887271353685e-09, 1.0473129528231729e-09, 1.3025393305165873e-10, 1.472694048282113e-11, 1.526320216682665e-12, 1.4602145628101854e-13, 1.2971882636323772e-14, 1.075538900390148e-15, 8.360273996196235e-17, 6.116260308083909e-18], [1.0629927841577393e-05, 1.322040280021781e-05, 8.221083567302524e-06, 3.408177296960931e-06, 1.0596844435797907e-06, 2.635851417627428e-07, 5.463664787114981e-08, 9.707343042281875e-09, 1.5091234278761381e-09, 2.0854348306979278e-10, 2.593647754370778e-11, 2.9324639354170135e-12, 3.0392456563132557e-13, 2.9076144827274494e-14, 2.5829925808320145e-15, 2.141639018784162e-16, 1.6647179373508097e-17, 1.2178845153886844e-18], [1.924233535741874e-06, 2.3931622870188676e-06, 1.4881836392590697e-06, 6.169495360932895e-07, 1.918244765185178e-07, 4.7714281494866817e-08, 9.89034654618929e-09, 1.7572268883941452e-09, 2.7318209048746305e-10, 3.775061973739283e-11, 4.695030919533753e-12, 5.308357244733351e-13, 5.5016539175001225e-14, 5.263374672017228e-15, 4.675742884320339e-16, 3.876803006393957e-17, 3.0134786711083865e-18, 2.204619130155725e-19], [3.192983551395287e-07, 3.971102091474938e-07, 2.4694226523693684e-07, 1.0237373396713732e-07, 3.1830460643255384e-08, 7.917485749515142e-09, 1.641158063873274e-09, 2.91586049535761e-10, 4.533056436551256e-11, 6.264162100781668e-12, 7.790715742610644e-13, 8.808440894794425e-14, 9.129188395146966e-15, 8.733798907678942e-16, 7.758710074883093e-17, 6.432986434072949e-18, 5.00042622197618e-19, 3.658242354124994e-20], [4.890727628242657e-08, 6.082580257847471e-08, 3.782441530734958e-08, 1.568069615957312e-08, 4.875506271231255e-09, 1.2127299022398713e-09, 2.51377965345008e-10, 4.466255229694208e-11, 6.943331839256264e-12, 9.594885210321816e-13, 1.1933124024243959e-13, 1.3491984707246106e-14, 1.3983277141552087e-15, 1.3377654763876025e-16, 1.1884100594935317e-17, 9.85347527752918e-19, 7.659207222073274e-20, 5.603369595909211e-21], [6.956096357895363e-09, 8.651271874942315e-09, 5.379777766391731e-09, 2.230270048468512e-09, 6.934446976838482e-10, 1.724869323608756e-10, 3.5753562293958076e-11, 6.3523680111113204e-12, 9.875521392726604e-13, 1.3646833587812338e-13, 1.6972517562419146e-14, 1.918968971833286e-15, 1.9888456399430034e-16, 1.9027077902029202e-17, 1.6902791394047773e-18, 1.4014627004542725e-19, 1.089371306514032e-20, 7.969689134385745e-22], [9.234097978286107e-10, 1.1484414248996806e-09, 7.14156222690636e-10, 2.9606450350877866e-10, 9.205358798211124e-11, 2.2897342869417062e-11, 4.746223748330241e-12, 8.43265900739766e-13, 1.3109584375379306e-13, 1.811593628949561e-14, 2.253072442443553e-15, 2.547398223299032e-16, 2.6401582954031137e-17, 2.5258117850595633e-18, 2.2438164138139186e-19, 1.860417570872133e-20, 1.4461216264876006e-21, 1.057962491273862e-22], [1.1491974236357086e-10, 1.42925267827426e-10, 8.887781926500797e-11, 3.684567409424685e-11, 1.1456207893204526e-11, 2.849608862231444e-12, 5.90674705467234e-13, 1.0494571346857746e-13, 1.6315075521775073e-14, 2.2545556002970914e-15, 2.803982643685699e-16, 3.170275518056372e-17, 3.2857168271359827e-18, 3.1434108700218787e-19, 2.7924633764229006e-20, 2.3153177325606845e-21, 1.7997201798500778e-22, 1.3166502804433074e-23], [1.3460644989232815e-11, 1.6740955475948393e-11, 1.0410332880477366e-11, 4.31576444717865e-12, 1.3418751574068642e-12, 3.3377705574136686e-13, 6.918621945096257e-14, 1.2292378690452675e-14, 1.910998363330413e-15, 2.640779723302439e-16, 3.284328188207652e-17, 3.713370078015461e-18, 3.8485874433395857e-19, 3.681903292368746e-20, 3.2708355746695824e-21, 2.71195091411502e-22, 2.108027212963844e-23, 1.5422034226243882e-24]] |
| Legacy trial inputs | {"lambda_home": 1.991224137041711, "lambda_away": 1.2436963822565341, "rho": -0.10286337681625446, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5373 |
| Legacy p draw | 0.2367 |
| Legacy p away | 0.2260 |
| Legacy p over 1 5 | 0.8433 |
| Legacy p under 3 5 | 0.5948 |
| Legacy p btts yes | 0.6245 |
| Legacy p over 2 5 | 0.6273 |
| Legacy goal margin distribution | {"-1": 0.13042726916787395, "-10": 1.2004678536755984e-07, "-11": 1.3326717438719646e-08, "-12": 1.3598974865461773e-09, "-13": 1.2837326395891768e-10, "-14": 1.127230690963222e-11, "-15": 9.247543215214173e-13, "-16": 7.062585536337675e-14, "-17": 4.509907779883023e-15, "-2": 0.06478010810104629, "-3": 0.022660790996323184, "-4": 0.006319938004159154, "-5": 0.0014580938983973116, "-6": 0.0002860624925519514, "-7": 4.8739440884610364e-05, "-8": 7.331570877583167e-06, "-9": 9.865786800113108e-07, "0": 0.23670437245152853, "1": 0.21484798850463727, "10": 1.3286430035000408e-05, "11": 2.36149340262825e-06, "12": 3.858117899728529e-07, "13": 5.8310891929311174e-08, "14": 8.19773136650723e-09, "15": 1.076745398536514e-09, "16": 1.3166069783951925e-10, "17": 1.3460644989232815e-11, "2": 0.16605548384760818, "3": 0.09300202315436827, "4": 0.04152751330568658, "5": 0.015339612101572172, "6": 0.004818319344847127, "7": 0.0013143801202178695, "8": 0.00031655068192383155, "9": 6.819989705284297e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.5373 |
| Legacy raw p draw | 0.2367 |
| Legacy raw p away | 0.2260 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.9912 |
| Legacy lambda away | 1.2437 |
| Legacy model home team | Chelsea |
| Legacy model away team | Tottenham |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 9.912800468011419, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,487.0848 |
| Elo away rating | 1,464.5626 |
| Elo rating diff | 82.5222 |
| Elo home expectancy | 0.6166 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **38.8%**. Expected goals are 1.40 for Crystal Palace and 1.49 for Newcastle United (2.89 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 55.1%; Under 3.5 goals: 67.3%; Double Chance 1X: 61.2%; Double Chance X2: 65.4%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.6% | 2.89 |
| Draw | 26.6% | 3.76 |
| Newcastle United win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.40 |
| Newcastle United expected goals | 1.49 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.48% |
| 2 | 1-2 | 8.64% |
| 3 | 2-1 | 8.11% |
| 4 | 0-1 | 7.43% |
| 5 | 1-0 | 6.91% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | fe235b26408c477368c40672a4488694 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3546 |
| Dc lambda away | 1.5518 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:32:17.000888+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4959 |
| Shot lambda away | 1.3446 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.49 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.05 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 6.02 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.1964656451683088, "-10": 9.977215725617826e-07, "-11": 1.3304558083613968e-07, "-12": 1.6300883453669544e-08, "-13": 1.8462971963650167e-09, "-14": 1.9302743237280774e-10, "-15": 1.6834294669348166e-11, "-2": 0.11764828061853243, "-3": 0.05044821306958747, "-4": 0.017117296544152633, "-5": 0.004783166445463092, "-6": 0.001133358317306163, "-7": 0.0002327772349719936, "-8": 4.215378257940555e-05, "-9": 6.822374874177048e-06, "0": 0.2657077943835348, "1": 0.18369223146980282, "10": 5.247741129252203e-07, "11": 6.562356179617819e-08, "12": 7.539920922785341e-09, "13": 8.008543944992633e-10, "14": 7.851764959737402e-11, "15": 6.421544341737764e-12, "2": 0.10346136231851222, "3": 0.041603962844749216, "4": 0.0132379394651272, "5": 0.003468941804390203, "6": 0.0007708059536763108, "7": 0.0001484617698490885, "8": 2.5211981726980247e-05, "9": 3.826505269969152e-06} |
| Raw goal margin distribution | {"-1": 0.1964656451683088, "-10": 9.977215725617826e-07, "-11": 1.3304558083613968e-07, "-12": 1.6300883453669544e-08, "-13": 1.8462971963650167e-09, "-14": 1.9302743237280774e-10, "-15": 1.6834294669348166e-11, "-2": 0.11764828061853243, "-3": 0.05044821306958747, "-4": 0.017117296544152633, "-5": 0.004783166445463092, "-6": 0.001133358317306163, "-7": 0.0002327772349719936, "-8": 4.215378257940555e-05, "-9": 6.822374874177048e-06, "0": 0.2657077943835348, "1": 0.18369223146980282, "10": 5.247741129252203e-07, "11": 6.562356179617819e-08, "12": 7.539920922785341e-09, "13": 8.008543944992633e-10, "14": 7.851764959737402e-11, "15": 6.421544341737764e-12, "2": 0.10346136231851222, "3": 0.041603962844749216, "4": 0.0132379394651272, "5": 0.003468941804390203, "6": 0.0007708059536763108, "7": 0.0001484617698490885, "8": 2.5211981726980247e-05, "9": 3.826505269969152e-06} |
| Unadjusted home-win probability | 34.6% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 38.8% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 67.3% |
| Raw p btts yes | 59.2% |
| P home draw | 61.2% |
| P draw away | 65.4% |
| P home away | 73.4% |
| Raw p home draw | 61.2% |
| Raw p draw away | 65.4% |
| Raw p home away | 73.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5509 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.05932998542955979, 0.0666450758010227, 0.06332388257451642, 0.034285314657067516, 0.013922268581891804, 0.004522742507223886, 0.001224369413787872, 0.0002841033084982403, 5.768304309701323e-05, 1.0410402324015466e-05, 1.690944576710971e-06, 2.496885040833566e-07, 3.3797078529876316e-08, 4.222772337931651e-09, 4.899271325839742e-10, 5.305204045222629e-11], [0.056464091202115284, 0.12143734388020058, 0.0894257123191274, 0.048417572654136876, 0.019660967306747452, 0.006386997352358426, 0.0017290491757338206, 0.0004012094600292274, 8.145974327482594e-05, 1.4701525009277142e-05, 2.387944597152628e-06, 3.5260902250073425e-07, 4.772808771292805e-08, 5.963380780334734e-09, 6.918729716901608e-10, 7.491986142575413e-11], [0.04786670826875088, 0.07774910923983458, 0.0631433015369273, 0.03418754305110894, 0.013882566377859161, 0.004509844979442929, 0.0012208778733114327, 0.0002832931296503034, 5.7518548070014544e-05, 1.0380714926828808e-05, 1.6861225014724725e-06, 2.4897646610797837e-07, 3.370069922936163e-08, 4.210730236606151e-09, 4.885300048914173e-10, 5.290075167899276e-11], [0.022532385935473943, 0.03659898494994197, 0.029723565520357424, 0.016093166672087923, 0.006534966675470543, 0.002122927839855394, 0.0005747061458055792, 0.00013335510965804438, 2.7075814703719104e-05, 4.886533531910774e-06, 7.937116278051499e-07, 1.1720116185340138e-07, 1.5863993760921335e-08, 1.982124992357559e-09, 2.299666513408161e-10, 2.490207069212453e-11], [0.00795503442227394, 0.01292123195168192, 0.01049387257720005, 0.0056816750434892805, 0.00230716289880057, 0.0007494973719345758, 0.00020289938161311747, 4.7080876865583714e-05, 9.559087022386645e-06, 1.7251853648905832e-06, 2.802190295617374e-07, 4.1377743109151864e-08, 5.600765795697959e-09, 6.997870793003613e-10, 8.11894768991663e-11, 8.791649056120382e-12], [0.0022468130216049304, 0.0036494615438656987, 0.002963880267758323, 0.0016047273706944463, 0.0006516330877807974, 0.00021168738757511424, 5.730672533703861e-05, 1.3297482021446002e-05, 2.699860246539787e-06, 4.872598579416851e-07, 7.914481963245081e-08, 1.168669387048249e-08, 1.5818754329332724e-09, 1.9764725564487195e-10, 2.2931085427308006e-11, 2.483105733064262e-12], [0.0005288232673469757, 0.0008589589605928258, 0.0006975964764978939, 0.0003776981721271935, 0.00015337223670952742, 4.982400176479904e-05, 1.3488051494396761e-05, 3.1297744059920364e-06, 6.354551550246582e-07, 1.1468437633483393e-07, 1.8627995168784928e-08, 2.7506497325967177e-09, 3.7231960422863227e-10, 4.651943286211851e-11, 5.397196563699599e-12, 5.844385243900123e-13], [0.00010668598921421957, 0.0001732883026592259, 0.0001407346740639919, 7.61976743571562e-05, 3.0941658209258345e-05, 1.0051605598890838e-05, 2.721109688443213e-06, 6.314076916391118e-07, 1.2819814482670875e-07, 2.313668269189397e-08, 3.758053426109124e-09, 5.549222317242801e-10, 7.511259003457599e-11, 9.384934474381293e-12, 1.0888425111674907e-12, 1.1790593561106825e-13], [1.8832686405333666e-05, 3.0589623677208946e-05, 2.4843112038658833e-05, 1.3450753154686908e-05, 5.4619594401090655e-06, 1.7743542287816804e-06, 4.803424124799318e-07, 1.1145890044360309e-07, 2.2630108011832206e-08, 4.084190368439447e-09, 6.633883435836371e-10, 9.795734609937287e-11, 1.3259209232931027e-11, 1.6566704699689907e-12, 1.9220733395871504e-13, 2.0813281360049065e-14], [2.9550486732463853e-06, 4.799837097953364e-06, 3.8981483410863075e-06, 2.1105661406152404e-06, 8.570394923715557e-07, 2.7841503844854786e-07, 7.537083017008067e-08, 1.7489086197712577e-08, 3.5509044868313537e-09, 6.408528804538772e-10, 1.0409268239069433e-10, 1.5370548810482367e-11, 2.080510863334522e-12, 2.599492058075076e-13, 3.0159373706879426e-14, 3.265825073766316e-15], [4.1731069195225846e-07, 6.778309131553283e-07, 5.50494817997078e-07, 2.9805323496873504e-07, 1.2103074539177515e-07, 3.931765097365991e-08, 1.0643835946275135e-08, 2.469801167356814e-09, 5.014571915081344e-10, 9.05009658226727e-11, 1.4699923459435172e-11, 2.170622236398456e-12, 2.93808841746929e-13, 3.67099140972174e-14, 4.259093673958996e-15, 4.611984004416512e-16], [5.35749408351786e-08, 8.702089778400957e-08, 7.067330857566408e-08, 3.826449869875457e-08, 1.553809942723378e-08, 5.0476560158037235e-09, 1.3664708143789302e-09, 3.170765905775884e-10, 6.437778826308295e-11, 1.1618642855263586e-11, 1.8871971047197393e-12, 2.786675734248246e-13, 3.771959745341216e-14, 4.7128710424891546e-15, 5.467885103215644e-16, 5.920930734208751e-17], [6.30485825655007e-09, 1.024087786814041e-08, 8.317044986793612e-09, 4.503079924918557e-09, 1.8285697181874304e-09, 5.940231610403913e-10, 1.6081034644306344e-10, 3.7314515497312164e-11, 7.576169446787549e-12, 1.3673164205869699e-12, 2.2209096383391218e-13, 3.279442821123222e-14, 4.438954326977706e-15, 5.54624670435148e-16, 6.434769689234946e-17, 6.967927251825339e-18], [6.848994987726563e-10, 1.112471023689485e-09, 9.034842197771369e-10, 4.891715337622099e-10, 1.9863832500220506e-10, 6.452899473723197e-11, 1.7468897982264526e-11, 4.053492072482829e-12, 8.230025871447278e-13, 1.4853217836431805e-13, 2.4125838142952172e-14, 3.562473021669339e-15, 4.822055421251167e-16, 6.024911954100581e-17, 6.990118342939622e-18, 7.56928972558831e-19], [6.908657868389612e-11, 1.1221619675500697e-10, 9.11354640369079e-11, 4.934327987937825e-11, 2.0036870072900176e-11, 6.509111892030015e-12, 1.762107283090999e-12, 4.0888028026297393e-13, 8.301719171311255e-14, 1.4982607004452126e-14, 2.4336002846620144e-15, 3.5935063927169264e-16, 4.864061250962574e-17, 6.077396092805169e-18, 7.051010575634015e-19, 7.635227228887859e-20], [6.504251118029346e-12, 1.0564748423052084e-11, 8.58007380227028e-12, 4.645491055377611e-12, 1.8863987341125647e-12, 6.128093054777794e-13, 1.658960174967219e-13, 3.8494597224287116e-14, 7.815767871300494e-15, 1.4105581752077344e-15, 2.2911465112165237e-16, 3.383156094531407e-17, 4.579337467917057e-18, 5.721648268645452e-19, 6.638271035195217e-20, 7.188289851076082e-21]] |
| Legacy trial inputs | {"lambda_home": 1.412195662732708, "lambda_away": 1.624283600269878, "rho": -0.10286337681625446, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3224 |
| Legacy p draw | 0.2625 |
| Legacy p away | 0.4150 |
| Legacy p over 1 5 | 0.8176 |
| Legacy p under 3 5 | 0.6391 |
| Legacy p btts yes | 0.6187 |
| Legacy p over 2 5 | 0.5849 |
| Legacy goal margin distribution | {"-1": 0.19760336410704396, "-10": 2.0793200960160566e-06, "-11": 3.018660803332878e-07, "-12": 4.027389138579459e-08, "-13": 4.9675460613008045e-09, "-14": 5.648469940097283e-10, "-15": 5.305204045222629e-11, "-2": 0.12796380558089762, "-3": 0.05908073236868048, "-4": 0.021673564460540914, "-5": 0.006563967784945866, "-6": 0.0016882762430424688, "-7": 0.000376780485575331, "-8": 7.419369569777009e-05, "-9": 1.3063910683640247e-05, "0": 0.2625367905502813, "1": 0.17032273430725697, "10": 5.131584559362022e-07, "11": 6.477053260170964e-08, "12": 7.51311023533184e-09, "13": 8.056957693299336e-10, "14": 7.96513271069482e-11, "15": 6.504251118029346e-12, "2": 0.09672821535369598, "3": 0.03882799024588035, "4": 0.012384041460112953, "5": 0.0032608551711833245, "6": 0.0007291914915351494, "7": 0.00014148796447566587, "8": 2.4223177719297667e-05, "9": 3.708261288235208e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3224 |
| Legacy raw p draw | 0.2625 |
| Legacy raw p away | 0.4150 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.4122 |
| Legacy lambda away | 1.6243 |
| Legacy model home team | Crystal Palace |
| Legacy model away team | Newcastle |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 9.512402246102315, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,406.2585 |
| Elo away rating | 1,456.9899 |
| Elo rating diff | 9.2687 |
| Elo home expectancy | 0.5133 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Hull City win** at **39.8%**. Expected goals are 1.31 for Hull City and 1.12 for Brentford (2.43 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 43.8%; Under 3.5 goals: 77.2%; Double Chance 1X: 69.0%; Double Chance X2: 60.2%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 39.8% | 2.52 |
| Draw | 29.3% | 3.42 |
| Brentford win | 31.0% | 3.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.31 |
| Brentford expected goals | 1.12 |
| Expected total goals | 2.43 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 43.8% |
| Under 2.5 | 56.2% |
| Over 3.5 | 22.8% |
| Under 3.5 | 77.2% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.90% |
| 2 | 1-0 | 10.51% |
| 3 | 0-0 | 9.77% |
| 4 | 0-1 | 8.91% |
| 5 | 2-1 | 8.44% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 69493b5ebb84f24ab1d6023a30ee89f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2137 |
| Dc lambda away | 1.0432 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:32:17.000888+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5235 |
| Shot lambda away | 1.3139 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.23 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.39 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 10.02 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.18186862109633675, "-10": 8.943205622096115e-08, "-11": 9.04217801881677e-09, "-12": 8.392978502917287e-10, "-13": 7.168713305726047e-11, "-14": 5.210862088366512e-12, "-2": 0.08834408789779775, "-3": 0.02971309368294274, "-4": 0.007805212220436552, "-5": 0.0016759326130479516, "-6": 0.00030372353518700744, "-7": 4.756520049524845e-05, "-8": 6.553929530335832e-06, "-9": 8.058522428230058e-07, "0": 0.2926960256151584, "1": 0.2129260922668222, "10": 4.015280049238162e-07, "11": 4.717565516197686e-08, "12": 5.088423626491729e-09, "13": 5.050456378867319e-10, "14": 4.26600395616531e-11, "2": 0.11929493811377666, "3": 0.04662455069399766, "4": 0.014232256616476733, "5": 0.0035511405755861056, "6": 0.0007478457347610288, "7": 0.00013609593983509495, "8": 2.1791135802189327e-05, "9": 3.113549547408081e-06} |
| Raw goal margin distribution | {"-1": 0.18186862109633675, "-10": 8.943205622096115e-08, "-11": 9.04217801881677e-09, "-12": 8.392978502917287e-10, "-13": 7.168713305726047e-11, "-14": 5.210862088366512e-12, "-2": 0.08834408789779775, "-3": 0.02971309368294274, "-4": 0.007805212220436552, "-5": 0.0016759326130479516, "-6": 0.00030372353518700744, "-7": 4.756520049524845e-05, "-8": 6.553929530335832e-06, "-9": 8.058522428230058e-07, "0": 0.2926960256151584, "1": 0.2129260922668222, "10": 4.015280049238162e-07, "11": 4.717565516197686e-08, "12": 5.088423626491729e-09, "13": 5.050456378867319e-10, "14": 4.26600395616531e-11, "2": 0.11929493811377666, "3": 0.04662455069399766, "4": 0.014232256616476733, "5": 0.0035511405755861056, "6": 0.0007478457347610288, "7": 0.00013609593983509495, "8": 2.1791135802189327e-05, "9": 3.113549547408081e-06} |
| Unadjusted home-win probability | 39.8% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 70.8% |
| Raw p under 3 5 | 77.2% |
| Raw p btts yes | 50.2% |
| P home draw | 69.0% |
| P draw away | 60.2% |
| P home away | 70.7% |
| Raw p home draw | 69.0% |
| Raw p draw away | 60.2% |
| Raw p home away | 70.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4384 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.11981849169351563, 0.10099159695248147, 0.06200131532416468, 0.022342276103836108, 0.006038306996676257, 0.0013055483234261597, 0.00023522824440402735, 3.6327807999493674e-05, 4.909044544024573e-06, 5.896607624918161e-07, 6.374556811082378e-08, 6.264769218706742e-09, 5.643799767769112e-10, 4.6932750983523355e-11], [0.10960915320157483, 0.14703229228109913, 0.07206241021048179, 0.025967808218464977, 0.007018156848709871, 0.0015174026283225495, 0.00027339926826887615, 4.222280428116715e-05, 5.7056464015877275e-06, 6.853463596626239e-07, 7.40897068761384e-08, 7.281367612156008e-09, 6.5596320317464e-10, 5.454863555713796e-11], [0.0716673145883743, 0.07747630458074539, 0.04187807095859954, 0.015090831850278605, 0.00407850458582224, 0.0008818175072975031, 0.00015888219562947424, 2.453719752910214e-05, 3.315757329965269e-06, 3.9827953849085343e-07, 4.3056206318914646e-08, 4.2314658730796175e-09, 3.812039243281113e-10, 3.1700183547626265e-11], [0.02776564440904277, 0.03001618709269493, 0.01622457369097178, 0.005846551854190208, 0.0015801109431964186, 0.00034163734865632484, 6.155479066173311e-05, 9.50630151695415e-06, 1.2846042788022529e-06, 1.5430308927646886e-07, 1.66810117153084e-08, 1.6393718312976553e-09, 1.4768758493349435e-10, 1.2281414884039184e-11], [0.008067809717832655, 0.008721745562651467, 0.004714343069562738, 0.0016988212904464855, 0.00045912978769626473, 9.926890515699375e-05, 1.7885856743096062e-05, 2.762227687903106e-06, 3.732649864490404e-07, 4.483555089940061e-08, 4.846969385526505e-09, 4.76349109598797e-10, 4.291329656810076e-11, 3.568587023966785e-12], [0.0018753983212997287, 0.002027408622546692, 0.0010958700549353188, 0.00039489857938140117, 0.00010672676515920476, 2.307549937341614e-05, 4.157647104252832e-06, 6.420921353029569e-07, 8.67671094720056e-08, 1.0422223606170154e-08, 1.1266996331006097e-09, 1.107294732695051e-10, 9.975387020763016e-12, 8.295339563309867e-13], [0.0003632872475660678, 0.0003927334741700385, 0.00021228323147458975, 7.649661212866752e-05, 2.0674260137679266e-05, 4.470002216793647e-06, 8.053863308399782e-07, 1.2438098182596688e-07, 1.6807834379153637e-08, 2.0189102679688954e-09, 2.1825529216595769e-10, 2.1449632918856554e-11, 1.9323526383812364e-12, 1.6069072065139763e-13], [6.031981400364068e-05, 6.520903299979482e-05, 3.5247273677863815e-05, 1.2701413128107986e-05, 3.432731356585544e-06, 7.421942391848455e-07, 1.3372545830557175e-07, 2.0652081072479975e-08, 2.7907542869920474e-09, 3.3521763472244385e-10, 3.623886804990754e-11, 3.5614733981998564e-12, 3.2084570134932407e-13, 2.6680910069766603e-14], [8.763505979316258e-06, 9.473831443920597e-06, 5.120866148756901e-06, 1.845312551647161e-06, 4.987210631486387e-07, 1.0782897395071382e-07, 1.9428174187953444e-08, 3.000417672923839e-09, 4.054520439897438e-10, 4.870177063352819e-11, 5.2649289803819635e-12, 5.174252264507389e-13, 4.6613758159848004e-14, 3.876310277015883e-15], [1.1317311208313219e-06, 1.2234635206390093e-06, 6.613156423739888e-07, 2.38306181029466e-07, 6.440551864876277e-08, 1.392518083919354e-08, 2.5089809262792568e-09, 3.874780326452334e-10, 5.2360630239869404e-11, 6.289413117950898e-12, 6.799201130378961e-13, 6.682099982125916e-14, 6.019764337802269e-15, 5.005919987789445e-16], [1.3153797117192627e-07, 1.4219977373203596e-07, 7.686288403754051e-08, 2.7697666869247237e-08, 7.485674909346764e-09, 1.618485170262189e-09, 2.916118985129705e-10, 4.503549769878593e-11, 6.0857309163475425e-12, 7.310010533152637e-13, 7.902523009378431e-14, 7.766419590645951e-15, 6.996605230277502e-16, 5.818242044622173e-17], [1.3898448894755674e-08, 1.502498685704474e-08, 8.121418143989794e-09, 2.9265664055517966e-09, 7.909447685970968e-10, 1.7101095011118647e-10, 3.081203877842847e-11, 4.758500968502484e-12, 6.430251232743893e-13, 7.723838744810388e-14, 8.349894042528626e-15, 8.206085650715857e-16, 7.392691202656025e-17, 6.147619504394387e-18], [1.3461484920478695e-09, 1.4552604793389351e-09, 7.866082661891356e-10, 2.834555843996403e-10, 7.660776505368804e-11, 1.656344059391485e-11, 2.98433155041875e-12, 4.608894813848616e-13, 6.228085641782197e-14, 7.481003065795849e-15, 8.087375331754238e-16, 7.948088242059189e-17, 7.160266724717776e-18, 5.954339788699173e-19], [1.20353159917768e-10, 1.3010837825583534e-10, 7.032715262287181e-11, 2.5342505288503613e-11, 6.849160143115512e-12, 1.4808636835861018e-12, 2.6681583380804023e-13, 4.1206082230307834e-14, 5.5682548519343615e-15, 6.688432692542981e-16, 7.230563213252238e-17, 7.106032810554639e-18, 6.401676570337731e-19, 5.323510838717762e-20]] |
| Legacy trial inputs | {"lambda_home": 1.1622722813816795, "lambda_away": 1.0810549415132322, "rho": -0.10286337681625446, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3627 |
| Legacy p draw | 0.3151 |
| Legacy p away | 0.3222 |
| Legacy p over 1 5 | 0.6696 |
| Legacy p under 3 5 | 0.8108 |
| Legacy p btts yes | 0.4678 |
| Legacy p over 2 5 | 0.3889 |
| Legacy goal margin distribution | {"-1": 0.1898285037298252, "-10": 7.142042106219194e-08, "-11": 6.952432605429008e-09, "-12": 6.189286123340492e-10, "-13": 4.6932750983523355e-11, "-2": 0.09240781057437109, "-3": 0.03030665630097523, "-4": 0.00772448203121917, "-5": 0.0016048153775278277, "-6": 0.0002809260687623286, "-7": 4.24489014364749e-05, "-8": 5.639130224667934e-06, "-9": 6.681331914129916e-07, "0": 0.3150584385247075, "1": 0.20512018631009055, "10": 1.4737490880044864e-07, "11": 1.542403652671748e-08, "12": 1.4762568703037049e-09, "13": 1.20353159917768e-10, "2": 0.10681417960620625, "3": 0.037663299753755757, "4": 0.010320715927659381, "5": 0.002305290436981594, "6": 0.00043386311260704613, "7": 7.048346653182952e-05, "8": 1.0066837039027097e-05, "9": 1.2823426174518905e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3627 |
| Legacy raw p draw | 0.3151 |
| Legacy raw p away | 0.3222 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.1623 |
| Legacy lambda away | 1.0811 |
| Legacy model home team | Hull |
| Legacy model away team | Brentford |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 9.96509439027004, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,402.4115 |
| Elo away rating | 1,496.3114 |
| Elo rating diff | -33.8998 |
| Elo home expectancy | 0.4514 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **50.4%**. Expected goals are 1.87 for Liverpool and 1.28 for Brighton and Hove Albion (3.14 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.8%; Under 3.5 goals: 61.5%; Double Chance 1X: 74.6%; Double Chance X2: 49.6%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 61.8%; BTTS No (at least one team does not score): 38.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 50.4% | 1.98 |
| Draw | 24.2% | 4.14 |
| Brighton and Hove Albion win | 25.4% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.87 |
| Brighton and Hove Albion expected goals | 1.28 |
| Expected total goals | 3.14 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 38.5% |
| Under 3.5 | 61.5% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.06% |
| 2 | 2-1 | 9.59% |
| 3 | 2-0 | 7.50% |
| 4 | 1-0 | 7.26% |
| 5 | 1-2 | 6.57% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 290ba8cd3f3a2e9252effca673bf5549 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9064 |
| Dc lambda away | 1.2774 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:32:17.000888+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7706 |
| Shot lambda away | 1.2826 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.66 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.86 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.60 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.77 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.14506119842603785, "-10": 1.7234249545776045e-07, "-11": 1.968704065046789e-08, "-12": 2.066981516484551e-09, "-13": 2.0074134016019955e-10, "-14": 1.8125590094856552e-11, "-15": 1.5166465419111083e-12, "-16": 1.0549751609091069e-13, "-2": 0.0730903467004493, "-3": 0.02642882666405914, "-4": 0.0076063316671911695, "-5": 0.0018091449924298644, "-6": 0.00036567697624611455, "-7": 6.416238680481066e-05, "-8": 9.93643128591576e-06, "-9": 1.3762725651541824e-06, "0": 0.24172191396303125, "1": 0.21518563149684267, "10": 7.520771822221731e-06, "11": 1.253249318216184e-06, "12": 1.9194669362844026e-07, "13": 2.7193672646429608e-08, "14": 3.5818731701452244e-09, "15": 4.3720934127666946e-10, "16": 4.4364367186160154e-11, "2": 0.15553711138424867, "3": 0.08204250141695411, "4": 0.034444768693129214, "5": 0.011951114084065555, "6": 0.0035238680530283017, "7": 0.0009019646894324216, "8": 0.0002037635329054103, "9": 4.1170627332685616e-05} |
| Raw goal margin distribution | {"-1": 0.14506119842603785, "-10": 1.7234249545776045e-07, "-11": 1.968704065046789e-08, "-12": 2.066981516484551e-09, "-13": 2.0074134016019955e-10, "-14": 1.8125590094856552e-11, "-15": 1.5166465419111083e-12, "-16": 1.0549751609091069e-13, "-2": 0.0730903467004493, "-3": 0.02642882666405914, "-4": 0.0076063316671911695, "-5": 0.0018091449924298644, "-6": 0.00036567697624611455, "-7": 6.416238680481066e-05, "-8": 9.93643128591576e-06, "-9": 1.3762725651541824e-06, "0": 0.24172191396303125, "1": 0.21518563149684267, "10": 7.520771822221731e-06, "11": 1.253249318216184e-06, "12": 1.9194669362844026e-07, "13": 2.7193672646429608e-08, "14": 3.5818731701452244e-09, "15": 4.3720934127666946e-10, "16": 4.4364367186160154e-11, "2": 0.15553711138424867, "3": 0.08204250141695411, "4": 0.034444768693129214, "5": 0.011951114084065555, "6": 0.0035238680530283017, "7": 0.0009019646894324216, "8": 0.0002037635329054103, "9": 4.1170627332685616e-05} |
| Unadjusted home-win probability | 50.4% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 61.5% |
| Raw p btts yes | 61.8% |
| P home draw | 74.6% |
| P draw away | 49.6% |
| P home away | 75.8% |
| Raw p home draw | 74.6% |
| Raw p draw away | 49.6% |
| Raw p home away | 75.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6084 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.05709758431464728, 0.05344379976008789, 0.045346686120393664, 0.021230909881790463, 0.007455090541985473, 0.002094243734202661, 0.0004902530239289624, 9.837087804586384e-05, 1.727113455357664e-05, 2.6953965301142202e-06, 3.7858811121024547e-07, 4.834132982877346e-08, 5.658243771307412e-09, 6.113397126183881e-10, 6.133365974229112e-11, 5.743173378763667e-12], [0.0658832562711259, 0.11929176486736687, 0.07596316647552896, 0.03556527013893735, 0.012488504285130056, 0.0035082031132154775, 0.000821254544885009, 0.00016478741942691356, 2.893199440927996e-05, 4.515233038000267e-06, 6.34197428256755e-07, 8.097968781405837e-08, 9.478490058078326e-09, 1.0240946877449466e-09, 1.027439798618886e-10, 9.620761135898044e-12], [0.0645018173431435, 0.09059750921521806, 0.06362540633805892, 0.02978884200202062, 0.010460150577740338, 0.0029384089546436168, 0.0006878682991989175, 0.00013802303151508417, 2.423292742876761e-05, 3.7818794302939135e-06, 5.311925627058587e-07, 6.782715599353566e-08, 7.939015833558768e-09, 8.577636196538773e-10, 8.605654254299544e-11, 8.058179575098548e-12], [0.036017055180928376, 0.05058858219916552, 0.03552767759698561, 0.016633738557395583, 0.005840824895755298, 0.0016407729552876409, 0.0003840975574014942, 7.707043533163697e-05, 1.3531381290454967e-05, 2.1117569355275393e-06, 2.966116712788928e-07, 3.787388512153747e-08, 4.433052945444573e-09, 4.789651035243361e-10, 4.805295988734574e-11, 4.499592575355642e-12], [0.015083624586167568, 0.021186051397193196, 0.014878677576480141, 0.0069660627889719775, 0.002446085876775542, 0.0006871412214122486, 0.0001608566644664466, 3.2276417585924146e-05, 5.666822967403229e-06, 8.843851523319358e-07, 1.2421834808459315e-07, 1.586124856469133e-08, 1.8565234182470656e-09, 2.0058635485728105e-10, 2.0124155169095904e-11, 1.884389627537062e-12], [0.005053510999464771, 0.007098024958081014, 0.004984847001508165, 0.002333860454158684, 0.0008195193279509604, 0.00023021493943683064, 5.38922802390523e-05, 1.0813662880695474e-05, 1.8985723248544442e-06, 2.962981523135552e-07, 4.1617237607232865e-08, 5.314040642487122e-09, 6.219964877327433e-10, 6.720303497498837e-11, 6.742254749247986e-12, 6.313325855887933e-13], [0.001410910514015918, 0.0019817267723696605, 0.0013917399301067103, 0.0006516000961246958, 0.0002288049707159502, 6.427465549582533e-05, 1.5046407304075216e-05, 3.019111001245039e-06, 5.300702135684456e-07, 8.27246994073945e-08, 1.161928768148768e-08, 1.4836488562480769e-09, 1.7365775681818977e-10, 1.876269164745716e-11, 1.882397824976586e-12, 1.7626434036503033e-13], [0.00033764392073519365, 0.00047424552485916463, 0.00033305622289781336, 0.000155933922826015, 5.475514331262755e-05, 1.5381518863122942e-05, 3.6007442744659384e-06, 7.225011547285346e-07, 1.268506991735212e-07, 1.979678482234197e-08, 2.780602887252548e-09, 3.550508780262975e-10, 4.15579055480133e-11, 4.490085450820754e-12, 4.5047519009509965e-13, 4.218168507175788e-14], [7.07011458680852e-05, 9.930491849918719e-05, 6.974050220154721e-05, 3.265187479016171e-05, 1.1465485195008514e-05, 3.220822120672071e-06, 7.539799491380377e-07, 1.5128855102468822e-07, 2.65619761973132e-08, 4.1453593134324855e-09, 5.822459646387169e-10, 7.434608585065065e-11, 8.702041889942841e-12, 9.402040638771556e-13, 9.432751537631143e-14, 8.832658567422958e-15], [1.315956240704992e-05, 1.848356566604049e-05, 1.2980758370346882e-05, 6.077474116332172e-06, 2.1340639688122747e-06, 5.994897137604044e-07, 1.4033784138179274e-07, 2.8159248400247467e-08, 4.943964898041395e-09, 7.715732738835993e-10, 1.083730965579001e-10, 1.3837992927256998e-11, 1.6197059031140545e-12, 1.749996255653115e-13, 1.755712457069049e-14, 1.6440175079345504e-15], [2.204443401261635e-06, 3.096301617328886e-06, 2.174490780753692e-06, 1.0180769920517633e-06, 3.574908563371494e-07, 1.0042439883224125e-07, 2.3508899370062577e-08, 4.71713780445749e-09, 8.281955325290903e-10, 1.292512288471937e-10, 1.8154278249660235e-11, 2.318091685089354e-12, 2.71327410415369e-13, 2.9315318995260604e-14, 2.9411074781827542e-15, 2.75400004561198e-16], [3.357096092801945e-07, 4.715286432721374e-07, 3.311481936766528e-07, 1.5504060073542757e-07, 5.444145929693696e-08, 1.5293400445153383e-08, 3.5801161497792675e-09, 7.183620538177335e-10, 1.2612399051561997e-10, 1.9683372006939788e-11, 2.764673229745596e-12, 3.530168447199127e-13, 4.13198265310055e-14, 4.4643624237260095e-15, 4.478944851959961e-16, 4.1940032515278255e-17], [4.686407306126073e-08, 6.582401032893598e-08, 4.622731287269925e-08, 2.1643211393042136e-08, 7.599867431628577e-09, 2.1349136754038945e-09, 4.997736739523031e-10, 1.0028122771562765e-10, 1.7606537742470496e-11, 2.7477407805008595e-12, 3.8594024313784516e-13, 4.9280112172784726e-14, 5.768126130138454e-15, 6.232118504025964e-16, 6.252475144505568e-17, 5.854705059536124e-18], [6.038849189929953e-09, 8.482004347620878e-09, 5.956797022935259e-09, 2.788918697218316e-09, 9.793099550496181e-10, 2.751024586025677e-10, 6.440024626433935e-11, 1.2922120746186118e-11, 2.268757690877687e-12, 3.5407063668525975e-13, 4.973180460835614e-14, 6.350177140712071e-15, 7.432739310317073e-16, 8.03063441165014e-17, 8.056865738515231e-18, 7.544303897751602e-19], [7.225762006028542e-10, 1.014911000794818e-09, 7.127582798014665e-10, 3.337070048688611e-10, 1.1717895981113468e-10, 3.291727994218268e-11, 7.705786947150811e-12, 1.546191437944949e-12, 2.714673377001355e-13, 4.236618722449602e-14, 5.9506401456344895e-15, 7.598280280193665e-16, 8.893615922511035e-17, 9.609025029598402e-18, 9.640412023886249e-19, 9.027108104837255e-20], [8.069560815965113e-11, 1.1334287009277193e-10, 7.959916588924382e-11, 3.7267612305195585e-11, 1.3086270233624797e-11, 3.676124292053558e-12, 8.605641363917625e-13, 1.726750179595111e-13, 3.031683287232154e-14, 4.731356001808572e-15, 6.645534755927213e-16, 8.48558045042385e-17, 9.932180786007331e-18, 1.0731132826376262e-18, 1.0766185082321699e-19, 1.0081261711014078e-20]] |
| Legacy trial inputs | {"lambda_home": 1.6751646696706732, "lambda_away": 1.4045729709172063, "rho": -0.10286337681625446, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4290 |
| Legacy p draw | 0.2593 |
| Legacy p away | 0.3117 |
| Legacy p over 1 5 | 0.8236 |
| Legacy p under 3 5 | 0.6294 |
| Legacy p btts yes | 0.6243 |
| Legacy p over 2 5 | 0.5944 |
| Legacy goal margin distribution | {"-1": 0.1657808168528369, "-10": 4.680065354491416e-07, "-11": 5.872752085602055e-08, "-12": 6.772894594170709e-09, "-13": 7.221418720553753e-10, "-14": 7.095442087818916e-11, "-15": 5.743173378763667e-12, "-2": 0.09318510058306433, "-3": 0.03707618125017427, "-4": 0.011734207494069806, "-5": 0.003067980220447947, "-6": 0.0006815148383527119, "-7": 0.00013139786602376857, "-8": 2.235735969043703e-05, "-9": 3.4020616721839026e-06, "0": 0.25934059115420244, "1": 0.19986205696460466, "10": 2.7251091311877933e-06, "11": 4.0783720990716823e-07, "12": 5.6096103300988265e-08, "13": 7.133359356614015e-09, "14": 8.359190706956262e-10, "15": 8.069560815965113e-11, "2": 0.13254790704999572, "3": 0.06289767482508916, "4": 0.02374141261731814, "5": 0.007403184040599217, "6": 0.001961347312421738, "7": 0.00045100431694650633, "8": 9.1522125763967e-05, "9": 1.660966851724763e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.4290 |
| Legacy raw p draw | 0.2593 |
| Legacy raw p away | 0.3117 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.6752 |
| Legacy lambda away | 1.4046 |
| Legacy model home team | Liverpool |
| Legacy model away team | Brighton |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 10.311435294722774, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,569.5028 |
| Elo away rating | 1,528.3139 |
| Elo rating diff | 101.1890 |
| Elo home expectancy | 0.6416 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **45.6%**. Expected goals are 1.71 for Manchester United and 1.33 for Bournemouth (3.04 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 58.5%; Under 3.5 goals: 63.9%; Double Chance 1X: 70.9%; Double Chance X2: 54.4%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 45.6% | 2.19 |
| Draw | 25.3% | 3.95 |
| Bournemouth win | 29.1% | 3.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.71 |
| Bournemouth expected goals | 1.33 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 36.1% |
| Under 3.5 | 63.9% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.72% |
| 2 | 2-1 | 9.30% |
| 3 | 1-0 | 7.37% |
| 4 | 1-2 | 7.24% |
| 5 | 2-0 | 7.00% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 33fb7467b23c91d57dc976d9ab05ea97 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6497 |
| Dc lambda away | 1.3127 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:32:17.000888+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.8445 |
| Shot lambda away | 1.3667 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.78 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.39 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.24 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.16105431812409204, "-10": 2.787159157141641e-07, "-11": 3.311104696630396e-08, "-12": 3.6149160210087735e-09, "-13": 3.650279184773939e-10, "-14": 3.426887119460178e-11, "-15": 2.983322097574746e-12, "-16": 2.1700297687609206e-13, "-2": 0.08502940838164715, "-3": 0.03216434852423022, "-4": 0.009662944173032715, "-5": 0.0023959571455811793, "-6": 0.0005044470841850928, "-7": 9.21447465476343e-05, "-8": 1.4849941982241915e-05, "-9": 2.139841360977584e-06, "0": 0.2532024819907751, "1": 0.20936722584566383, "10": 3.430761124384751e-06, "11": 5.238711659364858e-07, "12": 7.351444210002173e-08, "13": 9.541648333995493e-09, "14": 1.1513834815849676e-09, "15": 1.2883777363404331e-10, "16": 1.2045688527553955e-11, "2": 0.14048012970511475, "3": 0.06830356516575722, "4": 0.02637551539771244, "5": 0.008406077727483705, "6": 0.0022748504054329916, "7": 0.0005341099609814175, "8": 0.0001106388685187575, "9": 2.0492144876934305e-05} |
| Raw goal margin distribution | {"-1": 0.16105431812409204, "-10": 2.787159157141641e-07, "-11": 3.311104696630396e-08, "-12": 3.6149160210087735e-09, "-13": 3.650279184773939e-10, "-14": 3.426887119460178e-11, "-15": 2.983322097574746e-12, "-16": 2.1700297687609206e-13, "-2": 0.08502940838164715, "-3": 0.03216434852423022, "-4": 0.009662944173032715, "-5": 0.0023959571455811793, "-6": 0.0005044470841850928, "-7": 9.21447465476343e-05, "-8": 1.4849941982241915e-05, "-9": 2.139841360977584e-06, "0": 0.2532024819907751, "1": 0.20936722584566383, "10": 3.430761124384751e-06, "11": 5.238711659364858e-07, "12": 7.351444210002173e-08, "13": 9.541648333995493e-09, "14": 1.1513834815849676e-09, "15": 1.2883777363404331e-10, "16": 1.2045688527553955e-11, "2": 0.14048012970511475, "3": 0.06830356516575722, "4": 0.02637551539771244, "5": 0.008406077727483705, "6": 0.0022748504054329916, "7": 0.0005341099609814175, "8": 0.0001106388685187575, "9": 2.0492144876934305e-05} |
| Unadjusted home-win probability | 45.6% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 29.1% |
| Raw p over 1 5 | 81.5% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 61.0% |
| P home draw | 70.9% |
| P draw away | 54.4% |
| P home away | 74.7% |
| Raw p home draw | 70.9% |
| Raw p draw away | 54.4% |
| Raw p home away | 74.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5851 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.05917164491896115, 0.05472832175479047, 0.04547715166473482, 0.020889614216893147, 0.00719662456019114, 0.001983431748336008, 0.00045553780889499255, 8.967777137073264e-05, 1.5447323374404687e-05, 2.3652069531078272e-06, 3.259324231063221e-07, 4.083130857164427e-08, 4.688894603166146e-09, 4.970333577240529e-10, 4.8923319807115926e-11, 4.494517530537591e-12], [0.06826627245569072, 0.12088484880081789, 0.07552288626717607, 0.03469091402861509, 0.01195127307386635, 0.003293840640077827, 0.000756501427028757, 0.0001489258645276493, 2.5653023631251605e-05, 3.927846164042254e-06, 5.412686683306908e-07, 6.7807638792548e-08, 7.786742152285965e-09, 8.254121547259214e-10, 8.12458604453596e-11, 7.463944505298404e-12], [0.06604608292888028, 0.0910134304205628, 0.06270958207951864, 0.028805211614859362, 0.009923605635634911, 0.0027350036549859493, 0.0006281524803449051, 0.00012365892230761934, 2.13007006286911e-05, 3.2614430352721243e-06, 4.494363716936951e-07, 5.630331281880228e-08, 6.465634064929162e-09, 6.853717306711847e-10, 6.746158953982866e-11, 6.197602656976472e-12], [0.03656041643506765, 0.05038132118967501, 0.03471346571400864, 0.015945389725436666, 0.005493303137551378, 0.0015139864189280183, 0.00034771958074879467, 6.845253336744534e-05, 1.179119867233066e-05, 1.8054017779858279e-06, 2.487896356833333e-07, 3.116721646529587e-08, 3.579111181886665e-09, 3.7939382284251315e-10, 3.73439831337709e-11, 3.430739931725168e-12], [0.015178765991446956, 0.020916782664009887, 0.014411968577022564, 0.0066200378137016135, 0.0022806513430464275, 0.0006285608263776508, 0.0001443625281512807, 2.8419396900237872e-05, 4.895344825293043e-06, 7.495475648440449e-07, 1.0328984265924622e-07, 1.2939674420057605e-08, 1.4859374258965084e-09, 1.575127040950056e-10, 1.55040789041002e-11, 1.4243382236538433e-12], [0.0050414072811735015, 0.006947206411936441, 0.004786726625944845, 0.002198749677967578, 0.0007574853115945782, 0.0002087673746697405, 4.794792283908861e-05, 9.439091065779115e-06, 1.6259178815981428e-06, 2.4895136753013563e-07, 3.430622523247357e-08, 4.297725445800504e-09, 4.935325943165653e-10, 5.231556331715936e-11, 5.149455253415378e-12, 4.730733114686947e-13], [0.0013953586756761966, 0.0019228449910820048, 0.0013248682665542655, 0.0006085690498066935, 0.00020965647928860646, 5.778254983115698e-05, 1.3271006761152138e-05, 2.612547821382672e-06, 4.500208960496704e-07, 6.890465918154673e-08, 9.495263194980539e-09, 1.1895227169736182e-09, 1.3659975256914776e-10, 1.4479880532582866e-11, 1.4252641498916881e-12, 1.3093704050727994e-13], [0.0003310344102396766, 0.0004561750815048924, 0.0003143112899280307, 0.00014437671116729334, 4.973883072794712e-05, 1.3708312162987244e-05, 3.1484090600116243e-06, 6.197999427317553e-07, 1.0676280193487944e-07, 1.6346917543530885e-08, 2.2526529605713407e-09, 2.8220195849589387e-10, 3.24068781159082e-11, 3.4352018559827793e-12, 3.38129174612762e-13, 3.1063458262336064e-14], [6.871767799839903e-05, 9.469496642071275e-05, 6.524621412286975e-05, 2.9970395951522745e-05, 1.032502014369225e-05, 2.8456358371797715e-06, 6.535615431534066e-07, 1.2866098378482736e-07, 2.216232397186778e-08, 3.393369937612902e-09, 4.676162839826983e-10, 5.858080826219229e-11, 6.727171999098213e-12, 7.130953390253752e-13, 7.0190442516478e-14, 6.44829859482708e-15], [1.2679767482843276e-05, 1.747308976357239e-05, 1.2039213901160457e-05, 5.530129409246184e-06, 1.9051699430347592e-06, 5.250759601790708e-07, 1.205950003593909e-07, 2.3740490162422075e-08, 4.089386065246181e-09, 6.26143709238901e-10, 8.628443109253435e-11, 1.0809315002449996e-11, 1.2412959699780107e-12, 1.315801603795709e-13, 1.295152159605208e-14, 1.1898383243429338e-15], [2.1057005604939578e-06, 2.9017168460304627e-06, 1.999325263170803e-06, 9.183761936021409e-07, 3.1638730144797237e-07, 8.719818759665803e-08, 2.002694136096227e-08, 3.942529980068984e-09, 6.791151763087498e-10, 1.0398228211030801e-10, 1.432906203992239e-11, 1.795078710237579e-12, 2.0613923900878007e-13, 2.1851222259086582e-14, 2.150830156858764e-15, 1.9759378315542216e-16], [3.1789906503799637e-07, 4.3807419234465974e-07, 3.018395130786062e-07, 1.3864788696774072e-07, 4.776520897948147e-08, 1.3164370485556006e-08, 3.023481141462588e-09, 5.952064686035861e-10, 1.0252648626878928e-10, 1.5698276803245855e-11, 2.1632683729229804e-12, 2.7100427019892806e-13, 3.1120983001098123e-14, 3.2988940860953025e-15, 3.247123113081824e-16, 2.983086964069294e-17], [4.399398755647317e-08, 6.062499921010925e-08, 4.177150939668525e-08, 1.9187453141018304e-08, 6.610217646360439e-09, 1.8218145789800653e-09, 4.1841894595958637e-10, 8.237050326067718e-11, 1.4188619776465584e-11, 2.1724813637231784e-12, 2.9937427424742645e-13, 3.750422634762298e-14, 4.306826566891225e-15, 4.565332878737882e-16, 4.4936871334989254e-17, 4.12828803889234e-18], [5.6199868370782675e-09, 7.744505930982897e-09, 5.336077632720086e-09, 2.451090252984185e-09, 8.444184813909209e-10, 2.3272666384974625e-10, 5.345068949838902e-11, 1.0522372937763063e-11, 1.81251713720395e-12, 2.775223921734654e-13, 3.8243395838367005e-14, 4.7909559945636794e-15, 5.501731022776156e-16, 5.831958435786845e-17, 5.74043498734773e-18, 5.273657998939193e-19], [6.666418680004902e-10, 9.186519559991299e-10, 6.329646072127644e-10, 2.907479024873764e-10, 1.0016477442520763e-10, 2.7605996672222514e-11, 6.340311556965307e-12, 1.2481620605849975e-12, 2.1500046977987511e-13, 3.291965822942497e-14, 4.536425009426779e-15, 5.683023726412329e-16, 6.526143837316368e-17, 6.9178590243022214e-18, 6.80929406783158e-19, 6.25560401034012e-20], [7.380514703163953e-11, 1.0170564727172098e-10, 7.007667556386915e-11, 3.2189234913469055e-11, 1.108942636023878e-11, 3.056310653663949e-12, 7.019475510768307e-13, 1.3818631685569767e-13, 2.3803097353560738e-14, 3.644595895456488e-15, 5.022359544007879e-16, 6.291780067312687e-17, 7.225213845440754e-18, 7.658888931836554e-19, 7.538694672228584e-20, 6.925694228291808e-21]] |
| Legacy trial inputs | {"lambda_home": 1.660677582095366, "lambda_away": 1.3780291939276375, "rho": -0.10286337681625446, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4310 |
| Legacy p draw | 0.2612 |
| Legacy p away | 0.3078 |
| Legacy p over 1 5 | 0.8178 |
| Legacy p under 3 5 | 0.6386 |
| Legacy p btts yes | 0.6171 |
| Legacy p over 2 5 | 0.5854 |
| Legacy goal margin distribution | {"-1": 0.16522895431569837, "-10": 4.006010669388574e-07, "-11": 4.934219077595885e-08, "-12": 5.585199087363621e-09, "-13": 5.84476820826389e-10, "-14": 5.6387264312414326e-11, "-15": 4.494517530537591e-12, "-2": 0.09175992621357858, "-3": 0.035953727058432514, "-4": 0.011192224294500227, "-5": 0.0028761683727906314, "-6": 0.0006276775035037585, "-7": 0.00011885447570441207, "-8": 1.9857312835922755e-05, "-9": 2.9665208385355958e-06, "0": 0.2612147978522265, "1": 0.201431755531003, "10": 2.5881005735733656e-06, "11": 3.8416197920967326e-07, "12": 5.240364732958231e-08, "13": 6.608715468641266e-09, "14": 7.683475152722111e-10, "15": 7.380514703163953e-11, "2": 0.13326216516214803, "3": 0.06292520388366234, "4": 0.023606088113827396, "5": 0.0073105294339632755, "6": 0.0019226400815451025, "7": 0.00043873660850136514, "8": 8.833559033491803e-05, "9": 1.5903384021518974e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.4310 |
| Legacy raw p draw | 0.2612 |
| Legacy raw p away | 0.3078 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.6607 |
| Legacy lambda away | 1.3780 |
| Legacy model home team | Man United |
| Legacy model away team | Bournemouth |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 10.260798734512269, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,507.1575 |
| Elo away rating | 1,521.4601 |
| Elo rating diff | 45.6974 |
| Elo home expectancy | 0.5654 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Sunderland win** at **36.9%**. Expected goals are 1.22 for Sunderland and 1.14 for Leeds United (2.37 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 42.1%; Under 3.5 goals: 78.6%; Double Chance 1X: 66.8%; Double Chance X2: 63.1%; Double Chance 12 (either team wins): 70.1%; Under 4.5 goals: 90.8%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 36.9% | 2.71 |
| Draw | 29.9% | 3.35 |
| Leeds United win | 33.2% | 3.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.22 |
| Leeds United expected goals | 1.14 |
| Expected total goals | 2.37 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 69.4% |
| Under 1.5 | 30.6% |
| Over 2.5 | 42.1% |
| Under 2.5 | 57.9% |
| Over 3.5 | 21.4% |
| Under 3.5 | 78.6% |
| Over 4.5 | 9.2% |
| Under 4.5 | 90.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.12% |
| 2 | 1-0 | 10.47% |
| 3 | 0-0 | 10.38% |
| 4 | 0-1 | 9.75% |
| 5 | 2-1 | 8.01% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | e82f6b60fa41b82c8510f5b67ce61849 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1598 |
| Dc lambda away | 1.0977 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:32:17.000888+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3642 |
| Shot lambda away | 1.2538 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.63 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.27 |
| Fair Over 2.5 odds | 2.37 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.67 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.92 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.19227734787434458, "-10": 1.1322152485149821e-07, "-11": 1.1657887593723706e-08, "-12": 1.1019176546289322e-09, "-13": 9.587474147713385e-11, "-14": 7.126397503671846e-12, "-2": 0.0956380599268351, "-3": 0.03289510414471618, "-4": 0.008822296820726919, "-5": 0.0019322540903194368, "-6": 0.0003569852526790077, "-7": 5.697236659841189e-05, "-8": 7.997774925576765e-06, "-9": 1.0016966509507079e-06, "0": 0.29862319469018994, "1": 0.2058193606957749, "10": 2.1648802535438743e-07, "11": 2.3783470693676613e-08, "12": 2.398584355452074e-09, "13": 2.2266940533551767e-10, "14": 1.7659437847192285e-11, "2": 0.1088758938553984, "3": 0.03995606671063982, "4": 0.01143361638972865, "5": 0.0026718783140222634, "6": 0.0005266877327430401, "7": 8.96845587699132e-05, "8": 1.3433002068418894e-05, "9": 1.7951081279830407e-06} |
| Raw goal margin distribution | {"-1": 0.19227734787434458, "-10": 1.1322152485149821e-07, "-11": 1.1657887593723706e-08, "-12": 1.1019176546289322e-09, "-13": 9.587474147713385e-11, "-14": 7.126397503671846e-12, "-2": 0.0956380599268351, "-3": 0.03289510414471618, "-4": 0.008822296820726919, "-5": 0.0019322540903194368, "-6": 0.0003569852526790077, "-7": 5.697236659841189e-05, "-8": 7.997774925576765e-06, "-9": 1.0016966509507079e-06, "0": 0.29862319469018994, "1": 0.2058193606957749, "10": 2.1648802535438743e-07, "11": 2.3783470693676613e-08, "12": 2.398584355452074e-09, "13": 2.2266940533551767e-10, "14": 1.7659437847192285e-11, "2": 0.1088758938553984, "3": 0.03995606671063982, "4": 0.01143361638972865, "5": 0.0026718783140222634, "6": 0.0005266877327430401, "7": 8.96845587699132e-05, "8": 1.3433002068418894e-05, "9": 1.7951081279830407e-06} |
| Unadjusted home-win probability | 36.9% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 69.4% |
| Raw p under 3 5 | 78.6% |
| Raw p btts yes | 49.1% |
| P home draw | 66.8% |
| P draw away | 63.1% |
| P home away | 70.1% |
| Raw p home draw | 66.8% |
| Raw p draw away | 63.1% |
| Raw p home away | 70.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4213 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.1307188283682951, 0.11983648028381881, 0.07635749817400515, 0.029087995439116297, 0.008310691473330292, 0.001899549053751725, 0.00036181171157542166, 5.907013157731996e-05, 8.43842333267098e-06, 1.07152462772206e-06, 1.224575355247466e-07, 1.272260920970835e-08, 1.21165310387174e-09, 1.0651684752757313e-10], [0.10352936859292862, 0.14787045018560932, 0.0766148652231539, 0.02918603809020942, 0.00833870310535106, 0.0019059515858719277, 0.00036303121738405134, 5.9269230628761366e-05, 8.466865491784791e-06, 1.0751362590368866e-06, 1.2287028522605575e-07, 1.2765491447446335e-08, 1.215737045742449e-09, 1.0687586828373159e-10], [0.05885829508489996, 0.06726529260095306, 0.038436549870883165, 0.014642205599662214, 0.004183404576041102, 0.0009561878490352772, 0.00018212741680125743, 2.9734500377125148e-05, 4.2477017583618345e-06, 5.393800317745294e-07, 6.164221306120202e-08, 6.40425911103502e-09, 6.099173763793013e-10, 5.361804956931676e-11], [0.01968556004335494, 0.022497337960942925, 0.012855367442282469, 0.004897185980047971, 0.0013991683219589286, 0.0003198035771807364, 6.091376234752823e-05, 9.944907369279639e-06, 1.4206729551014206e-06, 1.8039934704816543e-07, 2.0616660483814846e-08, 2.1419483367914666e-09, 2.0399104521939377e-10, 1.7932924028496955e-11], [0.004937977820223391, 0.005643291611746951, 0.0032246742871936164, 0.0012284230521116808, 0.00035097107348615124, 8.022037307897901e-05, 1.527976886387787e-05, 2.494606803439957e-06, 3.5636535240205703e-07, 4.5251848184391587e-08, 5.171537511350556e-09, 5.37291972178916e-10, 5.116965199867802e-11, 4.498341978051106e-12], [0.0009909243079421197, 0.0011324625258509028, 0.0006471086450184833, 0.00024651270359874665, 7.043080806835897e-05, 1.6098152031097974e-05, 3.0662540291176827e-06, 5.006030019338185e-07, 7.151330019290822e-08, 9.080874393881241e-09, 1.0377936912644795e-09, 1.0782058872637115e-10, 1.0268424411864864e-11, 9.027007762634345e-13], [0.00016571071192494506, 0.00018937992527077655, 0.00010821495991100758, 4.122393131794817e-05, 1.1778033148358942e-05, 2.692068619538863e-06, 5.127648338378449e-07, 8.371505187363226e-08, 1.1959056602092484e-08, 1.5185803281343667e-09, 1.7354860510768555e-10, 1.8030667302045122e-11, 1.7171724479858074e-12, 1.5095722961975387e-13], [2.375274982580874e-05, 2.7145462925924253e-05, 1.5511386320881244e-05, 5.9089826846863304e-06, 1.6882473773920166e-06, 3.8587748306083506e-07, 7.349901932193244e-08, 1.1999602564676796e-08, 1.714195034964595e-09, 2.1767125495729847e-10, 2.4876222857626797e-11, 2.584491519243768e-12, 2.461371814228417e-13, 2.1638005581553585e-14], [2.979101218122348e-06, 3.404619770854785e-06, 1.9454585352089976e-06, 7.411124035283584e-07, 2.1174221323274395e-07, 4.839726298061908e-08, 9.218343964320842e-09, 1.5050059837101634e-09, 2.1499660267602005e-10, 2.7300615951796608e-11, 3.120008687874762e-12, 3.2415033584196117e-13, 3.0870850001764906e-14, 2.7138672052068245e-15], [3.3212693764453903e-07, 3.795661360746733e-07, 2.1689064530027624e-07, 8.262337363260032e-08, 2.3606211304022923e-08, 5.395598728351192e-09, 1.027712765313019e-09, 1.6778652080220635e-10, 2.396902891932344e-11, 3.0436260160353765e-12, 3.4783609386099213e-13, 3.613810021785503e-14, 3.4416557622141898e-15, 3.025571600441906e-16], [3.332463893281129e-08, 3.808454841247588e-08, 2.1762168687057088e-08, 8.29018601515546e-09, 2.3685777307233936e-09, 5.413784883690409e-10, 1.0311767263922353e-10, 1.6835205428324562e-11, 2.404981781879562e-12, 3.053884721011203e-13, 3.4900849409941295e-14, 3.6259905625802215e-15, 3.453256047829733e-16, 3.035769452040179e-17], [3.039723765306528e-09, 3.4739013116924347e-09, 1.985047204143149e-09, 7.561935029480001e-10, 2.1605101356302447e-10, 4.938211214948247e-11, 9.405930572166702e-12, 1.5356317629569145e-12, 2.1937162746902799e-13, 2.7856163668210916e-14, 3.1834985997801216e-15, 3.3074655986745177e-16, 3.149904938937325e-17, 2.7690924327682234e-18], [2.541641097947232e-10, 2.904675235553821e-10, 1.6597815936431664e-10, 6.322852448072711e-11, 1.8064935425787407e-11, 4.12904643425411e-12, 7.864694805334216e-13, 1.2840064102505285e-13, 1.834258594358248e-14, 2.329171197012694e-15, 2.6618572940106256e-16, 2.7655113242798538e-17, 2.6337682189429956e-18, 2.3153548396292116e-19], [1.961698335224965e-11, 2.241896614969442e-11, 1.2810584435845625e-11, 4.880126124524466e-12, 1.3942941739231111e-12, 3.1868950823484966e-13, 6.07015629356056e-14, 9.910263252514263e-15, 1.4157238934445988e-15, 1.797709072033821e-16, 2.054484020770853e-17, 2.134486637498577e-18, 2.0328042124601194e-19, 1.787045282681367e-20]] |
| Legacy trial inputs | {"lambda_home": 1.0033705537151343, "lambda_away": 1.1428345402109668, "rho": -0.10286337681625446, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3034 |
| Legacy p draw | 0.3223 |
| Legacy p away | 0.3743 |
| Legacy p over 1 5 | 0.6459 |
| Legacy p under 3 5 | 0.8298 |
| Legacy p btts yes | 0.4452 |
| Legacy p over 2 5 | 0.3628 |
| Legacy goal margin distribution | {"-1": 0.21257609151260096, "-10": 1.3585087727260074e-07, "-11": 1.3991964305020115e-08, "-12": 1.3185289721554715e-09, "-13": 1.0651684752757313e-10, "-2": 0.11006253696918657, "-3": 0.03844636781973796, "-4": 0.010409081005763824, "-5": 0.0022937817523893973, "-6": 0.00042551432440650355, "-7": 6.809754147271693e-05, "-8": 9.577395825458634e-06, "-9": 1.2010076614463482e-06, "0": 0.3222906086128647, "1": 0.18495164959326665, "10": 3.6969398529992564e-08, "11": 3.3430018732977557e-09, "12": 2.765830759444176e-10, "13": 1.961698335224965e-11, "2": 0.08483899333583025, "3": 0.026018921920848384, "4": 0.006184781531153775, "5": 0.0011965808890628453, "6": 0.00019488667551593355, "7": 2.7382770668740514e-05, "8": 3.3812041000119605e-06, "9": 3.722611560798127e-07} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3034 |
| Legacy raw p draw | 0.3223 |
| Legacy raw p away | 0.3743 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.0034 |
| Legacy lambda away | 1.1428 |
| Legacy model home team | Sunderland |
| Legacy model away team | Leeds |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 9.537692996453805, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,420.3203 |
| Elo away rating | 1,455.3116 |
| Elo rating diff | 25.0088 |
| Elo home expectancy | 0.5359 |

</details>


---
