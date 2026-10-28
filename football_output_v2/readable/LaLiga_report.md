# La Liga — football model report

Fixtures in this report: **3**.

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
| Training sha256 | f6dfad4b9b5be442ce7c37ab610104a316a9fe7634c5d0f12fc06265e7859543 |
| Training as of utc | 2026-10-28T15:59:44.737672+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 99, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 99, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 82, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-10-28T15:59:44.737672+00:00', 'observations': 385, 'observations_sha256': 'e9aba83339f7cd22cbb96ddc5864adef18c0911a1bfa03e0cc0fa7f6b0243bc7', 'eligible_training_matches': 140, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 153, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 20, 'retrospective_eligible_training_matches': 140, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '399eac33c0d3f071a8265fdfd4d8ddc53472a8540086322c85ce6a9ee576f360', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 80, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-20T00:00:00+00:00', 'audit_origin_utc': '2026-09-18T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 16, 'selected_ridge': 1.0, 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8175310728786089, 'audit_candidate_poisson_score': 0.8069323340505633, 'audit_gain': 0.010598738828045629, 'audit_gain_lower95': -0.01699136798163119, 'audit_baseline_briers': [0.5520932991942327, 0.18075667919310287, 0.22581865901120918, 0.25218525802844377], 'audit_candidate_briers': [0.5384658625434342, 0.1851688742905936, 0.2282336223405601, 0.2528553522553332], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1620, 'tuning_matches': 230, 'audit_matches': 135, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8136086322866952, 'audit_candidate_poisson_score': 0.8149346424284629, 'audit_gain': -0.0013260101417676973, 'audit_gain_lower95': -0.011138687548691902, 'audit_baseline_briers': [0.5676553269378789, 0.185585577181464, 0.20276536605746645, 0.2468256124387469], 'audit_candidate_briers': [0.5713050151595686, 0.18224292681030685, 0.2047833973410357, 0.24417579734749942], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1838.810 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.288 |
| Dixon-Coles low-score adjustment | -0.033 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1999, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 3.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261028T155944737672Z_1744bdb8ebd7b818e7e971ba125d41c592f98d6607cfa61200a8cdc3ccc1c94a.json |
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
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **67.9%**. Expected goals are 2.16 for Villarreal and 0.95 for Espanyol (3.12 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 61.0%; Under 3.5 goals: 61.7%; Double Chance 1X: 86.4%; Double Chance X2: 32.1%; Double Chance 12 (either team wins): 81.4%; Under 4.5 goals: 79.1%; BTTS Yes (both teams score): 54.1%; BTTS No (at least one team does not score): 45.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 67.9% | 1.47 |
| Draw | 18.6% | 5.39 |
| Espanyol win | 13.6% | 7.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.16 |
| Espanyol expected goals | 0.95 |
| Expected total goals | 3.12 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 82.4% |
| Under 1.5 | 17.6% |
| Over 2.5 | 61.0% |
| Under 2.5 | 39.0% |
| Over 3.5 | 38.3% |
| Under 3.5 | 61.7% |
| Over 4.5 | 20.9% |
| Under 4.5 | 79.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.89% |
| 2 | 2-1 | 10.36% |
| 3 | 1-0 | 9.75% |
| 4 | 1-1 | 8.71% |
| 5 | 3-0 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 67.9% | 69.2% | 1.42 | -3.6% |
| Draw | 18.6% | 17.9% | 5.16 | -4.3% |
| Espanyol win | 13.6% | 12.9% | 7.06 | -4.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:00:00+00:00 |
| Fixture id | 00b03cb40c27ed23e2ecb18f062a5122 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:00:15Z |
| Market best draw last update utc | 2026-10-28T16:00:15Z |
| Market best away last update utc | 2026-10-28T16:00:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1640 |
| Dc lambda away | 0.9515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T15:59:44.737672+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.1% |
| P btts no | 45.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.88 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.67 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.61 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.79 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.08989016813296845, "-10": 8.012332147128196e-09, "-11": 6.82554090388097e-10, "-12": 5.3423312748640034e-11, "-13": 3.866832958447924e-12, "-14": 2.602727488523979e-13, "-15": 1.6366252962840183e-14, "-16": 9.601194786290789e-16, "-17": 4.793261074074646e-17, "-2": 0.033954834902152675, "-3": 0.009312221524429662, "-4": 0.0020199654792484828, "-5": 0.0003607563831724087, "-6": 5.462424625020517e-05, "-7": 7.168558857642132e-06, "-8": 8.294088414227624e-07, "-9": 8.576006489792866e-08, "0": 0.18551215422550446, "1": 0.24343311434107126, "10": 3.475040230381238e-05, "11": 6.7327247790143565e-06, "12": 1.198498510702581e-06, "13": 1.9729450573862824e-07, "14": 3.0202380469802434e-08, "15": 4.319312544288955e-09, "16": 5.762932694779931e-10, "17": 6.543381577561473e-11, "2": 0.20572134231109393, "3": 0.12831691822924127, "4": 0.0633034625096047, "5": 0.025712863107713035, "6": 0.008854718651684742, "7": 0.0026428594067708904, "8": 0.0006954465570247994, "9": 0.0001635434283317098} |
| Raw goal margin distribution | {"-1": 0.10043476668670374, "-10": 8.952221655908277e-09, "-11": 7.626213438357266e-10, "-12": 5.969015369515784e-11, "-13": 4.320433191577663e-12, "-14": 2.908041374138921e-13, "-15": 1.828610216221815e-14, "-16": 1.0727466399309622e-15, "-17": 5.355536291032726e-17, "-2": 0.03793791904181003, "-3": 0.010404595024869802, "-4": 0.0022569182574385454, "-5": 0.0004030750406547654, "-6": 6.103196313373319e-05, "-7": 8.009469236748831e-06, "-8": 9.267029443416119e-07, "-9": 9.582018020390144e-08, "0": 0.20090649480470663, "1": 0.23220929653213354, "10": 3.314818731633616e-05, "11": 6.422303263511328e-06, "12": 1.1432400921229217e-06, "13": 1.8819797179702074e-07, "14": 2.8809858270401367e-08, "15": 4.120164711882576e-09, "16": 5.497224774201981e-10, "17": 6.241689990204089e-11, "2": 0.19623627750485423, "3": 0.12240069062024185, "4": 0.060384769496922626, "5": 0.024527336267421384, "6": 0.008446459696591777, "7": 0.0025210067469282646, "8": 0.0006633820391262072, "9": 0.00015600303413179683} |
| Unadjusted home-win probability | 64.8% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 15.2% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 54.6% |
| P home draw | 86.4% |
| P draw away | 32.1% |
| P home away | 81.4% |
| Raw p home draw | 84.8% |
| Raw p draw away | 35.2% |
| Raw p home away | 79.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6097 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:00:15Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:59:50Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.28, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:59:50Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.74, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:00:15Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.42 |
| Reference draw odds | 5.16 |
| Reference away odds | 7.06 |
| Market reference 1x2 last update utc | 2026-10-28T16:00:15Z |
| Market reference home last update utc | 2026-10-28T16:00:15Z |
| Market reference draw last update utc | 2026-10-28T16:00:15Z |
| Market reference away last update utc | 2026-10-28T16:00:15Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-28T16:00:17Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:00:17Z |
| Home probability edge | -1.3% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.0447 |
| Raw ev home | -0.0804 |
| Raw edge prob draw | 0.0220 |
| Raw ev draw | 0.0367 |
| Raw edge prob away | 0.0227 |
| Raw ev away | 0.0696 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.040705487501830964, 0.03486678700849665, 0.017943548228138314, 0.005856196040443777, 0.0014334552854906924, 0.0002807001734655722, 4.5805746541901085e-05, 6.4069371051372674e-06, 7.84131695194198e-07, 8.530510744398033e-08, 8.352251618657115e-09, 7.434288647335883e-10, 6.06578074560699e-11, 4.568481713999403e-12, 3.1950112395601814e-13, 2.0854974648709152e-14, 1.2761984670812486e-15, 7.350177589036864e-17], [0.0907280760102316, 0.08664505383220326, 0.039996415259752005, 0.013053541345228485, 0.003195191504256935, 0.00062568453901485, 0.00010210163768500691, 1.4281150736861293e-05, 1.7478403100975957e-06, 1.9014625522932e-07, 1.8617283485207622e-08, 1.6571131423907695e-09, 1.352070852940086e-10, 1.0183208438850765e-11, 7.121723901665709e-13, 4.64860247079412e-14, 2.844663897812392e-15, 1.638364672060976e-16], [0.1033289693814284, 0.10116973972947145, 0.0462628360702754, 0.01454826140337654, 0.0035610628570743722, 0.0006973297122138051, 0.00011379297582699935, 1.5916440494274538e-05, 1.947980019380209e-06, 2.1191930624714932e-07, 2.074909019708817e-08, 1.8468639683961304e-09, 1.5068922435863588e-10, 1.1349255682836136e-11, 7.937210158067944e-13, 5.180899352666138e-14, 3.1703974343521954e-15, 1.82596866956054e-16], [0.07677389694978584, 0.07516957944054667, 0.03679939339906346, 0.011218402583346858, 0.002645885993612515, 0.0005181191662514422, 8.454870160857062e-05, 1.1825988100239963e-05, 1.4473580658302563e-06, 1.5745701400959657e-07, 1.541666893736938e-08, 1.3722283773731469e-09, 1.119627830569691e-10, 8.432548891825481e-12, 5.897383457826548e-13, 3.849431920108674e-14, 2.3556197973515114e-15, 1.356703074748509e-16], [0.042782517488622045, 0.04188850605214098, 0.020506588231359896, 0.006692689722046155, 0.0015302145103277495, 0.0002887236830747386, 4.7115054060298676e-05, 6.5900724441494405e-06, 8.065452481092774e-07, 8.774346129619728e-08, 8.590991660364605e-09, 7.64678971444524e-10, 6.239164500588684e-11, 4.6990668022771295e-12, 3.2863371659588326e-13, 2.1451091449874442e-14, 1.3126772142705005e-15, 7.560274432892039e-17], [0.019072563726823897, 0.018674010974538354, 0.009141893320475228, 0.0029836194483303154, 0.0007303179467635815, 0.00013358373577178022, 2.1004020422519132e-05, 2.937872384177796e-06, 3.595600854302751e-07, 3.911627588602966e-08, 3.829887662933647e-09, 3.408959843776498e-10, 2.781436659758559e-11, 2.0948568785571893e-12, 1.4650581289950744e-13, 9.562955447782247e-15, 5.851951051871154e-16, 3.370391093791032e-17], [0.007085501050175864, 0.006937437791071476, 0.003396234279281642, 0.001108421449641686, 0.0002713147877166569, 5.3129043330968275e-05, 8.098272035240255e-06, 1.091426310669401e-06, 1.3357739417771464e-07, 1.4531785964339592e-08, 1.4228120270798507e-09, 1.2664363794530137e-10, 1.0333100812241365e-11, 7.782441220584078e-13, 5.442724460248509e-14, 3.552659822693367e-15, 2.1740132012402353e-16, 1.2521080006131173e-17], [0.0022562398690055174, 0.0022090920066369243, 0.0010814646884017142, 0.0003529552319070493, 8.639491219635004e-05, 1.6917909533367025e-05, 2.760730307134163e-06, 3.606928711369079e-07, 4.2535120693284604e-08, 4.6273643357633814e-09, 4.530667907414167e-10, 4.032720100732986e-11, 3.2903747890141943e-12, 2.4781668982517386e-13, 1.733129645491962e-14, 1.1312753574111594e-15, 6.922721802801494e-17, 3.987094167763874e-18], [0.0006286487041122125, 0.0006155120500769566, 0.0003013249540734859, 9.834275698966006e-05, 2.4071930622369053e-05, 4.713781566641051e-06, 7.692132178960971e-07, 1.0759131942085803e-07, 1.2299823015907734e-08, 1.2893073263592819e-09, 1.2623651181264281e-10, 1.1236235562535678e-11, 9.167863202723196e-13, 6.904835033548144e-14, 4.828962206829598e-15, 3.1520353717713094e-16, 1.9288552383301042e-17, 1.1109109524081331e-18], [0.00015569628767890683, 0.0001524427563307432, 7.462860644962784e-05, 2.435637277741981e-05, 5.961851524787465e-06, 1.1674537560555764e-06, 1.9050964660636727e-07, 2.6646947509356424e-08, 3.2612644356237674e-09, 3.3140199688282666e-10, 3.1264768590463296e-11, 2.782858141802908e-12, 2.2705880999593475e-13, 1.710108005832794e-14, 1.195980336914694e-15, 7.80658900284309e-17, 4.777160886732768e-18, 2.751373065757743e-19], [3.470491620292787e-05, 3.397969960023995e-05, 1.663481879874325e-05, 5.429068919041056e-06, 1.3289048869858026e-06, 2.6022704445117725e-07, 4.246486168609591e-08, 5.939641170399709e-09, 7.269403184957579e-10, 7.908329985218119e-11, 7.232632498098842e-12, 6.203028990330233e-13, 5.0611720366104765e-14, 3.8118542147118644e-15, 2.665856584748682e-16, 1.740099402582428e-17, 1.0648357178809348e-18, 6.132848323720911e-20], [7.032521319128891e-06, 6.885565159097629e-06, 3.370839945498516e-06, 1.100133557243836e-06, 2.6928611192075983e-07, 5.273178667875342e-08, 8.604978135522335e-09, 1.2035946986464027e-09, 1.473054496850931e-10, 1.60252509744025e-11, 1.5690376860287848e-12, 1.3045246973674695e-13, 1.0255838117897367e-14, 7.72425032627249e-16, 5.402028103558307e-17, 3.526095863338226e-18, 2.1577576627993203e-19, 1.2427457346781484e-20], [1.3062988779529412e-06, 1.279001603156924e-06, 6.261373750245665e-07, 2.043510664542162e-07, 5.002020326530225e-08, 9.79498968364904e-09, 1.5983845299788986e-09, 2.2356909179575117e-10, 2.736215574869042e-11, 2.976708696187685e-12, 2.9145054465034535e-13, 2.5941836696034448e-14, 1.9771111757983695e-15, 1.4347883321436202e-16, 1.003432898405002e-17, 6.549763393257351e-19, 4.0080595364028824e-20, 2.308414415147421e-21], [2.2398139436513451e-07, 2.1930093281504782e-07, 1.0735913862369537e-07, 3.503856397407584e-08, 8.576593812395099e-09, 1.6794743409515922e-09, 2.740631579790969e-10, 3.833373645381256e-11, 4.6915862065438e-12, 5.103941951138673e-13, 4.997286645576827e-14, 4.4480546172372436e-15, 3.629254301595446e-16, 2.553204868464187e-17, 1.7205120782833381e-18, 1.123039422557282e-19, 6.872322856686498e-21, 3.958067240228634e-22], [3.566125728465733e-08, 3.491605635392069e-08, 1.7093213814346877e-08, 5.578674283666068e-09, 1.3655246652818916e-09, 2.6739795394799094e-10, 4.3635038600597343e-11, 6.1033160465691465e-12, 7.469721458736998e-13, 8.126254754392435e-14, 7.956443225930643e-15, 7.081981991009384e-16, 5.778326890387059e-17, 4.351983997338286e-18, 2.842960790276016e-19, 1.7880502039977638e-20, 1.094178711719269e-21, 6.301847285300166e-23], [5.29929546043486e-09, 5.188557920312754e-09, 2.5400672120885166e-09, 8.289961027087878e-10, 2.0291821463494694e-10, 3.973558060993571e-11, 6.4842066595204e-12, 9.069583486922733e-13, 1.1100074431203052e-13, 1.2075688915437191e-14, 1.1823347430468226e-15, 1.0523890034573715e-16, 8.586646627378176e-18, 6.467088038116418e-19, 4.522819672384893e-20, 2.757589580157919e-21, 1.6259595767009155e-22, 9.364602724120085e-24], [7.3826264433898e-10, 7.22835425794832e-10, 3.5386529224421224e-10, 1.1549023063572988e-10, 2.826921783082604e-11, 5.535697157189379e-12, 9.033366021273192e-13, 1.263514129019572e-13, 1.546388640362204e-14, 1.6823047700371105e-15, 1.647150230464726e-16, 1.4661184573806488e-17, 1.1962345735318564e-18, 9.009517494993618e-20, 6.3008919508881845e-21, 4.1128162640866825e-22, 2.35088259989337e-23, 1.3046142495564088e-24], [9.679985683702454e-11, 9.47770637864509e-11, 4.6398270170505214e-11, 1.514290053456972e-11, 3.706616147927638e-12, 7.258320550525012e-13, 1.1844409903722356e-13, 1.656700196583338e-14, 2.0276008836325572e-15, 2.2058120120874374e-16, 2.1597179231629567e-17, 1.922351860395664e-18, 1.5684842833279576e-19, 1.1813140084677078e-20, 8.26163213686163e-22, 5.392661116113259e-23, 3.299982841407277e-24, 1.7753107231119214e-25]] |
| Legacy trial inputs | {"lambda_home": 2.2290137241101133, "lambda_away": 0.9791033466714802, "rho": -0.021863316965005233, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6735 |
| Legacy p draw | 0.1865 |
| Legacy p away | 0.1400 |
| Legacy p over 1 5 | 0.8337 |
| Legacy p under 3 5 | 0.5980 |
| Legacy p btts yes | 0.5560 |
| Legacy p over 2 5 | 0.6258 |
| Legacy goal margin distribution | {"-1": 0.09236821265136913, "-10": 1.0168824952358804e-08, "-11": 8.905969928638506e-10, "-12": 7.167457761105376e-11, "-13": 5.334894320234316e-12, "-14": 3.692932164057864e-13, "-15": 2.3882235413477597e-14, "-16": 1.4400349342873462e-15, "-17": 7.350177589036864e-17, "-2": 0.03512646285696636, "-3": 0.009840230587372581, "-4": 0.0021856059140301625, "-5": 0.0004002573130639177, "-6": 6.220127678562255e-05, "-7": 8.382906679652885e-06, "-8": 9.964638110779474e-07, "-9": 1.0588606687625418e-07, "0": 0.1865040498372525, "1": 0.23617621751447682, "10": 4.225306348117363e-05, "11": 8.424669307549067e-06, "12": 1.5435510157349307e-06, "13": 2.6155671477792735e-07, "14": 4.1218823397748864e-08, "15": 6.0685291564001976e-09, "16": 8.330397081254309e-10, "17": 9.679985683702454e-11, "2": 0.20227778580234224, "3": 0.12900402306542735, "4": 0.0652310010550645, "5": 0.02719603987517726, "6": 0.009621657657814838, "7": 0.0029520889558319256, "8": 0.0007988781570342305, "9": 0.0001932600288954515} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6547 |
| Legacy raw p draw | 0.1941 |
| Legacy raw p away | 0.1512 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2290 |
| Legacy lambda away | 0.9791 |
| Legacy model home team | Villarreal |
| Legacy model away team | Espanol |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 10.163900130311859, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,563.5990 |
| Elo away rating | 1,432.0064 |
| Elo rating diff | 191.5927 |
| Elo home expectancy | 0.7508 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **58.4%**. Expected goals are 1.22 for Levante and 1.87 for Atlético Madrid (3.09 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 60.7%; Under 3.5 goals: 62.2%; Double Chance 1X: 41.6%; Double Chance X2: 79.2%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 20.8% | 4.81 |
| Draw | 20.8% | 4.80 |
| Atlético Madrid win | 58.4% | 1.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.22 |
| Atlético Madrid expected goals | 1.87 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 60.7% |
| Under 2.5 | 39.3% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.85% |
| 2 | 1-1 | 9.60% |
| 3 | 0-1 | 9.12% |
| 4 | 0-2 | 8.88% |
| 5 | 1-3 | 6.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 20.8% | 19.2% | 4.90 | +1.9% |
| Draw | 20.8% | 19.8% | 4.76 | -0.8% |
| Atlético Madrid win | 58.4% | 61.0% | 1.61 | -6.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T13:00:00+00:00 |
| Fixture id | 005711684f3e51024ac40c1ee69978e9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:00:14Z |
| Market best draw last update utc | 2026-10-28T16:00:14Z |
| Market best away last update utc | 2026-10-28T16:00:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Levante |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2217 |
| Dc lambda away | 1.8698 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T15:59:44.737672+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.87 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.58 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.85 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.24977811511977874, "-10": 8.981317749531059e-06, "-11": 1.5010427450333084e-06, "-12": 2.3055093940582249e-07, "-13": 3.275280152316386e-08, "-14": 4.3259064907381754e-09, "-15": 5.29782011684294e-10, "-16": 5.4176234502448643e-11, "-2": 0.17892357378031976, "-3": 0.09514708318026457, "-4": 0.040194932909392425, "-5": 0.014016917823719619, "-6": 0.0041509300427776665, "-7": 0.0010665630695794073, "-8": 0.00024179522028703896, "-9": 4.901472715075777e-05, "0": 0.20836577089809208, "1": 0.12283714722881947, "10": 9.666687352595594e-08, "11": 1.0556398235871994e-08, "12": 1.0594359271814378e-09, "13": 9.834252355284147e-11, "14": 8.48701787994441e-12, "15": 6.791415358473908e-13, "16": 4.5379216713584826e-14, "2": 0.0579594716327219, "3": 0.02013897799829434, "4": 0.005559021466264063, "5": 0.0012666734419017134, "6": 0.000245099624794294, "7": 4.1149908027012605e-05, "8": 6.095581373581653e-06, "9": 8.07382079619156e-07} |
| Raw goal margin distribution | {"-1": 0.22344269022409158, "-10": 8.034370019768374e-06, "-11": 1.342779886583583e-06, "-12": 2.0624273711820191e-07, "-13": 2.929950080375136e-08, "-14": 3.869803339195178e-09, "-15": 4.73924298236872e-10, "-16": 4.846414818060982e-11, "-2": 0.16005871711703706, "-3": 0.08511522405627385, "-4": 0.035956969001646265, "-5": 0.01253904020246137, "-6": 0.003713275581591581, "-7": 0.000954109696304681, "-8": 0.00021630147412376189, "-9": 4.384684578916459e-05, "0": 0.23264750965907674, "1": 0.14482876426048355, "10": 1.1397320886660908e-07, "11": 1.2446317307377137e-08, "12": 1.249107453309927e-09, "13": 1.1594885164407289e-10, "14": 1.0006454395422473e-11, "15": 8.007287014857336e-13, "16": 5.350348838283041e-14, "2": 0.06833599479578484, "3": 0.023744472765464326, "4": 0.0065542568157886645, "5": 0.0014934468395824015, "6": 0.00028897997536153733, "7": 4.8517003719429864e-05, "8": 7.186877403954638e-06, "9": 9.519282360040645e-07} |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 52.2% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 60.0% |
| P home draw | 41.6% |
| P draw away | 79.2% |
| P home away | 79.2% |
| Raw p home draw | 47.8% |
| Raw p draw away | 75.5% |
| Raw p home away | 76.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6074 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:59:50Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.59, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:00:14Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:00:14Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:59:50Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.6, "price": 1.59, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.90 |
| Reference draw odds | 4.76 |
| Reference away odds | 1.61 |
| Market reference 1x2 last update utc | 2026-10-28T16:00:14Z |
| Market reference home last update utc | 2026-10-28T16:00:14Z |
| Market reference draw last update utc | 2026-10-28T16:00:14Z |
| Market reference away last update utc | 2026-10-28T16:00:14Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-28T15:59:52Z |
| Market reference under 2 5 last update utc | 2026-10-28T15:59:52Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.0532 |
| Raw ev home | 0.2020 |
| Raw edge prob draw | 0.0347 |
| Raw ev draw | 0.1074 |
| Raw edge prob away | -0.0879 |
| Raw ev away | -0.1595 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.03703340825597795, 0.07644441868709034, 0.08240580209817623, 0.057644617700730844, 0.030242730474590147, 0.012693261338737032, 0.004439603636011185, 0.001330970364210921, 0.0003491408183455401, 8.141048520374518e-05, 1.708451168575453e-05, 3.259358353815319e-06, 5.699976866663069e-07, 9.201358838703034e-08, 1.379260056623787e-08, 1.9296437058944935e-09, 2.530925558927618e-10, 3.124299629367253e-11], [0.04000659739739586, 0.0915943868186492, 0.10035293285692531, 0.07019901878744772, 0.036829284145682775, 0.015457722277177795, 0.005406503355979738, 0.0016208419333760972, 0.0004251800748119576, 9.914084624487821e-05, 2.0805341498299967e-05, 3.96921286740714e-06, 6.941372830820684e-07, 1.1205319555445208e-07, 1.6796486209757942e-08, 2.3499001323318754e-09, 3.082134949409837e-10, 3.8047397506946605e-11], [0.025531222714790438, 0.05357890592726415, 0.05726780859803571, 0.04274381924349166, 0.02242516051622853, 0.009412127097279677, 0.0032919919135486683, 0.0009869222650001994, 0.0002588899471476122, 6.036634820165903e-05, 1.2668264765852612e-05, 2.4168331733680695e-06, 4.2265659934742046e-07, 6.822861087185948e-08, 1.0227293527414227e-08, 1.4308420292992917e-09, 1.8766960199332473e-10, 2.3166863437883235e-11], [0.010363886254029012, 0.02174927902390688, 0.02282112744511561, 0.01626157329269918, 0.009103042788620425, 0.0038206636530635704, 0.0013363178928926496, 0.00040062123973817293, 0.00010509116600181832, 2.4504504673435432e-05, 5.142427236481754e-06, 9.810648077281577e-07, 1.7156894399788377e-07, 2.7696032040671623e-08, 4.151564066819439e-09, 5.808215378009024e-10, 7.61806996133784e-11, 9.404122168961157e-12], [0.0031552583522829465, 0.00662151172004964, 0.00694783319835469, 0.004860157639027046, 0.0025973895193560754, 0.0011631911627654338, 0.00040683852461382647, 0.0001219680997844228, 3.1994733553688284e-05, 7.460333039583086e-06, 1.5655986655207207e-06, 2.9868264209400565e-07, 5.223372104563937e-08, 8.43198528809139e-09, 1.263932937490257e-09, 1.7682961424047598e-10, 2.3193016870908387e-11, 2.863060660084782e-12], [0.0007684881926048534, 0.001612721687392427, 0.0016921998711327054, 0.001183729933584733, 0.000621033268395736, 0.00026551654037714763, 9.908874886149667e-05, 2.9706297898224914e-05, 7.79257107227297e-06, 1.8170232715401296e-06, 3.813139700399081e-07, 7.274652600766852e-08, 1.272193696923296e-08, 2.053676881776616e-09, 3.078408897968201e-10, 4.3068254790722394e-11, 5.648843177384271e-12, 6.973211275693687e-13], [0.00015597616112422087, 0.00032732596308163224, 0.00034345724800211285, 0.00024025567682770086, 0.00012604798104504157, 5.2903952107405305e-05, 1.8848794756898557e-05, 6.029337017751819e-06, 1.5816187325154685e-06, 3.687920221748014e-07, 7.739336765638863e-08, 1.4764994401981354e-08, 2.582107193864946e-09, 4.168244083533808e-10, 6.248090821645383e-11, 8.741345817958229e-12, 1.1465171255457235e-12, 1.4153174192620163e-13], [2.713516494164835e-05, 5.69448814093472e-05, 5.975124023933121e-05, 4.179726806902839e-05, 2.192856095166352e-05, 9.203697899425902e-06, 3.219091576909528e-06, 9.830644946953466e-07, 2.7515413171008967e-07, 6.41587296337382e-08, 1.3464120296390762e-08, 2.5686653368856587e-09, 4.492090592404114e-10, 7.2514921452427e-11, 1.0869800474235355e-11, 1.520731494304299e-12, 1.9945952692944353e-13, 2.4622270056945996e-14], [4.130615375551169e-06, 8.668360896799438e-06, 9.095555238804478e-06, 6.362535054171479e-06, 3.3380468195211965e-06, 1.4010210049228938e-06, 4.900220504088828e-07, 1.4690609351110333e-07, 3.925514108341452e-08, 9.766479609423406e-09, 2.0495582921326397e-09, 3.910117575478686e-10, 6.838026785263406e-11, 1.1038490097716173e-11, 1.6546413137565595e-12, 2.3149138418602386e-13, 3.036246842451933e-14, 3.748093202930653e-15], [5.589134056181331e-07, 1.1729155753967416e-06, 1.2307192251783376e-06, 8.609143704204668e-07, 4.5167098516463117e-07, 1.895720976198389e-07, 6.630486455918546e-08, 1.9877857792409588e-08, 5.2143696983912205e-09, 1.2385285700651187e-09, 2.773256526979069e-10, 5.290778568765915e-11, 9.25253138038691e-12, 1.4936176652790743e-12, 2.2388945173205327e-13, 3.1323090179850484e-14, 4.108344420195924e-15, 5.071543453364064e-16], [6.806389603490472e-08, 1.4283644474984872e-07, 1.498757133907957e-07, 1.048412609435414e-07, 5.5004025072951386e-08, 2.30858938322393e-08, 8.074537777410613e-09, 2.420704947455803e-09, 6.350005447558423e-10, 1.4806547884656975e-10, 3.165195464824537e-11, 6.443055379033512e-12, 1.1267636947048318e-12, 1.8189121331419676e-13, 2.7265025695973196e-14, 3.81449350125253e-15, 5.003099311646284e-16, 6.176073124682163e-17], [7.535228008949652e-09, 1.5813158544816414e-08, 1.6592462953112156e-08, 1.1606782038310601e-08, 6.089393856063186e-09, 2.5557965962911996e-09, 8.939171391021255e-10, 2.679917663267143e-10, 7.029973553216402e-11, 1.6392055235731063e-11, 3.439977768557725e-12, 6.685127121371188e-13, 1.2474192408047524e-13, 2.0136839719608477e-14, 3.0184605533551986e-15, 4.2229551855001626e-16, 5.5388386884789313e-17, 6.8374162963813316e-18], [7.646935563498011e-10, 1.604758400196634e-09, 1.6838441370517046e-09, 1.1778849192235548e-09, 6.179667341554894e-10, 2.593685534403706e-10, 9.071691996183251e-11, 2.7196466599476633e-11, 7.1341908580194866e-12, 1.6635062667255408e-12, 3.4909744343215084e-13, 6.660030380001463e-14, 1.186428808310006e-14, 2.0435362487431568e-15, 3.063208349508881e-16, 4.285559262799384e-17, 5.620950354402372e-18, 6.93877899608872e-19], [7.163353061462827e-11, 1.5032755152049784e-10, 1.577359970411198e-10, 1.1033969715198242e-10, 5.788873020096373e-11, 2.4296641522690743e-11, 8.498009705181952e-12, 2.5476596560624744e-12, 6.683033680550157e-13, 1.5583082411982586e-13, 3.27020964070295e-14, 6.238858509511923e-15, 1.0910536773894413e-15, 1.7941117249430526e-16, 2.8694949403124574e-17, 4.014545932856196e-18, 5.26548858626972e-19, 6.49997941681479e-20], [6.231040867304392e-12, 1.3076238305846478e-11, 1.372066175400145e-11, 9.59789579462096e-12, 5.03544974739669e-12, 2.1134427546310946e-12, 7.391991614737594e-13, 2.2160811140678562e-13, 5.813235174056318e-14, 1.3554940335135074e-14, 2.844591037330743e-15, 5.4268695127195075e-16, 9.490527681526913e-17, 1.5320369329410363e-17, 2.3393107610535857e-18, 3.492051774729825e-19, 4.580183928651905e-20, 5.654005468570259e-21], [5.058731382695463e-13, 1.0616071775823051e-12, 1.1139253245877613e-12, 7.792145437347201e-13, 4.088079055427772e-13, 1.7158191409853235e-13, 6.001260585259462e-14, 1.7991470954969975e-14, 4.719531750192135e-15, 1.1004710693476281e-15, 2.309409014950745e-16, 4.405857014650567e-17, 7.704977586136392e-18, 1.243799146428985e-18, 1.8644229740463734e-19, 2.6570510956535838e-20, 3.718467054190951e-21, 4.590259558699007e-22], [3.8502941985205085e-14, 8.08008895458474e-14, 8.478292066498379e-14, 5.930746288303586e-14, 3.1115127251172174e-14, 1.3059417439805069e-14, 4.5676706405633084e-15, 1.369364194306368e-15, 3.592123072527264e-16, 8.375889236663012e-17, 1.7577339968460446e-17, 3.353379418612469e-18, 5.864401221443038e-19, 9.466785791398444e-20, 1.4190468750950196e-20, 1.9853071636100114e-21, 2.652494220586371e-22, 3.493731612043981e-23], [2.7581461309584305e-15, 5.788146291899296e-15, 6.073397837841483e-15, 4.248471437602401e-15, 2.2289223476760938e-15, 9.355072580690107e-16, 3.272036487394406e-16, 9.809397307484737e-17, 2.5732060574032553e-17, 6.000041892984557e-18, 1.2591472164693062e-18, 2.4021827923267843e-19, 4.200945357766758e-20, 6.781502206556329e-21, 1.016529762763564e-21, 1.4221685382325058e-22, 1.865319847140828e-23, 2.3455846405452505e-24]] |
| Legacy trial inputs | {"lambda_home": 1.2177896495366591, "lambda_away": 2.0985640415970157, "rho": -0.021863316965005233, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2030 |
| Legacy p draw | 0.2050 |
| Legacy p away | 0.5919 |
| Legacy p over 1 5 | 0.8465 |
| Legacy p under 3 5 | 0.5750 |
| Legacy p btts yes | 0.6173 |
| Legacy p over 2 5 | 0.6470 |
| Legacy goal margin distribution | {"-1": 0.22991280802927927, "-10": 2.150538535688144e-05, "-11": 4.026058431825227e-06, "-12": 6.928828876239727e-07, "-13": 1.1031996038636104e-07, "-14": 1.633957442273203e-08, "-15": 2.2610240642733602e-09, "-16": 2.9113995339970836e-10, "-17": 3.124299629367253e-11, "-2": 0.17928883775850354, "-3": 0.10535249016403436, "-4": 0.04942695769381458, "-5": 0.01919963499819812, "-6": 0.006345481022708446, "-7": 0.001821971046969953, "-8": 0.00046198534559443587, "-9": 0.00010481297759014242, "0": 0.20503995541034906, "1": 0.12194409699291908, "10": 8.567645011135093e-08, "11": 9.307742496508658e-09, "12": 9.295530348025443e-10, "13": 8.588523063029322e-11, "14": 7.381679436989284e-12, "15": 5.927474256532352e-13, "16": 4.429108827710438e-14, "17": 2.7581461309584305e-15, "2": 0.05554782710123744, "3": 0.01894125190156164, "4": 0.005156770524486112, "5": 0.0011624036096546833, "6": 0.00022293516528829247, "7": 3.714544381140153e-05, "8": 5.46565646730854e-06, "9": 7.195802618209752e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2139 |
| Legacy raw p draw | 0.2121 |
| Legacy raw p away | 0.5739 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2178 |
| Legacy lambda away | 2.0986 |
| Legacy model home team | Levante |
| Legacy model away team | Ath Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 9.763974031546171, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,476.0819 |
| Elo away rating | 1,586.5836 |
| Elo rating diff | -50.5017 |
| Elo home expectancy | 0.4278 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **39.1%**. Expected goals are 1.17 for Rayo Vallecano and 1.10 for Celta Vigo (2.27 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.8%; Under 3.5 goals: 80.4%; Double Chance 1X: 68.3%; Double Chance X2: 60.9%; Double Chance 12 (either team wins): 70.9%; Under 4.5 goals: 91.9%; BTTS Yes (both teams score): 46.4%; BTTS No (at least one team does not score): 53.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 39.1% | 2.55 |
| Draw | 29.1% | 3.43 |
| Celta Vigo win | 31.7% | 3.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.17 |
| Celta Vigo expected goals | 1.10 |
| Expected total goals | 2.27 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 66.8% |
| Under 1.5 | 33.2% |
| Over 2.5 | 39.8% |
| Under 2.5 | 60.2% |
| Over 3.5 | 19.6% |
| Under 3.5 | 80.4% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.59% |
| 2 | 1-0 | 12.28% |
| 3 | 0-0 | 10.62% |
| 4 | 0-1 | 10.33% |
| 5 | 2-1 | 8.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 39.1% | 40.0% | 2.43 | -4.9% |
| Draw | 29.1% | 29.0% | 3.32 | -3.3% |
| Celta Vigo win | 31.7% | 31.0% | 3.11 | -1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:15:00+00:00 |
| Fixture id | 77383723574e3d39c7aba22eec6c4ce3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:00:14Z |
| Market best draw last update utc | 2026-10-28T16:00:14Z |
| Market best away last update utc | 2026-10-28T16:00:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Vallecano |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1744 |
| Dc lambda away | 1.0993 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T15:59:44.737672+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.4% |
| P btts no | 53.6% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.42 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.01 |
| Fair Over 2.5 odds | 2.51 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.11 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.35 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.18926729030115583, "-10": 7.798600661545034e-08, "-11": 7.717568864577803e-09, "-12": 6.983373798909191e-10, "-13": 5.3717534105777176e-11, "-2": 0.08891496333148133, "-3": 0.029584133989695716, "-4": 0.0076560231802751295, "-5": 0.001615738850334018, "-6": 0.0002873898565778161, "-7": 4.4132433433038684e-05, "-8": 5.9589462885595246e-06, "-9": 7.176699612501238e-07, "0": 0.2911265641668846, "1": 0.22471623968232005, "10": 1.6757335196558528e-07, "11": 1.7715815255895954e-08, "12": 1.7125303347117956e-09, "13": 1.4072828877787624e-10, "2": 0.11262227383224305, "3": 0.04003138842131607, "4": 0.01106719052866871, "5": 0.002495155803986012, "6": 0.00047412220101803994, "7": 7.778020539261079e-05, "8": 1.1219487946961913e-05, "9": 1.4435129649989702e-06} |
| Raw goal margin distribution | {"-1": 0.1993906564301458, "-10": 8.215725510033035e-08, "-11": 8.130359553964755e-09, "-12": 7.356894493739583e-10, "-13": 5.659073139429971e-11, "-2": 0.09367077045862973, "-3": 0.031166504717940646, "-4": 0.008065521967004925, "-5": 0.001702160101067509, "-6": 0.00030276151818540753, "-7": 4.64929510961544e-05, "-8": 6.277673285316797e-06, "-9": 7.560560752265685e-07, "0": 0.2940332519014991, "1": 0.21330398499132064, "10": 1.5906310911549448e-07, "11": 1.681611438850517e-08, "12": 1.6255591733332386e-09, "13": 1.335813772950565e-10, "2": 0.10690273137874691, "3": 0.03799838715294211, "4": 0.010505141265092851, "5": 0.0023684388672436155, "6": 0.0004500438196766454, "7": 7.383012365791467e-05, "8": 1.0649704231577849e-05, "9": 1.370203899176149e-06} |
| Unadjusted home-win probability | 37.2% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 66.7% |
| Raw p under 3 5 | 80.5% |
| Raw p btts yes | 46.5% |
| P home draw | 68.3% |
| P draw away | 60.9% |
| P home away | 70.9% |
| Raw p home draw | 66.6% |
| Raw p draw away | 62.8% |
| Raw p home away | 70.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3980 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:59:50Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:00:14Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:00:14Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:59:50Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.43 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.11 |
| Market reference 1x2 last update utc | 2026-10-28T16:00:14Z |
| Market reference home last update utc | 2026-10-28T16:00:14Z |
| Market reference draw last update utc | 2026-10-28T16:00:14Z |
| Market reference away last update utc | 2026-10-28T16:00:14Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.24 |
| Reference Under 2.5 odds | 1.77 |
| Market reference over 2 5 last update utc | 2026-10-28T16:00:16Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:00:16Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.0284 |
| Raw ev home | -0.0970 |
| Raw edge prob draw | 0.0042 |
| Raw ev draw | -0.0238 |
| Raw edge prob away | 0.0243 |
| Raw ev away | 0.0398 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10485739681681443, 0.10474220934303487, 0.057841510882393886, 0.020732135891266646, 0.005573265446262459, 0.0011985755022023588, 0.00021480274121924909, 3.299646780736584e-05, 4.4350971565107765e-06, 5.298907050031193e-07, 5.697862626365601e-08, 5.569868757394035e-09, 4.991020904070235e-10, 4.1283043709557175e-11, 3.1708036289957843e-12], [0.12215028762448034, 0.1353157916360729, 0.06986026859741278, 0.025040019872696773, 0.006731321763572523, 0.0014476248154787175, 0.0002594361206703013, 3.985272978908497e-05, 5.356656039629392e-06, 6.399955052014064e-07, 6.881808712058083e-08, 6.727219284348348e-09, 6.028093934866072e-10, 4.986115469791881e-11, 3.829657797869212e-12], [0.07554175287068324, 0.08122930376925186, 0.04299440840449027, 0.015121514698569302, 0.0040650040018398335, 0.0008742117632719574, 0.00015667188492663332, 2.4066819529199365e-05, 3.2348517872686584e-06, 3.8648936734566096e-07, 4.155882148703785e-08, 4.0625265397529695e-09, 3.6403290214568276e-10, 3.0110846057048873e-11, 2.3127068978133755e-12], [0.030412801379476998, 0.0327025861573063, 0.017582384602322892, 0.006204199627796913, 0.0016365540196872038, 0.00035195408776793905, 6.307546140978077e-05, 9.689203312904782e-06, 1.3023381263956377e-06, 1.555990418237299e-07, 1.6731411906923515e-08, 1.6355566035628787e-09, 1.4655816059105305e-10, 1.212250372411504e-11, 9.310863576669934e-13], [0.00918305227836269, 0.009874445782651809, 0.005308947208341217, 0.0019028862366109675, 0.0005035957727555009, 0.00010627145941700207, 1.904544248918598e-05, 2.925625280219408e-06, 3.932370106118031e-07, 4.6982654366548406e-08, 5.051998607921098e-09, 4.938513097604533e-10, 4.425278795384219e-11, 3.660352890684915e-12, 2.811386755018271e-13], [0.002218235619795242, 0.0023852469415235143, 0.0012824162864566325, 0.00045965653929840906, 0.00012356603878424082, 2.6161242260583094e-05, 4.600570446910998e-06, 7.067068780657344e-07, 9.49893692771646e-08, 1.1349014931992525e-08, 1.2203484117858736e-09, 1.19293512983081e-10, 1.0689595086565349e-11, 8.841858803601894e-13, 6.791116996792275e-14], [0.0004465263033623299, 0.000480145341595007, 0.00025814778135065054, 9.252792330878989e-05, 2.4873591437751053e-05, 5.349265639064772e-06, 9.437830145772108e-07, 1.422586523304291e-07, 1.912116618430588e-08, 2.2845335451128867e-09, 2.456536448455084e-10, 2.401354071320802e-11, 2.1517936759507756e-12, 1.779848132989797e-13, 1.3670379923655964e-14], [7.704414309481e-05, 8.284480919847401e-05, 4.454110419974222e-05, 1.5964870400665874e-05, 4.2917170244658925e-06, 9.229682198896971e-07, 1.6540977462518292e-07, 2.5014531436065454e-08, 3.2991871980448825e-09, 3.9417594894012116e-10, 4.238535204471818e-11, 4.143322919591132e-12, 3.7127286485055163e-13, 3.070969687844479e-14, 2.3587024976307823e-15], [1.1631621581869908e-05, 1.2507368268513824e-05, 6.724525033038344e-06, 2.41027187330286e-06, 6.479354089722983e-07, 1.3934371432540793e-07, 2.4972487551907402e-08, 3.836095744864337e-09, 5.076082752166111e-10, 5.951011057522973e-11, 6.399063650974775e-12, 6.255318361171957e-13, 5.605235250970374e-14, 4.6363494827170584e-15, 3.561014994078223e-16], [1.5609477913325547e-06, 1.6784718052167706e-06, 9.024221106404178e-07, 3.234552061947537e-07, 8.695205036053728e-08, 1.8699736883750403e-08, 3.351273854110632e-09, 5.147988299085956e-10, 6.919476472548405e-11, 8.138792381601965e-12, 8.587456359614248e-13, 8.394552136369997e-14, 7.522149446934646e-15, 6.221917927740547e-16, 4.7788336740361146e-17], [1.88529362918532e-07, 2.0272376941197728e-07, 1.0899343754309375e-07, 3.9066523746140826e-08, 1.0501962173211293e-08, 2.258531323733782e-09, 4.047627525976652e-10, 6.217677232562615e-11, 8.357258957301008e-12, 9.984975941906638e-13, 1.0570031100472061e-13, 1.0138837282348705e-14, 9.085159996273348e-16, 7.514756288209588e-17, 5.7718167965792754e-18], [2.0700314187798597e-08, 2.2258844220335843e-08, 1.1967358116651573e-08, 4.2894608205919814e-09, 1.1531037564041998e-09, 2.479842252714594e-10, 4.444249967529198e-11, 6.826940389544833e-12, 9.176177306644876e-13, 1.096339243687967e-13, 1.1788828042173006e-14, 1.134507026710268e-15, 9.97540454483714e-17, 8.251118754265025e-18, 6.337390593911554e-19], [2.0834655007410205e-09, 2.2403299582174246e-09, 1.204502383145141e-09, 4.317298546971509e-10, 1.160587164739319e-10, 2.4959359234538295e-11, 4.473092243920763e-12, 6.871245841097429e-13, 9.235728826930626e-14, 1.1034542619062037e-14, 1.1865335133180317e-15, 1.159879831930337e-16, 1.023201087951492e-17, 8.304666833105973e-19, 6.378518967078314e-20], [1.9356800927591596e-10, 2.0814177627568372e-10, 1.119064022853158e-10, 4.011061785711603e-11, 1.078263820494594e-11, 2.3188929589252527e-12, 4.1558046468987787e-13, 6.383851223999581e-14, 8.580615530256255e-15, 1.025183497054503e-15, 1.1023697298104629e-16, 1.0776066605671492e-17, 9.656165348808544e-19, 7.86304179106653e-20, 5.926074696926284e-21], [1.6699219388571928e-11, 1.7956506340881006e-11, 9.654227316480378e-12, 3.460365222087816e-12, 9.302241710577598e-13, 2.00052180133288e-13, 3.5852356902470903e-14, 5.507383814730198e-15, 7.402544550865768e-16, 8.844314819838671e-17, 9.510204725609129e-18, 9.296572355479698e-19, 8.330427337413501e-20, 6.890481977530343e-21, 5.210156970080692e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2077877553969156, "lambda_away": 1.0752901631539435, "rho": -0.021863316965005233, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3939 |
| Legacy p draw | 0.2899 |
| Legacy p away | 0.3162 |
| Legacy p over 1 5 | 0.6683 |
| Legacy p under 3 5 | 0.8027 |
| Legacy p btts yes | 0.4648 |
| Legacy p over 2 5 | 0.3996 |
| Legacy goal margin distribution | {"-1": 0.1914715643067867, "-10": 6.408228209254967e-08, "-11": 6.203720083295359e-09, "-12": 5.512759520027558e-10, "-13": 4.511270150742639e-11, "-14": 3.1708036289957843e-12, "-2": 0.08731826051589175, "-3": 0.02840376782172243, "-4": 0.007187656185859907, "-5": 0.001483429007920531, "-6": 0.00025805109531240687, "-7": 3.875684934749618e-05, "-8": 5.118332190446999e-06, "-9": 6.029216050881048e-07, "0": 0.28990252281359047, "1": 0.2229939468531649, "10": 2.1203375036404118e-07, "11": 2.3056010913523427e-08, "12": 2.3012615043331844e-09, "13": 2.1152451561679696e-10, "14": 1.6699219388571928e-11, "2": 0.11403876483104128, "3": 0.04166662584701241, "4": 0.011843078918466459, "5": 0.0027454215931832717, "6": 0.0005364298472841066, "7": 9.049417848191388e-05, "8": 1.3423494698912153e-05, "9": 1.7760816314062656e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3878 |
| Legacy raw p draw | 0.2899 |
| Legacy raw p away | 0.3222 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2078 |
| Legacy lambda away | 1.0753 |
| Legacy model home team | Vallecano |
| Legacy model away team | Celta |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 9.257935485706028, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.5850 |
| Elo away rating | 1,513.4884 |
| Elo rating diff | 21.0966 |
| Elo home expectancy | 0.5303 |

</details>


---
