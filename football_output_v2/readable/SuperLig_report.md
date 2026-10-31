# Super Lig — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,831 |
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
| Training sha256 | 36930ef41a7cb5e7e2f4d6e9884819c8b34ead9559d248ba647b034c279b2986 |
| Training as of utc | 2026-10-31T12:03:04.144735+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-31', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1800, 'tune_start_date': '2025-11-01', 'audit_start_date': '2026-05-02', 'training_shot_matches': 1504, 'tuning_matches': 190, 'audit_matches': 92, 'audit_matchdays': 35, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8870429599301157, 'audit_candidate_poisson_score': 0.8757927199223782, 'audit_gain': 0.011250240007737555, 'audit_gain_lower95': 0.003237169053261783, 'audit_baseline_briers': [0.6169227320749828, 0.17699394397921853, 0.20447088220876403, 0.24805987628525067], 'audit_candidate_briers': [0.6121147719206541, 0.17579562249955846, 0.2012281859789952, 0.2476236522689705], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1653.144 |
| Base scoring parameter | 0.124 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1831, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 53.00 |
| Over 1 5 in window quote fixtures | 6 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 2, 'ANCHORED_ALTERNATE': 5} |
| Shot features applied fixtures | 7 |
| Goal rate features used | {'shot_features': 7} |
| Legacy comparison status | {'AVAILABLE': 7} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-31 — Fenerbahce vs Goztepe

The model's most likely 1X2 outcome is **Fenerbahce win** at **69.6%**. Expected goals are 2.45 for Fenerbahce and 1.04 for Goztepe (3.49 combined). The most likely exact score is 2-0 at 10.5%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.6%; Under 3.5 goals: 58.1%; Double Chance 1X: 87.1%; Double Chance X2: 30.4%; Double Chance 12 (either team wins): 82.5%; Under 4.5 goals: 76.1%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 69.6% | 1.44 |
| Draw | 17.5% | 5.70 |
| Goztepe win | 12.9% | 7.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 2.45 |
| Goztepe expected goals | 1.04 |
| Expected total goals | 3.49 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 64.6% |
| Under 2.5 | 35.4% |
| Over 3.5 | 41.9% |
| Under 3.5 | 58.1% |
| Over 4.5 | 23.9% |
| Under 4.5 | 76.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.51% |
| 2 | 2-1 | 10.26% |
| 3 | 1-0 | 8.29% |
| 4 | 1-1 | 8.14% |
| 5 | 3-0 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 69.6% | 70.5% | 1.40 | -2.6% |
| Draw | 17.5% | 16.9% | 5.51 | -3.4% |
| Goztepe win | 12.9% | 12.6% | 7.32 | -5.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T16:00:00+00:00 |
| Fixture id | dc20aff5555a04cd21c2355e222a3297 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:03:01Z |
| Market best draw last update utc | 2026-10-31T12:03:01Z |
| Market best away last update utc | 2026-10-31T12:03:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Fenerbahce |
| Matched away-team name | Goztep |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5518 |
| Dc lambda away | 1.0230 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 2.0452 |
| Shot lambda away | 1.1230 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.84 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.66 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.39 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.19 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.0833461368344368, "-10": 9.47598895725781e-09, "-11": 8.278430259846136e-10, "-12": 6.646197783505602e-11, "-13": 4.935122654342751e-12, "-14": 3.4082400523164706e-13, "-15": 2.199680771725559e-14, "-16": 1.3320137157536622e-15, "-17": 7.551405526875906e-17, "-18": 3.644881782165168e-18, "-2": 0.03367629415877778, "-3": 0.009380892435724195, "-4": 0.0020742878175574815, "-5": 0.0003784389834867291, "-6": 5.861457389496388e-05, "-7": 7.875490120206474e-06, "-8": 9.334898654004704e-07, "-9": 9.892725106376939e-08, "0": 0.17532152686778732, "1": 0.23200620820226736, "10": 5.4680188096304345e-05, "11": 1.122368511974395e-05, "12": 2.1171067971878147e-06, "13": 3.693596769781169e-07, "14": 5.993268469068106e-08, "15": 9.088144858358125e-09, "16": 1.2930231627253458e-09, "17": 1.722294549037743e-10, "18": 1.9531927622935593e-11, "2": 0.20925389127898944, "3": 0.13695422365527604, "4": 0.07115121433199476, "5": 0.030499392767817993, "6": 0.011098977305378368, "7": 0.003503781118118594, "8": 0.0009757779721888119, "9": 0.00024296256816915964} |
| Raw goal margin distribution | {"-1": 0.08619976008220337, "-10": 1.6057379058759755e-08, "-11": 1.4940015262207255e-09, "-12": 1.2778338937982248e-10, "-13": 1.0111430656315256e-11, "-14": 7.443059159919788e-13, "-15": 5.121076706668783e-14, "-16": 3.305989757739988e-15, "-17": 1.9950014547972134e-16, "-18": 1.0122237558140838e-17, "-2": 0.03596989092568959, "-3": 0.010504411393324281, "-4": 0.0024492479506175373, "-5": 0.0004728292676524563, "-6": 7.766382647141339e-05, "-7": 1.108252700334075e-05, "-8": 1.3965895381238352e-06, "-9": 1.5747043295636724e-07, "0": 0.18922738669892525, "1": 0.21259359125076469, "10": 8.231802012457848e-05, "11": 1.7995061016572552e-05, "12": 3.616252204976945e-06, "13": 6.723245062902271e-07, "14": 1.1627860968628898e-07, "15": 1.8797135243929974e-08, "16": 2.8511096140630787e-09, "17": 4.0423848091785046e-10, "18": 4.818956296654435e-11, "2": 0.1985652158537542, "3": 0.13624412970725877, "4": 0.07463814822856635, "5": 0.033854349974017955, "6": 0.013065045855254913, "7": 0.004380392007670717, "8": 0.001296955244983654, "9": 0.00034358741866102156} |
| Unadjusted home-win probability | 67.5% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.8% |
| Raw p btts yes | 59.9% |
| P home draw | 87.1% |
| P draw away | 30.4% |
| P home away | 82.5% |
| Raw p home draw | 86.4% |
| Raw p draw away | 32.5% |
| Raw p home away | 81.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9368 |
| Totals anchor target over 2 5 | 0.6464 |
| Totals anchor reference over odds | 1.51 |
| Totals anchor reference under odds | 2.67 |
| Totals anchor reference last update utc | 2026-10-31T12:03:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6842 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.13, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.78, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.05, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.40 |
| Reference draw odds | 5.51 |
| Reference away odds | 7.32 |
| Market reference 1x2 last update utc | 2026-10-31T12:03:01Z |
| Market reference home last update utc | 2026-10-31T12:03:01Z |
| Market reference draw last update utc | 2026-10-31T12:03:01Z |
| Market reference away last update utc | 2026-10-31T12:03:01Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-10-31T12:03:02Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:03:02Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0295 |
| Raw ev home | -0.0549 |
| Raw edge prob draw | 0.0199 |
| Raw ev draw | 0.0426 |
| Raw edge prob away | 0.0097 |
| Raw ev away | -0.0068 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.03326569105114088, 0.0215459787763215, 0.014824058461687696, 0.005150619313181231, 0.0013421870625651465, 0.0002798057478341728, 4.860925543630549e-05, 7.238265625435717e-06, 9.43100808577269e-07, 1.0922679623552734e-07, 1.1385255549179113e-08, 1.078856507640084e-09, 9.371217704590815e-11, 7.513914734572648e-12, 5.594378091943655e-13, 3.8875334875497297e-14, 2.5326066803873754e-15, 1.5528603977357018e-16, 8.992356103562906e-18], [0.06347663240088827, 0.07749266145794366, 0.03790905937254214, 0.013171503192150796, 0.0034323292218079496, 0.000715537700747613, 0.0001243067919053646, 1.851016994152045e-05, 2.4117595487799955e-06, 2.793219626235714e-07, 2.911512590839165e-08, 2.7589229702703954e-09, 2.3964695584174465e-10, 1.921507801182164e-11, 1.4306312389960469e-12, 9.941456867102124e-14, 6.476548730715908e-15, 3.971076960278674e-16, 2.2995845726730754e-17], [0.09006575130889014, 0.09388003953438276, 0.047167650933681984, 0.01684151805753289, 0.004388689257800439, 0.0009149100852185046, 0.0001589427607469856, 2.3667713302752865e-05, 3.0837552402834853e-06, 3.5715026666005366e-07, 3.7227559495694344e-08, 3.5276498320131287e-09, 3.0642049547136633e-10, 2.4569031992175707e-11, 1.8292522496278747e-12, 1.271147437790242e-13, 8.281128646261419e-15, 5.077549871015544e-16, 2.9403246190288186e-17], [0.07677402520201652, 0.08002540828710739, 0.04170724378894509, 0.013969833035150177, 0.003741015144887066, 0.0007798894576390573, 0.00013548630130688383, 2.0174878809902206e-05, 2.628660718350169e-06, 3.0444273405799413e-07, 3.17335896208739e-08, 3.007046220910525e-09, 2.6119956254016133e-10, 2.094318266315578e-11, 1.5592948071029249e-12, 1.0835540036710249e-13, 7.059015998309443e-15, 4.3282150661787096e-16, 2.5063973055554347e-17], [0.04908289938234875, 0.051161562164442835, 0.026664128199886443, 0.009264451703993067, 0.0023273446955987855, 0.0004985961811684059, 8.661862494813803e-05, 1.289813246175219e-05, 1.6805461119124056e-06, 1.9463525644430062e-07, 2.0287806745883496e-08, 1.922454198677949e-09, 1.6698918433855296e-10, 1.3389321775131126e-11, 9.96882864003352e-13, 6.92733929184804e-14, 4.5129452451102174e-15, 2.767099211477004e-16, 1.602381097474829e-17], [0.02510360508454356, 0.02616674377932886, 0.01363745322050614, 0.00473833330607006, 0.0012347504785013412, 0.00024814765672874733, 4.430137137428813e-05, 6.5967908930090675e-06, 8.595206569028763e-07, 9.954682129197345e-08, 1.0376263321627493e-08, 9.832453176979474e-10, 8.54071497359959e-11, 6.848011230437775e-12, 5.098589131531325e-13, 3.543009725536576e-14, 2.308160207058947e-15, 1.4152416973894452e-16, 8.195429115259552e-18], [0.010699432255954426, 0.011152553646496966, 0.005812432373165097, 0.002019529706736978, 0.0005262642179575467, 0.00010971030579191728, 1.837372258286931e-05, 2.811624745877847e-06, 3.663371460056962e-07, 4.242794877955026e-08, 4.422477413335895e-09, 4.1906995558063906e-10, 3.640146543482239e-11, 2.9186976134036127e-12, 2.1730746970423358e-13, 1.5100696658069472e-14, 9.837632359235296e-16, 6.031915581855418e-17, 3.49298191761251e-18], [0.003908756197055741, 0.004074292180735249, 0.0021234193100229913, 0.0007377820680114366, 0.00019225679213824405, 4.0079775018565594e-05, 6.962859186372904e-06, 9.995178443593476e-07, 1.3383164222237942e-07, 1.5499935300598535e-08, 1.6156358190029699e-09, 1.530961874135048e-10, 1.3298318097307314e-11, 1.0662694160593569e-12, 7.938756922361167e-14, 5.51664240027685e-15, 3.593920268724289e-16, 2.203601728266775e-17, 1.276069083859406e-18], [0.0012494661223336509, 0.0013023810633551746, 0.0006787684771389152, 0.00023583811657015597, 6.145646759606605e-05, 1.2811830298900097e-05, 2.2257353053909406e-06, 3.314278979944478e-07, 4.162939076245467e-08, 4.954682021623449e-09, 5.16451300644834e-10, 4.8938457654561624e-11, 4.250916943634853e-12, 3.4084180375593067e-13, 2.5376890570467527e-14, 1.7634401944453183e-15, 1.148826223933253e-16, 7.043994477473813e-18, 4.0790599609171e-19], [0.0003550241246757581, 0.00037005941077327054, 0.00019286572092379702, 6.701119734572579e-05, 1.7462281068658812e-05, 3.6403618762116016e-06, 6.324218915839815e-07, 9.417214062502181e-08, 1.2270041825601571e-08, 1.3699493586403275e-09, 1.4674481178140138e-10, 1.3905405501785061e-11, 1.2078583324569002e-12, 9.684701399134272e-14, 7.210606354773107e-15, 5.010650551146493e-16, 3.264282378418473e-17, 2.001485217474522e-18, 1.159026776508163e-19], [9.078910917547652e-05, 9.463403163599457e-05, 4.9320893359428726e-05, 1.7136545065372354e-05, 4.4655696112010586e-06, 9.309373331163525e-07, 1.6172709449651676e-07, 2.408232050230933e-08, 3.13777596919534e-09, 3.634067676572813e-10, 3.6516907425286186e-11, 3.555981947378461e-12, 3.0888149393816793e-13, 2.4766356750007358e-14, 1.8439437831521003e-15, 1.2813565848339742e-16, 8.347638051484087e-18, 5.118329918800714e-19, 2.963939665953788e-20], [2.1106535820000668e-05, 2.200039846911199e-05, 1.1466058118856431e-05, 3.983882048608489e-06, 1.0381499037880267e-06, 2.164231188745228e-07, 3.759810779129661e-08, 5.5986270261590596e-09, 7.294661385095714e-10, 8.448433989988875e-11, 8.806225512554959e-12, 8.044482242339826e-13, 7.18083741006928e-14, 5.7576508969221525e-15, 4.2867768901603034e-16, 2.978881377029444e-17, 1.9406482026991947e-18, 1.18990278405473e-19, 6.890528973784932e-21], [4.497918713336854e-06, 4.6884057535066975e-06, 2.4434799637816965e-06, 8.489871464924424e-07, 2.212354466559199e-07, 4.612095536122953e-08, 8.012363282290817e-09, 1.193098170382443e-09, 1.5545324079371692e-10, 1.800407687269682e-11, 1.8766550259399286e-12, 1.7783013113629592e-13, 1.4891041788593304e-14, 1.226987030699103e-15, 9.135357009121634e-17, 6.348159832962571e-18, 4.1356279123041634e-19, 2.535748189610409e-20, 1.4684095713427244e-21], [8.847980152172505e-07, 9.222692470932596e-07, 4.806636935804604e-07, 1.6700660684109907e-07, 4.3519835855735263e-08, 9.072580534312371e-09, 1.5761341147295124e-09, 2.3469763692785075e-10, 3.057963642284906e-11, 3.5416316963547438e-12, 3.691619942520675e-13, 3.4981456336388525e-14, 3.038576869402339e-15, 2.3487016609702047e-16, 1.7970413129087774e-17, 1.248764056992086e-18, 8.135307909486766e-20, 4.988140311663293e-21, 2.888549031350078e-22], [1.6161884305582413e-07, 1.6846340762256327e-07, 8.779891988833045e-08, 3.0505735903702185e-08, 7.949413764514706e-09, 1.6572143520533616e-09, 2.878995745270213e-10, 4.2870304742830496e-11, 5.585732986206013e-12, 6.469210005564329e-13, 6.743181312013947e-14, 6.389777558561497e-15, 5.550320748045677e-16, 4.45029004394106e-17, 3.194193787660784e-18, 2.281015538797327e-19, 1.4860103996857515e-20, 9.11142941446578e-22, 5.276277122323717e-23], [2.755349053234141e-08, 2.8720381975330554e-08, 1.4968345659158816e-08, 5.200751901895735e-09, 1.3552509890357575e-09, 2.8252918469160597e-10, 4.908238452279616e-11, 7.308717928652468e-12, 9.522803037171492e-13, 1.1028993480573094e-13, 1.1496071802361681e-14, 1.0893573554587284e-15, 9.462430697509168e-17, 7.587050016782336e-18, 5.648829923644573e-19, 3.784148925141461e-20, 2.5334158260593208e-21, 1.553356523043944e-22, 8.995229082647315e-24], [4.4038501298870524e-09, 4.590353361727681e-09, 2.3923775065053185e-09, 8.312315970200095e-10, 2.1660857222750958e-10, 4.515639081155944e-11, 7.844794299370904e-12, 1.1681459509322246e-12, 1.522021224240616e-13, 1.7627543165514842e-14, 1.8374070334427154e-15, 1.7411102690235708e-16, 1.5123719663525292e-17, 1.2126315234960247e-18, 9.028475126863747e-20, 6.2738876100879225e-21, 3.9401951450153475e-22, 2.4827160528857566e-23, 1.4376995436379625e-24], [6.62459753884428e-10, 6.905149513638577e-10, 3.5987914379792993e-10, 1.2504001338414272e-10, 3.258386575720587e-11, 6.792758759050218e-12, 1.1800720613915398e-12, 1.757211658734399e-13, 2.289537054802485e-14, 2.6516656022791568e-15, 2.7639637482195535e-16, 2.6191070229099445e-17, 2.275021926409882e-18, 1.8241301518321167e-19, 1.3581300984571055e-20, 9.437646421868595e-22, 6.148331956935369e-23, 3.634204534505906e-24, 2.162694137510502e-25], [9.411587479317592e-11, 9.810168591270314e-11, 5.112814814750287e-11, 1.7764475765952856e-11, 4.629200509013632e-12, 9.650494677123465e-13, 1.6765322531008753e-13, 2.496476374433577e-14, 3.252752812840614e-15, 3.7672300295093117e-16, 3.926772374245864e-17, 3.720973948873641e-18, 3.23213112226402e-19, 2.591547697344939e-20, 1.929499891121419e-21, 1.340809526578137e-22, 8.734955402992874e-24, 5.355812422961952e-25, 2.9898805147206326e-26]] |
| Legacy trial inputs | {"lambda_home": 2.5572659113910605, "lambda_away": 1.0423500406098996, "rho": -0.09482779564960894, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6993 |
| Legacy p draw | 0.1745 |
| Legacy p away | 0.1262 |
| Legacy p over 1 5 | 0.8817 |
| Legacy p under 3 5 | 0.5144 |
| Legacy p btts yes | 0.6027 |
| Legacy p over 2 5 | 0.6993 |
| Legacy goal margin distribution | {"-1": 0.08058341946527026, "-10": 1.4472575516752448e-08, "-11": 1.3447034334294576e-09, "-12": 1.1486952067012154e-10, "-13": 9.079004638696291e-12, "-14": 6.675823518292408e-13, "-15": 4.588470256637031e-14, "-16": 2.959117622605531e-15, "-17": 1.7828188550030093e-16, "-18": 8.992356103562906e-18, "-2": 0.03325773815287188, "-3": 0.009647146668389341, "-4": 0.0022386270757260907, "-5": 0.0004306143579968625, "-6": 7.052893189785229e-05, "-7": 1.0040919891726838e-05, "-8": 1.2628314370540403e-06, "-9": 1.4214468618640917e-07, "0": 0.17449074510734808, "1": 0.20968013514202255, "10": 0.00011540823418192874, "11": 2.63075126154082e-05, "12": 5.513411201204551e-06, "13": 1.0690945490112178e-06, "14": 1.9286127175155317e-07, "15": 3.252148751363297e-08, "16": 5.145493229398413e-09, "17": 7.605614397971312e-10, "18": 9.411587479317592e-11, "2": 0.20206228822654862, "3": 0.14379829616819756, "4": 0.08186512191711134, "5": 0.03863384819847964, "6": 0.015524194356663197, "7": 0.0054222254172338405, "8": 0.0016730609119053343, "9": 0.00046201842890111186} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6939 |
| Legacy raw p draw | 0.1796 |
| Legacy raw p away | 0.1265 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.5573 |
| Legacy lambda away | 1.0424 |
| Legacy model home team | Fenerbahce |
| Legacy model away team | Goztep |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 85.7% |
| Market reference home draw last update utc | 2026-10-31T12:03:01Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.1% |
| Market reference draw away last update utc | 2026-10-31T12:03:01Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.2% |
| Market reference home away last update utc | 2026-10-31T12:03:01Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.10 |
| Market reference dc draw away odds | 2.85 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.1% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.18 |
| Market reference under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.4% |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.22 |
| Market reference btts yes last update utc | 2026-10-31T12:03:03Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,643.4256 |
| Elo away rating | 1,515.6231 |
| Elo rating diff | 187.8026 |
| Elo home expectancy | 0.7467 |

</details>


---

## 2026-10-31 — Kocaelispor vs Çaykur Rizespor

The model's most likely 1X2 outcome is **Çaykur Rizespor win** at **36.5%**. Expected goals are 1.18 for Kocaelispor and 0.89 for Çaykur Rizespor (2.07 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.1%; Double Chance 1X: 63.5%; Double Chance X2: 65.9%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Kocaelispor win | 34.1% | 2.93 |
| Draw | 29.4% | 3.40 |
| Çaykur Rizespor win | 36.5% | 2.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Kocaelispor expected goals | 1.18 |
| Çaykur Rizespor expected goals | 0.89 |
| Expected total goals | 2.07 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 75.7% |
| Under 1.5 | 24.3% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.03% |
| 2 | 1-2 | 9.23% |
| 3 | 0-1 | 8.85% |
| 4 | 0-0 | 8.43% |
| 5 | 2-1 | 7.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Kocaelispor win | 34.1% | 31.0% | 3.12 | +6.4% |
| Draw | 29.4% | 28.2% | 3.43 | +0.9% |
| Çaykur Rizespor win | 36.5% | 40.8% | 2.39 | -12.8% |
| Over 2.5 | 49.6% | 49.6% | 1.96 | -2.8% |
| Under 2.5 | 50.4% | 50.4% | 1.93 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T13:00:00+00:00 |
| Fixture id | 7d597f0fe7ec1c85b6e7f9f2ce731746 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:03:01Z |
| Market best draw last update utc | 2026-10-31T12:03:01Z |
| Market best away last update utc | 2026-10-31T12:03:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Kocaelispor |
| Matched away-team name | Rizespor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1504 |
| Dc lambda away | 0.8781 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.2857 |
| Shot lambda away | 0.9315 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.87 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.57 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.21255970763757742, "-10": 1.2646063487586254e-07, "-11": 1.3146285603654518e-08, "-12": 1.2552508812177778e-09, "-13": 1.1078515079239642e-10, "-14": 9.040101882754117e-12, "-15": 6.243132500485238e-13, "-2": 0.10470380459670454, "-3": 0.03557744969003465, "-4": 0.009506405101488728, "-5": 0.0020843949337352365, "-6": 0.0003866650214771284, "-7": 6.208151781321324e-05, "-8": 8.779353967979405e-06, "-9": 1.1087709427705324e-06, "0": 0.29415132995792626, "1": 0.16463740518641792, "10": 1.2096924818297795e-06, "11": 1.6659546249426487e-07, "12": 2.107323071496273e-08, "13": 2.463897414431109e-09, "14": 2.663513334231302e-10, "15": 2.4368263611682642e-11, "2": 0.10557430558141209, "3": 0.0475237897140207, "4": 0.01682259738699038, "5": 0.004886492364702506, "6": 0.0012008605666827363, "7": 0.0002554232962440306, "8": 4.785212404302992e-05, "9": 8.006099405711108e-06} |
| Raw goal margin distribution | {"-1": 0.16997556650313778, "-10": 1.1803877050523877e-08, "-11": 9.462133938183466e-10, "-12": 6.942542516712667e-11, "-13": 4.3928778048794e-12, "-2": 0.06992895220196743, "-3": 0.01912946444106524, "-4": 0.004045789242592255, "-5": 0.0006954889478484415, "-6": 0.00010056342982695515, "-7": 1.2537546025285394e-05, "-8": 1.3731725078096978e-06, "-9": 1.340624360038955e-07, "0": 0.3236492844310598, "1": 0.22931104344761957, "10": 1.965302893414077e-07, "11": 2.0870573791173392e-08, "12": 2.0286369318412692e-09, "13": 1.7004950967842988e-10, "2": 0.12272639694278903, "3": 0.04447584994811371, "4": 0.012461352515900465, "5": 0.002837870941617647, "6": 0.0005436044043862469, "7": 8.978337190592865e-05, "8": 1.30271361745176e-05, "9": 1.684889567491725e-06} |
| Unadjusted home-win probability | 41.2% |
| Unadjusted draw probability | 32.4% |
| Unadjusted away-win probability | 26.4% |
| Raw p over 1 5 | 62.4% |
| Raw p under 3 5 | 84.5% |
| Raw p btts yes | 42.0% |
| P home draw | 63.5% |
| P draw away | 65.9% |
| P home away | 70.6% |
| Raw p home draw | 73.6% |
| Raw p draw away | 58.8% |
| Raw p home away | 67.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.3037 |
| Totals anchor target over 2 5 | 0.4960 |
| Totals anchor reference over odds | 1.96 |
| Totals anchor reference under odds | 1.93 |
| Totals anchor reference last update utc | 2026-10-31T12:03:01Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3487 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.35, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.35, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.12 |
| Reference draw odds | 3.43 |
| Reference away odds | 2.39 |
| Market reference 1x2 last update utc | 2026-10-31T12:03:01Z |
| Market reference home last update utc | 2026-10-31T12:03:01Z |
| Market reference draw last update utc | 2026-10-31T12:03:01Z |
| Market reference away last update utc | 2026-10-31T12:03:01Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:03:01Z |
| Market best over 2 5 last update utc | 2026-10-31T12:03:01Z |
| Market best under 2 5 last update utc | 2026-10-31T12:03:01Z |
| Home probability edge | +3.1% |
| Draw probability edge | +1.3% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1021 |
| Raw ev home | 0.2869 |
| Raw edge prob draw | 0.0421 |
| Raw ev draw | 0.1101 |
| Raw edge prob away | -0.1443 |
| Raw ev away | -0.3693 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.13236610743630206, 0.12906077901531834, 0.06401090353168375, 0.018831944806091547, 0.004155254717707659, 0.0007334831084868817, 0.00010789500423461748, 1.360397315699015e-05, 1.5008533165907188e-06, 1.4718318942900053e-07, 1.2990344832452699e-08, 1.0422945441521194e-09, 7.666050721127346e-11, 5.2046413283628885e-12], [0.12109654748224725, 0.13550796440332985, 0.07441459834464488, 0.021892701578570612, 0.004830608439777051, 0.0008526961486118731, 0.00012543118375979006, 1.5815027479930407e-05, 1.7447870685506742e-06, 1.7110487932765414e-07, 1.5101666118287544e-08, 1.2116987197580103e-09, 8.912014263632455e-11, 6.0505518999018545e-12], [0.07681849016758036, 0.06779977255939416, 0.03174867972042945, 0.012725461638282646, 0.0028078637151898174, 0.0004956424445529858, 7.290875963622415e-05, 9.19272227696351e-06, 1.0141836916804537e-06, 9.945728124017151e-08, 8.778070270255252e-09, 7.043180815349834e-10, 5.180242156257772e-11, 3.516974175905537e-12], [0.029767934189696636, 0.02627309080433098, 0.011594276176738205, 0.003619510282801219, 0.0010880753071958005, 0.00019206641055932096, 2.825287445729413e-05, 3.562271936975606e-06, 3.930063364217025e-07, 3.8540692432055256e-08, 3.4015901321081844e-09, 2.7293030953887555e-10, 2.007395709779944e-11, 1.3628627116574352e-12], [0.00865152944286923, 0.007635814336337821, 0.0033696735914757183, 0.0009913546534740785, 0.00023211140830106547, 5.582074306369961e-05, 8.211203829440446e-06, 1.0353120357582105e-06, 1.1422041815596945e-07, 1.1201178193947473e-08, 9.886126794345519e-10, 7.932242102457626e-11, 5.83414454492502e-12, 3.96092211214777e-13], [0.002011532576600234, 0.0017753727115931378, 0.0007834693560858946, 0.00023049591330593665, 5.08587530942115e-05, 9.52627539600673e-06, 1.9091542258620853e-06, 2.4071626879689327e-07, 2.6556933493765624e-08, 2.604341230324364e-09, 2.2985838786709689e-10, 1.844293948248038e-11, 1.3564736600860697e-12, 9.209381895508014e-14], [0.0003897445083211058, 0.0003439873520398325, 0.00015180111051864672, 4.465973728015838e-05, 9.854138058270846e-06, 1.7394466297427828e-06, 2.7151091050295963e-07, 4.6639982329145946e-08, 5.145538833150601e-09, 5.0460415313218e-10, 4.4536213534337305e-11, 3.5734118672559558e-12, 2.6282356341169215e-13, 1.7843638529943593e-14], [6.472709992377788e-05, 5.712794723884572e-05, 2.5210478760577343e-05, 7.416898033931681e-06, 1.6365330752393806e-06, 2.8887985183021174e-07, 4.249408401621538e-08, 5.685358572392473e-09, 8.545490676692685e-10, 8.380249816074498e-11, 7.396383738879363e-12, 5.934569495207036e-13, 4.364861258611024e-14, 2.963395120322949e-15], [9.405899770766219e-06, 8.301619359912165e-06, 3.663492365242074e-06, 1.077795847478202e-06, 2.3781485800185977e-07, 4.1978938270191184e-08, 6.1750811573161545e-09, 7.785869132892803e-10, 9.114745378712237e-11, 1.2177865208977547e-11, 1.074814786943167e-12, 8.623894152572449e-14, 6.342852925612667e-15, 4.3062948155809323e-16], [1.214960116851387e-06, 1.0723202110788586e-06, 4.7321332574609063e-07, 1.3921889459889317e-07, 3.0718546306963085e-08, 5.4224196503312175e-09, 7.976352616235108e-10, 1.0057007518716583e-10, 1.1095356419229452e-11, 1.1545857064459305e-12, 1.3883383099580826e-13, 1.1139484475359116e-14, 8.193063417095886e-16, 5.562441212265359e-17], [1.4124276351685586e-07, 1.2466044595789998e-07, 5.501247072586461e-08, 1.6184614732760647e-08, 3.5711232915694862e-09, 6.303725741596223e-10, 9.272749538656296e-11, 1.1691573368964175e-11, 1.2898685159458161e-12, 1.2649268254422487e-13, 1.184657562547563e-14, 1.294998535038569e-15, 9.524682354993107e-17, 6.466505013814455e-18], [1.4927177794997247e-08, 1.3174683038505888e-08, 5.8139681709715545e-09, 1.7104637125753963e-09, 3.774125553324501e-10, 6.662064135022268e-11, 9.799863551627743e-12, 1.2356186613479549e-12, 1.3631917268026736e-13, 1.3368322136223675e-14, 1.1798841637728428e-15, 1.0045559153948522e-16, 1.0066117612948567e-17, 6.834096675114266e-19], [1.446107718564969e-09, 1.2763304017197083e-09, 5.63242721631599e-10, 1.6570545424263362e-10, 3.656278613714235e-11, 6.45404141327998e-12, 9.493863151842364e-13, 1.1970365114677202e-13, 1.3206261123746588e-14, 1.2950896740799192e-15, 1.1430423216479126e-16, 9.17132524929014e-18, 7.157778877417388e-19, 6.620702243269391e-20], [1.293187435539344e-10, 1.1413634115297452e-10, 5.036819881549123e-11, 1.4818274508593336e-11, 3.269641329885505e-12, 5.77155156352157e-13, 8.489923942094576e-14, 1.0704545426588546e-14, 1.180975022568038e-15, 1.1581389635890059e-16, 1.0221700290152987e-17, 8.201493171889121e-19, 6.032178043858731e-20, 4.345684846413758e-21]] |
| Legacy trial inputs | {"lambda_home": 1.1625300415859867, "lambda_away": 0.8825970467720496, "rho": -0.09482779564960894, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T12:03:01Z", "over": 1.96, "under": 1.93, "bookmaker": "pinnacle", "event_id": "7d597f0fe7ec1c85b6e7f9f2ce731746", "kickoff_utc": "2026-10-31T13:00:00Z", "home_team": "Kocaelispor", "away_team": "\u00c7aykur Rizespor"}} |
| Legacy p home | 0.3600 |
| Legacy p draw | 0.3035 |
| Legacy p away | 0.3365 |
| Legacy p over 1 5 | 0.6175 |
| Legacy p under 3 5 | 0.8497 |
| Legacy p btts yes | 0.4119 |
| Legacy p over 2 5 | 0.3411 |
| Legacy goal margin distribution | {"-1": 0.21734669170958063, "-10": 1.4255208836484945e-08, "-11": 1.1349316609643494e-09, "-12": 8.271105911117531e-11, "-13": 5.2046413283628885e-12, "-2": 0.08891199238652914, "-3": 0.024187510945935735, "-4": 0.005084538767788187, "-5": 0.00086851145551413, "-6": 0.00012476376342006627, "-7": 1.5451699793651424e-05, "-8": 1.681015122736531e-06, "-9": 1.630096436781321e-07, "0": 0.3034841768151427, "1": 0.2015345923554716, "10": 1.5499550755150194e-07, "11": 1.625387639553245e-08, "12": 1.5602440597179437e-09, "13": 1.293187435539344e-10, "2": 0.10670189977155767, "3": 0.03823355694087849, "4": 0.010586363494269035, "5": 0.0023818395620877515, "6": 0.00045067880552381625, "7": 7.351850117566488e-05, "8": 1.0534980056224812e-05, "9": 1.3456035060758311e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4096 |
| Legacy raw p draw | 0.3255 |
| Legacy raw p away | 0.2649 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1625 |
| Legacy lambda away | 0.8826 |
| Legacy model home team | Kocaelispor |
| Legacy model away team | Rizespor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 59.4% |
| Market reference home draw last update utc | 2026-10-31T12:03:01Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.5% |
| Market reference draw away last update utc | 2026-10-31T12:03:01Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.1% |
| Market reference home away last update utc | 2026-10-31T12:03:01Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.59 |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 75.5% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market reference over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.9% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.05 |
| Market reference under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.8% |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.28 |
| Market reference btts yes last update utc | 2026-10-31T12:03:03Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,459.3997 |
| Elo away rating | 1,449.0338 |
| Elo rating diff | 70.3660 |
| Elo home expectancy | 0.5999 |

</details>


---

## 2026-11-01 — Amed SK vs Eyüpspor

The model's most likely 1X2 outcome is **Amed SK win** at **78.2%**. Expected goals are 2.79 for Amed SK and 0.80 for Eyüpspor (3.59 combined). The most likely exact score is 2-0 at 14.0%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 60.2%; Under 3.5 goals: 63.0%; Double Chance 1X: 92.5%; Double Chance X2: 21.8%; Double Chance 12 (either team wins): 85.7%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 44.3%; BTTS No (at least one team does not score): 55.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Amed SK win | 78.2% | 1.28 |
| Draw | 14.3% | 7.00 |
| Eyüpspor win | 7.5% | 13.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Amed SK expected goals | 2.79 |
| Eyüpspor expected goals | 0.80 |
| Expected total goals | 3.59 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 60.2% |
| Under 2.5 | 39.8% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.03% |
| 2 | 1-0 | 11.09% |
| 3 | 3-0 | 11.07% |
| 4 | 2-1 | 9.50% |
| 5 | 3-1 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Amed SK win | 78.2% | 78.2% | 1.26 | -1.5% |
| Draw | 14.3% | 14.2% | 6.27 | -10.4% |
| Eyüpspor win | 7.5% | 7.6% | 11.29 | -14.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T10:30:00+00:00 |
| Fixture id | 5706f8b2f4d8a94519bbea0efc91e36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:03:01Z |
| Market best draw last update utc | 2026-10-31T12:03:01Z |
| Market best away last update utc | 2026-10-31T12:03:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Amedspor |
| Matched away-team name | Eyupspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.0105 |
| Dc lambda away | 0.7473 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9187 |
| Shot lambda away | 1.0062 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 44.3% |
| P btts no | 55.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.32 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.59 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.02 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.054589198961777365, "-10": 2.865454274426525e-10, "-11": 1.7433031918974638e-11, "-12": 9.739839956360767e-13, "-13": 5.0302581233002286e-14, "-14": 2.4151436373938443e-15, "-15": 1.0832726578825616e-16, "-16": 4.5582074281136745e-18, "-17": 1.8003619635941365e-19, "-18": 6.2201914879300695e-21, "-2": 0.016801490788975262, "-3": 0.00337427781688565, "-4": 0.0005308650335092479, "-5": 6.838495249701152e-05, "-6": 7.442877553661958e-06, "-7": 7.004988825322854e-07, "-8": 5.803368526124979e-08, "-9": 4.291810651717146e-09, "0": 0.14286110182128034, "1": 0.23492992846058164, "10": 8.791315987855218e-05, "11": 1.8688691048410872e-05, "12": 3.6484074296246955e-06, "13": 6.583962269311688e-07, "14": 1.1045505056680459e-07, "15": 1.7311151095147092e-08, "16": 2.545234500890707e-09, "17": 3.5126841211208484e-10, "18": 4.240612358581469e-11, "2": 0.23197640483508522, "3": 0.16278799855117085, "4": 0.08948932225490117, "5": 0.04028034665866486, "6": 0.015318599990814905, "7": 0.005037687223751867, "8": 0.0014583086593951968, "9": 0.0003768386240779714} |
| Raw goal margin distribution | {"-1": 0.05173463140818929, "-10": 9.860807075550611e-10, "-11": 7.045948057279765e-11, "-12": 4.626607827109388e-12, "-13": 2.8098359297480856e-13, "-14": 1.587096507776544e-14, "-15": 8.3776862825626e-16, "-16": 4.150274677456887e-17, "-17": 1.9363702127800494e-18, "-18": 8.491474081175258e-20, "-19": 3.195999899701755e-21, "-2": 0.017469224250880454, "-3": 0.003982565599204577, "-4": 0.0007205400474120658, "-5": 0.00010754657725051464, "-6": 1.3626390400707777e-05, "-7": 1.4976230443553701e-06, "-8": 1.4520011390904896e-07, "-9": 1.2586159350063833e-08, "0": 0.14497743716946715, "1": 0.19549506953841317, "10": 0.0002675272205592374, "11": 6.67944694058946e-05, "12": 1.532531136454515e-05, "13": 3.252169194622317e-06, "14": 6.418611024965946e-07, "15": 1.1838791354333617e-07, "16": 2.0493005913607102e-08, "17": 3.340894562223612e-09, "18": 5.119210833712333e-10, "19": 6.732436044673507e-11, "2": 0.21328716564151037, "3": 0.16990243092857282, "4": 0.1074089151103219, "5": 0.05601758101890916, "6": 0.0248001402450868, "7": 0.009524043600648376, "8": 0.003226497771466688, "9": 0.000977244398797385} |
| Unadjusted home-win probability | 78.1% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 7.4% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 51.7% |
| Raw p btts yes | 52.2% |
| P home draw | 92.5% |
| P draw away | 21.8% |
| P home away | 85.7% |
| Raw p home draw | 92.6% |
| Raw p draw away | 21.9% |
| Raw p home away | 85.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8475 |
| Totals anchor target over 2 5 | 0.6025 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.38 |
| Totals anchor reference last update utc | 2026-10-31T12:03:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6965 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 4.14, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.14, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.26 |
| Reference draw odds | 6.27 |
| Reference away odds | 11.29 |
| Market reference 1x2 last update utc | 2026-10-31T12:03:01Z |
| Market reference home last update utc | 2026-10-31T12:03:01Z |
| Market reference draw last update utc | 2026-10-31T12:03:01Z |
| Market reference away last update utc | 2026-10-31T12:03:01Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:39Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:39Z |
| Home probability edge | -0.0% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | -0.0011 |
| Raw ev home | -0.0159 |
| Raw edge prob draw | 0.0030 |
| Raw ev draw | -0.0910 |
| Raw edge prob away | -0.0019 |
| Raw ev away | -0.1642 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.029831310252823606, 0.01401681240764326, 0.007135840077416987, 0.001712245501545358, 0.0003081401025410404, 4.436294805075888e-05, 5.3224467905044595e-06, 5.473378332104393e-07, 4.925016181903738e-08, 3.939193662327367e-09, 2.835629675634839e-10, 1.855662569691362e-11, 1.1131660228049376e-12, 6.16394521072765e-14, 3.1693697921851527e-15, 1.5209811628421816e-16, 6.8429920104649885e-18, 2.8976057297296416e-19, 1.1588012815485165e-20, 4.390333849215181e-22, 1.5801915335921102e-23], [0.061835644226961126, 0.05999075869280563, 0.022048776611612902, 0.005290606033519518, 0.0009521110636305362, 0.0001370754838662021, 1.644563765973693e-05, 1.6911995622959092e-06, 1.5217631060291581e-07, 1.2171573374438171e-08, 8.761710547465705e-10, 5.733745294424638e-11, 3.439531814360394e-12, 1.9045753481452822e-13, 9.792922177255363e-15, 4.6996252054625185e-16, 2.114391586090721e-17, 8.953208136702624e-19, 3.580538565455431e-20, 1.3565535275671153e-21, 4.882577208813542e-23], [0.10253081016585457, 0.07380683279262905, 0.030469134467124726, 0.008173627022716883, 0.0014709469329246651, 0.0002117723134140542, 2.54073933174749e-05, 2.612788469904846e-06, 2.3510206518513047e-07, 1.880425425971611e-08, 1.35362477648611e-09, 8.85824708605419e-11, 5.313843065469832e-12, 2.9424395681272695e-13, 1.5129399700572617e-14, 7.260601778442386e-16, 3.266591406576441e-17, 1.3832098535123567e-18, 5.531688919769663e-20, 2.0957830729475695e-21, 7.54325019886452e-23], [0.10560209237821237, 0.07601769616471972, 0.027360680077698398, 0.007530072838844524, 0.0015150087436438622, 0.00021811589480394414, 2.6168464794742195e-05, 2.6910538297444074e-06, 2.421444828713232e-07, 1.9367530523027576e-08, 1.3941722342844405e-09, 9.123593440618832e-11, 5.47301777266115e-12, 3.0305795359272773e-13, 1.5582596706515083e-14, 7.478091107328719e-16, 3.36444125352323e-17, 1.4246435241541728e-18, 5.697389139597279e-20, 2.15856167834913e-21, 7.769206183428199e-23], [0.08157403050325017, 0.05872108900568567, 0.02113519629189018, 0.0050713923493877645, 0.0010467928888317985, 0.0001684871223219397, 2.021425046905556e-05, 2.0787477051804085e-06, 1.8704839068145583e-07, 1.4960759678887193e-08, 1.0769507100199046e-09, 7.047666129178382e-11, 4.22772038581314e-12, 2.341019784161613e-13, 1.2037026828072256e-14, 5.776571451922997e-16, 2.598916624287659e-17, 1.1004887467512656e-18, 4.40103964794435e-20, 1.6674155997038543e-21, 6.001447963011849e-23], [0.050410534887606835, 0.03628803784363017, 0.013060977169520857, 0.0031339827072461284, 0.0005639995852820687, 9.31327279773377e-05, 1.2491857668557244e-05, 1.284609612496154e-06, 1.1559082426045569e-07, 9.245343071623703e-09, 6.655262833620595e-10, 4.355266217561684e-11, 2.6126163521561983e-12, 1.4466866326698769e-13, 7.438555593197265e-15, 3.5697642363805417e-16, 1.6060598740847364e-17, 6.800721506498695e-19, 2.7197229479251977e-20, 1.0304175451728108e-21, 3.7087318114496225e-23], [0.02596028429612957, 0.018687518017210032, 0.0067261075737836875, 0.0016139301485425222, 0.0002904470188516337, 4.181567378785653e-05, 5.754152830517082e-06, 6.61544870021596e-07, 5.952665780110784e-08, 4.761142389973107e-09, 3.427309700471572e-10, 2.2428635094888942e-11, 1.3454382781279738e-12, 7.450108663844672e-14, 3.830687739824797e-15, 1.8383477710207297e-16, 8.270844778934494e-18, 3.5022176241758585e-19, 1.4005957503181255e-20, 5.306417096356268e-22, 1.9099129262959216e-23], [0.011459107487383933, 0.008248841776496268, 0.0029689655467750632, 0.0007124035637789834, 0.00012820597688551928, 1.8457821768302843e-05, 2.21447803960193e-06, 2.611962164714934e-07, 2.6275612482769067e-08, 2.1016119002046523e-09, 1.5128459227279239e-10, 9.900205152451354e-12, 5.938887906943227e-13, 3.2885462654357163e-14, 1.6909006873934996e-15, 8.114635597600107e-17, 3.650826710992869e-18, 1.5459109669929499e-19, 6.182358045925323e-21, 2.3423011545795714e-22, 8.430530753945528e-24], [0.00442588571241576, 0.003185975085997539, 0.0011467125348630686, 0.0002751537812063313, 4.9517381870153466e-05, 7.12902027811401e-06, 8.553045450287663e-07, 8.795588849216384e-08, 9.077546387787844e-09, 8.117119149461962e-10, 5.84311052310109e-11, 3.823786152844842e-12, 2.2937946226542894e-13, 1.2701451615524489e-14, 6.53081682119502e-16, 3.134140227973179e-17, 1.4100698327927106e-18, 5.970818642737887e-20, 2.3878308301605987e-21, 9.046740529872935e-23, 3.2561493687923757e-24], [0.0015194873004576147, 0.001093803364412962, 0.0003936873311283355, 9.446531234257922e-05, 1.700022047395794e-05, 2.4475227064519982e-06, 2.9364165246045657e-07, 3.019686097844597e-08, 2.7171523680213867e-09, 2.492671379431724e-10, 2.0060464304615386e-11, 1.3127755383773945e-12, 7.875015365181548e-14, 4.3606400348354355e-15, 2.2421485474834614e-16, 1.076007512100714e-17, 4.841026955749024e-19, 2.0498909575375695e-20, 8.197858819291083e-22, 3.1059110512309146e-23, 1.1178954757899806e-24], [0.000469500937359851, 0.00033797038298680367, 0.00012164403804874545, 2.918849843593623e-05, 5.2528372204516674e-06, 7.562512727435503e-07, 9.073128221378353e-08, 9.330419892575445e-09, 8.395631759155758e-10, 6.715108782468389e-11, 5.5442983992894615e-12, 4.0562981054573315e-13, 2.4332727852101593e-14, 1.3473785422408924e-15, 6.927934471229085e-17, 3.324717063350135e-18, 1.4958115759335187e-19, 6.333884631740743e-21, 2.533027027499167e-22, 9.596843287009171e-24, 3.454145181704814e-25], [0.0001318812842124703, 9.49347798637465e-05, 3.416941411208142e-05, 8.198954148231123e-06, 1.4755048675467647e-06, 2.124285195202751e-07, 2.548612167610356e-08, 2.620884560090454e-09, 2.358305617873185e-10, 1.886252186925027e-11, 1.357819172011862e-12, 1.0191609975463386e-13, 6.83498400572548e-15, 3.7847424431202093e-16, 1.9460342297575666e-17, 9.339021950059775e-19, 4.201686000528543e-20, 1.779167564573707e-21, 7.115190423473971e-23, 2.695722023887112e-24, 9.702581319244504e-26], [3.39579379501495e-05, 2.4444631269516967e-05, 8.798237377956223e-06, 2.1111378910535874e-06, 3.7992580248592094e-07, 5.469793934588881e-08, 6.562387859923872e-09, 6.74848109021075e-10, 6.072370034720525e-11, 4.8568858806939934e-12, 3.496230679435731e-13, 2.2879660424568648e-14, 1.5742071198136988e-15, 9.745283404559131e-17, 5.01081787439296e-18, 2.404692445853714e-19, 1.0818865871983118e-20, 4.5811550988066375e-22, 1.832080998806201e-23, 6.941179088803121e-25, 2.4983048683721417e-26], [8.071185839916733e-06, 5.810045417190667e-06, 2.09118142112848e-06, 5.017791798017104e-07, 9.030147124200946e-08, 1.3000707939606163e-08, 1.5597605499136572e-09, 1.603991534945809e-10, 1.4432922019858754e-11, 1.1543936679516869e-12, 8.309906094524771e-14, 5.438080236555374e-15, 3.2621696678547065e-16, 2.0718424965363836e-17, 1.1909805104648315e-18, 5.715517722784397e-20, 2.571448159134295e-21, 1.0888574629658185e-22, 4.354524187202601e-24, 1.649792353590988e-25, 5.938017469435741e-27], [1.7813477124371461e-06, 1.2823036562834603e-06, 4.615333254247939e-07, 1.1074496509147229e-07, 1.9929948636682834e-08, 2.8693158363108392e-09, 3.4424630316368267e-10, 3.5400828431101276e-11, 3.1854120489591328e-12, 2.5477997415047484e-13, 1.8340343669006528e-14, 1.2002092358633522e-15, 7.1997579917882e-17, 3.9867291026414675e-18, 2.3511602713701485e-19, 1.2614409608218101e-20, 5.675303960008736e-22, 2.4031583329820657e-23, 9.610634488507331e-25, 3.6411673493270985e-26, 1.3105476748259699e-27], [3.6694149862311683e-07, 2.641429419093031e-07, 9.507168584407418e-08, 2.281246001098365e-08, 4.105388953075708e-09, 5.910530805681158e-10, 7.091162129460257e-11, 7.29225010160193e-12, 6.561660381161772e-13, 5.2482367637268866e-14, 3.777944723638961e-15, 2.4723223466936913e-16, 1.483084952356679e-17, 8.212300952328932e-19, 4.2225908363601606e-20, 2.32424168376915e-21, 1.1690612257716614e-22, 4.950288559478446e-24, 1.9797036801462332e-25, 7.500475031186766e-27, 2.6996095397891095e-28], [7.086246192543751e-08, 5.1010363325370255e-08, 1.8359912257382484e-08, 4.4054626827974e-09, 7.928183905828513e-10, 1.14142108687164e-10, 1.369420488801386e-11, 1.4082538963691366e-12, 1.267164958644541e-13, 1.013521172287076e-14, 7.295835034735088e-16, 4.774462654602374e-17, 2.8640819139539976e-18, 1.585930906529473e-19, 8.154520093558655e-21, 3.9133557355481386e-22, 2.019402499954208e-23, 9.559824546480743e-25, 3.823134673630863e-26, 1.4484655682568872e-27, 5.213391751673679e-29], [1.2879728378505194e-08, 9.271476128093552e-09, 3.3370373608680497e-09, 8.007224303859942e-10, 1.4410006718275226e-10, 2.0746094850435358e-11, 2.4890137108530574e-12, 2.559596037220817e-13, 2.3031574171490647e-14, 1.842142800324547e-15, 1.3260670175507707e-16, 8.677906535240067e-18, 5.205661234904806e-19, 2.882535936257624e-20, 1.4821387940572853e-21, 7.112786876549695e-23, 3.2000885321562733e-24, 1.554198967027161e-25, 6.948804037125134e-27, 2.632683451556599e-28, 9.47568964834294e-30], [2.2109228498130495e-09, 1.591533440822242e-09, 5.728328994993355e-10, 1.374513084183299e-10, 2.4736090842229246e-11, 3.5612564024071255e-12, 4.2726190530593063e-13, 4.393780053954228e-14, 3.953579773304393e-15, 3.1622061352266096e-16, 2.2763149837688623e-17, 1.4896418063694428e-18, 8.935992308537183e-20, 4.948135845407388e-21, 2.5442264231630655e-22, 1.2209747417856049e-23, 5.4932438396578495e-25, 2.3260665510426406e-26, 1.0669478065853932e-27, 4.519241266830743e-29, 1.626588554167151e-30], [3.595500687719587e-10, 2.5882221903351184e-10, 9.315662390808536e-11, 2.23529407183001e-11, 4.02269267976718e-12, 5.791472934066118e-13, 6.948322391682524e-14, 7.14535977907002e-15, 6.429486580715465e-16, 5.142519710662797e-17, 3.7018442729918905e-18, 2.422521500336419e-19, 1.4532106578716292e-20, 8.046877726464572e-22, 4.137533724874507e-23, 1.985603217294352e-24, 8.933356496347795e-26, 3.782752475810059e-27, 1.5127863572931694e-28, 6.573815971455194e-30, 2.6452303686848814e-31], [5.5548043825504266e-11, 3.998627511042503e-11, 1.4392065742488649e-11, 3.45337753623556e-12, 6.214786998524126e-13, 8.947432368863342e-14, 1.073468621616948e-14, 1.1039095598352228e-15, 9.933120123739714e-17, 7.944843710837719e-18, 5.719097999721551e-19, 3.742631198167318e-20, 2.245111775026275e-21, 1.2431879602604843e-22, 6.392208614055357e-24, 3.067622123145341e-25, 1.3801429098952837e-26, 5.844095678385239e-28, 2.3371521846889878e-29, 8.85473507027501e-31, 3.6554354565654827e-32]] |
| Legacy trial inputs | {"lambda_home": 3.089864174701917, "lambda_away": 0.7198502837658123, "rho": -0.09482779564960894, "max_goals": 20, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8075 |
| Legacy p draw | 0.1290 |
| Legacy p away | 0.0635 |
| Legacy p over 1 5 | 0.8943 |
| Legacy p under 3 5 | 0.4785 |
| Legacy p btts yes | 0.5010 |
| Legacy p over 2 5 | 0.7247 |
| Legacy goal margin distribution | {"-1": 0.04593589241827485, "-10": 3.4652972395789967e-10, "-11": 2.2306578139032893e-11, "-12": 1.3195274499126087e-12, "-13": 7.21932070999598e-14, "-14": 3.673467930234477e-15, "-15": 1.7468392039295148e-16, "-16": 7.795848289490927e-18, "-17": 3.2773943376230033e-19, "-18": 1.3019998845040925e-20, "-19": 4.878591570096535e-22, "-2": 0.014137069486784963, "-20": 1.5801915335921102e-23, "-3": 0.0029044965982450172, "-4": 0.00047351068015320043, "-5": 6.367916798468715e-05, "-6": 7.269237830868457e-06, "-7": 7.197857358088188e-07, "-8": 6.287097220668186e-08, "-9": 4.909661933787292e-09, "0": 0.12896722654991594, "1": 0.16868266992535885, "10": 0.0005737562687372427, "11": 0.0001585320639328714, "12": 4.0253143151767976e-05, "13": 9.453114376637782e-06, "14": 2.064676615007039e-06, "15": 4.214304627847769e-07, "16": 8.072974537244855e-08, "17": 1.4567871820771757e-08, "18": 2.48413713458905e-09, "19": 3.995363438823837e-10, "2": 0.20312747653051738, "20": 5.5548043825504266e-11, "3": 0.17913372691196916, "4": 0.12535263780308306, "5": 0.07235995488020627, "6": 0.0354557759115971, "7": 0.01506949020158045, "8": 0.0056499253472032576, "9": 0.001893831478577858} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8329 |
| Legacy raw p draw | 0.1160 |
| Legacy raw p away | 0.0511 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 3.0899 |
| Legacy lambda away | 0.7199 |
| Legacy model home team | Amedspor |
| Legacy model away team | Eyupspor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 90.2% |
| Market reference home draw last update utc | 2026-10-31T12:03:01Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 26.0% |
| Market reference draw away last update utc | 2026-10-31T12:03:01Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.8% |
| Market reference home away last update utc | 2026-10-31T12:03:01Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 3.64 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.79 |
| Market reference over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.1% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 44.6% |
| Market reference btts yes odds | 2.05 |
| Market reference btts yes opposite odds | 1.69 |
| Market reference btts yes last update utc | 2026-10-31T12:02:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,486.7305 |
| Elo away rating | 1,373.7821 |
| Elo rating diff | 172.9484 |
| Elo home expectancy | 0.7302 |

</details>


---

## 2026-11-01 — Basaksehir vs Samsunspor

The model's most likely 1X2 outcome is **Basaksehir win** at **54.2%**. Expected goals are 1.78 for Basaksehir and 1.03 for Samsunspor (2.81 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 60.5%; Under 3.5 goals: 61.8%; Double Chance 1X: 78.1%; Double Chance X2: 45.8%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 79.3%; BTTS Yes (both teams score): 60.1%; BTTS No (at least one team does not score): 39.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Basaksehir win | 54.2% | 1.85 |
| Draw | 23.9% | 4.18 |
| Samsunspor win | 21.9% | 4.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Basaksehir expected goals | 1.78 |
| Samsunspor expected goals | 1.03 |
| Expected total goals | 2.81 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.5% |
| Under 2.5 | 39.5% |
| Over 3.5 | 38.2% |
| Under 3.5 | 61.8% |
| Over 4.5 | 20.7% |
| Under 4.5 | 79.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.08% |
| 2 | 2-1 | 9.53% |
| 3 | 2-0 | 8.31% |
| 4 | 1-0 | 7.43% |
| 5 | 3-1 | 6.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Basaksehir win | 54.2% | 54.2% | 1.79 | -3.0% |
| Draw | 23.9% | 23.3% | 3.99 | -4.4% |
| Samsunspor win | 21.9% | 22.4% | 4.14 | -9.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:00:00+00:00 |
| Fixture id | f4e049de3ce6858d46dd45ab5cfa0e8c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:03:01Z |
| Market best draw last update utc | 2026-10-31T12:03:01Z |
| Market best away last update utc | 2026-10-31T12:03:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Buyuksehyr |
| Matched away-team name | Samsunspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8390 |
| Dc lambda away | 1.0100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.5493 |
| Shot lambda away | 1.0853 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.1% |
| P btts no | 39.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.53 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.53 |
| Fair Over 3.5 odds | 2.62 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.83 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.131228673673448, "-10": 6.147347669748056e-08, "-11": 6.301253755892375e-09, "-12": 5.935913075330369e-10, "-13": 5.172051999355723e-11, "-14": 4.191340050519453e-12, "-15": 3.173280523639953e-13, "-16": 2.238886586069513e-14, "-17": 1.3313501317680154e-15, "-2": 0.06117347674625191, "-3": 0.01995093701010002, "-4": 0.005169119067625656, "-5": 0.001105549640491147, "-6": 0.0002007953173116802, "-7": 3.16430589024478e-05, "-8": 4.399712433899997e-06, "-9": 5.470014669239668e-07, "0": 0.23949998577691323, "1": 0.21366516068426056, "10": 1.3987899657976245e-05, "11": 2.491264430542438e-06, "12": 4.077636576256523e-07, "13": 6.17322337269198e-08, "14": 8.692208438745983e-09, "15": 1.1434411740448772e-09, "16": 1.4017339121549957e-10, "17": 1.4482845482307944e-11, "2": 0.16757255508140842, "3": 0.09495791074186569, "4": 0.0427476765725273, "5": 0.01588555352258044, "6": 0.0050130935671385745, "7": 0.001372646842248077, "8": 0.0003316139357729176, "9": 7.16349723928355e-05} |
| Raw goal margin distribution | {"-1": 0.12799605389183324, "-10": 2.515755678809076e-08, "-11": 2.312762747869097e-09, "-12": 1.9529860347379785e-10, "-13": 1.5247822302875615e-11, "-14": 1.1066405816593477e-12, "-15": 7.465051228051429e-14, "-16": 4.292781557700031e-15, "-2": 0.056066927655109275, "-3": 0.01680388609662419, "-4": 0.003964362076575469, "-5": 0.0007679054518108875, "-6": 0.00012588905267391987, "-7": 1.786663399341849e-05, "-8": 2.2337824067874213e-06, "-9": 2.4944151790004677e-07, "0": 0.2538011046511874, "1": 0.23020690636934013, "10": 6.308842968483528e-06, "11": 1.0077213620604497e-06, "12": 1.478552142485602e-07, "13": 2.0057345466167557e-08, "14": 2.5293000379230224e-09, "15": 2.964521990863194e-10, "16": 2.9620255412178557e-11, "2": 0.16926338021608825, "3": 0.08814427416012612, "4": 0.03613148533099279, "5": 0.012160414509305568, "6": 0.00346383119421468, "7": 0.0008541607674708684, "8": 0.00018555209872321695, "9": 3.600160569173812e-05} |
| Unadjusted home-win probability | 54.0% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 54.4% |
| P home draw | 78.1% |
| P draw away | 45.8% |
| P home away | 76.1% |
| Raw p home draw | 79.4% |
| Raw p draw away | 46.0% |
| Raw p home away | 74.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1187 |
| Totals anchor target over 2 5 | 0.6047 |
| Totals anchor reference over odds | 1.60 |
| Totals anchor reference under odds | 2.38 |
| Totals anchor reference last update utc | 2026-10-31T12:03:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5371 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.99, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.86, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.99 |
| Reference away odds | 4.14 |
| Market reference 1x2 last update utc | 2026-10-31T12:03:01Z |
| Market reference home last update utc | 2026-10-31T12:03:01Z |
| Market reference draw last update utc | 2026-10-31T12:03:01Z |
| Market reference away last update utc | 2026-10-31T12:03:01Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:39Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:39Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | -0.0017 |
| Raw ev home | -0.0326 |
| Raw edge prob draw | 0.0204 |
| Raw ev draw | 0.0127 |
| Raw edge prob away | -0.0187 |
| Raw ev away | -0.1482 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.06258819357072712, 0.04902886839134392, 0.03039068805526804, 0.010282723560860874, 0.002609378330875475, 0.0005297316597761333, 8.961765210790882e-05, 1.2995242975975918e-05, 1.648858166091474e-06, 1.8596433971433411e-07, 1.8876373190198746e-08, 1.7418660400796385e-09, 1.473405845370918e-10, 1.1504504507347002e-11, 8.341204432089224e-13, 5.644511844142548e-14, 3.5809255221392e-15], [0.09009100444558443, 0.11226736409320179, 0.05807610191556842, 0.01965011454838237, 0.00498647880576468, 0.0010123084349098524, 0.000171257850029186, 2.4833694259170526e-05, 3.1509406672234397e-06, 3.5537477553223505e-07, 3.607243676736219e-08, 3.3286771751584965e-09, 2.815654186017111e-10, 2.1984917716957823e-11, 1.5939903624940562e-12, 1.078656871894125e-13, 6.84308940941423e-15], [0.09524947348739096, 0.09668330016818538, 0.049727145296239526, 0.018775521848815594, 0.004764539236439102, 0.0009672523328346148, 0.00016363545856626404, 2.372838936902005e-05, 3.010697733904328e-06, 3.39557657340613e-07, 3.4466914836452314e-08, 3.1805234964895927e-09, 2.6903342755640743e-10, 2.1006406956194315e-11, 1.5230446012983858e-12, 1.0306477153483275e-13, 6.538515305012935e-15], [0.06067338916006173, 0.061586728845907185, 0.031256908691331124, 0.010717582300847564, 0.003034985209646552, 0.0006161344000901064, 0.000104234884398499, 1.5114853128491139e-05, 1.9177978477400696e-06, 2.1629635452875434e-07, 2.1955234611303237e-08, 2.0259759216493606e-09, 1.7137280920881964e-10, 1.3380965347556767e-11, 9.701710090286318e-13, 6.565169090255982e-14, 4.164998179045956e-15], [0.028986460638984125, 0.029422804895012734, 0.014932858803839212, 0.005052549609077679, 0.001299339534800757, 0.00029435566042669694, 4.979778475626988e-05, 7.221058545406443e-06, 9.162199869928849e-07, 1.0333468846389255e-07, 1.0489022497182612e-08, 9.679016142232433e-10, 8.187265055556579e-11, 6.392700831913938e-12, 4.634951855434367e-13, 3.1364823699060136e-14, 1.989810647627803e-15], [0.011078529312530283, 0.01124529864290744, 0.0057072892078350165, 0.0019310677369109184, 0.000490034209159099, 0.00010081576560416533, 1.9032548505747624e-05, 2.7598646747230553e-06, 3.501762463877869e-07, 3.949417589841144e-08, 4.008869680299806e-09, 3.699287932517097e-10, 3.129145604808731e-11, 2.4432690984475208e-12, 1.7714632576954672e-13, 1.1987531801832296e-14, 7.604990433527471e-16], [0.003528481028240446, 0.0035815965999673365, 0.00181775587033473, 0.0006150397477606316, 0.00015607454396054476, 3.168479872877736e-05, 5.432150079442165e-06, 8.790092863912049e-07, 1.1153016858675037e-07, 1.2578786087239941e-08, 1.2768139355489509e-09, 1.1782130027965047e-10, 9.966242440394683e-12, 7.781744686099688e-13, 5.642061613660046e-14, 3.8179958137903466e-15, 2.422168476306806e-16], [0.0009632669785023649, 0.0009777674040053756, 0.0004962430549741224, 0.00016790439703162502, 4.2607981502164835e-05, 8.649875142206694e-06, 1.4633475023915365e-06, 2.1504110768643417e-07, 3.044747233910801e-08, 3.4339788624357364e-09, 3.485671856989618e-10, 3.216493641746876e-11, 2.7207606235503403e-12, 2.1243979013241494e-13, 1.5402694812914092e-14, 1.0423038304724838e-15, 6.612462674226799e-17], [0.00023009840676224694, 0.00023356216590699087, 0.00011853903317012269, 4.01078154941214e-05, 1.01778934374416e-05, 2.0662210304443006e-06, 3.4955410738081196e-07, 5.0688011254683885e-08, 6.517594289950889e-09, 8.202845968312784e-10, 8.326326539671211e-11, 7.683332646547653e-12, 6.499160654647664e-13, 5.0746115389913975e-14, 3.679286859606551e-15, 2.489781712716697e-16, 1.579538341986959e-17], [4.885713858370787e-05, 4.959260373940622e-05, 2.5169570066408892e-05, 8.516152403918278e-06, 2.161087324159963e-06, 4.387237993059934e-07, 7.422134601937936e-08, 1.07626611815765e-08, 1.3655844535515832e-09, 1.5608030760205635e-10, 1.767941357639449e-11, 1.6314135033754456e-12, 1.3799764946221297e-13, 1.077499851944497e-14, 7.812284774955093e-16, 5.286590719729386e-17, 3.353857367316584e-18], [9.33651832604235e-06, 9.477064500120442e-06, 4.809863184701457e-06, 1.6274226303762044e-06, 4.129802111031866e-07, 8.383939197080314e-08, 1.4183576389890063e-08, 2.056726739872606e-09, 2.609609290666583e-10, 2.943214150441853e-11, 3.0275681000208628e-12, 3.117604205477772e-13, 2.6371122429678297e-14, 2.0590843847212946e-15, 1.4929146913641115e-16, 1.0102587373689972e-17, 6.409165923467596e-19], [1.621993818554252e-06, 1.64641031061428e-06, 8.355971767244884e-07, 2.827252466567409e-07, 7.174530442747405e-08, 1.4565062775990195e-08, 2.464052704231726e-09, 3.57306432872681e-10, 4.5335637873665175e-11, 5.113121392781206e-12, 5.190091160767168e-13, 4.85349245335008e-14, 4.581343502530986e-15, 3.577160165351746e-16, 2.5935775162215802e-17, 1.755079752355112e-18, 1.1134372736094217e-19], [2.583002786398197e-07, 2.62188571326492e-07, 1.3306769798356221e-07, 4.502360561092688e-08, 1.142534078288498e-08, 2.319466159740421e-09, 3.923969948625101e-10, 5.6900556657532386e-11, 7.2196378069550554e-12, 8.142575300637209e-13, 8.265148594630015e-14, 7.626879119275556e-15, 6.537890988090774e-16, 5.696578229090916e-17, 4.130236425383751e-18, 2.794940300527835e-19, 1.773133502306595e-20], [3.796981212905437e-08, 3.854138620397665e-08, 1.956078220080828e-08, 6.618412707186249e-09, 1.6795105499730888e-09, 3.409585726690197e-10, 5.768185870101554e-11, 8.364309391000613e-12, 1.06127756661135e-12, 1.196948203230514e-13, 1.214966321404656e-14, 1.1211415210810266e-15, 9.48348743611364e-17, 7.504068307880332e-18, 6.071394965046779e-19, 4.108526660590471e-20, 2.606483675389061e-21], [5.182834470573229e-09, 5.26085365612844e-09, 2.670023647131732e-09, 9.034055107435441e-10, 2.292512046808675e-10, 4.6540442113861274e-11, 7.873505525554021e-12, 1.1417183442170745e-12, 1.44863133280306e-13, 1.6338201479924722e-14, 1.6584146663035988e-15, 1.530344922987735e-16, 1.2944848243672891e-17, 1.010747075791377e-18, 7.426539848319838e-20, 5.608090323808439e-21, 3.55781940502566e-22], [6.602873932461173e-10, 6.702269514060248e-10, 3.401580667644039e-10, 1.1509286532684833e-10, 2.920635053978873e-11, 5.929200976485072e-12, 1.0030759169898732e-12, 1.4545365737698107e-13, 1.845540335007823e-14, 2.0814688423410505e-15, 2.1128019873141364e-16, 1.9496425473438717e-17, 1.649159383983955e-18, 1.2876806228226123e-19, 9.336175505293686e-21, 6.402503225208149e-22, 4.5326226680070334e-23], [7.886239255670471e-11, 8.004953825335839e-11, 4.06272772536566e-11, 1.3746285055148196e-11, 3.488303282747989e-12, 7.081628087072556e-13, 1.1980384229499612e-13, 1.7372470751681064e-14, 2.2042481481146333e-15, 2.486032818713291e-16, 2.523456019643353e-17, 2.3285841511830237e-18, 1.9696976810193058e-19, 1.537960224644892e-20, 1.1150798049574773e-21, 7.54577017922358e-23, 4.851272264982051e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9109834502579248, "lambda_away": 1.0150533816964797, "rho": -0.09482779564960894, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5576 |
| Legacy p draw | 0.2367 |
| Legacy p away | 0.2057 |
| Legacy p over 1 5 | 0.7983 |
| Legacy p under 3 5 | 0.6653 |
| Legacy p btts yes | 0.5536 |
| Legacy p over 2 5 | 0.5604 |
| Legacy goal margin distribution | {"-1": 0.1292297758693461, "-10": 2.24879404831954e-08, "-11": 2.045440161969315e-09, "-12": 1.7091618835689818e-10, "-13": 1.3205724639554938e-11, "-14": 9.485246457033478e-13, "-15": 6.328820785083971e-14, "-16": 3.5809255221392e-15, "-2": 0.05547414893867947, "-3": 0.016348273753827147, "-4": 0.0038013941012826876, "-5": 0.0007267431611738221, "-6": 0.00011768920958921788, "-7": 1.6508696522051043e-05, "-8": 2.04081020578018e-06, "-9": 2.2539524651867285e-07, "0": 0.23670609442935941, "1": 0.22360699735312348, "10": 1.1122850047556878e-05, "11": 1.9046764921056443e-06, "12": 2.9963026965953766e-07, "13": 4.358457013700237e-08, "14": 5.893688699232911e-09, "15": 7.403369314994757e-10, "16": 7.886239255670471e-11, "2": 0.17386521387607742, "3": 0.09646327353743767, "4": 0.0422280507147185, "5": 0.015198724231713083, "6": 0.0046337315640020155, "7": 0.0012237002607190092, "8": 0.0002847953732535303, "9": 5.9216550937604196e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5730 |
| Legacy raw p draw | 0.2400 |
| Legacy raw p away | 0.1869 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9110 |
| Legacy lambda away | 1.0151 |
| Legacy model home team | Buyuksehyr |
| Legacy model away team | Samsunspor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 76.5% |
| Market reference home draw last update utc | 2026-10-31T12:03:01Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.2% |
| Market reference draw away last update utc | 2026-10-31T12:03:01Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.3% |
| Market reference home away last update utc | 2026-10-31T12:03:01Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.23 |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.6% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.3% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.40 |
| Market reference under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.0% |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-31T12:02:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,539.1035 |
| Elo away rating | 1,443.8010 |
| Elo rating diff | 155.3026 |
| Elo home expectancy | 0.7097 |

</details>


---

## 2026-11-01 — Kasimpasa SK vs Besiktas JK

The model's most likely 1X2 outcome is **Besiktas JK win** at **56.0%**. Expected goals are 1.24 for Kasimpasa SK and 1.56 for Besiktas JK (2.80 combined). The most likely exact score is 1-2 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.5%; Under 3.5 goals: 65.6%; Double Chance 1X: 44.0%; Double Chance X2: 79.5%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 58.7%; BTTS No (at least one team does not score): 41.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Kasimpasa SK win | 20.5% | 4.88 |
| Draw | 23.5% | 4.26 |
| Besiktas JK win | 56.0% | 1.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Kasimpasa SK expected goals | 1.24 |
| Besiktas JK expected goals | 1.56 |
| Expected total goals | 2.80 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.6% |
| Under 1.5 | 19.4% |
| Over 2.5 | 57.5% |
| Under 2.5 | 42.5% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.67% |
| 2 | 1-1 | 11.01% |
| 3 | 0-1 | 9.61% |
| 4 | 0-2 | 9.00% |
| 5 | 1-3 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Kasimpasa SK win | 20.5% | 16.8% | 5.40 | +10.7% |
| Draw | 23.5% | 21.9% | 4.21 | -1.1% |
| Besiktas JK win | 56.0% | 61.3% | 1.59 | -10.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:00:00+00:00 |
| Fixture id | bf609ced8c6472e7d11428e42a2e468e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:03:01Z |
| Market best draw last update utc | 2026-10-31T12:03:01Z |
| Market best away last update utc | 2026-10-31T12:03:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Kasimpasa |
| Matched away-team name | Besiktas |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2413 |
| Dc lambda away | 1.5812 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.2163 |
| Shot lambda away | 1.4845 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.7% |
| P btts no | 41.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.58 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.16 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.54 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.26242258742898616, "-10": 3.1276980555845027e-06, "-11": 4.5871583962270576e-07, "-12": 6.181628532468148e-08, "-13": 7.701029638913491e-09, "-14": 8.853339774169513e-10, "-15": 8.472400959123661e-11, "-2": 0.1733490222836302, "-3": 0.08155996130484457, "-4": 0.030391355986388428, "-5": 0.00933130009950239, "-6": 0.0024302400136287515, "-7": 0.0005487482579828709, "-8": 0.00010926632017490621, "-9": 1.9446899680209665e-05, "0": 0.23480602305552703, "1": 0.11368232551275567, "10": 1.6758868956860323e-07, "11": 1.9455588466235773e-08, "12": 2.0753162561080173e-09, "13": 2.0464961340987687e-10, "14": 1.8623015950422648e-11, "15": 1.4106852765862812e-12, "2": 0.060269180296325046, "3": 0.022445622212489566, "4": 0.006620418827907087, "5": 0.0016090083349681499, "6": 0.0003317004447462226, "7": 5.928581449622644e-05, "8": 9.344255463166555e-06, "9": 1.3164049576890027e-06} |
| Raw goal margin distribution | {"-1": 0.21053641797059733, "-10": 1.7263800457718878e-06, "-11": 2.41633110696394e-07, "-12": 3.106897988658909e-08, "-13": 3.6927634183899578e-09, "-14": 4.0547959829995473e-10, "-15": 3.740520258935171e-11, "-2": 0.13529055049450617, "-3": 0.061381630247403014, "-4": 0.021969518382745235, "-5": 0.006464337739600276, "-6": 0.0016110782205630003, "-7": 0.00034778492664416804, "-8": 6.616151930990457e-05, "-9": 1.1244575046545125e-05, "0": 0.27170299233725864, "1": 0.1642971382807684, "10": 1.667031873049685e-07, "11": 1.8469055668138053e-08, "12": 1.879732234493067e-09, "13": 1.7684843849820024e-10, "14": 1.5370907242379223e-11, "15": 1.1223886208891368e-12, "2": 0.08476741961242026, "3": 0.03044252473092135, "4": 0.008624690808128934, "5": 0.0020087587738753312, "6": 0.0003962790600228094, "7": 6.771361538640903e-05, "8": 1.0196508047307674e-05, "9": 1.3717336534897586e-06} |
| Unadjusted home-win probability | 29.1% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 57.2% |
| P home draw | 44.0% |
| P draw away | 79.5% |
| P home away | 76.5% |
| Raw p home draw | 56.2% |
| Raw p draw away | 70.9% |
| Raw p home away | 72.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0493 |
| Totals anchor target over 2 5 | 0.5750 |
| Totals anchor reference over odds | 1.68 |
| Totals anchor reference under odds | 2.23 |
| Totals anchor reference last update utc | 2026-10-31T12:03:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5457 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.23, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.42, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.40 |
| Reference draw odds | 4.21 |
| Reference away odds | 1.59 |
| Market reference 1x2 last update utc | 2026-10-31T12:03:01Z |
| Market reference home last update utc | 2026-10-31T12:03:01Z |
| Market reference draw last update utc | 2026-10-31T12:03:01Z |
| Market reference away last update utc | 2026-10-31T12:03:01Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:39Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:39Z |
| Home probability edge | +3.7% |
| Draw probability edge | +1.6% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.1223 |
| Raw ev home | 0.5693 |
| Raw edge prob draw | 0.0527 |
| Raw ev draw | 0.1439 |
| Raw edge prob away | -0.1750 |
| Raw ev away | -0.3041 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.06667878573889564, 0.10310004771010833, 0.09046360942301977, 0.04681427454887375, 0.018169540621211795, 0.005641564835805974, 0.0014597348414084348, 0.0003237438855410796, 6.282568442950592e-05, 1.0837281636827933e-05, 1.6824648534778565e-06, 2.3745370824768504e-07, 3.072015134443284e-08, 3.6686445821281045e-09, 4.068208889709789e-10, 4.210538339112087e-11], [0.05160368564297197, 0.11690661367815937, 0.11002361810695506, 0.05693643994276409, 0.02209815207725196, 0.006861381930029377, 0.0017753581772039038, 0.0003937436705700318, 7.640983103666763e-05, 1.318051472556501e-05, 2.0462467913679964e-06, 2.887958625678671e-07, 3.736245128030085e-08, 4.461877577609688e-09, 4.947835534261268e-10, 5.1209394053790466e-11], [0.03679804762623599, 0.057128183877177385, 0.05040468747510643, 0.034623608125889146, 0.013438103235787435, 0.0041724737160632, 0.0010796127378598563, 0.0002394393918125282, 4.646556843804215e-05, 8.015200409688972e-06, 1.2443427636923674e-06, 1.7561959939855246e-07, 2.272047344463737e-08, 2.7133115612452806e-09, 3.008827365775319e-10, 3.114093529319815e-11], [0.014918169360891817, 0.023160139663286717, 0.017977811360323663, 0.010574651617979451, 0.005447895007823578, 0.001691548154465701, 0.00043768207028696863, 9.707029663664803e-05, 1.8837445574547368e-05, 3.2494147077514498e-06, 5.044647009622268e-07, 7.1197335074148e-08, 9.21102864612537e-09, 1.0999942662899174e-09, 1.219798307677595e-10, 1.2624738993741635e-11], [0.0045359426267817405, 0.007041954156675466, 0.005466241796349886, 0.0028287412566995744, 0.0012479113575396103, 0.0005143235200968569, 0.0001330793820317683, 2.9514700205964034e-05, 5.7276177990891535e-06, 9.880004931181595e-07, 1.5338496872142207e-07, 2.1647899233715677e-08, 2.8006584763675116e-09, 3.344586564863656e-10, 3.708856633827804e-11, 3.838613865306255e-12], [0.0011033404979242404, 0.0017129125839712351, 0.001329630121366432, 0.0006880741322074771, 0.00026705510265884446, 9.425000463583162e-05, 3.2370751509826506e-05, 7.179271587135966e-06, 1.3932082467388866e-06, 2.4032511998499716e-07, 3.730996215956572e-08, 5.265720024436924e-09, 6.812431664338515e-10, 8.135503707738928e-11, 9.021568528966526e-12, 9.33719511459264e-13], [0.0002236507297608517, 0.00034721298651000634, 0.00026952037699610576, 0.00013947487841449064, 5.4132943283036116e-05, 1.680804791111377e-05, 4.943295028409271e-06, 1.4552618458536424e-06, 2.8240787107715126e-07, 4.871468831754916e-08, 7.562851431661665e-09, 1.0673786817372058e-09, 1.3809021929691365e-10, 1.6490932260993295e-11, 1.828701465129615e-12, 1.89268000696689e-13], [3.885834415706453e-05, 6.032675028619431e-05, 4.6827996393552075e-05, 2.4233155118654544e-05, 9.405364080753722e-06, 2.9203254156017248e-06, 7.556238174111834e-07, 1.9048382467271235e-07, 4.906714258752555e-08, 8.463965783485703e-09, 1.3140126305623997e-09, 1.8545241593983984e-10, 2.399257660326781e-11, 2.8652279469587694e-12, 3.177289471334122e-13, 3.2884494125531095e-14], [5.907535147383768e-06, 9.171322282870503e-06, 7.11914108996268e-06, 3.6841048866316182e-06, 1.4298735596249555e-06, 4.4396963917796965e-07, 1.1487556550309981e-07, 2.5477409235378024e-08, 5.619734267001819e-09, 1.2867551728424602e-09, 1.997659953748268e-10, 2.819385872191524e-11, 3.6475303473355544e-12, 4.3559331127206326e-13, 4.830352304630125e-14, 4.999345933663311e-15], [7.98317805057119e-07, 1.2393713607569665e-06, 9.620487981942681e-07, 4.978534115025045e-07, 1.9322669999424884e-07, 5.999606587487193e-08, 1.5523768715577377e-08, 3.442902820195051e-09, 6.68129147030898e-10, 1.3099913042923254e-10, 2.699548068254977e-11, 3.809991620775665e-12, 4.929108922955321e-13, 5.886412648874009e-14, 6.5275214675492345e-15, 6.755891878613411e-16], [9.709297901310178e-08, 1.5073477850190969e-07, 1.1700626389758723e-07, 6.054990948267181e-08, 2.3500610669669563e-08, 7.296839338865584e-09, 1.8880312333732277e-09, 4.187326014123277e-10, 8.125917878791533e-11, 1.4017015717355369e-11, 2.4734666800748965e-12, 4.633786621477114e-13, 5.994879059168066e-14, 7.159170648069017e-15, 7.938899782035839e-16, 8.216648360211181e-17], [1.0735126143225994e-08, 1.6666054310382987e-08, 1.2936846878688235e-08, 6.69472625996659e-09, 2.5983549227354774e-09, 8.067781166649091e-10, 2.0875096900546375e-10, 4.62973465448612e-11, 8.984455348367802e-12, 1.5497972500883524e-12, 2.406027166839869e-13, 3.8597426212257324e-14, 6.6282632964499874e-15, 7.915567198482093e-16, 8.77767800152509e-17, 9.084771887521894e-18], [1.0880226006950043e-09, 1.689131875320279e-09, 1.3111705999491494e-09, 6.785214611480181e-10, 2.633475231539071e-10, 8.176828226946088e-11, 2.1157252291650644e-11, 4.692311829498483e-12, 9.105892509821706e-13, 1.5707448725743372e-13, 2.438547903845378e-14, 3.4416305417064412e-15, 5.060966995218315e-16, 8.022556879504431e-17, 8.896320285261881e-18, 9.207564963751864e-19], [1.0179034239811704e-10, 1.5802733494193517e-10, 1.2266703304316873e-10, 6.3479317259227e-11, 2.4637571438689827e-11, 7.649860806381798e-12, 1.979374282845588e-12, 4.3899090649246176e-13, 8.519050209279874e-14, 1.469515966830988e-14, 2.281392187332083e-15, 3.2198297261870864e-16, 4.165597464100052e-17, 5.654372973874216e-18, 8.322984167255996e-19, 8.61417023611936e-20], [8.842815225778472e-12, 1.3728281982275638e-11, 1.0656432446731498e-11, 5.514628008484805e-12, 2.140335583037408e-12, 6.645650659979536e-13, 1.7195384781597006e-13, 3.813638288716123e-14, 7.40074010215579e-15, 1.2766101242879809e-15, 1.9819099823054899e-16, 2.797157240692019e-17, 3.6187724505276375e-18, 4.321590019441282e-19, 5.447108578385659e-20, 7.48337356244251e-21], [7.169870342315749e-13, 1.1131070741897195e-12, 8.64037492629901e-13, 4.471332578755559e-13, 1.735412108882104e-13, 5.388380550288345e-14, 1.3942243077845872e-14, 3.092147847087732e-15, 6.000616954535802e-16, 1.0350922002926537e-16, 1.6069585579314978e-17, 2.2679717070607356e-18, 2.9341480745848385e-19, 3.5040017597237565e-20, 3.885634268827943e-21, 4.571104667214406e-22]] |
| Legacy trial inputs | {"lambda_home": 1.216219635814774, "lambda_away": 1.5524786656465595, "rho": -0.09482779564960894, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2278 |
| Legacy p draw | 0.2459 |
| Legacy p away | 0.5263 |
| Legacy p over 1 5 | 0.7786 |
| Legacy p under 3 5 | 0.6944 |
| Legacy p btts yes | 0.5580 |
| Legacy p over 2 5 | 0.5344 |
| Legacy goal margin distribution | {"-1": 0.25374336886559185, "-10": 1.995119206042501e-06, "-11": 2.7765528953386424e-07, "-12": 3.54955363976138e-08, "-13": 4.194569070847429e-09, "-14": 4.5803028302476936e-10, "-15": 4.210538339112087e-11, "-2": 0.16267025048512945, "-3": 0.07355354037832354, "-4": 0.026213581280667794, "-5": 0.007676226252665693, "-6": 0.0019033522868174325, "-7": 0.0004086957276444592, "-8": 7.732462312893684e-05, "-9": 1.3068702725733626e-05, "0": 0.2459120394044154, "1": 0.12982306707135946, "10": 1.1513587746008169e-07, "11": 1.2552613220808816e-08, "12": 1.2571535013415466e-09, "13": 1.1638266187302258e-10, "14": 9.955922299968191e-12, "15": 7.169870342315749e-13, "2": 0.06616967488808072, "3": 0.023439093802713296, "4": 0.0065441005477472995, "5": 0.0015012663227835276, "6": 0.00029161880354104495, "7": 4.9054947288927694e-05, "8": 7.270878670728244e-06, "9": 9.626932679776123e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2873 |
| Legacy raw p draw | 0.2728 |
| Legacy raw p away | 0.4399 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2162 |
| Legacy lambda away | 1.5525 |
| Legacy model home team | Kasimpasa |
| Legacy model away team | Besiktas |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 40.3% |
| Market reference home draw last update utc | 2026-10-31T12:03:01Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.6% |
| Market reference draw away last update utc | 2026-10-31T12:03:01Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.2% |
| Market reference home away last update utc | 2026-10-31T12:03:01Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.35 |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 3.95 |
| Market reference over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.8% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.4% |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-10-31T12:02:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,457.3688 |
| Elo away rating | 1,573.4966 |
| Elo rating diff | -56.1278 |
| Elo home expectancy | 0.4199 |

</details>


---

## 2026-11-01 — Trabzonspor vs Gazişehir Gaziantep

The model's most likely 1X2 outcome is **Trabzonspor win** at **72.5%**. Expected goals are 2.31 for Trabzonspor and 0.95 for Gazişehir Gaziantep (3.26 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 70.5%; Under 3.5 goals: 51.0%; Double Chance 1X: 88.9%; Double Chance X2: 27.5%; Double Chance 12 (either team wins): 83.6%; Under 4.5 goals: 70.1%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Trabzonspor win | 72.5% | 1.38 |
| Draw | 16.4% | 6.09 |
| Gazişehir Gaziantep win | 11.1% | 9.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Trabzonspor expected goals | 2.31 |
| Gazişehir Gaziantep expected goals | 0.95 |
| Expected total goals | 3.26 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 49.0% |
| Under 3.5 | 51.0% |
| Over 4.5 | 29.9% |
| Under 4.5 | 70.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.75% |
| 2 | 2-0 | 9.33% |
| 3 | 3-1 | 8.30% |
| 4 | 3-0 | 7.95% |
| 5 | 1-1 | 7.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Trabzonspor win | 72.5% | 74.8% | 1.31 | -5.0% |
| Draw | 16.4% | 15.0% | 5.82 | -4.4% |
| Gazişehir Gaziantep win | 11.1% | 10.3% | 8.28 | -8.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:00:00+00:00 |
| Fixture id | cd2960ff2b4d605144a83562b0085400 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:03:01Z |
| Market best draw last update utc | 2026-10-31T12:03:01Z |
| Market best away last update utc | 2026-10-31T12:03:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Trabzonspor |
| Matched away-team name | Gaziantep |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3917 |
| Dc lambda away | 0.8904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9971 |
| Shot lambda away | 1.1671 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.96 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.64 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.04 |
| Fair Under 3.5 odds | 1.96 |
| Fair Over 4.5 odds | 3.34 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.070746090171473, "-10": 1.2993737791094745e-08, "-11": 1.2103345479578392e-09, "-12": 1.0365174551030307e-10, "-13": 8.213055125079456e-12, "-14": 6.054349436008164e-13, "-15": 4.171841754234401e-14, "-16": 2.697238826224913e-15, "-17": 1.6291095588582386e-16, "-18": 8.236061404601844e-18, "-2": 0.029284367122063747, "-3": 0.008513920097031225, "-4": 0.001980329146304239, "-5": 0.0003818490957157582, "-6": 6.269498239471354e-05, "-7": 8.947692263803757e-06, "-8": 1.1281371372476866e-06, "-9": 1.2730080263673982e-07, "0": 0.16418984766948805, "1": 0.21760380527029793, "10": 0.00011889702678454067, "11": 2.7082581836915235e-05, "12": 5.671644383495413e-06, "13": 1.098967498041535e-06, "14": 1.9810495220889394e-07, "15": 3.338131288918298e-08, "16": 5.277676034387555e-09, "17": 7.79509397799701e-10, "18": 9.636922748563756e-11, "2": 0.20955152839964605, "3": 0.14898148480476964, "4": 0.08473988024931406, "5": 0.0399567329637807, "6": 0.0160427467475356, "7": 0.005598925906426541, "8": 0.0017262485050121002, "9": 0.00047634356163310927} |
| Raw goal margin distribution | {"-1": 0.08550332823180089, "-10": 7.388708976116155e-09, "-11": 6.25055531246571e-10, "-12": 4.858972090489136e-11, "-13": 3.4934049251501842e-12, "-14": 2.3358464592658685e-13, "-15": 1.459565593750898e-14, "-16": 8.556955757319018e-16, "-17": 4.6978257678220794e-17, "-18": 2.2009061165414053e-18, "-2": 0.033706241094768684, "-3": 0.009118222163406093, "-4": 0.001955902093077542, "-5": 0.00034594679584210047, "-6": 5.192536214345006e-05, "-7": 6.7592006486901585e-06, "-8": 7.760502958375936e-07, "-9": 7.965259992558556e-08, "0": 0.19751160515124516, "1": 0.22075664077061874, "10": 5.649967418020383e-05, "11": 1.1688094740757664e-05, "12": 2.2218629305956245e-06, "13": 3.9063353629857717e-07, "14": 6.387231063174554e-08, "15": 9.759772416245653e-09, "16": 1.3992106375066546e-09, "17": 1.8784881320305918e-10, "18": 2.1520918633102182e-11, "2": 0.20156067280488207, "3": 0.13333783037711025, "4": 0.06994200281976579, "5": 0.0302515759227978, "6": 0.011103655104299056, "7": 0.0035345123737461556, "8": 0.0009923657678296304, "9": 0.0002490746909742563} |
| Unadjusted home-win probability | 67.2% |
| Unadjusted draw probability | 19.8% |
| Unadjusted away-win probability | 13.1% |
| Raw p over 1 5 | 84.4% |
| Raw p under 3 5 | 59.0% |
| Raw p btts yes | 55.9% |
| P home draw | 88.9% |
| P draw away | 27.5% |
| P home away | 83.6% |
| Raw p home draw | 86.9% |
| Raw p draw away | 32.8% |
| Raw p home away | 80.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1049 |
| Totals anchor target over 2 5 | 0.7050 |
| Totals anchor reference over odds | 1.38 |
| Totals anchor reference under odds | 3.08 |
| Totals anchor reference last update utc | 2026-10-31T12:03:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6479 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.57, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.31 |
| Reference draw odds | 5.82 |
| Reference away odds | 8.28 |
| Market reference 1x2 last update utc | 2026-10-31T12:03:01Z |
| Market reference home last update utc | 2026-10-31T12:03:01Z |
| Market reference draw last update utc | 2026-10-31T12:03:01Z |
| Market reference away last update utc | 2026-10-31T12:03:01Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.92 |
| Market reference over 2 5 last update utc | 2026-10-31T12:03:02Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:03:02Z |
| Home probability edge | -2.3% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0758 |
| Raw ev home | -0.1199 |
| Raw edge prob draw | 0.0476 |
| Raw ev draw | 0.1495 |
| Raw edge prob away | 0.0282 |
| Raw ev away | 0.0821 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.039545102546268904, 0.02356153713558169, 0.013426352781123033, 0.003913656014863232, 0.0008555955395539292, 0.00014963884910159357, 2.1809161109897407e-05, 2.7244997510804228e-06, 2.978123046184045e-07, 2.8936498647366604e-08, 2.530415455928652e-09, 2.011615615669497e-10, 1.4659177518645625e-11, 9.860798937282745e-13, 6.15927960610294e-14, 3.590744570862224e-15, 1.9625032366408437e-16, 1.0095022985296858e-17, 4.9043409964788425e-19], [0.08262061978429414, 0.07719925375701066, 0.03294816510778551, 0.009604081365572902, 0.002099624787331839, 0.00036721256972110597, 5.351951142841119e-05, 6.685901160062459e-06, 7.308290750033875e-07, 7.100994220970413e-08, 6.209619812049656e-09, 4.936489046501454e-10, 3.597350740759206e-11, 2.4198323757518033e-12, 1.5114824160751822e-13, 8.811659198095138e-15, 4.815967651044955e-16, 2.4773107746289208e-17, 1.2035214591117746e-18], [0.11054177109398891, 0.09666567109957269, 0.037829127730043925, 0.01178417041843266, 0.0025762314340001314, 0.00045056839240199066, 6.566823201273767e-05, 8.203574675387266e-06, 8.967244277476701e-07, 8.712892243935001e-08, 7.61917931694906e-09, 6.057052827689074e-10, 4.413935343773786e-11, 2.96912489747519e-12, 1.8545830358478838e-13, 1.0811871506183206e-14, 5.909173545010589e-16, 3.0396506689638196e-17, 1.476716141457624e-18], [0.09042288164393904, 0.07907226788900175, 0.034573237633204475, 0.009019923395696818, 0.0021073506217475168, 0.0003685637747202745, 5.371644322584407e-05, 6.710502777262775e-06, 7.335182528287334e-07, 7.127123225480605e-08, 6.232468891914623e-09, 4.954653481022417e-10, 3.610587646860671e-11, 2.4287364544050724e-12, 1.5170441064015974e-13, 8.844082810305573e-15, 4.833688611879351e-16, 2.4864263523056737e-17, 1.2079499682267905e-18], [0.05547426174655179, 0.04851068231867134, 0.02121061393998028, 0.00618269519491967, 0.001209767457175285, 0.0002261131578358642, 3.295493328047461e-05, 4.116880381922557e-06, 4.500120192312188e-07, 4.3724762153357115e-08, 3.8236075244621236e-09, 3.039670259039183e-10, 2.2150884879949074e-11, 1.4900250836464037e-12, 9.307036041051336e-14, 5.425827576022141e-15, 2.9654585474571105e-16, 1.52541772362963e-17, 7.410749524442249e-19], [0.02722668121498618, 0.02380896728371567, 0.010410136267453463, 0.00303445716665113, 0.0006633868707147711, 0.00010384388327828671, 1.6174229897604593e-05, 2.020558475765625e-06, 2.2086519774699323e-07, 2.1460045124882543e-08, 1.8766206143558766e-09, 1.4918654261618644e-10, 1.0871619779486628e-11, 7.313019890218806e-13, 4.5678787850086664e-14, 2.6629877187868766e-15, 1.4554424337677536e-16, 7.486726415703118e-18, 3.637184317800161e-19], [0.011135677258901036, 0.00973783669943799, 0.004257732214227245, 0.0012410890404515062, 0.00027132436861257556, 4.745310649184753e-05, 6.190096947027457e-06, 8.264057925825475e-07, 9.033357905113009e-08, 8.777130586911523e-09, 7.675353941913862e-10, 6.101710218837559e-11, 4.4464783713415725e-12, 2.9910156380196865e-13, 1.8682564909761924e-14, 1.0891585186851728e-15, 5.952740652954157e-17, 3.0620613813581606e-18, 1.4876036625376594e-19], [0.0039038378892881664, 0.003413796483422732, 0.0014926345253996223, 0.000435088976399899, 9.511826949100112e-05, 1.663565051144295e-05, 2.4245681141645635e-06, 2.710943098667967e-07, 3.16682713027561e-08, 3.077001438509434e-09, 2.6907512525284565e-10, 2.139078476139818e-11, 1.5588033252372329e-12, 1.0485612957057814e-13, 6.549552673638808e-15, 3.8182664545934986e-16, 2.0868541684371508e-17, 1.0734678243586012e-18, 5.215096852251519e-20], [0.0011974984702392195, 0.0010471787462855344, 0.0004578641868549041, 0.00013346311973826103, 2.917743652210034e-05, 5.102969591424219e-06, 7.437339075143483e-07, 9.291062758820825e-08, 9.089907405940534e-09, 9.438671942934601e-10, 8.253853259476991e-11, 6.56160239114373e-12, 4.781614017573272e-13, 3.2164515616930103e-14, 2.0090689034384533e-15, 1.1712495159923707e-16, 6.4014048359254485e-18, 3.2928520957483825e-19, 1.5997258799748214e-20], [0.0003265168794614071, 0.00028552983153887196, 0.00012484390521111293, 3.639082843372295e-05, 7.955689097436874e-06, 1.3914052906016958e-06, 2.027908015470886e-07, 2.5333550683235863e-08, 2.7691847320410792e-09, 2.4082050994220267e-10, 2.2505435094864184e-11, 1.7891245711526997e-12, 1.3037826156847248e-13, 8.770163411173059e-15, 5.478043816144745e-16, 3.19359687328966e-17, 1.7454441764572722e-18, 8.97848153924517e-20, 4.361905382799253e-21], [8.012698780043136e-05, 7.00687981770283e-05, 3.06365970614129e-05, 8.930280942186803e-06, 1.9523199055003064e-06, 3.414497741415395e-07, 4.9764704686649536e-08, 6.216833597961587e-09, 6.795557755158025e-10, 6.602804677335004e-11, 5.167880979342648e-12, 4.3904977568900404e-13, 3.199472379918176e-14, 2.1521912674591525e-15, 1.3443076840330368e-16, 7.837061842795843e-18, 4.28330640866168e-19, 2.2033123737681934e-20, 1.0704081821763883e-21], [1.7875545792639874e-05, 1.5631662250530378e-05, 6.834724588249083e-06, 1.9922581680069095e-06, 4.355434396157995e-07, 7.617409865394657e-08, 1.1102017958032049e-08, 1.3869146553015213e-09, 1.516022343700313e-10, 1.4730210208766042e-11, 1.2881154708996463e-12, 9.165289003639374e-14, 7.137709354800674e-15, 4.801327818762536e-16, 2.999018710797068e-17, 1.7483716996771167e-18, 9.555636865152133e-20, 4.9153739974450124e-21, 2.387975762294589e-22], [3.6555375075236737e-06, 3.1966647801760303e-06, 1.3976967403270028e-06, 4.0741550173076604e-07, 8.906835059139742e-08, 1.5577553712847363e-08, 2.2703554635796155e-09, 2.836231464482881e-10, 3.1002558489275703e-11, 3.012318422972206e-12, 2.634187773910641e-13, 2.0941119562754236e-14, 1.3658490439926478e-15, 9.818684213060478e-17, 6.132973790147388e-18, 3.575408773193466e-19, 1.9541215341923792e-20, 1.0051907907933725e-21, 4.883394928125522e-23], [6.900508122923727e-07, 6.034300355684707e-07, 2.6384130077067845e-07, 7.690726666904511e-08, 1.6813310641359242e-08, 2.940553494788283e-09, 4.2857189363017196e-10, 5.353915318574865e-11, 5.852310535628651e-12, 5.686312260172557e-13, 4.972520209070522e-14, 3.9530264796487456e-15, 2.880675435689124e-16, 1.7343431511599166e-17, 1.1577130687207505e-18, 6.749250207777957e-20, 3.688768475804611e-21, 1.8974848986453387e-22, 9.218317771222174e-24], [1.209556654673954e-07, 1.0577232895752828e-07, 4.6247464018604966e-08, 1.3480702367887947e-08, 2.9471238075638822e-09, 5.154353831176896e-10, 7.512229196926957e-11, 9.38461891035242e-12, 1.0258231752633455e-12, 9.967261413687974e-14, 8.71608989112185e-15, 6.929068699560669e-16, 5.049396480845335e-17, 3.396580973858018e-18, 1.8988820516845099e-19, 1.1830433871612483e-20, 6.465863640735088e-22, 3.326009397301264e-23, 1.615834284440592e-24], [1.9788284038660383e-08, 1.730429807280414e-08, 7.566061089669003e-09, 2.205435904681254e-09, 4.821479240002415e-10, 8.432496092924192e-11, 1.2289967943037703e-11, 1.5353187787858989e-12, 1.6782413859748813e-13, 1.6306387896712746e-14, 1.4259477785148313e-15, 1.1335920398640438e-16, 8.260786412994737e-18, 5.556788829302902e-19, 3.470896864385038e-20, 1.811066939305076e-21, 1.0578119328573505e-22, 5.441334096648189e-24, 2.6434964957085864e-25], [3.035018427631977e-09, 2.6540382898077935e-09, 1.160440934993232e-09, 3.3825765784398666e-10, 7.394920303985582e-11, 1.293329981667887e-11, 1.884967848109119e-12, 2.354787700035499e-13, 2.573994552785493e-14, 2.500984302527152e-15, 2.1870404610011724e-16, 1.7386412706036774e-17, 1.266994093130481e-18, 8.522697805653463e-20, 5.3234711626525546e-21, 3.1034839133615397e-22, 1.518146101289635e-23, 8.345619671703195e-25, 4.054449876594382e-26], [4.3811244545780764e-10, 3.831170166546831e-10, 1.6751253014167138e-10, 4.882833274540808e-11, 1.0674751061964802e-11, 1.8669539396982128e-12, 2.720997889257517e-13, 3.399194510332696e-14, 3.71562504480672e-15, 3.610232935839773e-16, 3.157047205911006e-17, 2.5097718415909814e-18, 1.8289374307196187e-19, 1.2302725886399458e-20, 7.684562795928563e-22, 4.4799560831090405e-23, 2.4484972794929757e-24, 1.1272876707448958e-25, 5.852699061886105e-27], [5.972914041197596e-11, 5.2231454091820973e-11, 2.2837469095729698e-11, 6.6569082272601934e-12, 1.4553197738464803e-12, 2.5452724560335587e-13, 3.709615343575173e-14, 4.634220467832667e-15, 5.065619393386716e-16, 4.9219352743879265e-17, 4.304094024356011e-18, 3.4216447462880376e-19, 2.4934434466936657e-20, 1.6772663035192695e-21, 1.047658734649817e-22, 6.1076540669346335e-24, 3.338107358542531e-25, 1.717106493518743e-26, 7.466357455493095e-28]] |
| Legacy trial inputs | {"lambda_home": 2.453992208078239, "lambda_away": 0.8744718864453694, "rho": -0.09482779564960894, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7304 |
| Legacy p draw | 0.1649 |
| Legacy p away | 0.1047 |
| Legacy p over 1 5 | 0.8543 |
| Legacy p under 3 5 | 0.5708 |
| Legacy p btts yes | 0.5356 |
| Legacy p over 2 5 | 0.6531 |
| Legacy goal margin distribution | {"-1": 0.07064436971216365, "-10": 3.070728244435941e-09, "-11": 2.4026147276868884e-10, "-12": 1.7273616462134046e-11, "-13": 1.148538993598832e-12, "-14": 7.102097795210111e-14, "-15": 4.1039457926245835e-15, "-16": 2.225001475518312e-16, "-17": 1.1298544444408633e-17, "-18": 4.9043409964788425e-19, "-2": 0.026010298342113207, "-3": 0.006521912436302451, "-4": 0.0012956591055426382, "-5": 0.00021214111744961424, "-6": 2.9467035277405357e-05, "-7": 3.5490053618307675e-06, "-8": 3.769597927509127e-07, "-9": 3.5789466432885975e-08, "0": 0.1649134892967196, "1": 0.22075558400446146, "10": 9.723628742619264e-05, "11": 2.1350027933912298e-05, "12": 4.307496296268564e-06, "13": 8.037383892757216e-07, "14": 1.3947068812771205e-07, "15": 2.261649176683711e-08, "16": 3.4409729133823902e-09, "17": 4.903438995496286e-10, "18": 5.972914041197596e-11, "2": 0.21414783987075767, "3": 0.1506852196718979, "4": 0.08400667024590666, "5": 0.038598924090028165, "6": 0.015045759576553517, "7": 0.005085242380847198, "8": 0.0015157492425953137, "9": 0.00040384515900365124} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7132 |
| Legacy raw p draw | 0.1799 |
| Legacy raw p away | 0.1069 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.4540 |
| Legacy lambda away | 0.8745 |
| Legacy model home team | Trabzonspor |
| Legacy model away team | Gaziantep |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 86.9% |
| Market reference home draw last update utc | 2026-10-31T12:03:01Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 30.1% |
| Market reference draw away last update utc | 2026-10-31T12:03:01Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.1% |
| Market reference home away last update utc | 2026-10-31T12:03:01Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.09 |
| Market reference dc draw away odds | 3.15 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-31T12:03:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.7% |
| Market under 3 5 odds | 1.85 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 1.92 |
| Market reference under 3 5 last update utc | 2026-10-31T12:03:01Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-31T12:02:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,616.7819 |
| Elo away rating | 1,414.5620 |
| Elo rating diff | 262.2199 |
| Elo home expectancy | 0.8190 |

</details>


---

## 2026-11-02 — Genclerbirligi SK vs Alanyaspor

The model's most likely 1X2 outcome is **Alanyaspor win** at **35.4%**. Expected goals are 1.15 for Genclerbirligi SK and 1.17 for Alanyaspor (2.32 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 47.1%; Under 3.5 goals: 74.4%; Double Chance 1X: 64.6%; Double Chance X2: 64.7%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 88.3%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genclerbirligi SK win | 35.3% | 2.83 |
| Draw | 29.3% | 3.41 |
| Alanyaspor win | 35.4% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genclerbirligi SK expected goals | 1.15 |
| Alanyaspor expected goals | 1.17 |
| Expected total goals | 2.32 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 47.1% |
| Under 2.5 | 52.9% |
| Over 3.5 | 25.6% |
| Under 3.5 | 74.4% |
| Over 4.5 | 11.7% |
| Under 4.5 | 88.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.00% |
| 2 | 0-0 | 9.01% |
| 3 | 1-0 | 8.66% |
| 4 | 0-1 | 8.61% |
| 5 | 2-1 | 8.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genclerbirligi SK win | 35.3% | 35.8% | 2.68 | -5.4% |
| Draw | 29.3% | 28.7% | 3.31 | -3.0% |
| Alanyaspor win | 35.4% | 35.5% | 2.70 | -4.5% |
| Over 2.5 | 47.1% | 47.1% | 2.03 | -4.4% |
| Under 2.5 | 52.9% | 52.9% | 1.82 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T17:00:00+00:00 |
| Fixture id | 10a70d197a090f08183739878151539d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:03:01Z |
| Market best draw last update utc | 2026-10-31T12:03:01Z |
| Market best away last update utc | 2026-10-31T12:03:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genclerbirligi |
| Matched away-team name | Alanyaspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1093 |
| Dc lambda away | 1.1527 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.3271 |
| Shot lambda away | 1.2460 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.09 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 3.91 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.55 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.19174441445635865, "-10": 3.1252987573277813e-07, "-11": 3.623921615255394e-08, "-12": 3.858199620498782e-09, "-13": 3.776604039583388e-10, "-14": 3.1177071816312925e-11, "-2": 0.10582727433141616, "-3": 0.040420714479445674, "-4": 0.012104451683582582, "-5": 0.002969388183839093, "-6": 0.0006156314709974512, "-7": 0.00011039387867596154, "-8": 1.74274271232464e-05, "-9": 2.456126970958964e-06, "0": 0.2931746526808787, "1": 0.19327310151620428, "10": 2.7318602000513973e-07, "11": 3.117608581282647e-08, "12": 3.2666555857571962e-09, "13": 3.146994386099908e-10, "14": 2.5568526419837573e-11, "2": 0.10508909553427123, "3": 0.03950389247255682, "4": 0.01164278524558224, "5": 0.002810959592296447, "6": 0.0005735671903004695, "7": 0.0001012241972204062, "8": 1.5727094089819242e-05, "9": 2.181433031111916e-06} |
| Raw goal margin distribution | {"-1": 0.1988628882999839, "-10": 1.481890974281272e-07, "-11": 1.5619269242844864e-08, "-12": 1.5048870554994185e-09, "-13": 1.228379299593574e-10, "-2": 0.10294577548198754, "-3": 0.0363533487816426, "-4": 0.00999887506660629, "-5": 0.0022445115646449977, "-6": 0.0004248467251114532, "-7": 6.94486618901564e-05, "-8": 9.984197748400608e-06, "-9": 1.2804782564372075e-06, "0": 0.3072897316932577, "1": 0.19551682039565, "10": 1.26349888539595e-07, "11": 1.3106755035059181e-08, "12": 1.2428371856652337e-09, "13": 9.984324384073061e-11, "2": 0.09971494441844751, "3": 0.03465548700489811, "4": 0.009381117727003003, "5": 0.002072531559655292, "6": 0.0003860890112443019, "7": 6.211477401376882e-05, "8": 8.788607359193845e-06, "9": 1.109315183698526e-06} |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 30.7% |
| Unadjusted away-win probability | 35.1% |
| Raw p over 1 5 | 68.7% |
| Raw p under 3 5 | 79.4% |
| Raw p btts yes | 48.5% |
| P home draw | 64.6% |
| P draw away | 64.7% |
| P home away | 70.7% |
| Raw p home draw | 64.9% |
| Raw p draw away | 65.8% |
| Raw p home away | 69.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1023 |
| Totals anchor target over 2 5 | 0.4710 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.82 |
| Totals anchor reference last update utc | 2026-10-31T12:03:01Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4153 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.9, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:03:01Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.68 |
| Reference draw odds | 3.31 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-31T12:03:01Z |
| Market reference home last update utc | 2026-10-31T12:03:01Z |
| Market reference draw last update utc | 2026-10-31T12:03:01Z |
| Market reference away last update utc | 2026-10-31T12:03:01Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-31T12:03:01Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:03:01Z |
| Market best over 2 5 last update utc | 2026-10-31T12:03:01Z |
| Market best under 2 5 last update utc | 2026-10-31T12:03:01Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0160 |
| Raw ev home | -0.0840 |
| Raw edge prob draw | 0.0202 |
| Raw ev draw | 0.0171 |
| Raw edge prob away | -0.0041 |
| Raw ev away | -0.0525 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.11586743859685074, 0.11054206795408435, 0.06994918698872808, 0.026471430789359436, 0.007513346597031571, 0.0017060015391330329, 0.00032280790966861494, 5.2355477741869586e-05, 7.429988459217631e-06, 9.372633370545268e-07, 1.064088202865362e-07, 1.0982493186790029e-08, 1.0390482034322022e-09, 9.074199909537227e-11], [0.10954857572782169, 0.13995739611534866, 0.07591874733151983, 0.028730539297405162, 0.008154545985017548, 0.0018515940695278657, 0.0003503567830559181, 5.682356660909466e-05, 8.064073948455604e-06, 1.0172506862789714e-06, 1.1548989615105085e-07, 1.191975434185402e-08, 1.127722013900613e-09, 9.848604677547852e-11], [0.06662119415651788, 0.07563597546185613, 0.039379700566110794, 0.015591221624702306, 0.004425233107709806, 0.001004805833895388, 0.00019012835769622734, 3.083648417934307e-05, 4.376136585076734e-06, 5.520321332460471e-07, 6.2672981793541e-08, 6.4685013299641865e-09, 6.119816849859155e-10, 5.344549109650602e-11], [0.02410224632969569, 0.027363618065530018, 0.015533149553651048, 0.005391532927166179, 0.001600962873432848, 0.00036351911773248454, 6.878472488332956e-05, 1.1156037459883585e-05, 1.583200710844563e-06, 1.9971443961428766e-07, 2.2673860241165808e-08, 2.340177392684998e-09, 2.214030160753234e-10, 1.933553440355916e-11], [0.006539791339966121, 0.007424716767358385, 0.004214692503918505, 0.0015949998237133113, 0.0004152165360285835, 9.863558547777246e-05, 1.8663727104959443e-05, 3.0270272807972522e-06, 4.2957831218631493e-07, 5.418958651362333e-08, 6.1522197068446615e-09, 6.349728418388077e-10, 6.007446390537578e-11, 5.246413911645128e-12], [0.0014195812352179498, 0.001611670472624688, 0.0009148760380491682, 0.0003462238628443893, 9.826820100554014e-05, 2.0465247163871755e-05, 4.051303076829714e-06, 6.570715949378984e-07, 9.324782387314672e-08, 1.1762840151924156e-08, 1.335451728773353e-09, 1.3783246043933506e-10, 1.3040260345109312e-11, 1.1388300259127852e-12], [0.00025678837680282905, 0.0002915354432272429, 0.00016549213736991963, 6.262851434251745e-05, 1.7775757527305266e-05, 4.036213331728846e-06, 7.004817987466103e-07, 1.1885783224053667e-07, 1.6867620350803765e-08, 2.1277828660083668e-09, 2.4157017099313166e-10, 2.4932545534474436e-11, 2.3588556991546923e-12, 2.0600322584819844e-13], [3.981472170915521e-05, 4.520221158358915e-05, 2.5659352173466614e-05, 9.710474051244897e-06, 2.756109322122882e-06, 6.258099083859924e-07, 1.1841512668192062e-07, 1.7615019847207028e-08, 2.6153037708501765e-09, 3.2991011401065285e-10, 3.745515763242526e-11, 3.865760492415729e-12, 3.657376723324657e-13, 3.1940546571669875e-14], [5.40157063941147e-06, 6.132478853173449e-06, 3.4811445961870316e-06, 1.317397416792953e-06, 3.73914937849834e-07, 8.49021739165707e-08, 1.6065104667055167e-08, 2.6055626415110357e-09, 3.39145082754616e-10, 4.4758137417172076e-11, 5.081454072183429e-12, 5.24458729797629e-13, 4.9618778878554094e-14, 4.333299622903413e-15], [6.513942385585931e-07, 7.395370087161967e-07, 4.198033655249355e-07, 1.588695482254033e-07, 4.509170618805682e-08, 1.0238649204517219e-08, 1.9373469904488168e-09, 3.1421388447651997e-10, 4.459142836776105e-11, 5.159205982529289e-12, 6.127902654774931e-13, 6.324630700176418e-14, 5.983701564499864e-15, 5.225677116415448e-16], [7.069851236199015e-08, 8.026501196658693e-08, 4.5562996523955345e-08, 1.7242769515449373e-08, 4.8939894746594524e-09, 1.1112429685552554e-09, 2.102682861561567e-10, 3.410293318701804e-11, 4.839692252533455e-12, 6.105078272765028e-13, 6.35719055240847e-14, 6.864383429777977e-15, 6.494358930228716e-16, 5.671643627554662e-17], [6.9756382880270276e-09, 7.919539916148107e-09, 4.4955823319504776e-09, 1.7012992099146353e-09, 4.8287720943602e-10, 1.0964345273723731e-10, 2.074662476854727e-11, 3.3648476965872907e-12, 4.775198437865661e-13, 6.023721904196348e-14, 6.838815903906534e-15, 6.473843862072827e-16, 6.4078150015289e-17, 5.596063215848564e-18], [6.309124087819846e-10, 7.162837003056945e-10, 4.0660346205118745e-10, 1.538742030859687e-10, 4.3673884850667846e-11, 9.916714717326534e-12, 1.8764308678800906e-12, 3.0433403765820015e-13, 4.318933729715948e-14, 5.448162217545585e-15, 6.185374924837988e-16, 6.383948039913597e-17, 5.53964698911014e-18, 5.061365824066934e-19], [5.267348816677299e-11, 5.980094936624062e-11, 3.3946427980818156e-11, 1.2846618488718227e-11, 3.646236505824685e-12, 8.279246818505085e-13, 1.566590825275773e-13, 2.540817886635484e-14, 3.605782697228282e-15, 4.548550703742972e-16, 5.164033364623393e-17, 5.329817687162984e-18, 5.04251393402094e-19, 4.039036218894129e-20]] |
| Legacy trial inputs | {"lambda_home": 1.085341382791965, "lambda_away": 1.1353140155992878, "rho": -0.09482779564960894, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T12:03:01Z", "over": 2.03, "under": 1.82, "bookmaker": "pinnacle", "event_id": "10a70d197a090f08183739878151539d", "kickoff_utc": "2026-11-02T17:00:00Z", "home_team": "Genclerbirligi SK", "away_team": "Alanyaspor"}} |
| Legacy p home | 0.3439 |
| Legacy p draw | 0.3010 |
| Legacy p away | 0.3551 |
| Legacy p over 1 5 | 0.6640 |
| Legacy p under 3 5 | 0.8146 |
| Legacy p btts yes | 0.4590 |
| Legacy p over 2 5 | 0.3875 |
| Legacy goal margin distribution | {"-1": 0.20375580819080777, "-10": 1.189598918477797e-07, "-11": 1.2163660691787147e-08, "-12": 1.1375342502076807e-09, "-13": 9.074199909537227e-11, "-2": 0.10348781651295125, "-3": 0.035702689774028885, "-4": 0.009566666648353957, "-5": 0.0020888335574199978, "-6": 0.0003842136197453642, "-7": 6.099490590291781e-05, "-8": 8.51231351797676e-06, "-9": 1.0594483839655289e-06, "0": 0.301032468429856, "1": 0.2024151260472776, "10": 7.903750235867817e-08, "11": 7.72586841631354e-09, "12": 6.907133581482253e-10, "13": 5.267348816677299e-11, "2": 0.0985641465404656, "3": 0.03250731063287474, "4": 0.008327048791275805, "5": 0.0017381396520391736, "6": 0.00030563560806559707, "7": 4.638473964795228e-05, "8": 6.188416445671069e-06, "9": 7.363123532967223e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3300 |
| Legacy raw p draw | 0.3149 |
| Legacy raw p away | 0.3551 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0853 |
| Legacy lambda away | 1.1353 |
| Legacy model home team | Genclerbirligi |
| Legacy model away team | Alanyaspor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,419.5227 |
| Elo away rating | 1,462.0223 |
| Elo rating diff | 17.5004 |
| Elo home expectancy | 0.5252 |

</details>


---
