# Ligue 1 — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,756 |
| Training data through | 2026-10-31 |
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
| Training sha256 | 47b25ac334e6029623ac9a98dd81bd03d80ab2d781f8f78ce52f1d10b87f3ef8 |
| Training as of utc | 2026-11-01T09:25:32.352914+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 76, 'bbs_added_results': 4, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 76, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 134, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-01T09:25:32.352914+00:00', 'observations': 462, 'observations_sha256': 'fad4edfd2cff03c9620cae8d9fa11469dc7b5cfbfd352bf74a0a68c8c62cd190', 'eligible_training_matches': 176, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 173, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 19, 'retrospective_eligible_training_matches': 176, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'c4783747d26d9f9fbf43cad53b735a1f684b3a12eed1526f37dd9a5b35168d9c', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 116, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-08-31T00:00:00+00:00', 'audit_origin_utc': '2025-10-04T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 27, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1750, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1465, 'tuning_matches': 188, 'audit_matches': 92, 'audit_matchdays': 31, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8740131822227161, 'audit_candidate_poisson_score': 0.8703668995811455, 'audit_gain': 0.0036462826415705196, 'audit_gain_lower95': -0.0020867462808750554, 'audit_baseline_briers': [0.5996494887036665, 0.17689503454333355, 0.2163131972282897, 0.24794984738788303], 'audit_candidate_briers': [0.5975481546118023, 0.17562674277288576, 0.21497744296286103, 0.24618847014566814], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1591.936 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.196 |
| Dixon-Coles low-score adjustment | -0.053 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1756, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-31'} |
| Training data health | {'training_end': '2026-10-31', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 16.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261101T092532352914Z_0ca811d67770e4869b3dd3fcfe40c1a1a5dffb53ecdf6ce6fce7ccf806f89ba0.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 5} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 5} |
| Legacy comparison status | {'AVAILABLE': 5} |
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

## 2026-11-01 — Lyon vs Angers

The model's most likely 1X2 outcome is **Lyon win** at **68.8%**. Expected goals are 2.05 for Lyon and 0.74 for Angers (2.79 combined). The most likely exact score is 2-0 at 13.2%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.2%; Under 3.5 goals: 69.3%; Double Chance 1X: 88.4%; Double Chance X2: 31.2%; Double Chance 12 (either team wins): 80.4%; Under 4.5 goals: 84.8%; BTTS Yes (both teams score): 45.6%; BTTS No (at least one team does not score): 54.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 68.8% | 1.45 |
| Draw | 19.6% | 5.11 |
| Angers win | 11.6% | 8.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 2.05 |
| Angers expected goals | 0.74 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 30.7% |
| Under 3.5 | 69.3% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.19% |
| 2 | 1-0 | 12.36% |
| 3 | 2-1 | 9.72% |
| 4 | 1-1 | 9.30% |
| 5 | 3-0 | 9.01% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:15:00+00:00 |
| Fixture id | 961df571fad52d969150e9ced52b16f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 12.00 |
| Matched home-team name | Lyon |
| Matched away-team name | Angers |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0503 |
| Dc lambda away | 0.7372 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:25:32.352914+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 45.6% |
| P btts no | 54.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.84 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.25 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.57 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.08295806212450442, "-10": 9.047144722481092e-10, "-11": 5.99536686624177e-11, "-12": 3.648175963233948e-12, "-13": 2.051921514521592e-13, "-14": 1.072830250140471e-14, "-15": 5.239341802092341e-16, "-16": 2.3926415896709247e-17, "-17": 9.528648154926358e-19, "-2": 0.026410025490441393, "-3": 0.00580762869751642, "-4": 0.0009984172414904604, "-5": 0.00014037685269687207, "-6": 1.666377224256827e-05, "-7": 1.7097576224456216e-06, "-8": 1.5436976707952697e-07, "-9": 1.2438775298107018e-08, "0": 0.1956528785030941, "1": 0.24865823407677162, "10": 2.6015726283395598e-05, "11": 4.794607522353176e-06, "12": 8.113831014439181e-07, "13": 1.269181718740839e-07, "14": 1.8454698540596585e-08, "15": 2.506487587825018e-09, "16": 3.1833130968138613e-10, "17": 3.52570426792673e-11, "2": 0.21222189208500622, "3": 0.12978756553561765, "4": 0.06205248779170171, "5": 0.02426361513658908, "6": 0.008010252581227086, "7": 0.002285705745400098, "8": 0.0005739326109624441, "9": 0.00012861427018671145} |
| Raw goal margin distribution | {"-1": 0.08458383084379137, "-10": 9.22444593362314e-10, "-11": 6.112860930859103e-11, "-12": 3.7196710079781096e-12, "-13": 2.0921339993278846e-13, "-14": 1.0938550163550613e-14, "-15": 5.342019682859498e-16, "-16": 2.4395313283332626e-17, "-17": 9.71538561853925e-19, "-2": 0.026927595359099745, "-3": 0.00592144356767919, "-4": 0.0010179837004751923, "-5": 0.000143127884847117, "-6": 1.6990340136796934e-05, "-7": 1.7432645582267726e-06, "-8": 1.5739502504836487e-07, "-9": 1.2682543911645158e-08, "0": 0.20619016102448226, "1": 0.24402594270696037, "10": 2.5531075434050557e-05, "11": 4.705288062935751e-06, "12": 7.962677244993973e-07, "13": 1.245537943000719e-07, "14": 1.811090320601024e-08, "15": 2.4597938563074195e-09, "16": 3.1240106818324e-10, "17": 3.460023396696134e-11, "2": 0.20826837877047477, "3": 0.1273697335986554, "4": 0.06089650273156462, "5": 0.02381160462740585, "6": 0.007861028389879494, "7": 0.002243124991790001, "8": 0.0005632407346588678, "9": 0.00012621829574398883} |
| Unadjusted home-win probability | 67.5% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 45.9% |
| P home draw | 88.4% |
| P draw away | 31.2% |
| P home away | 80.4% |
| Raw p home draw | 88.1% |
| Raw p draw away | 32.5% |
| Raw p home away | 79.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5323 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.2, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.78, "price": 2.2, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.44 |
| Reference draw odds | 5.20 |
| Reference away odds | 8.60 |
| Market reference 1x2 last update utc | 2026-11-01T09:25:56Z |
| Market reference home last update utc | 2026-11-01T09:25:56Z |
| Market reference draw last update utc | 2026-11-01T09:25:56Z |
| Market reference away last update utc | 2026-11-01T09:25:56Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-01T09:25:09Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:25:09Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.0183 |
| Raw edge prob draw | 0.0151 |
| Raw edge prob away | 0.0033 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0560752683715906, 0.03574919384608974, 0.01690372982187003, 0.004643792116488648, 0.000956806816383576, 0.00015771236281271006, 2.1663367636026218e-05, 2.5505827134405715e-06, 2.6276100057374595e-07, 2.4061897893610218e-08, 1.9830851461232226e-09, 1.4857993308314013e-10, 1.0204468617145228e-11, 6.469318367095851e-13, 3.8083948608751575e-14, 2.09248422895716e-15, 1.0778385009594329e-16, 5.2253604448266e-18], [0.10777987571394972, 0.094185630896245, 0.03592590531401279, 0.009869563559817584, 0.0020335246393210294, 0.00033518989435858356, 4.604167853343195e-05, 5.420815052312917e-06, 5.584523017289529e-07, 5.113933282835991e-08, 4.214698764119652e-09, 3.157805208529256e-10, 2.1687803649408884e-11, 1.3749398597331436e-12, 8.094073592749702e-14, 4.447207277492061e-15, 2.290756202170669e-16, 1.1105584776298821e-17], [0.12054029534892373, 0.09934447825881415, 0.038892478526469494, 0.010488010920580718, 0.00216094951871034, 0.0003561935896348893, 4.892674578098832e-05, 5.760494587478699e-06, 5.934460833711828e-07, 5.4343829686524044e-08, 4.478800546461242e-09, 3.3556798445435654e-10, 2.3046806491473137e-11, 1.4610964483508992e-12, 8.60126506286078e-14, 4.725878526414278e-15, 2.434299745793221e-16, 1.1801483794832543e-17], [0.08539573381857514, 0.07037973979720022, 0.029002079802048476, 0.007569370643063722, 0.001530906070546756, 0.000252342280067388, 3.466173155813226e-05, 4.080972765428569e-06, 4.2042176539012405e-07, 3.8499417984326556e-08, 3.172967663510109e-09, 2.3773024776113464e-10, 1.6327311517008177e-11, 1.0351011918916204e-12, 6.09349213625954e-14, 3.348007929899245e-15, 1.7245586840868737e-16, 8.360659527923964e-18], [0.04537340397232181, 0.03739494026797208, 0.015409705193137216, 0.004233353718226212, 0.0008286601402854253, 0.00013407728584099204, 1.8416853840832213e-05, 2.16834749941052e-06, 2.233831334048848e-07, 2.0455935756853334e-08, 1.6858962052298976e-09, 1.2631345953443665e-10, 8.675207391707095e-12, 5.499813917134385e-13, 3.237661507635296e-14, 1.778900531829753e-15, 9.163115573582534e-17, 4.4422779133378616e-18], [0.019286638298904764, 0.015895273971454262, 0.006550123736232958, 0.0017994497835022046, 0.0003707585902653893, 5.8059474519899246e-05, 7.828356868455375e-06, 9.216882637453425e-07, 9.495231388599612e-08, 8.695098878821775e-09, 7.166151858388178e-10, 5.369140935095159e-11, 3.687525565282776e-12, 2.337777474129094e-13, 1.3762160421144465e-14, 7.561480542226583e-16, 3.894918174235989e-17, 1.888256111223752e-18], [0.006831726376897054, 0.005630434955839657, 0.002320189366713189, 0.0006374023486794902, 0.00013133036464530294, 2.164744414713919e-05, 2.8249272007923966e-06, 3.264810551802114e-07, 3.363407439228045e-08, 3.0799839474123404e-09, 2.538399274827511e-10, 1.9018608209005664e-11, 1.3061978598548798e-12, 8.280891561195737e-14, 4.87484199657337e-15, 2.678432875036429e-16, 1.3796606134462928e-17, 6.688593875956559e-19], [0.0020742332992610764, 0.0017094999170664488, 0.0007044506438815892, 0.00019352665837572974, 3.9874228053482814e-05, 6.5725479939793294e-06, 9.028050874368494e-07, 1.009829005155452e-07, 1.021190153783345e-08, 9.351377547140486e-10, 7.707030422753616e-11, 5.774386776690144e-12, 3.965848376915128e-13, 2.51422555240038e-14, 1.4800884930232627e-15, 8.132197270113034e-17, 4.1888943265743855e-18, 2.0307757332992302e-19], [0.0005510522669678317, 0.00045415518351593967, 0.00018714824625377808, 5.1413360230329714e-05, 1.059320750963336e-05, 1.7460993771180026e-06, 2.3984418254175845e-07, 2.8238565498605368e-08, 2.7637867285678035e-09, 2.484338573900816e-10, 2.047492240897573e-11, 1.5340554626992653e-12, 1.0535891692261904e-13, 6.67943037464608e-15, 3.932084783732002e-16, 2.1604444122663556e-17, 1.1128447873099963e-18, 5.3950709013130594e-20], [0.00013012941045673212, 0.0001072474424467764, 4.4194520942669716e-05, 1.2141117381090383e-05, 2.501555534213757e-06, 4.1233635385170624e-07, 5.66385149767614e-08, 6.668456153346781e-09, 6.869842730063576e-10, 5.976627221028371e-11, 4.835094131611442e-12, 3.622627923616511e-13, 2.488020568528136e-14, 1.5773283024897226e-15, 9.285505304033205e-17, 5.101827440792901e-18, 2.6279510090637347e-19, 1.274030500996237e-20], [2.765671794273663e-05, 2.2793558008292093e-05, 9.392768291470808e-06, 2.580381004877615e-06, 5.316616404010038e-07, 8.763484131671267e-08, 1.2037520403034427e-08, 1.4172630944788644e-09, 1.4600642700944377e-10, 1.3370293654084653e-11, 1.0468701792954306e-12, 7.699258633639672e-14, 5.287850214490084e-15, 3.352333942952786e-16, 1.973470872173199e-17, 1.0843037098783955e-18, 5.585247759896063e-20, 2.7077277990291157e-21], [5.3435900649657805e-06, 4.403972675663003e-06, 1.814788849087225e-06, 4.985587346278613e-07, 1.0272302973376957e-07, 1.6932040467506814e-08, 2.325784808076646e-09, 2.7383122635087854e-10, 2.821008965721167e-11, 2.5832916430492495e-12, 2.1290453928805146e-13, 1.515458747468066e-14, 1.0216723448415238e-15, 6.477087552145577e-17, 3.812968468593563e-18, 2.0949971516896516e-19, 1.0791329073083713e-20, 5.231635726076301e-22], [9.464050869929196e-07, 7.79989125766139e-07, 3.214178815577191e-07, 8.829991015030876e-08, 1.8193311371086063e-08, 2.998839551087652e-09, 4.1192055282195083e-10, 4.849834333196377e-11, 4.9962987488791296e-12, 4.575276775434613e-13, 3.7707596686196434e-14, 2.825189933631309e-15, 1.8433944988315595e-16, 1.1471592194990628e-17, 6.753161659760774e-19, 3.710456710730973e-20, 1.9112560293762763e-21, 9.265768152602878e-23], [1.5472443019882164e-07, 1.27517671559542e-07, 5.254747598382518e-08, 1.4435840923069635e-08, 2.9743603178055327e-09, 4.902697028753379e-10, 6.734343855342863e-11, 7.928823123159158e-12, 8.168272631328239e-13, 7.479958654177423e-14, 6.1646820073383275e-15, 4.618803392883932e-16, 3.17219380123656e-17, 1.9105932664997318e-18, 1.1040505849001543e-19, 6.06609482805473e-21, 3.124645082465824e-22, 1.5148277597715347e-23], [2.3488540642735613e-08, 1.9358313404318e-08, 7.977172859730146e-09, 2.191488673106579e-09, 4.515342736834804e-10, 7.44272887422596e-11, 1.022333119243779e-11, 1.2036656650670555e-12, 1.2400162239108349e-13, 1.1355240580227803e-14, 9.358533987996556e-16, 7.011753158512239e-17, 4.815671509097363e-18, 3.0529872071299825e-19, 1.7074532903227856e-20, 9.208869906863423e-22, 4.74348833725299e-23, 2.299642878401036e-24], [3.328050854210454e-09, 2.74284607295257e-09, 1.1302718782667369e-09, 3.105082542784768e-10, 6.39771132695874e-11, 1.0545474307781296e-11, 1.448526182421283e-12, 1.70545314233863e-13, 1.756957622864321e-14, 1.608904473359866e-15, 1.3259945565218434e-16, 9.93483224166017e-18, 6.823241989878622e-19, 4.3257249724984086e-20, 2.5464921990255463e-21, 1.3292386908564594e-22, 6.72096689736853e-24, 3.2583243728292357e-25], [4.420741795173718e-10, 3.643398134102778e-10, 1.5013713284584608e-10, 4.124566833762954e-11, 8.498256515750443e-12, 1.400784455062038e-12, 1.9241173036559188e-13, 2.2654004750283094e-14, 2.3338152978999542e-15, 2.1371522135322957e-16, 1.761355163420309e-17, 1.3196711842062859e-18, 9.063500638843684e-20, 5.745979859699925e-21, 3.382575864510569e-22, 1.858522266809539e-23, 9.094936454915932e-25, 4.328122185685966e-26], [5.526770190565724e-11, 4.554942390416343e-11, 1.8770004419062008e-11, 5.156495014190569e-12, 1.0624441091381322e-12, 1.751247670265822e-13, 2.4055135200628355e-14, 2.832182560118938e-15, 2.9177141340400023e-16, 2.671847778883385e-17, 2.202029809299878e-18, 1.6498406150258456e-19, 1.1331104025940119e-20, 7.183570467483646e-22, 4.2288648198620846e-23, 2.3235072163498665e-24, 1.196838427923099e-25, 5.512371601082697e-27]] |
| Legacy trial inputs | {"lambda_home": 2.125324155828135, "lambda_away": 0.8241599041320185, "rho": -0.060463437633334456, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6807 |
| Legacy p draw | 0.1976 |
| Legacy p away | 0.1217 |
| Legacy p over 1 5 | 0.8004 |
| Legacy p under 3 5 | 0.6565 |
| Legacy p btts yes | 0.4975 |
| Legacy p over 2 5 | 0.5688 |
| Legacy goal margin distribution | {"-1": 0.08383625874024314, "-10": 2.3229807214223272e-09, "-11": 1.7179158662083548e-10, "-12": 1.1668862654848725e-11, "-13": 7.327753493098184e-13, "-14": 4.2782946520350887e-14, "-15": 2.333361332969059e-15, "-16": 1.188894348722421e-16, "-17": 5.2253604448266e-18, "-2": 0.029205958312624607, "-3": 0.007070438535429521, "-4": 0.0013452367672421306, "-5": 0.00020995614967191993, "-6": 2.7717869109047706e-05, "-7": 3.1666818978155318e-06, "-8": 3.1862577813875694e-07, "-9": 2.8629055969339504e-08, "0": 0.19761239678689063, "1": 0.24075312527167433, "10": 3.239700661587233e-05, "11": 6.178383557341711e-06, "12": 1.0822191130477531e-06, "13": 1.7525532359385313e-07, "14": 2.638668034354822e-08, "15": 3.711160672039794e-09, "16": 4.876236034215352e-10, "17": 5.526770190565724e-11, "2": 0.20826733969666925, "3": 0.1300198785833422, "4": 0.06379341182915214, "5": 0.025675528824343333, "6": 0.008741064671254243, "7": 0.0025752691751587385, "8": 0.0006682097304180177, "9": 0.00015482910748334023} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6679 |
| Legacy raw p draw | 0.2041 |
| Legacy raw p away | 0.1280 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1253 |
| Legacy lambda away | 0.8242 |
| Legacy model home team | Lyon |
| Legacy model away team | Angers |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 86.4% |
| Market reference home draw last update utc | 2026-11-01T09:25:56Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.0% |
| Market reference draw away last update utc | 2026-11-01T09:25:56Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.6% |
| Market reference home away last update utc | 2026-11-01T09:25:56Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.88 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 82.7% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-11-01T09:25:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.6% |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-11-01T09:25:32Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 53.7% |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-11-01T09:25:56Z |
| Market btts yes bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.904560292539232, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,581.6014 |
| Elo away rating | 1,418.6457 |
| Elo rating diff | 222.9557 |
| Elo home expectancy | 0.7830 |

</details>


---

## 2026-11-01 — Marseille vs Toulouse

The model's most likely 1X2 outcome is **Marseille win** at **51.4%**. Expected goals are 1.96 for Marseille and 1.16 for Toulouse (3.12 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 59.8%; Under 3.5 goals: 62.5%; Double Chance 1X: 75.1%; Double Chance X2: 48.6%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 79.8%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 51.4% | 1.94 |
| Draw | 23.7% | 4.22 |
| Toulouse win | 24.9% | 4.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 1.96 |
| Toulouse expected goals | 1.16 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 59.8% |
| Under 2.5 | 40.2% |
| Over 3.5 | 37.5% |
| Under 3.5 | 62.5% |
| Over 4.5 | 20.2% |
| Under 4.5 | 79.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.95% |
| 2 | 2-1 | 9.11% |
| 3 | 2-0 | 7.88% |
| 4 | 1-0 | 7.54% |
| 5 | 1-2 | 6.69% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T19:45:00+00:00 |
| Fixture id | df1e1589c51bbcac432125567d1f7c58 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 7.00 |
| Matched home-team name | Marseille |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9618 |
| Dc lambda away | 1.1562 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:25:32.352914+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.48 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.57 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.66 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.95 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.1504821045897427, "-10": 7.366571383553757e-08, "-11": 7.613853174233308e-09, "-12": 7.231974823985082e-10, "-13": 6.353473657890325e-11, "-14": 5.189329495390477e-12, "-15": 3.930450394108429e-13, "-16": 2.4875576062859752e-14, "-2": 0.06844492283032914, "-3": 0.022527611435220914, "-4": 0.005888479297914253, "-5": 0.0012703316420189072, "-6": 0.00023269788367397915, "-7": 3.698131732010625e-05, "-8": 5.185240511187558e-06, "-9": 6.500640905397671e-07, "0": 0.23691352545281222, "1": 0.20828689903610365, "10": 1.1692648207861335e-05, "11": 2.050614238302845e-06, "12": 3.304976422798369e-07, "13": 4.9266837219103863e-08, "14": 6.827892663673935e-09, "15": 8.775052971789582e-10, "16": 9.423507126096876e-11, "2": 0.15810034117125066, "3": 0.08829552734007848, "4": 0.03916144422906419, "5": 0.014335229563578057, "6": 0.004455659131645105, "7": 0.0012015279883412346, "8": 0.0002858593547174948, "9": 6.080953312223259e-05} |
| Raw goal margin distribution | {"-1": 0.13043532663186, "-10": 6.385218675604849e-08, "-11": 6.5995583223378125e-09, "-12": 6.268552668980819e-10, "-13": 5.5070828127581265e-11, "-14": 4.498022469694643e-12, "-15": 3.406847494348513e-13, "-16": 2.1561725879370473e-14, "-2": 0.05932689398520657, "-3": 0.019526550109061635, "-4": 0.005104033617036113, "-5": 0.0011011018427025477, "-6": 0.00020169856439944362, "-7": 3.205477632755887e-05, "-8": 4.494478207793507e-06, "-9": 5.634644877699108e-07, "0": 0.2287306030865212, "1": 0.22503223685078597, "10": 1.263268497971293e-05, "11": 2.2154744782261753e-06, "12": 3.570681788452336e-07, "13": 5.3227671223127606e-08, "14": 7.37682478443969e-09, "15": 9.480528097850575e-10, "16": 1.0181115074344288e-10, "2": 0.17081090354353995, "3": 0.09539409397906258, "4": 0.0423098497022901, "5": 0.015487718091680473, "6": 0.004813874255552339, "7": 0.0012981254803183086, "8": 0.000308841172029979, "9": 6.569834840152865e-05} |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 82.3% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 59.4% |
| P home draw | 75.1% |
| P draw away | 48.6% |
| P home away | 76.3% |
| Raw p home draw | 78.4% |
| Raw p draw away | 44.4% |
| Raw p home away | 77.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5980 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.88, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.14, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.22, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.46, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 6.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.00 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-11-01T09:25:56Z |
| Market reference home last update utc | 2026-11-01T09:25:56Z |
| Market reference draw last update utc | 2026-11-01T09:25:56Z |
| Market reference away last update utc | 2026-11-01T09:25:56Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-11-01T09:25:33Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:25:33Z |
| Home probability edge | +1.8% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | 0.0591 |
| Raw edge prob draw | -0.0117 |
| Raw edge prob away | -0.0474 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05959555044555627, 0.05651576120488755, 0.033389487738488016, 0.011639828040756134, 0.0030432990889120172, 0.0006365502522644531, 0.00011095311694640699, 1.657675543132184e-05, 2.1670433843446166e-06, 2.518159063334364e-07, 2.633547903404653e-08, 2.5038401557682033e-09, 2.1821440540616235e-10, 1.7554890616405747e-11, 1.3113787894409748e-12, 9.143131350166122e-14, 5.97630893049601e-15], [0.08771812531726883, 0.11213556352109576, 0.06345578389186869, 0.022121166352646215, 0.005783704464615627, 0.0012097458805109763, 0.00021086328326519143, 3.1503658232701966e-05, 4.118405102776299e-06, 4.785690591596112e-07, 5.004983842106018e-08, 4.758477909832248e-09, 4.147103501556474e-10, 3.336257668655327e-11, 2.4922385666679622e-12, 1.7376264397801258e-13, 1.135780731153477e-14], [0.08897944652204727, 0.09305672475032584, 0.052542072478847304, 0.0210203277526108, 0.005495883966168696, 0.0011495440385162837, 0.00020036987447073345, 2.9935908934494934e-05, 3.913456627843075e-06, 4.547535295122555e-07, 4.755915627613575e-08, 4.5216768263336565e-09, 3.9407268783677376e-10, 3.170232009665577e-11, 2.3682147077561624e-12, 1.6511551286901814e-13, 1.079259693785995e-14], [0.05636764654336284, 0.05895056413853588, 0.030825918992184943, 0.01160337184486166, 0.0034815910522838843, 0.000728225388916758, 0.00012693244005856759, 1.8964118116376472e-05, 2.4791381446318717e-06, 2.8808210455143833e-07, 3.01282803575265e-08, 2.864439947566285e-09, 2.4964135930956045e-10, 2.0083123054379335e-11, 1.500241851386617e-12, 1.0459913195707243e-13, 6.837009143763693e-15], [0.026781282372189838, 0.02800847296293434, 0.014645948368216238, 0.005105688408130985, 0.0014413974439471632, 0.00034599297588509793, 6.030788453770973e-05, 9.010193495013698e-06, 1.1778831078210193e-06, 1.368729876354086e-07, 1.4314487709234072e-08, 1.3609469221841436e-09, 1.1860909840015077e-10, 9.541852860949354e-12, 7.127918781858878e-13, 4.969692830218311e-14, 3.2483859747367688e-15], [0.010179415029466673, 0.010645863281265723, 0.005566842725015589, 0.0019406434910477595, 0.000507392252491131, 0.0001145943641456229, 2.2922688231538408e-05, 3.4247239473785388e-06, 4.477067544442529e-07, 5.2024653939301215e-08, 5.44085638997647e-09, 5.172882822210766e-10, 4.508265220860902e-11, 3.6268046866407497e-12, 2.7092818995186567e-13, 1.888952335616651e-14, 1.2346932664838043e-15], [0.003224282072023226, 0.0033720273728532536, 0.0017632713809273858, 0.0006146897437879286, 0.00016071412143575298, 3.361569518918426e-05, 6.326744244064863e-06, 1.0847652829948299e-06, 1.4180901925107384e-07, 1.6478565665525273e-08, 1.7233657989061536e-09, 1.6384864254036542e-10, 1.4279719105145098e-11, 1.1487734114401521e-12, 8.581523625265445e-14, 5.983168122141363e-15, 3.910833139279225e-16], [0.0008753796488762667, 0.0009154919053956076, 0.0004787211068482058, 0.00016688579971145998, 4.363323929150133e-05, 9.126526400022654e-06, 1.5907880758414899e-06, 2.5662781062873597e-07, 3.850057988307375e-08, 4.473864477130061e-09, 4.678869014041303e-10, 4.4484249197786944e-11, 3.876886456298724e-12, 3.118873730901132e-13, 2.329849240886806e-14, 1.6244061446650161e-15, 1.0617755096494096e-16], [0.00020795430532467507, 0.00021748333247328743, 0.00011372450267341056, 3.964522203834664e-05, 1.0365468260060076e-05, 2.1680883945387257e-06, 3.779060087301083e-07, 5.6460383044235366e-08, 7.96972369824167e-09, 1.0628067269471407e-09, 1.111507397697838e-10, 1.0567633313946379e-11, 9.209892312177792e-13, 7.40916493703635e-14, 5.534766327065034e-15, 3.858922832083052e-16, 2.5223431776525752e-17], [4.3912368671969644e-05, 4.592455184164131e-05, 2.4014469335627854e-05, 8.371625696866028e-06, 2.188809041403139e-06, 4.5782123503411074e-07, 7.979997313736799e-08, 1.1922374733854101e-08, 1.5585862625359209e-09, 1.9555898140006135e-10, 2.3470984432433177e-11, 2.2314989312084187e-12, 1.9447935257222212e-13, 1.564545546477636e-14, 1.1687408879937449e-15, 8.148638318141393e-17, 5.326269314856292e-18], [8.345422363028878e-06, 8.727832124345338e-06, 4.563882466166012e-06, 1.5910039567082013e-06, 4.1597701228505e-07, 8.700764018594205e-08, 1.5165760821615538e-08, 2.2658138409151238e-09, 2.962049427859628e-10, 3.441976135177794e-11, 3.886845578332929e-12, 4.240901059721057e-13, 3.6960254870960985e-14, 2.9733748796580354e-15, 2.22115924014712e-16, 1.54862583151566e-17, 1.0122425274701641e-18], [1.441840078808832e-06, 1.5079090800419433e-06, 7.885027705539364e-07, 2.748780313969327e-07, 7.1868421043948e-08, 1.503232518685107e-08, 2.6201911451606627e-09, 3.9146505291620785e-10, 5.117537968384792e-11, 5.946708178592034e-12, 6.21920238634698e-13, 6.384566821440399e-14, 6.385629687482898e-15, 5.137104971231649e-16, 3.837500697446253e-17, 2.675563553080058e-18, 1.748853182131247e-19], [2.2834804865360976e-07, 2.388115721260172e-07, 1.248772812326775e-07, 4.3533165022774644e-08, 1.1381993014620192e-08, 2.3807093266402867e-09, 4.1496664150936876e-10, 6.199736174857021e-11, 8.104781009811031e-12, 9.417959928092652e-13, 9.849516253407586e-14, 9.364406957735965e-15, 8.812283590374703e-16, 8.135769792712463e-17, 6.077551934141386e-18, 4.2373611704516567e-19, 2.769705304982538e-20], [3.338223496933089e-08, 3.491189901166686e-08, 1.8255828193058462e-08, 6.364119826368163e-09, 1.6639352404088417e-09, 3.4803624819295004e-10, 6.066403463036933e-11, 9.063403473654608e-12, 1.1848391332430407e-12, 1.3768129533186687e-13, 1.4399022362755715e-14, 1.3689840366701874e-15, 1.1930954812922508e-16, 1.036385386199583e-17, 8.884782151634646e-19, 6.194604555456973e-20, 4.049036277379537e-21], [4.531571443409879e-09, 4.739220269158934e-09, 2.4781920620792663e-09, 8.639165021186916e-10, 2.2587587158401684e-10, 4.7245222647065265e-11, 8.235021029166274e-12, 1.230338843371288e-12, 1.6083953594393787e-13, 1.8689959698347767e-14, 1.9546384060872815e-15, 1.8583683725065308e-16, 1.6196031863212603e-17, 1.302936748146006e-18, 1.0509564729027776e-19, 8.409051440838334e-21, 5.496485536322236e-22], [5.741416189745188e-10, 6.004503364873141e-10, 3.1398229519721513e-10, 1.0945660360415615e-10, 2.8618050099844357e-11, 5.9858812683722184e-12, 1.0433617487925987e-12, 1.5588162831410437e-13, 2.037806811945043e-14, 2.3679829069854325e-15, 2.4764902705280345e-16, 2.3545179401145646e-17, 2.0520069187987206e-18, 1.6507964694892708e-19, 1.2331717258033866e-20, 9.283713544237936e-22, 6.963944282691156e-23], [6.819625158358402e-11, 7.132118776491954e-11, 3.729465847521279e-11, 1.3001200104960424e-11, 3.3992375399060105e-12, 7.109999544302187e-13, 1.239299816662588e-13, 1.8515541097255295e-14, 2.420496641131204e-15, 2.8126781395649394e-16, 2.941562638062706e-17, 2.7966845199083388e-18, 2.4373634563472277e-19, 1.9608077106073536e-20, 1.4647551488926743e-21, 1.0212494536278796e-22, 7.207776084354325e-24]] |
| Legacy trial inputs | {"lambda_home": 1.900471920649543, "lambda_away": 1.045822697124423, "rho": -0.060463437633334456, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5317 |
| Legacy p draw | 0.2374 |
| Legacy p away | 0.2309 |
| Legacy p over 1 5 | 0.7962 |
| Legacy p under 3 5 | 0.6629 |
| Legacy p btts yes | 0.5607 |
| Legacy p over 2 5 | 0.5617 |
| Legacy goal margin distribution | {"-1": 0.14484350391833872, "-10": 3.150884482725478e-08, "-11": 2.9518039994934616e-09, "-12": 2.540530443184036e-10, "-13": 2.021908170508649e-11, "-14": 1.4959340303568473e-12, "-15": 1.0278912081319598e-13, "-16": 5.97630893049601e-15, "-2": 0.061798642451008225, "-3": 0.01870948384141376, "-4": 0.004473610638558771, "-5": 0.0008799710642536018, "-6": 0.00014667316028471865, "-7": 2.118144954600543e-05, "-8": 2.696158363095882e-06, "-9": 3.066468818105364e-07, "0": 0.23743914163974272, "1": 0.21724911425768723, "10": 9.9848048298127e-06, "11": 1.6998007246800805e-06, "12": 2.6585099556849995e-07, "13": 3.8448438733792e-08, "14": 5.1693164383724055e-09, "15": 6.454628067394384e-10, "16": 6.819625158358402e-11, "2": 0.16468683329831796, "3": 0.09060353542070548, "4": 0.03936814168905982, "5": 0.014072087231280355, "6": 0.0042623015393198635, "7": 0.0011185427656872934, "8": 0.00025872935608646524, "9": 5.347394897423204e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5669 |
| Legacy raw p draw | 0.2345 |
| Legacy raw p away | 0.1987 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9005 |
| Legacy lambda away | 1.0458 |
| Legacy model home team | Marseille |
| Legacy model away team | Toulouse |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 72.7% |
| Market reference home draw last update utc | 2026-11-01T09:25:56Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.7% |
| Market reference draw away last update utc | 2026-11-01T09:25:56Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.6% |
| Market reference home away last update utc | 2026-11-01T09:25:56Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 85.4% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-11-01T09:25:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.7% |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.16 |
| Market reference under 3 5 last update utc | 2026-11-01T09:25:32Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 66.7% |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.70 |
| Market reference btts yes last update utc | 2026-11-01T09:25:56Z |
| Market btts yes bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.523036445585282, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,566.8488 |
| Elo away rating | 1,531.5216 |
| Elo rating diff | 95.3273 |
| Elo home expectancy | 0.6338 |

</details>


---

## 2026-11-01 — Paris FC vs AS Monaco

The model's most likely 1X2 outcome is **Paris FC win** at **38.4%**. Expected goals are 1.52 for Paris FC and 1.50 for AS Monaco (3.02 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.6%; Under 3.5 goals: 64.3%; Double Chance 1X: 65.4%; Double Chance X2: 61.6%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 81.4%; BTTS Yes (both teams score): 61.7%; BTTS No (at least one team does not score): 38.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 38.4% | 2.60 |
| Draw | 27.0% | 3.71 |
| AS Monaco win | 34.6% | 2.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.52 |
| AS Monaco expected goals | 1.50 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.6% |
| Under 2.5 | 42.4% |
| Over 3.5 | 35.7% |
| Under 3.5 | 64.3% |
| Over 4.5 | 18.6% |
| Under 4.5 | 81.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.45% |
| 2 | 2-1 | 8.59% |
| 3 | 1-2 | 7.84% |
| 4 | 1-0 | 6.94% |
| 5 | 2-2 | 6.74% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:15:00+00:00 |
| Fixture id | cf3a2e2b4a4e9815d1d0be8dcef916da |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 14.00 |
| Matched home-team name | Paris FC |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5228 |
| Dc lambda away | 1.4980 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:25:32.352914+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.7% |
| P btts no | 38.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.21 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.38 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.17778772299332685, "-10": 8.840880485082167e-07, "-11": 1.1838250003766126e-07, "-12": 1.4567669911123861e-08, "-13": 1.657296504123785e-09, "-14": 1.7382620773716625e-10, "-15": 1.506829215152706e-11, "-2": 0.10368476484831772, "-3": 0.0441829263490597, "-4": 0.014955986183673851, "-5": 0.004178929749951591, "-6": 0.0009915546281783502, "-7": 0.00020413135030428628, "-8": 3.707815358542542e-05, "-9": 6.02200050982628e-06, "0": 0.26985808444757614, "1": 0.19496440014300007, "10": 1.122817189405796e-06, "11": 1.5283046837151307e-07, "12": 1.911707450326189e-08, "13": 2.2107541983523457e-09, "14": 2.357026163973013e-10, "15": 2.0769310712533013e-11, "2": 0.11552001870353694, "3": 0.050038661502696535, "4": 0.01721770117896579, "5": 0.0048902840433301025, "6": 0.001179490817717818, "7": 0.000246829197012482, "8": 4.5573651264880226e-05, "9": 7.52394162388661e-06} |
| Raw goal margin distribution | {"-1": 0.18890471274338366, "-10": 9.393696934268733e-07, "-11": 1.2578490678064082e-07, "-12": 1.5478580036736157e-08, "-13": 1.7609265407705822e-09, "-14": 1.8469548564438067e-10, "-15": 1.6010505970226315e-11, "-2": 0.11016812853985372, "-3": 0.0469456657051875, "-4": 0.015891177558570616, "-5": 0.004440236427455768, "-6": 0.0010535561120406183, "-7": 0.00021689559572455746, "-8": 3.9396634560490715e-05, "-9": 6.3985536081810434e-06, "0": 0.25382554030040944, "1": 0.1921196765150047, "10": 1.1064341749360813e-06, "11": 1.5060052052393085e-07, "12": 1.883813745886974e-08, "13": 2.1784971057799065e-09, "14": 2.3226348186015536e-10, "15": 2.0466265906005336e-11, "2": 0.11383446725685546, "3": 0.04930854788920824, "4": 0.016966477871902325, "5": 0.004818929957376635, "6": 0.0011622808788997342, "7": 0.00024322771464798103, "8": 4.490868657146883e-05, "9": 7.4141598663071265e-06} |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 36.8% |
| Raw p over 1 5 | 81.0% |
| Raw p under 3 5 | 64.3% |
| Raw p btts yes | 61.3% |
| P home draw | 65.4% |
| P draw away | 61.6% |
| P home away | 73.0% |
| Raw p home draw | 63.2% |
| Raw p draw away | 62.1% |
| Raw p home away | 74.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5759 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.9, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.76, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.67, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.93, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:55Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.9, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.58 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.96 |
| Market reference 1x2 last update utc | 2026-11-01T09:25:56Z |
| Market reference home last update utc | 2026-11-01T09:25:56Z |
| Market reference draw last update utc | 2026-11-01T09:25:56Z |
| Market reference away last update utc | 2026-11-01T09:25:56Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-11-01T09:25:09Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:25:09Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.7% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +5.1% |
| Under 2.5 probability edge | -5.1% |
| Raw edge prob home | -0.0080 |
| Raw edge prob draw | -0.0229 |
| Raw edge prob away | 0.0309 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05368766573640843, 0.06009027075343963, 0.05300264277484799, 0.028324932213886225, 0.011352761054708803, 0.003640190418591784, 0.000972669865635262, 0.000222771705885708, 4.46439540891547e-05, 7.952666176205806e-06, 1.2749858416546147e-06, 1.8582548983080264e-07, 2.482656584421979e-08, 3.0617230698722166e-09, 3.50614990410746e-10, 3.7474153425683604e-11], [0.06343430560503027, 0.1201133331665242, 0.07994480443045522, 0.042722986020983934, 0.017123566198760865, 0.005490562278944246, 0.0014670948109875867, 0.00033601042376934376, 6.733724946170725e-05, 1.1995144182870283e-05, 1.923083235597583e-06, 2.8028380595706385e-07, 3.744633941230232e-08, 4.6180499542430475e-09, 5.288386648537907e-10, 5.65229148957609e-11], [0.05297468977167706, 0.08492998188081621, 0.06847323667891762, 0.0322199100207266, 0.01291388579176199, 0.0041407551078918, 0.0011064222612782227, 0.0002534051719736311, 5.0782970030086417e-05, 9.046241900505194e-06, 1.4503098819658508e-06, 2.113784603858878e-07, 2.8240481268733707e-08, 3.4827423795670547e-09, 3.9882826047555147e-10, 4.2627245931642427e-11], [0.026634214143817957, 0.04270045439423489, 0.03422907084152406, 0.018397706103522447, 0.006492745895993723, 0.002081857557562565, 0.0005562786222511666, 0.00012740513714353443, 2.5532277857029755e-05, 4.5482011317724135e-06, 7.291758410981051e-07, 1.0627526472686025e-07, 1.4198535732399468e-08, 1.7510268912369027e-09, 2.005198584813904e-10, 2.1431804535296568e-11], [0.010043211665555, 0.016101458799610162, 0.012907075152299732, 0.006897618866316496, 0.0027805392082683312, 0.0007850254561758584, 0.00020976117103077853, 4.8041843949376525e-05, 9.627694267128646e-06, 1.7150326424971526e-06, 2.749571387394272e-07, 4.007420578288356e-08, 5.353974362879121e-09, 6.602760496634674e-10, 7.561189419749311e-11, 8.081490527954816e-12], [0.003029670033123228, 0.004857221856834325, 0.003893593016495584, 0.002080759609085634, 0.0008339778706569223, 0.0002689517310982496, 6.327728172496571e-05, 1.4492469122063974e-05, 2.9043236148483643e-06, 5.173626899273988e-07, 8.294452326332745e-08, 1.2088923783018423e-08, 1.6150984590872427e-09, 1.9918116115337748e-10, 2.2809346016623038e-11, 2.43789043692936e-12], [0.0007616173005929942, 0.001221038647291193, 0.0009787956346434526, 0.0005230742949987376, 0.00020965054532662487, 6.722311010271658e-05, 1.806579893390181e-05, 3.6432070459815445e-06, 7.301069381833004e-07, 1.30057851522476e-07, 2.0851110258256575e-08, 3.0389888661259536e-09, 4.0601349822041765e-10, 5.007139940260396e-11, 5.733955299271833e-12, 6.128520642234882e-13], [0.00016410865291432975, 0.00026310196394865914, 0.00021090491635982806, 0.00011270886028917656, 4.517422142264755e-05, 1.4484825955344069e-05, 3.870389209250491e-06, 8.915514723190018e-07, 1.5731899211766593e-07, 2.8024072979523098e-08, 4.492870124649745e-09, 6.548227944051041e-10, 8.748531343249303e-11, 1.0789079894979866e-11, 1.2355177322020234e-12, 1.320536266930595e-13], [3.094099057077435e-05, 4.960515634685858e-05, 3.9763942440170905e-05, 2.1250090848473643e-05, 8.517132608539999e-06, 2.73096424438735e-06, 7.297218879199605e-07, 1.6712904916397126e-07, 3.368618091602344e-08, 5.28364935313172e-09, 8.470842316588357e-10, 1.2346007079707913e-10, 1.6494451754528076e-11, 2.0341695173877942e-12, 2.329441002848503e-13, 2.4897346640700734e-14], [5.185425796329732e-06, 8.313368531740984e-06, 6.664071482177906e-06, 3.561320023286761e-06, 1.427393186978343e-06, 4.5768452077537633e-07, 1.2229468520444648e-07, 2.8009293395716502e-08, 5.6131257937647026e-09, 1.0056621086201266e-09, 1.4196353592689607e-10, 2.0690773763803487e-11, 2.7643185963488543e-12, 3.409081252729358e-13, 3.9039291387808096e-14, 4.172566590443906e-15], [7.82126757220753e-07, 1.2539197795316729e-06, 1.0051534479448696e-06, 5.371600695183282e-07, 2.1529618751859522e-07, 6.903334926083607e-08, 1.8445919259318683e-08, 4.224690252272464e-09, 8.466374888744405e-10, 1.5081606140517087e-10, 2.431853543091601e-11, 3.120825255994622e-12, 4.169469633945316e-13, 5.141976319835717e-14, 5.8883639601890144e-15, 6.293554482992407e-16], [1.0724503083476592e-07, 1.719371753730215e-07, 1.3782639645467758e-07, 7.365525816225014e-08, 2.9521360899461424e-08, 9.465836070374868e-09, 2.529299965098732e-09, 5.792885004756536e-10, 1.1609072667818322e-10, 2.067986168028562e-11, 3.315432870629981e-12, 4.860012375462396e-13, 5.717166627133785e-14, 7.050665430907541e-15, 8.07411034907935e-16, 8.629706609031107e-17], [1.347996151286897e-08, 2.1611318385750272e-08, 1.7323828481423634e-08, 9.257958504178067e-09, 3.7106316780809886e-09, 1.1897903793078673e-09, 3.179155800380367e-10, 7.281257351019372e-11, 1.4591804538095234e-11, 2.599316139609299e-12, 4.167270702122352e-13, 6.073676225882475e-14, 8.16131634781194e-15, 8.862200692093894e-16, 1.0148600444148887e-16, 1.0846946665185714e-17], [1.5640045773888318e-09, 2.5074404586728737e-09, 2.009986973403383e-09, 1.0741491705289488e-09, 4.305238500853486e-10, 1.3804472643295054e-10, 3.688596751022105e-11, 8.448035860687457e-12, 1.6930055080763279e-12, 3.015841207371797e-13, 4.835051232984247e-14, 7.046946988527542e-15, 9.41482751212989e-16, 1.167774094618178e-16, 1.1774853758733785e-17, 1.25851058393952e-18], [1.685010858782253e-10, 2.701439920123289e-10, 2.165498698124053e-10, 1.1572555748622026e-10, 4.638332731542907e-11, 1.487251804758101e-11, 3.973981706318224e-12, 9.101656329168932e-13, 1.823992529388583e-13, 3.24917539005455e-14, 5.209136819758488e-15, 7.592165885317436e-16, 1.0143248185364324e-16, 1.2509107045830093e-17, 1.4407482298486313e-18, 1.355880942094759e-19], [1.6943540487313893e-11, 2.7164190914314973e-11, 2.1775061374623382e-11, 1.1636724229194599e-11, 4.6640517490389845e-12, 1.495498443669433e-12, 3.996016974365908e-13, 9.152123958793966e-14, 1.8341063565957258e-14, 3.2671916910707207e-15, 5.238020879777671e-16, 7.634263565354428e-17, 1.0199491321129978e-17, 1.2578468594816034e-18, 1.4404306154107386e-19, 1.5484276069039128e-20]] |
| Legacy trial inputs | {"lambda_home": 1.5083173261766571, "lambda_away": 1.6032181074937424, "rho": -0.060463437633334456, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3703 |
| Legacy p draw | 0.2637 |
| Legacy p away | 0.3660 |
| Legacy p over 1 5 | 0.8228 |
| Legacy p under 3 5 | 0.6231 |
| Legacy p btts yes | 0.6316 |
| Legacy p over 2 5 | 0.5967 |
| Legacy goal margin distribution | {"-1": 0.17959983979334587, "-10": 1.5853392055562837e-06, "-11": 2.2696317297168137e-07, "-12": 2.9864875863473684e-08, "-13": 3.6331889806576495e-09, "-14": 4.071379053065069e-10, "-15": 3.7474153425683604e-11, "-2": 0.11094638478451958, "-3": 0.05019661298735254, "-4": 0.01808731731180625, "-5": 0.00538802378512381, "-6": 0.0013642989236686818, "-7": 0.00029992611372507504, "-8": 5.8201242440250656e-05, "-9": 1.0102010106169422e-05, "0": 0.26374042469180137, "1": 0.19039622146002405, "10": 9.725097890714862e-07, "11": 1.3098672580315483e-07, "12": 1.6215588565583442e-08, "13": 1.8559236307757841e-09, "14": 1.9566527679254027e-10, "15": 1.6943540487313893e-11, "2": 0.1108878728975018, "3": 0.04720037207870409, "4": 0.0160009318745577, "5": 0.004484362717997521, "6": 0.0010682696155779822, "7": 0.00022094578977863751, "8": 4.0337020550529916e-05, "9": 6.586875726790091e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3541 |
| Legacy raw p draw | 0.2508 |
| Legacy raw p away | 0.3951 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5083 |
| Legacy lambda away | 1.6032 |
| Legacy model home team | Paris FC |
| Legacy model away team | Monaco |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 67.1% |
| Market reference home draw last update utc | 2026-11-01T09:25:56Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.6% |
| Market reference draw away last update utc | 2026-11-01T09:25:56Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.3% |
| Market reference home away last update utc | 2026-11-01T09:25:56Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.55 |
| Market reference dc home draw odds | 1.40 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 78.0% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-11-01T09:25:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 69.4% |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 2.98 |
| Market reference under 3 5 last update utc | 2026-11-01T09:25:55Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.8% |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-11-01T09:25:56Z |
| Market btts yes bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 8.959867238398926, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,504.1286 |
| Elo away rating | 1,558.3951 |
| Elo rating diff | 5.7335 |
| Elo home expectancy | 0.5083 |

</details>


---

## 2026-11-01 — Strasbourg vs Auxerre

The model's most likely 1X2 outcome is **Strasbourg win** at **52.4%**. Expected goals are 1.82 for Strasbourg and 1.12 for Auxerre (2.94 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 56.1%; Under 3.5 goals: 66.2%; Double Chance 1X: 76.8%; Double Chance X2: 47.6%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 82.6%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 52.4% | 1.91 |
| Draw | 24.5% | 4.09 |
| Auxerre win | 23.2% | 4.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.82 |
| Auxerre expected goals | 1.12 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 79.7% |
| Under 1.5 | 20.3% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 33.8% |
| Under 3.5 | 66.2% |
| Over 4.5 | 17.4% |
| Under 4.5 | 82.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.51% |
| 2 | 2-1 | 9.64% |
| 3 | 1-0 | 8.91% |
| 4 | 2-0 | 8.63% |
| 5 | 1-2 | 6.17% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | 448a1083448ea9dff55bfebf15ff20b4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 11.00 |
| Matched home-team name | Strasbourg |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8217 |
| Dc lambda away | 1.1175 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:25:32.352914+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.81 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.92 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 2.96 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.75 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.14125627876500157, "-10": 5.450501557421662e-08, "-11": 5.4539467266712626e-09, "-12": 5.014063039679963e-10, "-13": 4.2627159943285086e-11, "-14": 3.3690179612963583e-12, "-15": 2.472276809098726e-13, "-16": 1.5317740046462208e-14, "-2": 0.06352999777636219, "-3": 0.020491145164912846, "-4": 0.005225032239758796, "-5": 0.0010966598654048173, "-6": 0.00019511086214029274, "-7": 3.0082658335779948e-05, "-8": 4.088903343742273e-06, "-9": 4.966520249285389e-07, "0": 0.24454161373562813, "1": 0.22440260356946076, "10": 6.930384133209744e-06, "11": 1.130515452048363e-06, "12": 1.6943384764431224e-07, "13": 2.3482349853307046e-08, "14": 3.0255424741096698e-09, "15": 3.6194434451373775e-10, "16": 3.655814635579844e-11, "2": 0.16193528933128803, "3": 0.08514784553270818, "4": 0.03539493998898065, "5": 0.01211069112449291, "6": 0.003512555525560125, "7": 0.0008828821444248887, "8": 0.00019563120912693206, "9": 3.873720458930255e-05} |
| Raw goal margin distribution | {"-1": 0.13785151563763284, "-10": 5.3191256859161663e-08, "-11": 5.322487814713822e-09, "-12": 4.89320684054275e-10, "-13": 4.159969848338921e-11, "-14": 3.2878130178393107e-12, "-15": 2.412686417833557e-13, "-16": 1.4948529722073172e-14, "-2": 0.06199870588759151, "-3": 0.019997237948150302, "-4": 0.005099090955840085, "-5": 0.0010702265832481547, "-6": 0.00019040801795543665, "-7": 2.935756259652936e-05, "-8": 3.99034668163942e-06, "-9": 4.846809995242602e-07, "0": 0.24097057661417842, "1": 0.22832767726470088, "10": 7.051604956972383e-06, "11": 1.1502895384106187e-06, "12": 1.7239745113149797e-07, "13": 2.389308463198403e-08, "14": 3.078462881404694e-09, "15": 3.682751900707593e-10, "16": 3.719759267382418e-11, "2": 0.1647677339392161, "3": 0.08663718461964684, "4": 0.036014040416896785, "5": 0.012322521800286344, "6": 0.0035739943817816784, "7": 0.0008983248239034565, "8": 0.00019905303623899787, "9": 3.941476527862645e-05} |
| Unadjusted home-win probability | 53.3% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 57.0% |
| P home draw | 76.8% |
| P draw away | 47.6% |
| P home away | 75.5% |
| Raw p home draw | 77.4% |
| Raw p draw away | 46.7% |
| Raw p home away | 75.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5614 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.6, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.05, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.6, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.98, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 4.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 7.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:26:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.6, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.91 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-11-01T09:25:56Z |
| Market reference home last update utc | 2026-11-01T09:25:56Z |
| Market reference draw last update utc | 2026-11-01T09:25:56Z |
| Market reference away last update utc | 2026-11-01T09:25:56Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-01T09:25:09Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:25:09Z |
| Home probability edge | +0.4% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0131 |
| Raw edge prob draw | -0.0051 |
| Raw edge prob away | -0.0080 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.06778649844568832, 0.059193246958785604, 0.03415985150849162, 0.011743592946062021, 0.0030279400200667215, 0.0006245734713205361, 0.0001073590236519912, 1.581782561164427e-05, 2.039215230803569e-06, 2.3368284250312584e-07, 2.410089089661217e-08, 2.2596786458265704e-09, 1.9421005239805707e-10, 1.5407586801553627e-11, 1.135044418405187e-12, 7.804190613730683e-14, 5.030534775872892e-15], [0.09950645778601462, 0.11758592842291753, 0.06012493129316081, 0.020669958674770745, 0.005329492887902853, 0.0010993149967687423, 0.00018896317272258027, 2.7841036658806778e-05, 3.589233273263885e-06, 4.1130637954905347e-07, 4.2420102701633705e-08, 3.9772720701426855e-09, 3.4183011755691184e-10, 2.711897320767156e-11, 1.997797550564089e-12, 1.373619625754653e-13, 8.85427027374597e-15], [0.0933949293721041, 0.09632290411153195, 0.0503204539758985, 0.018190650577683688, 0.004690233996375727, 0.0009674550053859485, 0.00016629752875328729, 2.450157629966589e-05, 3.1587140227537655e-06, 3.619712428298775e-07, 3.733192106749255e-08, 3.500208569292105e-09, 3.008284788201342e-10, 2.3866122492467465e-11, 1.7581669000442142e-12, 1.208857503389695e-13, 7.792223448742382e-15], [0.05479496605570697, 0.05651281388253811, 0.02914225852129863, 0.010149553332796418, 0.0027517683706444755, 0.0005676075193476271, 9.756704678130041e-05, 1.4375117050546361e-05, 1.8532229621041452e-06, 2.1236915213010946e-07, 2.1902702442629413e-08, 2.0535784012225177e-09, 1.7649658708840727e-10, 1.400229520647516e-11, 1.0315195509636032e-12, 7.092387810532448e-14, 4.571710929521349e-15], [0.02411122577985655, 0.024867123990762505, 0.012823359982149259, 0.004408459439402044, 0.001151520930412269, 0.00024976223252737187, 4.293206589864743e-05, 6.3254294649114004e-06, 8.154668298230243e-07, 9.344801072565802e-08, 9.637764959035886e-09, 9.036284909488689e-10, 7.766313891565011e-11, 6.1613780509745e-12, 4.538957240038169e-13, 3.120837115661281e-14, 2.011673012259245e-15], [0.008487658636615521, 0.008753750706623764, 0.0045140924437714995, 0.0015518704514089867, 0.0004001305790623461, 8.361356034175398e-05, 1.5112990241119526e-05, 2.226684222459177e-06, 2.8706147684964576e-07, 3.289566538640286e-08, 3.392695988960129e-09, 3.180962359823934e-10, 2.733905848597675e-11, 2.1689346740511568e-12, 1.5978084221592702e-13, 1.0986003092527276e-14, 7.081512143946306e-16], [0.002489861976514804, 0.002567920314594931, 0.0013242129090504065, 0.0004552425344689474, 0.00011737865023815939, 2.421170516995606e-05, 4.216179619723262e-06, 6.531997358245875e-07, 8.42097316504618e-08, 9.649971793684054e-09, 9.952502925064053e-10, 9.331380499073183e-11, 8.01993637023687e-12, 6.362588560250947e-13, 4.6871847778221307e-14, 3.222753475965081e-15, 2.0773676909408016e-16], [0.0006260598486927278, 0.0006456871179102991, 0.00033296485560115356, 0.00011446781987773714, 2.9514109898863212e-05, 6.087878211029624e-06, 1.0464560069554158e-06, 1.5619528270638468e-07, 2.1173997736749596e-08, 2.4264236082272694e-09, 2.502493123775966e-10, 2.3463158674849118e-11, 2.016561639896165e-12, 1.5998321468808957e-13, 1.1785625952269458e-14, 8.103407227258668e-16, 5.223408022359615e-17], [0.00013774139715851702, 0.00014205965441471986, 7.325664552830392e-05, 2.518442521521206e-05, 6.49349218265346e-06, 1.339413240234286e-06, 2.3023407868104042e-07, 3.3921717826340717e-08, 4.430296865549537e-09, 5.338450925954045e-10, 5.5058138605796694e-11, 5.162203365020295e-12, 4.4367007134472135e-13, 3.519841043801537e-14, 2.592992648295558e-15, 1.782856120796936e-16, 1.149218434038153e-17], [2.6937705049973722e-05, 2.778221470863234e-05, 1.4326600070136631e-05, 4.925248562128113e-06, 1.2699143523230417e-06, 2.619453523034763e-07, 4.502624361233162e-08, 6.63397677419232e-09, 8.552443812992479e-10, 9.92870708611135e-11, 1.0767568276200072e-11, 1.0095578709345195e-12, 8.676733188375317e-14, 6.883656026198121e-15, 5.071044188418628e-16, 3.4866825311273936e-17, 2.2474947875318726e-18], [4.741319396316715e-06, 4.889961978063999e-06, 2.521632287152743e-06, 8.668955464460333e-07, 2.2351828187145774e-07, 4.6105136920440785e-08, 7.925092422921075e-09, 1.1676496826972025e-09, 1.505320058305772e-10, 1.7250139405993316e-11, 1.802343594316934e-12, 1.776928029424212e-13, 1.5271962955414794e-14, 1.2115958569610013e-15, 8.925571100256685e-17, 6.136927953945765e-18, 3.955827198151009e-19], [7.586564353228011e-07, 7.824406695790242e-07, 4.0348527535443674e-07, 1.3871157584845967e-07, 3.576506216514544e-08, 7.377262720014987e-09, 1.2680905597390846e-09, 1.8683511316892635e-10, 2.4086560174396698e-11, 2.7601872341143738e-12, 2.846720395517373e-13, 2.7039403455432096e-14, 2.4436600886111046e-15, 1.9386692122196496e-16, 1.428176713722625e-17, 9.819671480031928e-19, 6.329701734993084e-20], [1.1127625959175767e-07, 1.1476482240103586e-07, 5.918137664341874e-08, 2.034558016492329e-08, 5.2458559059223e-09, 1.0820631886681261e-09, 1.8599772932967142e-10, 2.7404120740101278e-11, 3.532906593612738e-12, 4.048516520583922e-13, 4.175439407983914e-14, 3.914855806633387e-15, 3.4086271805764354e-16, 2.843551421661797e-17, 2.0947843495387e-18, 1.4403045460925674e-19, 9.284117297466768e-21], [1.506599384289392e-08, 1.5538319799912576e-08, 8.012726698352972e-09, 2.754643143285017e-09, 7.102506237115485e-10, 1.4650346262450826e-10, 2.5182735788871202e-11, 3.7103180485666595e-12, 4.783297819513641e-13, 5.4813960494130066e-14, 5.653240380549407e-15, 5.300429192618629e-16, 4.5555001067601413e-17, 3.6613199924350945e-18, 2.8361852050136903e-19, 1.9500672922447915e-20, 1.2570017589870524e-21], [1.894123833902331e-09, 1.9535055024393676e-09, 1.0073744070361728e-09, 3.4631868869724457e-10, 8.929398541142841e-11, 1.8418678727735242e-11, 3.1660188207938334e-12, 4.66467856049394e-13, 6.013648020218183e-14, 6.891309666337261e-15, 7.107355449125089e-16, 6.663794880273352e-17, 5.727256640044912e-18, 4.543699089035886e-19, 3.390989965309341e-20, 2.4516596611357372e-21, 1.5803252117201157e-22], [2.222571436838278e-10, 2.2922500914224968e-10, 1.1820566022168252e-10, 4.0637154327760456e-11, 1.0477787032963774e-11, 2.1612541118933004e-12, 3.715017399412347e-13, 5.473549904720919e-14, 7.0564353194370886e-15, 8.086286520799096e-16, 8.339795387156749e-17, 7.819319886457018e-18, 6.720382686585508e-19, 5.331592175826027e-20, 3.927671489589716e-21, 2.735828537665331e-22, 1.854359051724834e-23], [2.4449746748171683e-11, 2.5216257749843234e-11, 1.3003399615050766e-11, 4.4703540926158655e-12, 1.152625446323874e-12, 2.377521586860962e-13, 4.086763335260682e-14, 6.021264683140235e-15, 7.762542685715459e-16, 8.89544670149912e-17, 9.174323118163506e-18, 8.601765855444474e-19, 7.392862700132378e-20, 5.865101850175768e-21, 4.320696812656389e-22, 2.97076845305202e-23, 1.939964572727184e-24]] |
| Legacy trial inputs | {"lambda_home": 1.7601051713651232, "lambda_away": 1.0313504679441665, "rho": -0.060463437633334456, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5288 |
| Legacy p draw | 0.2471 |
| Legacy p away | 0.2241 |
| Legacy p over 1 5 | 0.7735 |
| Legacy p under 3 5 | 0.6946 |
| Legacy p btts yes | 0.5398 |
| Legacy p over 2 5 | 0.5284 |
| Legacy goal margin distribution | {"-1": 0.14052614734156943, "-10": 2.839345883024533e-08, "-11": 2.6264383219492845e-09, "-12": 2.231601280568904e-10, "-13": 1.7530841813386207e-11, "-14": 1.2801986044293946e-12, "-15": 8.68961764110528e-14, "-16": 5.030534775872892e-15, "-2": 0.06013289714134525, "-3": 0.018144730282545186, "-4": 0.004308777044298602, "-5": 0.0008399883793776795, "-6": 0.00013858110752942472, "-7": 1.9791864445955113e-05, "-8": 2.4899869895886074e-06, "-9": 2.797859747950208e-07, "0": 0.24708194557437085, "1": 0.2298055033929875, "10": 5.5857875817895996e-06, "11": 8.817910186500787e-07, "12": 1.278637435784805e-07, "13": 1.7142175359647584e-08, "14": 2.1363522426596314e-09, "15": 2.4747340143367106e-10, "16": 2.4449746748171683e-11, "2": 0.16440667723803953, "3": 0.08466232476623946, "4": 0.034310420768459395, "5": 0.011415045547496045, "6": 0.003213962073829128, "7": 0.0007833498715057332, "8": 0.00016818935131104968, "9": 3.225222693038253e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5379 |
| Legacy raw p draw | 0.2481 |
| Legacy raw p away | 0.2140 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7601 |
| Legacy lambda away | 1.0314 |
| Legacy model home team | Strasbourg |
| Legacy model away team | Auxerre |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 75.7% |
| Market reference home draw last update utc | 2026-11-01T09:25:56Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.5% |
| Market reference draw away last update utc | 2026-11-01T09:25:56Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.7% |
| Market reference home away last update utc | 2026-11-01T09:25:56Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.7% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-11-01T09:26:04Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.2% |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-11-01T09:26:04Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 60.5% |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-11-01T09:25:56Z |
| Market btts yes bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.310538983395414, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,524.8199 |
| Elo away rating | 1,446.2294 |
| Elo rating diff | 138.5904 |
| Elo home expectancy | 0.6895 |

</details>


---

## 2026-11-02 — Lorient vs Brest

The model's most likely 1X2 outcome is **Lorient win** at **39.9%**. Expected goals are 1.49 for Lorient and 1.29 for Brest (2.78 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 51.9%; Under 3.5 goals: 69.8%; Double Chance 1X: 68.3%; Double Chance X2: 60.1%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 39.9% | 2.51 |
| Draw | 28.4% | 3.53 |
| Brest win | 31.7% | 3.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.49 |
| Brest expected goals | 1.29 |
| Expected total goals | 2.78 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.43% |
| 2 | 2-1 | 8.60% |
| 3 | 1-0 | 8.34% |
| 4 | 1-2 | 7.57% |
| 5 | 0-0 | 7.32% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T19:45:00+00:00 |
| Fixture id | 5118966f484adf525196d196a61bc5d6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 14.00 |
| Matched home-team name | Lorient |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4862 |
| Dc lambda away | 1.2928 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:25:32.352914+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.67 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.36 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.82 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.17670887570769095, "-10": 2.6040233189162496e-07, "-11": 3.017075267429088e-08, "-12": 3.211245321746044e-09, "-13": 3.159460788429419e-10, "-14": 2.8718923591722505e-11, "-15": 2.194161347482099e-12, "-2": 0.09242952184674039, "-3": 0.03473190539780167, "-4": 0.010293706372655314, "-5": 0.0025077626142906723, "-6": 0.0005174387835541157, "-7": 9.247246413776603e-05, "-8": 1.4563043878149362e-05, "-9": 2.048917380813416e-06, "0": 0.28350660491865237, "1": 0.2019006300072904, "10": 1.0383254954913078e-06, "11": 1.3829516114113137e-07, "12": 1.6921019093624695e-08, "13": 1.9138072333494974e-09, "14": 1.9997954276114192e-10, "15": 1.7563787097558548e-11, "2": 0.12084865676242461, "3": 0.05220257447145832, "4": 0.017785549147236002, "5": 0.004980972199108091, "6": 0.0011814595641443926, "7": 0.00024271940935758526, "8": 4.3941656528465346e-05, "9": 7.106911454545833e-06} |
| Raw goal margin distribution | {"-1": 0.1801440168016928, "-10": 2.6546443614458e-07, "-11": 3.075725854126195e-08, "-12": 3.273670486998628e-09, "-13": 3.2208792856370773e-10, "-14": 2.9277206554082666e-11, "-15": 2.2368148575642646e-12, "-2": 0.0942263101943721, "-3": 0.035407078022986226, "-4": 0.010493811396405164, "-5": 0.002556512392001903, "-6": 0.0005274975608616989, "-7": 9.427008726422806e-05, "-8": 1.4846142903476958e-05, "-9": 2.088747413486418e-06, "0": 0.2652134639851591, "1": 0.2080330869054763, "10": 1.0698632195051366e-06, "11": 1.4249568847428058e-07, "12": 1.7434972023148925e-08, "13": 1.9719365238303073e-09, "14": 2.0605364924836463e-10, "15": 1.8097263230549332e-11, "2": 0.12451927026557451, "3": 0.0537881566358577, "4": 0.018325761000720826, "5": 0.005132262451748659, "6": 0.0012173447907224543, "7": 0.00025009168113397743, "8": 4.527632455147237e-05, "9": 7.322774219177388e-06} |
| Unadjusted home-win probability | 41.1% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 32.3% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.8% |
| P home draw | 68.3% |
| P draw away | 60.1% |
| P home away | 71.6% |
| Raw p home draw | 67.7% |
| Raw p draw away | 58.9% |
| Raw p home away | 73.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5191 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:25:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.52 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.15 |
| Market reference 1x2 last update utc | 2026-11-01T09:25:56Z |
| Market reference home last update utc | 2026-11-01T09:25:56Z |
| Market reference draw last update utc | 2026-11-01T09:25:56Z |
| Market reference away last update utc | 2026-11-01T09:25:56Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-11-01T09:25:09Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:25:09Z |
| Home probability edge | +0.5% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +5.9% |
| Under 2.5 probability edge | -5.9% |
| Raw edge prob home | 0.0173 |
| Raw edge prob draw | -0.0261 |
| Raw edge prob away | 0.0088 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0731301813147352, 0.07430694028587038, 0.05622298417252379, 0.025997055647896127, 0.009015622066848084, 0.002501250675556899, 0.0005782790966969723, 0.00011459640123625459, 1.9870670312823756e-05, 3.0626793738442296e-06, 4.2484749227738106e-07, 5.3576199037839116e-08, 6.193300872804525e-09, 6.608613478474639e-10, 6.548077962010854e-11], [0.08284272210658303, 0.13288840308896868, 0.07747801172349487, 0.03582520942117451, 0.012423966505342813, 0.0034468453074197212, 0.0007968967726056016, 0.00015791942475354916, 2.7382751913816668e-05, 4.2205214099605385e-06, 5.854605455725804e-07, 7.383061284005233e-08, 8.534670378894266e-09, 9.106991386123009e-10, 9.023570494768734e-11], [0.062306514391679, 0.08643009326380674, 0.05988630130157554, 0.024684442104790365, 0.008560415608672668, 0.0023749603926915734, 0.0005490812912108406, 0.00010881033106387865, 1.8867383197680283e-05, 2.908042076499984e-06, 4.033965795405404e-07, 5.0871090990309565e-08, 5.880595822191233e-09, 6.274938939692818e-10, 6.217459913157178e-11], [0.028620470930983615, 0.039701626643222084, 0.027536569225551005, 0.012719823379261185, 0.003932223275161651, 0.001090937047994203, 0.0002522202579822943, 4.998197937422001e-05, 8.666724460918535e-06, 1.335807893109493e-06, 1.8530004753307363e-07, 2.336761404695139e-08, 2.7012491940708683e-09, 2.8823905376603735e-10, 2.8559875712263497e-11], [0.009860100877597868, 0.013677694006184665, 0.009486683536466837, 0.0043865661604642215, 0.0015196976703648972, 0.0003758411023449217, 8.689295131013805e-05, 1.7219400752707605e-05, 2.9857921509771922e-06, 4.60202091395091e-07, 6.383812361807961e-08, 8.050427693077627e-09, 9.306132527761776e-10, 9.930186522262126e-11, 9.839225086604728e-12], [0.0027175398909640523, 0.0037697057605826515, 0.0026146224327048906, 0.0012089803819855718, 0.00041926710308433065, 0.00011620191585127577, 2.39485441741672e-05, 4.745834654724086e-06, 8.229134140851333e-07, 1.2683618117058474e-07, 1.759440898729323e-08, 2.218776325601849e-09, 2.5648608151919735e-10, 2.7368561776352944e-11, 2.711786319526647e-12], [0.0006241503975346127, 0.0008658063702687722, 0.0006005128521578932, 0.00027767231257096723, 9.629508289220986e-05, 2.6715643063901527e-05, 6.170308625827217e-06, 1.0899985668025517e-06, 1.890024636788655e-07, 2.9131072983553788e-08, 4.040992148935816e-09, 5.095969815455047e-10, 5.890838632198011e-11, 6.285868615750619e-12, 6.228289472361861e-13], [0.0001228728086135971, 0.00017044619510086663, 0.00011821942442824488, 5.466371094946761e-05, 1.895704518875808e-05, 5.259351127783117e-06, 1.21594082876538e-06, 2.4071707991822214e-07, 3.7207800617997224e-08, 5.734862574077644e-09, 7.955262976463997e-10, 1.0032135304381534e-10, 1.1596946676422012e-11, 1.237461891307232e-12, 1.2261266248495198e-13], [2.1165589674701532e-05, 2.936039525607335e-05, 2.0364015906044213e-05, 9.416157155578262e-06, 3.2654664969188913e-06, 9.059552653012102e-07, 2.0945321378058408e-07, 4.150692055742865e-08, 7.1899030092902705e-09, 9.878650081601368e-10, 1.3703425014372876e-10, 1.728096409689535e-11, 1.997644699442312e-12, 2.131603478834341e-13, 2.112077791955007e-14], [3.240801543446221e-06, 4.495561698231561e-06, 3.1180673533491867e-06, 1.441769263797302e-06, 4.999968829564821e-07, 1.3871672215164943e-07, 3.2070748272665844e-08, 6.355395444852463e-09, 1.1020064001131334e-09, 1.6968135061221213e-10, 2.0982208206635013e-11, 2.646001173517833e-12, 3.058724148350997e-13, 3.263837176470767e-14, 3.2339401232121807e-15], [4.465982438892925e-07, 6.1951030719123e-07, 4.2968487445654935e-07, 1.986828297485715e-07, 6.890200676744727e-08, 1.9115840226713837e-08, 4.419505380621837e-09, 8.758044597432842e-10, 1.518618515967309e-10, 2.3406566222325225e-11, 3.2436218087767232e-12, 3.646318546755163e-13, 4.215070916507649e-14, 4.497726663640179e-15, 4.456527067479314e-16], [5.594855828416401e-08, 7.761048997344681e-08, 5.382969944753141e-08, 2.489042004161159e-08, 8.631847514563886e-09, 2.394778115921535e-09, 5.536630691189909e-10, 1.0971829274282713e-10, 1.9024821014090137e-11, 2.932308069815285e-12, 4.06762699577678e-13, 5.124375437741363e-14, 5.280521006763568e-15, 5.634624090669076e-16, 5.583010407932303e-17], [6.424986623133155e-09, 8.912586404131619e-09, 6.1816623963938725e-09, 2.8583509694616148e-09, 9.912588727008486e-10, 2.750100776863617e-10, 6.358122392975468e-11, 1.2599762796483028e-11, 2.184760863759907e-12, 3.3673861670893497e-13, 4.671156833572664e-14, 5.8906509465532145e-15, 6.802593944737818e-16, 6.470655459084377e-17, 6.4113836509583996e-18], [6.810726640014643e-10, 9.447675647369752e-10, 6.552793839462592e-10, 3.0299591635150475e-10, 1.0507715591417562e-10, 2.915209901958706e-11, 6.739848049861726e-12, 1.3356220824943168e-12, 2.3159284041613826e-13, 3.569555552510747e-14, 4.95160132653874e-15, 6.244310795024356e-16, 7.218297712679032e-17, 7.694562700811416e-18, 6.796306979646726e-19], [6.703937979240287e-11, 9.299540994029598e-11, 6.450049431202925e-11, 2.9824509755675617e-11, 1.034296006163126e-11, 2.8695009229083235e-12, 6.634170728613984e-13, 1.3146802210705676e-13, 2.279615848130041e-14, 3.513586773089662e-15, 4.873962786292107e-16, 6.14640324088149e-17, 7.10511854890541e-18, 7.581576153459785e-19, 7.504538171859523e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3780487262246464, "lambda_away": 1.387175869291597, "rho": -0.060463437633334456, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3787 |
| Legacy p draw | 0.2803 |
| Legacy p away | 0.3411 |
| Legacy p over 1 5 | 0.7697 |
| Legacy p under 3 5 | 0.7002 |
| Legacy p btts yes | 0.5710 |
| Legacy p over 2 5 | 0.5183 |
| Legacy goal margin distribution | {"-1": 0.18080253525142095, "-10": 5.048567792184773e-07, "-11": 6.276692318641491e-08, "-12": 7.166174610548398e-09, "-13": 7.510970527951512e-10, "-14": 6.548077962010854e-11, "-2": 0.10179137991337925, "-3": 0.04106627506227027, "-4": 0.013064647416529246, "-5": 0.0034161028215980026, "-6": 0.0007564678296082238, "-7": 0.0001450808085963602, "-8": 2.4518914521015283e-05, "-9": 3.7018142732527325e-06, "0": 0.2802670270593424, "1": 0.20164319207612824, "10": 5.307037351355462e-07, "11": 6.554624858199758e-08, "12": 7.43425468218216e-09, "13": 7.740680739417602e-10, "14": 6.703937979240287e-11, "2": 0.11280557535082422, "3": 0.04521035564881751, "4": 0.014288391915951569, "5": 0.0037115015220377696, "6": 0.0008164737395298464, "7": 0.00015555886778167652, "8": 2.6116747741820046e-05, "9": 3.917107847711281e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3633 |
| Legacy raw p draw | 0.2692 |
| Legacy raw p away | 0.3675 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3780 |
| Legacy lambda away | 1.3872 |
| Legacy model home team | Lorient |
| Legacy model away team | Brest |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 67.7% |
| Market reference home draw last update utc | 2026-11-01T09:25:56Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.0% |
| Market reference draw away last update utc | 2026-11-01T09:25:56Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.3% |
| Market reference home away last update utc | 2026-11-01T09:25:56Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.53 |
| Market reference dc home draw odds | 1.40 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 72.7% |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.20 |
| Market reference over 1 5 last update utc | 2026-11-01T09:25:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 76.7% |
| Market reference under 3 5 odds | 1.25 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market reference under 3 5 last update utc | 2026-11-01T09:25:32Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 53.7% |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-11-01T09:25:56Z |
| Market btts yes bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.147035869889242, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,498.9880 |
| Elo away rating | 1,450.3969 |
| Elo rating diff | 108.5911 |
| Elo home expectancy | 0.6514 |

</details>


---
