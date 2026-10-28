# La Liga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,999 |
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
| Training sha256 | 6dcf18d065b80178c455efad87d64d39fdcb495470ef88dfe2315b54745d4758 |
| Training as of utc | 2026-10-27T11:09:50.329525+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 98, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 98, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 71, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-10-27T11:09:50.329525+00:00', 'observations': 356, 'observations_sha256': '8f28f0cb7578e6b78f36d45352ed53fbcb098bcf3c6322ddd69b23c496281a58', 'eligible_training_matches': 125, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 142, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 20, 'retrospective_eligible_training_matches': 125, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '5ad6a171f151dc06f740f507c3bf065ab0fe840a61886d9530fa161bb51998a5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 65, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-20T00:00:00+00:00', 'audit_origin_utc': '2026-09-18T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 16, 'selected_ridge': 1.0, 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8175310729051967, 'audit_candidate_poisson_score': 0.8126906056458083, 'audit_gain': 0.004840467259388359, 'audit_gain_lower95': -0.026685529545786346, 'audit_baseline_briers': [0.552093299134768, 0.18075667919524327, 0.22581865901912312, 0.2521852580679206], 'audit_candidate_briers': [0.5470740827394455, 0.1856155448426209, 0.22770400315207753, 0.25227791876363415], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-27', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-10-28', 'audit_start_date': '2026-04-28', 'training_shot_matches': 1620, 'tuning_matches': 230, 'audit_matches': 135, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8133482612547668, 'audit_candidate_poisson_score': 0.81463656116035, 'audit_gain': -0.0012882999055832123, 'audit_gain_lower95': -0.011081835699235662, 'audit_baseline_briers': [0.5681496176107701, 0.18533589590382055, 0.2023504703592159, 0.24643224739779093], 'audit_candidate_briers': [0.5715846134636372, 0.18207449322873548, 0.20445929168328134, 0.24385806851016284], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1842.002 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.288 |
| Dixon-Coles low-score adjustment | -0.033 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1999, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261027T110950329525Z_38e99356deaf6291211f928a106d23c5e652a27e9278f0405a680808c79eb10b.json |
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
| Legacy comparison status | {'AVAILABLE': 1} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Villarreal CF vs RCD Espanyol de Barcelona

The model's most likely 1X2 outcome is **Villarreal CF win** at **64.8%**. Expected goals are 2.16 for Villarreal CF and 0.95 for RCD Espanyol de Barcelona (3.12 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 60.2%; Under 3.5 goals: 62.1%; Double Chance 1X: 84.8%; Double Chance X2: 35.2%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 54.6%; BTTS No (at least one team does not score): 45.4%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal CF win | 64.8% | 1.54 |
| Draw | 20.1% | 4.98 |
| RCD Espanyol de Barcelona win | 15.2% | 6.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal CF expected goals | 2.16 |
| RCD Espanyol de Barcelona expected goals | 0.95 |
| Expected total goals | 3.12 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 60.2% |
| Under 2.5 | 39.8% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.38% |
| 2 | 2-1 | 9.88% |
| 3 | 1-1 | 9.43% |
| 4 | 1-0 | 9.30% |
| 5 | 3-0 | 7.49% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:00:00+00:00 |
| Fixture id | fdorg:564737 |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1639 |
| Dc lambda away | 0.9517 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-27T11:09:50.329525+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.6% |
| P btts no | 45.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.13 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.57 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.51 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.89 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.1004542871352242, "-10": 8.966783027903193e-09, "-11": 7.639883821012791e-10, "-12": 5.980707791100746e-11, "-13": 4.3296158774268024e-12, "-14": 2.9147071041941627e-13, "-15": 1.8331068077945496e-14, "-16": 1.0755622114049876e-15, "-17": 5.3704182735176755e-17, "-2": 0.03795069806387659, "-3": 0.010409678632425087, "-4": 0.002258375452253844, "-5": 0.0004033998566134925, "-6": 6.109104240001169e-05, "-7": 8.018531836218935e-06, "-8": 9.279038511940784e-07, "-9": 9.596017097616153e-08, "0": 0.20092194515621592, "1": 0.23220585806167846, "10": 3.3133507640521595e-05, "11": 6.419195210285343e-06, "12": 1.1426401701271673e-06, "13": 1.8809157662234243e-07, "14": 2.8792407089590623e-08, "15": 4.117502771937071e-09, "16": 5.493444492696435e-10, "17": 6.237066757595176e-11, "2": 0.19622119639659782, "3": 0.12238453671199685, "4": 0.060373790840608586, "5": 0.024521730558200547, "6": 0.008444150935957774, "7": 0.0025202079959212513, "8": 0.0006631435957972549, "9": 0.00015594041693243628} |
| Raw goal margin distribution | {"-1": 0.1004542871352242, "-10": 8.966783027903193e-09, "-11": 7.639883821012791e-10, "-12": 5.980707791100746e-11, "-13": 4.3296158774268024e-12, "-14": 2.9147071041941627e-13, "-15": 1.8331068077945496e-14, "-16": 1.0755622114049876e-15, "-17": 5.3704182735176755e-17, "-2": 0.03795069806387659, "-3": 0.010409678632425087, "-4": 0.002258375452253844, "-5": 0.0004033998566134925, "-6": 6.109104240001169e-05, "-7": 8.018531836218935e-06, "-8": 9.279038511940784e-07, "-9": 9.596017097616153e-08, "0": 0.20092194515621592, "1": 0.23220585806167846, "10": 3.3133507640521595e-05, "11": 6.419195210285343e-06, "12": 1.1426401701271673e-06, "13": 1.8809157662234243e-07, "14": 2.8792407089590623e-08, "15": 4.117502771937071e-09, "16": 5.493444492696435e-10, "17": 6.237066757595176e-11, "2": 0.19622119639659782, "3": 0.12238453671199685, "4": 0.060373790840608586, "5": 0.024521730558200547, "6": 0.008444150935957774, "7": 0.0025202079959212513, "8": 0.0006631435957972549, "9": 0.00015594041693243628} |
| Unadjusted home-win probability | 64.8% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 15.2% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 54.6% |
| P home draw | 84.8% |
| P draw away | 35.2% |
| P home away | 79.9% |
| Raw p home draw | 84.8% |
| Raw p draw away | 35.2% |
| Raw p home away | 79.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6022 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04236165978304871, 0.037660185885778796, 0.019384345149975068, 0.006327238394787553, 0.0015489540165556715, 0.00030335617477356076, 4.95091998587743e-05, 6.92583572284028e-06, 8.477474998994731e-07, 9.223767063832611e-08, 9.032181277106547e-09, 8.04052263304151e-10, 6.561261564980456e-11, 4.942291052709634e-12, 3.456882359558457e-13, 2.2567199069595806e-14, 1.3811536510959744e-15, 7.955681589238258e-17], [0.08818676951736087, 0.09017663726062845, 0.04320642457334373, 0.01410299632754447, 0.0034525161601332973, 0.000676160870166346, 0.00011035273530442079, 1.5437230221143322e-05, 1.889573164750134e-06, 2.0559167350881e-07, 2.013213529075927e-08, 1.7921793694187183e-09, 1.462461851148332e-10, 1.1016040208543493e-11, 7.705162375700738e-13, 5.030079566207982e-14, 3.078500232459659e-15, 1.7732688613182492e-16], [0.1004331043432746, 0.0983470200811951, 0.048152132815651026, 0.01571732349918917, 0.0038477152028331854, 0.0007535589520888782, 0.00012298447787385672, 1.72042830957338e-05, 2.1058668680044644e-06, 2.291251281804929e-07, 2.2436599694513295e-08, 1.997324700617812e-09, 1.6298654190831487e-10, 1.2277012885523455e-11, 8.587148919279019e-13, 5.6058575023764006e-14, 3.4308868074648486e-15, 1.9762495640690906e-16], [0.07461958458232185, 0.07306966991964205, 0.03577597417655919, 0.011677625200619402, 0.002858767653393987, 0.0005598777049743485, 9.137475844273725e-05, 1.2782403431964463e-05, 1.5646127031887467e-06, 1.7023492397250113e-07, 1.666989942800213e-08, 1.4839682633596872e-09, 1.210954110124752e-10, 9.121550184273665e-12, 6.38006252313999e-13, 4.165028660522837e-14, 2.5490733358889646e-15, 1.4683099010640625e-16], [0.0415805309388344, 0.04071686659461639, 0.01993557066073219, 0.006507163751505282, 0.0015930010536007323, 0.0003119826030117671, 5.091707480983316e-05, 7.122783172145652e-06, 8.718545845087131e-07, 9.486059943552223e-08, 9.289026102103401e-09, 8.269168025024648e-10, 6.747841752723971e-11, 5.082833170009053e-12, 3.5551844548591767e-13, 2.3208934229450382e-14, 1.4204290107157663e-15, 8.181914387587628e-17], [0.018536051229263686, 0.018151041077448582, 0.008887013963229993, 0.0029008076119215326, 0.0007101388190845921, 0.00013907772174847705, 2.2698159109792655e-05, 3.1752426145795195e-06, 3.886612527072974e-07, 4.22876016990271e-08, 4.14092508707593e-09, 3.686285833163603e-10, 3.008098684440758e-11, 2.265859860415954e-12, 1.5848542502184539e-13, 1.0346236186510886e-14, 6.332084828087059e-16, 3.647389314601795e-17], [0.006885938912117837, 0.006742911880461898, 0.0033014278232748966, 0.001077618084048183, 0.0002638087512198923, 5.166584210150446e-05, 8.432116156477191e-06, 1.1795676654491219e-06, 1.4438337543135692e-07, 1.5709378358846825e-08, 1.538308069857108e-09, 1.369414593529816e-10, 1.1174755359965578e-11, 8.417419864275967e-13, 5.887559014934866e-14, 3.843512810224738e-15, 2.352299784525774e-16, 1.3549649652137366e-17], [0.0021926146951588956, 0.002147072151808432, 0.0010512377836492646, 0.00034313421553812726, 8.400175372138916e-05, 1.645139262420155e-05, 2.6849471120696233e-06, 3.755969128112064e-07, 4.5974429158865516e-08, 5.002166629855407e-09, 4.898267211918728e-10, 4.360478069671173e-11, 3.5582559081300875e-12, 2.680267531455273e-13, 1.8747114343468787e-14, 1.2238480149598528e-15, 7.490172568760152e-17, 4.314467688531042e-18], [0.0006108991605844222, 0.0005982102455802922, 0.00029289244527270895, 9.560293685108468e-05, 2.3404294858243285e-05, 4.583633397495388e-06, 7.480712140616373e-07, 1.0464758776864732e-07, 1.2809245620541458e-08, 1.3936873642364353e-09, 1.3647392470214646e-10, 1.214902188875396e-11, 9.913896646869386e-13, 7.467674045617256e-14, 5.2232599011087594e-15, 3.409845453798277e-16, 2.0868874704665998e-17, 1.2020829264310028e-18], [0.0001512948739447892, 0.00014815234581590873, 7.253754538559689e-05, 2.3676958838508075e-05, 5.796291874025681e-06, 1.1351795547071407e-06, 1.8526681216079393e-07, 2.5916950982445812e-08, 3.1723291281554286e-09, 3.451596723244439e-10, 3.379904011458944e-11, 3.008818564185119e-12, 2.455268954789295e-13, 1.8494391157970876e-14, 1.2935890230445228e-15, 8.444800245102481e-17, 5.168371429405029e-18, 2.977070465305195e-19], [3.372262776407222e-05, 3.302217900751332e-05, 1.6168139595070707e-05, 5.277437686273752e-06, 1.2919551613560579e-06, 2.5302402236538307e-07, 4.1294748332416445e-08, 5.776717135040958e-09, 7.070912023955835e-10, 7.693381041590301e-11, 7.533582723914224e-12, 6.706457780365503e-13, 5.472632275251895e-14, 4.122277592636711e-15, 2.8833244621188776e-16, 1.8822901779967737e-17, 1.1519958430574073e-18, 6.635693365628272e-20], [6.8332281053245354e-06, 6.691295923670615e-06, 3.276155899379604e-06, 1.0693690828080946e-06, 2.6178933566982644e-07, 5.1270348000324864e-08, 8.367569599899323e-09, 1.1705382557917553e-09, 1.4327814282565748e-10, 1.5589125475676625e-11, 1.5265325573970538e-12, 1.3589319347405475e-13, 1.1089214320717468e-14, 8.352985805562035e-16, 5.842490653208004e-17, 3.81409130885318e-18, 2.3342932902706673e-19, 1.3445929161141741e-20], [1.2692344967073319e-06, 1.2428713754458424e-06, 6.085279197461153e-07, 1.9862941916935331e-07, 4.8625927684651485e-08, 9.523184845753292e-09, 1.5542299812172573e-09, 2.174210360120805e-10, 2.6613126138256975e-11, 2.895594223147647e-12, 2.835450174252869e-13, 2.5241412457838947e-14, 2.059760502692469e-15, 1.5515211217176968e-16, 1.0852104699919954e-17, 7.084464601753784e-19, 4.335821260138189e-20, 2.497507308193928e-21], [2.176184486207648e-07, 2.1309832128053752e-07, 1.0433604048827446e-07, 3.405629626535864e-08, 8.337229229847662e-09, 1.6328115233535763e-09, 2.664827643668835e-10, 3.7278240291461714e-11, 4.562992290377095e-12, 4.964683234747755e-13, 4.86156238002621e-14, 4.3278031241049435e-15, 3.5315923597183807e-16, 2.6601831291732455e-17, 1.8606634118385825e-18, 1.214677193175817e-19, 7.434045470525634e-21, 4.282137518623631e-22], [3.46469388178768e-08, 3.392729130454128e-08, 1.6611295752761982e-08, 5.4220881572665464e-09, 1.3273666496011568e-09, 2.5995921443839195e-10, 4.242660533403469e-11, 5.9350524682177326e-12, 7.264720234571772e-13, 7.904250644861511e-14, 7.74007237932251e-15, 6.890276583029209e-16, 5.622632878431825e-17, 4.235266022019563e-18, 2.962354147785337e-19, 1.9338822908701307e-20, 1.183571155014838e-21, 6.817572570606553e-23], [5.148382495083579e-09, 5.041446044513945e-09, 2.4683653792250624e-09, 8.05698416890665e-10, 1.9724083733014528e-10, 3.862879419406993e-11, 6.30440667141598e-12, 8.819226539866434e-13, 1.0795054271302802e-13, 1.1745368290880903e-14, 1.1501406620033942e-15, 1.0238647498649563e-16, 8.35498479094025e-18, 6.293418753213822e-19, 4.401927777477133e-20, 2.8736639003532167e-21, 1.7587346022674275e-22, 1.0130612538664581e-23], [7.172127760427528e-10, 7.023156333680493e-10, 3.438639587506191e-10, 1.1224053356238134e-10, 2.7477299642293577e-11, 5.3813143731200765e-12, 8.782566202931864e-13, 1.2285920782396806e-13, 1.5038414198725087e-14, 1.6362281173925214e-15, 1.602242214565125e-16, 1.4263292990452976e-17, 1.1639193166839395e-18, 8.767259113133802e-20, 6.1322538568937984e-21, 4.003254352904711e-22, 2.4500645156400545e-23, 1.4112791248139753e-24], [9.403646411690215e-11, 9.208324372071303e-11, 4.50852967184469e-11, 1.4716278431397688e-11, 3.602652083386597e-12, 7.055643636770785e-13, 1.1515152813550679e-13, 1.6108532744933854e-14, 1.9717430369495062e-15, 2.1453202144167655e-16, 2.1007600191934936e-17, 1.870113980520671e-18, 1.5260583848243415e-19, 1.1495083112499456e-20, 8.040228632725224e-22, 5.2488173228709467e-23, 3.2123717201511125e-24, 1.850381131130207e-25]] |
| Legacy trial inputs | {"lambda_home": 2.2289339278195475, "lambda_away": 0.9792291169757196, "rho": -0.021880307715209636, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6547 |
| Legacy p draw | 0.1941 |
| Legacy p away | 0.1512 |
| Legacy p over 1 5 | 0.8318 |
| Legacy p under 3 5 | 0.6007 |
| Legacy p btts yes | 0.5591 |
| Legacy p over 2 5 | 0.6218 |
| Legacy goal margin distribution | {"-1": 0.09977860934409015, "-10": 1.0996834842843971e-08, "-11": 9.632373232491836e-10, "-12": 7.753047793978505e-11, "-13": 5.771496757783237e-12, "-14": 3.995667494154968e-13, "-15": 2.5843324258462376e-14, "-16": 1.5584805372277993e-15, "-17": 7.955681589238258e-17, "-2": 0.037949176227831866, "-3": 0.010632215921481128, "-4": 0.002361797493137073, "-5": 0.00043257694797713136, "-6": 6.7232200974671e-05, "-7": 9.062061773823575e-06, "-8": 1.0773295457641484e-06, "-9": 1.1449347127892731e-07, "0": 0.19410895471044293, "1": 0.22958152503332144, "10": 4.1057874793563255e-05, "11": 8.186060346719152e-06, "12": 1.4997779950215283e-06, "13": 2.541299484901769e-07, "14": 4.004696509957276e-08, "15": 5.8957834251700745e-09, "16": 8.092960197634658e-10, "17": 9.403646411690215e-11, "2": 0.19662018739054776, "3": 0.12538985980108763, "4": 0.06340071602191297, "5": 0.026431861735756162, "6": 0.009350925285793444, "7": 0.002868911508858999, "8": 0.0007763393171411987, "9": 0.00018780044188853337} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.6547 |
| Legacy raw p draw | 0.1941 |
| Legacy raw p away | 0.1512 |
| Legacy market weight | 0 |
| Legacy lambda home | 2.2289 |
| Legacy lambda away | 0.9792 |
| Legacy model home team | Villarreal |
| Legacy model away team | Espanol |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 10.164044473652304, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,563.5990 |
| Elo away rating | 1,432.0064 |
| Elo rating diff | 191.5927 |
| Elo home expectancy | 0.7508 |

</details>


---
