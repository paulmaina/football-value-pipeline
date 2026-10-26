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
| Training as of utc | 2026-10-26T11:35:40.173016+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 80, 'bbs_added_results': 10, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 80, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 119, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-26T11:35:40.173016+00:00', 'observations': 348, 'observations_sha256': '7ca0f5f7384002c4ccd320aa6b69d6a2a66bfbbae3f82d69733caa599b57c0b1', 'eligible_training_matches': 179, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 166, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 18, 'retrospective_eligible_training_matches': 179, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '225649214bca033d026dcd3cf885df7a03af2e521b4933744f23380d822ec47a', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 118, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-21T00:00:00+00:00', 'audit_origin_utc': '2025-10-19T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 31, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1969, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1609, 'tuning_matches': 248, 'audit_matches': 105, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9094261757751134, 'audit_candidate_poisson_score': 0.8955631912992509, 'audit_gain': 0.013862984475862539, 'audit_gain_lower95': 0.003252758122502132, 'audit_baseline_briers': [0.625786200280283, 0.15863361164873582, 0.2306533668033659, 0.2523682911503458], 'audit_candidate_briers': [0.6238183660512071, 0.15613922359773086, 0.22796688126399844, 0.24779469717444716], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1877.843 |
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
| Bbs statistics model artifact | bbs/feature_models/EPL/20261026T113540173016Z_973100bf0296eab266e778210a8ef964a86d67e2fbd4eac6d96afe98990e85c4.json |
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

The model's most likely 1X2 outcome is **Chelsea win** at **50.8%**. Expected goals are 1.89 for Chelsea and 1.29 for Tottenham Hotspur (3.18 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.6%; Under 3.5 goals: 60.6%; Double Chance 1X: 74.8%; Double Chance X2: 49.2%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 78.4%; BTTS Yes (both teams score): 62.3%; BTTS No (at least one team does not score): 37.7%.

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
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
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
| Dc lambda home | 1.9631 |
| Dc lambda away | 1.3073 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:35:40.173016+00:00 |
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
| Goal margin distribution | {"-1": 0.14362093552410413, "-10": 1.7967855757447515e-07, "-11": 2.0671418215809534e-08, "-12": 2.185937756154525e-09, "-13": 2.1383011315173823e-10, "-14": 1.944726902428971e-11, "-15": 1.638492792943785e-12, "-16": 1.1448998107841575e-13, "-2": 0.07252619489190923, "-3": 0.026339172526856736, "-4": 0.007621314127935311, "-5": 0.001823569077460158, "-6": 0.0003709443111205634, "-7": 6.551888628322512e-05, "-8": 1.0215746967160173e-05, "-9": 1.4248033886995123e-06, "0": 0.23936519667754466, "1": 0.21473601581811289, "10": 8.46923817992777e-06, "11": 1.4323632740954996e-06, "12": 2.2266681876771468e-07, "13": 3.202000446950742e-08, "14": 4.2810071572874465e-09, "15": 5.302329064527293e-10, "16": 5.446586863836327e-11, "2": 0.15673446705714278, "3": 0.08367708744636874, "4": 0.035593369246331254, "5": 0.012519767570885005, "6": 0.00374384251261827, "7": 0.000972098274903453, "8": 0.00022281714372099885, "9": 4.568443141968156e-05} |
| Raw goal margin distribution | {"-1": 0.14362093552410413, "-10": 1.7967855757447515e-07, "-11": 2.0671418215809534e-08, "-12": 2.185937756154525e-09, "-13": 2.1383011315173823e-10, "-14": 1.944726902428971e-11, "-15": 1.638492792943785e-12, "-16": 1.1448998107841575e-13, "-2": 0.07252619489190923, "-3": 0.026339172526856736, "-4": 0.007621314127935311, "-5": 0.001823569077460158, "-6": 0.0003709443111205634, "-7": 6.551888628322512e-05, "-8": 1.0215746967160173e-05, "-9": 1.4248033886995123e-06, "0": 0.23936519667754466, "1": 0.21473601581811289, "10": 8.46923817992777e-06, "11": 1.4323632740954996e-06, "12": 2.2266681876771468e-07, "13": 3.202000446950742e-08, "14": 4.2810071572874465e-09, "15": 5.302329064527293e-10, "16": 5.446586863836327e-11, "2": 0.15673446705714278, "3": 0.08367708744636874, "4": 0.035593369246331254, "5": 0.012519767570885005, "6": 0.00374384251261827, "7": 0.000972098274903453, "8": 0.00022281714372099885, "9": 4.568443141968156e-05} |
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
| Unanchored p over 2 5 | 0.6165 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.04937660615976461, 0.03891750403271151, 0.030437122899954337, 0.012618927622715301, 0.003923761163400717, 0.0009760513493839285, 0.00020233057793297315, 3.5950388522837735e-05, 5.589252213522266e-06, 7.724160764621709e-07, 9.60708007343803e-08, 1.0862726161807564e-08, 1.1258944847693814e-09, 1.0771952896128474e-10, 9.569880532190528e-12, 7.935154067661591e-13, 6.168442019638146e-14, 4.5130139066141116e-15], [0.06834005452994704, 0.10749495677514972, 0.06061459634783371, 0.025130207171932283, 0.007814049963480537, 0.0019437763139483197, 0.00040293513780993663, 7.159409567133798e-05, 1.1130824287252082e-05, 1.5382429161003975e-06, 1.9132205190577865e-07, 2.163278584836303e-08, 2.2421843204060084e-09, 2.145201367497469e-10, 1.9058123445583325e-11, 1.580261585006445e-12, 1.22842630147524e-13, 8.987528721447744e-15], [0.07803162020243977, 0.09705339471681212, 0.060356054389364235, 0.025023018254238416, 0.007780720371222868, 0.0019354854440042073, 0.00040121648181051794, 7.128872239781985e-05, 1.1083347519542672e-05, 1.5316817846222927e-06, 1.905059980016288e-07, 2.1540514627281374e-08, 2.23262063838261e-09, 2.1360513508961625e-10, 1.8976834039115966e-11, 1.5735212295525026e-12, 1.2231866436872663e-13, 8.949193841444429e-15], [0.0517991924585558, 0.0644262858908977, 0.040065743467107826, 0.01661085768926177, 0.00516502196070738, 0.0012848199583016297, 0.00026633677097733606, 4.732310109708283e-05, 7.3573821709766014e-06, 1.0167657590740848e-06, 1.264622832307547e-07, 1.4299091316317405e-08, 1.4820651658199024e-09, 1.4179602414941136e-10, 1.2597260906489627e-11, 1.0445397493446512e-12, 8.119795565530316e-14, 5.940681648532634e-15], [0.025789125604442582, 0.032075742887255274, 0.01994742469267882, 0.008270003353597382, 0.002571495688875083, 0.000639669881152028, 0.00013260037683621604, 2.3560625953017607e-05, 3.6630002114224496e-06, 5.062144528997752e-07, 6.296143919756882e-08, 7.119050403748034e-09, 7.378718258181147e-10, 7.0595607835499e-11, 6.271764642843101e-12, 5.20042215257215e-13, 4.042580931920874e-14, 2.9576713060265068e-15], [0.01027165046982293, 0.012775571554897487, 0.007944936845048203, 0.003293891585753585, 0.001024210952550917, 0.00025477658824287316, 5.2813916373876036e-05, 9.384052734147224e-06, 1.458950505717704e-06, 2.016221101371273e-07, 2.5077154861079437e-08, 2.835474088805662e-09, 2.9388982017397716e-10, 2.8117797381467752e-11, 2.498005369719886e-12, 2.0712962302817813e-13, 1.6101351773442488e-14, 1.1780223310438842e-15], [0.0034092794573086227, 0.004240359792756774, 0.00263701632517721, 0.0010932806709986315, 0.00033994744766101183, 8.45632930220394e-05, 1.752954899336397e-05, 3.1146755145943418e-06, 4.842425278183302e-07, 6.692070765542458e-08, 8.323397409871076e-09, 9.41126607753688e-10, 9.754542656751228e-11, 9.33262179033792e-12, 8.291168411788305e-13, 6.874871481118654e-14, 5.3442246693820315e-15, 3.9099922113568245e-16], [0.0009699250616754187, 0.0012063637742276369, 0.0007502195856527746, 0.00031103355871096573, 9.671355876449646e-05, 2.405788619763864e-05, 4.987079851163898e-06, 8.861115313136265e-07, 1.3776487657917952e-07, 1.9038647993758343e-08, 2.3679700790768627e-09, 2.677463946562128e-10, 2.7751246286609326e-11, 2.655089991576317e-12, 2.358801070392006e-13, 1.9558708016850498e-14, 1.5204084930455226e-15, 1.1123756454228885e-16], [0.00024144699999384422, 0.00030030455516365175, 0.0001867549107140242, 7.742672358465476e-05, 2.4075260600112635e-05, 5.98881777379727e-06, 1.2414520630215682e-06, 2.2058299073750873e-07, 3.4294315580533374e-08, 4.73936041418639e-09, 5.894674694565471e-10, 6.665109120620302e-11, 6.908219435445838e-12, 6.609412814557338e-13, 5.871849945238425e-14, 4.868820861548612e-15, 3.784808578684306e-16, 2.7690774583103996e-17], [5.342603245870244e-05, 6.644970081251167e-05, 4.132407493936109e-05, 1.7132549369054955e-05, 5.327238086644816e-06, 1.3251718711779584e-06, 2.747015213135985e-07, 4.880936198536433e-08, 7.588453024478556e-09, 1.0486989829166115e-09, 1.3043404207688479e-10, 1.474817811893014e-11, 1.528611893290777e-12, 1.4624936469391088e-13, 1.2992898887744986e-14, 1.0773452616571574e-15, 8.374811282804036e-17, 6.1272586601665996e-18], [1.063963043614536e-05, 1.3233254028063067e-05, 8.22956272881088e-06, 3.4118946387543e-06, 1.060903119299972e-06, 2.6390391209767055e-07, 5.470596509824716e-08, 9.720234676788709e-09, 1.5112171360452592e-09, 2.0884518470689466e-10, 2.597553926661903e-11, 2.9370544202988555e-12, 3.0441836828295395e-13, 2.912511223937605e-14, 2.5874959471614894e-15, 2.1455000322220946e-16, 1.6678179703943425e-17, 1.2202247618000849e-18], [1.926227050544625e-06, 2.3957835780636934e-06, 1.4899019695774693e-06, 6.176984986668128e-07, 1.9206872820134655e-07, 4.7777867593984826e-08, 9.904113721883242e-09, 1.7597771919280697e-09, 2.735947779546716e-10, 3.7809888846492e-11, 4.70268085796153e-12, 5.317321599894738e-13, 5.511271271953329e-14, 5.2728879430853225e-15, 4.684471623812098e-16, 3.884270439479485e-17, 3.019462103725016e-18, 2.209127429782453e-19], [3.196685057005834e-07, 3.9759412378986063e-07, 2.472578381248061e-07, 1.025106339288943e-07, 3.187491491129048e-08, 7.929013111414418e-09, 1.6436448822935433e-09, 2.920451901817907e-10, 4.540463379513036e-11, 6.274769459210873e-12, 7.804370529560646e-13, 8.824402344921836e-14, 9.146273029016726e-15, 8.750662124779759e-16, 7.77415125365101e-17, 6.44617116541002e-18, 5.010971777415366e-19, 3.6661745778155175e-20], [4.897000158919332e-08, 6.090742292917681e-08, 3.787741522855363e-08, 1.5703598624473463e-08, 4.882916540184046e-09, 1.2146451018555568e-09, 2.517898731424432e-10, 4.4738387336517816e-11, 6.955533464991628e-12, 9.61231603707582e-13, 1.1955511112915397e-13, 1.3518097314824559e-14, 1.4011170846641451e-15, 1.340513471034055e-16, 1.1909218220030129e-17, 9.874886220728023e-19, 7.676305032478696e-20, 5.616210909123613e-21], [6.965875400712828e-09, 8.663947423616047e-09, 5.387979302034439e-09, 2.233802487460557e-09, 6.945841761726222e-10, 1.7278060365591523e-10, 3.5816557617972524e-11, 6.3639375475083674e-12, 9.894093912652082e-13, 1.3673308893933176e-13, 1.700645253456241e-14, 1.9229197160279226e-15, 1.993058345281793e-16, 1.9068510331151314e-17, 1.694060190901363e-18, 1.4046809225545816e-19, 1.091937567057618e-20, 7.9889369302598905e-22], [9.248218083585619e-10, 1.1502656971171427e-09, 7.153330306476747e-10, 2.9656994090903823e-10, 9.221620498688105e-11, 2.293915138160465e-11, 4.755171702043703e-12, 8.449057573388935e-13, 1.313585629658546e-13, 1.815331674786843e-14, 2.2578552273801216e-15, 2.5529570754643325e-16, 2.6460763608533846e-17, 2.531623549475873e-18, 2.2491125940284923e-19, 1.864919304802329e-20, 1.449706773792617e-21, 1.0606481847133515e-22], [1.1510964093006451e-10, 1.431699276256571e-10, 8.903523636560269e-11, 3.691312110089667e-11, 1.147785892161572e-11, 2.8551635081610788e-12, 5.918611588048057e-13, 1.0516274320957286e-13, 1.6349784228083845e-14, 2.259485831379417e-15, 2.81028087948191e-16, 3.177584801856563e-17, 3.293487426642441e-18, 3.1510316378404344e-19, 2.7993992006893715e-20, 2.3212059836732577e-21, 1.8044040990051063e-22, 1.3201551973798491e-23], [1.348454811667693e-11, 1.6771677527013243e-11, 1.043005537286928e-11, 4.324196944756161e-12, 1.3445766979586911e-12, 3.34468854178508e-13, 6.933372574017892e-14, 1.2319316257382668e-14, 1.915299625118539e-15, 2.6468804147079756e-16, 3.292110672447889e-17, 3.7223897850127835e-18, 3.8581642091310787e-19, 3.6912840135993324e-20, 3.2793633021943964e-21, 2.719182643839292e-22, 2.1137737637237718e-23, 1.5464991582560162e-24]] |
| Legacy trial inputs | {"lambda_home": 1.991469316829701, "lambda_away": 1.243770082756498, "rho": -0.102861516365706, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5373 |
| Legacy p draw | 0.2367 |
| Legacy p away | 0.2260 |
| Legacy p over 1 5 | 0.8434 |
| Legacy p under 3 5 | 0.5947 |
| Legacy p btts yes | 0.6246 |
| Legacy p over 2 5 | 0.6274 |
| Legacy goal margin distribution | {"-1": 0.1304158817061956, "-10": 1.2008448759500345e-07, "-11": 1.3331649412775931e-08, "-12": 1.3604775991392389e-09, "-13": 1.284353292633819e-10, "-14": 1.1278401463214231e-11, "-15": 9.253072307551275e-13, "-16": 7.06719489178292e-14, "-17": 4.5130139066141116e-15, "-2": 0.0647753587166827, "-3": 0.022659888734523154, "-4": 0.006319950280779098, "-5": 0.0014581648529224283, "-6": 0.00028609068405654363, "-7": 4.874677939162247e-05, "-8": 7.333067057623966e-06, "-9": 9.868338720710702e-07, "0": 0.2366831983207141, "1": 0.2148431857779698, "10": 1.329909357846636e-05, "11": 2.3640275327527206e-06, "12": 3.862722902004795e-07, "13": 5.838753974125589e-08, "14": 8.20950053114033e-09, "15": 1.0784217913570884e-09, "16": 1.3188131845707776e-10, "17": 1.348454811667693e-11, "2": 0.16606451951687473, "3": 0.09301613994014324, "4": 0.04153820398782495, "5": 0.015345257917069343, "6": 0.004820641061997349, "7": 0.0013151658424459603, "8": 0.0003167770882719245, "9": 6.825675964966546e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.5373 |
| Legacy raw p draw | 0.2367 |
| Legacy raw p away | 0.2260 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.9915 |
| Legacy lambda away | 1.2438 |
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
| Dc lambda away | 1.5516 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:35:40.173016+00:00 |
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
| Goal margin distribution | {"-1": 0.19646074538569577, "-10": 9.96777150548499e-07, "-11": 1.329055402630267e-07, "-12": 1.6281994363165328e-08, "-13": 1.8439615541575256e-09, "-14": 1.9276296294226029e-10, "-15": 1.680962228687214e-11, "-2": 0.11763335801986512, "-3": 0.05043700676570169, "-4": 0.01711179361715371, "-5": 0.004781142182125527, "-6": 0.0011327616994780845, "-7": 0.0002326304430324806, "-8": 4.212277897487002e-05, "-9": 6.816638257708292e-06, "0": 0.2657099104994527, "1": 0.1837103469945719, "10": 5.248909956873866e-07, "11": 6.563889159734876e-08, "12": 7.54176261689032e-09, "13": 8.010584856468266e-10, "14": 7.853858299248049e-11, "15": 6.423393501423989e-12, "2": 0.10347244337123294, "3": 0.041609320119401494, "4": 0.013239877080573009, "5": 0.0034695023288690073, "6": 0.0007709410759547135, "7": 0.00014848968360639168, "8": 2.5217025303900965e-05, "9": 3.827314859171832e-06} |
| Raw goal margin distribution | {"-1": 0.19646074538569577, "-10": 9.96777150548499e-07, "-11": 1.329055402630267e-07, "-12": 1.6281994363165328e-08, "-13": 1.8439615541575256e-09, "-14": 1.9276296294226029e-10, "-15": 1.680962228687214e-11, "-2": 0.11763335801986512, "-3": 0.05043700676570169, "-4": 0.01711179361715371, "-5": 0.004781142182125527, "-6": 0.0011327616994780845, "-7": 0.0002326304430324806, "-8": 4.212277897487002e-05, "-9": 6.816638257708292e-06, "0": 0.2657099104994527, "1": 0.1837103469945719, "10": 5.248909956873866e-07, "11": 6.563889159734876e-08, "12": 7.54176261689032e-09, "13": 8.010584856468266e-10, "14": 7.853858299248049e-11, "15": 6.423393501423989e-12, "2": 0.10347244337123294, "3": 0.041609320119401494, "4": 0.013239877080573009, "5": 0.0034695023288690073, "6": 0.0007709410759547135, "7": 0.00014848968360639168, "8": 2.5217025303900965e-05, "9": 3.827314859171832e-06} |
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
| Legacy trial matrix | [[0.05931167353751746, 0.06662341874792514, 0.06330856786095934, 0.03427889553931661, 0.013920422453435364, 0.004522389843274881, 0.001224340829871182, 0.0002841121972430679, 5.768799938815225e-05, 1.0411865627422658e-05, 1.6912746549361637e-06, 2.497508883165447e-07, 3.3807369605393646e-08, 4.224288932949425e-09, 4.901298646783293e-10, 5.3076893064165036e-11], [0.056454341833917634, 0.12142369471556734, 0.08942069715042411, 0.04841750240511294, 0.019662012938729347, 0.0063876859994651146, 0.0017293300773642056, 0.0004012965638744265, 8.148187989074571e-05, 1.4706323559323736e-05, 2.3888545235991225e-06, 3.5276265601603067e-07, 4.775149179769406e-08, 5.966630965002447e-09, 6.922878794231359e-10, 7.496888558275196e-11], [0.0478676868800448, 0.0777549466230292, 0.063151492357473, 0.03419384583818264, 0.013885884357890094, 0.004511169297848011, 0.0012213031059297198, 0.00028340728370709, 5.754486913177186e-05, 1.0386032646344148e-05, 1.6870784169397324e-06, 2.491312289583573e-07, 3.372348981184059e-08, 4.213808008590622e-09, 4.889137987038608e-10, 5.294520346853471e-11], [0.022537033434887305, 0.03660853377274049, 0.029732944862993282, 0.016099124422988685, 0.006537743109061942, 0.002123945816534149, 0.0005750131398963485, 0.00013343363435553796, 2.7093238135340267e-05, 4.889945185633546e-06, 7.943091711351962e-07, 1.1729580438635575e-07, 1.5877671702314386e-08, 1.983942366293716e-09, 2.3019007907733597e-10, 2.4927626517184265e-11], [0.007958153649424147, 0.01292700467811409, 0.010499134429257687, 0.005684834525781564, 0.002308571992524935, 0.0007499960986375893, 0.00020304548648577916, 4.711735318982374e-05, 9.567015666210454e-06, 1.7267106266210426e-06, 2.8048209837836805e-07, 4.141885117383843e-08, 5.606636355543196e-09, 7.005588480925313e-10, 8.128345832041823e-11, 8.802306768206827e-12], [0.0022481116582027064, 0.00365177039835265, 0.002965917416429822, 0.0016059180728795757, 0.0006521522251045131, 0.00021186760739103297, 5.7358646920212504e-05, 1.3310257086750515e-05, 2.7026016838682113e-06, 4.877812695071748e-07, 7.92338402924898e-08, 1.1700478062522302e-08, 1.5838277456620666e-09, 1.9790199875920228e-10, 2.296189522332089e-11, 2.4865778340575595e-12], [0.0005292272398000077, 0.0008596620907382388, 0.0006982056616470755, 0.00037804865516976585, 0.00015352294480667413, 4.987568506816487e-05, 1.3502780556956737e-05, 3.1333633244360474e-06, 6.362185900392057e-07, 1.1482843120603991e-07, 1.8652412767732753e-08, 2.754405763955557e-09, 3.7284837836992586e-10, 4.658804564803937e-11, 5.405452342758758e-12, 5.853644852846124e-13], [0.00010678732602387775, 0.00017346237882374276, 0.00014088374523238675, 7.628255304424286e-05, 3.097781732741388e-05, 1.0063901933791382e-05, 2.7245873249258925e-06, 6.322491846872027e-07, 1.2837601107350917e-07, 2.3170049078810894e-08, 3.7636786876513085e-09, 5.557832329808315e-10, 7.523324263034812e-11, 9.400522961200015e-12, 1.0907106781783321e-12, 1.181146838860927e-13], [1.8854077462423065e-05, 3.06260419558379e-05, 2.487404774246112e-05, 1.346823839194138e-05, 5.469358483395836e-06, 1.776854929315345e-06, 4.81045667027963e-07, 1.1162818236483342e-07, 2.2665716496690037e-08, 4.090840331017978e-09, 6.645047887497593e-10, 9.812756360800212e-11, 1.3282975022566676e-11, 1.6597305569588017e-12, 1.9257288651340575e-13, 2.0854004705952267e-14], [2.95895485973945e-06, 4.8064444341242516e-06, 3.903727700049846e-06, 2.113702434997991e-06, 8.583599434316441e-07, 2.788592302449331e-07, 7.549520346704179e-08, 1.7518902919042952e-08, 3.5571526695498355e-09, 6.420156012410984e-10, 1.0428723855145029e-10, 1.5400118716547077e-11, 2.084627241675192e-12, 2.604777564513175e-13, 3.022234736961056e-14, 3.2728230109741238e-15], [4.1793996505440315e-07, 6.788901196724255e-07, 5.513851666815902e-07, 2.9855160477042727e-07, 1.2123974233034085e-07, 3.938769682817248e-08, 1.0663380887658707e-08, 2.474471568796091e-09, 5.024328970451899e-10, 9.068201127296463e-11, 1.4730135099002922e-11, 2.175202185677849e-12, 2.9444485564538285e-13, 3.679139074068165e-14, 4.268779823369559e-15, 4.622725251564726e-16], [5.3665697601033944e-08, 8.717307487434863e-08, 7.080076587788902e-08, 3.833560195141322e-08, 1.556782287685842e-08, 5.0575881799357465e-09, 1.369234392425827e-09, 3.177352108838916e-10, 6.451503606296364e-11, 1.1644048910697013e-11, 1.8914270994461308e-12, 2.793074424038399e-13, 3.780827368636144e-14, 4.724208773750292e-15, 5.481338619926565e-16, 5.935823232670352e-17], [6.316712274879445e-09, 1.0260692708989847e-08, 8.333592720932242e-09, 4.512285840605916e-09, 1.8324080791881113e-09, 5.953026004616739e-10, 1.611655131760867e-10, 3.7398971716954235e-11, 7.593731907537172e-12, 1.3705608977694417e-12, 2.2263012147783603e-13, 3.2875837429969923e-14, 4.450216752274913e-15, 5.560622312616077e-16, 6.45180077610578e-17, 6.986751156031001e-18], [6.863147066248779e-10, 1.1148306270563492e-09, 9.054500180644981e-10, 4.902626553402963e-10, 1.9909227436024798e-10, 6.467999677833643e-11, 1.751073296996179e-11, 4.0634214738684485e-12, 8.250636817882945e-13, 1.489122916370472e-13, 2.418890078554956e-14, 3.571980128100358e-15, 4.835188103945995e-16, 6.041650632579568e-17, 7.009921560721565e-18, 7.591148466555662e-19], [6.924219580895753e-11, 1.1247510774186358e-10, 9.13507270656722e-11, 4.946253147602552e-11, 2.0086392018461925e-11, 6.5255559273570875e-12, 1.766655426964607e-12, 4.099580303787752e-13, 8.32405607191365e-14, 1.502374050324518e-14, 2.4404148540443893e-15, 3.6037658098854564e-16, 4.8782145892374595e-17, 6.095412965396923e-18, 7.072300165326537e-19, 7.65869918657316e-20], [6.520113186008316e-12, 1.0591091523278367e-11, 8.601938068741661e-12, 4.6575834275963996e-12, 1.8914124245892763e-12, 6.144716058021304e-13, 1.663551135245043e-13, 3.8603235041209664e-14, 7.838253412023603e-15, 1.4146935609702885e-15, 2.297989092241779e-16, 3.3934453842494135e-17, 4.593515687344891e-18, 5.739676794696508e-19, 6.659551596338751e-20, 7.211727613581385e-21]] |
| Legacy trial inputs | {"lambda_home": 1.4124580632879458, "lambda_away": 1.62437234157316, "rho": -0.102861516365706, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3225 |
| Legacy p draw | 0.2625 |
| Legacy p away | 0.4150 |
| Legacy p over 1 5 | 0.8176 |
| Legacy p under 3 5 | 0.6390 |
| Legacy p btts yes | 0.6187 |
| Legacy p over 2 5 | 0.5850 |
| Legacy goal margin distribution | {"-1": 0.19758632552782832, "-10": 2.079828513166483e-06, "-11": 3.019551805086749e-07, "-12": 4.028784199561714e-08, "-13": 4.969522015841096e-09, "-14": 5.650987502610812e-10, "-15": 5.3076893064165036e-11, "-2": 0.1279529162529123, "-3": 0.05907702956302344, "-4": 0.021672919211865236, "-5": 0.006564029218277852, "-6": 0.0016883647730842018, "-7": 0.0003768174693298228, "-8": 7.42045072307234e-05, "-9": 1.3066453157790253e-05, "0": 0.26252058298595016, "1": 0.17033193562116108, "10": 5.139575961686486e-07, "11": 6.488319427198891e-08, "12": 7.527551212429063e-09, "13": 8.073917524354831e-10, "14": 7.983328733223589e-11, "15": 6.520113186008316e-12, "2": 0.09674535908053616, "3": 0.03884083689244291, "4": 0.012390171469042975, "5": 0.003263024887679214, "6": 0.0007298038314453097, "7": 0.0001416318283385425, "8": 2.425214155851495e-05, "9": 3.7133638153157714e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3225 |
| Legacy raw p draw | 0.2625 |
| Legacy raw p away | 0.4150 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.4125 |
| Legacy lambda away | 1.6244 |
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

The model's most likely 1X2 outcome is **Hull City win** at **39.7%**. Expected goals are 1.31 for Hull City and 1.12 for Brentford (2.43 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 43.8%; Under 3.5 goals: 77.2%; Double Chance 1X: 69.0%; Double Chance X2: 60.3%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 39.7% | 2.52 |
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
| Dc lambda home | 1.2138 |
| Dc lambda away | 1.0437 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:35:40.173016+00:00 |
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
| Fair Under 0.5 odds | 10.24 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.39 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 10.01 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.1818925865072447, "-10": 8.965782509971173e-08, "-11": 9.067568265671422e-09, "-12": 8.41892918919858e-10, "-13": 7.192898117625919e-11, "-14": 5.229772392204768e-12, "-2": 0.08837355395583074, "-3": 0.02973055600514758, "-4": 0.007811871721952481, "-5": 0.0016778183067504154, "-6": 0.0003041490780677295, "-7": 4.7645092913224154e-05, "-8": 6.566775403802296e-06, "-9": 8.076587591804744e-07, "0": 0.2926656061976558, "1": 0.21290050684713557, "10": 4.0159002655656775e-07, "11": 4.71851157497174e-08, "12": 5.0896804853033905e-09, "13": 5.051926734064664e-10, "14": 4.267321803080103e-11, "2": 0.11927825155236974, "3": 0.046618838282177895, "4": 0.01423092044269544, "5": 0.0035509314480885, "6": 0.0007478307790193697, "7": 0.00013609885813244008, "8": 2.1792544326842254e-05, "9": 3.1138891948907635e-06} |
| Raw goal margin distribution | {"-1": 0.1818925865072447, "-10": 8.965782509971173e-08, "-11": 9.067568265671422e-09, "-12": 8.41892918919858e-10, "-13": 7.192898117625919e-11, "-14": 5.229772392204768e-12, "-2": 0.08837355395583074, "-3": 0.02973055600514758, "-4": 0.007811871721952481, "-5": 0.0016778183067504154, "-6": 0.0003041490780677295, "-7": 4.7645092913224154e-05, "-8": 6.566775403802296e-06, "-9": 8.076587591804744e-07, "0": 0.2926656061976558, "1": 0.21290050684713557, "10": 4.0159002655656775e-07, "11": 4.71851157497174e-08, "12": 5.0896804853033905e-09, "13": 5.051926734064664e-10, "14": 4.267321803080103e-11, "2": 0.11927825155236974, "3": 0.046618838282177895, "4": 0.01423092044269544, "5": 0.0035509314480885, "6": 0.0007478307790193697, "7": 0.00013609885813244008, "8": 2.1792544326842254e-05, "9": 3.1138891948907635e-06} |
| Unadjusted home-win probability | 39.7% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 70.8% |
| Raw p under 3 5 | 77.2% |
| Raw p btts yes | 50.2% |
| P home draw | 69.0% |
| P draw away | 60.3% |
| P home away | 70.7% |
| Raw p home draw | 69.0% |
| Raw p draw away | 60.3% |
| Raw p home away | 70.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4385 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.11992413201367425, 0.10105525056906792, 0.062010461134600035, 0.022336233005941016, 0.006034150880761389, 0.001304104477853855, 0.00023486989895307958, 3.625730718732342e-05, 4.897469999534653e-06, 5.880246066426746e-07, 6.354212363630872e-08, 6.2421653024237925e-09, 5.621086188743995e-10, 4.672433373871282e-11], [0.10967279793776906, 0.1470479128816565, 0.07204006760564702, 0.02594890775462468, 0.007010117800110578, 0.0015150310613800384, 0.0002728578870327162, 4.21215842163135e-05, 5.689589520988814e-06, 6.831320335511242e-07, 7.381946205221663e-08, 7.251776590019944e-09, 6.530243795080237e-10, 5.428155346336462e-11], [0.07167221264404519, 0.07744921803728516, 0.041845934102644915, 0.0150729492631753, 0.004071969075889803, 0.0008800365139163153, 0.00015849503671569223, 2.446717633669595e-05, 3.304913447190242e-06, 3.968110942908854e-07, 4.287953144962919e-08, 4.21234148438376e-09, 3.793224529146792e-10, 3.1530541054615823e-11], [0.02775483872587195, 0.029991965878680586, 0.016204706252345217, 0.005836952153275525, 0.0015768572062836853, 0.00034079136970323803, 6.1376704033717e-05, 9.474837014940229e-06, 1.279817328722469e-06, 1.536638471227012e-07, 1.6604963571252212e-08, 1.6312159795876612e-09, 1.4689142580313223e-10, 1.221010276683645e-11], [0.008060980444314114, 0.008710720779984827, 0.0047064161134629575, 0.001695256010192255, 0.00045797474194940555, 9.897778884256585e-05, 1.782595156970074e-05, 2.7518256057925354e-06, 3.7170392381020926e-07, 4.462938080413053e-08, 4.822664903530518e-09, 4.737624398318579e-10, 4.2662431676560463e-11, 3.546242894749234e-12], [0.00187295358089884, 0.0020239195206819154, 0.0010935268946258411, 0.00039388953201957897, 0.00010640956628301883, 2.2997302291297954e-05, 4.141826178098502e-06, 6.393814819404133e-07, 8.63647046341045e-08, 1.0369552335206856e-08, 1.1205370814308187e-09, 1.1007780806667745e-10, 9.912535420530335e-12, 8.239628385580074e-13], [0.0003626476891195197, 0.0003918782315934102, 0.00021173242378798958, 7.626624066503464e-05, 2.0603384785557786e-05, 4.4528164589748495e-06, 8.019545746036725e-07, 1.2379923307027666e-07, 1.6722229998896855e-08, 2.0077882494888127e-09, 2.1696222869474596e-10, 2.1313642327198013e-11, 1.9192990687177466e-12, 1.5953850771892688e-13], [6.018607543490479e-05, 6.503726210207517e-05, 3.5139734823787285e-05, 1.2657369263670046e-05, 3.4193982427646607e-06, 7.390024956406674e-07, 1.330947362153359e-07, 2.0546084268292056e-08, 2.77527039699882e-09, 3.332184339418828e-10, 3.600768860392053e-11, 3.5372746701125272e-12, 3.1853250964441666e-13, 2.6477479240682245e-14], [8.7400755935313e-06, 9.444553130619732e-06, 5.102906884645102e-06, 1.8380724009719742e-06, 4.965567020310983e-07, 1.0731614628525638e-07, 1.932769410893528e-08, 2.983652420569576e-09, 4.0301802180961025e-10, 4.8389171095897e-11, 5.228949023050697e-12, 5.136744303141135e-13, 4.6256516863282055e-14, 3.844995182316038e-15], [1.12818892009164e-06, 1.2191244896174746e-06, 6.586948757945356e-07, 2.3726258370552306e-07, 6.409667324197439e-08, 1.3852613274371247e-08, 2.494862900357494e-09, 3.851366691590781e-10, 5.2022486755076925e-11, 6.246184726733294e-12, 6.749646829022789e-13, 6.630626870592325e-14, 5.970896847369473e-15, 4.963207601665641e-16], [1.3106628234698708e-07, 1.4163063625846584e-07, 7.652325513388982e-08, 2.7563756594771206e-08, 7.446370481951553e-09, 1.6093142649503112e-09, 2.8983834133800714e-10, 4.474288882227425e-11, 6.0436632695164816e-12, 7.256446118252662e-13, 7.841338460967061e-14, 7.703068148267068e-15, 6.936633024179098e-16, 5.76595955944845e-17], [1.384227415875829e-08, 1.4958004921348288e-08, 8.081833543425143e-09, 2.9110849014546395e-09, 7.864318713639622e-10, 1.699641499258171e-10, 3.061063235088157e-11, 4.725420776741817e-12, 6.382880661739295e-13, 7.663734317357765e-14, 8.2814553678242e-15, 8.135424249664959e-16, 7.325970824836702e-17, 6.089590059394354e-18], [1.3400942732984055e-09, 1.4481100796855144e-09, 7.824161496210769e-10, 2.818271160347227e-10, 7.613581663439129e-11, 1.6454520505036064e-11, 2.9634677542854757e-12, 4.57476080101354e-13, 6.179376108175036e-14, 7.419392473362831e-15, 8.017418803958354e-16, 7.876043576937046e-17, 7.092397850322255e-18, 5.895436451940144e-19], [1.197570666427329e-10, 1.2940986225697778e-10, 6.992035175398228e-11, 2.518538388618577e-11, 6.803851227676563e-12, 1.4704526002082449e-12, 2.6482928284593087e-13, 4.088219351710833e-14, 5.522178335825514e-15, 6.630314721770705e-16, 7.164738907846527e-17, 7.038399419488365e-18, 6.33809709467123e-19, 5.268436632635168e-20]] |
| Legacy trial inputs | {"lambda_home": 1.1617405561503034, "lambda_away": 1.0806031400471903, "rho": -0.102861516365706, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3627 |
| Legacy p draw | 0.3151 |
| Legacy p away | 0.3222 |
| Legacy p over 1 5 | 0.6693 |
| Legacy p under 3 5 | 0.8110 |
| Legacy p btts yes | 0.4676 |
| Legacy p over 2 5 | 0.3886 |
| Legacy goal margin distribution | {"-1": 0.18984837088276998, "-10": 7.118543278201019e-08, "-11": 6.926720222986432e-09, "-12": 6.163901723377641e-10, "-13": 4.672433373871282e-11, "-2": 0.09239061172861378, "-3": 0.030290604258627694, "-4": 0.007717534109894461, "-5": 0.001602755130105895, "-6": 0.0002804549951521942, "-7": 4.236079660068813e-05, "-8": 5.6251562669095104e-06, "-9": 6.662068478479729e-07, "0": 0.3151367261054942, "1": 0.20513297675147885, "10": 1.4683188880184265e-07, "11": 1.536030459019779e-08, "12": 1.4695041355553834e-09, "13": 1.197570666427329e-10, "2": 0.1067858462744414, "3": 0.03763888189578827, "4": 0.010309800461989213, "5": 0.002301875356778147, "6": 0.0004330327400289274, "7": 7.031769034913498e-05, "8": 1.0038712029453354e-05, "9": 1.2781900208607933e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3627 |
| Legacy raw p draw | 0.3151 |
| Legacy raw p away | 0.3222 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.1617 |
| Legacy lambda away | 1.0806 |
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
| Dc lambda home | 1.9066 |
| Dc lambda away | 1.2771 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:35:40.173016+00:00 |
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
| Goal margin distribution | {"-1": 0.14503847900644437, "-10": 1.7212239562637082e-07, "-11": 1.9659450523213233e-08, "-12": 2.0638276772789702e-09, "-13": 2.0041006889864751e-10, "-14": 1.8093423427398336e-11, "-15": 1.5137669241854779e-12, "-16": 1.0528442562512165e-13, "-2": 0.07306909624582826, "-3": 0.026417940348981803, "-4": 0.00760226778433892, "-5": 0.0018079557491445944, "-6": 0.00036539142970454426, "-7": 6.410434011038531e-05, "-8": 9.926209702717081e-06, "-9": 1.374685926765643e-06, "0": 0.24170199654353566, "1": 0.21520051325152487, "10": 7.527909640960959e-06, "11": 1.25456189435476e-06, "12": 1.921665755208236e-07, "13": 2.7227493151905894e-08, "14": 3.586679482991222e-09, "15": 4.378390924265987e-10, "16": 4.4432766765849095e-11, "2": 0.15556114780165337, "3": 0.08206350457753964, "4": 0.03445704018962854, "5": 0.011956561564661924, "6": 0.0035258234833338933, "7": 0.0009025543106495205, "8": 0.00020391682397284097, "9": 4.1205652965678044e-05} |
| Raw goal margin distribution | {"-1": 0.14503847900644437, "-10": 1.7212239562637082e-07, "-11": 1.9659450523213233e-08, "-12": 2.0638276772789702e-09, "-13": 2.0041006889864751e-10, "-14": 1.8093423427398336e-11, "-15": 1.5137669241854779e-12, "-16": 1.0528442562512165e-13, "-2": 0.07306909624582826, "-3": 0.026417940348981803, "-4": 0.00760226778433892, "-5": 0.0018079557491445944, "-6": 0.00036539142970454426, "-7": 6.410434011038531e-05, "-8": 9.926209702717081e-06, "-9": 1.374685926765643e-06, "0": 0.24170199654353566, "1": 0.21520051325152487, "10": 7.527909640960959e-06, "11": 1.25456189435476e-06, "12": 1.921665755208236e-07, "13": 2.7227493151905894e-08, "14": 3.586679482991222e-09, "15": 4.378390924265987e-10, "16": 4.4432766765849095e-11, "2": 0.15556114780165337, "3": 0.08206350457753964, "4": 0.03445704018962854, "5": 0.011956561564661924, "6": 0.0035258234833338933, "7": 0.0009025543106495205, "8": 0.00020391682397284097, "9": 4.1205652965678044e-05} |
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
| Legacy trial matrix | [[0.05709437036654913, 0.0534391839297412, 0.04534217235360221, 0.02122836611615252, 0.007454046165571688, 0.0020939078941622983, 0.0004901644659207405, 9.835111426460417e-05, 1.726731445445425e-05, 2.6947457084270516e-06, 3.7848902369942666e-07, 4.8327697527336435e-08, 5.656533440106975e-09, 6.11142528951829e-10, 6.131263369325868e-11, 5.741088121829418e-12], [0.06588323676665458, 0.11928833657499377, 0.07595957125325604, 0.03556286575806262, 0.012487406788171241, 0.0035078236799949113, 0.0008211490703303882, 0.00016476291461200396, 2.892710548640694e-05, 4.51437851394451e-06, 6.340645467990657e-07, 8.096107868863232e-08, 9.47611974872872e-09, 1.023817829277947e-09, 1.0271412078424319e-10, 9.617770160204475e-12], [0.06450474834759272, 0.09059978887695677, 0.06362571713571744, 0.029788383477230212, 0.010459777470489127, 0.002938244562771417, 0.0006878158685349222, 0.00013800971262209913, 2.4230097680472272e-05, 3.7813611324126782e-06, 5.311089943611933e-07, 6.781511015209519e-08, 7.937444942475957e-09, 8.575765045718394e-10, 8.603602530974049e-11, 8.056095019931838e-12], [0.03602057256301012, 0.05059249672365567, 0.03552970625682932, 0.016634351052644422, 0.005840921529348975, 0.0016407668302317708, 0.00038408833515705986, 7.706702212241119e-05, 1.3530507661314617e-05, 2.111577775996395e-06, 2.9658049306952527e-07, 3.7869136128382875e-08, 4.432407207833452e-09, 4.788856247420014e-10, 4.804401182999325e-11, 4.498663473210631e-12], [0.015085885314699071, 0.02118879709705473, 0.014880304107267131, 0.006966683048295971, 0.002446254072440869, 0.0006871745357667446, 0.00016086120132480464, 3.2276673427395256e-05, 5.666752977654274e-06, 8.843562968363578e-07, 1.2421177640075438e-07, 1.5860087831756843e-08, 1.8563499147175452e-09, 2.0056354187813967e-10, 2.0121458404290162e-11, 1.88409890230268e-12], [0.005054532330492967, 0.0070993155348307805, 0.004985652258967165, 0.0023341901366304867, 0.0008196184738130568, 0.00023023812227580833, 5.389661434227747e-05, 1.0814313244219895e-05, 1.8986480101742825e-06, 2.9630395570348217e-07, 4.161720883784275e-08, 5.313929215142795e-09, 6.21970833326255e-10, 6.719890053475852e-11, 6.74170324906668e-12, 6.312681434914628e-13], [0.0014112693502926989, 0.0019821905900018933, 0.0013920374357585105, 0.0006517261701362694, 0.00022884460032986537, 6.428448449653123e-05, 1.5048403083096654e-05, 3.019450233597269e-06, 5.301190235916157e-07, 8.273063929814184e-08, 1.1619886358873024e-08, 1.483695214632162e-09, 1.736596615583907e-10, 1.8762516984201988e-11, 1.882342132184676e-12, 1.7625555134965112e-13], [0.00033774742839244956, 0.0004743812895943648, 0.00033314481325336337, 0.0001559722372869021, 5.476748662250729e-05, 1.5384674314463527e-05, 3.6014099233961082e-06, 7.226200663572469e-07, 1.268690040798024e-07, 1.9799240071652884e-08, 2.7808913550825037e-09, 3.550805118500338e-10, 4.1560531371764616e-11, 4.49027810337522e-12, 4.504853835083134e-13, 4.2181784218506157e-14], [7.072651276086824e-05, 9.93385338023288e-05, 6.97626951533817e-05, 3.2661603030757115e-05, 1.1468668643678226e-05, 3.221651070454254e-06, 7.541587100057004e-07, 1.513213515428733e-07, 2.6567196318020534e-08, 4.146089911767205e-09, 5.823367741035561e-10, 7.435617340457141e-11, 8.703046138364876e-12, 9.40293500056489e-13, 9.433457532728803e-14, 8.83314053346338e-15], [1.31649713149972e-05, 1.849078792281578e-05, 1.2985567147307625e-05, 6.0796022625287495e-06, 2.1347679649599362e-06, 5.996753165656801e-07, 1.4037844362197357e-07, 2.816682421688337e-08, 4.945194719683022e-09, 7.717495551118766e-10, 1.0839565853702084e-10, 1.3840593177184712e-11, 1.6199774072285848e-12, 1.7502541087775853e-13, 1.755935546257157e-14, 1.6441930643118692e-15], [2.2054646364316877e-06, 3.0976732032125213e-06, 2.1754099148526836e-06, 1.018486669872405e-06, 3.5762746010262625e-07, 1.0046073571918498e-07, 2.3516928804310725e-08, 4.718653253741415e-09, 8.284448035298995e-10, 1.292875093500721e-10, 1.815900588965126e-11, 2.3186483334563246e-12, 2.7138706176981125e-13, 2.9321169407189444e-14, 2.941634781013073e-15, 2.7544379490407195e-16], [3.3588266828888996e-07, 4.717621510655502e-07, 3.313054649586346e-07, 1.5511108844932286e-07, 5.446510615876261e-08, 1.5299732951610175e-08, 3.581525936199886e-09, 7.186303599775767e-10, 1.261685390657166e-10, 1.968992515209259e-11, 2.7655375882870807e-12, 3.5312005289050605e-13, 4.1331068719291813e-14, 4.4654865261279415e-15, 4.479981782780579e-16, 4.1948891525045795e-17], [4.689067989445524e-08, 6.586004608284237e-08, 4.6251682421723954e-08, 2.1654181901109752e-08, 7.603565469211607e-09, 2.1359091969805328e-09, 4.999965823291423e-10, 1.003239206828115e-10, 1.7613676252545347e-11, 2.748799103437085e-12, 3.8608106351268557e-13, 4.9297093680821856e-14, 5.769996775615555e-15, 6.234013214685249e-16, 6.254249222787407e-17, 5.856247523722592e-18], [6.042593217260445e-09, 8.487091009224254e-09, 5.9602484569954275e-09, 2.790478043301782e-09, 9.798376401167677e-10, 2.752451117238959e-10, 6.443233418316762e-11, 1.2928297137329758e-11, 2.2697960638279715e-12, 3.5422550612247825e-13, 4.9752548287753e-14, 6.35269705145843e-15, 7.435538034088523e-16, 8.033495366703661e-17, 8.059572609681957e-18, 7.546685534331283e-19], [7.230619440321889e-10, 1.0155726694920596e-09, 7.132084986160696e-10, 3.3391102234144643e-10, 1.1724822165340962e-10, 3.293606873948522e-11, 7.7100289789381e-12, 1.547011245840831e-12, 2.7160576518373385e-13, 4.238693121871713e-14, 5.953433069553504e-15, 7.601692377296271e-16, 8.897429286644629e-17, 9.612950215860885e-18, 9.644154470929765e-19, 9.030429349217573e-20], [8.075407125756094e-11, 1.1342268583802306e-10, 7.96536042231206e-11, 3.729234364275406e-11, 1.3094688946594926e-11, 3.678414641905025e-12, 8.610828362656989e-13, 1.7277559331392105e-13, 3.0333875951622756e-14, 4.7339198145840165e-15, 6.649000992153463e-16, 8.489834280186002e-17, 9.936958300087553e-18, 1.0736076945192647e-18, 1.0770926941906886e-19, 1.00854973930231e-20]] |
| Legacy trial inputs | {"lambda_home": 1.6752521396831892, "lambda_away": 1.4045444901009045, "rho": -0.102861516365706, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4290 |
| Legacy p draw | 0.2593 |
| Legacy p away | 0.3117 |
| Legacy p over 1 5 | 0.8236 |
| Legacy p under 3 5 | 0.6294 |
| Legacy p btts yes | 0.6244 |
| Legacy p over 2 5 | 0.5944 |
| Legacy goal margin distribution | {"-1": 0.1657722819157693, "-10": 4.678871856818248e-07, "-11": 5.8711321891369294e-08, "-12": 6.770885958167874e-09, "-13": 7.21912744756004e-10, "-14": 7.093040385346315e-11, "-15": 5.741088121829418e-12, "-2": 0.0931778084416717, "-3": 0.03707236671122639, "-4": 0.011732727777005217, "-5": 0.0030675246844956484, "-6": 0.0006813987599407474, "-7": 0.00013137266265699388, "-8": 2.2352596572227503e-05, "-9": 3.4012652540867242e-06, "0": 0.25933506570523474, "1": 0.19986707571561899, "10": 2.726389874598559e-06, "11": 4.080499685400158e-07, "12": 5.6128271745938316e-08, "13": 7.1378194909756244e-09, "14": 8.36484629870212e-10, "15": 8.075407125756094e-11, "2": 0.13255675176385182, "3": 0.06290488245292598, "4": 0.023745303120068617, "5": 0.007404768249642365, "6": 0.0019618663776972472, "7": 0.00045114668303699343, "8": 9.155570838037155e-05, "9": 1.6616617799861153e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.4290 |
| Legacy raw p draw | 0.2593 |
| Legacy raw p away | 0.3117 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.6753 |
| Legacy lambda away | 1.4045 |
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
| Bbs statistics cutoff utc | 2026-10-26T11:35:40.173016+00:00 |
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
| Goal margin distribution | {"-1": 0.16105725185653263, "-10": 2.78645152184313e-07, "-11": 3.310161753437839e-08, "-12": 3.6137744531623783e-09, "-13": 3.6490129088311644e-10, "-14": 3.425591668751697e-11, "-15": 2.9821033765548797e-12, "-16": 2.169087965254453e-13, "-2": 0.08502750977732983, "-3": 0.032162824084802526, "-4": 0.009662223024619103, "-5": 0.0023957099988094455, "-6": 0.0005043802514766612, "-7": 9.212978536705019e-05, "-8": 1.4847081526351373e-05, "-9": 2.1393638429872738e-06, "0": 0.2531991203634496, "1": 0.20937301815680784, "10": 3.4303497973954387e-06, "11": 5.237991920972455e-07, "12": 7.350304702252407e-08, "13": 9.540000353810006e-09, "14": 1.1511642036577076e-09, "15": 1.2881103469814414e-10, "16": 1.2043042824820779e-11, "2": 0.14048075841866733, "3": 0.06830307408596813, "4": 0.026374960882373677, "5": 0.008405773889758567, "6": 0.0022747319289896082, "7": 0.0005340733417816677, "8": 0.00011062941764046172, "9": 2.049004330103964e-05} |
| Raw goal margin distribution | {"-1": 0.16105725185653263, "-10": 2.78645152184313e-07, "-11": 3.310161753437839e-08, "-12": 3.6137744531623783e-09, "-13": 3.6490129088311644e-10, "-14": 3.425591668751697e-11, "-15": 2.9821033765548797e-12, "-16": 2.169087965254453e-13, "-2": 0.08502750977732983, "-3": 0.032162824084802526, "-4": 0.009662223024619103, "-5": 0.0023957099988094455, "-6": 0.0005043802514766612, "-7": 9.212978536705019e-05, "-8": 1.4847081526351373e-05, "-9": 2.1393638429872738e-06, "0": 0.2531991203634496, "1": 0.20937301815680784, "10": 3.4303497973954387e-06, "11": 5.237991920972455e-07, "12": 7.350304702252407e-08, "13": 9.540000353810006e-09, "14": 1.1511642036577076e-09, "15": 1.2881103469814414e-10, "16": 1.2043042824820779e-11, "2": 0.14048075841866733, "3": 0.06830307408596813, "4": 0.026374960882373677, "5": 0.008405773889758567, "6": 0.0022747319289896082, "7": 0.0005340733417816677, "8": 0.00011062941764046172, "9": 2.049004330103964e-05} |
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
| Legacy trial matrix | [[0.05914912341697958, 0.05471175398707289, 0.045471405487074526, 0.020890164101213738, 0.007197912921885946, 0.001984089744054907, 0.0004557585135192702, 8.973491961714412e-05, 1.5459527611348683e-05, 2.3674370392335153e-06, 3.262895508888842e-07, 4.088228948740706e-08, 4.695465903665699e-09, 4.978059315529412e-10, 4.900684674862563e-11, 4.50287849999635e-12], [0.06824438263456246, 0.1208670224993164, 0.07552340699569365, 0.03469645041148469, 0.011955005597389746, 0.0032953724577269696, 0.0007569688101691154, 0.00014904062857476114, 2.567671228207217e-05, 3.932073555578498e-06, 5.419339535750232e-07, 6.790134931612943e-08, 7.798694117289798e-09, 8.268053201968881e-10, 8.139541747008709e-11, 7.478825911903037e-12], [0.06603517188635664, 0.09101228974877221, 0.06271837150336733, 0.028813648024111786, 0.009928027775874565, 0.002736640232047127, 0.0006286243290819174, 0.00012377070743882423, 2.1323211491026907e-05, 3.265388306057228e-06, 4.500487515419556e-07, 5.638863792561359e-08, 6.476421209615139e-09, 6.866200201485326e-10, 6.759477934902596e-11, 6.210786835642761e-12], [0.03655924794188542, 0.05038740373706111, 0.03472295791474459, 0.015952185360198344, 0.005496483444561365, 0.001515094243160753, 0.0003480271505730032, 6.852354361984221e-05, 1.1805232780484e-05, 1.8078266066018106e-06, 2.4916182427561376e-07, 3.121860875255232e-08, 3.5855602706067075e-09, 3.801354769193671e-10, 3.7422698044171333e-11, 3.4384963247952763e-12], [0.015180303600667999, 0.020922095760664988, 0.014417830582755064, 0.006623741747830213, 0.0022822758158789385, 0.0006291045874730435, 0.00014450947720182026, 2.84526694202336e-05, 4.901824511520934e-06, 7.506543020032808e-07, 1.0345814947322038e-07, 1.2962738172501242e-08, 1.4888132702517537e-09, 1.5784164811578227e-10, 1.553882943023549e-11, 1.4277486840852533e-12], [0.005042589886417002, 0.006949897133858033, 0.004789311768275517, 0.0022002730661050108, 0.0007581258748118069, 0.00020897582246975045, 4.8003126116479064e-05, 9.451401423468418e-06, 1.6282869800903538e-06, 2.4935217970940916e-07, 3.4366705167749265e-08, 4.305959493856896e-09, 4.945536622208633e-10, 5.243180369653546e-11, 5.16168491704055e-12, 4.742692415187712e-13], [0.0013958719926104389, 0.0019238460749718292, 0.0013257604349747282, 0.0006090718496350662, 0.00020986173759116134, 5.784795200260178e-05, 1.3288056497362888e-05, 2.6163036921712083e-06, 4.507366735420447e-07, 6.902479317032957e-08, 9.513270423038043e-09, 1.1919605587954434e-09, 1.3690060494440506e-10, 1.4513987445059888e-11, 1.4288394600133084e-12, 1.3128554296590724e-13], [0.00033120032086279085, 0.00045647340207012436, 0.00031456486251985814, 0.00014451525146684776, 4.979416106560805e-05, 1.372565705590743e-05, 3.152874044946697e-06, 6.207737005318925e-07, 1.0694686310209143e-07, 1.6377600357714895e-08, 2.257225757981108e-09, 2.8281799593282416e-10, 3.2482580439989585e-11, 3.4437522382067768e-12, 3.3902255373204163e-13, 3.115028755153849e-14], [6.876128074800513e-05, 9.476952097140054e-05, 6.530755395658688e-05, 3.0003152631597794e-05, 1.0337883368362176e-05, 2.849616074686962e-06, 6.545756260226939e-07, 1.2888029393224857e-07, 2.220349080497389e-08, 3.4001922861723326e-09, 4.686279700811875e-10, 5.871651201383208e-11, 6.74378523316435e-12, 7.149655346378937e-13, 7.038527298629058e-14, 6.467184760366776e-15], [1.268950389041235e-05, 1.748917693180098e-05, 1.2052138223581099e-05, 5.536911440590658e-06, 1.9077976703519557e-06, 5.258804645951979e-07, 1.207982146729437e-07, 2.378412637839358e-08, 4.097528142080528e-09, 6.274861778921364e-10, 8.648263070163645e-11, 1.0835798861302938e-11, 1.2445272691467001e-12, 1.3194282937438607e-13, 1.2989202435895314e-14, 1.1934822226107316e-15], [2.1075982952879406e-06, 2.9047754589762087e-06, 2.001738302297706e-06, 9.196250077330611e-07, 3.1686590370377566e-07, 8.734342810229859e-08, 2.0063362091790153e-08, 3.950302915143071e-09, 6.805579951528472e-10, 1.0421910976688603e-10, 1.4363890551820663e-11, 1.7997166323752132e-12, 2.067033962513492e-13, 2.191436991284041e-14, 2.157375193503592e-15, 1.9822533012747297e-16], [3.182279703304308e-07, 4.3859439469197104e-07, 3.0224408441450783e-07, 1.3885492331735674e-07, 4.784383894597621e-08, 1.3188054815208041e-08, 3.0293832609133916e-09, 5.964594304744483e-10, 1.0275800183262604e-10, 1.5736127631584295e-11, 2.1688154457962542e-12, 2.717406691641098e-13, 3.121031289337179e-14, 3.3088684281179423e-15, 3.257438244302971e-16, 2.9930202835890595e-17], [4.404537361307648e-08, 6.070507868541589e-08, 4.183307207897625e-08, 1.921866569169776e-08, 6.621981591596978e-09, 1.8253354692939893e-09, 4.192916084830112e-10, 8.255490060478097e-11, 1.4222554283181463e-11, 2.1780097457696923e-12, 3.001819309242921e-13, 3.7611148029422895e-14, 4.319764508890265e-15, 4.579746588637037e-16, 4.508562975871401e-17, 4.142586727537258e-18], [5.627300941236274e-09, 7.75576907180201e-09, 5.344654082238019e-09, 2.455404658074873e-09, 8.460339914605652e-10, 2.3320751220465273e-10, 5.3569305230468566e-11, 1.0547334073221006e-11, 1.8170942039817289e-12, 2.7826569028700056e-13, 3.8351679730805743e-14, 4.805254930204804e-15, 5.518993913036155e-16, 5.851150796280127e-17, 5.760205578143133e-18, 5.292629004763944e-19], [6.675984213435947e-10, 9.201105899097319e-10, 6.340664317031925e-10, 2.912984911609098e-10, 1.0036977993538925e-10, 2.7666721332143574e-11, 6.355228550559299e-12, 1.2512896769155042e-12, 2.1557212501670325e-13, 3.301222690764341e-14, 4.549875883932405e-15, 5.700744707023761e-16, 6.547493482618677e-17, 6.941549910749511e-18, 6.833656473574162e-19, 6.278944035933291e-20], [7.392089855846757e-11, 1.0188071062601178e-10, 7.02080155955583e-11, 3.225448941596254e-11, 1.1113603752997863e-11, 3.0634417872390285e-12, 7.036928039109094e-13, 1.3855104253897454e-13, 2.386956690718649e-14, 3.6553314064430206e-15, 5.037922543209325e-16, 6.312240378692255e-17, 7.249816447540443e-18, 7.68614170414526e-19, 7.566674977299023e-20, 6.952460795224634e-21]] |
| Legacy trial inputs | {"lambda_home": 1.660898892099598, "lambda_away": 1.3782396130565087, "rho": -0.102861516365706, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4310 |
| Legacy p draw | 0.2612 |
| Legacy p away | 0.3078 |
| Legacy p over 1 5 | 0.8179 |
| Legacy p under 3 5 | 0.6385 |
| Legacy p btts yes | 0.6172 |
| Legacy p over 2 5 | 0.5855 |
| Legacy goal margin distribution | {"-1": 0.1652251269040908, "-10": 4.0106346999021985e-07, "-11": 4.9406454071573654e-08, "-12": 5.593304499536409e-09, "-13": 5.854121358586709e-10, "-14": 5.648567266052867e-11, "-15": 4.50287849999635e-12, "-2": 0.09176540639016754, "-3": 0.035959989379626155, "-4": 0.011195594231972241, "-5": 0.0028774207406217943, "-6": 0.0006280380847165631, "-7": 0.00011893965418086103, "-8": 1.9874411232285383e-05, "-9": 2.9695083256233346e-06, "0": 0.2611918860940252, "1": 0.20142263183101702, "10": 2.5905845999386853e-06, "11": 3.845801151929986e-07, "12": 5.2467463605997647e-08, "13": 6.617619546741565e-09, "14": 7.694791319696064e-10, "15": 7.392089855846757e-11, "2": 0.13326494572327646, "3": 0.06293249595109382, "4": 0.02361136085912752, "5": 0.007313002231427513, "6": 0.0019235203440944298, "7": 0.0004389913290843853, "8": 8.839791258830457e-05, "9": 1.5916616503900358e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.4310 |
| Legacy raw p draw | 0.2612 |
| Legacy raw p away | 0.3078 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.6609 |
| Legacy lambda away | 1.3782 |
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

The model's most likely 1X2 outcome is **Sunderland win** at **36.9%**. Expected goals are 1.22 for Sunderland and 1.14 for Leeds United (2.37 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 42.1%; Under 3.5 goals: 78.6%; Double Chance 1X: 66.8%; Double Chance X2: 63.1%; Double Chance 12 (either team wins): 70.1%; Under 4.5 goals: 90.8%; BTTS Yes (both teams score): 49.0%; BTTS No (at least one team does not score): 51.0%.

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
| 3 | 0-0 | 10.39% |
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
| Dc lambda home | 1.1596 |
| Dc lambda away | 1.0975 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:35:40.173016+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3642 |
| Shot lambda away | 1.2538 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.0% |
| P btts no | 51.0% |
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
| Goal margin distribution | {"-1": 0.19228540285512727, "-10": 1.1311289861561008e-07, "-11": 1.16453222147653e-08, "-12": 1.1005991789544757e-09, "-13": 9.574878999394292e-11, "-14": 7.116327344701701e-12, "-2": 0.09563216871780948, "-3": 0.0328898185578755, "-4": 0.008819937438672069, "-5": 0.0019315227629877318, "-6": 0.0003568095608865434, "-7": 5.693775424721013e-05, "-8": 7.991983987934719e-06, "-9": 1.0008537863297913e-06, "0": 0.298635560367594, "1": 0.2058288459763364, "10": 2.1629166025263933e-07, "11": 2.3759205636971705e-08, "12": 2.3958650685081013e-09, "13": 2.2239203543884357e-10, "14": 1.7635777731352865e-11, "2": 0.10887032846623239, "3": 0.039950274747705836, "4": 0.011430798302527339, "5": 0.0026709370468928286, "6": 0.0005264450767178988, "7": 8.963336138322887e-05, "8": 1.342383851803788e-05, "9": 1.7936822680539341e-06} |
| Raw goal margin distribution | {"-1": 0.19228540285512727, "-10": 1.1311289861561008e-07, "-11": 1.16453222147653e-08, "-12": 1.1005991789544757e-09, "-13": 9.574878999394292e-11, "-14": 7.116327344701701e-12, "-2": 0.09563216871780948, "-3": 0.0328898185578755, "-4": 0.008819937438672069, "-5": 0.0019315227629877318, "-6": 0.0003568095608865434, "-7": 5.693775424721013e-05, "-8": 7.991983987934719e-06, "-9": 1.0008537863297913e-06, "0": 0.298635560367594, "1": 0.2058288459763364, "10": 2.1629166025263933e-07, "11": 2.3759205636971705e-08, "12": 2.3958650685081013e-09, "13": 2.2239203543884357e-10, "14": 1.7635777731352865e-11, "2": 0.10887032846623239, "3": 0.039950274747705836, "4": 0.011430798302527339, "5": 0.0026709370468928286, "6": 0.0005264450767178988, "7": 8.963336138322887e-05, "8": 1.342383851803788e-05, "9": 1.7936822680539341e-06} |
| Unadjusted home-win probability | 36.9% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 69.4% |
| Raw p under 3 5 | 78.6% |
| Raw p btts yes | 49.0% |
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
| Unanchored p over 2 5 | 0.4212 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.13070518375051327, 0.11981931519600375, 0.0763463869507311, 0.02908331545604078, 0.008309226589151786, 0.001899185025564926, 0.0003617368117468242, 5.905699514476174e-05, 8.436417008129254e-06, 1.071253388517562e-06, 1.2242465482373618e-07, 1.2718997518031087e-08, 1.211290513787558e-09, 1.0648333469158152e-10], [0.10353160256177958, 0.14787045847170993, 0.07661382065460846, 0.029185191380810636, 0.008338332972987961, 0.0019058376794234904, 0.00036300393936422766, 5.926386585053101e-05, 8.465968927192484e-06, 1.0750058812408565e-06, 1.2285349605896775e-07, 1.2763550885278827e-08, 1.2155335424561283e-09, 1.0685633508800054e-10], [0.05886706635007143, 0.06727428221596085, 0.038441095575907296, 0.01464371208334201, 0.004183770656777561, 0.0009562568184292334, 0.0001821377528010249, 2.9735730601773286e-05, 4.247812181825862e-06, 5.393857592841048e-07, 6.164191974092675e-08, 6.4041301592423114e-09, 6.098957170133835e-10, 5.361532103361982e-11], [0.019691090584800848, 0.022503312416898357, 0.01285858362064036, 0.004898335843951571, 0.0013994753279995705, 0.0003198688299166559, 6.092525433472182e-05, 9.946630623695791e-06, 1.4208972800196638e-06, 1.8042505775730757e-07, 2.0619281725734227e-08, 2.142187727388634e-09, 2.0401070676045382e-10, 1.7934376701021135e-11], [0.0049400166229580005, 0.0056455348134400625, 0.0032259064859866053, 0.0012288735552630893, 0.00035109438727958593, 8.024732455266325e-05, 1.528466734106559e-05, 2.495368167236394e-06, 3.5646863501968593e-07, 4.526426714055314e-08, 5.172877248211156e-09, 5.374228988091115e-10, 5.118133392956735e-11, 4.499299754063423e-12], [0.0009914642007259112, 0.0011330621106546118, 0.0006474413022987182, 0.0002466356351109968, 7.046484711119721e-05, 1.6105684569611517e-05, 3.0676415982578123e-06, 5.008218381185289e-07, 7.154346174892504e-08, 9.084564661865554e-09, 1.0381994632398486e-09, 1.078610874188769e-10, 1.0272123397467338e-11, 9.030120695864525e-13], [0.00016582286666012356, 0.00018950518551769585, 0.00010828487066172624, 4.1249929149939975e-05, 1.1785279728900931e-05, 2.6936835267489485e-06, 5.130645396339214e-07, 8.376269442911051e-08, 1.1965678548261877e-08, 1.5193978294797272e-09, 1.7363936189868125e-10, 1.8039818990722053e-11, 1.718017601853333e-12, 1.510292049858005e-13], [2.377196106576406e-05, 2.7167000442227817e-05, 1.5523454522456843e-05, 5.913489071008251e-06, 1.689508910968206e-06, 3.861598898336058e-07, 7.355167900576838e-08, 1.2008015244444838e-08, 1.7153704450046904e-09, 2.1781716100608377e-10, 2.489251472777844e-11, 2.586144379953612e-12, 2.462908063534037e-13, 2.1651177868456914e-14], [2.9819039813830733e-06, 3.4077704635644495e-06, 1.947228952515758e-06, 7.41775428452143e-07, 2.1192838631449054e-07, 4.843907112920673e-08, 9.226165391149701e-09, 1.5062597640497955e-09, 2.1517240186267046e-10, 2.7322519072816893e-11, 3.1224638374618493e-12, 3.244004229050034e-13, 3.0894192280205007e-14, 2.71587747047783e-15], [3.324832545213754e-07, 3.7996750447417204e-07, 2.171166554901609e-07, 8.270819922959578e-08, 2.3630083345146137e-08, 5.400972035176366e-09, 1.0287204132505753e-09, 1.6794844892141363e-10, 2.3991792123802565e-11, 3.0464696783559815e-12, 3.4815572375442267e-13, 3.617075165697966e-14, 3.4447123915664856e-15, 3.0282121285707043e-16], [3.3364790987423775e-08, 3.812984923720035e-08, 2.1787719326634515e-08, 8.299791772112408e-09, 2.371285714708129e-09, 5.41989109622948e-10, 1.032323917245433e-10, 1.685367554222112e-11, 2.407583295515803e-12, 3.057141154798721e-13, 3.493752781884767e-14, 3.629745415691457e-15, 3.4567788721225797e-16, 3.038819650655447e-17], [3.0437876808863343e-09, 3.4784922053307617e-09, 1.987639955725071e-09, 7.571695551577063e-10, 2.1632655361188753e-10, 4.944433117134483e-11, 9.417636763198535e-12, 1.537519297285697e-12, 2.1963789248255567e-13, 2.78895455668055e-14, 3.18726458726254e-15, 3.3113273166313875e-16, 3.153534200313385e-17, 2.772240299837873e-18], [2.545374802135057e-10, 2.9088975109768066e-10, 1.6621687152456698e-10, 6.331848698727311e-11, 1.8090360311730937e-11, 4.134794140283594e-12, 7.875521496862738e-13, 1.2857542271042387e-13, 1.8367271824832095e-14, 2.3322699863241606e-15, 2.665357711741925e-16, 2.769105468920445e-17, 2.6371505941608316e-18, 2.318292648656714e-19], [1.9648392259205333e-11, 2.245451604594996e-11, 1.2830700960319094e-11, 4.8877142515191705e-12, 1.3964406939877832e-12, 3.1917522366926085e-13, 6.079314350341105e-14, 9.925062266619787e-15, 1.4178161944678612e-15, 1.800338225523028e-16, 2.057457070270178e-17, 2.1375425895951304e-18, 2.0356832823679027e-19, 1.7895487648511062e-20]] |
| Legacy trial inputs | {"lambda_home": 1.0035028992799615, "lambda_away": 1.1428169668910162, "rho": -0.102861516365706, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3035 |
| Legacy p draw | 0.3223 |
| Legacy p away | 0.3743 |
| Legacy p over 1 5 | 0.6459 |
| Legacy p under 3 5 | 0.8298 |
| Legacy p btts yes | 0.4452 |
| Legacy p over 2 5 | 0.3629 |
| Legacy goal margin distribution | {"-1": 0.21255972373384394, "-10": 1.358160358027294e-07, "-11": 1.3988146381520834e-08, "-12": 1.3181468488755585e-09, "-13": 1.0648333469158152e-10, "-2": 0.11005101549406981, "-3": 0.0384413989580399, "-4": 0.010407514381456382, "-5": 0.002293391913566376, "-6": 0.0004254341973149428, "-7": 6.808351695901548e-05, "-8": 9.575259081184424e-06, "-9": 1.2007195247422866e-06, "0": 0.3222827990047402, "1": 0.18496657556652135, "10": 3.7014387778530624e-08, "11": 3.347508132944334e-09, "12": 2.769919962594556e-10, "13": 1.9648392259205333e-11, "2": 0.0848551017242357, "3": 0.026027055623467743, "4": 0.006187494527492155, "5": 0.0011972587978146007, "6": 0.00019502222578161982, "7": 2.7405368498731677e-05, "8": 3.384434784274573e-06, "9": 3.7266545864198205e-07} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3035 |
| Legacy raw p draw | 0.3223 |
| Legacy raw p away | 0.3743 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.0035 |
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
