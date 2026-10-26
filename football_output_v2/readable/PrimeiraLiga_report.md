# Primeira Liga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,602 |
| Training data through | 2026-10-19 |
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
| Training sha256 | 9aa0490d3c785bbac1db1df68144a198798f6e850afaca727c2a89dab1ac3be4 |
| Training as of utc | 2026-10-26T11:01:08.952231+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1602, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1304, 'tuning_matches': 197, 'audit_matches': 95, 'audit_matchdays': 39, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8842989647630213, 'audit_candidate_poisson_score': 0.8712722566731389, 'audit_gain': 0.013026708089882377, 'audit_gain_lower95': 0.0016952519471041152, 'audit_baseline_briers': [0.6014046160164832, 0.17871464745604035, 0.23959646082409236, 0.25147632394995034], 'audit_candidate_briers': [0.596003028732249, 0.17800083852090984, 0.2385408793338746, 0.24933758220041838], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1441.464 |
| Base scoring parameter | 0.092 |
| Home-advantage parameter | 0.178 |
| Dixon-Coles low-score adjustment | 0.043 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1602, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-19'} |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 7, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Additional event odds calls used before this league | 5.00 |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE': 1} |
| Shot features applied fixtures | 1 |
| Goal rate features used | {'shot_features': 1} |
| Legacy comparison status | {'AVAILABLE': 1} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-26 — Santa Clara vs Benfica

The model's most likely 1X2 outcome is **Benfica win** at **69.6%**. Expected goals are 0.80 for Santa Clara and 1.69 for Benfica (2.49 combined). The most likely exact score is 0-1 at 17.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 47.6%; Under 3.5 goals: 75.0%; Double Chance 1X: 30.4%; Double Chance X2: 87.7%; Double Chance 12 (either team wins): 81.9%; Under 4.5 goals: 88.4%; BTTS Yes (both teams score): 42.8%; BTTS No (at least one team does not score): 57.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Santa Clara win | 12.3% | 8.16 |
| Draw | 18.1% | 5.51 |
| Benfica win | 69.6% | 1.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Santa Clara expected goals | 0.80 |
| Benfica expected goals | 1.69 |
| Expected total goals | 2.49 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 71.9% |
| Under 1.5 | 28.1% |
| Over 2.5 | 47.6% |
| Under 2.5 | 52.4% |
| Over 3.5 | 25.0% |
| Under 3.5 | 75.0% |
| Over 4.5 | 11.6% |
| Under 4.5 | 88.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.13% |
| 2 | 0-2 | 13.96% |
| 3 | 1-2 | 11.19% |
| 4 | 1-1 | 8.48% |
| 5 | 0-3 | 7.84% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T18:45:00+00:00 |
| Fixture id | 7f4d1fc269584543a305935a2d3552fd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 11.00 |
| Matched home-team name | Santa Clara |
| Matched away-team name | Benfica |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7109 |
| Dc lambda away | 1.7675 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.0142 |
| Shot lambda away | 1.4934 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 42.8% |
| P btts no | 57.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.20 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.55 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.99 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.66 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.31148159797739156, "-10": 5.655944581123236e-06, "-11": 8.578241934439906e-07, "-12": 1.1944531506338043e-07, "-13": 1.5369413779198055e-08, "-14": 1.8320027924130894e-09, "-15": 1.8881731143887603e-10, "-2": 0.21406956734129468, "-3": 0.10875263202356165, "-4": 0.04303346280809812, "-5": 0.01389769770610588, "-6": 0.0037846249464803814, "-7": 0.0008900746331648527, "-8": 0.00018409811353172775, "-9": 3.396903676112935e-05, "0": 0.18132387736014166, "1": 0.08658765498664606, "10": 1.927549631873234e-09, "11": 1.3910956530254071e-10, "12": 9.21692603260526e-12, "13": 5.643292536844093e-13, "14": 3.200808348632142e-14, "15": 1.5697613369474343e-15, "2": 0.027758060848143546, "3": 0.006710150294301907, "4": 0.001263447045851019, "5": 0.00019415648010959763, "6": 2.5158813499651494e-05, "7": 2.815477175621963e-06, "8": 2.770978807241957e-07, "9": 2.4329062662830104e-08} |
| Raw goal margin distribution | {"-1": 0.26350966162749756, "-10": 4.784860654477059e-06, "-11": 7.257088843069122e-07, "-12": 1.0104929074373691e-07, "-13": 1.3002338021469378e-08, "-14": 1.5498521873014263e-09, "-15": 1.5973715997913768e-10, "-2": 0.18110026281213487, "-3": 0.09200341031931054, "-4": 0.036405788646443615, "-5": 0.011757284037701073, "-6": 0.003201746894551432, "-7": 0.0007529923659423157, "-8": 0.00015574477567219667, "-9": 2.873739392908511e-05, "0": 0.2300570676937061, "1": 0.12790940922845553, "10": 2.847423627645957e-09, "11": 2.0549606429022034e-10, "12": 1.3615469363556864e-11, "13": 8.336410249271722e-13, "14": 4.728312656003759e-14, "15": 2.3188899765166657e-15, "2": 0.04100488880269525, "3": 0.009912398714466553, "4": 0.0018663949872665443, "5": 0.00028681271796222093, "6": 3.716521682133112e-05, "7": 4.159091989332036e-06, "8": 4.0933579073547083e-07, "9": 3.593948851905745e-08} |
| Unadjusted home-win probability | 18.1% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 58.9% |
| Raw p over 1 5 | 70.5% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 44.4% |
| P home draw | 30.4% |
| P draw away | 87.7% |
| P home away | 81.9% |
| Raw p home draw | 41.1% |
| Raw p draw away | 81.9% |
| Raw p home away | 77.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4761 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:01:11Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 3.52, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 7.75 |
| Reference draw odds | 5.00 |
| Reference away odds | 1.30 |
| Market reference 1x2 last update utc | 2026-10-26T11:00:51Z |
| Market reference home last update utc | 2026-10-26T11:00:51Z |
| Market reference draw last update utc | 2026-10-26T11:00:51Z |
| Market reference away last update utc | 2026-10-26T11:00:51Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-26T11:00:50Z |
| Market reference under 2 5 last update utc | 2026-10-26T11:00:50Z |
| Home probability edge | +2.5% |
| Draw probability edge | +2.1% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | 0.0835 |
| Raw edge prob draw | 0.0696 |
| Raw edge prob away | -0.1532 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06600316637102525, 0.1607884254659671, 0.14337350186725206, 0.08790745986952532, 0.040424423272442694, 0.014871402261742373, 0.004559096278258256, 0.0011980055127820705, 0.00027545262940882007, 5.6296643964542556e-05, 1.0355250249835077e-05, 1.7315937373758771e-06, 2.6542562781166914e-07, 3.755584983060792e-08, 4.934323864670868e-09, 6.050823499009076e-10, 6.956208569609142e-11], [0.050741416092743144, 0.08559560188330881, 0.09974580093059669, 0.061157744480417685, 0.02812351253162935, 0.010346123308978019, 0.0031717904903768124, 0.0008334595851774468, 0.00019163403823574466, 3.9165911195690354e-05, 7.204209401001483e-06, 1.2046800975879141e-06, 1.846581933814687e-07, 2.6127828867928577e-08, 3.4328385616768656e-09, 4.209594020777637e-10, 4.839475817912118e-11], [0.016296885835327728, 0.02997662369076579, 0.02867896710898334, 0.021273903918299267, 0.009782847757482933, 0.0035989298668879168, 0.001103316787015537, 0.00028992140383018707, 6.666047205531404e-05, 1.3623979084391303e-05, 2.5060057382150075e-06, 4.1905156683106045e-07, 6.423390360614002e-08, 9.08864323974628e-09, 1.194123137610642e-09, 1.4643198419743117e-10, 1.683426104737406e-11], [0.003779280246230193, 0.006951638669370901, 0.006393450212867517, 0.004077789641671862, 0.002268661856953426, 0.000834598995840842, 0.000255861357846846, 6.723335031773683e-05, 1.5458696083941853e-05, 3.1594278532084916e-06, 5.811477161388012e-07, 9.717889200913027e-08, 1.4895970033164159e-08, 2.1076744482401263e-09, 2.769195311999659e-10, 3.395786844711086e-11, 3.903898626957755e-12], [0.0006573169556994627, 0.001209074127760576, 0.0011119903676183177, 0.0006818013603881538, 0.0003261434474933098, 0.00014515887561478188, 4.4501068421369413e-05, 1.1693660769511108e-05, 2.6886767815421093e-06, 5.495082033925998e-07, 1.0107698363070403e-07, 1.6901983788422565e-08, 2.590803813545376e-09, 3.6658042316514685e-10, 4.816364264165156e-11, 5.906172936490455e-12, 6.789913935043188e-13], [9.14598658156652e-05, 0.00016823201733553745, 0.00015472366706630915, 9.486665510960816e-05, 4.362462328320654e-05, 1.6694463648569875e-05, 6.191931778393205e-06, 1.6270699174880086e-06, 3.7410569669523105e-07, 7.645922733487688e-08, 1.4063972151880904e-08, 2.3517621992006975e-09, 3.604875351031012e-10, 5.100643764416056e-11, 6.701546727197413e-12, 8.217919522260268e-13, 9.447567296330322e-14], [1.0604862416435282e-05, 1.9506669750407118e-05, 1.7940363099936983e-05, 1.0999883023800553e-05, 5.058318463091219e-06, 1.8608623832589918e-06, 5.934358678322255e-07, 1.8866037537883245e-07, 4.3377927654668284e-08, 8.865523463456001e-09, 1.630731560440673e-09, 2.726891662946759e-10, 4.1798888272078417e-11, 5.914247180932998e-12, 7.770510090456317e-13, 9.528759429688637e-14, 1.0954548255026636e-14], [1.0539808678628946e-06, 1.938700937862793e-06, 1.7830310971825912e-06, 1.093240609877966e-06, 5.027289062603297e-07, 1.8494472371853762e-07, 5.6698136917311595e-08, 1.5498209734227112e-08, 4.311183308206396e-09, 8.811139406760105e-10, 1.6207281130408262e-10, 2.7101640064905375e-11, 4.154248004993741e-12, 5.877967230253581e-13, 7.722843208398272e-14, 9.470306863948802e-15, 1.088734942848977e-15], [9.165759751743434e-08, 1.6859572662794837e-07, 1.550581719742285e-07, 9.507175212116268e-08, 4.3718937558915325e-08, 1.6083393509731086e-08, 4.930654029890181e-09, 1.2956407035313239e-09, 3.098884442836801e-10, 7.662452839892339e-11, 1.4094377763374259e-11, 2.3568465926410027e-12, 3.612668913064677e-13, 5.111671103704842e-14, 6.716035139431966e-15, 8.235686257403019e-16, 9.467992469081474e-17], [7.08519306929278e-09, 1.3032561469762567e-08, 1.1986099517828206e-08, 7.349109484200217e-09, 3.379502864782717e-09, 1.2432569837342702e-09, 3.811428261908506e-10, 1.0015388556532521e-10, 2.302798345260819e-11, 4.895805825501762e-12, 1.089504747558529e-12, 1.8218580451435074e-13, 2.7926170266056324e-14, 3.951355660351537e-15, 5.191539699039027e-16, 6.3662400905416e-17, 7.318820964000546e-18], [4.929211104147138e-10, 9.066830795430398e-10, 8.338800969976791e-10, 5.112819329103851e-10, 2.351140312573981e-10, 8.64941303588661e-11, 2.651633389170992e-11, 6.967765592608761e-12, 1.6020705523560705e-12, 3.274290598918486e-13, 6.265099989934035e-14, 1.267477515217177e-14, 1.94284033230288e-15, 2.7489817153823284e-16, 3.611785152761997e-17, 4.429031225975701e-18, 5.091747424833032e-19], [3.117528712424125e-11, 5.734407542753475e-11, 5.273957820394617e-11, 3.233653565072085e-11, 1.487002134118463e-11, 5.470407518620064e-12, 1.677051976655675e-12, 4.406832825261423e-13, 1.013245495226844e-13, 2.0708577375313934e-14, 3.809152481176523e-15, 6.625924122967109e-16, 1.2287687404002605e-16, 1.7386208962369314e-17, 2.2843095332982054e-18, 2.8011849611361476e-19, 3.2203264291061576e-20], [1.807402776053598e-12, 3.3245512929810982e-12, 3.057603276397349e-12, 1.8747267369230833e-12, 8.620968828586998e-13, 3.1714959659859166e-13, 9.722792242823369e-14, 2.5548832478236455e-14, 5.87434115233148e-15, 1.2005900727425645e-15, 2.2083750957778736e-16, 3.6928209298338527e-17, 5.888270978445485e-18, 1.0079741116225257e-18, 1.324339812940651e-19, 1.6240009129090847e-20, 1.8670002635643405e-21], [9.672468447995496e-14, 1.7791616739305435e-13, 1.636302190595064e-13, 1.003275830476225e-13, 4.613584204386973e-14, 1.6972528243496564e-14, 5.203234300683381e-15, 1.367267325816791e-15, 3.1437032299325624e-16, 6.425059068977941e-17, 1.1818305647339054e-17, 1.976244277211186e-18, 3.0292664304902946e-19, 4.458665639475535e-20, 7.087316244507552e-21, 8.690977903623179e-22, 9.991409430694514e-23], [4.806567161774419e-15, 8.84123853531348e-15, 8.131322855525782e-15, 4.9856070215130525e-15, 2.292641475556655e-15, 8.434206567444094e-16, 2.585657969229765e-16, 6.794400276384516e-17, 1.5622093566497473e-17, 3.1928228145122873e-18, 5.872904123464502e-19, 9.820606701959775e-20, 1.5053419535400727e-20, 2.1299524396709167e-21, 2.9110700482178825e-22, 4.3188322835955426e-23, 4.9650594083221795e-24], [2.2293049739962654e-16, 4.1006016101906735e-16, 3.7713398932932436e-16, 2.312344373306684e-16, 1.063336238323108e-16, 3.9118185639944096e-17, 1.1992384539424692e-17, 3.151269881741115e-18, 7.245589153313977e-19, 1.4808439249714678e-19, 2.7238762995687125e-20, 4.554836462590445e-21, 6.981835875051559e-22, 9.878804161723064e-23, 1.297939451495857e-23, 1.6556706862829323e-24, 2.3028143085539314e-25], [9.693379845901737e-18, 1.783008133384314e-17, 1.6398397949187535e-17, 1.0054448631501074e-17, 4.6235585450209675e-18, 1.7009222009258928e-18, 5.214483435632332e-19, 1.370223290082591e-19, 3.150499760672745e-20, 6.438949728584105e-21, 1.1843856239031113e-21, 1.9805168194958032e-22, 3.0358155545357825e-23, 4.295464383735635e-24, 5.643651392288946e-25, 6.920652028777004e-26, 8.276330331322252e-27]] |
| Legacy trial inputs | {"lambda_home": 0.6957059681987138, "lambda_away": 1.8394080926666176, "rho": 0.04515742613058527, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1184 |
| Legacy p draw | 0.1847 |
| Legacy p away | 0.6969 |
| Legacy p over 1 5 | 0.7225 |
| Legacy p under 3 5 | 0.7442 |
| Legacy p btts yes | 0.4090 |
| Legacy p over 2 5 | 0.4772 |
| Legacy goal margin distribution | {"-1": 0.2842283360284952, "-10": 1.1626320921866511e-05, "-11": 1.9256234941769017e-06, "-12": 2.9278221667704894e-07, "-13": 4.113902427510917e-08, "-14": 5.372117527796006e-09, "-15": 6.534771080800288e-10, "-16": 6.956208569609142e-11, "-2": 0.2151948655126525, "-3": 0.11989784042233698, "-4": 0.05194386351296132, "-5": 0.018349136701103913, "-6": 0.00546247923448352, "-7": 0.0014038619462819755, "-8": 0.0003172243678316018, "-9": 6.393517428075449e-05, "0": 0.18469897216505626, "1": 0.08783883485956795, "10": 5.534254489828029e-10, "11": 3.46685622778494e-11, "12": 1.993686124298054e-12, "13": 1.0595311145322927e-13, "14": 5.233025720742674e-15, "15": 2.407605787334697e-16, "16": 9.693379845901737e-18, "2": 0.024460629823044283, "3": 0.0051545971245937775, "4": 0.0008446275659023142, "5": 0.0001128481061152896, "6": 1.2706211318806241e-05, "7": 1.2350891683844288e-06, "8": 1.0555725495100498e-07, "9": 8.046537445168797e-09} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1394 |
| Legacy raw p draw | 0.2090 |
| Legacy raw p away | 0.6517 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.6957 |
| Legacy lambda away | 1.8394 |
| Legacy model home team | Santa Clara |
| Legacy model away team | Benfica |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 29.4% |
| Market reference home draw last update utc | 2026-10-26T11:00:30Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.4% |
| Market reference draw away last update utc | 2026-10-26T11:00:30Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.1% |
| Market reference home away last update utc | 2026-10-26T11:00:30Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home draw odds | 3.25 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 80.9% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-26T11:01:11Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 3.88 |
| Market reference over 1 5 last update utc | 2026-10-26T11:01:11Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.0% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-26T11:01:11Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market reference under 3 5 last update utc | 2026-10-26T11:01:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 46.2% |
| Market reference btts yes odds | 2.14 |
| Market reference btts yes opposite odds | 1.84 |
| Market reference btts yes last update utc | 2026-10-26T11:00:50Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,479.7454 |
| Elo away rating | 1,690.3969 |
| Elo rating diff | -150.6514 |
| Elo home expectancy | 0.2958 |

</details>


---
