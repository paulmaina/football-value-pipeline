# Ligue 1 — football model report

Fixtures in this report: **3**.

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
| Training sha256 | dad0ad7f0e260e5fee63d5ef1fe615b35e955888ac9e3dc448efa81a654046cd |
| Training as of utc | 2026-10-28T16:10:42.048441+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 107, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-28T16:10:42.048441+00:00', 'observations': 337, 'observations_sha256': 'fb5fe05f26d7789c54cd577539c872a5e747fc3a59e91f0e25d0df20f3ada3e5', 'eligible_training_matches': 144, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 143, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 15, 'retrospective_eligible_training_matches': 144, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '55953c539863c32a7c169d31e44708bd47ebe68340e08606f0789d8190dc1a74', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 83, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-08-24T00:00:00+00:00', 'audit_origin_utc': '2025-09-27T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 28, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1750, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1453, 'tuning_matches': 196, 'audit_matches': 97, 'audit_matchdays': 32, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8794253162837602, 'audit_candidate_poisson_score': 0.874802846530951, 'audit_gain': 0.004622469752809222, 'audit_gain_lower95': -0.002788835744845332, 'audit_baseline_briers': [0.6035182490482103, 0.16831698204664922, 0.2150009196655041, 0.24570077103396187], 'audit_candidate_briers': [0.6021999125629951, 0.16740770566389948, 0.2130723246518978, 0.24370844486079418], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1585.691 |
| Base scoring parameter | 0.208 |
| Home-advantage parameter | 0.192 |
| Dixon-Coles low-score adjustment | -0.056 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1752, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 3.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 7.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261028T161042048441Z_d6d86b3f78fce5588d5f86e4aec25d43341e3915c98aba7ff559c14d9e9e8667.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 3} |
| Legacy comparison status | {'AVAILABLE': 3} |
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

## 2026-10-30 — Le Havre vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **76.7%**. Expected goals are 0.80 for Le Havre and 2.26 for Paris Saint Germain (3.06 combined). The most likely exact score is 0-2 at 13.1%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 61.2%; Under 3.5 goals: 62.2%; Double Chance 1X: 23.3%; Double Chance X2: 90.9%; Double Chance 12 (either team wins): 85.8%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 9.1% | 10.96 |
| Draw | 14.2% | 7.04 |
| Paris Saint Germain win | 76.7% | 1.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 0.80 |
| Paris Saint Germain expected goals | 2.26 |
| Expected total goals | 3.06 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 61.2% |
| Under 2.5 | 38.8% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 13.14% |
| 2 | 0-1 | 11.09% |
| 3 | 1-2 | 10.48% |
| 4 | 0-3 | 9.91% |
| 5 | 1-3 | 7.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 9.1% | 8.2% | 10.39 | -5.2% |
| Draw | 14.2% | 12.3% | 7.16 | +1.8% |
| Paris Saint Germain win | 76.7% | 79.5% | 1.24 | -4.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T18:00:00+00:00 |
| Fixture id | 9a9f6c78276f74f15f42b013b033aa5d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:10:56Z |
| Market best draw last update utc | 2026-10-28T16:10:56Z |
| Market best away last update utc | 2026-10-28T16:10:56Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Le Havre |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7973 |
| Dc lambda away | 2.2620 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:10:42.048441+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.56 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.66 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.65 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.2523827956317257, "-10": 5.840466997108167e-05, "-11": 1.18499567336239e-05, "-12": 2.2084164847579073e-06, "-13": 3.8052258104023694e-07, "-14": 6.09611185909612e-08, "-15": 9.12312827953935e-09, "-16": 1.275234005897511e-09, "-17": 1.5340465041130182e-10, "-2": 0.2304863016963688, "-3": 0.15264530666639764, "-4": 0.07953890868621243, "-5": 0.0340196382601687, "-6": 0.01231268534654152, "-7": 0.0038574687364187512, "-8": 0.0010645404687781412, "-9": 0.00026237823506546163, "0": 0.14213893305817352, "1": 0.06380853172152515, "10": 1.289757758534755e-09, "11": 9.224367723673686e-11, "12": 6.05982512063343e-12, "13": 3.680601617934442e-13, "14": 2.07850261013102e-14, "15": 1.0964799541533513e-15, "16": 5.402640477875366e-17, "17": 2.2909413768631395e-18, "2": 0.021351655335143126, "3": 0.004984586703163975, "4": 0.0009155553291052028, "5": 0.00013803649595052806, "6": 1.7610686420013134e-05, "7": 1.944845855795972e-06, "8": 1.8919263013929965e-07, "9": 1.6437248209610277e-08} |
| Raw goal margin distribution | {"-1": 0.2305801012278735, "-10": 5.335924217973793e-05, "-11": 1.0826269739764502e-05, "-12": 2.0176371187829567e-06, "-13": 3.476502232893092e-07, "-14": 5.56948458411532e-08, "-15": 8.335004915630726e-09, "-16": 1.165069851267279e-09, "-17": 1.4015242097674144e-10, "-2": 0.21057518854944587, "-3": 0.13945867496632702, "-4": 0.07266774888722254, "-5": 0.03108077004270761, "-6": 0.01124902442928489, "-7": 0.0035242320281794366, "-8": 0.0009725775817548479, "-9": 0.00023971206060204177, "0": 0.18780246246923843, "1": 0.07819391092368286, "10": 1.5805285055630639e-09, "11": 1.1303964668237554e-10, "12": 7.425988545918237e-12, "13": 4.510378585646756e-13, "14": 2.547092740834855e-14, "15": 1.3436769903882329e-15, "16": 6.62064424430502e-17, "17": 2.807424980966698e-18, "2": 0.026165300944954163, "3": 0.006108341912012606, "4": 0.0011219636296004119, "5": 0.00016915627389263034, "6": 2.1580945495520395e-05, "7": 2.3833036038518193e-06, "8": 2.318453546791011e-07, "9": 2.0142960316686793e-08} |
| Unadjusted home-win probability | 11.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 70.0% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 49.7% |
| P home draw | 23.3% |
| P draw away | 90.9% |
| P home away | 85.8% |
| Raw p home draw | 30.0% |
| Raw p draw away | 88.8% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6121 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:10:56Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:10:28Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.33, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:10:28Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.71, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:10:56Z", "line": 2.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.39 |
| Reference draw odds | 7.16 |
| Reference away odds | 1.24 |
| Market reference 1x2 last update utc | 2026-10-28T16:10:56Z |
| Market reference home last update utc | 2026-10-28T16:10:56Z |
| Market reference draw last update utc | 2026-10-28T16:10:56Z |
| Market reference away last update utc | 2026-10-28T16:10:56Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.42 |
| Market reference over 2 5 last update utc | 2026-10-28T16:10:32Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:10:32Z |
| Home probability edge | +0.9% |
| Draw probability edge | +2.0% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -12.7% |
| Under 2.5 probability edge | +12.7% |
| Raw edge prob home | 0.0294 |
| Raw ev home | 0.1614 |
| Raw edge prob draw | 0.0652 |
| Raw ev draw | 0.3447 |
| Raw edge prob away | -0.0946 |
| Raw ev away | -0.1315 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.03937770403178491, 0.09939625063525029, 0.1221954702999692, 0.0950121599877248, 0.055406987611974254, 0.025848769476497255, 0.0100492572063344, 0.0033487386974638657, 0.000976419879045433, 0.000253069287362073, 5.9031630779273125e-05, 1.2518071699164685e-05, 2.4333328970770112e-06, 4.3661988820596683e-07, 7.274795965994543e-08, 1.131292471811539e-08, 1.649302257186863e-09, 2.263063138919091e-10, 2.932712596867264e-11], [0.026126288485323796, 0.07252542951181133, 0.10175931541564452, 0.07912218294817597, 0.046140639377194786, 0.021525782255333165, 0.008368604263660491, 0.0027886905834011585, 0.0008131219447494914, 0.00021074559778257228, 4.915909175046922e-05, 1.0424530494493076e-05, 2.02637863070597e-06, 3.63598919105806e-07, 6.058148108688801e-08, 9.420934113499911e-09, 1.3734704583796237e-09, 1.8845850438929433e-10, 2.442241315782432e-11], [0.012703824683173935, 0.02963328723128701, 0.033176779929447966, 0.03294483482584459, 0.019212004603515385, 0.008962888970891269, 0.003484513127876352, 0.0011611528806114333, 0.00033856710172654663, 8.775009296404635e-05, 2.0468825524802882e-05, 4.340558140351103e-06, 8.437420050323363e-07, 1.513950435447706e-07, 2.5224871376713762e-08, 3.9226814366043005e-09, 5.718845929608783e-10, 7.847020983606647e-11, 1.0168985960107467e-11], [0.003526405956365668, 0.008225790516261837, 0.009593851424746015, 0.007160710744201282, 0.005332986652224071, 0.002487973963861288, 0.0009672526310483951, 0.0003223199734378174, 9.39815428765555e-05, 2.4358211658092782e-05, 5.681862750048645e-06, 1.20487888189759e-06, 2.3421110621298116e-07, 4.202516931988497e-08, 7.00207527180524e-09, 1.088882090862608e-09, 1.5874725016018905e-10, 2.1782244502293715e-11, 2.8227697999814127e-12], [0.0007341611254421273, 0.001712524223754956, 0.0019973403080838395, 0.00155301678888535, 0.0008693618063605804, 0.0005179703607526768, 0.000201371960285934, 6.710367364949145e-05, 1.956598194955092e-05, 5.071126894049684e-06, 1.1829048620036026e-06, 2.5084327978705954e-07, 4.8760321827943784e-08, 8.749204143410712e-09, 1.4577594087542337e-09, 2.266939516303874e-10, 3.304953011098027e-11, 4.534837263869826e-12, 5.876713795464986e-13], [0.00012227578214867566, 0.00028522381756741153, 0.000332660420069164, 0.00025865758342437606, 0.00015083792982276337, 6.754993819868552e-05, 3.353884194283127e-05, 1.1176230797564672e-05, 3.258747519418748e-06, 8.446047956730026e-07, 1.9701481350140428e-07, 4.177837421482979e-08, 8.121114402158522e-09, 1.4571948074337401e-09, 2.4279230500344156e-10, 3.775626260146449e-11, 5.504455362619003e-12, 7.55284847073197e-13, 9.78776662100775e-14], [1.6971032631592904e-05, 3.95870926375135e-05, 4.6170964887950484e-05, 3.589988312948684e-05, 2.0935261129562626e-05, 9.766831986213004e-06, 3.6449104558827214e-06, 1.5511835150893608e-06, 4.5229161096621117e-07, 1.1722530247844037e-07, 2.734429312236246e-08, 5.798549309074734e-09, 1.1271544953713804e-09, 2.0224855807895223e-10, 3.369789224413226e-11, 5.240308042988744e-12, 7.639803233036642e-13, 1.0482831154775573e-13, 1.358474293082552e-14], [2.018967359952123e-06, 4.709498216493559e-06, 5.492751861942424e-06, 4.270847498672612e-06, 2.4905737800525416e-06, 1.1619160376600846e-06, 4.517194957859704e-07, 1.444957893327609e-07, 5.3807097042581955e-08, 1.3945766566019007e-08, 3.253027467064117e-09, 6.898273101131854e-10, 1.3409249661931312e-10, 2.406060056702982e-11, 4.008886554930929e-12, 6.234158595154279e-13, 9.088730013543046e-14, 1.247095235795007e-14, 1.6161157170612757e-15], [2.1016402642720407e-07, 4.902343283318328e-07, 5.717669687828517e-07, 4.4457306461798075e-07, 2.5925580775227404e-07, 1.2094943072818023e-07, 4.7021655690509645e-08, 1.5669141986969637e-08, 4.385707121585401e-09, 1.451681939621817e-09, 3.3862328045397223e-10, 7.180744370046303e-11, 1.3958333137123808e-11, 2.50458367664922e-12, 4.1730428960186165e-13, 6.489435627995762e-14, 9.460896360411092e-15, 1.2981614328776334e-15, 1.6822926066419424e-16], [1.9446208604885605e-08, 4.536075548266526e-08, 5.290486643862293e-08, 4.1135777143425915e-08, 2.398860835170149e-08, 1.1191296153611881e-08, 4.350853669152942e-09, 1.4498456701567156e-09, 4.2274368405068447e-10, 1.0517657286960789e-10, 3.1332379104658504e-11, 6.644250937333738e-12, 1.2915467150845448e-12, 2.317459247069681e-13, 3.86126322628399e-14, 6.004591798858279e-15, 8.754046415145315e-16, 1.2011721727885581e-16, 1.556603835554484e-17], [1.6193995327365854e-09, 3.777455427211217e-09, 4.405697672536173e-09, 3.4256167687147e-09, 1.997671728461583e-09, 9.319646893699683e-10, 3.623210334718602e-10, 1.2073712920070558e-10, 3.520433922770048e-11, 9.124288875720737e-12, 2.0430708323367404e-12, 5.533056382311789e-13, 1.075546493104015e-13, 1.9298838648156094e-14, 3.2154997364608575e-15, 5.000374803601584e-16, 7.290006480069895e-17, 1.0002863256651887e-17, 1.296275060692087e-18], [1.2259715551809252e-10, 2.8597346183611985e-10, 3.3353474038174453e-10, 2.5933740454389455e-10, 1.512343721344884e-10, 7.055468255383641e-11, 2.7429628816158865e-11, 9.140442680265156e-12, 2.6651556728046322e-12, 6.907571847933173e-13, 1.6112790104201451e-13, 3.279914038218207e-14, 8.142458856906461e-15, 1.4610247040570331e-15, 2.4343042793961356e-16, 3.785549613009624e-17, 5.518922539484318e-18, 7.572699371041752e-19, 9.813491482323576e-20], [8.507818515968314e-12, 1.9845569037903515e-11, 2.314615724929865e-11, 1.799711879886233e-11, 1.0495142289877673e-11, 4.896250912862416e-12, 1.903521357751363e-12, 6.343151042181445e-13, 1.8495258462729166e-13, 4.793615921990494e-14, 1.1181718973259995e-14, 2.371162002123199e-15, 4.4245018171351755e-16, 1.0139006061710095e-16, 1.6893229646499376e-17, 2.627040485121777e-18, 3.8299413368273635e-19, 5.255191415538402e-20, 6.81022362931483e-21], [5.449967774143474e-13, 1.2712743168311895e-12, 1.482704536623249e-12, 1.1528656528949011e-12, 6.723014502193301e-13, 3.136457323241768e-13, 1.2193642868224757e-13, 4.0633176062146994e-14, 1.184775655558938e-14, 3.07071104624942e-15, 7.162824165726784e-16, 1.5189271461997276e-16, 2.9525756697477086e-17, 5.085598630284134e-18, 1.08215234024827e-18, 1.682838668738858e-19, 2.4533970515934833e-20, 3.3663886703605826e-21, 4.362516577523862e-22], [3.241790669915708e-14, 7.561889152371202e-14, 8.819534228938369e-14, 6.8575618647733e-14, 3.99903386407519e-14, 1.8656510475737516e-14, 7.253114022074692e-15, 2.416973026377434e-15, 7.047371333746753e-16, 1.8265433544334954e-16, 4.260644743784601e-17, 9.034996269507007e-18, 1.756273184553378e-18, 3.1513312560725406e-19, 5.040230735480061e-20, 1.0009987070333422e-20, 1.4593480183842794e-21, 2.0024205344223356e-22, 2.5949448004932654e-23], [1.7997524702655504e-15, 4.1981515981746645e-15, 4.8963613420283344e-15, 3.807128578862094e-15, 2.2201529365657827e-15, 1.0357578336826043e-15, 4.0267281905299736e-16, 1.3418365396495814e-16, 3.912505543462231e-17, 1.0140463246734819e-17, 2.3653920574549782e-18, 5.015979904497682e-19, 9.750342709337476e-20, 1.749531906971978e-20, 2.915004103801737e-21, 4.351433075489079e-22, 8.101896354500075e-23, 1.1116884679758699e-23, 1.4406415436478309e-24], [9.367244692164921e-17, 2.1850289928538308e-16, 2.548429050649896e-16, 1.9815116557374925e-16, 1.1555320053413606e-16, 5.3908508143345226e-17, 2.0958075564673253e-17, 6.983911071910296e-18, 2.0363576319834057e-18, 5.277848042628598e-19, 1.2311251997789978e-19, 2.6106874091123833e-20, 5.0748004239357565e-21, 9.105859689104006e-22, 1.5171840111405369e-22, 2.3593498129421094e-23, 3.301845527194858e-24, 5.786050066902495e-25, 7.498165484421466e-26], [4.588619148077575e-18, 1.0703537918786357e-17, 1.2483681940229803e-17, 9.706592092401673e-18, 5.660465227689488e-18, 2.640751051563271e-18, 1.0266479632303732e-18, 3.421124260781119e-19, 9.975259459453063e-20, 2.5853957470873064e-20, 6.03076448948952e-21, 1.2788659449793315e-21, 2.485931259746132e-22, 4.460577630055863e-23, 7.432046277706054e-24, 1.1557462289561806e-24, 1.6849531943762301e-25, 2.2193373237544097e-26, 3.673035865717187e-27], [2.1228953089361593e-19, 4.951923379026033e-19, 5.775495628193039e-19, 4.490692766984018e-19, 2.618778044216781e-19, 1.2217265888759965e-19, 4.749721157363257e-20, 1.582761264364828e-20, 4.614990006474154e-21, 1.1961168112055204e-21, 2.790094629971594e-22, 5.916591522947053e-23, 1.1501002021193681e-23, 2.0636577193290035e-24, 3.4383886894053236e-25, 5.346986029118696e-26, 7.79532821680546e-27, 1.0696232219628617e-27, 1.3305852812494495e-28]] |
| Legacy trial inputs | {"lambda_home": 0.8327584906858053, "lambda_away": 2.332627218205864, "rho": -0.061598984472994917, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0971 |
| Legacy p draw | 0.1532 |
| Legacy p away | 0.7497 |
| Legacy p over 1 5 | 0.8351 |
| Legacy p under 3 5 | 0.6023 |
| Legacy p btts yes | 0.5048 |
| Legacy p over 2 5 | 0.6277 |
| Legacy goal margin distribution | {"-1": 0.239986503205847, "-10": 7.034342474040928e-05, "-11": 1.470307975353865e-05, "-12": 2.823279388050094e-06, "-13": 5.012874306945493e-07, "-14": 8.276314828228806e-08, "-15": 1.276768815613106e-08, "-16": 1.8479297475362646e-09, "-17": 2.507287270497334e-10, "-18": 2.932712596867264e-11, "-2": 0.22323064658935943, "-3": 0.15115342393947664, "-4": 0.0807600416036806, "-5": 0.035477782240538804, "-6": 0.013202098937994894, "-7": 0.004255551768644866, "-8": 0.0012088894330822316, "-9": 0.00030681214568806383, "0": 0.15318132986101, "1": 0.06706751651272042, "10": 1.929713064876176e-09, "11": 1.439962798151873e-10, "12": 9.871213545116547e-12, "13": 6.257159640835481e-13, "14": 3.688086967229355e-14, "15": 2.0311881207678615e-15, "16": 1.0495353440325487e-16, "17": 5.083811485980178e-18, "18": 2.1228953089361593e-19, "2": 0.023207758775519, "3": 0.005610106480834671, "4": 0.0010700975741496101, "5": 0.00016782514836176734, "6": 2.229550376529329e-05, "7": 2.5656884265074007e-06, "8": 2.6020063316433173e-07, "9": 2.35758872589958e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1119 |
| Legacy raw p draw | 0.1838 |
| Legacy raw p away | 0.7043 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8328 |
| Legacy lambda away | 2.3326 |
| Legacy model home team | Le Havre |
| Legacy model away team | Paris SG |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015445853721645362, "mu": 9.295394800205962, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,379.4397 |
| Elo away rating | 1,704.9432 |
| Elo rating diff | -265.5035 |
| Elo home expectancy | 0.1782 |

</details>


---

## 2026-10-30 — Lille vs RC Lens

The model's most likely 1X2 outcome is **Lille win** at **38.2%**. Expected goals are 1.28 for Lille and 1.09 for RC Lens (2.37 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 42.7%; Under 3.5 goals: 78.5%; Double Chance 1X: 65.8%; Double Chance X2: 61.8%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 38.2% | 2.62 |
| Draw | 27.7% | 3.62 |
| RC Lens win | 34.2% | 2.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.28 |
| RC Lens expected goals | 1.09 |
| Expected total goals | 2.37 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 69.3% |
| Under 1.5 | 30.7% |
| Over 2.5 | 42.7% |
| Under 2.5 | 57.3% |
| Over 3.5 | 21.5% |
| Under 3.5 | 78.5% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 1-0 | 10.69% |
| 3 | 0-1 | 10.49% |
| 4 | 0-0 | 9.55% |
| 5 | 2-1 | 7.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 38.2% | 37.3% | 2.60 | -0.8% |
| Draw | 27.7% | 27.0% | 3.56 | -1.5% |
| RC Lens win | 34.2% | 35.6% | 2.72 | -7.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:05:00+00:00 |
| Fixture id | 7932d9a82dcdb164a3e4ef5e03694ee3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:10:56Z |
| Market best draw last update utc | 2026-10-28T16:10:56Z |
| Market best away last update utc | 2026-10-28T16:10:56Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lille |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2816 |
| Dc lambda away | 1.0894 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:10:42.048441+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.47 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.25 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.64 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.70 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.20457424103991392, "-10": 7.642721888130796e-08, "-11": 7.49049113353214e-09, "-12": 6.739232358782042e-10, "-13": 5.581349437014412e-11, "-14": 3.949234710670503e-12, "-2": 0.09578173139601677, "-3": 0.031361142835371135, "-4": 0.008006380613665685, "-5": 0.001669185067696611, "-6": 0.00029354262218165693, "-7": 4.4592569455708834e-05, "-8": 5.958576190962223e-06, "-9": 7.103673729920746e-07, "0": 0.27657458507675964, "1": 0.2073046261538572, "10": 3.322628214609544e-07, "11": 3.830954220603507e-08, "12": 4.054805940248635e-09, "13": 3.9505888429739204e-10, "14": 3.2885052559081265e-11, "2": 0.11350436689868836, "3": 0.04372046209065564, "4": 0.01313082673375793, "5": 0.003220500012205006, "6": 0.0006662741428729615, "7": 0.00011907134597713809, "8": 1.871760327486151e-05, "9": 2.6251475763780235e-06} |
| Raw goal margin distribution | {"-1": 0.18400484604413225, "-10": 6.874266560809324e-08, "-11": 6.737342203076318e-09, "-12": 6.061620496939206e-10, "-13": 5.020159618609885e-11, "-14": 3.5521496804052115e-12, "-2": 0.08615113344561234, "-3": 0.02820786346246115, "-4": 0.007201360370198537, "-5": 0.001501352955481597, "-6": 0.00026402769345427166, "-7": 4.0108905381734126e-05, "-8": 5.359457227297344e-06, "-9": 6.389418259001566e-07, "0": 0.29168016729248253, "1": 0.2177626385226868, "10": 3.4902466976607595e-07, "11": 4.024216509857758e-08, "12": 4.259361002347691e-09, "13": 4.149886406904394e-10, "14": 3.4544023189853577e-11, "2": 0.1192303851500209, "3": 0.04592605268358178, "4": 0.013793244890758831, "5": 0.0033829663767349465, "6": 0.0006998860470377308, "7": 0.00012507820473424994, "8": 1.9661860671307966e-05, "9": 2.7575798637471847e-06} |
| Unadjusted home-win probability | 40.1% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.5% |
| Raw p btts yes | 48.7% |
| P home draw | 65.8% |
| P draw away | 61.8% |
| P home away | 72.3% |
| Raw p home draw | 69.3% |
| Raw p draw away | 59.9% |
| Raw p home away | 70.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4274 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:10:28Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:10:56Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:10:28Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:10:56Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.60 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.72 |
| Market reference 1x2 last update utc | 2026-10-28T16:10:56Z |
| Market reference home last update utc | 2026-10-28T16:10:56Z |
| Market reference draw last update utc | 2026-10-28T16:10:56Z |
| Market reference away last update utc | 2026-10-28T16:10:56Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-28T16:10:28Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:10:28Z |
| Home probability edge | +0.8% |
| Draw probability edge | +0.6% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -13.0% |
| Under 2.5 probability edge | +13.0% |
| Raw edge prob home | 0.0275 |
| Raw ev home | 0.0425 |
| Raw edge prob draw | 0.0216 |
| Raw ev draw | 0.0384 |
| Raw edge prob away | -0.0491 |
| Raw ev away | -0.1639 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09753298911177463, 0.10210347364746682, 0.06206060768301392, 0.023217793772179314, 0.006514590749749357, 0.001462323011502444, 0.0002735383633591828, 4.3857753709486584e-05, 6.1529385484284255e-06, 7.673018556310611e-07, 8.611770127701387e-08, 8.786702531747742e-09, 8.218089337829754e-10, 7.095021013911499e-11, 5.687898406103323e-12], [0.10725126774492, 0.1333036904416439, 0.07732224807571521, 0.02892739979268052, 0.008116626969505955, 0.0018219303175332322, 0.00034080557666973677, 5.464303749150543e-05, 7.666039031816147e-06, 9.559929663128338e-07, 1.0729534418777741e-07, 1.0947485342030714e-08, 1.023904157905923e-09, 8.8397937987035e-11, 7.086638497524096e-12], [0.07177518440372685, 0.08055648300888218, 0.04389714909089194, 0.01802054206735743, 0.005056314041265454, 0.0011349852446540664, 0.0002123074066519099, 3.404029269346981e-05, 4.775616884093465e-06, 5.955430349428536e-07, 6.684044461046493e-08, 6.819818633949976e-09, 6.378488243922494e-10, 5.506816276539614e-11, 4.414674947490466e-12], [0.029808595292803136, 0.03345551279557085, 0.01877430528712028, 0.006820377847394105, 0.0020999126673309355, 0.00047136508393894847, 8.817233442346625e-05, 1.4137104863996954e-05, 1.983337725343803e-06, 2.4733201949304183e-07, 2.7759173022492698e-08, 2.832304999542109e-09, 2.6490182675603925e-10, 2.2870085128010773e-11, 1.833436722625645e-12], [0.009284744728053823, 0.010420682122112944, 0.005847797600833234, 0.002187747812768392, 0.0005960779835669954, 0.00014682021863497355, 2.7463810661219926e-05, 4.403408096443594e-06, 6.177676038891414e-07, 7.703867429879736e-08, 8.646393191092434e-09, 8.822028899526228e-10, 8.251129633132309e-11, 7.123546085840125e-12, 5.710766232828387e-13], [0.0023136007267255997, 0.002596657036552746, 0.0014571718636650014, 0.0005451496059142868, 0.0001529614146273541, 3.3340929356662e-05, 6.843515267842091e-06, 1.0972545256111465e-06, 1.5393719689319228e-07, 1.9196729480901367e-08, 2.154534363236052e-09, 2.1982997993975444e-10, 2.0560413963608736e-11, 1.775066723295645e-12, 1.4230259736178263e-13], [0.00048042501252367153, 0.0005392023675023206, 0.0003025854041121374, 0.00011320168740580983, 3.1762822637936034e-05, 7.12976581921307e-06, 1.2950598199718334e-06, 2.278476632199432e-07, 3.196544628075842e-08, 3.986249180656228e-09, 4.4739448189286727e-10, 4.564824848369824e-11, 4.26942169487403e-12, 3.6859707162030384e-13, 2.9549492412393163e-14], [8.550982519233894e-05, 9.597148147266152e-05, 5.385653189759188e-05, 2.014852734394558e-05, 5.653397180795932e-06, 1.2690118394557638e-06, 2.3737807510223635e-07, 3.695799293139759e-08, 5.689461731612224e-09, 7.095040052566439e-10, 7.963079136474215e-11, 8.12483456611277e-12, 7.599052782104462e-13, 6.560580806376567e-14, 5.259451245956069e-15], [1.3317247774554764e-05, 1.4946539712690605e-05, 8.387583274146385e-06, 3.1379193014156104e-06, 8.804566125036827e-07, 1.9763512621927347e-07, 3.696911594980753e-08, 5.927440532555488e-09, 8.075009330915515e-10, 1.1049771899063903e-10, 1.240165064894972e-11, 1.2653567563822466e-12, 1.1834718235428166e-13, 1.021740834424401e-14, 8.191037140239992e-16], [1.8435733400223067e-06, 2.069124387138792e-06, 1.1611351814733557e-06, 4.3439789250483095e-07, 1.2188602069562446e-07, 2.7359620840423817e-08, 5.11781996723698e-09, 8.20565294374593e-10, 1.1511961749577384e-10, 1.3940316778011513e-11, 1.716822642014591e-12, 1.7516967628556437e-13, 1.638339347203492e-14, 1.414447034886642e-15, 1.1339263152955695e-16], [2.2969358577839927e-07, 2.577953312655798e-07, 1.4466758529001096e-07, 5.412228926179143e-08, 1.518596333655997e-08, 3.4087764668468947e-09, 6.37636916374983e-10, 1.022354688791103e-10, 1.4342926946276027e-11, 1.7886338981671312e-12, 1.9493385501501741e-13, 2.182465443180355e-14, 2.041231727599503e-15, 1.7622809154574036e-16, 1.4127759157418475e-17], [2.6016246030262692e-08, 2.9199190482092776e-08, 1.6385775330879444e-08, 6.130161573228514e-09, 1.7200382719944771e-09, 3.860950967486631e-10, 7.222195098819189e-11, 1.1579701289283144e-11, 1.6245517477723709e-12, 2.025896343386703e-13, 2.2737536060626758e-14, 2.25276831887422e-15, 2.3120012972952993e-16, 1.996047635183376e-17, 1.6001807662591724e-18], [2.7011694759011772e-09, 3.0316426881690587e-09, 1.7012737391574843e-09, 6.364717378781647e-10, 1.7858513762088586e-10, 4.0086809177598715e-11, 7.498534925923167e-12, 1.2022770551247475e-12, 1.6867112910910335e-13, 2.1034123669227608e-14, 2.360753288261671e-15, 2.408707685784144e-16, 2.1876037874275413e-17, 2.072421570095224e-18, 1.6614078129164234e-19], [2.588790639292656e-10, 2.905514919678892e-10, 1.630494335915723e-10, 6.099921133766e-11, 1.7115532243140678e-11, 3.8419046743987115e-12, 7.186567595194141e-13, 1.1522577957108369e-13, 1.6165377406054506e-14, 2.0159024802563958e-15, 2.262537048806323e-16, 2.3084963625504854e-17, 2.159106817938601e-18, 1.81007508597342e-19, 1.5922869825451396e-20], [2.3038666727887126e-11, 2.5857320747140735e-11, 1.451041078282554e-11, 5.428559881753467e-12, 1.5231785731729375e-12, 3.419062169429357e-13, 6.395609333180763e-14, 1.0254395599655446e-14, 1.4386205548485998e-15, 1.7940309538216704e-16, 2.0135207627754972e-17, 2.054421764823445e-18, 1.921474129788561e-19, 1.6588891612289712e-20, 1.2913832473421768e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2459150975551665, "lambda_away": 1.1223444938261888, "rho": -0.061598984472994917, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3782 |
| Legacy p draw | 0.2822 |
| Legacy p away | 0.3396 |
| Legacy p over 1 5 | 0.6931 |
| Legacy p under 3 5 | 0.7849 |
| Legacy p btts yes | 0.4858 |
| Legacy p over 2 5 | 0.4260 |
| Legacy goal margin distribution | {"-1": 0.19970007384113475, "-10": 9.772647660518812e-08, "-11": 9.867508289141686e-09, "-12": 9.146215467175009e-10, "-13": 7.803684863663909e-11, "-14": 5.687898406103323e-12, "-2": 0.09654428035361481, "-3": 0.032562139733218025, "-4": 0.008563602998770958, "-5": 0.0018392314582181407, "-6": 0.00033321322031329236, "-7": 5.214799808642852e-05, "-8": 7.178688580263813e-06, "-9": 8.816891861282277e-07, "0": 0.28218495824407963, "1": 0.20893013845658426, "10": 2.6065657238956036e-07, "11": 2.9216366711905076e-08, "12": 3.0062313786518923e-09, "13": 2.8473638467640634e-10, "14": 2.3038666727887126e-11, "2": 0.11165671404475176, "3": 0.04180550721999516, "4": 0.012205044161683321, "5": 0.002909922913664663, "6": 0.0005852340548366169, "7": 0.00010167338322975702, "8": 1.5537352399555186e-05, "9": 2.1184083757951046e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3830 |
| Legacy raw p draw | 0.2943 |
| Legacy raw p away | 0.3227 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2459 |
| Legacy lambda away | 1.1223 |
| Legacy model home team | Lille |
| Legacy model away team | Lens |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015445853721645362, "mu": 8.924214617605585, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,569.6537 |
| Elo away rating | 1,580.6843 |
| Elo rating diff | 48.9694 |
| Elo home expectancy | 0.5700 |

</details>


---

## 2026-10-30 — Nice vs Rennes

The model's most likely 1X2 outcome is **Rennes win** at **39.8%**. Expected goals are 1.44 for Nice and 1.50 for Rennes (2.95 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 56.7%; Under 3.5 goals: 65.8%; Double Chance 1X: 60.2%; Double Chance X2: 65.0%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 35.0% | 2.86 |
| Draw | 25.2% | 3.97 |
| Rennes win | 39.8% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nice expected goals | 1.44 |
| Rennes expected goals | 1.50 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.0% |
| Under 1.5 | 20.0% |
| Over 2.5 | 56.7% |
| Under 2.5 | 43.3% |
| Over 3.5 | 34.2% |
| Under 3.5 | 65.8% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.75% |
| 2 | 1-2 | 8.87% |
| 3 | 2-1 | 8.05% |
| 4 | 0-1 | 7.50% |
| 5 | 1-0 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 35.0% | 34.7% | 2.79 | -2.3% |
| Draw | 25.2% | 25.0% | 3.84 | -3.2% |
| Rennes win | 39.8% | 40.4% | 2.41 | -4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T18:00:00+00:00 |
| Fixture id | a547720e6b4661d6319c4f11dbdf8e1f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:10:56Z |
| Market best draw last update utc | 2026-10-28T16:10:56Z |
| Market best away last update utc | 2026-10-28T16:10:56Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Nice |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4444 |
| Dc lambda away | 1.5038 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:10:42.048441+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.40 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.99 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.93 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.65 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.20225586227513356, "-10": 1.0761970864978067e-06, "-11": 1.4477454286323854e-07, "-12": 1.789590898788693e-08, "-13": 2.0450724633884433e-09, "-14": 2.1560445164537402e-10, "-15": 1.8880824647161617e-11, "-2": 0.11981464830706218, "-3": 0.05158282042146624, "-4": 0.01760387875017572, "-5": 0.004952914068537497, "-6": 0.0011824239085021886, "-7": 0.00024479310546793813, "-8": 4.469733049279049e-05, "-9": 7.295640732015784e-06, "0": 0.2521163461661168, "1": 0.18340273880986474, "10": 6.800082950712308e-07, "11": 8.786543361897892e-08, "12": 1.0432372186971644e-08, "13": 1.1450948648447404e-09, "14": 1.159561922164437e-10, "15": 9.753503329480363e-12, "2": 0.10449720368026268, "3": 0.04321189301055681, "4": 0.014164786468845406, "5": 0.0038279469674982187, "6": 0.0008777721100072673, "7": 0.00017454652733677758, "8": 3.061237838912379e-05, "9": 4.799349550472113e-06} |
| Raw goal margin distribution | {"-1": 0.1953387179796471, "-10": 1.0393911790993803e-06, "-11": 1.3982325793120597e-07, "-12": 1.728386944858441e-08, "-13": 1.975131047773302e-09, "-14": 2.0823078600224152e-10, "-15": 1.8235101022476096e-11, "-2": 0.11571699100442484, "-3": 0.04981868954283648, "-4": 0.01700182663605915, "-5": 0.004783524559082319, "-6": 0.0011419850470445335, "-7": 0.0002364211887580107, "-8": 4.316868315884525e-05, "-9": 7.046130042418402e-06, "0": 0.25813794888749664, "1": 0.18737221539005064, "10": 6.947260523911788e-07, "11": 8.976714884538017e-08, "12": 1.0658165200427662e-08, "13": 1.169878721823041e-09, "14": 1.1846588968507249e-10, "15": 9.964603247029984e-12, "2": 0.10675888856782446, "3": 0.04414714947621257, "4": 0.014471361978656661, "5": 0.003910797125223671, "6": 0.0008967701678117715, "7": 0.00017832432453278565, "8": 3.127493730110051e-05, "9": 4.90322425683882e-06} |
| Unadjusted home-win probability | 35.8% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 79.9% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 60.1% |
| P home draw | 60.2% |
| P draw away | 65.0% |
| P home away | 74.8% |
| Raw p home draw | 61.6% |
| Raw p draw away | 64.2% |
| Raw p home away | 74.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5672 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:10:28Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:10:56Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:10:28Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:10:56Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.79 |
| Reference draw odds | 3.84 |
| Reference away odds | 2.41 |
| Market reference 1x2 last update utc | 2026-10-28T16:10:56Z |
| Market reference home last update utc | 2026-10-28T16:10:56Z |
| Market reference draw last update utc | 2026-10-28T16:10:56Z |
| Market reference away last update utc | 2026-10-28T16:10:56Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-28T16:10:28Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:10:28Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.0108 |
| Raw ev home | -0.0018 |
| Raw edge prob draw | 0.0086 |
| Raw ev draw | -0.0088 |
| Raw edge prob away | -0.0194 |
| Raw ev away | -0.0743 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.07486767696353898, 0.09104022267079764, 0.06461956736821435, 0.02805005225411452, 0.009131971903052104, 0.0023784030085263227, 0.0005162084132377104, 9.603243074405951e-05, 1.563215375486354e-05, 2.2618676639627262e-06, 2.945493543984377e-07, 3.48703473356161e-08, 3.784128804629998e-09, 3.7906478591968634e-10, 3.525951134060729e-11], [0.0848772437758381, 0.12539190910150863, 0.0867137308925565, 0.03764068349182213, 0.012254296745867074, 0.003191605992349085, 0.0006927059287615493, 0.0001288670087970067, 2.0976964550788223e-05, 3.0352258907866957e-06, 3.952591218437336e-07, 4.679291487299452e-08, 5.0779653933254835e-09, 5.086713386640944e-10, 4.731513846835823e-11], [0.06191552327993417, 0.08062884358758228, 0.05160166778382935, 0.025255230202355608, 0.00822208994563261, 0.0021414261531543665, 0.00046477497405726805, 8.646405088166054e-05, 1.4074613411095735e-05, 2.0365020365430426e-06, 2.652013509242784e-07, 3.139597178710791e-08, 3.407089698461321e-09, 3.412959214221805e-10, 3.174636067207269e-11], [0.027695047813071277, 0.03606558678628536, 0.023483016873962127, 0.010019266731976933, 0.003677771939972691, 0.0009578680201349749, 0.0002078956043161893, 3.8675697085733536e-05, 6.2956278283949775e-06, 9.109350658069179e-07, 1.1862556762593503e-07, 1.4043536963267268e-08, 1.5240041124370067e-09, 1.52662956904328e-10, 1.420026723716634e-11], [0.009291074750759005, 0.012099205064495732, 0.007878031719675936, 0.0034196948447101313, 0.0010942855524594369, 0.0003213434920388624, 6.974436776903788e-05, 1.2974839223482572e-05, 2.1120436097954384e-06, 3.055985260117545e-07, 3.979624890351667e-08, 4.7112954117804646e-09, 5.112696040348922e-10, 5.121503865397068e-11, 4.763874945144401e-12], [0.00249355973260892, 0.003247212120744139, 0.0021143240362795413, 0.0009177854652264952, 0.00029879413434064333, 7.649012422833432e-05, 1.8718151743524944e-05, 3.482216804047121e-06, 5.668350583951185e-07, 8.201722612825811e-08, 1.0680607619326756e-08, 1.2644281573863366e-09, 1.372156969272222e-10, 1.3745208333526536e-11, 1.2785395719075654e-12], [0.0005576893512400808, 0.0007262451335232344, 0.00047287257035962796, 0.00020526445546352378, 6.68258733711711e-05, 1.740465914270625e-05, 3.7129369549461257e-06, 7.788043754999639e-07, 1.2677373308629922e-07, 1.8343307774754226e-08, 2.3887380984614217e-09, 2.827917493055985e-10, 3.068855018733966e-11, 3.074141845466832e-12, 2.859477938576935e-13], [0.00010690995289734172, 0.0001392223696655596, 9.065043847650824e-05, 3.9349528938121606e-05, 1.2810628279972372e-05, 3.3365013784170022e-06, 7.241540126478579e-07, 1.324147011073438e-07, 2.430273018973569e-08, 3.51644184315111e-09, 4.579249666911019e-10, 5.421163687416945e-11, 5.883044830819774e-12, 5.893179763389857e-13, 5.481665573217009e-14], [1.7932959904487196e-05, 2.335300975595373e-05, 1.5205606535851596e-05, 6.60044743809198e-06, 2.1488409364152527e-06, 5.596611336820269e-07, 1.214688111027168e-07, 2.2597355817239014e-08, 3.61552143063893e-09, 5.898441526790522e-10, 7.681183878942064e-11, 9.093401353890907e-12, 9.868155789825896e-13, 9.885156016136772e-14, 9.194886562965898e-15], [2.6738269374934063e-06, 3.4819632057165946e-06, 2.267175110691712e-06, 9.84135037019944e-07, 3.203948935801715e-07, 8.344618083558322e-08, 1.8111152922974753e-08, 3.3692942504788803e-09, 5.484535313829037e-10, 7.800108266203995e-11, 1.1452742032962615e-11, 1.3558376097962839e-12, 1.4713544732576884e-13, 1.4738892284400786e-14, 1.3709691824550708e-15], [3.588038715733024e-07, 4.672485946521669e-07, 3.042348013792582e-07, 1.320621976247713e-07, 4.29941544222195e-08, 1.1197737718912111e-08, 2.4303561671464754e-09, 4.521294196679741e-10, 7.359760187871952e-11, 1.0649078715905405e-11, 1.3630611519439632e-12, 1.819413877532599e-13, 1.9744272677440532e-14, 1.97782868449313e-15, 1.8397191066288962e-16], [4.3771180703496656e-08, 5.700056295461844e-08, 3.7114193916225245e-08, 1.611052381064904e-08, 5.244940346259732e-09, 1.3660337582637505e-09, 2.964838659615547e-10, 5.5156145453159884e-11, 8.978314300377621e-12, 1.2991017815827227e-12, 1.6917417281286043e-13, 1.9685419745965297e-14, 2.4086421460109635e-15, 2.4127916003220017e-16, 2.244309045686468e-17], [4.894753682921694e-09, 6.374141866098677e-09, 4.1503298389572844e-09, 1.801574563184506e-09, 5.865204151211885e-10, 1.5275801707406798e-10, 3.3154588738938266e-11, 6.167888134464969e-12, 1.0040084887335747e-12, 1.452732854744354e-13, 1.8918061887346575e-14, 2.2396225932177934e-15, 2.3888940953421144e-16, 2.6981270283292153e-17, 2.50971981802418e-18], [5.052558094810152e-10, 6.579641013478222e-10, 4.284134398247964e-10, 1.8596564265085942e-10, 6.054295401077448e-11, 1.5768285918200248e-11, 3.4223476106163014e-12, 6.366737764641265e-13, 1.036377220514384e-13, 1.499568235771563e-14, 1.952797074560401e-15, 2.3118269060533833e-16, 2.50879370438043e-17, 2.4701589599447287e-18, 2.590631930368046e-19], [4.842917896191779e-11, 6.306639254167428e-11, 4.106377553239287e-11, 1.7824957614950348e-11, 5.803091225576747e-12, 1.5114029889920576e-12, 3.280347930579436e-13, 6.102569764098831e-14, 9.933759680250039e-15, 1.4373483113511261e-15, 1.871771827766559e-16, 2.2159048319946707e-17, 2.4046991050488413e-18, 2.408841766541634e-19, 2.2023358081328644e-20]] |
| Legacy trial inputs | {"lambda_home": 1.341911350140206, "lambda_away": 1.3022395566785563, "rho": -0.061598984472994917, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3589 |
| Legacy p draw | 0.2631 |
| Legacy p away | 0.3780 |
| Legacy p over 1 5 | 0.7492 |
| Legacy p under 3 5 | 0.7258 |
| Legacy p btts yes | 0.5423 |
| Legacy p over 2 5 | 0.4973 |
| Legacy goal margin distribution | {"-1": 0.20702782105805181, "-10": 3.44906785801743e-07, "-11": 4.0303808917600936e-08, "-12": 4.324546503966165e-09, "-13": 4.2637992438804455e-10, "-14": 3.525951134060729e-11, "-2": 0.11151356577873973, "-3": 0.042667231242209294, "-4": 0.012829225071331586, "-5": 0.0031641851839065748, "-6": 0.0006601020624757437, "-7": 0.00011916937453908392, "-8": 1.894714983429794e-05, "-9": 2.6900992552842306e-06, "0": 0.2630551453041033, "1": 0.1927257451862185, "10": 4.201465331007546e-07, "11": 5.0591560967035075e-08, "12": 5.593781559801909e-09, "13": 5.683222020226895e-10, "14": 4.842917896191779e-11, "2": 0.10684721453889277, "3": 0.04212723023113163, "4": 0.013052743744449646, "5": 0.0033173876474348824, "6": 0.0007131458564678888, "7": 0.00013266760114334858, "8": 2.1735871052129532e-05, "9": 3.180053354981983e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3709 |
| Legacy raw p draw | 0.2766 |
| Legacy raw p away | 0.3525 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3419 |
| Legacy lambda away | 1.3022 |
| Legacy model home team | Nice |
| Legacy model away team | Rennes |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015445853721645362, "mu": 10.005841990679913, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,480.4127 |
| Elo away rating | 1,532.6617 |
| Elo rating diff | 7.7510 |
| Elo home expectancy | 0.5112 |

</details>


---
