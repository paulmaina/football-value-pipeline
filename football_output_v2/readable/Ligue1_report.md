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
| Training as of utc | 2026-11-01T12:21:43.479248+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 76, 'bbs_added_results': 4, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 76, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 134, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-01T12:21:43.479248+00:00', 'observations': 462, 'observations_sha256': 'fad4edfd2cff03c9620cae8d9fa11469dc7b5cfbfd352bf74a0a68c8c62cd190', 'eligible_training_matches': 176, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 173, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 19, 'retrospective_eligible_training_matches': 176, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'c4783747d26d9f9fbf43cad53b735a1f684b3a12eed1526f37dd9a5b35168d9c', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 116, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-08-31T00:00:00+00:00', 'audit_origin_utc': '2025-10-04T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 27, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1750, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1465, 'tuning_matches': 188, 'audit_matches': 92, 'audit_matchdays': 31, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8740131822125641, 'audit_candidate_poisson_score': 0.8703668995733247, 'audit_gain': 0.0036462826392393843, 'audit_gain_lower95': -0.002086746289812877, 'audit_baseline_briers': [0.5996494886895843, 0.17689503454482072, 0.21631319722829082, 0.2479498473885013], 'audit_candidate_briers': [0.5975481546017649, 0.1756267427737864, 0.21497744296289117, 0.24618847014565895], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1591.655 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.196 |
| Dixon-Coles low-score adjustment | -0.053 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1756, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-31'} |
| Training data health | {'training_end': '2026-10-31', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261101T122143479248Z_ca0cf59994ccefc46a0a698130d242bd657ad0d7318efe701dd84b8dfbab0f59.json |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
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

## 2026-11-01 — Olympique Lyonnais vs Angers SCO

The model's most likely 1X2 outcome is **Olympique Lyonnais win** at **67.5%**. Expected goals are 2.05 for Olympique Lyonnais and 0.74 for Angers SCO (2.79 combined). The most likely exact score is 2-0 at 12.9%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 52.8%; Under 3.5 goals: 69.5%; Double Chance 1X: 88.1%; Double Chance X2: 32.5%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Olympique Lyonnais win | 67.5% | 1.48 |
| Draw | 20.6% | 4.85 |
| Angers SCO win | 11.9% | 8.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Olympique Lyonnais expected goals | 2.05 |
| Angers SCO expected goals | 0.74 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 52.8% |
| Under 2.5 | 47.2% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.94% |
| 2 | 1-0 | 12.13% |
| 3 | 1-1 | 9.80% |
| 4 | 2-1 | 9.54% |
| 5 | 3-0 | 8.84% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:15:00+00:00 |
| Fixture id | fdorg:559640 |
| Matched home-team name | Lyon |
| Matched away-team name | Angers |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.0503 |
| Dc lambda away | 0.7373 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T12:21:43.479248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.04 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.65 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.08458647884853714, "-10": 9.228420718127684e-10, "-11": 6.115777312671002e-11, "-12": 3.721617771092694e-12, "-13": 2.0933259291419231e-13, "-14": 1.094528968446749e-14, "-15": 5.345559106937399e-16, "-16": 2.441260277277759e-17, "-17": 9.722684928103254e-19, "-2": 0.02692956120766975, "-3": 0.005922122840407641, "-4": 0.001018144719472114, "-5": 0.00014315688622932785, "-6": 1.6994548411242617e-05, "-7": 1.743775590259594e-06, "-8": 1.5744836345951489e-07, "-9": 1.2687424360055919e-08, "0": 0.20619192971499262, "1": 0.2440235988915063, "10": 2.5531273340625352e-05, "11": 4.705342729464126e-06, "12": 7.962801223640057e-07, "13": 1.2455623423487315e-07, "14": 1.811133175940227e-08, "15": 2.4598621530026086e-09, "16": 3.1241093609283896e-10, "17": 3.460133576592816e-11, "2": 0.2082659611686711, "3": 0.12736817864366407, "4": 0.06089582927753439, "5": 0.0238113922028292, "6": 0.007860979841544501, "7": 0.002243118188171145, "8": 0.0005632409504225804, "9": 0.00012621879998366448} |
| Raw goal margin distribution | {"-1": 0.08458647884853714, "-10": 9.228420718127684e-10, "-11": 6.115777312671002e-11, "-12": 3.721617771092694e-12, "-13": 2.0933259291419231e-13, "-14": 1.094528968446749e-14, "-15": 5.345559106937399e-16, "-16": 2.441260277277759e-17, "-17": 9.722684928103254e-19, "-2": 0.02692956120766975, "-3": 0.005922122840407641, "-4": 0.001018144719472114, "-5": 0.00014315688622932785, "-6": 1.6994548411242617e-05, "-7": 1.743775590259594e-06, "-8": 1.5744836345951489e-07, "-9": 1.2687424360055919e-08, "0": 0.20619192971499262, "1": 0.2440235988915063, "10": 2.5531273340625352e-05, "11": 4.705342729464126e-06, "12": 7.962801223640057e-07, "13": 1.2455623423487315e-07, "14": 1.811133175940227e-08, "15": 2.4598621530026086e-09, "16": 3.1241093609283896e-10, "17": 3.460133576592816e-11, "2": 0.2082659611686711, "3": 0.12736817864366407, "4": 0.06089582927753439, "5": 0.0238113922028292, "6": 0.007860979841544501, "7": 0.002243118188171145, "8": 0.0005632409504225804, "9": 0.00012621879998366448} |
| Unadjusted home-win probability | 67.5% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 45.9% |
| P home draw | 88.1% |
| P draw away | 32.5% |
| P home away | 79.4% |
| Raw p home draw | 88.1% |
| Raw p draw away | 32.5% |
| Raw p home away | 79.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5276 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05791809830694776, 0.037614576524137605, 0.01778642276516103, 0.004886333531632279, 0.001006789941586286, 0.00016595281184429773, 2.2795499687879847e-05, 2.683903076742426e-06, 2.764983810830978e-07, 2.5320124396135152e-08, 2.0868036450411347e-09, 1.5635243639071806e-10, 1.0738389652258047e-11, 6.807874764453142e-13, 4.007737552712591e-14, 2.2020327131951138e-15, 1.1342780698129164e-16, 5.499033504277182e-18], [0.10575258114103331, 0.09727756109527318, 0.03780046931869934, 0.010384645815637989, 0.002139673210278771, 0.00035269004089791566, 4.844597465904895e-05, 5.703946051787572e-06, 5.8762623090653e-07, 5.3811415483527786e-08, 4.4349647031350766e-09, 3.322869107928641e-10, 2.2821686740602102e-11, 1.4468387744798365e-12, 8.517415918812494e-14, 4.6798544661237605e-15, 2.410616454075299e-16, 1.1686782103711423e-17], [0.11826991093946662, 0.09747427673966794, 0.04016759017762484, 0.01103494757553148, 0.0022736626865636446, 0.00037477600881291584, 5.147973268410292e-05, 6.061135523789522e-06, 6.244242477962971e-07, 5.718116528651114e-08, 4.712688700921425e-09, 3.530952047601721e-10, 2.4250814253916306e-11, 1.5374419416971072e-12, 9.050789002505701e-14, 4.9729138202312284e-15, 2.561572793881585e-16, 1.2418625548780171e-17], [0.08378409754488815, 0.06905217265829955, 0.028455295745573914, 0.007817314790608617, 0.0016106951869839627, 0.0002654966882991618, 3.6468979392376786e-05, 4.293795149789923e-06, 4.423510736685628e-07, 4.050795584472456e-08, 3.3385361219962846e-09, 2.501376964205223e-10, 1.717962388618884e-11, 1.0891458748005852e-12, 6.411708460931037e-14, 3.5228833207613355e-15, 1.8146548274713212e-16, 8.797532069547108e-18], [0.04451539034093941, 0.0366881605202859, 0.015118604060901287, 0.004153423257146169, 0.0008557796416014284, 0.00014106124026139845, 1.9376360199112476e-05, 2.281339451493474e-06, 2.3502587351424105e-07, 2.1522311741501485e-08, 1.7738000765403975e-09, 1.3290084301710452e-10, 9.127718572065497e-12, 5.786748938722688e-13, 3.406609526798718e-14, 1.871745721976137e-15, 9.641455878387569e-17, 4.674223218827473e-18], [0.018921203763227555, 0.015594250788000186, 0.006426141293178562, 0.0017654066865750075, 0.00036374792742794064, 5.9957880850589296e-05, 8.235894523425686e-06, 9.696801102763706e-07, 9.989741544069446e-08, 9.148028194243186e-09, 7.539512161164445e-10, 5.6489315532716195e-11, 3.8797238813969045e-12, 2.4596494596053494e-13, 1.4479745657544314e-14, 7.955828743096355e-16, 4.098087197527414e-17, 1.986771974386277e-18], [0.006702025769582062, 0.00552359521869421, 0.0022761852303265716, 0.0006253196813097439, 0.00012884211880810476, 2.123751044482357e-05, 2.9172127747406733e-06, 3.434676339120429e-07, 3.5384379396587304e-08, 3.2402970480046695e-09, 2.670549158843904e-10, 2.0008919788818777e-11, 1.3742259613798272e-12, 8.712254393904224e-14, 5.128829526293435e-15, 2.8180114712489166e-16, 1.4515718105208987e-17, 7.037288503016965e-19], [0.0020347761308975648, 0.0016769973876778715, 0.0006910637970374303, 0.00018985089067911554, 3.9117257530531465e-05, 6.447838432514641e-06, 8.856836913000916e-07, 1.042788803337696e-07, 1.074291461688744e-08, 9.837740583186238e-10, 8.107951045886545e-11, 6.074830773721615e-12, 4.1722343076723285e-13, 2.6450938710922377e-14, 1.5571441021473923e-15, 8.555655671032132e-17, 4.4070610497158316e-18, 2.136563953121256e-19], [0.0005405491995351683, 0.0004455033562497971, 0.0001835848065268672, 5.043490801239448e-05, 1.0391709399899722e-05, 1.7129028842551056e-06, 2.3528662593581364e-07, 2.7702244211002317e-08, 2.8539129237139184e-09, 2.613448583717276e-10, 2.153920709592273e-11, 1.6138113978161937e-12, 1.1083764356379609e-13, 7.026833827088313e-15, 4.1366368771260904e-16, 2.2728558460310356e-17, 1.1707594199444822e-18, 5.675896807900637e-20], [0.00012764426303053537, 0.00010520031781572492, 4.3351368113904294e-05, 1.1909603547264333e-05, 2.4538785537344753e-06, 4.044816392136687e-07, 5.556013771613074e-08, 6.541555421127305e-09, 6.739175864362428e-10, 6.171347931393701e-11, 5.0862275226480295e-12, 3.810823634956177e-13, 2.6172990989364058e-14, 1.6593032161883154e-15, 9.7681758859277e-17, 5.367078698678202e-18, 2.7646090952197933e-19, 1.3402955100199145e-20], [2.7127506818541822e-05, 2.2357623218649054e-05, 9.213218880207144e-06, 2.531080079621406e-06, 5.215088059412514e-07, 8.596217460332616e-08, 1.1807879014295388e-08, 1.3902394441969454e-09, 1.4322385892745552e-10, 1.3115613589968206e-11, 1.0809469107771995e-12, 8.098926006318329e-14, 5.56239641851947e-15, 3.5264224370513885e-16, 2.075974678837143e-17, 1.1406346085386838e-18, 5.875465947360026e-20, 2.8484535633402e-21], [5.241140200672687e-06, 4.319580071496351e-06, 1.7800298484358048e-06, 4.890145506242525e-07, 1.0075753684652198e-07, 1.660822765853258e-08, 2.2813283137469513e-09, 2.6859968696279653e-10, 2.767140857216862e-11, 2.5339877380801776e-12, 2.0884316228408428e-13, 1.5647441159235204e-14, 1.074676699049015e-15, 6.813185790723418e-17, 4.010864108379856e-18, 2.203750584629655e-19, 1.1351629539852913e-20, 5.503323464420814e-22], [9.282246818557876e-07, 7.650130857214401e-07, 3.1524965494074484e-07, 8.660622656455342e-08, 1.7844520276700833e-08, 2.941376541034195e-09, 4.040314067470619e-10, 4.756996558603913e-11, 4.900705463880948e-12, 4.4877829478861337e-13, 3.698687126210059e-14, 2.771217814403074e-15, 1.9032908849577576e-16, 1.2066395804880256e-17, 7.103383840962418e-19, 3.9029211335442294e-20, 2.0104142065923653e-21, 9.746582759331378e-23], [1.517463805468005e-07, 1.2506451196392946e-07, 5.1537084760818824e-08, 1.4158405471089341e-08, 2.917226203433409e-09, 4.808569009766455e-10, 6.605114558958065e-11, 7.776748713452981e-12, 8.01168435623867e-13, 7.336637694871971e-14, 6.046622064124593e-15, 4.530393139317702e-16, 3.111504235619198e-17, 1.972617110304499e-18, 1.1612627939882178e-19, 6.380504280395416e-21, 3.286629683670234e-22, 1.5933735498946455e-23], [2.303556593948924e-08, 1.898517646123772e-08, 7.823487519498003e-09, 2.149289371199967e-09, 4.4284388416678467e-10, 7.299555224969426e-11, 1.0026766464708733e-11, 1.1805343042652321e-12, 1.2161982553355966e-13, 1.1137241019217772e-14, 9.178957729825694e-16, 6.877275722591393e-17, 4.723358852602126e-18, 2.9944932692328456e-19, 1.7628325346278e-20, 9.685801173551678e-22, 4.9892046534525816e-23, 2.4187899139720238e-24], [3.263744917612559e-09, 2.6898741427976425e-09, 1.1084541051363916e-09, 3.045174700790581e-10, 6.274338907243686e-11, 1.0342218779824084e-11, 1.420620972597071e-12, 1.6726147930265958e-13, 1.7231444997217317e-14, 1.5779561860204107e-15, 1.3005010043336216e-16, 9.743921093837721e-18, 6.692190020308346e-19, 4.242683776016841e-20, 2.4976315930795475e-21, 1.3723120341920266e-22, 7.06884796032749e-24, 3.427010783774887e-25], [4.3351567671580217e-10, 3.572897511084495e-10, 1.47233390974722e-10, 4.0448350114835246e-11, 8.334059021094518e-12, 1.3737329620594313e-12, 1.886977928234003e-13, 2.2216954822995256e-14, 2.2888129211470957e-15, 2.0959626474452644e-16, 1.7274253570517482e-17, 1.2942624664278033e-18, 8.889080974768475e-20, 5.635458574981185e-21, 3.3175461857254813e-22, 1.822810284460529e-23, 9.389386990954398e-25, 4.552019035014812e-26], [5.419565465330156e-11, 4.466632466196065e-11, 1.8406277879384705e-11, 5.056621782922333e-12, 1.0418764737395415e-12, 1.7173625129694452e-13, 2.358992064870921e-14, 2.7774368395549276e-15, 2.8613432293896277e-16, 2.6202528284030245e-17, 2.1595285503713402e-18, 1.6180130368672946e-19, 1.1112621493722909e-20, 7.045128541980923e-22, 4.147406819057766e-23, 2.2787733404130494e-24, 1.173807550912537e-25, 5.690674290393551e-27]] |
| Legacy trial inputs | {"lambda_home": 2.125242934894172, "lambda_away": 0.8241680065993929, "rho": -0.060476960468338566, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6679 |
| Legacy p draw | 0.2041 |
| Legacy p away | 0.1280 |
| Legacy p over 1 5 | 0.7987 |
| Legacy p under 3 5 | 0.6586 |
| Legacy p btts yes | 0.4999 |
| Legacy p over 2 5 | 0.5654 |
| Legacy goal margin distribution | {"-1": 0.0882103402171989, "-10": 2.4444653923702326e-09, "-11": 1.8077759558794942e-10, "-12": 1.227935760141446e-11, "-13": 7.711206891596363e-13, "-14": 4.502218480470738e-14, "-15": 2.455512984151424e-15, "-16": 1.2511458908500306e-16, "-17": 5.499033504277182e-18, "-2": 0.030730610386050593, "-3": 0.007439636290000176, "-4": 0.0014154979574620675, "-5": 0.00022092456979703125, "-6": 2.91662096337965e-05, "-7": 3.332185878327058e-06, "-8": 3.3528200186305577e-07, "-9": 3.012595736882109e-08, "0": 0.2040993263012847, "1": 0.23622147639447444, "10": 3.177694832802818e-05, "11": 6.059903801238102e-06, "12": 1.0614257046045664e-06, "13": 1.7188150133976317e-07, "14": 2.5877730095044527e-08, "15": 3.6394409466003934e-09, "16": 4.781820013777628e-10, "17": 5.419565465330156e-11, "2": 0.20434162627645971, "3": 0.12756460617858062, "4": 0.0625864855224381, "5": 0.02518883985741064, "6": 0.008575056096299036, "7": 0.002526265701503398, "8": 0.0006554700863552453, "9": 0.0001518715139890645} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.6679 |
| Legacy raw p draw | 0.2041 |
| Legacy raw p away | 0.1280 |
| Legacy market weight | 0 |
| Legacy lambda home | 2.1252 |
| Legacy lambda away | 0.8242 |
| Legacy model home team | Lyon |
| Legacy model away team | Angers |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 90/100 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 9.904724219664642, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,581.6014 |
| Elo away rating | 1,418.6457 |
| Elo rating diff | 222.9557 |
| Elo home expectancy | 0.7830 |

</details>


---

## 2026-11-01 — Olympique de Marseille vs Toulouse FC

The model's most likely 1X2 outcome is **Olympique de Marseille win** at **55.6%**. Expected goals are 1.96 for Olympique de Marseille and 1.16 for Toulouse FC (3.12 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.1%; Double Chance 1X: 78.4%; Double Chance X2: 44.4%; Double Chance 12 (either team wins): 77.1%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 59.4%; BTTS No (at least one team does not score): 40.6%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Olympique de Marseille win | 55.6% | 1.80 |
| Draw | 22.9% | 4.37 |
| Toulouse FC win | 21.6% | 4.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Olympique de Marseille expected goals | 1.96 |
| Toulouse FC expected goals | 1.16 |
| Expected total goals | 3.12 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.57% |
| 2 | 2-1 | 9.84% |
| 3 | 2-0 | 8.51% |
| 4 | 1-0 | 8.15% |
| 5 | 3-1 | 6.44% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T19:45:00+00:00 |
| Fixture id | fdorg:559645 |
| Matched home-team name | Marseille |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9617 |
| Dc lambda away | 1.1562 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T12:21:43.479248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.4% |
| P btts no | 40.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.17 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.65 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.88 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.13044226293042913, "-10": 6.385656146665383e-08, "-11": 6.599998657079822e-09, "-12": 6.26895884238043e-10, "-13": 5.507428463252151e-11, "-14": 4.498295535333862e-12, "-15": 3.407049729273005e-13, "-16": 2.1563096253278305e-14, "-2": 0.0593307819299811, "-3": 0.019527921157610643, "-4": 0.005104403595006726, "-5": 0.0011011825884251214, "-6": 0.0002017133431837073, "-7": 3.205710374017211e-05, "-8": 4.494799659760047e-06, "-9": 5.635040040205727e-07, "0": 0.22874056371952398, "1": 0.225032963443681, "10": 1.2627216388766712e-05, "11": 2.2144003958931655e-06, "12": 3.568764837399982e-07, "13": 5.3196319624311194e-08, "14": 7.372094885241862e-09, "15": 9.4739614528808e-10, "16": 1.0173595628775255e-10, "2": 0.1708049650279099, "3": 0.09538644016097265, "4": 0.04230442956838977, "5": 0.015484970515618295, "6": 0.004812778602616149, "7": 0.0012977640767424417, "8": 0.00030873937055772116, "9": 6.567330774187455e-05} |
| Raw goal margin distribution | {"-1": 0.13044226293042913, "-10": 6.385656146665383e-08, "-11": 6.599998657079822e-09, "-12": 6.26895884238043e-10, "-13": 5.507428463252151e-11, "-14": 4.498295535333862e-12, "-15": 3.407049729273005e-13, "-16": 2.1563096253278305e-14, "-2": 0.0593307819299811, "-3": 0.019527921157610643, "-4": 0.005104403595006726, "-5": 0.0011011825884251214, "-6": 0.0002017133431837073, "-7": 3.205710374017211e-05, "-8": 4.494799659760047e-06, "-9": 5.635040040205727e-07, "0": 0.22874056371952398, "1": 0.225032963443681, "10": 1.2627216388766712e-05, "11": 2.2144003958931655e-06, "12": 3.568764837399982e-07, "13": 5.3196319624311194e-08, "14": 7.372094885241862e-09, "15": 9.4739614528808e-10, "16": 1.0173595628775255e-10, "2": 0.1708049650279099, "3": 0.09538644016097265, "4": 0.04230442956838977, "5": 0.015484970515618295, "6": 0.004812778602616149, "7": 0.0012977640767424417, "8": 0.00030873937055772116, "9": 6.567330774187455e-05} |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 82.3% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 59.4% |
| P home draw | 78.4% |
| P draw away | 44.4% |
| P home away | 77.1% |
| Raw p home draw | 78.4% |
| Raw p draw away | 44.4% |
| Raw p home away | 77.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6027 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.058843056343371586, 0.048623187079586225, 0.028728587177415416, 0.010015375567521592, 0.002618674226974273, 0.0005477541734336585, 9.5479177791384e-05, 1.426542964061886e-05, 1.864958167806768e-06, 2.1672090767931932e-07, 2.266600794189656e-08, 2.1550461606186544e-09, 1.8782333891543567e-10, 1.5110555489289514e-11, 1.1288250022120416e-12, 7.870631630677428e-14, 5.144744713343733e-15], [0.09351802950839182, 0.11072542487169185, 0.05459971147852751, 0.019034580884842847, 0.00497688439623137, 0.0010410264746380643, 0.00018146160573168852, 2.7111961256045914e-05, 3.5444199623510237e-06, 4.1188586677028467e-07, 4.307756195440249e-08, 4.095742608783339e-09, 3.5696499971910846e-10, 2.8718153277097988e-11, 2.145372449048869e-12, 1.4958418022261456e-13, 9.777772058351499e-15], [0.09486761350554894, 0.0992183958701065, 0.051884356079334504, 0.01808795222001262, 0.004729373749187365, 0.000989254097420961, 0.00017243714868737703, 2.5763627933657058e-05, 3.368148703379952e-06, 3.9140193962305374e-07, 4.093522663303437e-08, 3.892052946231946e-09, 3.392123996949965e-10, 2.728994073816383e-11, 2.0386786862971053e-12, 1.4214505279130803e-13, 9.29150344205735e-15], [0.06009976861574103, 0.06285604131772127, 0.03286936057437905, 0.011458934224077986, 0.0029961148754616353, 0.0006267043109890811, 0.00010924099757461823, 1.6321566657985595e-05, 2.133762516590587e-06, 2.479578133977395e-07, 2.593295602122831e-08, 2.465662124989276e-09, 2.148951152024828e-10, 1.7288504087909813e-11, 1.2915273484889797e-12, 9.005059226171239e-14, 5.8862786395205936e-15], [0.028555442059167584, 0.029865040868838337, 0.015617350000208408, 0.005444528986252519, 0.001423555975329439, 0.000297768511474636, 5.190410959270571e-05, 7.754930871645295e-06, 1.013823069770813e-06, 1.1781318192533833e-07, 1.2321628521098348e-08, 1.1715198505635239e-09, 1.0210397065248301e-10, 8.214355697913423e-12, 6.136485250618409e-13, 4.2786096002531956e-14, 2.796770977765829e-15], [0.010854128592846641, 0.011351916505068498, 0.0059362668884803465, 0.002069504566653817, 0.0005411038492531525, 0.00011318394958654146, 1.97291247969164e-05, 2.9477049150584236e-06, 3.8536142942161526e-07, 4.4781636505589255e-08, 4.683539486595043e-09, 4.453031082741237e-10, 3.881045248768936e-11, 3.122335590805905e-12, 2.3325221119081003e-13, 1.626330235179351e-14, 1.0630727331943343e-15], [0.003438110187716622, 0.0035957874878971337, 0.0018803480621871328, 0.0006555279563232546, 0.0001713978824570048, 3.585169337462547e-05, 6.249318347279811e-06, 9.337031722218438e-07, 1.2206553894346473e-07, 1.4184851356373126e-08, 1.4835391607620887e-09, 1.410524244376597e-10, 1.2293443084482723e-11, 9.890184838324824e-13, 7.388403377965063e-14, 5.1514983467643344e-15, 3.367346501393009e-16], [0.0009334645518339158, 0.0009762747476424261, 0.0005105241441743912, 0.00017797920268817311, 4.653540427663491e-05, 9.73391865333378e-06, 1.6967219873151515e-06, 2.5350520071109676e-07, 3.3141419961266884e-08, 3.851259904791311e-09, 4.027884919966934e-10, 3.8296456766626373e-11, 3.33773285694887e-12, 2.685235915546057e-13, 2.0059894161102435e-14, 1.3986582258811178e-15, 9.142518480130248e-17], [0.00022176036229529478, 0.00023193065158349146, 0.00012128368340306469, 4.228198316863278e-05, 1.1055275844883583e-05, 2.312457739156108e-06, 4.0308513256574804e-07, 6.022446705982315e-08, 7.873307329295017e-09, 9.149322168709619e-10, 9.568924897905993e-11, 9.097973897892791e-12, 7.92935142687223e-13, 6.379234094213149e-14, 4.765568642142535e-15, 3.3227502243049993e-16, 2.1719605811082154e-17], [4.682928124644124e-05, 4.897694791015473e-05, 2.5611555022278936e-05, 8.92871413523665e-06, 2.334549855702622e-06, 4.883232184354558e-07, 8.511975198726023e-08, 1.2717640234128233e-08, 1.6626114759510676e-09, 1.9320683670342887e-10, 2.0206761507424788e-11, 1.92122511898621e-12, 1.674446344817991e-13, 1.3471070503438332e-14, 1.0063482577871355e-15, 7.016673455757429e-17, 4.586543413626928e-18], [8.900073049232837e-06, 9.30824481022703e-06, 4.867567994545105e-06, 1.696934181439374e-06, 4.43689582667005e-07, 9.280758106963942e-08, 1.6177314501848546e-08, 2.4170331913049703e-09, 3.1598528088837246e-10, 3.6719653056865866e-11, 3.8403675802342975e-12, 3.651357323426302e-13, 3.1823454021160235e-14, 2.560225319304429e-15, 1.9126009985375025e-16, 1.333543984803309e-17, 8.716890445090814e-19], [1.537718945639776e-06, 1.6082412263540923e-06, 8.409988865256562e-07, 2.931894857343867e-07, 7.665890757030012e-08, 1.6034921839443256e-08, 2.7950515531116755e-09, 4.1760530615309876e-10, 5.459467020972817e-11, 6.344274464997704e-12, 6.635233164581824e-13, 6.308668819316202e-14, 5.498328821947424e-15, 4.423454680453905e-16, 3.30451533895464e-17, 2.3040438420365186e-18, 1.5060693895807835e-19], [2.4354083921270585e-07, 2.5471001643918064e-07, 1.3319571510917042e-07, 4.643476209131724e-08, 1.2141083866943295e-08, 2.5395787263734296e-09, 4.426746531398048e-10, 6.613948992993005e-11, 8.646594253858415e-12, 1.004793451873898e-12, 1.0508749065336585e-13, 9.991543011990809e-15, 8.708142793983445e-16, 7.005778709768726e-17, 5.23362504651614e-18, 3.6490983769402686e-19, 2.3852824606935372e-20], [3.560446997414378e-08, 3.7237348617748146e-08, 1.9472556859948812e-08, 6.788533282472817e-09, 1.7749666026920362e-09, 3.712738890218119e-10, 6.471685178954746e-11, 9.669267343119689e-12, 1.264089449988414e-12, 1.4689584877473005e-13, 1.5363273025260545e-14, 1.4607143274852988e-15, 1.2730875431046163e-16, 1.0242103070836544e-17, 7.651301786878672e-19, 5.3348019171845026e-20, 3.487165356995456e-21], [4.833398115982308e-09, 5.055065579796726e-09, 2.6434495362122945e-09, 9.215608040680111e-10, 2.4095626868237117e-10, 5.0401382663880094e-11, 8.785478613754513e-12, 1.312627841198129e-12, 1.7160338492453692e-13, 1.9941488224063257e-14, 2.0856037163182583e-15, 1.9829571634075677e-16, 1.7282489914302887e-17, 1.3903917604230095e-18, 1.038683841336997e-19, 7.242130427551312e-21, 4.733916409613941e-22], [6.124031113764739e-10, 6.404889096644333e-10, 3.3493138406913547e-10, 1.167639598872887e-10, 3.052973603784345e-11, 6.385975833228761e-12, 1.1131411708471045e-12, 1.6631308961929935e-13, 2.1742559650326512e-14, 2.5266342934823032e-15, 2.642509833295747e-16, 2.5124541936274186e-17, 2.189732842584316e-18, 1.7616596433464178e-19, 1.3160372907580557e-20, 9.175952612224031e-22, 5.997985410424931e-23], [7.2743381407897e-11, 7.60795106650038e-11, 3.9784320105843165e-11, 1.386963114816031e-11, 3.6264287225640973e-12, 7.5854852313544e-13, 1.3222279777410462e-13, 1.975524991065095e-14, 2.58265720739513e-15, 3.0012244986140723e-16, 3.138865513689083e-17, 2.9843808805301037e-18, 2.60104118333891e-19, 2.0925608796926704e-20, 1.5632350785000663e-21, 1.0899517135886385e-22, 7.124616650115601e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9005359066682659, "lambda_away": 1.0458616191952914, "rho": -0.060476960468338566, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5669 |
| Legacy p draw | 0.2345 |
| Legacy p away | 0.1987 |
| Legacy p over 1 5 | 0.7990 |
| Legacy p under 3 5 | 0.6592 |
| Legacy p btts yes | 0.5580 |
| Legacy p over 2 5 | 0.5647 |
| Legacy goal margin distribution | {"-1": 0.12462543106996142, "-10": 2.711888170302487e-08, "-11": 2.5406364775931514e-09, "-12": 2.1867301824207022e-10, "-13": 1.740395926976921e-11, "-14": 1.2877006858767134e-12, "-15": 8.848408836512579e-14, "-16": 5.144744713343733e-15, "-2": 0.05317422395138407, "-3": 0.01609890994795747, "-4": 0.003849519544306193, "-5": 0.000757235810791976, "-6": 0.00012622002506264027, "-7": 1.8228395838332458e-05, "-8": 2.320350224945731e-06, "-9": 2.639138705459889e-07, "0": 0.2344550223373584, "1": 0.23162902912821684, "10": 1.0648545998445887e-05, "11": 1.8128543680275344e-06, "12": 2.8354202775527615e-07, "13": 4.10083365691578e-08, "14": 5.513671345752584e-09, "15": 6.884826220414777e-10, "16": 7.2743381407897e-11, "2": 0.17559205731645175, "3": 0.09660553978379896, "4": 0.041977246031890125, "5": 0.015005152427998911, "6": 0.004545057509919938, "7": 0.0011927829571589444, "8": 0.00027591058899785936, "9": 5.7026786206167016e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.5669 |
| Legacy raw p draw | 0.2345 |
| Legacy raw p away | 0.1987 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.9005 |
| Legacy lambda away | 1.0459 |
| Legacy model home team | Marseille |
| Legacy model away team | Toulouse |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 9.52299035579764, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,566.8488 |
| Elo away rating | 1,531.5216 |
| Elo rating diff | 95.3273 |
| Elo home expectancy | 0.6338 |

</details>


---

## 2026-11-01 — Paris FC vs AS Monaco FC

The model's most likely 1X2 outcome is **Paris FC win** at **37.9%**. Expected goals are 1.52 for Paris FC and 1.50 for AS Monaco FC (3.02 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 58.1%; Under 3.5 goals: 64.3%; Double Chance 1X: 63.2%; Double Chance X2: 62.1%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 81.2%; BTTS Yes (both teams score): 61.3%; BTTS No (at least one team does not score): 38.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 37.9% | 2.64 |
| Draw | 25.4% | 3.94 |
| AS Monaco FC win | 36.8% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.52 |
| AS Monaco FC expected goals | 1.50 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 58.1% |
| Under 2.5 | 41.9% |
| Over 3.5 | 35.7% |
| Under 3.5 | 64.3% |
| Over 4.5 | 18.8% |
| Under 4.5 | 81.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.71% |
| 2 | 2-1 | 8.47% |
| 3 | 1-2 | 8.33% |
| 4 | 1-0 | 6.84% |
| 5 | 0-1 | 6.71% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:15:00+00:00 |
| Fixture id | fdorg:559642 |
| Matched home-team name | Paris FC |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.5228 |
| Dc lambda away | 1.4980 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T12:21:43.479248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.3% |
| P btts no | 38.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.29 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.26 |
| Fair Over 2.5 odds | 1.72 |
| Fair Under 2.5 odds | 2.39 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.31 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.18889833630374503, "-10": 9.389490985508408e-07, "-11": 1.2572252889469417e-07, "-12": 1.5470157416520236e-08, "-13": 1.759883365633477e-09, "-14": 1.845772399233491e-10, "-15": 1.5999541168932737e-11, "-2": 0.11016020964909996, "-3": 0.04694019690195332, "-4": 0.015888596344833833, "-5": 0.004439307727219408, "-6": 0.0010532860034612017, "-7": 0.00021682967422365925, "-8": 3.938277810942077e-05, "-9": 6.395996314325899e-06, "0": 0.25382863750763845, "1": 0.19212643659805206, "10": 1.1066780267783465e-06, "11": 1.5063651849456345e-07, "12": 1.8842990022666356e-08, "13": 2.1790986689895386e-09, "14": 2.3233202637214345e-10, "15": 2.0472759508223456e-11, "2": 0.11384149786208005, "3": 0.04931268823572182, "4": 0.01696825674698015, "5": 0.004819532016680847, "6": 0.0011624488595805872, "7": 0.00024326755136124046, "8": 4.491689622779227e-05, "9": 7.415655033082764e-06} |
| Raw goal margin distribution | {"-1": 0.18889833630374503, "-10": 9.389490985508408e-07, "-11": 1.2572252889469417e-07, "-12": 1.5470157416520236e-08, "-13": 1.759883365633477e-09, "-14": 1.845772399233491e-10, "-15": 1.5999541168932737e-11, "-2": 0.11016020964909996, "-3": 0.04694019690195332, "-4": 0.015888596344833833, "-5": 0.004439307727219408, "-6": 0.0010532860034612017, "-7": 0.00021682967422365925, "-8": 3.938277810942077e-05, "-9": 6.395996314325899e-06, "0": 0.25382863750763845, "1": 0.19212643659805206, "10": 1.1066780267783465e-06, "11": 1.5063651849456345e-07, "12": 1.8842990022666356e-08, "13": 2.1790986689895386e-09, "14": 2.3233202637214345e-10, "15": 2.0472759508223456e-11, "2": 0.11384149786208005, "3": 0.04931268823572182, "4": 0.01696825674698015, "5": 0.004819532016680847, "6": 0.0011624488595805872, "7": 0.00024326755136124046, "8": 4.491689622779227e-05, "9": 7.415655033082764e-06} |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 36.8% |
| Raw p over 1 5 | 81.0% |
| Raw p under 3 5 | 64.3% |
| Raw p btts yes | 61.3% |
| P home draw | 63.2% |
| P draw away | 62.1% |
| P home away | 74.6% |
| Raw p home draw | 63.2% |
| Raw p draw away | 62.1% |
| Raw p home away | 74.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5814 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05104281896218787, 0.06488175244979368, 0.05723209949627118, 0.030586172220157755, 0.012259474219647938, 0.003931049810624189, 0.001050422468964323, 0.0002405872839775817, 4.82158013148575e-05, 8.589217215100446e-06, 1.377083556027097e-06, 2.0071245067449757e-07, 2.6816356717177957e-08, 3.307220324397857e-09, 3.787405443387175e-10, 4.0481560585262286e-11], [0.06065331160133512, 0.11419731938979825, 0.08632396555779757, 0.04613354569405211, 0.01849113416436079, 0.005929256683662607, 0.0015843667073216622, 0.00036288112088353404, 7.272455857252881e-05, 1.2955234869429888e-05, 2.077074133344306e-06, 3.027373594808509e-07, 4.0447480941881313e-08, 4.988326059818395e-09, 5.712595902054421e-10, 6.105889653612578e-11], [0.050653525157445006, 0.08121128480310146, 0.0651018143245761, 0.034791931840731274, 0.013945216432544935, 0.004471589844237495, 0.001194861085627893, 0.00027366930146225114, 5.484572770067636e-05, 9.770279777476163e-06, 1.5664397910082617e-06, 2.2831146876401262e-07, 3.05037468698324e-08, 3.7619805211486496e-09, 4.3081936206681567e-10, 4.6047988174233034e-11], [0.025467137029498647, 0.04083070056809741, 0.032731321682342426, 0.01749238365848758, 0.00701125413660256, 0.0022481868922043426, 0.0006007418221005797, 0.00013759306147880098, 2.7574856014347883e-05, 4.912215944223449e-06, 7.875609186541131e-07, 1.1478844645750403e-07, 1.53364074668549e-08, 1.8914157136468476e-09, 2.1660359658313277e-10, 2.3151605364499733e-11], [0.009603108566432136, 0.015396377297720957, 0.012342276058524681, 0.006596000923212, 0.0026437928449771363, 0.0008477428294535307, 0.00022652679534986182, 5.1883378404027437e-05, 1.0397883975053554e-05, 1.852290776128336e-06, 2.969722507777061e-07, 4.328424951052279e-08, 5.783028761837523e-09, 7.132121063065551e-10, 8.167654854403717e-11, 8.729971474412741e-12], [0.002896900237568566, 0.004644513674183536, 0.0037232050641452714, 0.001989767845408681, 0.0007975338472656497, 0.0002557324419537828, 6.833469836616347e-05, 1.5651283142821794e-05, 3.1366543811483925e-06, 5.587671483970158e-07, 8.958546890081003e-08, 1.3057246184669244e-08, 1.744524419164949e-09, 2.1514953266469847e-10, 2.463877308521459e-11, 2.6335072922734915e-12], [0.0007282391016383423, 0.0011675640126541844, 0.0009359602639972874, 0.0005001990504945657, 0.00020048855149612692, 6.428746194743422e-05, 1.7178361444255338e-05, 3.934507729193454e-06, 7.885098489255141e-07, 1.4046603362330317e-07, 2.2520499859164172e-08, 3.282404104939131e-09, 4.385483764070297e-10, 5.4085501583290466e-11, 6.193833582653002e-12, 6.620258992049182e-13], [0.00015691615539673912, 0.0002515789877707909, 0.00020167454054603685, 0.00010777959019246117, 4.3199949894282085e-05, 1.3852238016759653e-05, 3.7014799504501086e-06, 8.477817585664302e-07, 1.69902898247974e-07, 3.026669387898922e-08, 4.852568679109208e-09, 7.072707733583261e-10, 9.449550982150935e-11, 1.1653986928278044e-11, 1.3346063823963554e-12, 1.4264897152953892e-13], [2.958485035747436e-05, 4.743250742707397e-05, 3.802356161404453e-05, 2.03206804256188e-05, 8.144885081088886e-06, 2.611690222754897e-06, 6.97874161894829e-07, 1.5984011588589757e-07, 3.203336079232005e-08, 5.706459012849287e-09, 9.14899538915139e-10, 1.3334828360481276e-10, 1.7816110205187317e-11, 2.1972336657709953e-12, 2.516256532636594e-13, 2.6894926565583765e-14], [4.958137567649438e-06, 7.949233954552386e-06, 6.372384751535435e-06, 3.4055514157097925e-06, 1.36500473102889e-06, 4.376942675740898e-07, 1.1695702556455349e-07, 2.6787672535618822e-08, 5.368484465642891e-09, 9.563478762944525e-10, 1.5332840016796867e-10, 2.2347895173840473e-11, 2.985809434571122e-12, 3.6823531812831826e-13, 4.2170049513726444e-14, 4.507332103179096e-15], [7.478427322913034e-07, 1.1989939284830223e-06, 9.611555869069913e-07, 5.136640201958588e-07, 2.058855474893867e-07, 6.601803046098771e-08, 1.7640789583885074e-08, 4.040421619495149e-09, 8.097359212550311e-10, 1.442472700829257e-10, 2.3126734213191437e-11, 3.3707638724690893e-12, 4.503537578747344e-13, 5.5541441252464566e-14, 6.360566769057123e-15, 6.798471219070642e-16], [1.0254377404091977e-07, 1.644053718381339e-07, 1.3179311246360602e-07, 7.043332099856141e-08, 2.823091025483011e-08, 9.052355135519454e-09, 2.418895127122383e-09, 5.54020335679574e-10, 1.110305332346913e-10, 1.977910439014782e-11, 3.1711247633521853e-12, 4.621972427608301e-13, 6.175225350454728e-14, 7.615811126825572e-15, 8.721573311811158e-16, 9.322025426069428e-17], [1.2889015803464838e-08, 2.0664574281717302e-08, 1.6565447539051784e-08, 8.85296251217269e-09, 3.5484226304709854e-09, 1.1378160155654812e-09, 3.0403774204724827e-10, 6.963637655042245e-11, 1.3955740471947117e-11, 2.4860913443781158e-12, 3.9858760389777445e-13, 5.809487335510963e-14, 7.761814686107274e-15, 9.57252752670168e-16, 1.0962391164007025e-16, 1.1717116339892439e-17], [1.4954369556797137e-09, 2.3975894300603907e-09, 1.9219917808318777e-09, 1.0271573493137641e-09, 4.1170267900129726e-10, 1.3201412306310132e-10, 3.527571711539421e-11, 8.079500602764083e-12, 1.6192027664373329e-12, 2.8844660665084106e-13, 4.624578338900983e-14, 6.740407636664487e-15, 9.005578627362739e-16, 1.110644260273373e-16, 1.2719019915287807e-17, 1.3594683299219354e-18], [1.6111344282087107e-10, 2.5830837340273157e-10, 2.0706905209687912e-10, 1.1066254330426238e-10, 4.43554880602278e-11, 1.4222765986150852e-11, 3.8004893558706015e-12, 8.704587334428697e-13, 1.74447562857789e-13, 3.1076285557214676e-14, 4.982368096129496e-15, 7.261892761407022e-16, 9.702313238534257e-17, 1.1965714759305927e-17, 1.3703052342502983e-18, 1.464646317638371e-19], [1.6200641960692256e-11, 2.597400564271445e-11, 2.0821673942448333e-11, 1.1127589424832974e-11, 4.460132987502785e-12, 1.430159615473707e-12, 3.8215536985536726e-13, 8.752832808460587e-14, 1.7541444446175584e-14, 3.124852693641575e-15, 5.009983042291088e-16, 7.302142051256421e-17, 9.756088642630388e-18, 1.2032035144008113e-18, 1.3779001980383345e-19, 1.4727641701187568e-20]] |
| Legacy trial inputs | {"lambda_home": 1.508313801478169, "lambda_away": 1.6032701485370384, "rho": -0.060476960468338566, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3541 |
| Legacy p draw | 0.2508 |
| Legacy p away | 0.3952 |
| Legacy p over 1 5 | 0.8234 |
| Legacy p under 3 5 | 0.6222 |
| Legacy p btts yes | 0.6285 |
| Legacy p over 2 5 | 0.6013 |
| Legacy goal margin distribution | {"-1": 0.19392909178659312, "-10": 1.7123003881472633e-06, "-11": 2.4514724570558507e-07, "-12": 3.225865374442767e-08, "-13": 3.9245279027775315e-09, "-14": 4.397994408748433e-10, "-15": 4.0481560585262286e-11, "-2": 0.11980204630781358, "-3": 0.05420480353863461, "-4": 0.019532164947502123, "-5": 0.005818605930807178, "-6": 0.0014733720134482156, "-7": 0.0003239147674671734, "-8": 6.285826893653022e-05, "-9": 1.0910677737580911e-05, "0": 0.250751920778489, "1": 0.18205760715523225, "10": 9.298864946654785e-07, "11": 1.252454627797607e-07, "12": 1.5504801875046942e-08, "13": 1.7745670030248937e-09, "14": 1.8708744846358551e-10, "15": 1.6200641960692256e-11, "2": 0.10603133591074354, "3": 0.045132851192987274, "4": 0.015299962883213244, "5": 0.004287892984138181, "6": 0.0010214624526363274, "7": 0.00021126411648553206, "8": 3.8569357544703516e-05, "9": 6.298203878708596e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3541 |
| Legacy raw p draw | 0.2508 |
| Legacy raw p away | 0.3952 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.5083 |
| Legacy lambda away | 1.6033 |
| Legacy model home team | Paris FC |
| Legacy model away team | Monaco |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 8.959826441164532, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,504.1286 |
| Elo away rating | 1,558.3951 |
| Elo rating diff | 5.7335 |
| Elo home expectancy | 0.5083 |

</details>


---

## 2026-11-01 — RC Strasbourg Alsace vs AJ Auxerre

The model's most likely 1X2 outcome is **RC Strasbourg Alsace win** at **53.3%**. Expected goals are 1.82 for RC Strasbourg Alsace and 1.12 for AJ Auxerre (2.94 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 56.3%; Under 3.5 goals: 66.1%; Double Chance 1X: 77.4%; Double Chance X2: 46.7%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 82.5%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Strasbourg Alsace win | 53.3% | 1.88 |
| Draw | 24.1% | 4.15 |
| AJ Auxerre win | 22.6% | 4.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Strasbourg Alsace expected goals | 1.82 |
| AJ Auxerre expected goals | 1.12 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 79.7% |
| Under 1.5 | 20.3% |
| Over 2.5 | 56.3% |
| Under 2.5 | 43.7% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.5% |
| Under 4.5 | 82.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.34% |
| 2 | 2-1 | 9.81% |
| 3 | 1-0 | 9.07% |
| 4 | 2-0 | 8.78% |
| 5 | 1-2 | 6.02% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | fdorg:559647 |
| Matched home-team name | Strasbourg |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8217 |
| Dc lambda away | 1.1173 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T12:21:43.479248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.06 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.93 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.73 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.1378400166407334, "-10": 5.3129285680679184e-08, "-11": 5.315603411021816e-09, "-12": 4.886247992992646e-10, "-13": 4.153517489532001e-11, "-14": 3.282289354586691e-12, "-15": 2.4083254452742103e-13, "-16": 1.4919799698409564e-14, "-2": 0.06198766699892977, "-3": 0.019991414705536663, "-4": 0.005096999581592968, "-5": 0.0010696567178657779, "-6": 0.00019028293658864142, "-7": 2.9334582918172865e-05, "-8": 3.986717232185922e-06, "-9": 4.841783585082974e-07, "0": 0.24097296466140067, "1": 0.22833725037460123, "10": 7.051796999239478e-06, "11": 1.1503102211541451e-06, "12": 1.7239890174750053e-07, "13": 2.389305131401169e-08, "14": 3.0784281308722043e-09, "15": 3.6826793917680726e-10, "16": 3.71970340624838e-11, "2": 0.16477770747138257, "3": 0.08664295900928033, "4": 0.03601645198879927, "5": 0.012323308919576819, "6": 0.003574204029175586, "7": 0.000898371560526945, "8": 0.00019906187626509748, "9": 3.941618758167425e-05} |
| Raw goal margin distribution | {"-1": 0.1378400166407334, "-10": 5.3129285680679184e-08, "-11": 5.315603411021816e-09, "-12": 4.886247992992646e-10, "-13": 4.153517489532001e-11, "-14": 3.282289354586691e-12, "-15": 2.4083254452742103e-13, "-16": 1.4919799698409564e-14, "-2": 0.06198766699892977, "-3": 0.019991414705536663, "-4": 0.005096999581592968, "-5": 0.0010696567178657779, "-6": 0.00019028293658864142, "-7": 2.9334582918172865e-05, "-8": 3.986717232185922e-06, "-9": 4.841783585082974e-07, "0": 0.24097296466140067, "1": 0.22833725037460123, "10": 7.051796999239478e-06, "11": 1.1503102211541451e-06, "12": 1.7239890174750053e-07, "13": 2.389305131401169e-08, "14": 3.0784281308722043e-09, "15": 3.6826793917680726e-10, "16": 3.71970340624838e-11, "2": 0.16477770747138257, "3": 0.08664295900928033, "4": 0.03601645198879927, "5": 0.012323308919576819, "6": 0.003574204029175586, "7": 0.000898371560526945, "8": 0.00019906187626509748, "9": 3.941618758167425e-05} |
| Unadjusted home-win probability | 53.3% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 57.0% |
| P home draw | 77.4% |
| P draw away | 46.7% |
| P home away | 75.9% |
| Raw p home draw | 77.4% |
| Raw p draw away | 46.7% |
| Raw p home away | 75.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5630 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.06806361229485129, 0.056520393075395546, 0.03261844777203202, 0.011213741152126224, 0.002891339086068703, 0.0005963998346113787, 0.00010251673248285676, 1.5104460122762919e-05, 1.947258962662514e-06, 2.2314630170904004e-07, 2.3014321992645336e-08, 2.157813924703161e-09, 1.8545614873512011e-10, 1.4713174167719907e-11, 1.0838940488702834e-12, 7.452535684903445e-14, 4.803884676791712e-15], [0.10121601585868743, 0.1180671236919947, 0.05741247131575477, 0.019737560681559022, 0.005089111643300581, 0.0010497369046084924, 0.00018044203096946625, 2.6585703574822962e-05, 3.4274147598790964e-06, 3.927648775816935e-07, 4.0508031237072605e-08, 3.798017334318996e-09, 3.2642558266414184e-10, 2.5896992271723294e-11, 1.9077865514937035e-12, 1.3117377449396117e-13, 8.45542660822074e-15], [0.0950018821862495, 0.09798073684378389, 0.05052649785206233, 0.017370264587584075, 0.004478730537481161, 0.0009238328927564692, 0.0001588000600088894, 2.339705056730841e-05, 3.0163353106807682e-06, 3.456571941373861e-07, 3.564955324836491e-08, 3.3424883180721754e-09, 2.872745437246491e-10, 2.2790942358076746e-11, 1.6789692359016815e-12, 1.154409709828549e-13, 7.441294279232672e-15], [0.05573832405188238, 0.057486040648482006, 0.029644279099268332, 0.010191265837781825, 0.002627705139039009, 0.0005420197575169834, 9.316919834157738e-05, 1.3727226833487629e-05, 1.7697067797694046e-06, 2.0279969464102513e-07, 2.0915862986447257e-08, 1.9610632202748483e-09, 1.685461513129762e-10, 1.3371618555007118e-11, 9.850639712628177e-13, 6.773009230376743e-14, 4.365863731922166e-15], [0.024526572763226145, 0.025295621689708017, 0.013044392358564904, 0.004484469660176216, 0.0011562708852342503, 0.000238505323724342, 4.099730591628676e-05, 6.040400989729337e-06, 7.787252817861337e-07, 8.923808800464225e-08, 9.2036214609765e-09, 8.62927986865678e-10, 7.416547796255147e-11, 5.883922436315363e-12, 4.334583713913098e-13, 2.98033187291765e-14, 1.9211139968192638e-15], [0.008633955638133493, 0.008904679737211625, 0.0045919462958608085, 0.0015786433954836866, 0.00040703573324953627, 8.395972826591407e-05, 1.4432057996090267e-05, 2.1263694151371827e-06, 2.7413041365956e-07, 3.141399740199933e-08, 3.2399006649387265e-09, 3.037718326741911e-10, 2.6108068697218506e-11, 2.07128512343699e-12, 1.5258798633217149e-13, 1.0491499740341867e-14, 6.762792822486901e-16], [0.0025328035936403592, 0.002612221533663314, 0.0013470648411246756, 0.0004631010202899399, 0.00011940547428355043, 2.462990434346812e-05, 4.233698884747309e-06, 6.237785230537381e-07, 8.041719530923499e-08, 9.215415140538463e-09, 9.504371334676668e-10, 8.911261786494867e-11, 7.658900855045368e-12, 6.076193374128974e-13, 4.476226382511493e-14, 3.077721192781037e-15, 1.9838908933221013e-16], [0.0006368635962631122, 0.0006568329278835447, 0.0003387142063728745, 0.0001164449473917029, 3.0024041325851957e-05, 6.193093493385514e-06, 1.0645470908227687e-06, 1.568466794903422e-07, 2.0220590469244505e-08, 2.3171802354502708e-09, 2.389837144743763e-10, 2.2407020595040324e-11, 1.9258007822691903e-12, 1.5278351521430068e-13, 1.1255296852910567e-14, 7.738810036638181e-16, 4.9884163623551605e-17], [0.00014011976140023165, 0.0001445133207093134, 7.452232166874908e-05, 2.561967482601578e-05, 6.605749695121555e-06, 1.3625755777442725e-06, 2.3421669136160173e-07, 3.450867569690024e-08, 4.4488401104210606e-09, 5.09815200017314e-10, 5.258008347026986e-11, 4.92988828045686e-12, 4.2370571610511107e-13, 3.361471722254326e-14, 2.4763379768798274e-15, 1.7026569303350004e-16, 1.0975281277805106e-17], [2.7403108539425608e-05, 2.826235338410726e-05, 1.457427024490597e-05, 5.01041910852797e-06, 1.291881131331946e-06, 2.664778049645975e-07, 4.5805569114511143e-08, 6.748833827748959e-09, 8.700560663402399e-10, 9.970414680637856e-11, 1.0283044446759112e-11, 9.641342683329625e-13, 8.286378460236386e-14, 6.574003091115236e-15, 4.842954175957322e-16, 3.3298724035151057e-17, 2.146426892973013e-18], [4.82328341917993e-06, 4.974521057289716e-06, 2.5652504319999255e-06, 8.818952555888316e-07, 2.273869342720705e-07, 4.690336413535028e-08, 8.062342332376605e-09, 1.187877581601714e-09, 1.5314054580698877e-10, 1.754915349923901e-11, 1.8099420256422882e-12, 1.6969946397223686e-13, 1.4585043070863827e-14, 1.1571052262700105e-15, 8.524193721721754e-17, 5.860984102862617e-18, 3.777974760952296e-19], [7.717791614197016e-07, 7.959788709062556e-07, 4.1046869013910087e-07, 1.411130803783628e-07, 3.638444648565421e-08, 7.505061571998237e-09, 1.2900647263681055e-09, 1.900736664472659e-10, 2.4504195949233346e-11, 2.8080603593415028e-12, 2.8961091799286856e-13, 2.715380760687993e-14, 2.3337696196205213e-15, 1.851497462607865e-16, 1.3639661016329096e-17, 9.378228486458282e-19, 6.04518113382669e-20], [1.132021703300734e-07, 1.1675170855574394e-07, 6.020627259592456e-08, 2.0698028347134613e-08, 5.3367576041543605e-09, 1.1008191214287232e-09, 1.8922268725486453e-10, 2.787941504515942e-11, 3.594199354312595e-12, 4.118775719605601e-13, 4.247922994936764e-14, 3.9828361628339715e-15, 3.4231007935670964e-16, 2.7157189725398028e-17, 2.0006231144860927e-18, 1.375569426577285e-19, 8.86688392996725e-21], [1.5326900999702027e-08, 1.5807487377338438e-08, 8.151571449100242e-09, 2.8023900110798575e-09, 7.225652584202341e-10, 1.4904436587674444e-10, 2.5619627132558765e-11, 3.774707084509345e-12, 4.866332289930255e-13, 5.576577508214156e-14, 5.751435242620696e-15, 5.392523428464006e-16, 4.6346750086174176e-17, 3.67692206905262e-18, 2.7087247818691175e-19, 1.862439241040412e-20, 1.2005233801984188e-21], [1.9269447727309417e-09, 1.987365558919238e-09, 1.024840441893105e-09, 3.523250253334788e-10, 9.084310962124183e-11, 1.8738312574523328e-11, 3.2209777164581204e-12, 4.745676954021654e-13, 6.118101479637145e-14, 7.011043445371716e-15, 7.230879925879293e-16, 6.779645038817611e-17, 5.826854875186895e-18, 4.622738648104878e-19, 3.40549146842596e-20, 2.3415154571178975e-21, 1.5093346346137412e-22], [2.261106194969764e-10, 2.332004861028408e-10, 1.2025633037401067e-10, 4.134235234439918e-11, 1.0659668135885283e-11, 2.1987819913223083e-12, 3.7795440593874966e-13, 5.5686492482376365e-14, 7.179072982696644e-15, 8.22686461587846e-16, 8.484824073248668e-17, 7.955338219289472e-18, 6.83731980382735e-19, 5.424391577212871e-20, 3.996055291850229e-21, 2.747569717944372e-22, 1.7710761309317908e-23], [2.4873902543556353e-11, 2.5653842253568266e-11, 1.3229118776567929e-11, 4.547975877575732e-12, 1.172645260751272e-12, 2.418828849717482e-13, 4.1577883781588195e-14, 6.125941320582847e-15, 7.897530957278308e-16, 9.050182125441012e-17, 9.333957315526723e-18, 8.751482261552143e-19, 7.52157624608178e-20, 5.9672468170600524e-21, 4.395967341528353e-22, 3.022537444186199e-23, 1.9483195957810955e-24]] |
| Legacy trial inputs | {"lambda_home": 1.7601227292299866, "lambda_away": 1.0313557435808944, "rho": -0.060476960468338566, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5379 |
| Legacy p draw | 0.2481 |
| Legacy p away | 0.2140 |
| Legacy p over 1 5 | 0.7742 |
| Legacy p under 3 5 | 0.6938 |
| Legacy p btts yes | 0.5395 |
| Legacy p over 2 5 | 0.5285 |
| Legacy goal margin distribution | {"-1": 0.13418441601887765, "-10": 2.711342963750421e-08, "-11": 2.5080459932946533e-09, "-12": 2.131017614490457e-10, "-13": 1.6740767553928388e-11, "-14": 1.2225091176434772e-12, "-15": 8.298078345725519e-14, "-16": 4.803884676791712e-15, "-2": 0.05741996521185515, "-3": 0.01732617887734102, "-4": 0.0041144143900732795, "-5": 0.000802101191989116, "-6": 0.0001323310862704896, "-7": 1.8899337594868462e-05, "-8": 2.3777107390230535e-06, "-9": 2.671714070535258e-07, "0": 0.24809312538613623, "1": 0.23375826704317426, "10": 5.682364036162687e-06, "11": 8.970456680009002e-07, "12": 1.3007701314691008e-07, "13": 1.7439070864872848e-08, "14": 2.1733743776103505e-09, "15": 2.517644617505447e-10, "16": 2.4873902543556353e-11, "2": 0.1672367982780738, "3": 0.08612042669301333, "4": 0.03490164277252093, "5": 0.011611851155929036, "6": 0.0032694043473564327, "7": 0.0007968705938399918, "8": 0.0001710939673761412, "9": 3.28095380028529e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.5379 |
| Legacy raw p draw | 0.2481 |
| Legacy raw p away | 0.2140 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.7601 |
| Legacy lambda away | 1.0314 |
| Legacy model home team | Strasbourg |
| Legacy model away team | Auxerre |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 9.310457896058361, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,524.8199 |
| Elo away rating | 1,446.2294 |
| Elo rating diff | 138.5904 |
| Elo home expectancy | 0.6895 |

</details>


---

## 2026-11-02 — FC Lorient vs Stade Brestois 29

The model's most likely 1X2 outcome is **FC Lorient win** at **41.1%**. Expected goals are 1.49 for FC Lorient and 1.29 for Stade Brestois 29 (2.78 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.7%; Double Chance 1X: 67.7%; Double Chance X2: 58.9%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Lorient win | 41.1% | 2.43 |
| Draw | 26.5% | 3.77 |
| Stade Brestois 29 win | 32.3% | 3.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Lorient expected goals | 1.49 |
| Stade Brestois 29 expected goals | 1.29 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.56% |
| 2 | 2-1 | 8.87% |
| 3 | 1-0 | 8.60% |
| 4 | 1-2 | 7.71% |
| 5 | 0-1 | 7.40% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T19:45:00+00:00 |
| Fixture id | fdorg:559641 |
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
| Bbs statistics cutoff utc | 2026-11-01T12:21:43.479248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.61 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.71 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.18014473823262145, "-10": 2.6548109139268834e-07, "-11": 3.0759380768950174e-08, "-12": 3.2739168645926535e-09, "-13": 3.2211418589586986e-10, "-14": 2.927977635376535e-11, "-15": 2.2370249929559264e-12, "-2": 0.0942275272143574, "-3": 0.03540775361522254, "-4": 0.010494076694278254, "-5": 0.0025565929294675467, "-6": 0.0005275174672500798, "-7": 9.427423331782728e-05, "-8": 1.484688862183391e-05, "-9": 2.0888653928116145e-06, "0": 0.2652147814489833, "1": 0.20803150379552693, "10": 1.0698058332046074e-06, "11": 1.424872787132407e-07, "12": 1.7433849306680144e-08, "13": 1.971798940665135e-09, "14": 2.060381630683821e-10, "15": 1.8095804142942605e-11, "2": 0.12451798027229782, "3": 0.053787305014907284, "4": 0.018325371210018693, "5": 0.005132125489706849, "6": 0.0012173057263167573, "7": 0.000250082306554128, "8": 4.527438340571579e-05, "9": 7.322420838801687e-06} |
| Raw goal margin distribution | {"-1": 0.18014473823262145, "-10": 2.6548109139268834e-07, "-11": 3.0759380768950174e-08, "-12": 3.2739168645926535e-09, "-13": 3.2211418589586986e-10, "-14": 2.927977635376535e-11, "-15": 2.2370249929559264e-12, "-2": 0.0942275272143574, "-3": 0.03540775361522254, "-4": 0.010494076694278254, "-5": 0.0025565929294675467, "-6": 0.0005275174672500798, "-7": 9.427423331782728e-05, "-8": 1.484688862183391e-05, "-9": 2.0888653928116145e-06, "0": 0.2652147814489833, "1": 0.20803150379552693, "10": 1.0698058332046074e-06, "11": 1.424872787132407e-07, "12": 1.7433849306680144e-08, "13": 1.971798940665135e-09, "14": 2.060381630683821e-10, "15": 1.8095804142942605e-11, "2": 0.12451798027229782, "3": 0.053787305014907284, "4": 0.018325371210018693, "5": 0.005132125489706849, "6": 0.0012173057263167573, "7": 0.000250082306554128, "8": 4.527438340571579e-05, "9": 7.322420838801687e-06} |
| Unadjusted home-win probability | 41.1% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 32.3% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.8% |
| P home draw | 67.7% |
| P draw away | 58.9% |
| P home away | 73.5% |
| Raw p home draw | 67.7% |
| Raw p draw away | 58.9% |
| Raw p home away | 73.5% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5255 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.07023516466326027, 0.08005413000179465, 0.06057378965901603, 0.028009199437299008, 0.009713548436559062, 0.0026949152457026566, 0.0006230617153756721, 0.0001234724972581221, 2.1410038608645998e-05, 3.2999863732348324e-06, 4.5777213373282396e-07, 5.772897844282594e-08, 6.673441102244048e-09, 7.121044259902808e-10, 7.055907112874623e-11], [0.07948272514303371, 0.12763363025831664, 0.0834778190621221, 0.038599976918461135, 0.013386414213190048, 0.003713910728301873, 0.0008586524540309016, 0.00017015964897166901, 2.950555577167155e-05, 4.547770032601271e-06, 6.30863935813571e-07, 7.955733402547781e-08, 9.196788115632431e-09, 9.813638004289033e-10, 9.723871341109289e-11], [0.05978373335004901, 0.08293163693078867, 0.05752113508661059, 0.02659765805590287, 0.009224027998493981, 0.002559103281594929, 0.0005916621248095365, 0.00011725002239823485, 2.0331066125300106e-05, 3.1336814656528855e-06, 4.347024165329311e-07, 5.48196899370909e-08, 6.3371288026649605e-09, 6.762174715126717e-10, 6.700320195961645e-11], [0.02746300946084042, 0.03809652228136343, 0.026423633797379293, 0.012218235528190884, 0.004237265791121582, 0.001175581946717814, 0.0002717933728916568, 5.386144849055057e-05, 9.339534854385794e-06, 1.4395274252041157e-06, 1.9969038246562253e-07, 2.5182663895670406e-08, 2.911103380632375e-09, 3.10635782964579e-10, 3.077943557906023e-11], [0.00946181569445586, 0.013125374075990322, 0.009103720163119614, 0.004209542033040427, 0.0014598628755957254, 0.00040502260793501515, 9.364082275623531e-05, 1.855685551799033e-05, 3.2177448575018896e-06, 4.959595999053746e-07, 6.879921872871466e-08, 8.676169478658787e-09, 1.002960862476723e-09, 1.0702317714687534e-10, 1.0604422178993523e-11], [0.002607899366994183, 0.0036176623863423863, 0.002509199800267002, 0.0011602489794568839, 0.00040237260924403875, 0.00011163377484418479, 2.5809617337388294e-05, 5.1147066611249e-06, 8.86886306815825e-07, 1.3669815270295203e-07, 1.8962685890979797e-08, 2.391356756672667e-09, 2.7643964782632643e-10, 2.949810955402399e-11, 2.922828638919786e-12], [0.0005989987658459124, 0.0008309275013030444, 0.0005763288271943878, 0.000266493299382822, 9.241947729953045e-05, 2.5640749104310167e-05, 5.92811560434929e-06, 1.174778067149443e-06, 2.0370563755326963e-07, 3.139769340749527e-08, 4.355469229210457e-09, 5.492618941026057e-10, 6.349440088622006e-11, 6.7753117475591996e-12, 6.713337062196331e-13], [0.0001179272677770338, 0.0001635879997366682, 0.00011346414685211526, 5.246559503794967e-05, 1.819498982092869e-05, 5.047996186365362e-06, 1.16709168056474e-06, 2.31283227282903e-07, 4.010433850145093e-08, 6.181388692542612e-09, 8.574785381441993e-10, 1.0813537215571005e-10, 1.2500395063548028e-11, 1.3338825524939918e-12, 1.321681349865697e-13], [2.0314708674736982e-05, 2.8180442233399753e-05, 1.9545870363810727e-05, 9.037971444041559e-06, 3.1343549674264174e-06, 8.695916885913543e-07, 2.0104873058035197e-07, 3.984194217480355e-08, 6.9085629524665125e-09, 1.064835240071353e-09, 1.4771330690179161e-10, 1.862791044163687e-11, 2.1533771520529825e-12, 2.297809147199389e-13, 2.276790778712816e-14], [3.1106735632241555e-06, 4.315107740846648e-06, 2.9929458100732393e-06, 1.3839321688682264e-06, 4.799456044899398e-07, 1.331555337470573e-07, 3.078542651777278e-08, 6.1007656184009504e-09, 1.0578681919683319e-09, 1.6305204684518024e-10, 2.261848230623314e-11, 2.8523839291363714e-12, 3.2973415891866644e-13, 3.518501929794632e-14, 3.4863177206877623e-15], [4.286874675233427e-07, 5.946726880581467e-07, 4.124631960497491e-07, 1.9072215860583234e-07, 6.614215910347711e-08, 1.83504014126061e-08, 4.2425944935383026e-09, 8.407573825249122e-10, 1.457867008450615e-10, 2.2470493163580108e-11, 3.117093356793963e-12, 3.930921127314828e-13, 4.544125208569711e-14, 4.8489102154335044e-15, 4.804556583283286e-16], [5.37074399063299e-08, 7.450263904922643e-08, 5.1674807391490726e-08, 2.389432779853893e-08, 8.286517111983169e-09, 2.2990013839649016e-09, 5.315268256500345e-10, 1.0533297569586915e-10, 1.8264659146705498e-11, 2.8151806448199043e-12, 3.905201733785608e-13, 4.9247931468929156e-14, 5.6930363039551086e-15, 6.074881440111233e-16, 6.019313684722964e-17], [6.1679316747782514e-09, 8.556117886977059e-09, 5.93449775029169e-09, 2.7440999148941538e-09, 9.516497427122595e-10, 2.640245649624588e-10, 6.104221593207598e-11, 1.2096770919006839e-11, 2.097571023241339e-12, 3.233042181807825e-13, 4.484856755828409e-14, 5.6557876702798515e-15, 6.538062325456083e-16, 6.976585314871521e-17, 6.912769553190571e-18], [6.538566588124384e-10, 9.070260419487042e-10, 6.291105471552034e-10, 2.90899461344097e-10, 1.0088349773296173e-10, 2.798899679720713e-11, 6.4710281274783295e-12, 1.2823673530407006e-12, 2.2236153919906672e-13, 3.4273177302544305e-14, 4.754354633352488e-15, 5.995647526647936e-16, 6.930938623576578e-17, 7.395812736634793e-18, 7.32816224549381e-19], [6.43636796001397e-11, 8.928491094516131e-11, 6.192774692194634e-11, 2.863526657327438e-11, 9.930667582125797e-12, 2.7551525214359516e-12, 6.36988513410524e-13, 1.2623237880715266e-13, 2.1888600003549248e-14, 3.3737483178442754e-15, 4.680043465219476e-16, 5.901934792580212e-17, 6.822607170604379e-18, 7.280215242098547e-19, 7.213622136745783e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3781178217846064, "lambda_away": 1.3871940122106925, "rho": -0.060476960468338566, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3633 |
| Legacy p draw | 0.2692 |
| Legacy p away | 0.3675 |
| Legacy p over 1 5 | 0.7702 |
| Legacy p under 3 5 | 0.6996 |
| Legacy p btts yes | 0.5684 |
| Legacy p over 2 5 | 0.5222 |
| Legacy goal margin distribution | {"-1": 0.19479892110647185, "-10": 5.439878367661104e-07, "-11": 6.763276346555011e-08, "-12": 7.721808104632568e-09, "-13": 8.093431394013737e-10, "-14": 7.055907112874623e-11, "-2": 0.10967234208974433, "-3": 0.04424598632093495, "-4": 0.01407634164696487, "-5": 0.0036806727412675316, "-6": 0.0008150632133243821, "-7": 0.00015632038439451854, "-8": 2.6418726851981608e-05, "-9": 3.988691048371913e-06, "0": 0.269185828660432, "1": 0.1934767592769481, "10": 5.09425434451787e-07, "11": 6.292130360703544e-08, "12": 7.1368854636489015e-09, "13": 7.431415697575996e-10, "14": 6.43636796001397e-11, "2": 0.10824189954561837, "3": 0.04338317286276677, "4": 0.013711544363591538, "5": 0.0035618278264486184, "6": 0.0007835850716222188, "7": 0.0001492999351180501, "8": 2.5067154215159942e-05, "9": 3.759868797238941e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3633 |
| Legacy raw p draw | 0.2692 |
| Legacy raw p away | 0.3675 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.3781 |
| Legacy lambda away | 1.3872 |
| Legacy model home team | Lorient |
| Legacy model away team | Brest |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 9.147053040269235, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,498.9880 |
| Elo away rating | 1,450.3969 |
| Elo rating diff | 108.5911 |
| Elo home expectancy | 0.6514 |

</details>


---
