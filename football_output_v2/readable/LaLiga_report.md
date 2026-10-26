# La Liga — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,998 |
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
| Training sha256 | 56dcfd7c8c10501f08c1085ba680ee0b381343806f4e9c1a234ff9a27fa939ba |
| Training as of utc | 2026-10-26T11:38:12.675051+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 98, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 98, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 62, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-26T11:38:12.675051+00:00', 'observations': 332, 'observations_sha256': '52efabc87e46235c26e5fe0236415abc5f8894bcd748bed7cedd6b88ca6e7660', 'eligible_training_matches': 113, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 134, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 19, 'retrospective_eligible_training_matches': 113, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '6b6b80a9a81fb5a41297f9c776dfcafacd47f2758bd8cf370f9a7645f43bb742', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1619, 'tuning_matches': 230, 'audit_matches': 126, 'audit_matchdays': 53, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8017114427406927, 'audit_candidate_poisson_score': 0.804890612238348, 'audit_gain': -0.0031791694976552876, 'audit_gain_lower95': -0.012999016820511715, 'audit_baseline_briers': [0.5696352072370781, 0.18734612086762337, 0.2015294815624924, 0.2482262774976402], 'audit_candidate_briers': [0.5729352189213638, 0.1847766252980737, 0.20545599220389799, 0.2453999021619766], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1842.174 |
| Base scoring parameter | 0.092 |
| Home-advantage parameter | 0.286 |
| Dixon-Coles low-score adjustment | -0.032 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1998, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261026T113812675051Z_f8243e45de9aaaffa417000b5b13bec472b867d1ca5a78d7eb67b729761d3a87.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE': 7} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 7} |
| Legacy comparison status | {'AVAILABLE': 7} |
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

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **64.8%**. Expected goals are 1.99 for Atlético Madrid and 0.81 for Deportivo La Coruña (2.80 combined). The most likely exact score is 2-0 at 12.1%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.0%; Under 3.5 goals: 69.3%; Double Chance 1X: 86.0%; Double Chance X2: 35.2%; Double Chance 12 (either team wins): 78.8%; Under 4.5 goals: 84.8%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 64.8% | 1.54 |
| Draw | 21.2% | 4.71 |
| Deportivo La Coruña win | 14.0% | 7.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 1.99 |
| Deportivo La Coruña expected goals | 0.81 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 53.0% |
| Under 2.5 | 47.0% |
| Over 3.5 | 30.7% |
| Under 3.5 | 69.3% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.09% |
| 2 | 1-0 | 11.83% |
| 3 | 1-1 | 10.11% |
| 4 | 2-1 | 9.74% |
| 5 | 3-0 | 8.02% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 70df1835c3b5ddff1c99e0189532136b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.9906 |
| Dc lambda away | 0.8060 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:38:12.675051+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.58 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.25 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.59 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.09754903701024431, "-10": 2.2488786578829628e-09, "-11": 1.6282032755151624e-10, "-12": 1.0825586881515192e-11, "-13": 6.653565101955245e-13, "-14": 3.801637528060482e-14, "-15": 2.028977242997125e-15, "-16": 1.012251610150471e-16, "-17": 4.385335138210092e-18, "-2": 0.03278831370940592, "-3": 0.007835654598501598, "-4": 0.0014669567366690085, "-5": 0.00022487507467464714, "-6": 2.9125586951520522e-05, "-7": 3.2621045765978267e-06, "-8": 3.2161009365862984e-07, "-9": 2.8304202945631372e-08, "0": 0.2122630463116159, "1": 0.24556930191256138, "10": 1.8986154873519195e-05, "11": 3.3948979181215896e-06, "12": 5.574637671442797e-07, "13": 8.461876950142385e-08, "14": 1.1940708623419504e-08, "15": 1.573923683102636e-09, "16": 1.9392869286203699e-10, "17": 2.0749301552117762e-11, "2": 0.1999923027076179, "3": 0.11803657044680636, "4": 0.054576502953140246, "5": 0.020662212259860466, "6": 0.006609327678516358, "7": 0.0018282163007961876, "8": 0.00044515009202167425, "9": 9.675531387458618e-05} |
| Raw goal margin distribution | {"-1": 0.09754903701024431, "-10": 2.2488786578829628e-09, "-11": 1.6282032755151624e-10, "-12": 1.0825586881515192e-11, "-13": 6.653565101955245e-13, "-14": 3.801637528060482e-14, "-15": 2.028977242997125e-15, "-16": 1.012251610150471e-16, "-17": 4.385335138210092e-18, "-2": 0.03278831370940592, "-3": 0.007835654598501598, "-4": 0.0014669567366690085, "-5": 0.00022487507467464714, "-6": 2.9125586951520522e-05, "-7": 3.2621045765978267e-06, "-8": 3.2161009365862984e-07, "-9": 2.8304202945631372e-08, "0": 0.2122630463116159, "1": 0.24556930191256138, "10": 1.8986154873519195e-05, "11": 3.3948979181215896e-06, "12": 5.574637671442797e-07, "13": 8.461876950142385e-08, "14": 1.1940708623419504e-08, "15": 1.573923683102636e-09, "16": 1.9392869286203699e-10, "17": 2.0749301552117762e-11, "2": 0.1999923027076179, "3": 0.11803657044680636, "4": 0.054576502953140246, "5": 0.020662212259860466, "6": 0.006609327678516358, "7": 0.0018282163007961876, "8": 0.00044515009202167425, "9": 9.675531387458618e-05} |
| Unadjusted home-win probability | 64.8% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 14.0% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 69.3% |
| Raw p btts yes | 48.1% |
| P home draw | 86.0% |
| P draw away | 35.2% |
| P home away | 78.8% |
| Raw p home draw | 86.0% |
| Raw p draw away | 35.2% |
| Raw p home away | 78.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5297 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05774909171540099, 0.044170349180412356, 0.019207852318720957, 0.005318500114803119, 0.0011044874903944103, 0.0001834942318481687, 2.5404039893596516e-05, 3.0146463059991677e-06, 3.1302426070014894e-07, 2.8891301655266015e-08, 2.3999308504769195e-09, 1.8123316006368938e-10, 1.2545501790241951e-11, 8.016343236710789e-13, 4.756416622590605e-14, 2.6340271607194574e-15, 1.3675143299688817e-16, 6.682124826361946e-18], [0.11247603421038756, 0.0972315634472095, 0.03952172942195115, 0.010943249613752854, 0.0022725734778142274, 0.0003775544116675613, 5.227089287440079e-05, 6.202881698151113e-06, 6.440730555721692e-07, 5.9446219583565965e-08, 4.938054298319277e-09, 3.7290207127119627e-10, 2.5813397510001395e-11, 1.6494282811930158e-12, 9.786716789408044e-14, 5.4197266309967494e-15, 2.8137727442330683e-16, 1.3749019149516488e-17], [0.1178500669681753, 0.09789521248383892, 0.04065959771513719, 0.011258316209826296, 0.002338003036240992, 0.0003884245633606301, 5.377582174589066e-05, 6.381468579695572e-06, 6.626165332779797e-07, 6.115773295616513e-08, 5.080225592396498e-09, 3.836382776459918e-10, 2.65565898499025e-11, 1.6969168949380269e-12, 1.0068485702153894e-13, 5.575765731039825e-15, 2.8947839458358904e-16, 1.4144866527185978e-17], [0.08082872188223901, 0.06714247269452717, 0.027886817547995407, 0.00772163591584629, 0.001603544249382445, 0.00026640511806060117, 3.688271930351332e-05, 4.376798098619244e-06, 4.5446259693142406e-07, 4.1945681621012765e-08, 3.484326755772969e-09, 2.6312239309633025e-10, 1.8214119604175696e-11, 1.163848500784115e-12, 6.905578007133972e-14, 3.824198230421379e-15, 1.9854183581442084e-16, 9.701407152327302e-18], [0.041577928947299274, 0.03453778426814959, 0.01434485281440075, 0.003971974590093296, 0.000824855909039481, 0.00013703758777799596, 1.8972303988907035e-05, 2.251405145638616e-06, 2.3377350432373855e-07, 2.157666890521164e-08, 1.792321923533171e-09, 1.35348968904165e-10, 9.369260741786334e-12, 5.986784047077186e-13, 3.552198092887813e-14, 1.967150272851046e-15, 1.0212902233670309e-16, 4.990359959618753e-18], [0.01710999887456126, 0.014212864010299968, 0.005903141924679405, 0.0016345326110981445, 0.0003394417190242822, 5.639321226475865e-05, 7.807413888014717e-06, 9.264900990351119e-07, 9.620162661183303e-08, 8.879152714722512e-09, 7.375698326238062e-10, 5.569831793590855e-11, 3.85560427866978e-12, 2.4636597084373447e-13, 1.4617877058899787e-14, 8.095145623351341e-16, 4.202776572772361e-17, 2.053614873433437e-18], [0.005867537354946091, 0.0048740219746707825, 0.002024366337399478, 0.0005605307880969607, 0.00011640485664574081, 1.9338942214708948e-05, 2.6773989273348753e-06, 3.1772154428125984e-07, 3.2990454405624873e-08, 3.044930663985286e-09, 2.529350572451449e-10, 1.9100641881543513e-11, 1.3222036013468185e-12, 8.448636072457012e-14, 5.012913228219213e-15, 2.7760708628310945e-16, 1.4412595065624437e-17, 7.042468015856347e-19], [0.0017247055294103656, 0.0014326713477326575, 0.0005950427929908198, 0.00016476257263545963, 3.4216075290580694e-05, 5.684493945750519e-06, 7.869953704716154e-07, 9.339115732646644e-08, 9.697223160101133e-09, 8.950277493196888e-10, 7.434779966840737e-11, 5.614447880867045e-12, 3.886488869690559e-13, 2.4833943899580613e-14, 1.473497080657866e-15, 8.159990260860953e-17, 4.23644212198857e-18, 2.0700649681257438e-19], [0.0004435903617362257, 0.0003684798306451328, 0.0001530436606656973, 4.237656107065499e-05, 8.800297184952832e-06, 1.4620389873423358e-06, 2.0241342949227328e-07, 2.4019994459909357e-08, 2.49410386647092e-09, 2.301991130163617e-10, 1.91220859368824e-11, 1.4440232978637485e-12, 9.995961479750381e-14, 6.387234208913468e-15, 3.78980116825946e-16, 2.0987310412443993e-17, 1.0896033330454743e-18, 5.3241602834213564e-20], [0.00010141372253979175, 8.424193699856763e-05, 3.498887414612997e-05, 9.688138375660712e-06, 2.0119258080571444e-06, 3.3425166323352335e-07, 4.627580116148571e-08, 5.491456225582033e-09, 5.702025546941628e-10, 5.2628170019233714e-11, 4.371695340707575e-12, 3.301329124856636e-13, 2.285278832610545e-14, 1.4602508389138384e-15, 8.664251465125028e-17, 4.798123355731743e-18, 2.491053449930763e-19, 1.2172106526997565e-20], [2.0866704071771886e-05, 1.7333468546056305e-05, 7.199247442330042e-06, 1.9934138243664946e-06, 4.139702142835389e-07, 6.87750174978027e-08, 9.52162512466691e-09, 1.129912097816432e-09, 1.1732384604167248e-10, 1.0828677048112054e-11, 8.995121240194665e-13, 6.792755079557948e-14, 4.7021483806452216e-15, 3.0045857072464656e-16, 1.782740706073989e-17, 9.87253180895976e-19, 5.1255465103626593e-20, 2.504510617182821e-21], [3.9031775251847504e-06, 3.242275571156783e-06, 1.346640117121301e-06, 3.7287383819207984e-07, 7.743432939528046e-08, 1.2864566520342517e-08, 1.7810475991802626e-09, 2.1135333546027312e-10, 2.1945765726249954e-11, 2.0255354528582193e-12, 1.6825635203470105e-13, 1.2706045415424232e-14, 8.79550494236718e-16, 5.620164720158369e-17, 3.3346682031079004e-18, 1.8466857123608583e-19, 9.587483425616945e-21, 4.684759758393646e-22], [6.692589549511264e-07, 5.559372963219872e-07, 2.3090186179456567e-07, 6.393487195159917e-08, 1.327728960162367e-08, 2.2058249438439656e-09, 3.05387609775493e-10, 3.6239733269339814e-11, 3.762934209572517e-12, 3.473087584793323e-13, 2.885010215396308e-14, 2.1786440973846988e-15, 1.508122653405958e-16, 9.636624373338855e-18, 5.717794136496796e-19, 3.166422592882973e-20, 1.6439193699589483e-21, 8.032730768378817e-23], [1.0592731672723423e-07, 8.799127099058669e-08, 3.654611487269104e-08, 1.0119325831996938e-08, 2.101470067013314e-09, 3.491281151231762e-10, 4.833538621477839e-11, 5.735863040356596e-12, 5.955804115766235e-13, 5.497047830203383e-14, 4.566265248851365e-15, 3.448260522064157e-16, 2.386989143574715e-17, 1.5252418434215707e-18, 9.049869052884751e-20, 5.0116721846938726e-21, 2.60192211829864e-22, 1.2713847308158911e-23], [1.5568152175551118e-08, 1.2932089089248257e-08, 5.371187483473241e-09, 1.4872386966261174e-09, 3.0885334214472264e-10, 5.131140666006798e-11, 7.103858299303428e-12, 8.430005727449181e-13, 8.753253425722206e-14, 8.079018687621186e-15, 6.71104625930469e-16, 5.067913188689133e-17, 3.508161197385018e-18, 2.241650015930231e-19, 1.3300604880506455e-20, 7.365661439928756e-22, 3.8240484832550326e-23, 1.868555871568209e-24], [2.135516550462049e-09, 1.7739221694858396e-09, 7.367772126871349e-10, 2.0400769566734067e-10, 4.236606993419399e-11, 7.038494801081602e-12, 9.744513542284034e-13, 1.1563618179252733e-13, 1.2007023923092317e-14, 1.1082161790531486e-15, 9.205684911128026e-17, 6.951764325471347e-18, 4.812219339986798e-19, 3.0749190111851275e-20, 1.8244722644787697e-21, 1.0103634479350888e-22, 5.245528649562629e-24, 2.5631378369126777e-25], [2.746250136500156e-10, 2.2812438513000955e-10, 9.474871643933e-11, 2.623515898072985e-11, 5.448228688023135e-12, 9.051424726277014e-13, 1.2531334229104925e-13, 1.4870682222686366e-14, 1.5440896995445183e-15, 1.4251534750868121e-16, 1.1838406702253298e-17, 8.93989031534873e-19, 6.188459656961245e-20, 3.95431107867883e-21, 2.346250701864843e-22, 1.2993159693406067e-23, 6.745690529422498e-25, 3.2961662755398294e-26], [3.3239027033068393e-11, 2.761085927118738e-11, 1.146783792640603e-11, 3.175352263026741e-12, 6.594221634680635e-13, 1.0955322210668128e-13, 1.5167203877956375e-14, 1.7998615706214044e-15, 1.8688770765087875e-16, 1.7249235331873862e-17, 1.4328524382201088e-18, 1.082032739534926e-19, 7.490154487272297e-21, 4.786069961160657e-22, 2.8397664680693875e-23, 1.572617077206559e-24, 8.16459458241251e-26, 3.9894894671824265e-27]] |
| Legacy trial inputs | {"lambda_home": 2.0575819079695465, "lambda_away": 0.8306759173100422, "rho": -0.02181659734176786, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6564 |
| Legacy p draw | 0.2042 |
| Legacy p away | 0.1393 |
| Legacy p over 1 5 | 0.7856 |
| Legacy p under 3 5 | 0.6722 |
| Legacy p btts yes | 0.4942 |
| Legacy p over 2 5 | 0.5513 |
| Legacy goal margin distribution | {"-1": 0.09669911171664533, "-10": 2.8005897062138954e-09, "-11": 2.0881454013098553e-10, "-12": 1.4299543309324138e-11, "-13": 9.052807894919732e-13, "-14": 5.3283072658638717e-14, "-15": 2.92954930166995e-15, "-16": 1.5050045214640466e-16, "-17": 6.682124826361946e-18, "-2": 0.03277544278580248, "-3": 0.008018731602799384, "-4": 0.0015404374332144628, "-5": 0.00024262338963369995, "-6": 3.2313333174309465e-05, "-7": 3.7235007118375544e-06, "-8": 3.778234489915352e-07, "-9": 3.4231821929013995e-08, "0": 0.20424591125262728, "1": 0.2425896310901208, "10": 2.4350316849505382e-05, "11": 4.497191461455666e-06, "12": 7.628309789027638e-07, "13": 1.1962307761031384e-07, "14": 1.7439998413739313e-08, "15": 2.3751087735184642e-09, "16": 3.0223587292120295e-10, "17": 3.3239027033068393e-11, "2": 0.20109422246305714, "3": 0.12186590440545383, "4": 0.05798906615327941, "5": 0.02262352272201016, "6": 0.007463367647713036, "7": 0.0021302473373708717, "8": 0.0005354180536540881, "9": 0.00012015991984590356} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.6564 |
| Legacy raw p draw | 0.2042 |
| Legacy raw p away | 0.1393 |
| Legacy market weight | 0 |
| Legacy lambda home | 2.0576 |
| Legacy lambda away | 0.8307 |
| Legacy model home team | Ath Madrid |
| Legacy model away team | La Coruna |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 10.666991839562744, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,650.0417 |
| Elo away rating | 1,441.7911 |
| Elo rating diff | 268.2506 |
| Elo home expectancy | 0.8241 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.4%**. Expected goals are 1.24 for Valencia and 1.57 for Villarreal (2.81 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.3%; Under 3.5 goals: 69.0%; Double Chance 1X: 55.6%; Double Chance X2: 70.1%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.9% | 3.34 |
| Draw | 25.6% | 3.90 |
| Villarreal win | 44.4% | 2.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.24 |
| Villarreal expected goals | 1.57 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.3% |
| Under 2.5 | 46.7% |
| Over 3.5 | 31.0% |
| Under 3.5 | 69.0% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.11% |
| 2 | 1-2 | 9.18% |
| 3 | 0-1 | 9.04% |
| 4 | 0-2 | 7.38% |
| 5 | 2-1 | 7.30% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0dae715cc56fe201f9e667917c126691 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2445 |
| Dc lambda away | 1.5659 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:38:12.675051+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.63 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.43 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.22 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.50 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.2174411410274579, "-10": 1.7531534532015977e-06, "-11": 2.459888253670433e-07, "-12": 3.170805529999174e-08, "-13": 3.7781663481457134e-09, "-14": 4.158561564576345e-10, "-15": 3.842197196395431e-11, "-2": 0.1350373235561773, "-3": 0.06135939211668041, "-4": 0.022002843167633974, "-5": 0.0064876977250396895, "-6": 0.0016205014534914533, "-7": 0.00035062925307042294, "-8": 6.686118350120839e-05, "-9": 1.1391003681634602e-05, "0": 0.25617714373436673, "1": 0.17202928054329486, "10": 1.7620830311142488e-07, "11": 1.9649090815434954e-08, "12": 2.012877437809621e-09, "13": 1.9061165149968632e-10, "14": 1.6673706316612804e-11, "15": 1.2243041087391194e-12, "2": 0.08528940980303945, "3": 0.030799451312417313, "4": 0.008777308807568782, "5": 0.0020568083453336877, "6": 0.0004082942721715077, "7": 7.020897824644189e-05, "8": 1.0639940753884396e-05, "9": 1.4406145141015363e-06} |
| Raw goal margin distribution | {"-1": 0.2174411410274579, "-10": 1.7531534532015977e-06, "-11": 2.459888253670433e-07, "-12": 3.170805529999174e-08, "-13": 3.7781663481457134e-09, "-14": 4.158561564576345e-10, "-15": 3.842197196395431e-11, "-2": 0.1350373235561773, "-3": 0.06135939211668041, "-4": 0.022002843167633974, "-5": 0.0064876977250396895, "-6": 0.0016205014534914533, "-7": 0.00035062925307042294, "-8": 6.686118350120839e-05, "-9": 1.1391003681634602e-05, "0": 0.25617714373436673, "1": 0.17202928054329486, "10": 1.7620830311142488e-07, "11": 1.9649090815434954e-08, "12": 2.012877437809621e-09, "13": 1.9061165149968632e-10, "14": 1.6673706316612804e-11, "15": 1.2243041087391194e-12, "2": 0.08528940980303945, "3": 0.030799451312417313, "4": 0.008777308807568782, "5": 0.0020568083453336877, "6": 0.0004082942721715077, "7": 7.020897824644189e-05, "8": 1.0639940753884396e-05, "9": 1.4406145141015363e-06} |
| Unadjusted home-win probability | 29.9% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 44.4% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 69.0% |
| Raw p btts yes | 56.7% |
| P home draw | 55.6% |
| P draw away | 70.1% |
| P home away | 74.4% |
| Raw p home draw | 55.6% |
| Raw p draw away | 70.1% |
| Raw p home away | 74.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5330 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.06445652959090754, 0.09096347114542937, 0.07074353850405268, 0.035662138568260886, 0.013483084329910038, 0.0040781303723442085, 0.0010279020071185792, 0.00022207288419718823, 4.198048049313964e-05, 7.054183530004206e-06, 1.0668137720530112e-06, 1.466688164420743e-07, 1.8484103870844835e-08, 2.150289365343675e-09, 2.322794186184144e-10, 2.3418621653624026e-11], [0.07600498915315852, 0.12145839454929969, 0.08988070017959661, 0.045309268552257406, 0.017130455809521557, 0.005181324274145239, 0.0013059645314538223, 0.00028214684683043243, 5.333681436338007e-05, 8.962443330931693e-06, 1.3554024978248466e-06, 1.8634487608463595e-07, 2.3484324268127347e-08, 2.7319740831844042e-09, 2.951143980667112e-10, 2.975370127051544e-11], [0.04993009553739871, 0.07550996275140566, 0.05709737196925584, 0.028783044135323937, 0.01088224730564779, 0.0032914741294078446, 0.0008296235174189367, 0.00017923584742041067, 3.388260130679733e-05, 5.693457656616577e-06, 8.610293470314071e-07, 1.1837694502945846e-07, 1.4918588701518362e-08, 1.7355065117011276e-09, 1.8747357915802198e-10, 1.8901256282050968e-11], [0.021145638842471604, 0.03197883729570957, 0.024181015347984006, 0.012189759493181808, 0.0046086847790493225, 0.0013939553379717611, 0.0003513496035957265, 7.590725506097854e-05, 1.4349446812901493e-05, 2.4112070701235257e-06, 3.646501255231495e-07, 5.013321324396677e-08, 6.318095035195679e-09, 7.349954673670089e-10, 7.93959746063722e-11, 8.004774168915405e-12], [0.0067164608425592945, 0.010157395105784518, 0.007680583401994609, 0.0038718169229169258, 0.0014638503515917304, 0.0004427601603106502, 0.00011159870232246905, 2.4110319394050146e-05, 4.55779550332919e-06, 7.65868460651996e-07, 1.158233292243393e-07, 1.592374513596964e-08, 2.0068080335424867e-09, 2.3345562235338325e-10, 2.521843669388051e-11, 2.5425456596309796e-12], [0.001706672343576623, 0.0025810238034853763, 0.0019516587056767505, 0.00098384000392926, 0.00037196865562973255, 0.00011250665166564137, 2.835755665035975e-05, 6.126502672938229e-06, 1.1581491674781773e-06, 1.9460941576997268e-07, 2.9431046701796475e-08, 4.046270210869949e-09, 5.09935790589568e-10, 5.932175642241455e-11, 6.408078519710925e-12, 6.460682882384669e-13], [0.0003613920283076032, 0.0005465380809400263, 0.00041326848757073476, 0.00020833051867767184, 7.87652694032457e-05, 2.382355769493237e-05, 6.004781734638314e-06, 1.2973018726987394e-06, 2.452409088909042e-07, 4.120901809745095e-08, 6.232095869373595e-09, 8.568075788481147e-10, 1.0798014648881045e-10, 1.2561526503287757e-11, 1.3569262445183246e-12, 1.368065346523489e-13], [6.559340810579806e-05, 9.919780343894381e-05, 7.500909383485379e-05, 3.781242435399237e-05, 1.4296060941700439e-05, 4.324025490362064e-06, 1.0898804291585599e-06, 2.3546300003030316e-07, 4.4511737285544005e-08, 7.479522872609115e-09, 1.1311384194848339e-09, 1.5551236547943177e-10, 1.959862216422716e-11, 2.279943302071496e-12, 2.4628494807417376e-13, 2.4830671835831235e-14], [1.0417173024532502e-05, 1.5754032484640786e-05, 1.1912518825531135e-05, 6.005154760936516e-06, 2.2704193104091883e-06, 6.867172021758232e-07, 1.7308862787376458e-07, 3.739489810065764e-08, 7.069101641709931e-09, 1.1878553982016716e-09, 1.7964098787890499e-10, 2.4697591807405685e-11, 3.112542007237847e-12, 3.6208766322211175e-13, 3.9113578506067716e-14, 3.943466459495883e-15], [1.4705745180032728e-06, 2.2239698498958386e-06, 1.681669929913307e-06, 8.477374377196343e-07, 3.205112150107686e-07, 9.694269416625995e-08, 2.4434625872860778e-08, 5.278973875220243e-09, 9.979330011119076e-10, 1.676875170983735e-10, 2.5359611339997694e-11, 3.48651683930796e-12, 4.393922373449443e-13, 5.111529678577886e-14, 5.5215970516650836e-15, 5.566924226254257e-16], [1.868386429904619e-07, 2.825586216266226e-07, 2.1365862376663875e-07, 1.0770628114160972e-07, 4.0721418563097185e-08, 1.2316711056884413e-08, 3.104454948847943e-09, 6.707013504949465e-10, 1.267888471073949e-10, 2.130494426330747e-11, 3.221975705089807e-12, 4.4296706290285645e-13, 5.582542629498333e-14, 6.494273204513928e-15, 7.0152697985954325e-16, 7.072858636747829e-17], [2.158011164848301e-08, 3.263589643099295e-08, 2.467785508258412e-08, 1.2440218656466553e-08, 4.703377979046374e-09, 1.422596500892161e-09, 3.5856867365090143e-10, 7.74668976117974e-11, 1.4644280393856762e-11, 2.4607493851812747e-12, 3.7214247722879967e-13, 5.116328464520179e-14, 6.447910951330342e-15, 7.500971886009503e-16, 8.10272987829658e-17, 8.169245751947973e-18], [2.2848206186449275e-09, 3.4553653052455303e-09, 2.6127979796890124e-09, 1.3171233100985436e-09, 4.979758751415493e-10, 1.5061913813031752e-10, 3.7963895280186595e-11, 8.201902187022857e-12, 1.5504810324488594e-12, 2.6053483986377964e-13, 3.9401038275246044e-14, 5.416975110190127e-15, 6.826804294972968e-16, 7.941745392329886e-17, 8.578863999780899e-18, 8.649288491582159e-19], [2.2329984675433327e-10, 3.3769939611240637e-10, 2.553536954733062e-10, 1.287249558680876e-10, 4.866812549705183e-11, 1.472029365820268e-11, 3.710283393403078e-12, 8.015874360160683e-13, 1.5153144807782185e-13, 2.5462563380686904e-14, 3.85073810041249e-15, 5.294112378480211e-16, 6.671965144438285e-17, 7.761618197059823e-18, 8.384286279828272e-19, 8.453113469580696e-20], [2.0264694335830946e-11, 3.064657293357417e-11, 2.3173614588210597e-11, 1.1681924201810953e-11, 4.416683224062611e-12, 1.3358820252363621e-12, 3.3671209344510623e-13, 7.274489709873859e-14, 1.3751637191857176e-14, 2.310754223150085e-15, 3.4945850481504243e-16, 4.804462281941021e-17, 6.05487805910177e-18, 7.043749586083777e-19, 7.608827375136744e-20, 7.671288768756132e-21], [1.7164393661438028e-12, 2.59579460458844e-12, 1.9628277474049534e-12, 9.894703685139076e-13, 3.740973748695402e-13, 1.1315050987891347e-13, 2.851984257290168e-14, 6.1615637027191854e-15, 1.1647770765185347e-15, 1.9572313543781916e-16, 2.959947604231638e-17, 4.0694263911474436e-18, 5.128540744612474e-19, 5.96612456840078e-20, 6.444750964629738e-21, 6.497656373956814e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2705146233877969, "lambda_away": 1.5123136044241512, "rho": -0.02181659734176786, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3168 |
| Legacy p draw | 0.2568 |
| Legacy p away | 0.4265 |
| Legacy p over 1 5 | 0.7686 |
| Legacy p under 3 5 | 0.6958 |
| Legacy p btts yes | 0.5634 |
| Legacy p over 2 5 | 0.5264 |
| Legacy goal margin distribution | {"-1": 0.21470836098363472, "-10": 1.2688380968115147e-06, "-11": 1.7197058574216876e-07, "-12": 2.141155630735618e-08, "-13": 2.464305019692437e-09, "-14": 2.620331198889298e-10, "-15": 2.3418621653624026e-11, "-2": 0.12844698780854089, "-3": 0.05646072894464762, "-4": 0.01957469817222689, "-5": 0.005578476374312578, "-6": 0.0013464626422251278, "-7": 0.0002814842528353895, "-8": 5.185615389589359e-05, "-9": 8.534521068401114e-06, "0": 0.25678466009069995, "1": 0.17996470468373263, "10": 2.2222059219074588e-07, "11": 2.5302886670778525e-08, "12": 2.646683099714058e-09, "13": 2.559092474353124e-10, "14": 2.2860488940419386e-11, "15": 1.7164393661438028e-12, "2": 0.09065662403081703, "3": 0.03347803107099036, "4": 0.009750936103472113, "5": 0.0023345578679629547, "6": 0.00047339227080429186, "7": 8.314167458280401e-05, "8": 1.2867754755893903e-05, "9": 1.7791781505499431e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3168 |
| Legacy raw p draw | 0.2568 |
| Legacy raw p away | 0.4265 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.2705 |
| Legacy lambda away | 1.5123 |
| Legacy model home team | Valencia |
| Legacy model away team | Villarreal |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 9.873997057540466, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,456.5878 |
| Elo away rating | 1,556.2139 |
| Elo rating diff | -39.6261 |
| Elo home expectancy | 0.4432 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **51.2%**. Expected goals are 1.24 for Athletic Bilbao and 0.61 for Getafe (1.85 combined). The most likely exact score is 1-0 at 19.1%. Goal-market probabilities: at least one goal: 83.9%; Over 2.5 goals: 28.3%; Under 3.5 goals: 88.3%; Double Chance 1X: 82.1%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 69.2%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 32.9%; BTTS No (at least one team does not score): 67.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 51.2% | 1.95 |
| Draw | 30.8% | 3.24 |
| Getafe win | 17.9% | 5.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.24 |
| Getafe expected goals | 0.61 |
| Expected total goals | 1.85 |
| Over 0.5 | 83.9% |
| Under 0.5 | 16.1% |
| Over 1.5 | 55.6% |
| Under 1.5 | 44.4% |
| Over 2.5 | 28.3% |
| Under 2.5 | 71.7% |
| Over 3.5 | 11.7% |
| Under 3.5 | 88.3% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.10% |
| 2 | 0-0 | 16.11% |
| 3 | 1-1 | 12.29% |
| 4 | 2-0 | 12.07% |
| 5 | 0-1 | 9.22% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:00:00+00:00 |
| Fixture id | 9c4254cba9944a839b421db27260504d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2394 |
| Dc lambda away | 0.6108 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:38:12.675051+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 32.9% |
| P btts no | 67.1% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.21 |
| Fair Over 1.5 odds | 1.80 |
| Fair Under 1.5 odds | 2.25 |
| Fair Over 2.5 odds | 3.54 |
| Fair Under 2.5 odds | 1.39 |
| Fair Over 3.5 odds | 8.55 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.91 |
| Fair Under 4.5 odds | 1.04 |
| Goal margin distribution | {"-1": 0.13341018410697142, "-10": 3.354269709637201e-10, "-11": 1.8520045747803293e-11, "-12": 9.381339261026198e-13, "-13": 4.3840352356907765e-14, "-14": 1.8146116760910165e-15, "-2": 0.037463476222704406, "-3": 0.007190284676704566, "-4": 0.001058870556418794, "-5": 0.0001262249451660119, "-6": 1.2625420360968722e-05, "-7": 1.0871377367004918e-06, "-8": 8.214822323540749e-08, "-9": 5.529057887292734e-09, "0": 0.30842131104218345, "1": 0.2746563875839844, "10": 3.967842855462481e-07, "11": 4.4452294908108696e-08, "12": 4.568910196440873e-09, "13": 4.3322894438475006e-10, "14": 3.638503339120771e-11, "2": 0.15424083569611216, "3": 0.06006659728470536, "4": 0.017948388671815547, "5": 0.004341336328168967, "6": 0.000881088913854614, "7": 0.00015394093131241513, "8": 2.3602791032031743e-05, "9": 3.2233834515113107e-06} |
| Raw goal margin distribution | {"-1": 0.13341018410697142, "-10": 3.354269709637201e-10, "-11": 1.8520045747803293e-11, "-12": 9.381339261026198e-13, "-13": 4.3840352356907765e-14, "-14": 1.8146116760910165e-15, "-2": 0.037463476222704406, "-3": 0.007190284676704566, "-4": 0.001058870556418794, "-5": 0.0001262249451660119, "-6": 1.2625420360968722e-05, "-7": 1.0871377367004918e-06, "-8": 8.214822323540749e-08, "-9": 5.529057887292734e-09, "0": 0.30842131104218345, "1": 0.2746563875839844, "10": 3.967842855462481e-07, "11": 4.4452294908108696e-08, "12": 4.568910196440873e-09, "13": 4.3322894438475006e-10, "14": 3.638503339120771e-11, "2": 0.15424083569611216, "3": 0.06006659728470536, "4": 0.017948388671815547, "5": 0.004341336328168967, "6": 0.000881088913854614, "7": 0.00015394093131241513, "8": 2.3602791032031743e-05, "9": 3.2233834515113107e-06} |
| Unadjusted home-win probability | 51.2% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 17.9% |
| Raw p over 1 5 | 55.6% |
| Raw p under 3 5 | 88.3% |
| Raw p btts yes | 32.9% |
| P home draw | 82.1% |
| P draw away | 48.8% |
| P home away | 69.2% |
| Raw p home draw | 82.1% |
| Raw p draw away | 48.8% |
| Raw p home away | 69.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.2829 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.14931663500498682, 0.08935931333721323, 0.028813337759037317, 0.006019131889573665, 0.00094305150466434, 0.00011820257894533937, 1.2346311946046341e-05, 1.105352377944132e-06, 8.65909106436238e-08, 6.029639420940104e-09, 3.778791116606514e-10, 2.1528895248776318e-11, 1.1243513422751282e-12, 5.420261436910815e-14, 2.4263516483911823e-15], [0.18704774087330042, 0.12144113869273451, 0.03724126516970695, 0.007779733422961185, 0.001218894924552095, 0.00015277694042460977, 1.595761938085144e-05, 1.4286689503742837e-06, 1.1191883049210946e-07, 7.79331441677624e-09, 4.884090943276337e-10, 2.782611662264118e-11, 1.4532251289925876e-12, 7.005692820083638e-14, 3.136061704769001e-15], [0.1225553274468353, 0.0768057507784932, 0.02406718449349768, 0.005027656250329005, 0.0007877113973895115, 9.873216698722914e-05, 1.031261875679687e-05, 9.232779566457499e-07, 7.23275949266384e-08, 5.0364329737368305e-09, 3.1563459855404703e-10, 1.7982640478053274e-11, 9.39147398206579e-13, 4.527432159927657e-14, 2.026681297956084e-15], [0.052800957269361834, 0.03309050083241563, 0.010368952590708724, 0.002166083420190941, 0.00033937256503349916, 4.25371384403151e-05, 4.443023030141735e-06, 3.977791986051668e-07, 3.116116066658808e-08, 2.1698647278441936e-09, 1.3598600157315942e-10, 7.74752637239603e-12, 4.046162878055971e-13, 1.9505700567768154e-14, 8.731624715246703e-16], [0.017061321282241193, 0.010692375579707675, 0.003350470155454189, 0.0006999161959788493, 0.00010965983697751251, 1.3744822497347116e-05, 1.4356528233936155e-06, 1.2853249368516997e-07, 1.0068957101440484e-08, 7.011380318711423e-10, 4.394050757245052e-11, 2.5034212146525903e-12, 1.3074172968232812e-13, 6.302783915908145e-15, 2.8214082146806944e-16], [0.004410354644305106, 0.0027639810256491234, 0.0008660971425521353, 0.00018092846354008664, 2.8347087737625777e-05, 3.553039107201028e-06, 3.7111651509982147e-07, 3.322567291775663e-08, 2.6028272360048693e-09, 1.8124430833973664e-10, 1.1358629172934953e-11, 6.471348378034075e-13, 3.379676082350835e-14, 1.6292707848196325e-15, 7.29334534954786e-17], [0.0009500645625450479, 0.0005954079968165218, 0.00018657189029522091, 3.8975033852916745e-05, 6.106439432404614e-06, 7.65384377750024e-07, 7.994473869053396e-08, 7.157368726942117e-09, 5.606927602859304e-10, 3.904307213455449e-11, 2.4468397502296912e-12, 1.394037274030206e-13, 7.280390666244295e-15, 3.50972327689303e-16, 1.5711092458189162e-17], [0.00017542275831706897, 0.00010993791079397557, 3.4449191044809e-05, 7.196466654502345e-06, 1.1275112144578514e-06, 1.4132285742563563e-07, 1.4761235316958587e-08, 1.3215579381353687e-09, 1.0352798583949429e-10, 7.209029446028928e-12, 4.517917992807865e-13, 2.5739920574670542e-14, 1.3442730764288045e-15, 6.480457880808538e-17, 2.9009430346575634e-18], [2.8341759265803548e-05, 1.776185616849387e-05, 5.565701331231726e-06, 1.1626799592196491e-06, 1.8216365833160476e-07, 2.283249016455076e-08, 2.384863753327555e-09, 2.1351435411103017e-10, 1.6726251941798168e-11, 1.1647096366490129e-12, 7.299266375880705e-14, 4.1586088341493896e-15, 2.171842712151631e-16, 1.0469997105967513e-17, 4.686839377104602e-19], [4.070194393307532e-06, 2.5508016885517386e-06, 7.992971128132039e-07, 1.6697387790378847e-07, 2.616074372278969e-08, 3.2790015814273783e-09, 3.4249317364388966e-10, 3.06630551351116e-11, 2.4020773105887845e-12, 1.6726536233902558e-13, 1.048256489646163e-14, 5.972228541626533e-16, 3.119009637771957e-17, 1.5036089721527327e-18, 6.730826825574361e-20], [5.26072994253772e-07, 3.2969134944769207e-07, 1.0330922427868084e-07, 2.1581388853427362e-08, 3.3812784973569417e-09, 4.2381125160525445e-10, 4.426727373674716e-11, 3.963202655485021e-12, 3.1046871011573585e-13, 2.1619063243101648e-14, 1.3548724629979568e-15, 7.71911080322674e-17, 4.031322783862648e-18, 1.943415959365109e-19, 8.699599772815995e-21], [6.181362017280446e-08, 3.8738760726402475e-08, 1.2138842365340932e-08, 2.5358149685665785e-09, 3.9730050205403475e-10, 4.979785698531933e-11, 5.201408311655092e-12, 4.656766385841607e-13, 3.64800990209678e-14, 2.540241712457646e-15, 1.5919762604264733e-16, 9.069961554275849e-18, 4.7368075928157495e-19, 2.283515353612924e-20, 1.022203690145815e-21], [6.657846675055131e-09, 4.17249027927842e-09, 1.3074553966450983e-09, 2.731285954426903e-10, 4.279260491787145e-11, 5.363647940821408e-12, 5.602354131103436e-13, 5.015728978793025e-14, 3.929213420819664e-15, 2.736053929836541e-16, 1.7146922996285367e-17, 9.769111274861226e-19, 5.101940089261953e-20, 2.4595380535854777e-21, 1.100999330024781e-22], [6.619440663170257e-10, 4.1484211291347423e-10, 1.299913296330498e-10, 2.7155304397768396e-11, 4.2545754340909666e-12, 5.332707557749316e-13, 5.5700367633652183e-14, 4.986795577924458e-15, 3.906547621394814e-16, 2.7202709109603836e-17, 1.7048010395781707e-18, 9.712757828763901e-20, 5.0725093767106635e-21, 2.4453501258172974e-22, 1.0946481784561218e-23], [6.111166469249454e-11, 3.829884335355984e-11, 1.2000993669549482e-11, 2.5070182533885803e-12, 3.9278875749082916e-13, 4.923235251363797e-14, 5.142341118057811e-15, 4.603884146038693e-16, 3.606583101080387e-17, 2.5113947271753315e-18, 1.573897777765118e-19, 8.966963069452836e-21, 4.683016405053972e-22, 2.2575837529016358e-23, 1.0105955448813095e-24]] |
| Legacy trial inputs | {"lambda_home": 1.2925009063910415, "lambda_away": 0.626702668733937, "rho": -0.02181659734176786, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5249 |
| Legacy p draw | 0.2971 |
| Legacy p away | 0.1780 |
| Legacy p over 1 5 | 0.5743 |
| Legacy p under 3 5 | 0.8714 |
| Legacy p btts yes | 0.3404 |
| Legacy p over 2 5 | 0.3015 |
| Legacy goal margin distribution | {"-1": 0.13198173052336712, "-10": 4.066641635228884e-10, "-11": 2.3028267861839705e-11, "-12": 1.1964349517739207e-12, "-13": 5.733867607387715e-14, "-14": 2.4263516483911823e-15, "-2": 0.037424789164300025, "-3": 0.007341333178963106, "-4": 0.00110654909571856, "-5": 0.00013511535008092272, "-6": 1.3849522951063183e-05, "-7": 1.2224461649834e-06, "-8": 9.470773957203805e-08, "-9": 6.5364421477509655e-09, "0": 0.2971043357706861, "1": 0.2749514878877701, "10": 5.661467584699748e-07, "11": 6.611860879996931e-08, "12": 7.084689781638154e-09, "13": 7.002429096705855e-10, "14": 6.111166469249454e-11, "2": 0.1591834770763749, "3": 0.06439955571567232, "4": 0.02001925615223686, "5": 0.005041401101932589, "6": 0.0010657385801897718, "7": 0.00019400589570754023, "8": 3.0998449324620544e-05, "9": 4.412302017523794e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.5249 |
| Legacy raw p draw | 0.2971 |
| Legacy raw p away | 0.1780 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.2925 |
| Legacy lambda away | 0.6267 |
| Legacy model home team | Ath Bilbao |
| Legacy model away team | Getafe |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 9.81489003483115, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,505.1233 |
| Elo away rating | 1,442.8223 |
| Elo rating diff | 122.3011 |
| Elo home expectancy | 0.6691 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **52.2%**. Expected goals are 2.02 for Barcelona and 1.37 for Real Madrid (3.39 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.9%; Under 3.5 goals: 56.0%; Double Chance 1X: 74.3%; Double Chance X2: 47.8%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 74.5%; BTTS Yes (both teams score): 65.1%; BTTS No (at least one team does not score): 34.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 52.2% | 1.92 |
| Draw | 22.1% | 4.52 |
| Real Madrid win | 25.7% | 3.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.02 |
| Real Madrid expected goals | 1.37 |
| Expected total goals | 3.39 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 65.9% |
| Under 2.5 | 34.1% |
| Over 3.5 | 44.0% |
| Under 3.5 | 56.0% |
| Over 4.5 | 25.5% |
| Under 4.5 | 74.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.62% |
| 2 | 2-1 | 9.41% |
| 3 | 2-0 | 6.86% |
| 4 | 1-0 | 6.49% |
| 5 | 2-2 | 6.46% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T20:00:00+00:00 |
| Fixture id | 72089d103a5fe6a922c35e17efba6ffc |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0202 |
| Dc lambda away | 1.3729 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:38:12.675051+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.1% |
| P btts no | 34.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.31 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.92 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.93 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.14455476740046969, "-10": 2.8282298063782015e-07, "-11": 3.4585768536314854e-08, "-12": 3.888905450616064e-09, "-13": 4.0462391571767556e-10, "-14": 3.9167837416012676e-11, "-15": 3.5423154273166926e-12, "-16": 2.977323296821366e-13, "-17": 2.0672436865385918e-14, "-2": 0.07321346883833783, "-3": 0.027806147937472856, "-4": 0.008464157219757828, "-5": 0.0021381958618335003, "-6": 0.00046026005868472655, "-7": 8.615940126145822e-05, "-8": 1.4253443426382048e-05, "-9": 2.110867084331147e-06, "0": 0.221237969604734, "1": 0.21412615368426152, "10": 1.3458139018146577e-05, "11": 2.421668971990047e-06, "12": 4.006745544422605e-07, "13": 6.134271000008288e-08, "14": 8.737517018206062e-09, "15": 1.1627670149063348e-09, "16": 1.4380649454279987e-10, "17": 1.4692348122933064e-11, "2": 0.1585203589806702, "3": 0.0885894333048373, "4": 0.0396800168363201, "5": 0.014749681496172777, "6": 0.004671813288130387, "7": 0.0012868617517592144, "8": 0.0003132535839227544, "9": 6.82628115185771e-05} |
| Raw goal margin distribution | {"-1": 0.14455476740046969, "-10": 2.8282298063782015e-07, "-11": 3.4585768536314854e-08, "-12": 3.888905450616064e-09, "-13": 4.0462391571767556e-10, "-14": 3.9167837416012676e-11, "-15": 3.5423154273166926e-12, "-16": 2.977323296821366e-13, "-17": 2.0672436865385918e-14, "-2": 0.07321346883833783, "-3": 0.027806147937472856, "-4": 0.008464157219757828, "-5": 0.0021381958618335003, "-6": 0.00046026005868472655, "-7": 8.615940126145822e-05, "-8": 1.4253443426382048e-05, "-9": 2.110867084331147e-06, "0": 0.221237969604734, "1": 0.21412615368426152, "10": 1.3458139018146577e-05, "11": 2.421668971990047e-06, "12": 4.006745544422605e-07, "13": 6.134271000008288e-08, "14": 8.737517018206062e-09, "15": 1.1627670149063348e-09, "16": 1.4380649454279987e-10, "17": 1.4692348122933064e-11, "2": 0.1585203589806702, "3": 0.0885894333048373, "4": 0.0396800168363201, "5": 0.014749681496172777, "6": 0.004671813288130387, "7": 0.0012868617517592144, "8": 0.0003132535839227544, "9": 6.82628115185771e-05} |
| Unadjusted home-win probability | 52.2% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 56.0% |
| Raw p btts yes | 65.1% |
| P home draw | 74.3% |
| P draw away | 47.8% |
| P home away | 77.9% |
| Raw p home draw | 74.3% |
| Raw p draw away | 47.8% |
| Raw p home away | 77.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6589 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.047178172845865216, 0.05776620197502081, 0.04022711599979686, 0.017956405654449052, 0.006011476885928603, 0.0016100261954641233, 0.0003593382568139991, 6.874279428703918e-05, 1.150691644205228e-05, 1.7121358262122184e-06, 2.29276730386069e-07, 2.7911878088032114e-08, 3.1147957855639223e-09, 3.2085439385618035e-10, 3.0690341446673255e-11, 2.739884314315742e-12, 2.2931581551715525e-13], [0.07687179892312461, 0.10835246394064037, 0.07099987894458003, 0.03169261817705483, 0.010610110135194058, 0.002841656980235241, 0.0006342232620921465, 0.00012132935586823064, 2.0309426965016207e-05, 3.0218779889256757e-06, 4.0466783903430254e-07, 4.9263784293563654e-08, 5.497538618310179e-09, 5.663001822636364e-10, 5.4167704378624404e-11, 4.835829012439114e-12, 4.04736823337718e-13], [0.06987998270919535, 0.09357817125084486, 0.06265652762890676, 0.027968349185398384, 0.009363292849420824, 0.002507727643211383, 0.0005596942971577487, 0.00010707167746143856, 1.7922821710077628e-05, 2.6667704863567325e-06, 3.5711443475522044e-07, 4.347468907804111e-08, 4.851510811701585e-09, 4.997530072403754e-10, 4.780233877078774e-11, 4.267560151237276e-12, 3.5717531256201625e-13], [0.041112155235681236, 0.0550543968956886, 0.03686241453619311, 0.016454484801189464, 0.005508661196218055, 0.0014753593827513782, 0.0003292822627766192, 6.299296671921203e-05, 1.0544447778021408e-05, 1.5689282962373188e-06, 2.1009942345946297e-07, 2.5577255415723082e-08, 2.854266098609316e-09, 2.9401729102690876e-10, 2.8123320813510247e-11, 2.5107132058890354e-12, 2.1013523940769827e-13], [0.01814048790434598, 0.024292417053838097, 0.016265315724397537, 0.00726044112251164, 0.0024306631755565225, 0.000650993334792054, 0.00014529379135615528, 2.7795262600024564e-05, 4.652673309843704e-06, 6.922800475314858e-07, 9.270508996980581e-08, 1.128580804960088e-08, 1.2594275182311326e-09, 1.2973333752430386e-10, 1.2409243887188551e-11, 1.107836898396968e-12, 9.272089353865353e-14], [0.006403503771986473, 0.008575104763177481, 0.0057415771363447015, 0.002562900312243016, 0.0008580122483572178, 0.0002297974727504586, 5.1287999854318086e-05, 9.811592160096797e-06, 1.6423709905987275e-06, 2.4437148102156666e-07, 3.272444470260234e-08, 3.98383520865615e-09, 4.445717726040058e-10, 4.579523552893242e-11, 4.380402581127644e-12, 3.9106102300210097e-13, 3.273002328534283e-14], [0.0018836713384842902, 0.002522475138932684, 0.0016889572762872219, 0.0007539094273176306, 0.00025239511646255806, 6.759782276850012e-05, 1.5087011544586865e-05, 2.8862034903023316e-06, 4.831241258391829e-07, 7.188495097903025e-08, 9.626307838495067e-09, 1.171895335272401e-09, 1.3077638989092647e-10, 1.3471245692454274e-11, 1.2885506258604233e-12, 1.1503552849456485e-13, 9.627948848915577e-15], [0.000474947712257555, 0.0006360153026624332, 0.000425852630490644, 0.00019009025111675463, 6.363874668567659e-05, 1.7044072722009277e-05, 3.804029647587385e-06, 7.277255415118665e-07, 1.2181461469195928e-07, 1.812502654561235e-08, 2.4271712330979605e-09, 2.9548095632266217e-10, 3.297387709151873e-11, 3.3966314569711012e-12, 3.248943482746275e-13, 2.900498615156267e-14, 2.427584996438247e-15], [0.000104783891528111, 0.00014031893777869013, 9.395243873939212e-05, 4.1938082318350105e-05, 1.4040104536982738e-05, 3.7602965994112894e-06, 8.392524475333428e-07, 1.6055222972137244e-07, 2.6874978114431074e-08, 3.998778742342212e-09, 5.354872560606645e-10, 6.518958545724384e-11, 7.274761139485838e-12, 7.493714633480015e-13, 7.167882541403557e-14, 6.399136671768144e-15, 5.355785413365968e-16], [2.0549001529425698e-05, 2.7517722666829394e-05, 1.8424862631019017e-05, 8.22441030900022e-06, 2.753382465532449e-06, 7.374257573900761e-07, 1.645844564124657e-07, 3.1485641218164674e-08, 5.270409013474841e-09, 7.841941093606034e-10, 1.0501355011067257e-10, 1.2784225435110448e-11, 1.4266417824479899e-12, 1.4695804022811e-13, 1.405681991363437e-14, 1.2549244672774009e-15, 1.0503145192026746e-16], [3.6268486685164844e-06, 4.856810958521806e-06, 3.2519433319044613e-06, 1.4515883672409434e-06, 4.859652920232221e-07, 1.301538482290777e-07, 2.9048755276176355e-08, 5.557138908475218e-09, 9.30214340861589e-10, 1.3840834832389365e-10, 1.8534635556364497e-11, 2.256384619512983e-12, 2.5179879624380395e-13, 2.5937735795380467e-14, 2.480994442203716e-15, 2.2149110878775643e-16, 1.8537795182110806e-17], [5.819363156485648e-07, 7.792866296127648e-07, 5.217818812496722e-07, 2.3291073421490102e-07, 7.797426289880157e-08, 2.088348807144825e-08, 4.66094043744854e-09, 8.916558802184986e-10, 1.4925505742313576e-10, 2.220794183606114e-11, 2.973925441441566e-12, 3.6204216723014507e-13, 4.0401703286616454e-14, 4.161770116315235e-15, 3.9808133638814237e-16, 3.553876424890503e-17, 2.974432410751203e-18], [8.559195072280721e-08, 1.1461849176128618e-07, 7.674435821762024e-08, 3.4256813932495154e-08, 1.1468556074290253e-08, 3.0715706063809024e-09, 6.855371859709761e-10, 1.3114590739419034e-10, 2.1952628108203028e-11, 3.2663729899184225e-12, 4.3740882462968686e-13, 5.324963317095112e-14, 5.9423351040939305e-15, 6.121185654452698e-16, 5.855032107736641e-17, 5.227087701085704e-18, 4.374833903355924e-19], [1.1620592782357314e-08, 1.5561449491896792e-08, 1.0419378547388162e-08, 4.650957027720077e-09, 1.557055527015175e-09, 4.1701901776494687e-10, 9.307357068109351e-11, 1.7805333001886348e-11, 2.9804502595590765e-12, 4.434668221788602e-13, 5.93858392933754e-14, 7.229561864917787e-15, 8.067751212332417e-16, 8.310571874447075e-17, 7.94922224310338e-18, 7.096678729603914e-19, 5.939596288206031e-20], [1.4650044952901099e-09, 1.9618270673309107e-09, 1.3135677926196549e-09, 5.863446969207746e-10, 1.962975029945768e-10, 5.2573457059320616e-11, 1.1733755927453092e-11, 2.2447127591893255e-12, 3.7574443146065343e-13, 5.5907723484675615e-14, 7.486754174318668e-15, 9.11428601745907e-16, 1.0170988704546622e-16, 1.0477111953342828e-17, 1.0021559603987936e-18, 8.946760664640041e-20, 7.488030451975896e-21], [1.7237981435107653e-10, 2.3083846277785708e-10, 1.5456100848652333e-10, 6.899227294242946e-11, 2.3097353784627304e-11, 6.18605799287008e-12, 1.3806528750716679e-12, 2.6412421937580717e-13, 4.421198402248718e-14, 6.578384589305474e-15, 8.809292386544064e-16, 1.0724328400924693e-16, 1.1967698053441457e-17, 1.2327898100374341e-18, 1.1791872240648616e-19, 1.0527209625447324e-20, 8.810794119175744e-22], [1.901538559133444e-11, 2.5464016164282645e-11, 1.7049775722411326e-11, 7.61060497577159e-12, 2.5478916426934483e-12, 6.823900957754243e-13, 1.5230116638716697e-13, 2.913580046682429e-14, 4.877067115487706e-15, 7.256680256017147e-16, 9.717616424378985e-17, 1.1830111345656438e-17, 1.3201684546623985e-18, 1.359902473452417e-19, 1.3007729376191078e-20, 1.1612667700232856e-21, 9.719273000304302e-23]] |
| Legacy trial inputs | {"lambda_home": 1.764975618558849, "lambda_away": 1.3391269949259896, "rho": -0.02181659734176786, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4729 |
| Legacy p draw | 0.2373 |
| Legacy p away | 0.2897 |
| Legacy p over 1 5 | 0.8182 |
| Legacy p under 3 5 | 0.6239 |
| Legacy p btts yes | 0.6139 |
| Legacy p over 2 5 | 0.5997 |
| Legacy goal margin distribution | {"-1": 0.16294838476005838, "-10": 2.8369885271522017e-07, "-11": 3.393843360131786e-08, "-12": 3.731501740697775e-09, "-13": 3.7949979362544973e-10, "-14": 3.5883345771674385e-11, "-15": 3.14462113765346e-12, "-16": 2.2931581551715525e-13, "-2": 0.08291399359022003, "-3": 0.031433037707986514, "-4": 0.0094807281040447, "-5": 0.0023625917929208295, "-6": 0.0005002561858596968, "-7": 9.1940835344338e-05, "-8": 1.491279266199385e-05, "-9": 2.1632668516263904e-06, "0": 0.23731795228006983, "1": 0.2155024058975226, "10": 4.487733249236743e-06, "11": 7.075843103980403e-07, "12": 1.0253850817190878e-07, "13": 1.374459146315052e-08, "14": 1.7128927337903784e-09, "15": 1.9784383051535918e-10, "16": 1.901538559133444e-11, "2": 0.1440329065216648, "3": 0.07196762819064381, "4": 0.02860944768803666, "5": 0.00939665795516551, "6": 0.0026223710427001495, "7": 0.0006352242422312314, "8": 0.00013579836583890902, "9": 2.596346222190242e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.4729 |
| Legacy raw p draw | 0.2373 |
| Legacy raw p away | 0.2897 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.7650 |
| Legacy lambda away | 1.3391 |
| Legacy model home team | Barcelona |
| Legacy model away team | Real Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 10.654616418300819, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,725.4846 |
| Elo away rating | 1,670.4419 |
| Elo rating diff | 115.0427 |
| Elo home expectancy | 0.6598 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **40.1%**. Expected goals are 1.40 for Celta Vigo and 1.25 for Real Betis (2.65 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.6%; Double Chance 1X: 66.9%; Double Chance X2: 59.9%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 54.1%; BTTS No (at least one team does not score): 45.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 40.1% | 2.49 |
| Draw | 26.8% | 3.73 |
| Real Betis win | 33.1% | 3.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.40 |
| Real Betis expected goals | 1.25 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 1-0 | 9.51% |
| 3 | 2-1 | 8.66% |
| 4 | 0-1 | 8.44% |
| 5 | 1-2 | 7.72% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:15:00+00:00 |
| Fixture id | 2013e3955186ebe5258e85eb741a7553 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3994 |
| Dc lambda away | 1.2482 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:38:12.675051+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.1% |
| P btts no | 45.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.36 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.93 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.73 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.18765580302792859, "-10": 2.09748396438536e-07, "-11": 2.3492630247497576e-08, "-12": 2.4160979332081245e-09, "-13": 2.2832900156709258e-10, "-14": 1.809877392432889e-11, "-2": 0.09518400626523671, "-3": 0.034909133588825, "-4": 0.010061107188492215, "-5": 0.002378502593956391, "-6": 0.0004756051060781712, "-7": 8.22985114461609e-05, "-8": 1.254185803023313e-05, "-9": 1.7067742503756342e-06, "0": 0.26825868278129633, "1": 0.2108719633681629, "10": 6.580816131042637e-07, "11": 8.263629960510804e-08, "12": 9.528221900779355e-09, "13": 1.009523695836547e-09, "14": 8.971451334427122e-11, "2": 0.1196410460895566, "3": 0.049194143360985904, "4": 0.015895647336262763, "5": 0.004213026424973008, "6": 0.0009444852349290493, "7": 0.00018323091709624326, "8": 3.1305941283807584e-05, "9": 4.776382284349446e-06} |
| Raw goal margin distribution | {"-1": 0.18765580302792859, "-10": 2.09748396438536e-07, "-11": 2.3492630247497576e-08, "-12": 2.4160979332081245e-09, "-13": 2.2832900156709258e-10, "-14": 1.809877392432889e-11, "-2": 0.09518400626523671, "-3": 0.034909133588825, "-4": 0.010061107188492215, "-5": 0.002378502593956391, "-6": 0.0004756051060781712, "-7": 8.22985114461609e-05, "-8": 1.254185803023313e-05, "-9": 1.7067742503756342e-06, "0": 0.26825868278129633, "1": 0.2108719633681629, "10": 6.580816131042637e-07, "11": 8.263629960510804e-08, "12": 9.528221900779355e-09, "13": 1.009523695836547e-09, "14": 8.971451334427122e-11, "2": 0.1196410460895566, "3": 0.049194143360985904, "4": 0.015895647336262763, "5": 0.004213026424973008, "6": 0.0009444852349290493, "7": 0.00018323091709624326, "8": 3.1305941283807584e-05, "9": 4.776382284349446e-06} |
| Unadjusted home-win probability | 40.1% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 33.1% |
| Raw p over 1 5 | 74.6% |
| Raw p under 3 5 | 72.6% |
| Raw p btts yes | 54.1% |
| P home draw | 66.9% |
| P draw away | 59.9% |
| P home away | 73.2% |
| Raw p home draw | 66.9% |
| Raw p draw away | 59.9% |
| Raw p home away | 73.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4934 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.07815160211620305, 0.09306616705056928, 0.06087303481014216, 0.025782956504983384, 0.008190336429888841, 0.0020814249388908866, 0.00044079688843499357, 8.001464761272415e-05, 1.2708916511195019e-05, 1.7942999044683336e-06, 2.279943321608224e-07, 2.6336640910884915e-08, 2.7887408160714016e-09, 2.7257989350114713e-10, 2.4739721056384647e-11], [0.09635162347286853, 0.12866792700478652, 0.08000117625552551, 0.033884738196099586, 0.010763986884557606, 0.002735471361304836, 0.0005793085505685959, 0.00010515766047568212, 1.6702440957641763e-05, 2.358122990916288e-06, 2.996370200590002e-07, 3.46124069230592e-08, 3.6650471962395863e-09, 3.5823270799149307e-10, 3.251368674023469e-11], [0.06511930510074017, 0.08274443107446604, 0.05256997800610161, 0.022266171887546895, 0.007073177923931794, 0.0017975194369743263, 0.0003806723749269158, 6.910068272899791e-05, 1.0975425548581146e-05, 1.549558138647864e-06, 1.9689599942885235e-07, 2.274433396918695e-08, 2.408357720669538e-09, 2.3540010861875676e-10, 2.136523332322081e-11], [0.028527250865948695, 0.03624840804688905, 0.023029682953118916, 0.009754291300832153, 0.0030985945065497783, 0.0007874513991765954, 0.0001667637011862581, 3.02713996743194e-05, 4.808078303362578e-06, 6.78825329665222e-07, 8.625555143008915e-08, 9.963762971889266e-09, 1.0550454241825654e-09, 1.0312330486405198e-10, 9.359611099629487e-12], [0.009372843130502633, 0.011909687475685953, 0.007566575786748734, 0.0032048458732157545, 0.001018066562789434, 0.00025872308804164855, 5.479147003774325e-05, 9.94589635788617e-06, 1.5797303395393975e-06, 2.2303317476548128e-07, 2.83399110726873e-08, 3.273669368417884e-09, 3.466431203934006e-10, 3.388193850615598e-11, 3.075170720500517e-12], [0.002463614563122787, 0.003130414016196975, 0.0019888443710896486, 0.0008423809996481707, 0.0002675947495754051, 6.800433535916045e-05, 1.4401720122744796e-05, 2.6142393262570534e-06, 4.152258408796668e-07, 5.862338350927712e-08, 7.449032984352638e-09, 8.604709818130472e-10, 9.111376641184759e-11, 8.905732867644855e-12, 8.082964011697473e-13], [0.0005396260799350074, 0.0006856807348925317, 0.00043563319832446617, 0.00018451374799298068, 5.8613513609664784e-05, 1.4895557713351766e-05, 3.1545290771081356e-06, 5.72618680193164e-07, 9.095038491637794e-08, 1.2840769456866166e-08, 1.6316239272256814e-09, 1.8847614791862198e-10, 1.9957409463685148e-11, 1.95069707260698e-12, 1.7704791362976922e-13], [0.0001013132644917753, 0.0001287346113061265, 8.178889620857522e-05, 3.4641932345139985e-05, 1.1004520774539754e-05, 2.7965986717081373e-06, 5.922538784162256e-07, 1.0750753152317712e-07, 1.707567655694395e-08, 2.410818010163773e-09, 3.063327601031328e-10, 3.538586168179665e-11, 3.746946967071192e-12, 3.662378372894162e-13, 3.3240243139194026e-14], [1.6643618054588018e-05, 2.1148363067098255e-05, 1.3436178929091529e-05, 5.690933892197251e-06, 1.8078090915734677e-06, 4.594217783561503e-07, 9.729473621401559e-08, 1.7661204597830323e-08, 2.8051710707686193e-09, 3.96046207390199e-10, 5.0323967768092015e-11, 5.813145685500208e-12, 6.155438234427099e-13, 6.016509991619347e-14, 5.460666119344101e-15], [2.4303938073138775e-06, 3.088201763854609e-06, 1.9620256819233755e-06, 8.310218633992337e-07, 2.639863523997842e-07, 6.7087326890088e-08, 1.4207519278754203e-08, 2.578987461950183e-09, 4.0962670355035684e-10, 5.783287303844066e-11, 7.348586059947379e-12, 8.48867910133186e-13, 8.988513745742168e-14, 8.785642987789462e-15, 7.973968806983131e-16], [3.1940967614918396e-07, 4.058607795607952e-07, 2.5785532606839473e-07, 1.0921539688854234e-07, 3.4693881738042873e-08, 8.81681861235505e-09, 1.8671949862831823e-09, 3.389383019062017e-10, 5.383437545361547e-11, 7.600570406489501e-12, 9.657733189159108e-13, 1.1156077811469633e-13, 1.1812975559557998e-14, 1.1546356697615494e-15, 1.0479630036076883e-16], [3.81616199252477e-08, 4.849040579763092e-08, 3.080738526069864e-08, 1.3048560445297835e-08, 4.145067690436237e-09, 1.053393512967321e-09, 2.2308399123007892e-10, 4.049481158927744e-11, 6.431887097917545e-12, 9.080816917145194e-13, 1.1538621739561906e-13, 1.3328775960404822e-14, 1.4113607606537886e-15, 1.3795063478601082e-16, 1.2520586828032998e-17], [4.17942921601506e-09, 5.3106293465535905e-09, 3.3739994863899854e-09, 1.4290676040179198e-09, 4.539644030233558e-10, 1.1536679084064806e-10, 2.4431975172924666e-11, 4.43495844738181e-12, 7.044149830065794e-13, 9.945235973510388e-14, 1.2637003592964879e-14, 1.4597565766797966e-15, 1.5457106928291367e-16, 1.5108240020257335e-17, 1.3712443678554027e-18], [4.225178298767547e-10, 5.368760830276844e-10, 3.4109321328667414e-10, 1.4447105372262617e-10, 4.5893361148871686e-11, 1.1662962473213579e-11, 2.4699413714462785e-12, 4.4835046173314407e-13, 7.121256864744532e-14, 1.0054099026341071e-14, 1.2775331410768974e-15, 1.4757354390969683e-16, 1.5626304306073664e-17, 1.5273618613172045e-18, 1.3862543533860859e-19], [3.966326150873766e-11, 5.039848018987784e-11, 3.201964120991357e-11, 1.3562015089197211e-11, 4.308174131476536e-12, 1.0948440464076943e-12, 2.318622401225051e-13, 4.2088263154414446e-14, 6.684978794377619e-15, 9.4381427414041e-16, 1.1992661013948784e-16, 1.3853256951473107e-17, 1.4668971349391362e-18, 1.4337892661610836e-19, 1.3013265961348088e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3142301267719347, "lambda_away": 1.2706589996078679, "rho": -0.02181659734176786, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3751 |
| Legacy p draw | 0.2702 |
| Legacy p away | 0.3547 |
| Legacy p over 1 5 | 0.7324 |
| Legacy p under 3 5 | 0.7393 |
| Legacy p btts yes | 0.5288 |
| Legacy p over 2 5 | 0.4778 |
| Legacy goal margin distribution | {"-1": 0.1987058246062204, "-10": 2.651212952801357e-07, "-11": 3.024644782684289e-08, "-12": 3.1683387573861156e-09, "-13": 3.050935802413818e-10, "-14": 2.4739721056384647e-11, "-2": 0.10267590145110185, "-3": 0.03852160080290676, "-4": 0.011338391587152186, "-5": 0.0027348729249836506, "-6": 0.0005576380205000845, "-7": 9.835626902751601e-05, "-8": 1.5274254990413224e-05, "-9": 2.117770994155611e-06, "0": 0.27023313422666373, "1": 0.20561368401338515, "10": 3.7142286066105895e-07, "11": 4.3826904500177166e-08, "12": 4.7483249402526574e-09, "13": 4.729163100666326e-10, "14": 3.966326150873766e-11, "2": 0.10983817997478641, "3": 0.042621774956260385, "4": 0.012975409082192066, "5": 0.0032370481588782094, "6": 0.0006826636641958864, "7": 0.00012453713158419637, "8": 2.0003189564184054e-05, "9": 2.8685380279445846e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3751 |
| Legacy raw p draw | 0.2702 |
| Legacy raw p away | 0.3547 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.3142 |
| Legacy lambda away | 1.2707 |
| Legacy model home team | Celta |
| Legacy model away team | Betis |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 8.736079430814915, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,477.5606 |
| Elo away rating | 1,548.8372 |
| Elo rating diff | -11.2766 |
| Elo home expectancy | 0.4838 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **54.6%**. Expected goals are 2.01 for Real Sociedad and 1.25 for Levante (3.26 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 63.2%; Under 3.5 goals: 59.0%; Double Chance 1X: 76.8%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 77.1%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 54.6% | 1.83 |
| Draw | 22.2% | 4.51 |
| Levante win | 23.2% | 4.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 2.01 |
| Levante expected goals | 1.25 |
| Expected total goals | 3.26 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 83.9% |
| Under 1.5 | 16.1% |
| Over 2.5 | 63.2% |
| Under 2.5 | 36.8% |
| Over 3.5 | 41.0% |
| Under 3.5 | 59.0% |
| Over 4.5 | 22.9% |
| Under 4.5 | 77.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.98% |
| 2 | 2-1 | 9.69% |
| 3 | 2-0 | 7.76% |
| 4 | 1-0 | 7.42% |
| 5 | 3-1 | 6.48% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:30:00+00:00 |
| Fixture id | 3cb8660cd2375b60e81144a7572cfb89 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0063 |
| Dc lambda away | 1.2493 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:38:12.675051+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.99 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.21 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.71 |
| Fair Over 3.5 odds | 2.44 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.36 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.13661679604470478, "-10": 1.2329194606035227e-07, "-11": 1.3745244012814897e-08, "-12": 1.4086216844390468e-09, "-13": 1.3354656210873378e-10, "-14": 1.1777399624734833e-11, "-15": 9.703814678066599e-13, "-16": 7.441962500925765e-14, "-17": 4.766106406045559e-15, "-2": 0.06456646101968705, "-3": 0.022648521406538145, "-4": 0.006337439566453948, "-5": 0.001467455817276631, "-6": 0.00028900799507275345, "-7": 4.9437889422304396e-05, "-8": 7.467059621758006e-06, "-9": 1.0089938636201328e-06, "0": 0.22179943086960852, "1": 0.22129788225116942, "10": 1.4071996049758159e-05, "11": 2.519506892015157e-06, "12": 4.1466708711288023e-07, "13": 6.313642811656364e-08, "14": 8.942085277369022e-09, "15": 1.1832431235595434e-09, "16": 1.457340628027801e-10, "17": 1.498923362890796e-11, "2": 0.16652950155024954, "3": 0.09381367600329085, "4": 0.042158216492064776, "5": 0.01567745391009834, "6": 0.004958638583255119, "7": 0.0013622431088969212, "8": 0.0003304352850027719, "9": 7.170796902886298e-05} |
| Raw goal margin distribution | {"-1": 0.13661679604470478, "-10": 1.2329194606035227e-07, "-11": 1.3745244012814897e-08, "-12": 1.4086216844390468e-09, "-13": 1.3354656210873378e-10, "-14": 1.1777399624734833e-11, "-15": 9.703814678066599e-13, "-16": 7.441962500925765e-14, "-17": 4.766106406045559e-15, "-2": 0.06456646101968705, "-3": 0.022648521406538145, "-4": 0.006337439566453948, "-5": 0.001467455817276631, "-6": 0.00028900799507275345, "-7": 4.9437889422304396e-05, "-8": 7.467059621758006e-06, "-9": 1.0089938636201328e-06, "0": 0.22179943086960852, "1": 0.22129788225116942, "10": 1.4071996049758159e-05, "11": 2.519506892015157e-06, "12": 4.1466708711288023e-07, "13": 6.313642811656364e-08, "14": 8.942085277369022e-09, "15": 1.1832431235595434e-09, "16": 1.457340628027801e-10, "17": 1.498923362890796e-11, "2": 0.16652950155024954, "3": 0.09381367600329085, "4": 0.042158216492064776, "5": 0.01567745391009834, "6": 0.004958638583255119, "7": 0.0013622431088969212, "8": 0.0003304352850027719, "9": 7.170796902886298e-05} |
| Unadjusted home-win probability | 54.6% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 23.2% |
| Raw p over 1 5 | 83.9% |
| Raw p under 3 5 | 59.0% |
| Raw p btts yes | 62.0% |
| P home draw | 76.8% |
| P draw away | 45.4% |
| P home away | 77.8% |
| Raw p home draw | 76.8% |
| Raw p draw away | 45.4% |
| Raw p home away | 77.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6316 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04895172792846992, 0.0474917846688342, 0.026355697181937972, 0.009325160221844419, 0.0024745678105983783, 0.0005253302423613261, 9.29360480503045e-05, 1.4092537821083314e-05, 1.869830631971467e-06, 2.2052752782418059e-07, 2.340808345260237e-08, 2.2587918917144312e-09, 1.9980116777631144e-10, 1.6313897077682613e-11, 1.2368947055509563e-12, 8.752749909965099e-14, 5.8066758817398444e-15, 3.6256152253232016e-16], [0.09143584266439951, 0.10152380538330559, 0.05273124044655339, 0.018657342375207688, 0.004950998993545477, 0.0010510560632327136, 0.0001859420778006031, 2.819568745291865e-05, 3.7410692636273575e-06, 4.4122111490756573e-07, 4.683379340760056e-08, 4.519284674523666e-09, 3.997527876718503e-10, 3.2640078670093104e-11, 2.4747208042052786e-12, 1.7512090721213097e-13, 1.1617724243890076e-14, 7.253960572297963e-16], [0.09363869881719708, 0.09939359942644355, 0.052751094001372366, 0.018664366950516095, 0.004952863067462468, 0.001051451790679906, 0.0001860120858490295, 2.8206303259066287e-05, 3.742477793430146e-06, 4.413872366888461e-07, 4.6851426546455706e-08, 4.520986206011802e-09, 3.999032964369935e-10, 3.265236780999736e-11, 2.475652547982437e-12, 1.7518684104000688e-13, 1.1622098370559475e-14, 7.256691721852898e-16], [0.0624493028122954, 0.06628734771617752, 0.03518063668743075, 0.012447596113739629, 0.003303151895474581, 0.0007012317780802028, 0.00012405474683720565, 1.881128204140921e-05, 2.495924569033927e-06, 2.94368947343828e-07, 3.124604421617921e-08, 3.0151255854229165e-09, 2.667025745795865e-10, 2.1776441051212906e-11, 1.651056428376945e-12, 1.1683519979484832e-13, 7.750982762738469e-15, 4.839615933132143e-16], [0.031236407631169992, 0.033156152603899966, 0.017596941179563008, 0.006226141345494502, 0.0016521977736859762, 0.00035074789753666814, 6.2050727010288e-05, 9.409182287855359e-06, 1.2484321480630855e-06, 1.4723988930393393e-07, 1.562890424784649e-08, 1.5081303970441958e-09, 1.334014946634481e-10, 1.0892319990767051e-11, 8.258390293620997e-13, 5.843959439275809e-14, 3.8769505217182715e-15, 2.420719035407022e-16], [0.012499267312986062, 0.013267454419206586, 0.007041426603575537, 0.00249139420655126, 0.0006611279335019982, 0.00014035198229401676, 2.4829635757883196e-05, 3.7650899553238015e-06, 4.995608754059987e-07, 5.8918130320077836e-08, 6.253915440902433e-09, 6.034792860330315e-10, 5.338068837616415e-11, 4.358568399758066e-12, 3.304599846236286e-13, 2.338463886764833e-14, 1.5513640845761483e-15, 9.686521789078351e-17], [0.00416799111489329, 0.004424149892294286, 0.002348025911037559, 0.000830777409313724, 0.00022045895040433266, 4.6801608487191374e-05, 8.279661410023106e-06, 1.2555025096758709e-06, 1.6658298745857364e-07, 1.964677108914018e-08, 2.085423356286961e-09, 2.0123549958760906e-10, 1.7800262150372962e-11, 1.4534031402762549e-12, 1.1019480144312625e-13, 7.797814430617357e-15, 5.173160600989828e-16, 3.230056269710555e-17], [0.0011913029664967865, 0.0012645187443139638, 0.0006711171296011695, 0.00023745434309528103, 6.301198691834865e-05, 1.3376922716650203e-05, 2.366508211618878e-06, 3.5885006061470893e-07, 4.761305906295737e-08, 5.61547662540428e-09, 5.960595793664371e-10, 5.751750447992959e-11, 5.0877040088658354e-12, 4.1541438664299464e-13, 3.149608294092575e-14, 2.228785812472573e-15, 1.478602377078547e-16, 9.232206859337906e-18], [0.00029793787438719933, 0.00031624871036085763, 0.00016784245207262345, 5.938593643719229e-05, 1.5758927805387488e-05, 3.345489797411121e-06, 5.918498032141707e-07, 8.974629232869658e-08, 1.1907746399729932e-08, 1.404397719552281e-09, 1.4907099963562747e-10, 1.4384790021298635e-11, 1.2724048882126313e-12, 1.0389269801806529e-13, 7.876985340292663e-15, 5.574062401482458e-16, 3.697897694203642e-17, 2.3089207069320907e-18], [6.623334430415646e-05, 7.030395099031449e-05, 3.731236567302828e-05, 1.3201843447931574e-05, 3.5033024698367084e-06, 7.437220866052254e-07, 1.315716971978089e-07, 1.9951129382439547e-08, 2.6471621602391932e-09, 3.122058848355496e-10, 3.3139361234079816e-11, 3.197823546883037e-12, 2.828631010025752e-13, 2.3095958688271812e-14, 1.7511002358980792e-15, 1.23914690258696e-16, 8.22064437713727e-18, 5.132866724909409e-19], [1.3251656292649118e-05, 1.4066084150312654e-05, 7.465282790100348e-06, 2.6413628005550103e-06, 7.00924295869376e-07, 1.4880042027903134e-07, 2.6324246909520057e-08, 3.9917282149026295e-09, 5.296317657961738e-10, 6.246468635773634e-11, 6.630367671233645e-12, 6.398055084344397e-13, 5.659392005249821e-14, 4.6209308846117635e-15, 3.5035190663989935e-16, 2.4792268942023923e-17, 1.6447478975191255e-18, 1.0269598545729258e-19], [2.410299200410545e-06, 2.5584327446836044e-06, 1.3578351824442324e-06, 4.804285974201937e-07, 1.274887631080076e-07, 2.706480805861623e-08, 4.788028747215713e-09, 7.260420216281245e-10, 9.633294083537883e-11, 1.1361491745410301e-11, 1.2059752791254756e-12, 1.1637207239167754e-13, 1.0293677804358872e-14, 8.404855793392738e-16, 6.372433013561404e-17, 4.50938242644215e-18, 2.9915766412281208e-19, 1.867902744884748e-20], [4.018677815262106e-07, 4.265660010652991e-07, 2.2639106894038605e-07, 8.010158016652742e-08, 2.1256127202385916e-08, 4.5124996805775095e-09, 7.983052436807677e-10, 1.210525632986983e-10, 1.6061535105191675e-11, 1.8942948998940458e-12, 2.0107155572845832e-13, 1.940264783545768e-14, 1.716258903574582e-15, 1.4013367100495848e-16, 1.0624720439886106e-17, 7.518467049480498e-19, 4.987838306012815e-20, 3.114343364781e-21], [6.184909024558128e-08, 6.565024694288329e-08, 3.484250864926405e-08, 1.232795981234961e-08, 3.2714046510995955e-09, 6.944921011514131e-10, 1.2286243219702412e-10, 1.86304830994067e-11, 2.4719357457093896e-12, 2.9153970933011896e-13, 3.094573232230546e-14, 2.9861466187236144e-15, 2.641392435313788e-16, 2.1567143381124682e-17, 1.6351877993924937e-18, 1.15712273645261e-19, 7.676486538616263e-21, 4.793101429841901e-22], [8.838910958975803e-09, 9.382137794732979e-09, 4.979375287742275e-09, 1.7618001922829441e-09, 4.675194785733242e-10, 9.925051151787829e-11, 1.7558384352634578e-11, 2.6624996517248564e-12, 3.5326663441416965e-13, 4.166421076757408e-14, 4.4224833618583285e-15, 4.2675298809638356e-16, 3.77483847389636e-17, 3.0821805014156166e-18, 2.336862078754091e-19, 1.6536548549866096e-20, 1.097053824448988e-21, 6.849865792284463e-23], [1.178965179953185e-09, 1.2514226950414543e-09, 6.641666727286221e-10, 2.349951357556269e-10, 6.235940024128116e-11, 1.32383839723259e-11, 2.34199935535833e-12, 3.551336126803584e-13, 4.7119952123809795e-14, 5.5573196713017e-15, 5.898864596275366e-16, 5.692182167484029e-17, 5.035012957283047e-18, 4.111121275420926e-19, 3.116989224115152e-20, 2.205703284871255e-21, 1.463289160353416e-22, 9.136593064392158e-24], [1.4742613322146994e-10, 1.5648673268100952e-10, 8.305209181736677e-11, 2.9385451563278686e-11, 7.797859855324257e-12, 1.6554210356056395e-12, 2.928601411123644e-13, 4.440841526508475e-14, 5.8922116253424146e-15, 6.949265034681965e-16, 7.376356932445087e-17, 7.117906625348327e-18, 6.296135828555285e-19, 5.140836414387502e-20, 3.8977034811370224e-21, 2.758167177892191e-22, 1.8298001193246587e-23, 1.142504129218577e-24], [1.73507811575792e-11, 1.841713537133848e-11, 9.774513095568641e-12, 3.4584135671872872e-12, 9.177406806427691e-13, 1.9482874226442512e-13, 3.4467106388695485e-14, 5.226486498576716e-15, 6.9346236119399e-16, 8.17868407642833e-17, 8.681334311521382e-18, 8.377160647018597e-19, 7.410007473745984e-20, 6.050319956432371e-21, 4.587259981698705e-22, 3.2461242829813164e-23, 2.1535165264641745e-24, 1.3446285732749048e-25]] |
| Legacy trial inputs | {"lambda_home": 2.0007530092086143, "lambda_away": 1.0614585708893847, "rho": -0.02181659734176786, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5891 |
| Legacy p draw | 0.2175 |
| Legacy p away | 0.1934 |
| Legacy p over 1 5 | 0.8121 |
| Legacy p under 3 5 | 0.6333 |
| Legacy p btts yes | 0.5678 |
| Legacy p over 2 5 | 0.5906 |
| Legacy goal margin distribution | {"-1": 0.12256742604842888, "-10": 2.834989761483074e-08, "-11": 2.6929081268836956e-09, "-12": 2.350377080099214e-10, "-13": 1.897179777759418e-11, "-14": 1.42412167272696e-12, "-15": 9.987089251572636e-14, "-16": 6.5320719389696405e-15, "-17": 3.6256152253232016e-16, "-2": 0.050733122570444295, "-3": 0.015461594753573275, "-4": 0.0037317567362366304, "-5": 0.0007421282482236468, "-6": 0.00012518483285121012, "-7": 1.8307803362166066e-05, "-8": 2.3610561715350543e-06, "-9": 2.721602407403315e-07, "0": 0.21747542392103889, "1": 0.23294660863111394, "10": 1.6049289122034634e-05, "11": 2.8735335596057746e-06, "12": 4.727403915811894e-07, "13": 7.192569790528681e-08, "14": 1.017684415940181e-08, "15": 1.3452264257297632e-09, "16": 1.6584326859280841e-10, "17": 1.73507811575792e-11, "2": 0.1802488301347398, "3": 0.10354415256748441, "4": 0.047105872021047886, "5": 0.017657577285804336, "6": 0.0056142829611263625, "7": 0.0015476375321667713, "8": 0.00037620950530382983, "9": 8.174073825934373e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.5891 |
| Legacy raw p draw | 0.2175 |
| Legacy raw p away | 0.1934 |
| Legacy market weight | 0 |
| Legacy lambda home | 2.0008 |
| Legacy lambda away | 1.0615 |
| Legacy model home team | Sociedad |
| Legacy model away team | Levante |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 10.488199856444206, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,493.2106 |
| Elo away rating | 1,446.2845 |
| Elo rating diff | 106.9261 |
| Elo home expectancy | 0.6492 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **47.4%**. Expected goals are 1.54 for Sevilla and 1.09 for CA Osasuna (2.63 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 48.8%; Under 3.5 goals: 73.1%; Double Chance 1X: 73.6%; Double Chance X2: 52.6%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 52.4%; BTTS No (at least one team does not score): 47.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 47.4% | 2.11 |
| Draw | 26.2% | 3.81 |
| CA Osasuna win | 26.4% | 3.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.54 |
| CA Osasuna expected goals | 1.09 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 48.8% |
| Under 2.5 | 51.2% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.50% |
| 2 | 1-0 | 10.76% |
| 3 | 2-1 | 9.32% |
| 4 | 2-0 | 8.59% |
| 5 | 0-0 | 7.63% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T20:00:00+00:00 |
| Fixture id | 85e464708d03287f24590e1478aeca31 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 0.00 |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5399 |
| Dc lambda away | 1.0852 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:38:12.675051+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.4% |
| P btts no | 47.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.10 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.87 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.71 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.93 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.16143632727475765, "-10": 5.2580505835729985e-08, "-11": 5.123097955016768e-09, "-12": 4.584266377908576e-10, "-13": 3.791461173766754e-11, "-14": 2.9007837781266634e-12, "-15": 1.8882501926345612e-13, "-2": 0.07196531001448996, "-3": 0.023057191802744428, "-4": 0.005795774001145516, "-5": 0.0011938810064518483, "-6": 0.00020789491958986687, "-7": 3.131580582407596e-05, "-8": 4.153300071764615e-06, "-9": 4.917962422003225e-07, "0": 0.26231023418896693, "1": 0.23071325831835185, "10": 1.7400827999520462e-06, "11": 2.405760165831726e-07, "12": 3.054668106664558e-08, "13": 3.584885703892943e-09, "14": 3.8918722326221143e-10, "15": 3.594820993617798e-11, "2": 0.14490128320651105, "3": 0.06587641527504749, "4": 0.023496842409397495, "5": 0.006868052720532923, "6": 0.0016970356630844137, "7": 0.00036273143968678213, "8": 6.826363855510909e-05, "9": 1.1469799995262971e-05} |
| Raw goal margin distribution | {"-1": 0.16143632727475765, "-10": 5.2580505835729985e-08, "-11": 5.123097955016768e-09, "-12": 4.584266377908576e-10, "-13": 3.791461173766754e-11, "-14": 2.9007837781266634e-12, "-15": 1.8882501926345612e-13, "-2": 0.07196531001448996, "-3": 0.023057191802744428, "-4": 0.005795774001145516, "-5": 0.0011938810064518483, "-6": 0.00020789491958986687, "-7": 3.131580582407596e-05, "-8": 4.153300071764615e-06, "-9": 4.917962422003225e-07, "0": 0.26231023418896693, "1": 0.23071325831835185, "10": 1.7400827999520462e-06, "11": 2.405760165831726e-07, "12": 3.054668106664558e-08, "13": 3.584885703892943e-09, "14": 3.8918722326221143e-10, "15": 3.594820993617798e-11, "2": 0.14490128320651105, "3": 0.06587641527504749, "4": 0.023496842409397495, "5": 0.006868052720532923, "6": 0.0016970356630844137, "7": 0.00036273143968678213, "8": 6.826363855510909e-05, "9": 1.1469799995262971e-05} |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 26.4% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 73.1% |
| Raw p btts yes | 52.4% |
| P home draw | 73.6% |
| P draw away | 52.6% |
| P home away | 73.8% |
| Raw p home draw | 73.6% |
| Raw p draw away | 52.6% |
| Raw p home away | 73.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4878 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.75, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:35Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.44, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:38:35Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.35, "price": 3.44, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / unavailable reference |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.08788596359393058, 0.08073728685886591, 0.04086276051682056, 0.013341423266001778, 0.0032669153866148786, 0.000639975866472874, 0.00010447396121373435, 1.4618598441635588e-05, 1.78982868722206e-06, 1.947891086150225e-07, 1.9079209868142384e-08, 1.6988827827967229e-09, 1.3866852115439072e-10, 1.0447929818998585e-11, 7.3096726110473e-13, 4.7731203181801156e-14], [0.12366760396810295, 0.1264752694574884, 0.06061755009663187, 0.019791232480593998, 0.004846280686985593, 0.0009493673128271877, 0.00015498110009137169, 2.1685848243503317e-05, 2.6551077005042694e-06, 2.8895841593690064e-07, 2.8302908206855077e-08, 2.52019469296732e-09, 2.0570675895579875e-10, 1.5498901718804352e-11, 1.0843478024636743e-12, 7.080648892661918e-14], [0.09372978648229574, 0.09180648137397869, 0.04496132093431531, 0.014679576357459466, 0.003594589041589135, 0.0007041658458404677, 0.00011495276481568961, 1.608485300139483e-05, 1.969349623124697e-06, 2.143265779448292e-07, 2.0992866541691273e-08, 1.8692817876477973e-09, 1.5257706048868193e-10, 1.1495863709399453e-11, 8.042837342200297e-13, 5.251867269110663e-14], [0.0463475787063578, 0.045396541280268043, 0.02223250941832244, 0.007258768489052867, 0.0017774552228765846, 0.0003481964825406345, 5.6841933762592706e-05, 7.953650791716632e-06, 9.738055540684332e-07, 1.0598037521443204e-07, 1.0380569196078152e-08, 9.243239318989802e-10, 7.544642514596599e-11, 5.684483749139799e-12, 3.9770285490885245e-13, 2.5969474672432746e-14], [0.01718849044066511, 0.01683578813855292, 0.008245161587187968, 0.002691991173380783, 0.0006591880948234619, 0.00012913235337581755, 2.1080433161295198e-05, 2.949695634975129e-06, 3.611461035153442e-07, 3.9303944609764045e-08, 3.849744029259852e-09, 3.4279531986304576e-10, 2.798010583508433e-11, 2.1081510039876675e-12, 1.4749231590146276e-13, 9.631054730696702e-15], [0.00509962698160641, 0.0049949842741775635, 0.002446244400744564, 0.00079868275049567, 0.000195573509257243, 3.831208073489035e-05, 6.254321524300867e-06, 8.751406936852423e-07, 1.0714788597326094e-07, 1.1661027308210823e-08, 1.1421746773902298e-09, 1.0170341999354447e-10, 8.301374873922766e-12, 6.254641021762786e-13, 4.375926998052372e-14, 2.8574229212003127e-15], [0.0012608337849340616, 0.0012349618807047649, 0.0006048104298195063, 0.00019746663803080553, 4.8353671513435016e-05, 9.472293941478591e-06, 1.5463209187890065e-06, 2.1637013004064958e-07, 2.649128556002619e-08, 2.8830769878387263e-09, 2.823917174224628e-10, 2.5145193645282206e-11, 2.0524351957890668e-12, 1.5463999114674203e-13, 1.0819059157561234e-14, 7.064703692816867e-16], [0.0002671963216634644, 0.0002617135389786246, 0.00012817163061657838, 4.1847196643641137e-05, 1.024712640293737e-05, 2.0073717321990714e-06, 3.276968515190121e-07, 4.5853231056725305e-08, 5.614042185699861e-09, 6.109826492818605e-10, 5.984454815942022e-11, 5.3287779323634615e-12, 4.3495276008657334e-13, 3.2771359167410847e-14, 2.292778671782628e-15, 1.4971543933220985e-16], [4.9546292911989026e-05, 4.85296188979732e-05, 2.3766903354061367e-05, 7.759738044084587e-06, 1.9001276780507926e-06, 3.722275337010432e-07, 6.076492404767124e-08, 8.50257818952704e-09, 1.0410135020619276e-09, 1.1329469326898075e-10, 1.109699225585448e-11, 9.881168672387629e-13, 8.065341887928457e-14, 6.076802817957931e-15, 4.251506268771976e-16, 2.776177817276848e-17], [8.166563325382231e-06, 7.998988069419506e-06, 3.917425701938144e-06, 1.2790137949969675e-06, 3.1319221070035753e-07, 6.135312142969335e-08, 1.0015695847898045e-08, 1.4014538552284769e-09, 1.71587059041293e-10, 1.8674016412376315e-11, 1.829083159454356e-12, 1.6286826914614702e-13, 1.3293855382001259e-14, 1.0016207492429e-15, 7.007627237392046e-17, 4.57588865176768e-18], [1.2114626012354173e-06, 1.1866037778353314e-06, 5.811275247528114e-07, 1.8973432487655224e-07, 4.6460259370359743e-08, 9.10138195464858e-09, 1.4857707534533107e-09, 2.0789760212715053e-10, 2.5453951264716443e-11, 2.7701827068599184e-12, 2.7133394476246924e-13, 2.4160569034620988e-14, 1.972066826625986e-15, 1.4858466529706087e-16, 1.0395411121240259e-17, 6.788067083009656e-19], [1.6337590419466963e-07, 1.6002348312441702e-07, 7.836992632878742e-08, 2.5587266872176632e-08, 6.265556093940349e-09, 1.2273977791352476e-09, 2.0036866183396111e-10, 2.8036737322959717e-11, 3.4326790599720635e-12, 3.735823987105722e-13, 3.6591660790080506e-14, 3.258255605962276e-15, 2.659497706357376e-16, 2.003788975211824e-17, 1.401908477963752e-18, 9.15427844235423e-20], [2.0196561473590578e-08, 1.9782134520212925e-08, 9.68810573739283e-09, 3.163102973308249e-09, 7.745492791073714e-10, 1.5173115534415734e-10, 2.4769613463248455e-11, 3.465906993159533e-12, 4.2434846188349263e-13, 4.618232975175581e-14, 4.5234683181128905e-15, 4.027862001245789e-16, 3.287676305761639e-17, 2.4770878800919928e-18, 1.7330420232475446e-19, 1.131653705108641e-20], [2.3046488396034282e-09, 2.2573581857735117e-09, 1.1055189604841307e-09, 3.6094468885277075e-10, 8.838455494736864e-11, 1.7314186454603045e-11, 2.826484151777361e-12, 3.9549794356843346e-13, 4.8422806602307484e-14, 5.269909574050125e-15, 5.161772722526896e-16, 4.596231640416727e-17, 3.751598703062897e-18, 2.826628540662572e-19, 1.9775907364647854e-20, 1.2913408065634864e-21], [2.442009803458001e-10, 2.3919005467764204e-10, 1.171409757972279e-10, 3.8245760201638185e-11, 9.365242372147529e-12, 1.8346141214431577e-12, 2.994947381722024e-13, 4.1907028908047665e-14, 5.1308887671639104e-15, 5.584005086597941e-16, 5.469423096059091e-17, 4.870174810142821e-18, 3.9752003229682348e-19, 2.995100376428696e-20, 2.0954584849055503e-21, 1.368306899968339e-22], [2.4150538652692933e-11, 2.3654977357798636e-11, 1.1584792410739292e-11, 3.782358730678919e-12, 9.261864861480538e-13, 1.8143628739716188e-13, 2.9618878844236054e-14, 4.144444137898939e-15, 5.074251844468123e-16, 5.5223664741130043e-17, 5.409049288101201e-18, 4.816415758494251e-19, 3.9313203786527263e-20, 2.9620391903099253e-21, 2.0723279269052786e-22, 1.3532029490478718e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4834423648808441, "lambda_away": 0.9794803212457937, "rho": -0.02181659734176786, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4859 |
| Legacy p draw | 0.2673 |
| Legacy p away | 0.2468 |
| Legacy p over 1 5 | 0.7077 |
| Legacy p under 3 5 | 0.7655 |
| Legacy p btts yes | 0.4855 |
| Legacy p over 2 5 | 0.4466 |
| Legacy goal margin distribution | {"-1": 0.15794747731005437, "-10": 2.175781645508635e-08, "-11": 1.9164927393715608e-09, "-12": 1.5499767608208753e-10, "-13": 1.1584796294153365e-11, "-14": 8.017737500313491e-13, "-15": 4.7731203181801156e-14, "-2": 0.06461876120892937, "-3": 0.018951771520034473, "-4": 0.004339562209982457, "-5": 0.00081205609682529, "-6": 0.0001282390929886623, "-7": 1.749876454293603e-05, "-8": 2.1007329101712627e-06, "-9": 2.2503889765141567e-07, "0": 0.2672804158844575, "1": 0.2406039681108075, "10": 1.3815446814647392e-06, "11": 1.843027296220545e-07, "12": 2.2574842993891997e-08, "13": 2.5554236866918098e-09, "14": 2.678559577035987e-10, "15": 2.4150538652692933e-11, "2": 0.14822059533570306, "3": 0.06583770746469556, "4": 0.022832095336342464, "5": 0.006470842728448049, "6": 0.0015476409538891915, "7": 0.00031983952074440017, "8": 5.815278794013826e-05, "9": 9.434790381307606e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.4859 |
| Legacy raw p draw | 0.2673 |
| Legacy raw p away | 0.2468 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.4834 |
| Legacy lambda away | 0.9795 |
| Legacy model home team | Sevilla |
| Legacy model away team | Osasuna |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 95/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 8.559671036495459, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,440.7731 |
| Elo away rating | 1,423.7802 |
| Elo rating diff | 76.9929 |
| Elo home expectancy | 0.6090 |
| Market p home draw | 79.7% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-26T11:38:35Z |
| Market reference home draw last update utc | 2026-10-26T11:38:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.4% |
| Market draw away odds | 2.01 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-26T11:38:35Z |
| Market reference draw away last update utc | 2026-10-26T11:38:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-26T11:38:35Z |
| Market reference home away last update utc | 2026-10-26T11:38:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.01 |
| Market reference dc home draw odds | 1.22 |
| Market reference dc home away odds | 1.35 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:38:35Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.6, "price": 1.47, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:38:35Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.47, "price": 2.6, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:38:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.97, "price": 1.86, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:38:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.86, "price": 1.97, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:38:35Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.34, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:38:35Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.34, "price": 1.57, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 68.6% |
| Market over 1 5 odds | 1.42 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-26T11:38:23Z |
| Market reference over 1 5 odds | 1.43 |
| Market reference over 1 5 opposite odds | 3.00 |
| Market reference over 1 5 last update utc | 2026-10-26T11:38:25Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.9% |
| Market reference under 3 5 odds | 1.25 |
| Market reference under 3 5 opposite odds | 4.35 |
| Market reference under 3 5 last update utc | 2026-10-26T11:38:25Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 45.5% |
| Market btts yes odds | 2.11 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-26T11:38:35Z |
| Market reference btts yes odds | 2.11 |
| Market reference btts yes opposite odds | 1.78 |
| Market reference btts yes last update utc | 2026-10-26T11:38:35Z |
| Market btts yes bookmakers | 1 |

</details>


---
