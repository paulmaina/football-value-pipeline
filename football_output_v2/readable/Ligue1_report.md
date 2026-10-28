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
| Training sha256 | 75605fc70c5fab48a94dc33df8eaa78843d715720f70cba1d0b7be434d2a1503 |
| Training as of utc | 2026-10-28T12:07:18.629492+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 107, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-28T12:07:18.629492+00:00', 'observations': 330, 'observations_sha256': '7b9358c16fd1f008b4d972df06d71636243c316fd61918804a341803691724cf', 'eligible_training_matches': 144, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 143, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 15, 'retrospective_eligible_training_matches': 144, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'f700d16b6d25e158300163ac33592d057e48dfa5c8b457b44d350c75afe24e31', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 83, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-08-24T00:00:00+00:00', 'audit_origin_utc': '2025-09-27T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 28, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1750, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1453, 'tuning_matches': 196, 'audit_matches': 97, 'audit_matchdays': 32, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8794253162835202, 'audit_candidate_poisson_score': 0.8748028465307758, 'audit_gain': 0.004622469752744385, 'audit_gain_lower95': -0.0027888357450894592, 'audit_baseline_briers': [0.6035182490481663, 0.16831698204661508, 0.2150009196653262, 0.24570077103413518], 'audit_candidate_briers': [0.6021999125630176, 0.16740770566387364, 0.21307232465179426, 0.24370844486088672], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1586.078 |
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
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261028T120718629492Z_046e870c819c72e369ecec59eb9ab1f638f712c3743f4316c64bc372d9b093a2.json |
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

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **76.6%**. Expected goals are 0.80 for Le Havre and 2.26 for Paris Saint Germain (3.06 combined). The most likely exact score is 0-2 at 13.1%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 61.2%; Under 3.5 goals: 62.3%; Double Chance 1X: 23.4%; Double Chance X2: 90.8%; Double Chance 12 (either team wins): 85.8%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 9.2% | 10.92 |
| Draw | 14.2% | 7.03 |
| Paris Saint Germain win | 76.6% | 1.31 |

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
| Over 3.5 | 37.7% |
| Under 3.5 | 62.3% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 13.13% |
| 2 | 0-1 | 11.09% |
| 3 | 1-2 | 10.47% |
| 4 | 0-3 | 9.90% |
| 5 | 1-3 | 7.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 9.2% | 8.3% | 10.24 | -6.2% |
| Draw | 14.2% | 12.3% | 7.10 | +1.0% |
| Paris Saint Germain win | 76.6% | 79.4% | 1.24 | -5.0% |

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
| Market best home last update utc | 2026-10-28T12:07:28Z |
| Market best draw last update utc | 2026-10-28T12:07:28Z |
| Market best away last update utc | 2026-10-28T12:07:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-28T12:07:18.629492+00:00 |
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
| Fair Under 0.5 odds | 25.55 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.66 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.65 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.25222724180917616, "-10": 5.8369882353404544e-05, "-11": 1.1842946262992577e-05, "-12": 2.2071190187085157e-06, "-13": 3.8030059777825454e-07, "-14": 6.092581128459971e-08, "-15": 9.117882729266985e-09, "-16": 1.2745058172028465e-09, "-17": 1.5331724735619624e-10, "-2": 0.23034359532053333, "-3": 0.152550904590038, "-4": 0.07948987645276567, "-5": 0.033998759118664866, "-6": 0.012305167664386406, "-7": 0.003855126908637182, "-8": 0.0010638981182268805, "-9": 0.00026222091988759987, "0": 0.14224511063923181, "1": 0.06406484656015259, "10": 1.295245482612815e-09, "11": 9.263879628577011e-11, "12": 6.085955522566421e-12, "13": 3.696578263444278e-13, "14": 2.0875846493204536e-14, "15": 1.1013025689613819e-15, "16": 5.426556742233622e-17, "17": 2.301141984370725e-18, "2": 0.021437809069761143, "3": 0.005004825283591387, "4": 0.0009192969772930536, "5": 0.00013860437952559874, "6": 1.7683625072615663e-05, "7": 1.9529553696354814e-06, "8": 1.8998685619409733e-07, "9": 1.6506717872938304e-08} |
| Raw goal margin distribution | {"-1": 0.2305792301329018, "-10": 5.336014634842043e-05, "-11": 1.0826496821830642e-05, "-12": 2.0176877029425633e-06, "-13": 3.4766038127290844e-07, "-14": 5.569670651139944e-08, "-15": 8.335318441721058e-09, "-16": 1.1651182799392841e-09, "-17": 1.4015842463294654e-10, "-2": 0.21057380041143914, "-3": 0.1394578550839508, "-4": 0.07266746598967638, "-5": 0.031080733575109484, "-6": 0.01124904695606623, "-7": 0.003524251338920425, "-8": 0.0009725864949440699, "-9": 0.0002397151766745618, "0": 0.1878022604337699, "1": 0.07819580945451025, "10": 1.5809414116072088e-09, "11": 1.1307239541509983e-10, "12": 7.42835180201975e-12, "13": 4.5119428991462293e-13, "14": 2.5480490506623013e-14, "15": 1.3442199655220989e-15, "16": 6.623507583232362e-17, "17": 2.8087113260885685e-18, "2": 0.026166406744878995, "3": 0.006108753633888285, "4": 0.0011220688900116151, "5": 0.0001691767362740489, "6": 2.1584151853776975e-05, "7": 2.3837242131500555e-06, "8": 2.318927899384903e-07, "9": 2.0147650932086586e-08} |
| Unadjusted home-win probability | 11.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 70.0% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 49.7% |
| P home draw | 23.4% |
| P draw away | 90.8% |
| P home away | 85.8% |
| Raw p home draw | 30.0% |
| Raw p draw away | 88.8% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6120 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:07:28Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:07:05Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.33, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:07:05Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.71, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:07:28Z", "line": 2.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.24 |
| Reference draw odds | 7.10 |
| Reference away odds | 1.24 |
| Market reference 1x2 last update utc | 2026-10-28T12:07:28Z |
| Market reference home last update utc | 2026-10-28T12:07:28Z |
| Market reference draw last update utc | 2026-10-28T12:07:28Z |
| Market reference away last update utc | 2026-10-28T12:07:28Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.42 |
| Market reference over 2 5 last update utc | 2026-10-28T12:07:05Z |
| Market reference under 2 5 last update utc | 2026-10-28T12:07:05Z |
| Home probability edge | +0.9% |
| Draw probability edge | +2.0% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -12.7% |
| Under 2.5 probability edge | +12.7% |
| Raw edge prob home | 0.0289 |
| Raw ev home | 0.1447 |
| Raw edge prob draw | 0.0651 |
| Raw ev draw | 0.3334 |
| Raw edge prob away | -0.0939 |
| Raw ev away | -0.1315 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.039397209590091485, 0.09935151987146017, 0.12214048232260934, 0.09496940676786168, 0.05538205710137049, 0.025837139375013262, 0.01004473599728597, 0.0033472321636597887, 0.0009759806295961983, 0.0002529554483687558, 5.900507779270239e-05, 1.251244125029922e-05, 2.4322384768794138e-06, 4.3642352366231143e-07, 7.271524387375257e-08, 1.1307837405505898e-08, 1.6485606212522644e-09, 2.2620455692254358e-10, 2.931393994113996e-11], [0.02619660040759011, 0.0725613564384318, 0.101713524158258, 0.07908658018939423, 0.046119878485787934, 0.0215160972842681, 0.008364839225251258, 0.0027874360168519334, 0.0008127561596180867, 0.0002106507983213994, 4.913697974170333e-05, 1.0419841736252158e-05, 2.025467251908211e-06, 3.6343539646430207e-07, 6.055423700465823e-08, 9.416697652172874e-09, 1.3728528608000735e-09, 1.883737662381097e-10, 2.441143248887382e-11], [0.012738013756971676, 0.029713038303841654, 0.033193215634143375, 0.03293001072093731, 0.019203360283733557, 0.00895885638937634, 0.003482945459353421, 0.001160630510246419, 0.0003384147978789527, 8.771062082196247e-05, 2.0459618633323583e-05, 4.338605857827544e-06, 8.433625295279782e-07, 1.5132695677670112e-07, 2.5213527617280675e-08, 3.92091747929015e-09, 5.716274406625363e-10, 7.843492697381994e-11, 1.0164413882190516e-11], [0.0035358963857585507, 0.00824792834683172, 0.009619671307177769, 0.0071642583470940295, 0.005330587132119375, 0.0024868545859740615, 0.0009668174722123829, 0.0003221749720701405, 9.393926584923692e-05, 2.4347254844757455e-05, 5.6793070693594496e-06, 1.204336960582025e-06, 2.3410577009387023e-07, 4.2006269560018634e-08, 6.998926431946417e-09, 1.0883924455091477e-09, 1.5867586893858047e-10, 2.1772450563744705e-11, 2.8215006668304856e-12], [0.0007361369375961915, 0.0017171330979052393, 0.0020027157484787646, 0.0015571964588719758, 0.0008697925354435911, 0.0005177373201712925, 0.00020128136561791036, 6.707348616466124e-05, 1.955718039725778e-05, 5.0688458215239294e-06, 1.1823728010089233e-06, 2.507304584963299e-07, 4.8738392155552143e-08, 8.74526944802386e-09, 1.4571038593849487e-09, 2.265920135462488e-10, 3.303466942677474e-11, 4.532798287447879e-12, 5.874071617798914e-13], [0.00012260485755772427, 0.00028599143464230216, 0.00033355571026316667, 0.0002593537156997282, 0.000151243887702115, 6.758340801779789e-05, 3.352375339456922e-05, 1.1171203069868647e-05, 3.257281620273516e-06, 8.442248828857333e-07, 1.969261987059084e-07, 4.175958382105844e-08, 8.117462013707396e-09, 1.4565394836456993e-09, 2.426831232108331e-10, 3.7739284806538544e-11, 5.501980314643539e-12, 7.549452554102059e-13, 9.78336607229411e-14], [1.701670609664435e-05, 3.9693632751658647e-05, 4.629522517681166e-05, 3.599650163173231e-05, 2.0991605367096068e-05, 9.793118240122508e-06, 3.646716548595889e-06, 1.5504857080918284e-06, 4.520881562959238e-07, 1.171725737275688e-07, 2.7331994122093477e-08, 5.7959413579235165e-09, 1.1266475740808118e-09, 2.0215760456054997e-10, 3.368273871490095e-11, 5.237951665561578e-12, 7.636368071283923e-13, 1.0478117903544856e-13, 1.3578635333410749e-14], [2.0244009354074e-06, 4.722172835083608e-06, 5.507534573410485e-06, 4.282341785819698e-06, 2.497276811358472e-06, 1.1650432000919821e-06, 4.529352572860503e-07, 1.4456739264871338e-07, 5.3782893192975316e-08, 1.393949372522564e-08, 3.2515643246742505e-09, 6.895170569385681e-10, 1.3403219106507567e-10, 2.404978034220144e-11, 4.007083825404665e-12, 6.231355346421968e-13, 9.084643396215713e-14, 1.2465345269980403e-14, 1.6153891307985495e-15], [2.107296343665301e-07, 4.915536925260663e-07, 5.733057748672945e-07, 4.457695622318471e-07, 2.5995355967550966e-07, 1.2127495264528128e-07, 4.714821036199109e-08, 1.571131448604476e-08, 4.387880534954388e-09, 1.4510289758289365e-09, 3.384709764125679e-10, 7.177514827067061e-11, 1.3952055703236588e-11, 2.5034573584049273e-12, 4.171166366476849e-13, 6.486517620064048e-14, 9.456642445433302e-15, 1.2975777698239865e-15, 1.681536275443083e-16], [1.9498543670018736e-08, 4.5482834764509834e-08, 5.3047250431234815e-08, 4.1246487719068143e-08, 2.4053170550723463e-08, 1.1221416329705598e-08, 4.362563630265225e-09, 1.4537478439634137e-09, 4.238814837612613e-10, 1.0522869791990022e-10, 3.1318286744308774e-11, 6.641262711743322e-12, 1.290965877836217e-12, 2.3164170893963853e-13, 3.8595269144822285e-14, 6.001891829849494e-15, 8.750110360525567e-16, 1.2006321221130076e-16, 1.5559040188158367e-17], [1.6237577868678364e-09, 3.787621699729999e-09, 4.4175548398565586e-09, 3.434836301019046e-09, 2.0030482092183773e-09, 9.344729767209254e-10, 3.632961920249282e-10, 1.2106208657047123e-10, 3.529909062002163e-11, 9.148846835711518e-12, 2.0440834270540343e-12, 5.530567936419562e-13, 1.0750628006851628e-13, 1.9290160076542245e-14, 3.2140538222106564e-15, 4.998126403481905e-16, 7.286728729234715e-17, 9.998365982800486e-18, 1.2956922880634542e-18], [1.2292709907113262e-10, 2.8674310398523634e-10, 3.3443239246827903e-10, 2.6003537330710155e-10, 1.5164140098370698e-10, 7.074457355505771e-11, 2.7503453624914637e-11, 9.165043721399336e-12, 2.6723288687892654e-12, 6.926163559957521e-13, 1.6156158022914227e-13, 3.281539734662862e-14, 8.138797083919439e-15, 1.460367696466125e-15, 2.4332096561332767e-16, 3.7838474712169165e-17, 5.516441132091158e-18, 7.569294728913874e-19, 9.809079626815222e-20], [8.530715494782472e-12, 1.9898979628352016e-11, 2.32084513011687e-11, 1.8045555496097806e-11, 1.0523388730369984e-11, 4.909428713100021e-12, 1.908644552510945e-12, 6.360223341743241e-13, 1.8545038043193014e-13, 4.806517948181412e-14, 1.1211814858046558e-14, 2.3775441024482444e-15, 4.426694956001132e-16, 1.0134446700897468e-16, 1.688563341401173e-17, 2.625859269153111e-18, 3.8282193427792746e-19, 5.2528287347898905e-20, 6.807161984161571e-21], [5.464635223977094e-13, 1.2746957164941514e-12, 1.4866949970596509e-12, 1.1559684326657296e-12, 6.741108734285571e-13, 3.144898817879871e-13, 1.2226461259999229e-13, 4.074253856773085e-14, 1.1879644583483076e-14, 3.0789758843059406e-15, 7.182103123174577e-16, 1.5230154207749694e-16, 2.9605227574602895e-17, 5.0881196055974e-18, 1.0816657429240172e-18, 1.6820820087362123e-19, 2.4522939814904124e-20, 3.3648751909740966e-21, 4.3605553574865365e-22], [3.2505152866396725e-14, 7.582240611593506e-14, 8.843270623644789e-14, 6.876018082169811e-14, 4.009796828441942e-14, 1.870672288902336e-14, 7.272635335796724e-15, 2.4234782195495123e-15, 7.066339240545764e-16, 1.8314595153978965e-16, 4.272112416519343e-17, 9.059314490554444e-18, 1.7610003385670898e-18, 3.15981339919439e-19, 5.042729363961881e-20, 1.000548629264105e-20, 1.4586918883796416e-21, 2.001520284081406e-22, 2.5937782243098764e-23], [1.8045961439775606e-15, 4.209450183677442e-15, 4.909539153122114e-15, 3.817374976824445e-15, 2.2261282463373063e-15, 1.0385454924867267e-15, 4.037565901467044e-16, 1.345448048802687e-16, 3.9230360176859516e-17, 1.016775645671476e-17, 2.3717586024520284e-18, 5.029480730003055e-19, 9.776586603309291e-20, 1.7542409658284207e-20, 2.9228502298203834e-21, 4.353590364500677e-22, 8.09825373792512e-23, 1.1111886787894897e-23, 1.4399938991708043e-24], [9.392454798562743e-17, 2.1909096231274907e-16, 2.5552877706939653e-16, 1.9868446487954995e-16, 1.1586420041572963e-16, 5.4053598789879474e-17, 2.101448313092428e-17, 7.002708070926041e-18, 2.0418384796076054e-18, 5.292053473637223e-19, 1.2344388267134645e-19, 2.6177142500523623e-20, 5.088459712288868e-21, 9.130369158948716e-22, 1.5212677228738466e-22, 2.365700387441184e-23, 3.303482560548133e-24, 5.783448819302539e-25, 7.494794695923984e-26], [4.600968539005364e-18, 1.0732344700084369e-17, 1.2517279979741973e-17, 9.732716224940572e-18, 5.675699828668416e-18, 2.647858443676624e-18, 1.0294111371569958e-18, 3.430332135013301e-19, 1.0002107870503349e-19, 2.5923544016059345e-20, 6.0469965806004736e-21, 1.2823081044201503e-21, 2.4926223815120096e-22, 4.4725838080430413e-23, 7.452050696499437e-24, 1.1588571133709647e-24, 1.68948856819539e-25, 2.220437719355535e-26, 3.67138467438004e-27], [2.1286086850542139e-19, 4.965250674053461e-19, 5.791039571831974e-19, 4.502778949680712e-19, 2.6258262465050564e-19, 1.2250147837834683e-19, 4.762504825815679e-20, 1.587021235487167e-20, 4.62741127254157e-21, 1.1993361935028176e-21, 2.7976043154474397e-22, 5.932516479615415e-23, 1.1531958118961604e-23, 2.069212309913204e-24, 3.4476436210237944e-25, 5.361378360547437e-26, 7.81631086818506e-27, 1.0725023477532822e-27, 1.331245051903211e-28]] |
| Legacy trial inputs | {"lambda_home": 0.8327584943508111, "lambda_away": 2.3326272738227596, "rho": -0.061598984997362036, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0974 |
| Legacy p draw | 0.1533 |
| Legacy p away | 0.7493 |
| Legacy p over 1 5 | 0.8351 |
| Legacy p under 3 5 | 0.6023 |
| Legacy p btts yes | 0.5049 |
| Legacy p over 2 5 | 0.6276 |
| Legacy goal margin distribution | {"-1": 0.23987850870785057, "-10": 7.031178394745704e-05, "-11": 1.4696466585806507e-05, "-12": 2.822009596599823e-06, "-13": 5.010619846471467e-07, "-14": 8.27259288243135e-08, "-15": 1.2761946693946623e-08, "-16": 1.8470988013725646e-09, "-17": 2.506159894114174e-10, "-18": 2.931393994113996e-11, "-2": 0.2231301963232702, "-3": 0.15108541038024695, "-4": 0.08072370425804044, "-5": 0.03546182008089651, "-6": 0.01319615935036699, "-7": 0.004253637305320147, "-8": 0.0012083456127585947, "-9": 0.000306674133021063, "0": 0.1532572117323499, "1": 0.06724801256318982, "10": 1.9349064684628276e-09, "11": 1.4438381510449246e-10, "12": 9.897779852173804e-12, "13": 6.273999503329532e-13, "14": 3.698012712599315e-14, "15": 2.03665466416502e-15, "16": 1.05235996642895e-16, "17": 5.09749360641071e-18, "18": 2.1286086850542139e-19, "2": 0.023270216854510355, "3": 0.005625204733669531, "4": 0.0010729774868269385, "5": 0.00016827681024009385, "6": 2.2355506937201108e-05, "7": 2.5725933902232733e-06, "8": 2.60900904632064e-07, "9": 2.3639336546169947e-08} |
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
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.295393234483514, "version": "count-markets-nb2-v1"}} |
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
| Market best home last update utc | 2026-10-28T12:07:28Z |
| Market best draw last update utc | 2026-10-28T12:07:28Z |
| Market best away last update utc | 2026-10-28T12:07:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
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
| Bbs statistics cutoff utc | 2026-10-28T12:07:18.629492+00:00 |
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
| Goal margin distribution | {"-1": 0.20457408270666838, "-10": 7.641522046594511e-08, "-11": 7.489192742827718e-09, "-12": 6.737954190412871e-10, "-13": 5.580199014719032e-11, "-14": 3.948349272749536e-12, "-2": 0.09577966018965328, "-3": 0.03135989618413524, "-4": 0.008005922839333577, "-5": 0.0016690612026097286, "-6": 0.0002935159107547469, "-7": 4.4587769987002806e-05, "-8": 5.957836410483047e-06, "-9": 7.102674944864066e-07, "0": 0.2765733173947321, "1": 0.20730293566745364, "10": 3.32368864012411e-07, "11": 3.832320780945863e-08, "12": 4.056404767098946e-09, "13": 3.952294541645645e-10, "14": 3.290042909331042e-11, "2": 0.11350700949467418, "3": 0.043723044024100495, "4": 0.013132081156519058, "5": 0.003220926422262656, "6": 0.0006663870891462, "7": 0.00011909596896912196, "8": 1.8722173622864497e-05, "9": 2.6258869073717206e-06} |
| Raw goal margin distribution | {"-1": 0.1839987441792342, "-10": 6.87296475481393e-08, "-11": 6.73595619427708e-09, "-12": 6.060274561518367e-10, "-13": 5.0189623113242653e-11, "-14": 3.55123825146804e-12, "-2": 0.0861464803343612, "-3": 0.028205828612931888, "-4": 0.007200715403159963, "-5": 0.0015011929232444355, "-6": 0.0002639951173723982, "-7": 4.010328959961477e-05, "-8": 5.3586182719247445e-06, "-9": 6.388312990957873e-07, "0": 0.2916759416857244, "1": 0.21776750581099494, "10": 3.4914671271864664e-07, "11": 4.0257748171641024e-08, "12": 4.261170474247426e-09, "13": 4.151804805819293e-10, "14": 3.456122973219692e-11, "2": 0.11923679840873977, "3": 0.045930165981183206, "4": 0.013794983415720621, "5": 0.0033835175132398824, "6": 0.0007000260456552736, "7": 0.00012510788634538934, "8": 1.966726153725038e-05, "9": 2.7584406391494436e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:07:05Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:07:28Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:07:05Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:07:28Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.60 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.72 |
| Market reference 1x2 last update utc | 2026-10-28T12:07:28Z |
| Market reference home last update utc | 2026-10-28T12:07:28Z |
| Market reference draw last update utc | 2026-10-28T12:07:28Z |
| Market reference away last update utc | 2026-10-28T12:07:28Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-28T12:07:05Z |
| Market reference under 2 5 last update utc | 2026-10-28T12:07:05Z |
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
| Raw ev away | -0.1640 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09753298727663932, 0.10210347225775436, 0.06206060817025649, 0.023217794436536727, 0.006514591071421758, 0.0014623231140702133, 0.00027353838822474216, 4.3857758606926046e-05, 6.15293936325912e-06, 7.673019731760237e-07, 8.611771625767642e-08, 8.786704242683446e-09, 8.218091108678649e-10, 7.09502269007404e-11, 5.687899867938593e-12], [0.10725126573455954, 0.13330369044461973, 0.07732224867459551, 0.028927400617352245, 0.00811662736942352, 0.001821930445131161, 0.00034080560761404714, 5.464304358751666e-05, 7.66604004621476e-06, 9.559931126627101e-07, 1.0729536284105664e-07, 1.094748747255283e-08, 1.0239043784303067e-09, 8.839795886124255e-11, 7.086640318096792e-12], [0.07177518320680962, 0.0805564833381288, 0.043897149976983615, 0.01802054257918589, 0.00505631428986204, 0.00113498532402205, 0.00021230742590643445, 3.404029648742373e-05, 4.7756175155153626e-06, 5.95543126049591e-07, 6.68404562235927e-08, 6.81981996045311e-09, 6.378489617020791e-10, 5.506817576331376e-11, 4.41467608116279e-12], [0.029808594792562922, 0.033455512928768236, 0.01877430575167922, 0.006820378125957985, 0.0020999127703521274, 0.0004713651168509899, 8.817234241063642e-05, 1.4137106438149066e-05, 1.98333798736661e-06, 2.473320573039547e-07, 2.7759177842545523e-08, 2.832305550145811e-09, 2.6490188375346953e-10, 2.287009052369117e-11, 1.833437193251445e-12], [0.00928474457125706, 0.01042068216249834, 0.005847797744914644, 0.002187747912095753, 0.0005960780202258692, 0.0001468202288708387, 2.7463813146147568e-05, 4.4034085862925775e-06, 6.177676854383094e-07, 7.703868606794159e-08, 8.64639469152158e-09, 8.822030613606305e-10, 8.251131407608113e-11, 7.123547765726197e-12, 5.710767698123521e-13], [0.002313600687409675, 0.0025966570463413123, 0.001457171899413439, 0.0005451496306072887, 0.00015296142473181698, 3.3340932095865406e-05, 6.843515886319657e-06, 1.0972546475570796e-06, 1.539372171975699e-07, 1.9196732411540795e-08, 2.1545347368895164e-09, 2.198300226284561e-10, 2.056041838312534e-11, 1.7750671417068847e-12, 1.4230263385939025e-13], [0.00048042500430878015, 0.0005392023694778802, 0.0003025854115033694, 0.00011320169252139429, 3.176282473279188e-05, 7.129766437478909e-06, 1.2950599531229305e-06, 2.2784768851821115e-07, 3.19654504936308e-08, 3.986249788789036e-09, 4.47394559435604e-10, 4.5648257343283845e-11, 4.269422612145964e-12, 3.6859715846544397e-13, 2.9549499988086155e-14], [8.550982372113877e-05, 9.597148181413094e-05, 5.385653320744214e-05, 2.0148528252325337e-05, 5.653397553056591e-06, 1.2690119493652905e-06, 2.373781005903272e-07, 3.695799749467045e-08, 5.68946248085032e-09, 7.095041134218242e-10, 7.96308051579818e-11, 8.124836142151736e-12, 7.599054413933076e-13, 6.560582351420449e-14, 5.259452593780953e-15], [1.3317247544021685e-05, 1.4946539764289157e-05, 8.38758347725406e-06, 3.1379194425540532e-06, 8.804566703861573e-07, 1.9763514331560148e-07, 3.696911991539499e-08, 5.927441291449557e-09, 8.075010494759591e-10, 1.1049773582452471e-10, 1.240165279578803e-11, 1.2653570016996854e-12, 1.1834720775575664e-13, 1.0217410749404649e-14, 8.191039238467407e-16], [1.8435733079133584e-06, 2.06912439406287e-06, 1.1611352094676904e-06, 4.343979119973621e-07, 1.2188602869568667e-07, 2.73596232042588e-08, 5.117820515671522e-09, 8.205653993452642e-10, 1.1511963461266786e-10, 1.3940319075185859e-11, 1.7168229390304908e-12, 1.7516971022754915e-13, 1.6383396986754586e-14, 1.4144473676953951e-15, 1.133926605643705e-16], [2.2969358175359008e-07, 2.577953321009805e-07, 1.4466758876255822e-07, 5.4122291684667925e-08, 1.5185964331692778e-08, 3.4087767609999372e-09, 6.376369846377939e-10, 1.0223548194674587e-10, 1.4342929077377883e-11, 1.7886342010636101e-12, 1.9493389116425995e-13, 2.1824658658377123e-14, 2.0412321652877235e-15, 1.7622813299223638e-16, 1.4127762773414688e-17], [2.6016245571639575e-08, 2.9199190573624552e-08, 1.6385775722463583e-08, 6.130161847006941e-09, 1.720038384526187e-09, 3.8609513002505304e-10, 7.222195871233716e-11, 1.1579702768163624e-11, 1.6245519889797297e-12, 2.0258966862480445e-13, 2.2737540380813348e-14, 2.252768783171772e-15, 2.3120017927982423e-16, 1.996048104415926e-17, 1.6001811756556826e-18], [2.7011694279982045e-09, 3.031642697351638e-09, 1.7012737796341636e-09, 6.364717662361999e-10, 1.7858514928573353e-10, 4.00868126283196e-11, 7.49853572709874e-12, 1.2022772085441434e-12, 1.6867115413491128e-13, 2.1034127226802687e-14, 2.3607537365606533e-15, 2.4087081932016816e-16, 2.187604283484514e-17, 2.0724220570625092e-18, 1.6614082378016832e-19], [2.58879059310867e-10, 2.9055149281719655e-10, 1.6304943745358728e-10, 6.099921404902817e-11, 1.711553335928403e-11, 3.84190500470793e-12, 7.186568362277273e-13, 1.15225794262547e-13, 1.61653798028078e-14, 2.0159028209997177e-15, 2.2625374782149444e-16, 2.3084968486132442e-17, 2.1591073173765247e-18, 1.8100755338138614e-19, 1.5922873895850666e-20], [2.3038666314439595e-11, 2.5857320819987598e-11, 1.4510411124985892e-11, 5.4285601224743156e-12, 1.523178672341737e-12, 3.4190624630227094e-13, 6.395610015161416e-14, 1.0254396906021416e-14, 1.4386207679928664e-15, 1.79403125687271e-16, 2.0135211447100483e-17, 2.054422197172414e-18, 1.9214745740546853e-19, 1.6588895792261812e-20, 1.2913835935267014e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2459150974233186, "lambda_away": 1.1223445171295092, "rho": -0.061598984997362036, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3782 |
| Legacy p draw | 0.2822 |
| Legacy p away | 0.3396 |
| Legacy p over 1 5 | 0.6931 |
| Legacy p under 3 5 | 0.7849 |
| Legacy p btts yes | 0.4858 |
| Legacy p over 2 5 | 0.4260 |
| Legacy goal margin distribution | {"-1": 0.19970007367603262, "-10": 9.772649385922483e-08, "-11": 9.867510234070318e-09, "-12": 9.146217458102703e-10, "-13": 7.803686721883719e-11, "-14": 5.687899867938593e-12, "-2": 0.09654428194964895, "-3": 0.03256214088535893, "-4": 0.008563603468954526, "-5": 0.001839231595798349, "-6": 0.00033321325194563987, "-7": 5.2148004094369296e-05, "-8": 7.178689553626287e-06, "-9": 8.816893237116865e-07, "0": 0.2821849576161116, "1": 0.2089301373501057, "10": 2.606565684995702e-07, "11": 2.9216366266567276e-08, "12": 3.0062313319403873e-09, "13": 2.847363801308546e-10, "14": 2.3038666314439595e-11, "2": 0.11165671315201516, "3": 0.041805506801394283, "4": 0.012205044023035051, "5": 0.002909922877783589, "6": 0.0005852340471868244, "7": 0.00010167338184068867, "8": 1.5537352179704508e-05, "9": 2.1184083449426444e-06} |
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
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 8.924167775994395, "version": "count-markets-nb2-v1"}} |
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
| Market best home last update utc | 2026-10-28T12:07:28Z |
| Market best draw last update utc | 2026-10-28T12:07:28Z |
| Market best away last update utc | 2026-10-28T12:07:28Z |
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
| Bbs statistics cutoff utc | 2026-10-28T12:07:18.629492+00:00 |
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
| Goal margin distribution | {"-1": 0.2022559522049398, "-10": 1.0761343116120542e-06, "-11": 1.4476535567461333e-07, "-12": 1.7894682472527465e-08, "-13": 2.0449219504618338e-09, "-14": 2.155874296974924e-10, "-15": 1.8879190523796052e-11, "-2": 0.11981338132595266, "-3": 0.051581880142210296, "-4": 0.017603439761768307, "-5": 0.004952760093586357, "-6": 0.0011823802929301474, "-7": 0.0002447827137730639, "-8": 4.4695191637979545e-05, "-9": 7.2952530779710015e-06, "0": 0.2521156843865953, "1": 0.18340168788578629, "10": 6.801587276269293e-07, "11": 8.788722188400013e-08, "12": 1.0435238753554663e-08, "13": 1.1454402203106637e-09, "14": 1.1599424036631915e-10, "15": 9.756940534015186e-12, "2": 0.10449866290580759, "3": 0.04321354303750515, "4": 0.014165683822270306, "5": 0.0038282879452236885, "6": 0.0008778731883779261, "7": 0.00017457121972316495, "8": 3.061751951019818e-05, "9": 4.800283205612362e-06} |
| Raw goal margin distribution | {"-1": 0.19533547326526282, "-10": 1.0393128249829297e-06, "-11": 1.3981200036309265e-07, "-12": 1.7282390118046592e-08, "-13": 1.974951998343368e-09, "-14": 2.0821079503920148e-10, "-15": 1.8233211807255273e-11, "-2": 0.11571379378294887, "-3": 0.04981693176219229, "-4": 0.01700111269643799, "-5": 0.004783294267996182, "-6": 0.0011419234469055566, "-7": 0.00023640712038757486, "-8": 4.316588123171744e-05, "-9": 7.045635478413015e-06, "0": 0.2581357429557585, "1": 0.1873752926760903, "10": 6.948951349600427e-07, "11": 8.979139784830347e-08, "12": 1.0661329991738434e-08, "13": 1.1702574768959346e-09, "14": 1.1850738664365502e-10, "15": 9.968335674875713e-12, "2": 0.10676274450881593, "3": 0.044149813273615376, "4": 0.014472599367830382, "5": 0.003911232129070444, "6": 0.000896893302897212, "7": 0.00017835350244333912, "8": 3.128088266456956e-05, "9": 4.904286765015347e-06} |
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
| Unanchored p over 2 5 | 0.5673 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:07:05Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:07:28Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:07:05Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:07:28Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.79 |
| Reference draw odds | 3.84 |
| Reference away odds | 2.41 |
| Market reference 1x2 last update utc | 2026-10-28T12:07:28Z |
| Market reference home last update utc | 2026-10-28T12:07:28Z |
| Market reference draw last update utc | 2026-10-28T12:07:28Z |
| Market reference away last update utc | 2026-10-28T12:07:28Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-28T12:07:05Z |
| Market reference under 2 5 last update utc | 2026-10-28T12:07:05Z |
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
| Raw ev away | -0.0744 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.07486767780093775, 0.0910402237094823, 0.06461956877524536, 0.028050053186965466, 0.009131972311609612, 0.0023784031422444908, 0.0005162084481872993, 9.603243834857988e-05, 1.5632155172224474e-05, 2.2618678950174264e-06, 2.9454938786948387e-07, 3.4870351698501475e-08, 3.784129321541759e-09, 3.790648420525579e-10, 3.5259516966795324e-11], [0.08487724412885254, 0.12539190939439046, 0.08671373096702698, 0.037640683956360645, 0.012254297037813194, 0.003191606105033734, 0.0006927059611726727, 0.00012886701630631148, 2.0976966014022206e-05, 3.0352261373590696e-06, 3.952591584919613e-07, 4.6792919748913754e-08, 5.077965980768255e-09, 5.086714033504362e-10, 4.731514502859515e-11], [0.06191552235043887, 0.08062884330298437, 0.051601667392126974, 0.02525522998582058, 0.008222089969548346, 0.00214142618397228, 0.0004647749860828042, 8.646405411165278e-05, 1.4074614098486626e-05, 2.0365021593881984e-06, 2.652013699668584e-07, 3.1395974401978534e-08, 3.4070900213491996e-09, 3.41295957685554e-10, 3.174636440971733e-11], [0.027695046818055336, 0.036065585904662426, 0.02348301656956575, 0.010019266561413318, 0.003677771873748725, 0.0009578680138858832, 0.00020789560534706597, 3.867569772160892e-05, 6.295628004192811e-06, 9.109351017035743e-07, 1.1862557366266812e-07, 1.404353783918451e-08, 1.5240042249910278e-09, 1.5266296993208606e-10, 1.4200268612026583e-11], [0.009291074222627958, 0.012099204515672745, 0.007878031452786602, 0.0034196947681257874, 0.0010942855235087576, 0.00032134348322144737, 6.974436665615245e-05, 1.2974839165432506e-05, 2.1120436245977695e-06, 3.055985316626137e-07, 3.9796250096357834e-08, 4.711295607093304e-09, 5.112696311009334e-10, 5.121504195331876e-11, 4.763875306741842e-12], [0.002493559538714457, 0.0032472119055334896, 0.002114323920429537, 0.0009177854254768921, 0.00029879412483069614, 7.649012148318677e-05, 1.871815105335118e-05, 3.4822167156360363e-06, 5.668350505122977e-07, 8.20172259294367e-08, 1.068060771607646e-08, 1.2644281833589926e-09, 1.3721570132136537e-10, 1.3745208931528405e-11, 1.2785396422129148e-12], [0.0005576892962109998, 0.0007262450702013598, 0.0004728725345593024, 0.00020526444228029022, 6.682586984657285e-05, 1.7404658424582483e-05, 3.7129367866699187e-06, 7.788043394377607e-07, 1.2677372867178573e-07, 1.8343307346632368e-08, 2.3887380701385933e-09, 2.8279174919976857e-10, 3.0688550528239015e-11, 3.0741419149145987e-12, 2.859478036009447e-13], [0.0001069099401121282, 0.00013922235461478148, 9.065042971755025e-05, 3.9349525587868704e-05, 1.2810627336363537e-05, 3.336501170967714e-06, 7.241539759382397e-07, 1.3241469385707408e-07, 2.430272883516834e-08, 3.516441687532154e-09, 4.579249516839491e-10, 5.4211635720031087e-11, 5.883044773125307e-12, 5.89317977326495e-13, 5.481665645346238e-14], [1.793295738483682e-05, 2.335300674291825e-05, 1.5205604748604263e-05, 6.600446738074116e-06, 2.1488407331917627e-06, 5.5966108717925e-07, 1.2146880240453344e-07, 2.259735445855531e-08, 3.615521198569666e-09, 5.898441142389533e-10, 7.68118346655975e-11, 9.093400970106133e-12, 9.868155486654777e-13, 9.885155825950531e-14, 9.194886491641238e-15], [2.67382650588657e-06, 3.4819626836430345e-06, 2.2671747967923203e-06, 9.841349120629558e-07, 3.203948565781497e-07, 8.344617215666177e-08, 1.8111151247265124e-08, 3.369293977427752e-09, 5.484534932333194e-10, 7.800107691962991e-11, 1.1452741178558277e-11, 1.3558375242157902e-12, 1.4713543972807258e-13, 1.473889169256289e-14, 1.3709691431462917e-15], [3.588038061510153e-07, 4.672485148218979e-07, 3.042347528935928e-07, 1.3206217809453607e-07, 4.299414855764229e-08, 1.1197736320074195e-08, 2.430355891449567e-09, 4.5212937357052874e-10, 7.359759522007047e-11, 1.0649077874722554e-11, 1.3630610387386075e-12, 1.8194137246376465e-13, 1.9744271244940435e-14, 1.9778285637069267e-15, 1.8397190154017932e-16], [4.377117180701939e-08, 5.7000552023787575e-08, 3.7114187225111904e-08, 1.6110521091161988e-08, 5.244939521129297e-09, 1.3660335590458499e-09, 2.9648382612771717e-10, 5.515613867603802e-11, 8.978313300292334e-12, 1.2991016517941438e-12, 1.6917415785383538e-13, 1.9685417925359837e-14, 2.408641920880122e-15, 2.412791402508407e-16, 2.244308887456448e-17], [4.894752585689674e-09, 6.374140510431354e-09, 4.150329003911986e-09, 1.8015742213948962e-09, 5.865203105829709e-10, 1.5275799160136432e-10, 3.315458359104489e-11, 6.167887247603926e-12, 1.004008355898993e-12, 1.4527326792227624e-13, 1.891805981886326e-14, 2.23962237405619e-15, 2.388893851871659e-16, 2.698126750690262e-17, 2.5097195885905206e-18], [5.052556856528366e-10, 6.579639476489975e-10, 4.2841334466774464e-10, 1.8596560348046637e-10, 6.054294195365519e-11, 1.5768282959009377e-11, 3.422347007651126e-12, 6.366736716026294e-13, 1.0363770617211834e-13, 1.4995680232273843e-14, 1.952796820200124e-15, 2.311826631473658e-16, 2.5087934352140574e-17, 2.470158684891746e-18, 2.5906316393538185e-19], [4.842916607997775e-11, 6.306637649046749e-11, 4.106376555265287e-11, 1.7824953487622835e-11, 5.8030899485189376e-12, 1.5114026737398296e-12, 3.2803472840231015e-13, 6.102568631356053e-14, 9.933757950437179e-15, 1.4373480775632948e-15, 1.8717715448115774e-16, 2.2159045224615523e-17, 2.404698796755785e-18, 2.408841485377202e-19, 2.2023355421281583e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3419113220737786, "lambda_away": 1.302239571631634, "rho": -0.061598984997362036, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3589 |
| Legacy p draw | 0.2631 |
| Legacy p away | 0.3780 |
| Legacy p over 1 5 | 0.7492 |
| Legacy p under 3 5 | 0.7258 |
| Legacy p btts yes | 0.5423 |
| Legacy p over 2 5 | 0.4973 |
| Legacy goal margin distribution | {"-1": 0.2070278218789029, "-10": 3.4490682448498566e-07, "-11": 4.030381390556731e-08, "-12": 4.324547089301913e-09, "-13": 4.2637998708115304e-10, "-14": 3.5259516966795324e-11, "-2": 0.11151356766677002, "-3": 0.04266723249878878, "-4": 0.01282922560524973, "-5": 0.003164185353447404, "-6": 0.0006601021056591442, "-7": 0.00011916938373591994, "-8": 1.894715151817742e-05, "-9": 2.6900995257179533e-06, "0": 0.26305514584024625, "1": 0.19272574486338814, "10": 4.2014645587214384e-07, "11": 5.0591550615606105e-08, "12": 5.593780298891325e-09, "13": 5.68322062143304e-10, "14": 4.842916607997775e-11, "2": 0.10684721241739456, "3": 0.042127228557267624, "4": 0.013052742961745188, "5": 0.0033173873807211276, "6": 0.0007131457844697563, "7": 0.00013266758501081873, "8": 2.173586795909288e-05, "9": 3.1800528364996023e-06} |
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
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 10.005684323962337, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,480.4127 |
| Elo away rating | 1,532.6617 |
| Elo rating diff | 7.7510 |
| Elo home expectancy | 0.5112 |

</details>


---
