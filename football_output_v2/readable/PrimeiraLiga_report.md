# Primeira Liga — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,611 |
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
| Training sha256 | 84c0a9d8af08458f9d90e4a3ffe4465c5e09f0dc593fdcb0fb4ebd37c58b23a7 |
| Training as of utc | 2026-11-01T07:36:11.587046+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1611, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1310, 'tuning_matches': 198, 'audit_matches': 100, 'audit_matchdays': 40, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8767945865083158, 'audit_candidate_poisson_score': 0.8692694227707133, 'audit_gain': 0.0075251637376024805, 'audit_gain_lower95': -0.0029114938120154417, 'audit_baseline_briers': [0.5874602781324599, 0.1846374686751059, 0.2293671524574864, 0.24667944034048228], 'audit_candidate_briers': [0.5856380790775146, 0.18480680735752542, 0.22778937285479448, 0.24688804666670897], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1456.913 |
| Base scoring parameter | 0.094 |
| Home-advantage parameter | 0.170 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 6, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 25.00 |
| Over 1 5 in window quote fixtures | 6 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 3, 'ANCHORED_ALTERNATE': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 6} |
| Legacy comparison status | {'AVAILABLE': 6} |
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

## 2026-11-01 — Académico de Viseu vs Rio Ave FC

The model's most likely 1X2 outcome is **Académico de Viseu win** at **57.0%**. Expected goals are 2.16 for Académico de Viseu and 0.77 for Rio Ave FC (2.93 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.3%; Under 3.5 goals: 71.6%; Double Chance 1X: 81.0%; Double Chance X2: 43.0%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 46.5%; BTTS No (at least one team does not score): 53.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Académico de Viseu win | 57.0% | 1.75 |
| Draw | 24.0% | 4.17 |
| Rio Ave FC win | 19.0% | 5.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Académico de Viseu expected goals | 2.16 |
| Rio Ave FC expected goals | 0.77 |
| Expected total goals | 2.93 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 28.4% |
| Under 3.5 | 71.6% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.32% |
| 2 | 1-0 | 11.04% |
| 3 | 2-0 | 10.87% |
| 4 | 2-1 | 7.91% |
| 5 | 0-1 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Académico de Viseu win | 57.0% | 51.5% | 1.90 | +8.3% |
| Draw | 24.0% | 26.6% | 3.60 | -13.7% |
| Rio Ave FC win | 19.0% | 21.8% | 4.37 | -16.9% |
| Over 2.5 | 49.3% | 49.3% | 1.97 | -2.8% |
| Under 2.5 | 50.7% | 50.7% | 1.92 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T18:00:00+00:00 |
| Fixture id | ce5c2cbdf5db2a13f40f528d3e5044b9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:11Z |
| Market best draw last update utc | 2026-11-01T07:36:11Z |
| Market best away last update utc | 2026-11-01T07:36:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Academico Viseu |
| Matched away-team name | Rio Ave |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1612 |
| Dc lambda away | 0.7702 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 46.5% |
| P btts no | 53.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.46 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.85 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.53 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.44 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.14010472510689567, "-10": 1.2277346791455156e-09, "-11": 8.030245080843045e-11, "-12": 4.8227660439486405e-12, "-13": 2.677185802655629e-13, "-14": 1.381459415973061e-14, "-15": 6.658384048230307e-16, "-16": 3.001207460751169e-17, "-17": 1.181152230738525e-18, "-2": 0.03963523381415773, "-3": 0.008615803117151344, "-4": 0.0014632984486011693, "-5": 0.00020318573206345102, "-6": 2.3815386175831843e-05, "-7": 2.412383751214816e-06, "-8": 2.1501116668888704e-07, "-9": 1.7101501480795137e-08, "0": 0.2398295792162642, "1": 0.21166935752776153, "10": 2.0661026938122425e-05, "11": 3.791891846577797e-06, "12": 6.390032945936444e-07, "13": 9.953256064184802e-08, "14": 1.4411346354832622e-08, "15": 1.949014307705508e-09, "16": 2.465028612199957e-10, "17": 2.7221470548728706e-11, "2": 0.17357641583548342, "3": 0.10587290244679025, "4": 0.050454711387207675, "5": 0.019658111009858287, "6": 0.006465259549664996, "7": 0.0018376148507184681, "8": 0.00045956704057967485, "9": 0.00010256563233997122} |
| Raw goal margin distribution | {"-1": 0.0906033406029889, "-10": 1.2548829782358495e-09, "-11": 8.678408163364928e-11, "-12": 5.511957643855829e-12, "-13": 3.2363431314224316e-13, "-14": 1.7665856473667176e-14, "-15": 9.0077023324127e-16, "-16": 4.292362044532737e-17, "-17": 1.771303612671943e-18, "-2": 0.026635424075304035, "-3": 0.006059395362120128, "-4": 0.0010813336900577504, "-5": 0.00015812475821916158, "-6": 1.954572061368098e-05, "-7": 2.089903372440174e-06, "-8": 1.9674375242534353e-07, "-9": 1.653601497881189e-08, "0": 0.17773279837048078, "1": 0.24621367705744998, "10": 3.7966524165836016e-05, "11": 7.367454188616675e-06, "12": 1.312994795826539e-06, "13": 2.1631740053031294e-07, "14": 3.313228229417769e-08, "15": 4.740350369326762e-09, "16": 6.338296093890521e-10, "17": 7.339203788557615e-11, "2": 0.20970999890086642, "3": 0.13386547194669732, "4": 0.06703147538444561, "5": 0.027504178628906452, "6": 0.00953960194010153, "7": 0.002862098225696113, "8": 0.0007560300173283588, "9": 0.00017829891765759379} |
| Unadjusted home-win probability | 69.8% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.5% |
| Raw p over 1 5 | 78.6% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 47.1% |
| P home draw | 81.0% |
| P draw away | 43.0% |
| P home away | 76.0% |
| Raw p home draw | 87.5% |
| Raw p draw away | 30.2% |
| Raw p home away | 82.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9445 |
| Totals anchor target over 2 5 | 0.4933 |
| Totals anchor reference over odds | 1.97 |
| Totals anchor reference under odds | 1.92 |
| Totals anchor reference last update utc | 2026-11-01T07:36:11Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5271 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.3, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.90 |
| Reference draw odds | 3.60 |
| Reference away odds | 4.37 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:11Z |
| Market reference home last update utc | 2026-11-01T07:36:11Z |
| Market reference draw last update utc | 2026-11-01T07:36:11Z |
| Market reference away last update utc | 2026-11-01T07:36:11Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:36:11Z |
| Market best over 2 5 last update utc | 2026-11-01T07:36:11Z |
| Market best under 2 5 last update utc | 2026-11-01T07:36:11Z |
| Home probability edge | +5.5% |
| Draw probability edge | -2.7% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1823 |
| Raw ev home | 0.3256 |
| Raw edge prob draw | -0.0887 |
| Raw ev draw | -0.3602 |
| Raw edge prob away | -0.0936 |
| Raw ev away | -0.4557 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06291345552032668, 0.06402278888418908, 0.022513430031545354, 0.005834034527004721, 0.0011338551749308977, 0.0001762934451987397, 2.28419668778357e-05, 2.5367872150077778e-06, 2.465145944989696e-07, 2.129358126390065e-08, 1.6553784313156076e-09, 1.1699119846592846e-10, 7.579150425429847e-12, 4.5323741844515105e-13, 2.516786086382174e-14, 1.3043784891475938e-15, 6.337708035248273e-17, 2.8982236078569243e-18], [0.10709593744400676, 0.10666546253017442, 0.04744919760170823, 0.012295783303528632, 0.0023897077509571593, 0.00037155522305575293, 4.8141620289731775e-05, 5.3465206176816795e-06, 5.195529819177753e-07, 4.487825016548583e-08, 3.4888676751184736e-09, 2.465700910919555e-10, 1.5973781235706566e-11, 9.552410182792527e-13, 5.30436633452342e-14, 2.749101873515516e-15, 1.3357323183764885e-16, 6.1082822328917015e-18], [0.10863477024885806, 0.08445345727999133, 0.04599133464841515, 0.012957267080569948, 0.0025182683208782642, 0.0003915440067110256, 5.073152448989784e-05, 5.6341506583964035e-06, 5.475036915527948e-07, 4.7292592846521155e-08, 3.6765604239547693e-09, 2.5983497313603974e-10, 1.6833132517734653e-11, 1.0066307037639357e-12, 5.58972857547674e-14, 2.8969969889281736e-15, 1.4075915271202103e-16, 6.436893229271901e-18], [0.07631937429838809, 0.05933123439373536, 0.02306226568971435, 0.008372772516739489, 0.0017691634282892203, 0.000275072092793269, 3.5640506233896644e-05, 3.958169672257255e-06, 3.8463872174301566e-07, 3.3224547598588575e-08, 2.582900396288121e-09, 1.8254231610334243e-10, 1.1825809897626797e-11, 7.071900210661805e-13, 3.9269617489957304e-14, 2.0352323388987578e-15, 9.88877726453849e-17, 4.522121808314187e-18], [0.040212587185169776, 0.031261556554876224, 0.012151480253353894, 0.0031488829224578427, 0.0008574031953203949, 0.00014493515723031891, 1.8778940176458254e-05, 2.085554873878224e-06, 2.0266568319087955e-07, 1.75059744564007e-08, 1.3609271345734727e-09, 9.618132838182237e-11, 6.231005113908605e-12, 3.726175776470754e-13, 2.0691114563769792e-14, 1.0723614891031914e-15, 5.210384932537077e-17, 2.3827005809536955e-18], [0.016950371336144816, 0.013177341455574563, 0.005122080348367668, 0.0013273141214199147, 0.00025796590307522704, 5.619282647899015e-05, 7.915680924096513e-06, 8.791010981551524e-07, 8.542744517681268e-08, 7.379101629812357e-09, 5.736567057034158e-10, 4.054226165972292e-11, 2.6264873232806967e-12, 1.5706540537690198e-13, 8.721698845180416e-15, 4.52020790484823e-16, 2.1962764794036576e-17, 1.0043536727452321e-18], [0.005954086944430677, 0.004628750318622007, 0.0017992120128665667, 0.0004662401504238804, 9.061461752954228e-05, 1.4088892005650275e-05, 2.5574913012304368e-06, 3.0879821259129653e-07, 3.000774590340115e-08, 2.592026558262153e-09, 2.0150602215601149e-10, 1.4241112838106754e-11, 9.2259535623926e-13, 5.517171636129011e-14, 3.0636351379872308e-15, 1.5877947650019116e-16, 7.714769696220518e-18, 3.5279516724991567e-19], [0.0017926864578684547, 0.0013936474375486976, 0.0005417158063701317, 0.00014037793058451249, 2.728270501358502e-05, 4.241954499593796e-06, 5.49621025715256e-07, 8.551727894224689e-08, 9.034883133929212e-09, 7.80420399097187e-10, 6.067044711799446e-11, 4.28778591379668e-12, 2.7777965230579797e-13, 1.661137798311097e-14, 9.224146833893465e-16, 4.780612375430342e-17, 2.322801680436475e-18, 1.0622134420155578e-19], [0.00047228217700568173, 0.00036715558534786797, 0.00014271470575790316, 3.6982482000135076e-05, 7.1876123467460566e-06, 1.117540380267776e-06, 1.447973310745812e-07, 1.6080927715277816e-08, 2.1893222368574917e-09, 2.0560128819375968e-10, 1.5983593070069968e-11, 1.129614638975974e-12, 7.318088355219237e-14, 4.376257611861525e-15, 2.4300959761313375e-16, 1.2594494760523368e-17, 6.119407158870233e-19, 2.798394971066478e-20], [0.0001105977400507063, 8.597948422258568e-05, 3.342053691057607e-05, 8.660455824551807e-06, 1.6831752723565178e-06, 2.61702529738987e-07, 3.390824037391089e-08, 3.765787382671224e-09, 3.6594379856399843e-10, 4.4285388384518976e-11, 3.742993823412062e-12, 2.6453004640366564e-13, 1.713729784829253e-14, 1.024819960008279e-15, 5.690731858026642e-17, 2.949344111237949e-18, 1.4330259221554726e-19, 6.5532043053466895e-21], [2.3309526867364258e-05, 1.8120995027652764e-05, 7.043696396342746e-06, 1.8252735330166666e-06, 3.547452164527917e-07, 5.515630016862313e-08, 7.146484545329314e-09, 7.936755500872971e-10, 7.712614019655442e-11, 6.662046671858168e-12, 7.255982828813839e-13, 5.575222623034041e-14, 3.611848709075382e-15, 2.159905652780252e-16, 1.1993759282858924e-17, 6.216023561646411e-19, 3.0202385888534353e-20, 1.3811502093331451e-21], [4.466095226401483e-06, 3.471974778859861e-06, 1.3495691710487637e-06, 3.497216163617688e-07, 6.796902943606264e-08, 1.0567923162522322e-08, 1.3692633357622605e-09, 1.5206789076955904e-10, 1.4777334972202824e-11, 1.2764452495561972e-12, 9.923177828488622e-14, 9.825319110871626e-15, 6.920286443338666e-16, 4.1383698520562166e-17, 2.297999070705362e-18, 1.1909874153103012e-19, 5.786764021863271e-21, 2.6462778038976387e-22], [7.843934139483374e-07, 6.09793121703489e-07, 2.3702879490353358e-07, 6.142263401995774e-08, 1.1937600149441026e-08, 1.8560753650731521e-09, 2.4048773886047374e-10, 2.670813002094605e-11, 2.595386717099599e-12, 2.2418582593104703e-13, 1.7428368495349502e-14, 1.2317218099527284e-15, 1.1179437720250025e-16, 7.268340444793373e-18, 4.036043221078075e-19, 2.0917661565794223e-20, 1.0163463510562186e-21, 4.647735383214104e-23], [1.271679855902862e-07, 9.886131313049546e-08, 3.8427750461403984e-08, 9.958003852492655e-09, 1.9353560812619225e-09, 3.0091196723848806e-10, 3.898852382774276e-11, 4.329994404913319e-12, 4.207711267997466e-13, 3.634561353344498e-14, 2.825534322786624e-15, 1.9969007719081426e-16, 1.2936709370796405e-17, 1.0838496576131717e-18, 6.543342626964401e-20, 3.391227969637955e-21, 1.6477282423277685e-22, 7.535034534073262e-24], [1.9144188501929486e-08, 1.4882830811020176e-08, 5.785010237627133e-09, 1.4991029540191234e-09, 2.913533737760484e-10, 4.5300044634347636e-11, 5.869430471086198e-12, 6.518482518629474e-13, 6.334394407706125e-14, 5.471560105892717e-15, 4.2536304591924494e-16, 3.006184663506859e-17, 1.9475247770860485e-18, 1.1646306680532567e-19, 9.060429008787915e-21, 5.105239907859617e-22, 2.480531552391381e-23, 1.1343430566998435e-24], [2.689880016445303e-09, 2.0911322087465237e-09, 8.128306630263471e-10, 2.1063348170666762e-10, 4.093699859699585e-11, 6.36494384673087e-12, 8.246922417473413e-13, 9.158881747660534e-14, 8.90022626545612e-15, 7.687889296606536e-16, 5.976620825882302e-17, 4.223880292077387e-18, 2.736395945374164e-19, 1.6363800221775192e-20, 9.08666915891131e-22, 6.597843839460058e-23, 3.4853043012333145e-24, 1.5938240054953823e-25], [3.543236421725922e-10, 2.7545376594404405e-10, 1.0706987643770795e-10, 2.7745632498667315e-11, 5.392413919513878e-12, 8.384203281223088e-13, 1.0863233935376529e-13, 1.2064509640648305e-14, 1.1723796478863158e-15, 1.0126849225762514e-16, 7.872685941247614e-18, 5.563893705443741e-19, 3.604509390246268e-20, 2.155516699226707e-21, 1.1969387823690277e-22, 6.2033925290526066e-24, 4.2227741608798955e-25, 2.0994599132920734e-26], [4.3927695050431785e-11, 3.4149708319460674e-11, 1.3274115304312765e-11, 3.439797795906391e-12, 6.685309306194307e-13, 1.0394415758432452e-13, 1.3467823503075137e-14, 1.4957119349355888e-15, 1.4534716153825515e-16, 1.255488179911826e-17, 9.760256051062274e-19, 6.897903410766397e-20, 4.468733396684519e-21, 2.672327470421005e-22, 1.4839190945189738e-23, 7.690729684970152e-25, 3.736768102731455e-26, 2.394064248366753e-27]] |
| Legacy trial inputs | {"lambda_home": 2.1075952236164546, "lambda_away": 0.7774072434316127, "rho": 0.05, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T07:36:11Z", "over": 1.97, "under": 1.92, "bookmaker": "pinnacle", "event_id": "ce5c2cbdf5db2a13f40f528d3e5044b9", "kickoff_utc": "2026-11-01T18:00:00Z", "home_team": "Acad\u00e9mico de Viseu", "away_team": "Rio Ave FC"}} |
| Legacy p home | 0.6007 |
| Legacy p draw | 0.2249 |
| Legacy p away | 0.1744 |
| Legacy p over 1 5 | 0.7660 |
| Legacy p under 3 5 | 0.6859 |
| Legacy p btts yes | 0.4858 |
| Legacy p over 2 5 | 0.5282 |
| Legacy goal margin distribution | {"-1": 0.12635158587540735, "-10": 1.9195099959027094e-09, "-11": 1.3401197469993798e-10, "-12": 8.592377070005764e-12, "-13": 5.092793492525398e-13, "-14": 2.8062244011857595e-14, "-15": 1.4443886142145145e-15, "-16": 6.948536258537443e-17, "-17": 2.8982236078569243e-18, "-2": 0.037622242594438214, "-3": 0.008653100427069833, "-4": 0.0015603103428016524, "-5": 0.00023047194902309928, "-6": 2.8770618143517716e-05, "-7": 3.1063145540909378e-06, "-8": 2.952583385870926e-07, "-9": 2.5054491222459547e-08, "0": 0.22485926648037846, "1": 0.21803316420591096, "10": 2.7028786273425823e-05, "11": 5.115856990407145e-06, "12": 8.892558671562438e-07, "13": 1.4289206122776204e-07, "14": 2.1345830384909622e-08, "15": 2.9786078976936596e-09, "16": 3.8847335049205287e-10, "17": 4.3927695050431785e-11, "2": 0.18153980423093505, "3": 0.11319768631437001, "4": 0.0553369752002565, "5": 0.022159559671107384, "6": 0.0074994751015832984, "7": 0.0021951577184140913, "8": 0.0005656673237152928, "9": 0.00013013170837645577} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6859 |
| Legacy raw p draw | 0.1833 |
| Legacy raw p away | 0.1308 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1076 |
| Legacy lambda away | 0.7774 |
| Legacy model home team | Academico Viseu |
| Legacy model away team | Rio Ave |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 77.4% |
| Market reference home draw last update utc | 2026-11-01T07:36:12Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.4% |
| Market reference draw away last update utc | 2026-11-01T07:36:12Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.2% |
| Market reference home away last update utc | 2026-11-01T07:36:12Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 1.91 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 77.0% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market reference over 1 5 last update utc | 2026-11-01T07:36:12Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.5% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.35 |
| Market reference under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.7% |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-11-01T07:36:12Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,418.3104 |
| Elo away rating | 1,393.4483 |
| Elo rating diff | 84.8621 |
| Elo home expectancy | 0.6198 |

</details>


---

## 2026-11-01 — Arouca vs Nacional

The model's most likely 1X2 outcome is **Arouca win** at **53.8%**. Expected goals are 1.56 for Arouca and 1.07 for Nacional (2.63 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.4%; Double Chance 1X: 78.1%; Double Chance X2: 46.2%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arouca win | 53.8% | 1.86 |
| Draw | 24.3% | 4.12 |
| Nacional win | 21.9% | 4.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arouca expected goals | 1.56 |
| Nacional expected goals | 1.07 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.01% |
| 2 | 1-1 | 11.49% |
| 3 | 2-1 | 10.26% |
| 4 | 2-0 | 9.24% |
| 5 | 0-1 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arouca win | 53.8% | 55.8% | 1.76 | -5.2% |
| Draw | 24.3% | 24.3% | 3.93 | -4.6% |
| Nacional win | 21.9% | 19.9% | 4.78 | +4.7% |
| Over 2.5 | 51.5% | 51.5% | 1.89 | -2.7% |
| Under 2.5 | 48.5% | 48.5% | 2.00 | -2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:30:00+00:00 |
| Fixture id | fd5c6a92f2448c1cfe7a2d9b8075172b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:11Z |
| Market best draw last update utc | 2026-11-01T07:36:11Z |
| Market best away last update utc | 2026-11-01T07:36:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Arouca |
| Matched away-team name | Nacional |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5600 |
| Dc lambda away | 1.0677 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.41 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.00 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.13629547670598474, "-10": 4.972929899012905e-08, "-11": 4.957411960665639e-09, "-12": 4.539307415042694e-10, "-13": 3.841963335696001e-11, "-14": 3.006075287032008e-12, "-15": 1.9880789545598598e-13, "-2": 0.05779580922528831, "-3": 0.01880527171322995, "-4": 0.004814284082940527, "-5": 0.0010116820554413482, "-6": 0.00017990090530396798, "-7": 2.769183888809168e-05, "-8": 3.75475989349069e-06, "-9": 4.54694506368838e-07, "0": 0.24264110501220706, "1": 0.25867481011017796, "10": 2.8972531688424015e-06, "11": 4.220091852309227e-07, "12": 5.646109193691625e-08, "13": 6.982415324395798e-09, "14": 7.982613442661418e-10, "15": 7.713858319975858e-11, "2": 0.16207953614582726, "3": 0.07705560474547672, "4": 0.02882365946518454, "5": 0.008850223441703161, "6": 0.002299515395678792, "7": 0.000517186944254102, "8": 0.00010246385972333999, "9": 1.813013476274275e-05} |
| Raw goal margin distribution | {"-1": 0.16791291028001634, "-10": 4.453792512025296e-08, "-11": 4.269533941439429e-09, "-12": 3.758873062250435e-10, "-13": 3.058673745023969e-11, "-14": 2.3024599835063626e-12, "-15": 1.475042867050486e-13, "-2": 0.06936444242926872, "-3": 0.021872437058297722, "-4": 0.005410372649187551, "-5": 0.0010966599802855082, "-6": 0.00018790210544478207, "-7": 2.78494154829935e-05, "-8": 3.634144404761976e-06, "-9": 4.2339377473063385e-07, "0": 0.24095513210979477, "1": 0.24257030676906133, "10": 1.9754126115779415e-06, "11": 2.7669486272923563e-07, "12": 3.559353064867303e-08, "13": 4.23193851148005e-09, "14": 4.6546932829505297e-10, "15": 4.357088725315863e-11, "2": 0.14808888659978411, "3": 0.0682300245970456, "4": 0.024660297721126764, "5": 0.007303582107206218, "6": 0.0018284721556302626, "7": 0.0003959729994701688, "8": 7.549956567983761e-05, "9": 1.2852260670869577e-05} |
| Unadjusted home-win probability | 49.3% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 26.6% |
| Raw p over 1 5 | 73.2% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 51.2% |
| P home draw | 78.1% |
| P draw away | 46.2% |
| P home away | 75.7% |
| Raw p home draw | 73.4% |
| Raw p draw away | 50.7% |
| Raw p home away | 75.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0410 |
| Totals anchor target over 2 5 | 0.5147 |
| Totals anchor reference over odds | 1.89 |
| Totals anchor reference under odds | 2.00 |
| Totals anchor reference last update utc | 2026-11-01T07:36:11Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4902 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.91, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.16, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.76 |
| Reference draw odds | 3.93 |
| Reference away odds | 4.78 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:11Z |
| Market reference home last update utc | 2026-11-01T07:36:11Z |
| Market reference draw last update utc | 2026-11-01T07:36:11Z |
| Market reference away last update utc | 2026-11-01T07:36:11Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:36:11Z |
| Market best over 2 5 last update utc | 2026-11-01T07:36:11Z |
| Market best under 2 5 last update utc | 2026-11-01T07:36:11Z |
| Home probability edge | -1.9% |
| Draw probability edge | -0.1% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0647 |
| Raw ev home | -0.1320 |
| Raw edge prob draw | -0.0024 |
| Raw ev draw | -0.0530 |
| Raw edge prob away | 0.0671 |
| Raw ev away | 0.2709 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06920718092428066, 0.07470740525589094, 0.03677078815657461, 0.012985889191543002, 0.0034395506572426084, 0.0007288224040256021, 0.00012869464394793257, 1.9478362382233862e-05, 2.5796005627960246e-06, 3.0366865244833983e-07, 3.217288235580751e-08, 3.0987553845439048e-09, 2.735873778666176e-10, 2.229680899070382e-11, 1.687348098434028e-12, 1.191800150734995e-13], [0.13001527094638293, 0.11559353602839155, 0.05608923451205349, 0.019808348439813467, 0.005246603978372271, 0.0011117273462554658, 0.0001963075698596406, 2.9711803590278298e-05, 3.934857754421596e-06, 4.632085172775602e-07, 4.907570476051767e-08, 4.726763449265228e-09, 4.1732329835727956e-10, 3.401099108957882e-11, 2.5738383086469617e-12, 1.8179419451503814e-13], [0.09417235577943496, 0.09977309476079178, 0.04916052761538967, 0.015107578007387821, 0.00400151881000922, 0.0008479004525557941, 0.00014972131241059602, 2.266081858587004e-05, 3.0010664772746155e-06, 3.5328330525485694e-07, 3.7429422255459703e-08, 3.605042982216261e-09, 3.1828722638788327e-10, 2.59397547733779e-11, 1.9630340785066116e-12, 1.386521437297595e-13], [0.047882713540375335, 0.05073045561966275, 0.02687378113197883, 0.008827558589390726, 0.00203460535016091, 0.000431122001190818, 7.612704018827537e-05, 1.1522080720577879e-05, 1.5259170831780795e-06, 1.7962981985642737e-07, 1.9031299461569862e-08, 1.8330139348165017e-09, 1.618357739758249e-10, 1.318928295720171e-11, 9.98120920658259e-13, 7.04988297788854e-14], [0.018259771434620358, 0.019345739952855913, 0.010248147290987891, 0.0036192127449839674, 0.0008916352074791675, 0.00016440566167041744, 2.9030567631885524e-05, 4.39387296276753e-06, 5.818988755413779e-07, 6.850070121140181e-08, 7.257466266590271e-09, 6.990083270448056e-10, 6.171505381063417e-11, 5.029650042326092e-12, 3.806271309157261e-13, 2.6884285016244807e-14], [0.005570599127610997, 0.005901900935081938, 0.0031264531740286313, 0.0011041312007674356, 0.00029244937649359787, 5.7638647708327e-05, 8.856499398323154e-06, 1.340460639437092e-06, 1.7752277897097426e-07, 2.089784901061168e-08, 2.21407126579263e-09, 2.132499407657331e-10, 1.882771786870027e-11, 1.5344203096019134e-12, 1.1611980856475077e-13, 8.201722304912983e-15], [0.0014162086106266386, 0.001500435183336015, 0.0007948354933375356, 0.00028070232267080595, 7.43491526988131e-05, 1.5754188150453353e-05, 2.587485144785274e-06, 3.4078415198959657e-07, 4.5131462954305703e-08, 5.312842126031072e-09, 5.628814278907319e-10, 5.4214348476654817e-11, 4.786554471661908e-12, 3.900943516125095e-13, 2.9521038758400625e-14, 2.0851167862024347e-15], [0.00030860699430827244, 0.0003269608648113098, 0.00017320315010646207, 6.11680365765168e-05, 1.6201475101605985e-05, 3.433005996713405e-06, 6.061963545273084e-07, 8.533916081867466e-08, 9.834628194288883e-09, 1.1577250889777782e-09, 1.2265787985602292e-10, 1.1813886037847681e-11, 1.0430413835280893e-12, 8.500572898967409e-14, 6.432949899984647e-15, 4.543692358196669e-16], [5.884266745286538e-05, 6.234223395136268e-05, 3.302496557586956e-05, 1.1663022878286728e-05, 3.0891652789222745e-06, 6.545776147461886e-07, 1.1558458219828339e-07, 1.749411093415927e-08, 2.154938978657884e-09, 2.2074558797753173e-10, 2.338740523693957e-11, 2.252575541942233e-12, 1.9887863335077617e-13, 1.6208199861897002e-14, 1.2265824776726178e-15, 8.663542413896787e-17], [9.973013723178726e-06, 1.0566141571141209e-05, 5.597272339148755e-06, 1.976720163341897e-06, 5.235705492878511e-07, 1.1094180154185798e-07, 1.95899790806514e-08, 2.965008487437044e-09, 3.926684088116047e-10, 4.299486015711791e-11, 3.9638399051908105e-12, 3.817802245331878e-13, 3.370716226015918e-14, 2.747064445713719e-15, 2.0788867010895336e-16, 1.4683499427408477e-17], [1.5212584052574404e-06, 1.6117326339259631e-06, 8.53793830911429e-07, 3.015239171221414e-07, 7.986413344626702e-08, 1.692278309992753e-08, 2.9882060891980477e-09, 4.522749299632564e-10, 5.989665049747103e-11, 7.0509889806433725e-12, 6.948372992333857e-13, 5.82357942797525e-14, 5.141605669955879e-15, 4.19030294535069e-16, 3.1710814357551743e-17, 2.2397840354538584e-18], [2.109535701956657e-07, 2.2349967116205218e-07, 1.1839596495857691e-07, 4.181245381880637e-08, 1.1074794408923584e-08, 2.3466897538505007e-09, 4.1437584884868984e-10, 6.271716288042312e-11, 8.3058947917959e-12, 9.77763734114127e-13, 1.035914551462648e-13, 9.280349583852335e-15, 7.129887130726607e-16, 5.810711470636381e-17, 4.39735253354637e-18, 3.105918344400457e-19], [2.6815272083817698e-08, 2.8410064296590656e-08, 1.504985201741618e-08, 5.314972032013477e-09, 1.4077677143467021e-09, 2.982984558518805e-10, 5.2673207291700235e-11, 7.972265107453543e-12, 1.055800233838126e-12, 1.2428801531844662e-13, 1.316798313832359e-14, 1.2682842091112174e-15, 1.0415219493067281e-16, 7.386260822281947e-18, 5.589675705708144e-19, 3.9480747065796795e-20], [3.1464108411470238e-09, 3.3335382173661093e-09, 1.7658973363105631e-09, 6.236403482928808e-10, 1.651825714985105e-10, 3.500130419919085e-11, 6.180491100092348e-12, 9.354378834637115e-13, 1.23883930450162e-13, 1.4583523806890728e-14, 1.5450853816794045e-15, 1.488160617102707e-16, 1.3138886764287878e-17, 9.95974696631311e-19, 6.558731227474578e-20, 4.6325336620161185e-21], [3.4281827735664525e-10, 3.6320680511111653e-10, 1.9240395275334857e-10, 6.794894903614194e-11, 1.7997523994614978e-11, 3.8135791594298775e-12, 6.73397537423731e-13, 1.0192095691682463e-13, 1.3497816328910393e-14, 1.588952861427765e-15, 1.6834531015128717e-16, 1.621430528122545e-17, 1.43155193467207e-18, 1.16668540400344e-19, 8.212186742254998e-21, 5.0473930137810255e-22], [3.486175796540468e-11, 3.6935101094388054e-11, 1.956587637098567e-11, 6.909841078389284e-12, 1.830197999694454e-12, 3.8780917593738897e-13, 6.84789100078902e-14, 1.0364510781145795e-14, 1.372615280457829e-15, 1.6158324608785096e-16, 1.711931318935961e-17, 1.648859537623797e-18, 1.4557688535820166e-19, 1.1864216951835723e-20, 8.978443472083961e-22, 5.898517622221761e-23]] |
| Legacy trial inputs | {"lambda_home": 1.525374823983063, "lambda_away": 1.0594732810388068, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T07:36:11Z", "over": 1.89, "under": 2.0, "bookmaker": "pinnacle", "event_id": "fd5c6a92f2448c1cfe7a2d9b8075172b", "kickoff_utc": "2026-11-01T15:30:00Z", "home_team": "Arouca", "away_team": "Nacional"}} |
| Legacy p home | 0.5221 |
| Legacy p draw | 0.2437 |
| Legacy p away | 0.2342 |
| Legacy p over 1 5 | 0.7261 |
| Legacy p under 3 5 | 0.7372 |
| Legacy p btts yes | 0.5043 |
| Legacy p over 2 5 | 0.4795 |
| Legacy goal margin distribution | {"-1": 0.14811243613011046, "-10": 3.723151114327104e-08, "-11": 3.543043442880237e-09, "-12": 3.0963190186448193e-10, "-13": 2.500929944308054e-11, "-14": 1.869142292949066e-12, "-15": 1.191800150734995e-13, "-2": 0.06104219474882187, "-3": 0.01916109749618779, "-4": 0.004713124768250771, "-5": 0.000949387479600576, "-6": 0.00016159461942435074, "-7": 2.3786252974030737e-05, "-8": 3.082134795713389e-06, "-9": 3.565163838200173e-07, "0": 0.24374075203558374, "1": 0.26059018723907124, "10": 1.760449954118372e-06, "11": 2.4119931097560276e-07, "12": 3.0348124095015545e-08, "13": 3.529183522629126e-09, "14": 3.797533784510333e-10, "15": 3.486175796540468e-11, "2": 0.15633299066002695, "3": 0.0706524850933328, "4": 0.025020879058690614, "5": 0.007256441399737752, "6": 0.0017782534256226648, "7": 0.0003768594038925554, "8": 7.030585876151741e-05, "9": 1.1708626358724848e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4864 |
| Legacy raw p draw | 0.2441 |
| Legacy raw p away | 0.2695 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5254 |
| Legacy lambda away | 1.0595 |
| Legacy model home team | Arouca |
| Legacy model away team | Nacional |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 78.1% |
| Market reference home draw last update utc | 2026-11-01T07:36:12Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.9% |
| Market reference draw away last update utc | 2026-11-01T07:36:12Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market reference home away last update utc | 2026-11-01T07:36:12Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.00 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 77.5% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-11-01T07:36:12Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.4% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.13 |
| Market reference under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.1% |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-11-01T07:36:12Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,468.8191 |
| Elo away rating | 1,372.3854 |
| Elo rating diff | 156.4337 |
| Elo home expectancy | 0.7111 |

</details>


---

## 2026-11-01 — Braga vs Famalicão

The model's most likely 1X2 outcome is **Braga win** at **56.1%**. Expected goals are 1.54 for Braga and 0.96 for Famalicão (2.50 combined). The most likely exact score is 1-0 at 13.9%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 47.0%; Under 3.5 goals: 74.3%; Double Chance 1X: 81.1%; Double Chance X2: 43.9%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 88.3%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Braga win | 56.1% | 1.78 |
| Draw | 25.0% | 4.01 |
| Famalicão win | 18.9% | 5.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Braga expected goals | 1.54 |
| Famalicão expected goals | 0.96 |
| Expected total goals | 2.50 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 72.2% |
| Under 1.5 | 27.8% |
| Over 2.5 | 47.0% |
| Under 2.5 | 53.0% |
| Over 3.5 | 25.7% |
| Under 3.5 | 74.3% |
| Over 4.5 | 11.7% |
| Under 4.5 | 88.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.94% |
| 2 | 1-1 | 11.81% |
| 3 | 2-0 | 10.43% |
| 4 | 2-1 | 10.25% |
| 5 | 0-0 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Braga win | 56.1% | 58.2% | 1.68 | -5.7% |
| Draw | 25.0% | 25.2% | 3.75 | -6.4% |
| Famalicão win | 18.9% | 16.7% | 5.57 | +5.4% |
| Over 2.5 | 47.0% | 47.0% | 2.05 | -3.6% |
| Under 2.5 | 53.0% | 53.0% | 1.83 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T20:30:00+00:00 |
| Fixture id | 12fa9f636dbb126cfd4118fa8cdc8fad |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:11Z |
| Market best draw last update utc | 2026-11-01T07:36:11Z |
| Market best away last update utc | 2026-11-01T07:36:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Sp Braga |
| Matched away-team name | Famalicao |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5361 |
| Dc lambda away | 0.9608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.45 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.60 |
| Fair Over 2.5 odds | 2.13 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 3.88 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.56 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.1238630730040622, "-10": 1.6135670281966403e-08, "-11": 1.424842953655759e-09, "-12": 1.1553568835272048e-10, "-13": 8.658328297642225e-12, "-14": 6.005936965777627e-13, "-15": 3.5671621466966155e-14, "-2": 0.04761277536945699, "-3": 0.013925950978772946, "-4": 0.003186575011973244, "-5": 0.0005965841445373906, "-6": 9.432419510361821e-05, "-7": 1.2892275793555626e-05, "-8": 1.550785951054526e-06, "-9": 1.66493433784403e-07, "0": 0.24953859483361066, "1": 0.271914176407528, "10": 2.4528873456060385e-06, "11": 3.4630439101942534e-07, "12": 4.4895991066059214e-08, "13": 5.37930121202787e-09, "14": 5.965859091545934e-10, "15": 5.665203045141757e-11, "2": 0.16951605217105983, "3": 0.07927068329173843, "4": 0.029000954592436554, "5": 0.008680810213678133, "6": 0.002194381180140836, "7": 0.0004795335052030504, "8": 9.222350736186739e-05, "9": 1.583023254732885e-05} |
| Raw goal margin distribution | {"-1": 0.15982764969516516, "-10": 1.7381626753460582e-08, "-11": 1.501565724049365e-09, "-12": 1.1910645820533464e-10, "-13": 8.731272667003902e-12, "-14": 5.926217496820129e-13, "-15": 3.4558822577056786e-14, "-2": 0.060511012412244464, "-3": 0.01738235323656118, "-4": 0.003900454391458471, "-5": 0.0007154743088016822, "-6": 0.00011077602062093085, "-7": 1.4821814974076996e-05, "-8": 1.7448930818881191e-06, "-9": 1.8330943039213297e-07, "0": 0.24461940124414847, "1": 0.2518976151587287, "10": 1.897118653901334e-06, "11": 2.6202867948102154e-07, "12": 3.323075434474158e-08, "13": 3.89477925243813e-09, "14": 4.2265235264344896e-10, "15": 3.940624466313037e-11, "2": 0.15468038134613424, "3": 0.0710411189997436, "4": 0.02548688937000968, "5": 0.007474739831373179, "6": 0.0018503258013899669, "7": 0.00039582592898123296, "8": 7.450271173758586e-05, "9": 1.2513778832109518e-05} |
| Unadjusted home-win probability | 51.3% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 47.8% |
| P home draw | 81.1% |
| P draw away | 43.9% |
| P home away | 75.0% |
| Raw p home draw | 75.8% |
| Raw p draw away | 48.7% |
| Raw p home away | 75.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0227 |
| Totals anchor target over 2 5 | 0.4702 |
| Totals anchor reference over odds | 2.05 |
| Totals anchor reference under odds | 1.83 |
| Totals anchor reference last update utc | 2026-11-01T07:36:11Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4570 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.82, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.15, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.82, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.68 |
| Reference draw odds | 3.75 |
| Reference away odds | 5.57 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:11Z |
| Market reference home last update utc | 2026-11-01T07:36:11Z |
| Market reference draw last update utc | 2026-11-01T07:36:11Z |
| Market reference away last update utc | 2026-11-01T07:36:11Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:36:11Z |
| Market best over 2 5 last update utc | 2026-11-01T07:36:11Z |
| Market best under 2 5 last update utc | 2026-11-01T07:36:11Z |
| Home probability edge | -2.1% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0689 |
| Raw ev home | -0.1383 |
| Raw edge prob draw | -0.0070 |
| Raw ev draw | -0.0827 |
| Raw edge prob away | 0.0760 |
| Raw ev away | 0.3505 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07363145586605527, 0.06828943268067558, 0.029642027939533664, 0.009273897871194562, 0.0021760955905443043, 0.00040849205673440536, 6.390105331316765e-05, 8.568121734310127e-06, 1.00524354398985e-06, 1.048345498004438e-07, 9.839659859357829e-09, 8.395818704299958e-10, 6.566855460055967e-11, 4.741216164350658e-12, 3.178610927252451e-13, 1.9889403769360385e-14], [0.1361878489292054, 0.11536228118978066, 0.04811682677108376, 0.01505398140340635, 0.0035323768934139533, 0.0006630903112077131, 0.00010372825769652276, 1.3908320648112989e-05, 1.631775314684184e-06, 1.7017411503228836e-07, 1.5972362279156382e-08, 1.3628627400942314e-09, 1.0659737830583445e-10, 7.696243905096051e-12, 5.159723608360053e-13, 3.22857463633276e-14], [0.10557959840265867, 0.09909589332403117, 0.046253537799386964, 0.012218290477298152, 0.0028669895227359425, 0.0005381852028317653, 8.418915563117245e-05, 1.1288435741763026e-05, 1.3244007850298388e-06, 1.3811872842563553e-07, 1.2963677628246161e-08, 1.1061427799684876e-09, 8.651782524219245e-11, 6.246516525875421e-12, 4.187795915255414e-13, 2.6204139408213204e-14], [0.05712784178446736, 0.0536195875051098, 0.025163388589623168, 0.007830097401951222, 0.0015512933022149111, 0.0002912054940847392, 4.555373230842301e-05, 6.108035840315579e-06, 7.166172219926131e-07, 7.473437088554815e-08, 7.014488932481452e-09, 5.985204592659199e-10, 4.681374722720772e-11, 3.3799144265857117e-12, 2.2659656419599102e-13, 1.4178742416705701e-14], [0.023183387389657976, 0.02175968196898715, 0.010211703566724763, 0.003194865619919815, 0.0007456103010834217, 0.000118175824055003, 1.8486429561532855e-05, 2.4787381538094885e-06, 2.9081467369685226e-07, 3.032839710799507e-08, 2.8465912448735467e-09, 2.4288912786427966e-10, 1.8997763668799565e-11, 1.3716230658784521e-12, 9.195649205059748e-14, 5.7539593283574364e-15], [0.007526550054339168, 0.0070643401998770365, 0.003315257461871779, 0.0010372218520551828, 0.00024338136240255423, 4.543982063411262e-05, 6.0016698630917795e-06, 8.047291136829252e-07, 9.44137783373322e-08, 9.846196979955989e-09, 9.241536246917052e-10, 7.8854618947566e-11, 6.167675878008761e-12, 4.4530117568693316e-13, 2.9853926374409535e-14, 1.868038616083917e-15], [0.0020362625317408584, 0.0019112144550460085, 0.0008969228270516721, 0.0002806140900139497, 6.584535352935712e-05, 1.236035034788308e-05, 1.923086527107826e-06, 2.1771458776772112e-07, 2.55430759006991e-08, 2.663828958244365e-09, 2.5002416591215334e-10, 2.1333639563728295e-11, 1.668627353520447e-12, 1.2047353606167818e-13, 8.076798966681126e-15, 5.053865335797202e-16], [0.0004721987100790434, 0.00044320071026676385, 0.00020799174731765278, 6.507295069723098e-05, 1.526919565458955e-05, 2.8663010782826823e-06, 4.483799745805556e-07, 5.979535696495345e-08, 5.923306697319416e-09, 6.177281064435312e-10, 5.797930610223123e-11, 4.94716026359894e-12, 3.8694602078708635e-13, 2.7937187587668697e-14, 1.8729677505650545e-15, 1.17196513478859e-16], [9.58128758124704e-05, 8.99289508979807e-05, 4.220318063221542e-05, 1.3203819516705427e-05, 3.0982413034643933e-06, 5.815952974727045e-07, 9.097986484142247e-08, 1.2198962566580385e-08, 1.423482742977102e-09, 1.2534194838998838e-10, 1.176446258045979e-11, 1.0038181846817165e-12, 7.851442675393297e-14, 5.668677672666489e-15, 3.800400607947698e-16, 2.3780105180136487e-17], [1.728106216586319e-05, 1.621982199992159e-05, 7.611876607585812e-06, 2.3814755998100016e-06, 5.58806946519443e-07, 1.0489805681932552e-07, 1.6409367601528785e-08, 2.2002369585975396e-09, 2.581398895187526e-10, 2.6775149553245353e-11, 2.121869398835395e-12, 1.8105128674627355e-13, 1.416106841743741e-14, 1.0224176075387177e-15, 6.854502445962549e-17, 4.2890422862687705e-18], [2.805172022478868e-06, 2.6329047628592107e-06, 1.2356082683586894e-06, 3.865762799001776e-07, 9.070910093939169e-08, 1.7027720366821126e-08, 2.6636730115645908e-09, 3.5715646988840747e-10, 4.190291019230418e-11, 4.369958654897855e-12, 4.0794031124004126e-13, 2.938939744211476e-14, 2.2987147752685785e-15, 1.659653347942303e-16, 1.1126664729793055e-17, 6.962246480680364e-19], [4.1395761862803737e-07, 3.885362384102512e-07, 1.8233800003284082e-07, 5.704683882600238e-08, 1.3385889746461606e-08, 2.51277088079774e-09, 3.93076691138772e-10, 5.270537441834024e-11, 6.183588306809952e-12, 6.44872280127029e-13, 6.052702950751473e-14, 5.136602634996329e-15, 3.392200145481214e-16, 2.449140880334089e-17, 1.6419555014481847e-18, 1.0274147005419838e-19], [5.5996863267719e-08, 5.255806304258974e-08, 2.466522077836879e-08, 7.716838366648435e-09, 1.810735698822585e-09, 3.3990747144955867e-10, 5.317225903553988e-11, 7.129559916204037e-12, 8.364661823785326e-13, 8.723314482070905e-14, 8.187610621992155e-15, 6.986186045676287e-16, 5.434732787574181e-17, 3.3130011582823455e-18, 2.221105581073743e-19, 1.389804122851268e-20], [6.9921287101417905e-09, 6.562737983957499e-09, 3.079858197090107e-09, 9.63574099445519e-10, 2.2610011217386875e-10, 4.2443034327679274e-11, 6.6394304482376626e-12, 8.902427327479301e-13, 1.0444655053104155e-13, 1.0892491842993228e-14, 1.0223577528582027e-15, 8.723401486048083e-17, 6.823076902503411e-18, 4.8995501665802705e-19, 2.773415365684375e-20, 1.7353988673261673e-21], [8.107191745096082e-10, 7.609324343757654e-10, 3.571015635810439e-10, 1.11723915686539e-10, 2.6215721119700543e-11, 4.921159661135776e-12, 7.698247265388285e-13, 1.0322133406379239e-13, 1.2110306422718146e-14, 1.2629561556118772e-15, 1.1853972771532296e-16, 1.0114557590203992e-17, 7.911180562208167e-19, 5.711807940465684e-20, 3.808595544826669e-21, 2.0121499410085217e-22], [8.773406497794098e-11, 8.234626457642149e-11, 3.8644666079218694e-11, 1.2090491487834726e-11, 2.837001828099884e-12, 5.325559762886689e-13, 8.330856689141104e-14, 1.117036270338662e-14, 1.3105480220524103e-15, 1.3667405546164223e-16, 1.2828082153273803e-17, 1.0945729183953899e-18, 8.561287944334529e-20, 6.181180176149842e-21, 4.1439930537140957e-22, 2.5789745389833156e-23]] |
| Legacy trial inputs | {"lambda_home": 1.6232636602744108, "lambda_away": 0.9385894133268058, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T07:36:11Z", "over": 2.05, "under": 1.83, "bookmaker": "pinnacle", "event_id": "12fa9f636dbb126cfd4118fa8cdc8fad", "kickoff_utc": "2026-11-01T20:30:00Z", "home_team": "Braga", "away_team": "Famalic\u00e3o"}} |
| Legacy p home | 0.5610 |
| Legacy p draw | 0.2439 |
| Legacy p away | 0.1951 |
| Legacy p over 1 5 | 0.7219 |
| Legacy p under 3 5 | 0.7423 |
| Legacy p btts yes | 0.4843 |
| Legacy p over 2 5 | 0.4713 |
| Legacy goal margin distribution | {"-1": 0.1303002444905785, "-10": 1.1292514163651506e-08, "-11": 9.5265811578523e-10, "-12": 7.379775683959797e-11, "-13": 5.283392664594877e-12, "-14": 3.5014683908857267e-13, "-15": 1.9889403769360385e-14, "-2": 0.047873521691187755, "-3": 0.013392589574507261, "-4": 0.0029297840091450566, "-5": 0.0005242566416717398, "-6": 7.92114362600087e-05, "-7": 1.0345279445526454e-05, "-8": 1.1889993083684902e-06, "-9": 1.2196127058917464e-07, "0": 0.24387040671144677, "1": 0.2638981990170382, "10": 3.2193638040440292e-06, "11": 4.697101007852318e-07, "12": 6.292879330674537e-08, "13": 7.791705810596776e-09, "14": 8.930654390860297e-10, "15": 8.773406497794098e-11, "2": 0.1705169162038139, "3": 0.08249926286908824, "4": 0.031212929223870065, "5": 0.009659536311198392, "6": 0.0025241411741862164, "7": 0.0005701398464056904, "8": 0.00011332720687930491, "9": 2.0104252871702293e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5402 |
| Legacy raw p draw | 0.2361 |
| Legacy raw p away | 0.2237 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6233 |
| Legacy lambda away | 0.9386 |
| Legacy model home team | Sp Braga |
| Legacy model away team | Famalicao |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 80.9% |
| Market reference home draw last update utc | 2026-11-01T07:36:12Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.2% |
| Market reference draw away last update utc | 2026-11-01T07:36:12Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.9% |
| Market reference home away last update utc | 2026-11-01T07:36:12Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.17 |
| Market reference dc draw away odds | 2.05 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 73.9% |
| Market over 1 5 odds | 1.33 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.20 |
| Market reference over 1 5 last update utc | 2026-11-01T07:36:12Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.3% |
| Market under 3 5 odds | 1.30 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.65 |
| Market reference under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 46.9% |
| Market reference btts yes odds | 1.95 |
| Market reference btts yes opposite odds | 1.75 |
| Market reference btts yes last update utc | 2026-11-01T07:36:12Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,518.8201 |
| Elo away rating | 1,511.6518 |
| Elo rating diff | 67.1683 |
| Elo home expectancy | 0.5955 |

</details>


---

## 2026-11-01 — CS Maritimo vs Santa Clara

The model's most likely 1X2 outcome is **Santa Clara win** at **43.1%**. Expected goals are 0.98 for CS Maritimo and 1.33 for Santa Clara (2.32 combined). The most likely exact score is 0-1 at 14.1%. Goal-market probabilities: at least one goal: 88.6%; Over 2.5 goals: 37.1%; Under 3.5 goals: 81.9%; Double Chance 1X: 56.9%; Double Chance X2: 73.0%; Double Chance 12 (either team wins): 70.1%; Under 4.5 goals: 92.9%; BTTS Yes (both teams score): 43.7%; BTTS No (at least one team does not score): 56.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CS Maritimo win | 27.0% | 3.71 |
| Draw | 29.9% | 3.34 |
| Santa Clara win | 43.1% | 2.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CS Maritimo expected goals | 0.98 |
| Santa Clara expected goals | 1.33 |
| Expected total goals | 2.32 |
| Over 0.5 | 88.6% |
| Under 0.5 | 11.4% |
| Over 1.5 | 63.9% |
| Under 1.5 | 36.1% |
| Over 2.5 | 37.1% |
| Under 2.5 | 62.9% |
| Over 3.5 | 18.1% |
| Under 3.5 | 81.9% |
| Over 4.5 | 7.1% |
| Under 4.5 | 92.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.12% |
| 2 | 1-1 | 13.67% |
| 3 | 0-0 | 11.40% |
| 4 | 1-0 | 10.56% |
| 5 | 0-2 | 8.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CS Maritimo win | 27.0% | 26.4% | 3.65 | -1.5% |
| Draw | 29.9% | 31.5% | 3.08 | -7.8% |
| Santa Clara win | 43.1% | 42.1% | 2.32 | -0.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T18:00:00+00:00 |
| Fixture id | 6bf5102547eb3f3eb74023133e27d2d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:11Z |
| Market best draw last update utc | 2026-11-01T07:36:11Z |
| Market best away last update utc | 2026-11-01T07:36:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Maritimo |
| Matched away-team name | Santa Clara |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9840 |
| Dc lambda away | 1.3333 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.7% |
| P btts no | 56.3% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.77 |
| Fair Over 1.5 odds | 1.56 |
| Fair Under 1.5 odds | 2.77 |
| Fair Over 2.5 odds | 2.70 |
| Fair Under 2.5 odds | 1.59 |
| Fair Over 3.5 odds | 5.53 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 14.08 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.2387941823802212, "-10": 3.5162375345622177e-07, "-11": 4.0185363345258595e-08, "-12": 4.215196880370831e-09, "-13": 4.073572169096869e-10, "-14": 3.402029850802214e-11, "-2": 0.12484449224963273, "-3": 0.04826543616499145, "-4": 0.014476956936413968, "-5": 0.0035362235394342054, "-6": 0.0007273927633009235, "-7": 0.0001291061772627067, "-8": 2.0141313722050033e-05, "-9": 2.801924921492862e-06, "0": 0.29946857354603246, "1": 0.1773882721589823, "10": 1.6810424612078097e-08, "11": 1.4178858846740527e-09, "12": 1.097650666721434e-10, "13": 7.828789177104874e-12, "14": 4.825365390299386e-13, "2": 0.06780889244282644, "3": 0.01934756883430961, "4": 0.004282923819023797, "5": 0.0007721037817626309, "6": 0.0001172135573475561, "7": 1.535425661295238e-05, "8": 1.7678380139516851e-06, "9": 1.8150310963119877e-07} |
| Raw goal margin distribution | {"-1": 0.2450747318260218, "-10": 5.429813555757375e-07, "-11": 6.517390641066762e-08, "-12": 7.180755688752136e-09, "-13": 7.285426661435794e-10, "-14": 6.344012611339986e-11, "-2": 0.1327528555614053, "-3": 0.0534986703844619, "-4": 0.016777230145174234, "-5": 0.004291828631190639, "-6": 0.0009254876879509992, "-7": 0.00017231898302116786, "-8": 2.8213285592688905e-05, "-9": 4.120419547977029e-06, "0": 0.2640037257581773, "1": 0.18256541221854422, "10": 2.6032383607327392e-08, "11": 2.306086918984394e-09, "12": 1.875188679096859e-10, "13": 1.4041151134850384e-11, "14": 9.023700296630826e-13, "2": 0.07230855375072019, "3": 0.02150610163521566, "4": 0.004977506883013494, "5": 0.0009397382010426141, "6": 0.00014955745158909403, "7": 2.0551495741805866e-05, "8": 2.4833439768323084e-06, "9": 2.6766867861423974e-07} |
| Unadjusted home-win probability | 28.2% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 66.7% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 45.5% |
| P home draw | 56.9% |
| P draw away | 73.0% |
| P home away | 70.1% |
| Raw p home draw | 54.6% |
| Raw p draw away | 71.8% |
| Raw p home away | 73.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9513 |
| Totals anchor target over 2 5 | 0.3705 |
| Totals anchor reference over odds | 2.56 |
| Totals anchor reference under odds | 1.55 |
| Totals anchor reference last update utc | 2026-11-01T07:36:11Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3978 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.8, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.55, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.8, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.65 |
| Reference draw odds | 3.08 |
| Reference away odds | 2.32 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:11Z |
| Market reference home last update utc | 2026-11-01T07:36:11Z |
| Market reference draw last update utc | 2026-11-01T07:36:11Z |
| Market reference away last update utc | 2026-11-01T07:36:11Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.60 |
| Reference Under 2.5 odds | 1.60 |
| Market reference over 2 5 last update utc | 2026-11-01T07:35:58Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:35:58Z |
| Home probability edge | +0.5% |
| Draw probability edge | -1.5% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | 0.0182 |
| Raw ev home | 0.0310 |
| Raw edge prob draw | -0.0507 |
| Raw ev draw | -0.1869 |
| Raw edge prob away | 0.0325 |
| Raw ev away | 0.0522 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.10479143552820355, 0.135647042302499, 0.08024598366501373, 0.03326891790406069, 0.010344638273058737, 0.0025732496935193753, 0.0005334175549378303, 9.477763977336565e-05, 1.4735080994474776e-05, 2.0363228892189277e-06, 2.532697186829575e-07, 2.863697944839494e-08, 2.9681277329282084e-09, 2.839722218883992e-10, 2.522809448492715e-11], [0.10427012899282302, 0.13547024032565966, 0.08220413334253447, 0.03408074072546506, 0.010597066484083215, 0.002636041721573761, 0.0005464339249227224, 9.70903886024302e-05, 1.5094644087601297e-05, 2.0860129151459272e-06, 2.5944996590922495e-07, 2.9335774447358743e-08, 3.0405555118353257e-09, 2.909016666944705e-10, 2.5843706417436375e-11], [0.05028041714816838, 0.06253677731463769, 0.04542210737885557, 0.017456186758851636, 0.005427827203999235, 0.0013501829953341906, 0.0002798839591445879, 4.97297863795293e-05, 7.731490590950714e-06, 1.068457734574868e-06, 1.3289051127063843e-07, 1.502581066514228e-08, 1.5573753309180428e-09, 1.490001013530082e-10, 1.3237170207002472e-11], [0.01716911728575537, 0.021354263255695626, 0.013279790440126003, 0.006430307553855092, 0.0018534253921891194, 0.0004610433150507318, 9.557121427203681e-05, 1.698109489485016e-05, 2.640051063191755e-06, 3.648433565244724e-07, 4.537776143435799e-08, 5.130822699086924e-09, 5.31792718339609e-10, 5.087865934327129e-11, 4.5200605067734835e-12], [0.00439701883593206, 0.005468836644307107, 0.0034009604413914726, 0.0014099929809813184, 0.0005120575070837189, 0.00011807340509814906, 2.4475831944819552e-05, 4.348866215117179e-06, 6.761182919000539e-07, 9.343655146055471e-08, 1.1621265580429352e-08, 1.3140060537899938e-09, 1.3619235983033235e-10, 1.3030048065717554e-11, 1.1575895753432273e-12], [0.0009008628374660555, 0.0011204572645376236, 0.0006967900269847899, 0.00028887988090339826, 8.982431833002885e-05, 2.6096706658813322e-05, 5.014617457393388e-06, 8.909973107905199e-07, 1.3852336449558855e-07, 1.9143315053358353e-08, 2.380969169424307e-09, 2.692140439316322e-10, 2.7903140808798425e-11, 2.6696010435245665e-12, 2.3716737825703935e-13], [0.00015380759142524854, 0.0001912997472936029, 0.00011896549765679809, 4.9321513603494096e-05, 1.533603283338582e-05, 3.8148691860101605e-06, 9.236133000129409e-07, 1.5212321414493605e-07, 2.3650598252135224e-08, 3.2684078616604007e-09, 4.0651153313972295e-10, 4.596389367269868e-11, 4.764004799079704e-12, 4.557907036389603e-13, 4.049244979064928e-14], [2.25086828152865e-05, 2.799540188215525e-05, 1.7409782104422223e-05, 7.217864185919798e-06, 2.24432289390129e-06, 5.582798592320791e-07, 1.1572770346873047e-07, 2.401602201998363e-08, 3.4611023390727976e-09, 4.783090040445569e-10, 5.949016609264587e-11, 6.72649960933264e-12, 6.971793261914703e-13, 6.670183365657647e-14, 5.925791440499868e-15], [2.8822420123178958e-06, 3.5848176509765395e-06, 2.2293266033580337e-06, 9.242491693798366e-07, 2.8738606284042746e-07, 7.148786439945832e-08, 1.481895905077628e-08, 2.633032883393621e-09, 4.781102716559756e-10, 6.12475779964739e-11, 7.617729453077771e-12, 8.613298223160231e-13, 8.927397309556696e-14, 8.541185143586441e-15, 7.587989571048165e-16], [3.2806378017636247e-07, 4.0803264430821845e-07, 2.5374736389926086e-07, 1.0520028333351825e-07, 3.2710979072021674e-08, 8.136922205488557e-09, 1.6867298803151936e-09, 2.996981923666117e-10, 4.659408220102891e-11, 7.520557398679825e-12, 8.670684522871603e-13, 9.80386505643868e-14, 1.0161380258815103e-14, 9.72178419930028e-16, 8.636833867448031e-17], [3.360691401460307e-08, 4.179893917288172e-08, 2.5993926654781274e-08, 1.0776736384616477e-08, 3.3509187159153515e-09, 8.335478081620645e-10, 1.7278891934714938e-10, 3.070113797927391e-11, 4.773106355348124e-12, 6.596221444399442e-13, 9.58201850520019e-14, 1.0043097405796635e-14, 1.0409336637043645e-15, 9.95901362469126e-17, 8.84758850811569e-18], [3.1297258693742314e-09, 3.892628200998269e-09, 2.420747845599122e-09, 1.0036098713409072e-09, 3.120624817504364e-10, 7.762617351392104e-11, 1.609138972376361e-11, 2.8591183859133685e-12, 4.4450717584829147e-13, 6.142892169655173e-14, 7.640284259168102e-15, 1.0089708282706902e-15, 9.693948733830284e-17, 9.274574440575811e-18, 8.239532681696269e-19], [2.6717474501654176e-10, 3.323012910564771e-10, 2.0665154565968567e-10, 8.567498326145858e-11, 2.6639781715953423e-11, 6.6266995835448236e-12, 1.3736707704908173e-12, 2.4407384467868567e-13, 3.794616408019015e-14, 5.243991702761766e-15, 6.522267712875692e-16, 7.374669479708288e-17, 8.927360916642388e-18, 7.9174092707142585e-19, 7.033827035234297e-20], [2.105340772882043e-11, 2.6185388776144576e-11, 1.6284171051777162e-11, 6.7512008092369524e-12, 2.099218570370557e-12, 5.221848652653747e-13, 1.0824545117284763e-13, 1.9233053512011436e-14, 2.9901631012149037e-15, 4.132272885221965e-16, 5.1395561907317004e-17, 5.811249989664023e-18, 6.023167453251534e-19, 6.730438547100485e-20, 5.542665660918637e-21], [1.5405106872739477e-12, 1.916025746504368e-12, 1.1915381995057795e-12, 4.939958952262572e-13, 1.5360309761886543e-13, 3.8209081210773016e-14, 7.920488527483849e-15, 1.4073125294394028e-15, 2.1879489883283864e-16, 3.02364853443773e-17, 3.760693442909331e-18, 4.252182274151786e-19, 4.4072455882155005e-20, 4.216581746833035e-21, 4.375163294775158e-22]] |
| Legacy trial inputs | {"lambda_home": 1.024401840292656, "lambda_away": 1.2437601130148102, "rho": 0.05, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2873 |
| Legacy p draw | 0.2927 |
| Legacy p away | 0.4201 |
| Legacy p over 1 5 | 0.6553 |
| Legacy p under 3 5 | 0.8059 |
| Legacy p btts yes | 0.4553 |
| Legacy p over 2 5 | 0.3893 |
| Legacy goal margin distribution | {"-1": 0.23728403146507104, "-10": 2.8421490471015293e-07, "-11": 3.183105512209004e-08, "-12": 3.2722665698296816e-09, "-13": 3.0981592830583555e-10, "-14": 2.522809448492715e-11, "-2": 0.12024098587540843, "-3": 0.04531622931609936, "-4": 0.013278240723607176, "-5": 0.0031721493200751495, "-6": 0.0006386161727988255, "-7": 0.00011098746172788727, "-8": 1.695925414604375e-05, "-9": 2.311343725727079e-06, "0": 0.29265319311536603, "1": 0.18159044732408183, "10": 3.771309856516788e-08, "11": 3.4788053273777117e-09, "12": 2.9455167199219215e-10, "13": 2.2969433475324797e-11, "14": 1.5405106872739477e-12, "2": 0.07534043016234393, "3": 0.023386382999289877, "4": 0.005643955160983847, "5": 0.0011105301768988246, "6": 0.00018414095013210739, "7": 2.6358343365381013e-05, "8": 3.317299363039306e-06, "9": 3.723712796057564e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3103 |
| Legacy raw p draw | 0.2706 |
| Legacy raw p away | 0.4191 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0244 |
| Legacy lambda away | 1.2438 |
| Legacy model home team | Maritimo |
| Legacy model away team | Santa Clara |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 56.8% |
| Market reference home draw last update utc | 2026-11-01T07:36:12Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.5% |
| Market reference draw away last update utc | 2026-11-01T07:36:12Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.7% |
| Market reference home away last update utc | 2026-11-01T07:36:12Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.67 |
| Market reference dc draw away odds | 1.29 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 65.5% |
| Market over 1 5 odds | 1.50 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.50 |
| Market reference over 1 5 last update utc | 2026-11-01T07:36:12Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 82.8% |
| Market under 3 5 odds | 1.19 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference under 3 5 odds | 1.19 |
| Market reference under 3 5 opposite odds | 5.05 |
| Market reference under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.9% |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.73 |
| Market reference btts yes last update utc | 2026-11-01T07:36:12Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,412.3721 |
| Elo away rating | 1,471.5616 |
| Elo rating diff | 0.8105 |
| Elo home expectancy | 0.5012 |

</details>


---

## 2026-11-02 — Benfica vs Alverca

The model's most likely 1X2 outcome is **Benfica win** at **83.4%**. Expected goals are 2.78 for Benfica and 0.67 for Alverca (3.45 combined). The most likely exact score is 2-0 at 11.5%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.5%; Under 3.5 goals: 50.6%; Double Chance 1X: 94.3%; Double Chance X2: 16.6%; Double Chance 12 (either team wins): 89.1%; Under 4.5 goals: 69.9%; BTTS Yes (both teams score): 47.5%; BTTS No (at least one team does not score): 52.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Benfica win | 83.4% | 1.20 |
| Draw | 10.9% | 9.20 |
| Alverca win | 5.7% | 17.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Benfica expected goals | 2.78 |
| Alverca expected goals | 0.67 |
| Expected total goals | 3.45 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.6% |
| Under 1.5 | 12.4% |
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 49.4% |
| Under 3.5 | 50.6% |
| Over 4.5 | 30.1% |
| Under 4.5 | 69.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.48% |
| 2 | 3-0 | 11.17% |
| 3 | 4-0 | 8.15% |
| 4 | 1-0 | 8.14% |
| 5 | 2-1 | 8.13% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:15:00+00:00 |
| Fixture id | cdf1a22ce6d16f0903216518d909e02a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Benfica |
| Matched away-team name | Alverca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7757 |
| Dc lambda away | 0.6735 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 47.5% |
| P btts no | 52.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.18 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.09 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.32 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.04320343849214367, "-10": 2.4726709351563587e-10, "-11": 1.5679880810983046e-11, "-12": 9.135637969760559e-13, "-13": 4.9223127527093105e-14, "-14": 2.4663491091718247e-15, "-15": 1.1547772209455475e-16, "-16": 5.073922260094106e-18, "-17": 2.0999949761040287e-19, "-18": 8.213025357179762e-21, "-19": 3.031433373844141e-22, "-2": 0.011128887806358213, "-20": 9.730232557303895e-24, "-3": 0.002270922142481938, "-4": 0.0003665784453382408, "-5": 4.872536641716904e-05, "-6": 5.491264345266949e-06, "-7": 5.363928152171033e-07, "-8": 4.619518916529749e-08, "-9": 3.555489550526002e-09, "0": 0.10874422140335224, "1": 0.19606804829797228, "10": 0.00040191792938563346, "11": 0.00010503671465058689, "12": 2.5221131649498596e-05, "13": 5.600440769623615e-06, "14": 1.1564713298749168e-06, "15": 2.231546004352692e-07, "16": 4.040906120153756e-08, "17": 6.892559497003653e-09, "18": 1.1109454830502077e-09, "19": 1.6899152586953272e-10, "2": 0.21737234623744217, "20": 2.2354627419096687e-11, "3": 0.18280248266887136, "4": 0.12161134332697639, "5": 0.06661769323865707, "6": 0.030940985579828013, "7": 0.012455812455335407, "8": 0.00442092527529915, "9": 0.001402307145477026} |
| Raw goal margin distribution | {"-1": 0.051668142044577946, "-10": 1.9908150770368957e-10, "-11": 1.2021255158055095e-11, "-12": 6.667990137704787e-13, "-13": 3.419795439064107e-14, "-14": 1.6307993709900087e-15, "-15": 7.266249662821587e-17, "-16": 3.0379452630944656e-18, "-17": 1.1961515121912662e-19, "-18": 4.433025156766942e-21, "-19": 1.4306601144851334e-22, "-2": 0.01288708515772338, "-3": 0.002530890376859305, "-4": 0.00039160725151332236, "-5": 4.977704479084692e-05, "-6": 5.356691153937411e-06, "-7": 4.99152620927679e-07, "-8": 4.0980665898846876e-08, "-9": 3.0053949805080195e-09, "0": 0.11947612870296855, "1": 0.2036674532765431, "10": 0.0002813870331873837, "11": 7.002454421523168e-05, "12": 1.600747160291254e-05, "13": 3.3834147318262733e-06, "14": 6.649407645063721e-07, "15": 1.2210123449691875e-07, "16": 2.103860789595968e-08, "17": 3.4138981840133907e-09, "18": 5.214250395325476e-10, "19": 6.93514382890906e-11, "2": 0.21888163806182645, "3": 0.17715576198848712, "4": 0.11296918325983055, "5": 0.059178736588040765, "6": 0.02624584157304144, "7": 0.010079165291374165, "8": 0.003410338897441164, "9": 0.0010307358943218029} |
| Unadjusted home-win probability | 81.3% |
| Unadjusted draw probability | 11.9% |
| Unadjusted away-win probability | 6.8% |
| Raw p over 1 5 | 85.6% |
| Raw p under 3 5 | 54.8% |
| Raw p btts yes | 45.7% |
| P home draw | 94.3% |
| P draw away | 16.6% |
| P home away | 89.1% |
| Raw p home draw | 93.2% |
| Raw p draw away | 18.7% |
| Raw p home away | 88.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0517 |
| Totals anchor target over 2 5 | 0.7050 |
| Totals anchor reference over odds | 1.34 |
| Totals anchor reference under odds | 2.78 |
| Totals anchor reference last update utc | 2026-11-01T07:36:11Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6767 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 3.46, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.18 |
| Reference draw odds | 9.00 |
| Reference away odds | 17.50 |
| Market reference 1x2 last update utc | 2026-11-01T07:35:58Z |
| Market reference home last update utc | 2026-11-01T07:35:58Z |
| Market reference draw last update utc | 2026-11-01T07:35:58Z |
| Market reference away last update utc | 2026-11-01T07:35:58Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.05 |
| Market reference over 2 5 last update utc | 2026-11-01T07:36:13Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:36:13Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0303 |
| Raw edge prob draw | 0.0153 |
| Raw edge prob away | 0.0150 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.027306261680610802, 0.021595190206592074, 0.006230426822891919, 0.001365479169563899, 0.000224446905747559, 2.9514277257407123e-05, 3.2342190948819048e-06, 3.037805271318381e-07, 2.49665468580086e-08, 1.8239146177108892e-09, 1.1992039173287244e-10, 7.167849661841589e-12, 3.9273189791142365e-13, 1.9862840654005102e-14, 9.328286098115542e-16, 4.088830738821509e-17, 1.6802259380988792e-18, 6.498412833324555e-20, 2.3736863223475412e-21, 8.214067376746121e-23], [0.0931948707946713, 0.05237328210902597, 0.01737747779817075, 0.0038085005453843707, 0.0006260118660194701, 8.231919134098548e-05, 9.020661362914966e-06, 8.472837440854249e-07, 6.963497462612928e-08, 5.087137153842451e-09, 3.34473705273158e-10, 1.999207307942708e-11, 1.0953807869974262e-12, 5.5400068452030144e-14, 2.6017813734588778e-15, 1.1404285357029295e-16, 4.686370575438568e-18, 1.8124925939187824e-19, 6.620522564338531e-21, 2.291011154286058e-22], [0.12582977551115804, 0.08273170149760468, 0.02527456394905691, 0.0053112038350703996, 0.0008730146113886473, 0.00011479951218072112, 1.2579903994933002e-05, 1.1815927600254934e-06, 9.711053993088018e-08, 7.094346459727312e-09, 4.664455223276634e-10, 2.7880257320468486e-11, 1.5275803606786687e-12, 7.725902951023183e-14, 3.6283547931945725e-15, 1.5904024012258127e-16, 6.535451177234468e-18, 2.527639815497672e-19, 9.232752999471115e-21, 3.194965337100963e-22], [0.11698525063376121, 0.07691652310224907, 0.02528588644332678, 0.005149898143449941, 0.0008116507615574671, 0.00010673030012601653, 1.1695667546235034e-05, 1.0985390748500736e-06, 9.02846787006029e-08, 6.5956876685386855e-09, 4.336592520715304e-10, 2.592056512156408e-11, 1.420207344654753e-12, 7.182852305235305e-14, 3.37331917780014e-15, 1.4786136489565535e-16, 6.076076913176142e-18, 2.3499730181243784e-19, 8.583786463061443e-21, 2.9703924942136746e-22], [0.08157180291935559, 0.05363256846267784, 0.017631413656184442, 0.0038641538953681984, 0.0005902501880751752, 7.442120233309601e-05, 8.155187794387289e-06, 7.659924001310008e-07, 6.295395340613578e-08, 4.599059554097255e-09, 3.023831367842981e-10, 1.807396418095418e-11, 9.902861514181818e-13, 5.008479355023932e-14, 2.3521574357869002e-15, 1.0310118627189143e-16, 4.236743912581857e-18, 1.638595761959449e-19, 5.9853266447984916e-21, 2.0712035903541898e-22], [0.04550289200025973, 0.029917653933264867, 0.009835265161448305, 0.0021555264329164484, 0.00035430876494416575, 4.329658099707748e-05, 4.549177732613155e-06, 4.272906593794337e-07, 3.511736703503781e-08, 2.5654760922685675e-09, 1.6867724781562767e-10, 1.0082131456081561e-11, 5.524075990067667e-13, 2.7938611998375688e-14, 1.3120951350558271e-15, 5.751254693569299e-17, 2.3633669207674917e-18, 9.140517105186123e-20, 3.3387722492022888e-21, 1.1553717082312275e-22], [0.02115225590917198, 0.013907376968366142, 0.0045719741423980425, 0.001002007668606494, 0.00016470227138351727, 2.1657988495529557e-05, 2.2055077047422117e-06, 1.986282844338999e-07, 1.6324490636269887e-08, 1.1925748990243848e-09, 7.841049557532762e-11, 4.686731222879914e-12, 2.567895442842554e-13, 1.2987409036184601e-14, 6.099342449205647e-16, 2.6735006442339952e-17, 1.0986233999162166e-18, 4.249016896551479e-20, 1.5520456378281496e-21, 5.370805451790757e-23], [0.008428059537299871, 0.005541356988132768, 0.001821690813527729, 0.0003992472634649188, 6.56251775276079e-05, 8.629567327583652e-06, 9.456410261388183e-07, 8.254104759412088e-08, 6.504449435056153e-09, 4.751782644284562e-10, 3.1242451296719334e-11, 1.8674154639281874e-12, 1.0231710400427578e-13, 5.1747982372304316e-15, 2.430266611798851e-16, 1.0652491488079637e-17, 4.377435420280494e-19, 1.6930093666085392e-20, 6.184084145157382e-22, 2.1399830025373017e-23], [0.002938370469117983, 0.0019319464534758618, 0.0006351168340284756, 0.00013919412453715607, 2.2879653712024693e-05, 3.008624427060096e-06, 3.296896104370585e-07, 3.096675911874703e-08, 2.3650889546387294e-09, 1.6566681495117128e-10, 1.0892411932646105e-11, 6.510583401192709e-13, 3.5671978295985816e-14, 1.804148897694324e-15, 8.472915518203562e-17, 3.713899536729174e-18, 1.5261552095708243e-19, 5.9025315433123204e-21, 2.1560277487660856e-22, 7.46086668140051e-24], [0.0009106111924839504, 0.0005987169018693794, 0.00019682490811817355, 4.3136741627268855e-05, 7.090483983995586e-06, 9.323831375435493e-07, 1.0217195294634729e-07, 9.596705978654196e-09, 7.88716155577077e-10, 5.354512518830202e-11, 3.3755962099600794e-12, 2.0176523610740994e-13, 1.1054869709509376e-14, 5.591119963988678e-16, 2.6257858853867064e-17, 1.150950338444458e-18, 4.7296078895049643e-20, 1.8292149828687746e-21, 6.681604719236446e-23, 2.3121484431992835e-24], [0.00025398140817599183, 0.00016698999868512183, 5.4897049081510164e-05, 1.203140316421135e-05, 1.9776290054069985e-06, 2.60053889286051e-07, 2.8497098102450384e-08, 2.6766471996252253e-09, 2.199832832036614e-10, 1.6070733696938478e-11, 9.819229610388095e-13, 5.627497137141178e-14, 3.083348194265464e-15, 1.5594367096029002e-16, 7.323661319382623e-18, 3.210151490685856e-19, 1.3191496895838161e-20, 5.101920567639218e-22, 1.8635872142510863e-23, 6.448885346047749e-25], [6.439886072871365e-05, 4.2341546751955424e-05, 1.3919552000309418e-05, 3.0506510783898067e-06, 5.014424315815273e-07, 6.593858313632178e-08, 7.225649566445968e-09, 6.786836543134821e-10, 5.577838519527075e-11, 4.074853150039413e-12, 2.679171389173622e-13, 1.488159642014349e-14, 7.818056934428871e-16, 3.954066882225186e-17, 1.8569683848842096e-18, 8.139576052098312e-20, 3.344801406919054e-21, 1.2936296181832703e-22, 4.725262936695207e-24, 1.63516247995521e-25], [1.4968072604979754e-05, 9.841344067564114e-06, 3.2352880565249754e-06, 7.090555068381643e-07, 1.1654906062310736e-07, 1.5325946587963384e-08, 1.6794403830265416e-09, 1.577448125421224e-10, 1.29644361708263e-11, 9.471083356793836e-13, 6.227133744379249e-14, 3.722065768707442e-15, 1.8951540056769264e-16, 9.190342734076302e-18, 4.3161070390963795e-19, 1.8918621221390603e-20, 7.774241615687487e-22, 3.006752267014243e-23, 1.0982815210353256e-24, 3.8005688988835655e-26], [3.2113783233394757e-06, 2.1114461323889125e-06, 6.941263720906075e-07, 1.5212683321345008e-07, 2.5005432347121603e-08, 3.2881596686583407e-09, 3.603215045601843e-10, 3.384392132414474e-11, 2.7815010250189876e-12, 2.0320072325430938e-13, 1.3360225361668972e-14, 7.985638260262255e-16, 4.375391530158163e-17, 2.0564363902427697e-18, 9.260145211986557e-20, 4.0589628137981736e-21, 1.667952291781139e-22, 6.450943490699637e-24, 2.3563471147272166e-25, 8.154065590363544e-27], [6.39782532466504e-07, 4.206500193168251e-07, 1.3828639402601174e-07, 3.0307263987570353e-08, 4.981673668340988e-09, 6.550791928435366e-10, 7.178456770858839e-11, 6.742509761616e-12, 5.541408051837022e-13, 4.0482391120918234e-14, 2.6616729502375153e-15, 1.5909280549042026e-16, 8.716814999193624e-18, 4.408623497612474e-19, 1.924051473458229e-20, 8.086414139766393e-22, 3.3229555468860277e-23, 1.2851805510682696e-24, 4.694400885357644e-26, 1.6244827634870025e-27], [1.1896249454098304e-07, 7.821653935083348e-08, 2.571325967745602e-08, 5.635395691054185e-09, 9.263027614871636e-10, 1.2180678738152458e-10, 1.3347771798703914e-11, 1.2537162864019934e-12, 1.0303809367451504e-13, 7.527379989825392e-15, 4.949170034258326e-16, 2.958204709293885e-17, 1.62082270792634e-18, 8.197486210604411e-20, 3.849826819330398e-21, 1.5681645991656135e-22, 6.178772646110884e-24, 2.389691442515916e-25, 8.728866628236414e-27, 3.0205970322167447e-28], [2.0737625270966164e-08, 1.3634761857574953e-08, 4.482353415196979e-09, 9.82366119217841e-10, 1.6147374539598503e-10, 2.1233444388711064e-11, 2.326792917649628e-12, 2.185487001077894e-13, 1.7961672571691734e-14, 1.31217814575493e-15, 8.627427826623639e-17, 5.156763143951222e-18, 2.8254294832452104e-19, 1.4289915309472794e-20, 6.711045043686896e-22, 2.941625822324005e-23, 1.1233346561033447e-24, 4.1657268401561006e-26, 1.5216221370866432e-27, 5.265525877748273e-29], [3.4023504420268624e-09, 2.2370082122180145e-09, 7.354042193475094e-10, 1.611734109513743e-10, 2.6492438832566798e-11, 3.4836977695237357e-12, 3.8174886509082673e-13, 3.5856529216833034e-14, 2.946909485311089e-15, 2.152845292502131e-16, 1.4154722392715028e-17, 8.4605229060698755e-19, 4.635584415103666e-20, 2.3444969727455203e-21, 1.1010579452806598e-22, 4.82622372913358e-24, 1.9832433306094192e-25, 7.128018071550423e-27, 2.496472803934217e-28, 8.63896616105941e-30], [5.272000970987809e-10, 3.466282991088772e-10, 1.1395215820739937e-10, 2.497409933254471e-11, 4.10504930720551e-12, 5.398050064653568e-13, 5.915264819791433e-14, 5.556031339757682e-15, 4.566287315987947e-16, 3.335871088486822e-17, 2.1932987641920086e-18, 1.3109726859674503e-19, 7.182918383611213e-21, 3.63283868825373e-22, 1.7061083670074366e-23, 7.47831730438653e-25, 3.0730699094151115e-26, 1.1885352132846003e-27, 4.034421403443061e-29, 1.3386227775615023e-30], [7.739106504386133e-11, 5.088377902432705e-11, 1.6727764156812808e-11, 3.6661073404443624e-12, 6.0260637221141e-13, 7.92414200912692e-14, 8.68339453917756e-15, 8.156052799822466e-16, 6.703144415665157e-17, 4.896937952168998e-18, 3.2196831573875845e-19, 1.9244604272412066e-20, 1.0544264063871091e-21, 5.332875634198179e-23, 2.5045052975058322e-24, 1.097789898194899e-25, 4.5111553384125475e-27, 1.7447266513115517e-28, 6.372992751731228e-30, 2.04942266366991e-31]] |
| Legacy trial inputs | {"lambda_home": 2.7891311931186133, "lambda_away": 0.657489065378396, "rho": 0.05, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8306 |
| Legacy p draw | 0.1107 |
| Legacy p away | 0.0587 |
| Legacy p over 1 5 | 0.8579 |
| Legacy p under 3 5 | 0.5450 |
| Legacy p btts yes | 0.4464 |
| Legacy p over 2 5 | 0.6735 |
| Legacy goal margin distribution | {"-1": 0.045174698283289745, "-10": 1.4151428448178465e-10, "-11": 8.343968305196276e-12, "-12": 4.519125122440731e-13, "-13": 2.2629905596556233e-14, "-14": 1.0536480127247096e-15, "-15": 4.583623285202552e-17, "-16": 1.87100498973965e-18, "-17": 7.192414743129417e-20, "-18": 2.602787437776147e-21, "-19": 8.214067376746121e-23, "-2": 0.01102727156901092, "-3": 0.0021187885495571124, "-4": 0.0003205101399019755, "-5": 3.981158858672914e-05, "-6": 4.185521793885226e-06, "-7": 3.8096214707574354e-07, "-8": 3.05470689448049e-08, "-9": 2.1877402117165756e-09, "0": 0.11073984311959928, "1": 0.2054535567972545, "10": 0.0002997154756612524, "11": 7.496558635593375e-05, "12": 1.722360554449715e-05, "13": 3.6587510093802086e-06, "14": 7.226467829342131e-07, "15": 1.3335823732361027e-07, "16": 2.309225174873202e-08, "17": 3.7657065052925525e-09, "18": 5.780838761231079e-10, "19": 7.739106504386133e-11, "2": 0.22270691005165674, "3": 0.1815238306337877, "4": 0.11648451948428508, "5": 0.061378511830780906, "6": 0.027373911754395096, "7": 0.010569379437604665, "8": 0.0035951549814240173, "9": 0.0010922554727570606} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8178 |
| Legacy raw p draw | 0.1173 |
| Legacy raw p away | 0.0649 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7891 |
| Legacy lambda away | 0.6575 |
| Legacy model home team | Benfica |
| Legacy model away team | Alverca |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 92.5% |
| Market reference home draw last update utc | 2026-11-01T07:36:12Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.0% |
| Market reference draw away last update utc | 2026-11-01T07:36:12Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.5% |
| Market reference home away last update utc | 2026-11-01T07:36:12Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 4.80 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-11-01T07:36:12Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.79 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market reference under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 46.3% |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.75 |
| Market reference btts yes last update utc | 2026-11-01T07:36:12Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,677.3736 |
| Elo away rating | 1,429.6982 |
| Elo rating diff | 307.6754 |
| Elo home expectancy | 0.8546 |

</details>


---

## 2026-11-02 — Gil Vicente vs Vitória SC

The model's most likely 1X2 outcome is **Gil Vicente win** at **35.1%**. Expected goals are 1.17 for Gil Vicente and 1.02 for Vitória SC (2.19 combined). The most likely exact score is 1-1 at 14.2%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 42.2%; Under 3.5 goals: 77.6%; Double Chance 1X: 65.3%; Double Chance X2: 64.9%; Double Chance 12 (either team wins): 69.8%; Under 4.5 goals: 90.6%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gil Vicente win | 35.1% | 2.85 |
| Draw | 30.2% | 3.31 |
| Vitória SC win | 34.7% | 2.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gil Vicente expected goals | 1.17 |
| Vitória SC expected goals | 1.02 |
| Expected total goals | 2.19 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 68.8% |
| Under 1.5 | 31.2% |
| Over 2.5 | 42.2% |
| Under 2.5 | 57.8% |
| Over 3.5 | 22.4% |
| Under 3.5 | 77.6% |
| Over 4.5 | 9.4% |
| Under 4.5 | 90.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.24% |
| 2 | 0-1 | 11.24% |
| 3 | 1-0 | 10.43% |
| 4 | 0-0 | 9.55% |
| 5 | 1-2 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gil Vicente win | 35.1% | 33.1% | 2.89 | +1.5% |
| Draw | 30.2% | 31.3% | 3.05 | -7.8% |
| Vitória SC win | 34.7% | 35.6% | 2.69 | -6.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:15:00+00:00 |
| Fixture id | 97ce048d06fc45fc59e114548540828f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:11Z |
| Market best draw last update utc | 2026-11-01T07:36:11Z |
| Market best away last update utc | 2026-11-01T07:36:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Gil Vicente |
| Matched away-team name | Guimaraes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1705 |
| Dc lambda away | 1.0202 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.47 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.20 |
| Fair Over 2.5 odds | 2.37 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.47 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.61 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.2102338883825592, "-10": 9.668312634735385e-08, "-11": 9.791495298605546e-09, "-12": 9.103445569189853e-10, "-13": 7.788848580429048e-11, "-14": 5.6755598876050936e-12, "-2": 0.09405292018311724, "-3": 0.03171138186487976, "-4": 0.008348055939715339, "-5": 0.001796024007712714, "-6": 0.00032609259506369753, "-7": 5.115962161093535e-05, "-8": 7.061446583036955e-06, "-9": 8.697327246152401e-07, "0": 0.30219286726238603, "1": 0.19583659631234657, "10": 3.117371171832978e-07, "11": 3.622443676870939e-08, "12": 3.8643211689397035e-09, "13": 3.793634336561212e-10, "14": 3.1717993767885656e-11, "2": 0.10094661845578158, "3": 0.03905255483445015, "4": 0.011795990832566272, "5": 0.0029118969781419322, "6": 0.0006066240124420699, "7": 0.0001091995318129558, "8": 1.729425758553213e-05, "9": 2.444043033412078e-06} |
| Raw goal margin distribution | {"-1": 0.20388396702352293, "-10": 4.192097617865927e-08, "-11": 3.8527642108345746e-09, "-12": 3.2390814548102903e-10, "-13": 2.327982240384457e-11, "-2": 0.0851090281249653, "-3": 0.026452285362302746, "-4": 0.006379656061649155, "-5": 0.0012531199797885528, "-6": 0.00020729034370454288, "-7": 2.9588977658351843e-05, "-8": 3.7123960239539318e-06, "-9": 4.1534996397977264e-07, "0": 0.2776092454101563, "1": 0.2329521664554706, "10": 1.6579800868814695e-07, "11": 1.7483772481496884e-08, "12": 1.686550606762368e-09, "13": 1.390823316413613e-10, "2": 0.1120482855699026, "3": 0.0399583527093457, "4": 0.011057486937274085, "5": 0.0024921066034481677, "6": 0.0004730072805280249, "7": 7.746999109330751e-05, "8": 1.115251040960243e-05, "9": 1.4316844496296009e-06} |
| Unadjusted home-win probability | 39.9% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.3% |
| Raw p over 1 5 | 63.6% |
| Raw p under 3 5 | 82.1% |
| Raw p btts yes | 43.4% |
| P home draw | 65.3% |
| P draw away | 64.9% |
| P home away | 69.8% |
| Raw p home draw | 67.7% |
| Raw p draw away | 60.1% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1039 |
| Totals anchor target over 2 5 | 0.4221 |
| Totals anchor reference over odds | 2.24 |
| Totals anchor reference under odds | 1.67 |
| Totals anchor reference last update utc | 2026-11-01T07:36:11Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3670 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.31, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.76, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.31, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.89 |
| Reference draw odds | 3.05 |
| Reference away odds | 2.69 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:11Z |
| Market reference home last update utc | 2026-11-01T07:36:11Z |
| Market reference draw last update utc | 2026-11-01T07:36:11Z |
| Market reference away last update utc | 2026-11-01T07:36:11Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.22 |
| Reference Under 2.5 odds | 1.64 |
| Market reference over 2 5 last update utc | 2026-11-01T07:35:58Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:35:58Z |
| Home probability edge | +2.0% |
| Draw probability edge | -1.1% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0683 |
| Raw ev home | 0.1533 |
| Raw edge prob draw | -0.0351 |
| Raw ev draw | -0.1533 |
| Raw edge prob away | -0.0332 |
| Raw ev away | -0.1303 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.10874025220053371, 0.12514748152252653, 0.06216735670151011, 0.0217909877636986, 0.005728655353615765, 0.0012048097136810251, 0.00021115578272423724, 3.172055001472423e-05, 4.169524131535829e-06, 4.871691197841371e-07, 5.122895788720283e-08, 4.897321390477438e-09, 4.291539650269583e-10, 3.47140709436935e-11], [0.12321292781925443, 0.13527559451476853, 0.07265890991769632, 0.02546850149254841, 0.00669544074853332, 0.001408137085104483, 0.0002467910783021651, 3.7073807032294856e-05, 4.87318577380601e-06, 5.693852701351735e-07, 5.987451347136513e-08, 5.723808323670676e-09, 5.015793004587972e-10, 4.05725237070129e-11], [0.068406659616819, 0.07193399052606282, 0.04375201912866004, 0.01488332184180543, 0.003912691901497064, 0.0008228893027382716, 0.00014422014766483207, 2.166524803683775e-05, 2.8477997532631875e-06, 3.3273823471257393e-07, 3.4989559726416176e-08, 3.344887859496572e-09, 2.931136784824214e-10, 2.370983343650704e-11], [0.026650392223974737, 0.028024596910501843, 0.014734830643310041, 0.005974723840093275, 0.0015243365837560715, 0.0003205875392502875, 5.618639359671832e-05, 8.440513848295901e-06, 1.1094677159348133e-06, 1.2963071889016494e-07, 1.3631501606371568e-08, 1.3031271209576448e-09, 1.1419347972149679e-10, 9.237059142888847e-12], [0.007786998477233057, 0.008188528395121715, 0.004305381429940903, 0.001509128247294749, 0.0004589444257184529, 9.367271817170869e-05, 1.6417145297594007e-05, 2.466240193816632e-06, 3.241762200689711e-07, 3.787689885075132e-08, 3.982998875180681e-09, 3.8076170966855845e-10, 3.3366280136818835e-11, 2.698983372375275e-12], [0.0018202312303645734, 0.0019140898972955524, 0.0010063941530645776, 0.00035276266900302866, 9.27381435965244e-05, 2.2562246320097943e-05, 3.837550587878348e-06, 5.764900860697904e-07, 7.577703805083455e-08, 8.85382402463184e-09, 9.310363889639503e-10, 8.900404402184858e-11, 7.799455120442175e-12, 6.308944118835659e-13], [0.0003545698364696712, 0.00037285292689786544, 0.0001960393846251445, 6.871599595396273e-05, 1.8064819381730193e-05, 3.7992632692180617e-06, 7.702683993756658e-07, 1.1229671930374027e-07, 1.4760900451344871e-08, 1.7246704068011122e-09, 1.8136015615782068e-10, 1.7337439775519894e-11, 1.5192858360384418e-12, 1.2289434700358448e-13], [5.920116089973716e-05, 6.225381813917085e-05, 3.2731941519428585e-05, 1.1473245365033201e-05, 3.0162133629039747e-06, 6.343483651652327e-07, 1.1117633269826661e-07, 1.9320050027994412e-08, 2.4645707354743297e-09, 2.87961579779732e-10, 3.0281007240780855e-11, 2.8947655896495036e-12, 2.5366930849939047e-13, 2.051919611399222e-14], [8.649016230274604e-06, 9.094995356495496e-06, 4.781985507503687e-06, 1.6761881670556157e-06, 4.406548441492376e-07, 9.267536687758801e-08, 1.6242348820797974e-08, 2.4399816641516055e-09, 3.710141883650335e-10, 4.206985706629065e-11, 4.423915327237091e-12, 4.229118852942992e-13, 3.705991458595711e-14, 2.9977597993841742e-15], [1.1231834063110687e-06, 1.1810993982338302e-06, 6.210008893783318e-07, 2.1767408974234973e-07, 5.722456701220687e-08, 1.2035060575599409e-08, 2.1092730305186656e-09, 3.1686227010251995e-10, 4.165012526429759e-11, 5.629473057940062e-12, 5.745009783985735e-13, 5.4920420918114705e-14, 4.812695455068073e-15, 3.8929676776289285e-16], [1.3127352725007326e-07, 1.3804253443195289e-07, 7.258028984052559e-08, 2.5440943474474155e-08, 6.688195992605408e-09, 1.4066134199900011e-09, 2.4652403970162535e-10, 3.7033691572632806e-11, 4.867912776426363e-12, 5.687691706928805e-13, 6.918787475562278e-14, 6.41889590913606e-15, 5.624900656627128e-16, 4.549956807066117e-17], [1.3947968102292167e-08, 1.4667183150709262e-08, 7.711741954051945e-09, 2.7031304445579722e-09, 7.106287636274852e-10, 1.4945434563437986e-10, 2.6193471861666298e-11, 3.934873691488474e-12, 5.172215110895296e-13, 6.043239955972951e-14, 6.354854456784483e-15, 7.027597276582932e-16, 5.976523719648408e-17, 4.834383119063322e-18], [1.3584891541838366e-09, 1.4285384857879043e-09, 7.510999256388023e-10, 2.6327658368193886e-10, 6.921305389853594e-11, 1.4556393167875237e-11, 2.5511635224234182e-12, 3.8324458399728826e-13, 5.037578290777931e-14, 5.885929675284034e-15, 6.189432605986398e-16, 5.916895823443574e-17, 5.998002181268227e-18, 4.708540330930119e-19], [1.221347644551674e-10, 1.2843253914799868e-10, 6.752752660384864e-11, 2.3669841923672355e-11, 6.2225892706512934e-12, 1.3086903531028594e-12, 2.2936197535194624e-13, 3.4455547069382954e-14, 4.5290272364247915e-15, 5.291736281268933e-16, 5.564600137698148e-17, 5.319576350509835e-18, 4.6615631302530685e-19, 4.3619648375439524e-20]] |
| Legacy trial inputs | {"lambda_home": 1.1687630578626702, "lambda_away": 1.0515641449093145, "rho": 0.05, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3612 |
| Legacy p draw | 0.2942 |
| Legacy p away | 0.3446 |
| Legacy p over 1 5 | 0.6429 |
| Legacy p under 3 5 | 0.8160 |
| Legacy p btts yes | 0.4467 |
| Legacy p over 2 5 | 0.3770 |
| Legacy goal margin distribution | {"-1": 0.21431167493848477, "-10": 5.7255116948498815e-08, "-11": 5.422610524372743e-09, "-12": 4.697264887339712e-10, "-13": 3.47140709436935e-11, "-2": 0.09188614632353097, "-3": 0.029368047981177956, "-4": 0.00728978631456984, "-5": 0.0014744143332653095, "-6": 0.0002512110937714097, "-7": 3.694049420890833e-05, "-8": 4.775236085692924e-06, "-9": 5.505054135780926e-07, "0": 0.29422488632125704, "1": 0.21148752830132744, "10": 1.4671548016834501e-07, "11": 1.544403411468392e-08, "12": 1.4869216933318353e-09, "13": 1.221347644551674e-10, "2": 0.10110811635815171, "3": 0.03591714180367465, "4": 0.00990905394493333, "5": 0.0022275509447106006, "6": 0.00042183015444204535, "7": 6.894332350360423e-05, "8": 9.905469570537768e-06, "9": 1.269207181870026e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3915 |
| Legacy raw p draw | 0.2757 |
| Legacy raw p away | 0.3328 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1688 |
| Legacy lambda away | 1.0516 |
| Legacy model home team | Gil Vicente |
| Legacy model away team | Guimaraes |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 64.8% |
| Market reference home draw last update utc | 2026-11-01T07:36:12Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 66.6% |
| Market reference draw away last update utc | 2026-11-01T07:36:12Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.6% |
| Market reference home away last update utc | 2026-11-01T07:36:12Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.44 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 68.5% |
| Market over 1 5 odds | 1.37 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference over 1 5 odds | 1.40 |
| Market reference over 1 5 opposite odds | 2.80 |
| Market reference over 1 5 last update utc | 2026-11-01T07:36:12Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.8% |
| Market under 3 5 odds | 1.24 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market reference under 3 5 odds | 1.24 |
| Market reference under 3 5 opposite odds | 4.05 |
| Market reference under 3 5 last update utc | 2026-11-01T07:36:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.2% |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 1.91 |
| Market reference btts yes last update utc | 2026-11-01T07:36:12Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,467.0612 |
| Elo away rating | 1,413.2222 |
| Elo rating diff | 113.8391 |
| Elo home expectancy | 0.6582 |

</details>


---
