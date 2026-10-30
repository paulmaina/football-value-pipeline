# Primeira Liga — football model report

Fixtures in this report: **7**.

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
| Training as of utc | 2026-10-30T07:27:43.564568+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1611, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1305, 'tuning_matches': 198, 'audit_matches': 102, 'audit_matchdays': 41, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8837344359511681, 'audit_candidate_poisson_score': 0.8736484990801736, 'audit_gain': 0.01008593687099446, 'audit_gain_lower95': 0.00023297794577317968, 'audit_baseline_briers': [0.5954697810046405, 0.18598455544953954, 0.24306383498498632, 0.24914758134276963], 'audit_candidate_briers': [0.5923556867208057, 0.18512769162308795, 0.2410787201841528, 0.24810667643781506], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1461.138 |
| Base scoring parameter | 0.094 |
| Home-advantage parameter | 0.170 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 32.00 |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 2, 'ANCHORED_MAIN': 3, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 7 |
| Goal rate features used | {'shot_features': 7} |
| Legacy comparison status | {'AVAILABLE': 7} |
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

## 2026-10-30 — Casa Pia vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **75.4%**. Expected goals are 0.73 for Casa Pia and 2.38 for Sporting Lisbon (3.11 combined). The most likely exact score is 0-2 at 12.9%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 59.9%; Under 3.5 goals: 62.5%; Double Chance 1X: 24.6%; Double Chance X2: 90.9%; Double Chance 12 (either team wins): 84.5%; Under 4.5 goals: 79.9%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Casa Pia win | 9.1% | 10.97 |
| Draw | 15.5% | 6.44 |
| Sporting Lisbon win | 75.4% | 1.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Casa Pia expected goals | 0.73 |
| Sporting Lisbon expected goals | 2.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 59.9% |
| Under 2.5 | 40.1% |
| Over 3.5 | 37.5% |
| Under 3.5 | 62.5% |
| Over 4.5 | 20.1% |
| Under 4.5 | 79.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.89% |
| 2 | 0-1 | 11.30% |
| 3 | 0-3 | 10.15% |
| 4 | 1-2 | 9.36% |
| 5 | 1-3 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Casa Pia win | 9.1% | 8.7% | 10.02 | -8.6% |
| Draw | 15.5% | 15.5% | 5.82 | -9.6% |
| Sporting Lisbon win | 75.4% | 75.8% | 1.30 | -2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:15:00+00:00 |
| Fixture id | 75daf3f21fd7945dcc4215b1fe8a5da3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:27:32Z |
| Market best draw last update utc | 2026-10-30T07:27:32Z |
| Market best away last update utc | 2026-10-30T07:27:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Casa Pia |
| Matched away-team name | Sp Lisbon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6959 |
| Dc lambda away | 2.5773 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 0.8099 |
| Shot lambda away | 1.9040 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.23 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.32 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.97 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.23766418553538293, "-10": 8.076118671551342e-05, "-11": 1.7131610901589046e-05, "-12": 3.3377021923336045e-06, "-13": 6.01173235795861e-07, "-14": 1.0067013507869239e-07, "-15": 1.5749682873713572e-08, "-16": 2.3116285010678965e-09, "-17": 3.183426823945022e-10, "-18": 3.815891240870335e-11, "-2": 0.22045483339468325, "-3": 0.15338143113856334, "-4": 0.0838069243104777, "-5": 0.0375473143513942, "-6": 0.014225388617472133, "-7": 0.0046632314170884535, "-8": 0.0013461371370263719, "-9": 0.0003469794047670385, "0": 0.15527927806599517, "1": 0.06779505118054523, "10": 5.438472779478989e-10, "11": 3.546053753811514e-11, "12": 2.123574697667573e-12, "13": 1.1756889627400385e-13, "14": 6.051545462521258e-15, "15": 2.910116048015362e-16, "16": 1.3128931434067955e-17, "17": 5.557494692258813e-19, "18": 2.0476372370077877e-20, "2": 0.018629925959265024, "3": 0.003984163339451572, "4": 0.000669140162046996, "5": 9.214863763051466e-05, "6": 1.073116876979258e-05, "7": 1.0812912764266169e-06, "8": 9.594401356509068e-08, "9": 7.601601862780828e-09} |
| Raw goal margin distribution | {"-1": 0.2334801131898278, "-10": 8.256897855104704e-05, "-11": 1.760109701869971e-05, "-12": 3.446074642806813e-06, "-13": 6.237618812187113e-07, "-14": 1.0497048549717694e-07, "-15": 1.6504028819487994e-08, "-16": 2.434387745966018e-09, "-17": 3.368930165890007e-10, "-18": 4.0550267608839036e-11, "-2": 0.2172773394625003, "-3": 0.15176605317865557, "-4": 0.08328196277872968, "-5": 0.03748108102943744, "-6": 0.014266491265967855, "-7": 0.004698916756270925, "-8": 0.0013629629317437747, "-9": 0.00035302154150048466, "0": 0.15567428571215997, "1": 0.07445761601106961, "10": 6.216491816449464e-10, "11": 4.0732497212871e-11, "12": 2.4513133206473985e-12, "13": 1.363847530035641e-13, "14": 7.054837939371792e-15, "15": 3.40943688050872e-16, "16": 1.5458070370042918e-17, "17": 6.575524205967868e-19, "18": 2.432791794269546e-20, "2": 0.02052863748543027, "3": 0.004407508680456007, "4": 0.0007434338538095902, "5": 0.0001028433785606477, "6": 1.2032455034698126e-05, "7": 1.2181693532469837e-06, "8": 1.0860924831555612e-07, "9": 8.646827912403324e-09} |
| Unadjusted home-win probability | 10.0% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 74.4% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 62.4% |
| Raw p btts yes | 46.6% |
| P home draw | 24.6% |
| P draw away | 90.9% |
| P home away | 84.5% |
| Raw p home draw | 25.6% |
| Raw p draw away | 90.0% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9950 |
| Totals anchor target over 2 5 | 0.5987 |
| Totals anchor reference over odds | 1.62 |
| Totals anchor reference under odds | 2.36 |
| Totals anchor reference last update utc | 2026-10-30T07:27:32Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6017 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.02 |
| Reference draw odds | 5.82 |
| Reference away odds | 1.30 |
| Market reference 1x2 last update utc | 2026-10-30T07:27:32Z |
| Market reference home last update utc | 2026-10-30T07:27:32Z |
| Market reference draw last update utc | 2026-10-30T07:27:32Z |
| Market reference away last update utc | 2026-10-30T07:27:32Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:44Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:44Z |
| Home probability edge | +0.4% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.0130 |
| Raw ev home | 0.0045 |
| Raw edge prob draw | 0.0006 |
| Raw ev draw | -0.0940 |
| Raw edge prob away | -0.0135 |
| Raw ev away | -0.0327 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03853307137025416, 0.10426489620325273, 0.12582986195577528, 0.1048064278907985, 0.0654716644155369, 0.03271966368938348, 0.013626459648655564, 0.0048641890782728965, 0.0015193083162715196, 0.00042182164344307645, 0.00010540332549637453, 2.394346951304639e-05, 4.985759087649261e-06, 9.583262647956636e-07, 1.71045167667635e-07, 2.849344782326491e-08, 4.4499022900345205e-09, 6.540741829053153e-10, 9.07987680354078e-11], [0.03211041950650635, 0.070739883579569, 0.0887377320001258, 0.07391158637154752, 0.04617192548895925, 0.023074560382361574, 0.00960965152165477, 0.0034303232962094826, 0.0010714465715797167, 0.0002974770484995062, 7.43325304855428e-05, 1.6885412951884552e-05, 3.5160568950835243e-06, 6.758308237197908e-07, 1.2062446872700024e-07, 2.0094148538358142e-08, 3.1381599781029206e-09, 4.612661783834149e-10, 6.403310484993976e-11], [0.010064956448131084, 0.025149963191785762, 0.03280430207297749, 0.02606196351644929, 0.016280682050692625, 0.008136320438587042, 0.003388459099013036, 0.0012095662531991438, 0.00037780276177490737, 0.00010489337823169259, 2.6210392615051792e-05, 5.953965243013654e-06, 1.2397967763915036e-06, 2.3830469802847347e-07, 4.2533392360853724e-08, 7.085397456742995e-09, 1.1065465493727198e-09, 1.6264706120593112e-10, 2.257871227462279e-11], [0.0023660027755072993, 0.005912085464286408, 0.007386456790933462, 0.006423006347193317, 0.0038271540585000006, 0.0019126318965531405, 0.0007965363461107142, 0.0002843367606186255, 8.881135130194577e-05, 2.4657635162902733e-05, 6.1613641344532225e-06, 1.3996184049917142e-06, 2.9144315021372824e-07, 5.6019077663916966e-08, 9.998465954237405e-09, 1.665587937177724e-09, 2.6011957632762746e-10, 3.823398543495881e-11, 5.307652962478324e-12], [0.0004171381040660914, 0.001042330189625562, 0.0013022692168547644, 0.0010846883454315919, 0.0007074054913566968, 0.0003372065541780461, 0.00014043333536035838, 5.012999074581246e-05, 1.5657884718118315e-05, 4.347264208259972e-06, 1.0862792639605264e-06, 2.4675971385919844e-07, 5.1382882717513794e-08, 9.876443126000618e-09, 1.7627794755336657e-09, 2.9365147051473717e-10, 4.5860380225681066e-11, 6.7408425553556875e-12, 9.357657212951781e-13], [5.883482459619512e-05, 0.0001470144138839504, 0.00018367725269838924, 0.000152988777392759, 9.557075929768799e-05, 4.98630082825592e-05, 1.9807278627502803e-05, 7.07053415592899e-06, 2.2084506113399205e-06, 6.131555105447e-07, 1.5321316689754007e-07, 3.480397580752535e-08, 7.2472470447168955e-09, 1.3930129932711139e-09, 2.486294592458611e-10, 4.1417776491144925e-11, 6.4683312317717675e-12, 9.50755362574316e-13, 1.3198413556295684e-13], [6.915248913815755e-06, 1.7279583527338244e-05, 2.1588811234381432e-05, 1.7981790273913654e-05, 1.1233068067455824e-05, 5.613759977665804e-06, 2.4407653756552e-06, 8.310469858194696e-07, 2.5957391385291516e-07, 7.206825221959771e-08, 1.800816426737516e-08, 4.0907431534184315e-09, 8.518172289643236e-10, 1.6373009785895204e-10, 2.922307680515683e-11, 4.868107211312672e-12, 7.602660640481106e-13, 1.1174861204178271e-13, 1.5512974779084728e-14], [6.966816657832066e-07, 1.7408439212961648e-06, 2.1749801287700676e-06, 1.8115882389664913e-06, 1.1316834246495753e-06, 5.655622380755722e-07, 2.355345424421546e-07, 8.777685415592567e-08, 2.615095840377058e-08, 7.26056728140666e-09, 1.8142453056790734e-09, 4.1212482586432785e-10, 8.581693203148108e-11, 1.649510505505157e-11, 2.944099638590345e-12, 4.904409202700921e-13, 7.659354486593853e-14, 1.1258193328470078e-14, 1.5628656676050304e-15], [6.141422829482994e-08, 1.5345973815452563e-07, 1.917299287829534e-07, 1.5969602638967406e-07, 9.9760719439589e-08, 4.9855723366942376e-08, 2.0762957992584903e-08, 7.4116796368405905e-09, 2.4168522218202026e-09, 6.40037133845054e-10, 1.5993025345448084e-10, 3.6329832382118306e-11, 7.56497682398222e-12, 1.4540846951373286e-12, 2.595297338905113e-13, 4.323359164150399e-14, 6.751912216634705e-15, 9.924378510588602e-16, 1.3777051072033645e-16], [4.812282276961995e-09, 1.20247636199708e-08, 1.5023530602973723e-08, 1.2513425289770819e-08, 7.81702799864908e-09, 3.906583549533165e-09, 1.6269391888367035e-09, 5.807627246842842e-10, 1.813987127545285e-10, 5.257934064882878e-11, 1.2531778801392644e-11, 2.8467248282949716e-12, 5.927747511685749e-13, 1.1393884124080293e-13, 2.0336172470494264e-14, 3.3876880423707365e-15, 5.290648176792229e-16, 7.776522174485832e-17, 1.079539066817991e-17], [3.393717583128995e-10, 8.480103489653845e-10, 1.0594893863993324e-09, 8.824717459815305e-10, 5.512724283408979e-10, 2.7550007499524506e-10, 1.147350012751621e-10, 4.095654737093313e-11, 1.2792599552590025e-11, 3.5517447705580255e-12, 9.26542177823606e-13, 2.0075672099213418e-13, 4.180365947164896e-14, 8.035194667848237e-15, 1.4341475024659128e-15, 2.3890652737867665e-16, 3.7310707706581494e-17, 5.484158767138239e-18, 7.613125128328413e-19], [2.1757431148769543e-11, 5.436671240052648e-11, 6.792482524778013e-11, 5.6576063810899e-11, 3.534257524394061e-11, 1.7662559616004595e-11, 7.35576496703273e-12, 2.625761389057001e-12, 8.201451569303374e-13, 2.277055777639857e-13, 5.68982779889915e-14, 1.3493663692826841e-14, 2.6800705139477677e-15, 5.15143616020871e-16, 9.194449678783379e-17, 1.5316514097324068e-17, 2.39202330233192e-18, 3.5159439128967645e-19, 4.880843551332029e-20], [1.2786479194218635e-12, 3.195040959634215e-12, 3.991828625645427e-12, 3.3248808550165495e-12, 2.07702416676295e-12, 1.037999153036323e-12, 4.322860316800102e-13, 1.5431161491718058e-13, 4.8198562199848664e-14, 1.3381876806037348e-14, 3.3438168445462458e-15, 7.595830235674857e-16, 1.651267556178889e-16, 3.027413063264102e-17, 5.403424637595719e-18, 9.001259730263068e-19, 1.4057521762665885e-19, 2.066261562906822e-20, 2.8683903027252645e-21], [6.936369636354637e-14, 1.7332359254404152e-13, 2.1654748310213177e-13, 1.8036710698017103e-13, 1.1267376378967086e-13, 5.6309056608314923e-14, 2.345051877706274e-14, 8.371048699100388e-15, 2.614660676178504e-15, 7.259359088998075e-16, 1.8139434067611686e-16, 4.1205624636265815e-17, 8.58026516919718e-18, 1.7217924601393441e-18, 2.9312330641804847e-19, 4.88297550354352e-20, 7.625880872745498e-21, 1.120899173886263e-21, 1.5560354886459769e-22], [3.494047439918622e-15, 8.730804247108665e-15, 1.0908115031647376e-14, 9.08560618059562e-15, 5.675699199360934e-15, 2.8364479605489184e-15, 1.1812695890414114e-15, 4.2167362481993327e-16, 1.317079238968964e-16, 3.6567464495294505e-17, 9.137350874919666e-18, 2.0756449673039206e-18, 4.322124557942683e-19, 8.30767273504131e-20, 1.5480136596481785e-20, 2.4596941846813195e-21, 3.8413739372955326e-22, 5.646289189084325e-23, 7.838195050953634e-24], [1.6427146969198525e-16, 4.1047583638388466e-16, 5.128413734015256e-16, 4.271567304088432e-16, 2.6684109619025657e-16, 1.3335465050098383e-16, 5.553699393926935e-17, 1.9824844187327505e-17, 6.192203912699945e-18, 1.719207091158277e-18, 4.2958948987520335e-19, 9.75857526839215e-20, 2.032032379450472e-20, 3.905824501160911e-21, 6.971241749529556e-22, 1.212389952920549e-22, 1.8060090859290742e-23, 2.6545839441105363e-24, 3.685101140992487e-25], [7.240470100967327e-18, 1.809223492113237e-17, 2.2604123756944343e-17, 1.882746614948613e-17, 1.1761354435420646e-17, 5.8777726989827354e-18, 2.4478623395094776e-18, 8.738047566252706e-19, 2.7292911771632067e-19, 7.577619877780786e-20, 1.893469305999015e-20, 4.301213874284823e-21, 8.956436388616829e-22, 1.7215409086743544e-22, 3.0726618291494204e-23, 5.118573690285728e-24, 8.345501156328207e-25, 1.1700410128355974e-25, 1.6242543321993833e-26], [3.0036024339351853e-19, 7.505297320015211e-19, 9.376987983730444e-19, 7.810297171709025e-19, 4.879024747838435e-19, 2.438307477082695e-19, 1.0154596563980926e-19, 3.6248503994694537e-20, 1.1322062667657478e-20, 3.143464055641533e-21, 7.854778677036999e-22, 1.784295257286082e-22, 3.7154457875105543e-23, 7.141559030431546e-24, 1.2746485269595876e-24, 2.1233649445448067e-25, 3.31611905583221e-26, 5.088674093169563e-27, 6.73797998954799e-28], [1.1767780171783954e-20, 2.940491990150122e-20, 3.673799568787427e-20, 3.059987538782273e-20, 1.9115476148430668e-20, 9.553017422460067e-21, 3.978457959281931e-21, 1.4201760584097413e-21, 4.435858190113256e-22, 1.2315742445390572e-22, 3.0774148976928815e-23, 6.990670307118416e-24, 1.455670323529522e-24, 2.7979833750444507e-25, 4.993931118206151e-26, 8.319107618759743e-27, 1.2992185527486919e-27, 1.9096718487675704e-28, 2.767640551002809e-29]] |
| Legacy trial inputs | {"lambda_home": 0.7052199741847761, "lambda_away": 2.4987652277875227, "rho": 0.05, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0876 |
| Legacy p draw | 0.1493 |
| Legacy p away | 0.7632 |
| Legacy p over 1 5 | 0.8251 |
| Legacy p under 3 5 | 0.6026 |
| Legacy p btts yes | 0.4628 |
| Legacy p over 2 5 | 0.6185 |
| Legacy goal margin distribution | {"-1": 0.22324961746184996, "-10": 0.00012358635927122854, "-11": 2.770812980522585e-05, "-12": 5.705835718315646e-06, "-13": 1.0863031233824255e-06, "-14": 1.9228503250652212e-07, "-15": 3.179956251553624e-08, "-16": 4.933747180692558e-09, "-17": 7.18107287755255e-10, "-18": 9.07987680354078e-11, "-2": 0.2180825331413853, "-3": 0.1599636225252409, "-4": 0.09223531012572825, "-5": 0.04363219747094924, "-6": 0.01746036529361791, "-7": 0.006046944565897629, "-8": 0.0018444481814071287, "-9": 0.0005024097123401361, "0": 0.1492600628822348, "1": 0.06583295548516273, "10": 3.979164779844559e-10, "11": 2.5178378019521515e-11, "12": 1.4633187928916024e-12, "13": 7.862666690569826e-14, "14": 3.92792754525277e-15, "15": 1.833320032868785e-16, "16": 8.027737828656722e-18, "17": 3.2976516329501975e-19, "18": 1.1767780171783954e-20, "2": 0.017444119893714957, "3": 0.003611175215982628, "4": 0.0005876567021360753, "5": 7.8457184319495e-05, "6": 8.860905564963128e-06, "7": 8.660838107395456e-07, "8": 7.455719189960488e-08, "9": 5.731657898664171e-09} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0878 |
| Legacy raw p draw | 0.1434 |
| Legacy raw p away | 0.7688 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.7052 |
| Legacy lambda away | 2.4988 |
| Legacy model home team | Casa Pia |
| Legacy model away team | Sp Lisbon |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 28.3% |
| Market reference home draw last update utc | 2026-10-30T07:27:40Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.4% |
| Market reference draw away last update utc | 2026-10-30T07:27:40Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.3% |
| Market reference home away last update utc | 2026-10-30T07:27:40Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.28 |
| Market reference dc draw away odds | 1.04 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:27:32Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.52 |
| Market reference over 1 5 last update utc | 2026-10-30T07:27:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:27:32Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.58 |
| Market reference under 3 5 last update utc | 2026-10-30T07:27:32Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 46.1% |
| Market reference btts yes odds | 2.10 |
| Market reference btts yes opposite odds | 1.81 |
| Market reference btts yes last update utc | 2026-10-30T07:27:32Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,356.0841 |
| Elo away rating | 1,692.9144 |
| Elo rating diff | -276.8303 |
| Elo home expectancy | 0.1689 |

</details>


---

## 2026-10-31 — FC Porto vs Estoril

The model's most likely 1X2 outcome is **FC Porto win** at **79.7%**. Expected goals are 2.34 for FC Porto and 0.69 for Estoril (3.04 combined). The most likely exact score is 2-0 at 15.2%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 56.1%; Under 3.5 goals: 66.9%; Double Chance 1X: 93.6%; Double Chance X2: 20.3%; Double Chance 12 (either team wins): 86.1%; Under 4.5 goals: 83.1%; BTTS Yes (both teams score): 41.0%; BTTS No (at least one team does not score): 59.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Porto win | 79.7% | 1.26 |
| Draw | 13.9% | 7.19 |
| Estoril win | 6.4% | 15.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Porto expected goals | 2.34 |
| Estoril expected goals | 0.69 |
| Expected total goals | 3.04 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 78.6% |
| Under 1.5 | 21.4% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 16.9% |
| Under 4.5 | 83.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 15.19% |
| 2 | 1-0 | 14.24% |
| 3 | 3-0 | 11.15% |
| 4 | 2-1 | 9.87% |
| 5 | 3-1 | 7.25% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:30:00+00:00 |
| Fixture id | 60352ce6c1b34bca7b294edae8aa388b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 10.00 |
| Matched home-team name | Porto |
| Matched away-team name | Estoril |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5378 |
| Dc lambda away | 0.6307 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.8905 |
| Shot lambda away | 0.8335 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 41.0% |
| P btts no | 59.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.39 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.67 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.93 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.049077514027305924, "-10": 1.5764035356824788e-10, "-11": 9.213982769360755e-12, "-12": 4.944753497509161e-13, "-13": 2.452654383934098e-14, "-14": 1.1308084033174548e-15, "-15": 4.869716367782975e-17, "-16": 1.9615382714138224e-18, "-17": 6.916044870012e-20, "-2": 0.012412983452191117, "-3": 0.0024188506848106793, "-4": 0.00036781460830399273, "-5": 4.5695173363703434e-05, "-6": 4.78994936615026e-06, "-7": 4.3380547415824665e-07, "-8": 3.456224560037966e-08, "-9": 2.457016599612539e-09, "0": 0.13901812725782883, "1": 0.2677434945146389, "10": 5.2737324842126986e-05, "11": 1.0446305472746007e-05, "12": 1.8998731359697753e-06, "13": 3.1936030869355076e-07, "14": 4.9899735392497805e-08, "15": 7.282450012879716e-09, "16": 9.941118745065704e-10, "17": 1.187848100543941e-10, "2": 0.23867659447916723, "3": 0.15761855668263922, "4": 0.08122540583057257, "5": 0.03419777694539655, "6": 0.01214851232101612, "7": 0.0037286518447635104, "8": 0.0010067540555822208, "9": 0.000242546022100758} |
| Raw goal margin distribution | {"-1": 0.07241553737544362, "-10": 3.8361228667819977e-10, "-11": 2.382726634090349e-11, "-12": 1.3591392508630983e-12, "-13": 7.166713367373252e-14, "-14": 3.51314298172047e-15, "-15": 1.608859632717384e-16, "-16": 6.912007357775692e-18, "-17": 2.787226645368765e-19, "-18": 9.823767591862783e-21, "-2": 0.01910652146666119, "-3": 0.003913576929873829, "-4": 0.0006282155522844508, "-5": 8.258757040204174e-05, "-6": 9.17455632541134e-06, "-7": 8.814169480988868e-07, "-8": 7.454374606461234e-08, "-9": 5.62792552087725e-09, "0": 0.15604366842960965, "1": 0.23610701570355977, "10": 7.665470350493818e-05, "11": 1.6135601098978468e-05, "12": 3.1191733678046815e-06, "13": 5.573913497232647e-07, "14": 9.259779493542315e-08, "15": 1.4371020347894606e-08, "16": 2.092368970669548e-09, "17": 2.8593741998393794e-10, "18": 3.415398776694546e-11, "2": 0.21943752004985856, "3": 0.15232379986861594, "4": 0.0828642499172271, "5": 0.0369179723127506, "6": 0.013898657438546918, "7": 0.004525158614838813, "8": 0.0012969649907607363, "9": 0.0003318409751507267} |
| Unadjusted home-win probability | 74.8% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 9.6% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 44.7% |
| P home draw | 93.6% |
| P draw away | 20.3% |
| P home away | 86.1% |
| Raw p home draw | 90.4% |
| Raw p draw away | 25.2% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9397 |
| Totals anchor target over 2 5 | 0.5606 |
| Totals anchor reference over odds | 1.64 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-10-30T07:27:54Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5974 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.71, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:54Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 3.71, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.22 |
| Reference draw odds | 7.40 |
| Reference away odds | 19.00 |
| Market reference 1x2 last update utc | 2026-10-30T07:27:32Z |
| Market reference home last update utc | 2026-10-30T07:27:32Z |
| Market reference draw last update utc | 2026-10-30T07:27:32Z |
| Market reference away last update utc | 2026-10-30T07:27:32Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:43Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:43Z |
| Home probability edge | -2.1% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.0698 |
| Raw edge prob draw | 0.0243 |
| Raw edge prob away | 0.0455 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.037607167184167706, 0.024836968033745518, 0.0069803502760194015, 0.0014749266397491427, 0.0002337356121062282, 2.9632571488960335e-05, 3.1306358108910035e-06, 2.834973261216344e-07, 2.2463293856699682e-08, 1.5821417367158884e-09, 1.0029051135261731e-10, 5.779384898994658e-12, 3.052915832238197e-13, 1.4886271556234646e-14, 6.740193425615936e-16, 2.8483644652205284e-17, 1.1284700435900728e-18, 4.2078046743025626e-20, 1.4818270725637032e-21], [0.11040822536712652, 0.06295164246996793, 0.01783225334926528, 0.003767900531001107, 0.0005971093837715992, 7.570043067848576e-05, 7.997634605225899e-06, 7.242324444101026e-07, 5.7385536724110037e-08, 4.041796065806178e-09, 2.5620573986254014e-10, 1.476422409285757e-11, 7.799088358285025e-13, 3.802900360583565e-14, 1.721874003967269e-15, 7.27653409447841e-17, 2.8828300756606145e-18, 1.0749408844734226e-19, 3.7855286243349844e-21], [0.1366939554751632, 0.08664904272023426, 0.02682668050245377, 0.004812806965752917, 0.0007626985314203188, 9.66935186006918e-05, 1.0215522204178502e-05, 9.250750980825665e-07, 7.32995758796971e-08, 5.162658647598729e-09, 3.272561893104685e-10, 1.8858608387722612e-11, 9.961915519915198e-13, 4.8575128761740347e-14, 2.1993805654526454e-15, 9.294447581167847e-17, 3.682290589962853e-18, 1.3730412822739055e-19, 4.835323645716251e-21], [0.11640109492883192, 0.07378558482787484, 0.02338600221810709, 0.004826895485815765, 0.0006494723475469847, 8.233891102585688e-05, 8.6989798905353e-06, 7.877433492497945e-07, 6.241790912083163e-08, 4.396237691969366e-09, 2.786734689588889e-10, 1.6058959282686196e-11, 8.483022311234122e-13, 4.136392245378341e-14, 1.8728721770758737e-15, 7.914643127019214e-17, 3.1356372344912485e-18, 1.1692068466641848e-19, 4.1174971105354286e-21], [0.07434060372420483, 0.04712382581625589, 0.014935680155350925, 0.003155863484326737, 0.0004885301599738496, 5.258648434018824e-05, 5.555681561608149e-06, 5.030993582900699e-07, 3.986375772566573e-08, 2.807696648694978e-09, 1.7797731144186018e-10, 1.0256198440291555e-11, 5.417758315835564e-13, 2.6417440226791063e-14, 1.1961266208639388e-15, 5.054757849863646e-17, 2.0026028553657235e-18, 7.467244437230784e-20, 2.6296764752687395e-21], [0.03798263489159238, 0.024076843353520776, 0.00763104491729582, 0.0016124164250479818, 0.00025552399008999275, 3.164425238944114e-05, 2.8385487036313582e-06, 2.570471355198904e-07, 2.0367477249957622e-08, 1.4345285261519387e-09, 9.093344553082201e-11, 5.240170528861012e-12, 2.7680799688511243e-13, 1.3497388192153845e-14, 6.111335992499714e-16, 2.5826131650619044e-17, 1.0231842260846567e-18, 3.815218129756248e-20, 1.343573181268383e-21], [0.01617196705697322, 0.010251261363524609, 0.003249090205695762, 0.000686522811869761, 0.00010879512603051196, 1.3792846202162838e-05, 1.4234289907452106e-06, 1.0944363969433724e-07, 8.671914733142337e-09, 6.107830100105228e-10, 3.8716973946087135e-11, 2.2311212849643734e-12, 1.1785727397557885e-13, 5.7468187191776e-15, 2.6020397117493574e-16, 1.0996060474870196e-17, 4.356438579019812e-19, 1.624415527929646e-20, 5.720567119190206e-22], [0.005901926782480091, 0.0037411771729711275, 0.0011857489219544934, 0.00025054511648974566, 3.9704561965818936e-05, 5.033671421688482e-06, 5.317996792437498e-07, 4.704172021658113e-08, 3.1647978034216704e-09, 2.2290402845648585e-10, 1.4129681606695225e-11, 8.142432160727619e-13, 4.3011774593408676e-14, 2.097289908721856e-15, 9.496091483335341e-17, 4.012990107497388e-18, 1.589873478913625e-19, 5.928271728719978e-21, 2.0877094402171446e-22], [0.0018846592483252793, 0.0011946681852431538, 0.00037864459426827925, 8.000644337317756e-05, 1.2678837380991719e-05, 1.6073997098841262e-06, 1.6981931845009818e-07, 1.5378129432020776e-08, 1.19027329110315e-09, 7.11798289274854e-11, 4.512023970714105e-12, 2.6001186800775523e-13, 1.373492789083467e-14, 6.697265094215456e-16, 3.0323820163506474e-17, 1.2814660700271607e-18, 5.076934814908907e-20, 1.8930719664777684e-21, 6.666671833342936e-23], [0.0005349575731914788, 0.0003391046915853098, 0.00010747767450897338, 2.270970353109134e-05, 3.5988681148869936e-06, 4.5625788784492674e-07, 4.820294732844779e-08, 4.365057932084297e-09, 3.4587126577644535e-10, 2.379606449874646e-11, 1.2807309309095872e-12, 7.380396113197274e-14, 3.898637750548276e-15, 1.9010081981690634e-16, 8.607368816924967e-18, 3.6374213511440757e-19, 1.441079988463912e-20, 5.373455100510456e-22, 1.8923243490292683e-23], [0.0001366621816820708, 8.66289016046635e-05, 2.7456632481870523e-05, 5.801502372228505e-06, 9.193797654500277e-07, 1.165572775997004e-07, 1.2314097931376944e-08, 1.1151133661094048e-09, 8.835751493367449e-11, 6.223224119350162e-12, 3.853440035892855e-13, 1.8854224803102214e-14, 9.959599924895406e-16, 4.856383772779998e-17, 2.1988693309743158e-18, 9.292287135570046e-20, 3.681434660826082e-21, 1.372722126028418e-22, 4.8341997000924684e-24], [3.1738374028568886e-05, 2.0118663751535976e-05, 6.3765180721455315e-06, 1.347338743982416e-06, 2.135164133266511e-07, 2.706921861394779e-08, 2.8598215040916628e-09, 2.589735116344916e-10, 2.0520116265403743e-11, 1.4452792450148582e-12, 9.161492372405172e-14, 5.1571136555732944e-15, 2.3130137665049993e-16, 1.1278447534617796e-17, 5.106645921163988e-19, 2.1580372935629273e-20, 8.54975010561864e-22, 3.1880047381753494e-23, 1.1226927327068954e-24], [6.7566657855209345e-06, 4.2829883754613e-06, 1.3574734940750311e-06, 2.868299927645419e-07, 4.5454724406257824e-08, 5.762666451816797e-09, 6.088168880989284e-10, 5.513191897738428e-11, 4.368452125511007e-12, 3.076801860273416e-13, 1.9503564360676298e-14, 1.1239209355145177e-15, 5.799461617523089e-17, 2.4010272392136514e-18, 1.08713507954883e-19, 4.594166270827173e-21, 1.8201248734855954e-22, 6.786826104928628e-24, 2.3900592916025087e-25], [1.3277554555000867e-06, 8.416519866275655e-07, 2.667577315008372e-07, 5.6365091863842774e-08, 8.932328492256273e-09, 1.1324241959730383e-09, 1.1963888258409899e-10, 1.0833998382941614e-11, 8.584465068803154e-13, 6.046237279081096e-14, 3.83265427114632e-15, 2.2086221237670812e-16, 1.1666877300823125e-17, 5.557051757025955e-19, 2.13633407150268e-20, 9.028016958655837e-22, 3.576735637332668e-23, 1.3336822735349527e-24, 4.6967163452043305e-26], [2.4228083868192854e-07, 1.5357959807563724e-07, 4.867634822751994e-08, 1.028516333530131e-08, 1.6299176399702584e-09, 2.0663796394699766e-10, 2.1830984532107904e-11, 1.976922936843908e-12, 1.5664416123389166e-13, 1.1032810543369026e-14, 6.993597257271037e-16, 4.030160962706855e-17, 2.1289016780412674e-18, 1.0380701675817861e-19, 4.591259481202094e-21, 1.6473782964453937e-22, 6.5266123092683054e-24, 2.4336232883002346e-25, 8.570285819225944e-27], [4.126262175210283e-08, 2.6155996894803853e-08, 8.290023082768899e-09, 1.7516564936457316e-09, 2.7758974020007524e-10, 3.519231728086964e-11, 3.718014441938474e-12, 3.366878859253795e-13, 2.6677919763828136e-14, 1.8789875864318782e-15, 1.1910729708681783e-16, 6.863729228813637e-18, 3.625712423909732e-19, 1.767927538557928e-20, 8.004807333615242e-22, 3.304401327178172e-23, 1.1115412036091964e-24, 4.144680932199996e-26, 1.4595973168575128e-27], [6.588185906177049e-09, 4.176190527582645e-09, 1.3236244067064675e-09, 2.7967778424821506e-10, 4.43212945864809e-11, 5.6189723015775315e-12, 5.936358211192305e-13, 5.375718484783603e-14, 4.259523208440279e-15, 3.000080704804286e-16, 1.90172360036775e-17, 1.0958955647742136e-18, 5.788984431130047e-20, 2.822756964558619e-21, 1.2780855073587038e-22, 5.401111085089086e-24, 2.090240654847288e-25, 6.617594167226954e-27, 2.3304623078451014e-28], [9.900244808682414e-10, 6.275674241676089e-10, 1.9890461270764395e-10, 4.202793562657521e-11, 6.660280582435944e-12, 8.443781361218964e-13, 8.920725735400403e-14, 8.078237284108406e-15, 6.40090051075888e-16, 4.5083022620109886e-17, 2.8577713911255975e-18, 1.646831848785783e-19, 8.699263177759265e-21, 4.241833090705832e-22, 1.9206135937081728e-23, 8.116395430058355e-25, 3.215567816755183e-26, 1.1712292653885378e-27, 3.502048620613631e-29], [1.4050844845190285e-10, 8.906701477868127e-11, 2.822938125425724e-11, 5.9647818217057255e-12, 9.452551012392145e-13, 1.198377051334622e-13, 1.266067007804513e-14, 1.1464974947093723e-15, 9.084427878722506e-17, 6.3983726486423326e-18, 4.0558696472348474e-19, 2.33725319328608e-20, 1.234636107896809e-21, 6.020188365890897e-23, 2.7258157888267777e-24, 1.1519130596644194e-25, 4.5636694198501725e-27, 1.7016871316960628e-28, 5.853833600721762e-30]] |
| Legacy trial inputs | {"lambda_home": 2.5546358913430143, "lambda_away": 0.6338908141112215, "rho": 0.05, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8049 |
| Legacy p draw | 0.1327 |
| Legacy p away | 0.0623 |
| Legacy p over 1 5 | 0.8271 |
| Legacy p under 3 5 | 0.6018 |
| Legacy p btts yes | 0.4283 |
| Legacy p over 2 5 | 0.6205 |
| Legacy goal margin distribution | {"-1": 0.04818703841027167, "-10": 1.160935133143115e-10, "-11": 6.609793322977628e-12, "-12": 3.456011551534716e-13, "-13": 1.6704301689265635e-14, "-14": 7.505865244574823e-16, "-15": 3.150789635320383e-17, "-16": 1.2407994556831314e-18, "-17": 4.586357536736061e-20, "-18": 1.4818270725637032e-21, "-2": 0.011599109877569408, "-3": 0.0021779526140241604, "-4": 0.00032048064616953855, "-5": 3.8620600006295346e-05, "-6": 3.932747406339998e-06, "-7": 3.463347338118149e-07, "-8": 2.6848960608587056e-08, "-9": 1.8580814269280605e-09, "0": 0.13273403173993933, "1": 0.22386899815608266, "10": 0.0001581963497313078, "11": 3.629868859793258e-05, "12": 7.648790955203059e-06, "13": 1.4899115345610287e-06, "14": 2.6980343317416666e-07, "15": 4.564368167421482e-08, "16": 7.243982711598915e-09, "17": 1.0790914956469226e-09, "18": 1.4050844845190285e-10, "2": 0.22714163995508807, "3": 0.17188384977482143, "4": 0.10193023007268098, "5": 0.04950336996166017, "6": 0.020315445596537213, "7": 0.007210093545327011, "8": 0.0022526145204570217, "9": 0.0006282589655999268} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7923 |
| Legacy raw p draw | 0.1337 |
| Legacy raw p away | 0.0740 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.5546 |
| Legacy lambda away | 0.6339 |
| Legacy model home team | Porto |
| Legacy model away team | Estoril |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 91.4% |
| Market reference home draw last update utc | 2026-10-30T07:27:54Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 23.8% |
| Market reference draw away last update utc | 2026-10-30T07:27:54Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.9% |
| Market reference home away last update utc | 2026-10-30T07:27:54Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 4.00 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 80.4% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:27:54Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 3.68 |
| Market reference over 1 5 last update utc | 2026-10-30T07:27:54Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.4% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:27:54Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market reference under 3 5 last update utc | 2026-10-30T07:27:54Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 32.6% |
| Market reference btts yes odds | 2.60 |
| Market reference btts yes opposite odds | 1.40 |
| Market reference btts yes last update utc | 2026-10-30T07:27:54Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,693.7612 |
| Elo away rating | 1,387.3773 |
| Elo rating diff | 366.3839 |
| Elo home expectancy | 0.8918 |

</details>


---

## 2026-10-31 — Moreirense FC vs CF Estrela

The model's most likely 1X2 outcome is **Moreirense FC win** at **36.9%**. Expected goals are 1.42 for Moreirense FC and 1.07 for CF Estrela (2.49 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 47.9%; Under 3.5 goals: 73.0%; Double Chance 1X: 65.0%; Double Chance X2: 63.1%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 53.5%; BTTS No (at least one team does not score): 46.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Moreirense FC win | 36.9% | 2.71 |
| Draw | 28.1% | 3.56 |
| CF Estrela win | 35.0% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Moreirense FC expected goals | 1.42 |
| CF Estrela expected goals | 1.07 |
| Expected total goals | 2.49 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.2% |
| Under 1.5 | 26.8% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.34% |
| 2 | 0-1 | 10.40% |
| 3 | 1-0 | 8.96% |
| 4 | 1-2 | 8.31% |
| 5 | 0-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Moreirense FC win | 36.9% | 33.0% | 2.89 | +6.5% |
| Draw | 28.1% | 29.3% | 3.24 | -8.9% |
| CF Estrela win | 35.0% | 37.6% | 2.55 | -10.7% |
| Over 2.5 | 47.9% | 47.9% | 2.00 | -4.1% |
| Under 2.5 | 52.1% | 52.1% | 1.85 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:30:00+00:00 |
| Fixture id | 853df01a49c2a57a62c1ac2d356b395b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:27:32Z |
| Market best draw last update utc | 2026-10-30T07:27:32Z |
| Market best away last update utc | 2026-10-30T07:27:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Moreirense |
| Matched away-team name | Estrela |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4765 |
| Dc lambda away | 1.0418 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.2894 |
| Shot lambda away | 1.1237 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.5% |
| P btts no | 46.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.39 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.73 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.08 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.21457286483521895, "-10": 9.78090027426798e-08, "-11": 9.969872945466962e-09, "-12": 9.3336550831711e-10, "-13": 8.076517610192587e-11, "-14": 6.463522685448741e-12, "-15": 4.3908048879142423e-13, "-2": 0.09393785000173592, "-3": 0.03140387251425237, "-4": 0.008244983034133334, "-5": 0.0017749818900565453, "-6": 0.00032313792147476615, "-7": 5.090047516715895e-05, "-8": 7.060522989151849e-06, "-9": 8.74510687219384e-07, "0": 0.28117302314793674, "1": 0.18650448533080527, "10": 1.1317482628516847e-06, "11": 1.5366193506804787e-07, "12": 1.916170238859833e-08, "13": 2.2085750190217328e-09, "14": 2.3543062588456934e-10, "15": 2.130313341741743e-11, "2": 0.10968980731535458, "3": 0.04884437216984305, "4": 0.017081529718696725, "5": 0.00489820085115597, "6": 0.0011877806849458351, "7": 0.00024921595153589164, "8": 4.604649099447904e-05, "9": 7.5967958979915585e-06} |
| Raw goal margin distribution | {"-1": 0.1814419373723393, "-10": 4.99702695087296e-08, "-11": 4.789686749624719e-09, "-12": 4.2148387059840753e-10, "-13": 3.41226196124914e-11, "-14": 2.3453078161443067e-12, "-2": 0.07617683186479549, "-3": 0.024225236643345634, "-4": 0.006023198156867565, "-5": 0.001224824545549808, "-6": 0.00021029342492374911, "-7": 3.120814201079527e-05, "-8": 4.075504906983662e-06, "-9": 4.7499172660251027e-07, "0": 0.2531143381432321, "1": 0.23959002445315372, "10": 8.785538312079695e-07, "11": 1.1216812615854469e-07, "12": 1.3147675658392634e-08, "13": 1.4178035373599677e-09, "14": 1.298013502484552e-10, "2": 0.13515566190686273, "3": 0.05725125795867266, "4": 0.01896050172673777, "5": 0.0051357304742340685, "6": 0.001174518076707058, "7": 0.00023217079750437698, "8": 4.0385621299568265e-05, "9": 6.269559983848528e-06} |
| Unadjusted home-win probability | 45.8% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 28.9% |
| Raw p over 1 5 | 70.4% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 49.1% |
| P home draw | 65.0% |
| P draw away | 63.1% |
| P home away | 71.9% |
| Raw p home draw | 71.1% |
| Raw p draw away | 54.2% |
| Raw p home away | 74.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0650 |
| Totals anchor target over 2 5 | 0.4793 |
| Totals anchor reference over odds | 2.00 |
| Totals anchor reference under odds | 1.85 |
| Totals anchor reference last update utc | 2026-10-30T07:27:32Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4415 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.28, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.28, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.89 |
| Reference draw odds | 3.24 |
| Reference away odds | 2.55 |
| Market reference 1x2 last update utc | 2026-10-30T07:27:32Z |
| Market reference home last update utc | 2026-10-30T07:27:32Z |
| Market reference draw last update utc | 2026-10-30T07:27:32Z |
| Market reference away last update utc | 2026-10-30T07:27:32Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market best over 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market best under 2 5 last update utc | 2026-10-30T07:27:32Z |
| Home probability edge | +3.8% |
| Draw probability edge | -1.2% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1272 |
| Raw ev home | 0.3223 |
| Raw edge prob draw | -0.0401 |
| Raw ev draw | -0.1799 |
| Raw edge prob away | -0.0871 |
| Raw ev away | -0.2622 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.08567948387041507, 0.11081304448420445, 0.0514668211271487, 0.01710327900475499, 0.0042627776445306916, 0.0008499550637820388, 0.00014122708843290359, 2.0113759646625794e-05, 2.5065510813821933e-06, 2.7765617761547205e-07, 2.7680927066114553e-08, 2.508772244933269e-09, 2.0842666559138436e-10, 1.5983917116532354e-11, 1.1382259262756855e-12, 7.5650273948121e-14], [0.11015006340927641, 0.12827379843191478, 0.07541400249148904, 0.02506132489299678, 0.006246220708116059, 0.0012454336967763582, 0.00020693914575824855, 2.94725628450308e-05, 3.672833203150536e-06, 4.0684781402644546e-07, 4.056068467048801e-08, 3.6760878598382103e-09, 3.054062546309087e-10, 2.342113110642599e-11, 1.6678351403901336e-12, 1.1084986061041166e-13], [0.07686934630938642, 0.0766348794067479, 0.04931196347304162, 0.01836109921430057, 0.004576273546024151, 0.0009124629990226101, 0.0001516133006859342, 2.1592978535964767e-05, 2.6908894533133485e-06, 2.980757446127024e-07, 2.9716655388913725e-08, 2.6932739670853074e-09, 2.2375491183680644e-10, 1.7159416503011776e-11, 1.2219340604118512e-12, 8.121379445218057e-14], [0.03754538650427272, 0.03743086555535518, 0.018658346959134788, 0.008004011844552484, 0.002235194746462609, 0.00044567539095839075, 7.405266529171494e-05, 1.054668426147741e-05, 1.314314345256558e-06, 1.455894914728348e-07, 1.4514541436328112e-08, 1.3154790161623393e-09, 1.092888784734798e-10, 8.381194269564168e-12, 5.968307105962235e-13, 3.966735049252455e-14], [0.013753753434577073, 0.013711801731820555, 0.006834988995080039, 0.0022713803032147796, 0.0007307783571435418, 0.00016326132209087464, 2.7127223726398545e-05, 3.86349718009128e-06, 4.814640924825514e-07, 5.333283672961935e-08, 5.317016089539812e-09, 4.818907386823107e-10, 4.003507295083086e-11, 3.070227535352649e-12, 2.186330518874729e-13, 1.4531078485902517e-14], [0.0040306573169539926, 0.0040183630048246845, 0.002003053096404918, 0.0006656477944210978, 0.00016590435883087357, 4.270154658567166e-05, 7.949869344507299e-06, 1.132231521529009e-06, 1.410972485762817e-07, 1.5629652634147508e-08, 1.5581979063102747e-09, 1.4122228096362165e-10, 1.173262706007026e-11, 8.997569382748868e-13, 6.407232138557838e-14, 4.258459198140826e-15], [0.0009843493804554014, 0.0009813469176866846, 0.0004891768065153926, 0.00016256157309227067, 4.0516431933596965e-05, 8.07856974020806e-06, 1.732762501128529e-06, 2.765085962682146e-07, 3.445814870835619e-08, 3.817004939229827e-09, 3.8053623096456603e-10, 3.4488683567396984e-11, 2.8652905145561057e-12, 2.1973467727607443e-13, 1.5647460178504015e-14, 1.0399821527254819e-15], [0.00020605154656479712, 0.00020542304807708432, 0.00010239823331782143, 3.402863273218296e-05, 8.48120964666289e-06, 1.6910680517026666e-06, 2.8098499257263596e-07, 5.165839366198809e-08, 7.2130434316235685e-09, 7.990046893816376e-10, 7.965675650439472e-11, 7.219435222032967e-12, 5.997845415502638e-13, 4.5996544505066734e-14, 3.2754461308241868e-15, 2.1769702427174085e-16], [3.7740750996703445e-05, 3.7625634146953834e-05, 1.875543421332653e-05, 6.232742127464331e-06, 1.5534327539001768e-06, 3.097388945718035e-07, 5.146568815080255e-08, 7.3298153562462195e-09, 1.1791223197237996e-09, 1.4634705504463614e-10, 1.4590066721445373e-11, 1.3223240086960176e-12, 1.09857554634767e-13, 8.4248051607252e-15, 5.999362726825115e-16, 3.987375645918471e-17], [6.144586674943197e-06, 6.12584445486669e-06, 3.053579701157676e-06, 1.0147552238194636e-06, 2.5291500428460185e-07, 5.04287125728839e-08, 8.379149149836093e-09, 1.1933701523776927e-09, 1.4871626679865082e-10, 2.1265312937261866e-11, 2.3754145637153877e-12, 2.1528809759245998e-13, 1.7885952147841353e-14, 1.3716458777968263e-15, 9.767586308131607e-17, 6.491862142341507e-18], [9.003623395906591e-07, 8.976160541185993e-07, 4.4743907268364565e-07, 1.4869143129767651e-07, 3.7059473162590015e-08, 7.389286869337938e-09, 1.2277913440606236e-09, 1.748637620775971e-10, 2.179129907240827e-11, 2.413870138399105e-12, 3.1064882469932214e-13, 3.154602668798081e-14, 2.620817082344417e-15, 2.0098638963937312e-16, 1.4312381492485595e-17, 9.51248390817542e-19], [1.1993592311970225e-07, 1.195700945318568e-07, 5.960269089723857e-08, 1.9806963583999328e-08, 4.9366370944678036e-09, 9.843158725111282e-10, 1.6355225199139213e-10, 2.3293340694920123e-11, 2.902786417538328e-12, 3.2154803750632533e-13, 3.205672515880978e-14, 3.7504405122856615e-15, 3.4911513096135213e-16, 2.6773096914353055e-17, 1.9065309718785248e-18, 1.2671437803662754e-19], [1.4645111495914021e-08, 1.4600440972537614e-08, 7.277953351602348e-09, 2.4185847120521923e-09, 6.028018860636882e-10, 1.2019264391483473e-10, 1.9971005379524112e-11, 2.8442985447233158e-12, 3.544528580585889e-13, 3.9263522871896743e-14, 3.914376126292718e-15, 3.5476695409865848e-16, 3.8046764122253576e-17, 3.2692039149128086e-18, 2.3280229915525275e-19, 1.547281370094328e-20], [1.650722140614201e-09, 1.6456871074571755e-09, 8.203337160798805e-10, 2.726105113129017e-10, 6.794474866285243e-11, 1.3547500714114137e-11, 2.2510296872443355e-12, 3.205947994046664e-13, 3.995211513169694e-14, 4.425583686490531e-15, 4.4120847698331327e-16, 3.99875184325026e-17, 3.3221290410051647e-18, 3.2887355890276176e-19, 2.624028568909725e-20, 1.744016504133263e-21], [1.7277089658193683e-10, 1.722439107425542e-10, 8.585926615776664e-11, 2.853245939965741e-11, 7.111357420908867e-12, 1.4179332712839445e-12, 2.3560138180072757e-13, 3.355467862813125e-14, 4.1815412671933625e-15, 4.631985254216468e-16, 4.6178567714367094e-17, 4.185246712144792e-18, 3.477067392830816e-19, 2.6665089545002227e-20, 2.451155273696342e-21, 1.8253544170715823e-22], [1.6877339018210016e-11, 1.6825859753790973e-11, 8.387268755719674e-12, 2.7872286353677304e-12, 6.946817574418418e-13, 1.3851256778834508e-13, 2.3015012785581268e-14, 3.2778303409769145e-15, 4.084790377387919e-16, 4.5248121650909054e-17, 4.511010581699003e-18, 4.0884100871825567e-19, 3.3966163479471504e-20, 2.6048122982825414e-21, 1.8549050707478636e-22, 1.5914252414003563e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4652935782681984, "lambda_away": 0.9969497997069622, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T07:27:32Z", "over": 2.0, "under": 1.85, "bookmaker": "pinnacle", "event_id": "853df01a49c2a57a62c1ac2d356b395b", "kickoff_utc": "2026-10-31T15:30:00Z", "home_team": "Moreirense FC", "away_team": "CF Estrela"}} |
| Legacy p home | 0.4081 |
| Legacy p draw | 0.2720 |
| Legacy p away | 0.3199 |
| Legacy p over 1 5 | 0.6934 |
| Legacy p under 3 5 | 0.7700 |
| Legacy p btts yes | 0.4861 |
| Legacy p over 2 5 | 0.4367 |
| Legacy goal margin distribution | {"-1": 0.2069948359982861, "-10": 3.1589373923570225e-08, "-11": 2.8319492778562717e-09, "-12": 2.331093981087147e-10, "-13": 1.773296605137467e-11, "-14": 1.2490757868860972e-12, "-15": 7.5650273948121e-14, "-2": 0.08157838968433735, "-3": 0.024340023869616152, "-4": 0.005670868807866487, "-5": 0.001079856428553136, "-6": 0.00017354159137298458, "-7": 2.40996769822411e-05, "-8": 2.944471980508761e-06, "-9": 3.210225604713577e-07, "0": 0.27204452314525, "1": 0.20788894147291545, "10": 1.02749024785542e-06, "11": 1.3538592494947683e-07, "12": 1.637944509816433e-08, "13": 1.8313533201124748e-09, "14": 1.895967563357278e-10, "15": 1.6877339018210016e-11, "2": 0.12184310883540314, "3": 0.05343160241108712, "4": 0.018296926991559413, "5": 0.005120895680814087, "6": 0.0012095806820544939, "7": 0.0002468845109589375, "8": 4.4334458076103775e-05, "9": 7.104293390368034e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4858 |
| Legacy raw p draw | 0.2509 |
| Legacy raw p away | 0.2633 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4653 |
| Legacy lambda away | 0.9969 |
| Legacy model home team | Moreirense |
| Legacy model away team | Estrela |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 61.9% |
| Market reference home draw last update utc | 2026-10-30T07:27:40Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 66.8% |
| Market reference draw away last update utc | 2026-10-30T07:27:40Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.3% |
| Market reference home away last update utc | 2026-10-30T07:27:40Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.51 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 75.5% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:27:32Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.59 |
| Market reference over 1 5 last update utc | 2026-10-30T07:27:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 74.5% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:27:32Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.50 |
| Market reference under 3 5 last update utc | 2026-10-30T07:27:32Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.3% |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.14 |
| Market reference btts yes last update utc | 2026-10-30T07:27:32Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,438.8922 |
| Elo away rating | 1,379.1640 |
| Elo rating diff | 119.7282 |
| Elo home expectancy | 0.6658 |

</details>


---

## 2026-11-01 — Académico de Viseu vs Rio Ave FC

The model's most likely 1X2 outcome is **Académico de Viseu win** at **53.6%**. Expected goals are 2.00 for Académico de Viseu and 0.93 for Rio Ave FC (2.93 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.5%; Under 3.5 goals: 69.9%; Double Chance 1X: 77.8%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 85.4%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Académico de Viseu win | 53.6% | 1.87 |
| Draw | 24.2% | 4.13 |
| Rio Ave FC win | 22.2% | 4.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Académico de Viseu expected goals | 2.00 |
| Rio Ave FC expected goals | 0.93 |
| Expected total goals | 2.93 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.49% |
| 2 | 1-0 | 10.42% |
| 3 | 2-0 | 9.57% |
| 4 | 2-1 | 8.54% |
| 5 | 0-1 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Académico de Viseu win | 53.6% | 49.7% | 1.95 | +4.5% |
| Draw | 24.2% | 26.0% | 3.61 | -12.6% |
| Rio Ave FC win | 22.2% | 24.3% | 3.86 | -14.4% |
| Over 2.5 | 51.5% | 51.5% | 1.86 | -4.1% |
| Under 2.5 | 48.5% | 48.5% | 1.97 | -4.5% |

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
| Market best home last update utc | 2026-10-30T07:27:32Z |
| Market best draw last update utc | 2026-10-30T07:27:32Z |
| Market best away last update utc | 2026-10-30T07:27:32Z |
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
| Dc lambda home | 2.1615 |
| Dc lambda away | 0.7701 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6276 |
| Shot lambda away | 1.3047 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.50 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.11 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.86 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.15267330935142454, "-10": 7.899201056449569e-09, "-11": 6.3282916189033e-10, "-12": 4.656310690682461e-11, "-13": 3.167352773596719e-12, "-14": 2.0027287848313562e-13, "-15": 1.1776031448749513e-14, "-16": 5.933803402836238e-16, "-2": 0.05207343320773493, "-3": 0.013685538380176325, "-4": 0.0028244169728963106, "-5": 0.00047793502184882497, "-6": 6.838857796661597e-05, "-7": 8.466973815113429e-06, "-8": 9.230964717883869e-07, "-9": 8.986161751963395e-08, "0": 0.24222179186010453, "1": 0.21782242220226197, "10": 1.1360001395823872e-05, "11": 1.957390523155517e-06, "12": 3.097624200384238e-07, "13": 4.531886195138422e-08, "14": 6.1631179420628255e-09, "15": 7.794227469437678e-10, "16": 8.447010873935853e-11, "2": 0.16354797991260395, "3": 0.09244568397701634, "4": 0.04103451892360808, "5": 0.014934310268579654, "6": 0.00459616560070553, "7": 0.0012238722616499211, "8": 0.00028697941552292957, "9": 6.008605181011914e-05} |
| Raw goal margin distribution | {"-1": 0.11751530445473819, "-10": 8.457046841938225e-09, "-11": 7.055667617411247e-10, "-12": 5.407298209018649e-11, "-13": 3.831596838148252e-12, "-14": 2.5244676391276976e-13, "-15": 1.5537657882726557e-14, "-16": 8.929902410221086e-16, "-17": 4.405326435701819e-17, "-2": 0.04118029816392689, "-3": 0.011178391840393532, "-4": 0.0023903565603877863, "-5": 0.0004198646254243121, "-6": 6.243404393288753e-05, "-7": 8.03872816538623e-06, "-8": 9.119086923808938e-07, "-9": 9.240266794205e-08, "0": 0.19960071190233797, "1": 0.247038378989138, "10": 1.791333886042812e-05, "11": 3.214339161092361e-06, "12": 5.298216339576969e-07, "13": 8.074673174155224e-08, "14": 1.1442231635155739e-08, "15": 1.5146847838675433e-09, "16": 1.872316226947143e-10, "17": 1.9865813970197657e-11, "2": 0.19049388885713692, "3": 0.11121584621169862, "4": 0.051150020247003186, "5": 0.019323606653196556, "6": 0.006180109198195708, "7": 0.0017114247436133153, "8": 0.0004175587604657683, "9": 9.100107769641151e-05} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 20.0% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 51.9% |
| P home draw | 77.8% |
| P draw away | 46.4% |
| P home away | 75.8% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9592 |
| Totals anchor target over 2 5 | 0.5153 |
| Totals anchor reference over odds | 1.86 |
| Totals anchor reference under odds | 1.97 |
| Totals anchor reference last update utc | 2026-10-30T07:27:32Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5408 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 3.61 |
| Reference away odds | 3.86 |
| Market reference 1x2 last update utc | 2026-10-30T07:27:32Z |
| Market reference home last update utc | 2026-10-30T07:27:32Z |
| Market reference draw last update utc | 2026-10-30T07:27:32Z |
| Market reference away last update utc | 2026-10-30T07:27:32Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market best over 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market best under 2 5 last update utc | 2026-10-30T07:27:32Z |
| Home probability edge | +3.9% |
| Draw probability edge | -1.8% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1310 |
| Raw ev home | 0.2239 |
| Raw edge prob draw | -0.0609 |
| Raw ev draw | -0.2794 |
| Raw edge prob away | -0.0701 |
| Raw ev away | -0.3332 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.062089265481450606, 0.068563059903933, 0.02410332807302977, 0.00624435272697797, 0.0012132746003200353, 0.00018859091664338474, 2.4428746956796604e-05, 2.712281869140593e-06, 2.6349750283320613e-07, 2.2754414457942195e-08, 1.7684685227791217e-09, 1.2495001681546644e-10, 8.092575181667917e-12, 4.838102447686381e-13, 2.6858310770322822e-14, 1.3916150134333373e-15, 6.759752463726648e-17, 3.0903917892956033e-18], [0.10542918172862416, 0.10524650347631842, 0.050804163425067946, 0.01316163126784677, 0.0025572983484846634, 0.0003975054283211079, 5.149007012236727e-05, 5.716854158777033e-06, 5.553909466558077e-07, 4.796096984036584e-08, 3.727516945839981e-09, 2.633653350700963e-10, 1.705725080011435e-11, 1.0197585440265876e-12, 5.661102091638356e-14, 2.933198119074453e-15, 1.4247973053333057e-16, 6.513821204904115e-18], [0.10695378287519844, 0.08312426529653989, 0.045370967689010125, 0.013870816176218622, 0.002695092620185628, 0.0004189241145784793, 5.4264496781089885e-05, 6.0248939913980865e-06, 5.853169390802325e-07, 5.054523886519087e-08, 3.928365815550227e-09, 2.775561840020437e-10, 1.797634240810572e-11, 1.0747059403553122e-12, 5.9661378494741e-14, 3.0912469047439078e-15, 1.5015693046294514e-16, 6.864803814912023e-18], [0.07514449799432202, 0.05840215295745091, 0.02269501800599704, 0.008258277932668891, 0.0018935410842678456, 0.00029433126572482875, 3.8125611454880826e-05, 4.233021238537246e-06, 4.112369508807393e-07, 3.551250361064721e-08, 2.7600246500119833e-09, 1.9500778328140597e-10, 1.2629971467277472e-11, 7.550760357279777e-13, 4.1917398488540676e-14, 2.171874529249106e-15, 1.0549853269961205e-16, 4.823132222475993e-18], [0.0395967451572586, 0.03077451082933786, 0.011958944011985582, 0.0030981557578588907, 0.0008455192011855741, 0.00015509532210329, 2.008996215341868e-05, 2.2305540352440375e-06, 2.166977646787009e-07, 1.8713007510852958e-08, 1.454371186331356e-09, 1.0275766961486922e-10, 6.655254541337436e-12, 3.978808051034285e-13, 2.208801162969266e-14, 1.1444505525170453e-15, 5.559154196607847e-17, 2.5415079289980063e-18], [0.01669213069643347, 0.012973090460894824, 0.0050413299286747254, 0.0013060371660019764, 0.0002537623657514038, 5.5403528950880104e-05, 8.468985837584522e-06, 9.402969697100296e-07, 9.134961460282525e-08, 7.888526338565461e-09, 6.130946830845714e-10, 4.331781424105008e-11, 2.805543187472634e-12, 1.6772788707788863e-13, 9.311269789546973e-15, 4.82446678946745e-16, 2.343478688535449e-17, 1.0713805477791894e-18], [0.005863849542856942, 0.004557372090599187, 0.0017709902189998186, 0.0004588033474031688, 8.914526009094837e-05, 1.3856703429322814e-05, 2.5210931341776323e-06, 3.303209192558038e-07, 3.209059439867594e-08, 2.7711939479419224e-09, 2.15376637201962e-10, 1.5217299088678743e-11, 9.855711913903167e-13, 5.892184238505779e-14, 3.270995542259849e-15, 1.6948074450430575e-16, 8.232505895367645e-18, 3.7636982657122087e-19], [0.0017656599689274317, 0.001372267382555934, 0.0005332617271633658, 0.0001381499812024499, 2.6842471999294235e-05, 4.172383068091904e-06, 5.404612904553433e-07, 8.428431701082803e-08, 9.662778264468052e-09, 8.344324294567588e-10, 6.485192087047187e-11, 4.5820711530373324e-12, 2.9676470831107976e-13, 1.7741918109321162e-14, 9.849273664505406e-16, 5.103223810368681e-17, 2.4788845616130363e-18, 1.1332847669982885e-19], [0.0004651996466146818, 0.0003615522312677589, 0.00014049883408764555, 3.6398470581085024e-05, 7.072204562649507e-06, 1.0993006371416524e-06, 1.4239570798077828e-07, 1.5809951189176707e-08, 2.157350750740476e-09, 2.1984848619687352e-10, 1.7086580203522054e-11, 1.207241438707558e-12, 7.818880184381495e-14, 4.674475368967289e-15, 2.5949949077242294e-16, 1.344549887836706e-17, 6.531134206783224e-19, 2.985873171501198e-20], [0.00010894797413815949, 8.467414674194743e-05, 3.2904288414692176e-05, 8.52438229563233e-06, 1.6562832009834003e-06, 2.5745199562580907e-07, 3.334852900979209e-08, 3.7026299693444918e-09, 3.597095722012112e-10, 4.3630451133872504e-11, 4.001611591216023e-12, 2.8273131761806124e-13, 1.8311517696034255e-14, 1.0947442142610582e-15, 6.077378608362688e-17, 3.1488843010414174e-18, 1.5295665975491102e-19, 6.992800519858995e-21], [2.2963678153385315e-05, 1.784732455170597e-05, 6.93545240284099e-06, 1.7967398938972472e-06, 3.4910565945915947e-07, 5.426484351146025e-08, 7.029087902989035e-09, 7.80427572056387e-10, 7.581834274628649e-11, 6.547318193961671e-12, 7.14732722552601e-13, 5.959313179546012e-14, 3.859638531125919e-15, 2.3074640896664887e-16, 1.2809688980699311e-17, 6.637109703358488e-19, 3.2239677091878955e-20, 1.4739183706640719e-21], [4.400186239881519e-06, 3.4198159104376333e-06, 1.328937029446882e-06, 3.4428239696467536e-07, 6.68938969078218e-08, 1.0397960471905105e-08, 1.3468790000912975e-09, 1.4954166492184576e-10, 1.4527935213795393e-11, 1.254564675256475e-12, 9.750451465505795e-14, 9.67636535310421e-15, 7.395648137087796e-16, 4.421448371011251e-17, 2.4545291400422137e-18, 1.2717700794372432e-19, 6.177607200830589e-21, 2.824249360222173e-22], [7.72880063679578e-07, 6.006808336145885e-07, 2.3342396888471514e-07, 6.047221330726694e-08, 1.1749720689841654e-08, 1.8263718655417966e-09, 2.36575424450052e-10, 2.62665635513324e-11, 2.5517900563848197e-12, 2.203606786717469e-13, 1.712638769982534e-14, 1.2100540119981814e-15, 1.1007881049027424e-16, 7.766146958895896e-18, 4.311309873352739e-19, 2.233827584551751e-20, 1.0850789458616022e-21, 4.960712811633845e-23], [1.253115335652631e-07, 9.739187227206215e-08, 3.784638378764125e-08, 9.804711162482485e-09, 1.905050457114623e-09, 2.9612027801816414e-10, 3.835734758191356e-11, 4.258750503197744e-12, 4.137365424847357e-13, 3.572835667460938e-14, 2.77680070680167e-15, 1.9619308488613828e-16, 1.2706739302878598e-17, 1.0670161322502615e-18, 6.990177095949427e-20, 3.621834402195409e-21, 1.7593015156575235e-22, 8.043091796716388e-24], [1.886623768601084e-08, 1.4662802047773145e-08, 5.6979501549373424e-09, 1.4761451398066273e-09, 2.868142596710756e-10, 4.4582293343562955e-11, 5.77487814486308e-12, 6.411748141036182e-13, 6.228997226213107e-14, 5.379071263242481e-15, 4.180603385076226e-16, 2.953778687805985e-17, 1.913059054356167e-18, 1.1437120429125937e-19, 8.918028922361025e-21, 5.452841150938643e-22, 2.648710746043791e-23, 1.2109251020236426e-24], [2.651040331338466e-09, 2.0603832224536155e-09, 8.006628517086772e-10, 2.0742452022844608e-10, 4.0302480157705366e-11, 6.264601330925897e-12, 8.114725959351665e-13, 9.009641031330313e-14, 8.75284364869996e-15, 7.558547232007651e-16, 5.874487731798855e-17, 4.1505818815311515e-18, 2.688186586926642e-19, 1.607117859777108e-20, 8.92177695473796e-22, 6.492924017600449e-23, 3.72190742567519e-24, 1.7015641046837698e-25], [3.492357098771065e-10, 2.7142529248099944e-10, 1.0547559615870985e-10, 2.7325140516185905e-11, 5.309261085657632e-12, 8.252694110460317e-13, 1.0689962153240981e-13, 1.1868881601382274e-14, 1.153058868611676e-15, 9.957278193791504e-17, 7.738776618850298e-18, 5.467783317607032e-19, 3.541291846335102e-20, 2.1171422402769037e-21, 1.175313355787388e-22, 6.0896745345939245e-24, 4.1548401294133145e-25, 2.2415613258535916e-26], [4.3300410692392326e-11, 3.3652992246599624e-11, 1.3077519000861041e-11, 3.3879405029758688e-12, 6.582751390543938e-13, 1.0232202326255986e-13, 1.3254078504295824e-14, 1.471577600068672e-15, 1.4296339449639922e-16, 1.2345651460479069e-17, 9.595015526070276e-19, 6.779297091718055e-20, 4.390713406194608e-21, 2.6249643408590883e-22, 1.4572264392938532e-23, 7.550356417552745e-25, 3.6675761545318647e-26, 2.3551058818296003e-27]] |
| Legacy trial inputs | {"lambda_home": 2.107765503217577, "lambda_away": 0.7771979920853798, "rho": 0.05, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T07:27:32Z", "over": 1.86, "under": 1.97, "bookmaker": "pinnacle", "event_id": "ce5c2cbdf5db2a13f40f528d3e5044b9", "kickoff_utc": "2026-11-01T18:00:00Z", "home_team": "Acad\u00e9mico de Viseu", "away_team": "Rio Ave FC"}} |
| Legacy p home | 0.5913 |
| Legacy p draw | 0.2219 |
| Legacy p away | 0.1868 |
| Legacy p over 1 5 | 0.7639 |
| Legacy p under 3 5 | 0.6877 |
| Legacy p btts yes | 0.4855 |
| Legacy p over 2 5 | 0.5276 |
| Legacy goal margin distribution | {"-1": 0.13529548510503622, "-10": 2.0505878550971947e-09, "-11": 1.4312505921613387e-10, "-12": 9.17422364164101e-12, "-13": 5.436205526303942e-13, "-14": 2.99464889520827e-14, "-15": 1.54095954778158e-15, "-16": 7.411134584217059e-17, "-17": 3.0903917892956033e-18, "-2": 0.040275446428310165, "-3": 0.009261025542417494, "-4": 0.0016695023529897928, "-5": 0.00024653645932902447, "-6": 3.076792925084088e-05, "-7": 3.3210837024447755e-06, "-8": 3.1558867257751986e-07, "-9": 2.6772524923315876e-08, "0": 0.22186854488874141, "1": 0.21461479649579798, "10": 2.6627015931102345e-05, "11": 5.040230743427203e-06, "12": 8.761827222099148e-07, "13": 1.4080298188040015e-07, "14": 2.103548444512614e-08, "15": 2.9355431428203264e-09, "16": 3.828887021237061e-10, "17": 4.3300410692392326e-11, "2": 0.1787143808292241, "3": 0.1114471180160819, "4": 0.05448631265613148, "5": 0.02182087490638634, "6": 0.007385499886313312, "7": 0.0021619819877799294, "8": 0.0005571655798635427, "9": 0.0001281866583888545} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6860 |
| Legacy raw p draw | 0.1832 |
| Legacy raw p away | 0.1307 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1078 |
| Legacy lambda away | 0.7772 |
| Legacy model home team | Academico Viseu |
| Legacy model away team | Rio Ave |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,418.3104 |
| Elo away rating | 1,393.4483 |
| Elo rating diff | 84.8621 |
| Elo home expectancy | 0.6198 |

</details>


---

## 2026-11-01 — Arouca vs Nacional

The model's most likely 1X2 outcome is **Arouca win** at **52.7%**. Expected goals are 1.58 for Arouca and 1.14 for Nacional (2.71 combined). The most likely exact score is 1-0 at 11.7%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 51.9%; Under 3.5 goals: 69.9%; Double Chance 1X: 77.0%; Double Chance X2: 47.3%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 85.4%; BTTS Yes (both teams score): 54.2%; BTTS No (at least one team does not score): 45.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arouca win | 52.7% | 1.90 |
| Draw | 24.4% | 4.10 |
| Nacional win | 23.0% | 4.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arouca expected goals | 1.58 |
| Nacional expected goals | 1.14 |
| Expected total goals | 2.71 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.74% |
| 2 | 1-1 | 11.52% |
| 3 | 2-1 | 10.26% |
| 4 | 2-0 | 8.89% |
| 5 | 0-1 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arouca win | 52.7% | 54.6% | 1.78 | -6.3% |
| Draw | 24.4% | 24.6% | 3.81 | -7.2% |
| Nacional win | 23.0% | 20.8% | 4.47 | +2.7% |
| Over 2.5 | 51.9% | 51.9% | 1.85 | -3.9% |
| Under 2.5 | 48.1% | 48.1% | 1.99 | -4.4% |

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
| Market best home last update utc | 2026-10-30T07:27:32Z |
| Market best draw last update utc | 2026-10-30T07:27:32Z |
| Market best away last update utc | 2026-10-30T07:27:32Z |
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
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6115 |
| Shot lambda away | 1.2948 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.2% |
| P btts no | 45.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.79 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.86 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.14035413726031595, "-10": 7.104145019404361e-08, "-11": 7.351718197304259e-09, "-12": 6.988398011510423e-10, "-13": 6.140506181302012e-11, "-14": 4.986751117342832e-12, "-15": 3.4160305128874954e-13, "-2": 0.0616011660620233, "-3": 0.020758249879761614, "-4": 0.005508718891607621, "-5": 0.001200591869468826, "-6": 0.0002214914507318693, "-7": 3.5378546936879215e-05, "-8": 4.9785035902593526e-06, "-9": 6.257642443276037e-07, "0": 0.24366235075681106, "1": 0.2568987825414097, "10": 2.4943850106608554e-06, "11": 3.580330444811877e-07, "12": 4.720570429830336e-08, "13": 5.753122390029305e-09, "14": 6.480368824886472e-10, "15": 6.15724396675311e-11, "2": 0.157899182549162, "3": 0.07380134457325958, "4": 0.02716481425991912, "5": 0.008211719705409804, "6": 0.0021012526632099484, "7": 0.0004655259456568095, "8": 9.086263228642817e-05, "9": 1.584089896244563e-05} |
| Raw goal margin distribution | {"-1": 0.1723864871292115, "-10": 7.693639581159535e-08, "-11": 7.839314711419466e-09, "-12": 7.336841381437344e-10, "-13": 6.346963200176458e-11, "-14": 5.076213821684232e-12, "-15": 3.4341918615642407e-13, "-2": 0.07489015260601108, "-3": 0.024927484532327245, "-4": 0.006526196894793781, "-5": 0.0014022355241978487, "-6": 0.00025492256793152324, "-7": 4.011358451840542e-05, "-8": 5.55985632384623e-06, "-9": 6.882184138312408e-07, "0": 0.23851694270122747, "1": 0.23680238276324558, "10": 2.0274854158082213e-06, "11": 2.865408807046289e-07, "12": 3.71963402602463e-08, "13": 4.463131185490308e-09, "14": 4.951036972304537e-10, "15": 4.645830994485005e-11, "2": 0.14407542052818162, "3": 0.06651601551125409, "4": 0.024154081808832467, "5": 0.007198365860415947, "6": 0.001815113661746254, "7": 0.00039615906958631597, "8": 7.615953610805564e-05, "9": 1.3075840059198024e-05} |
| Unadjusted home-win probability | 48.1% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 28.0% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 53.2% |
| P home draw | 77.0% |
| P draw away | 47.3% |
| P home away | 75.6% |
| Raw p home draw | 72.0% |
| Raw p draw away | 51.9% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0160 |
| Totals anchor target over 2 5 | 0.5194 |
| Totals anchor reference over odds | 1.85 |
| Totals anchor reference under odds | 1.99 |
| Totals anchor reference last update utc | 2026-10-30T07:27:32Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5096 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.78 |
| Reference draw odds | 3.81 |
| Reference away odds | 4.47 |
| Market reference 1x2 last update utc | 2026-10-30T07:27:32Z |
| Market reference home last update utc | 2026-10-30T07:27:32Z |
| Market reference draw last update utc | 2026-10-30T07:27:32Z |
| Market reference away last update utc | 2026-10-30T07:27:32Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market best over 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market best under 2 5 last update utc | 2026-10-30T07:27:32Z |
| Home probability edge | -2.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0651 |
| Raw ev home | -0.1437 |
| Raw edge prob draw | -0.0074 |
| Raw ev draw | -0.0913 |
| Raw edge prob away | 0.0725 |
| Raw ev away | 0.2535 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06954842278800315, 0.07615118333332463, 0.037482670286186945, 0.013237851174654622, 0.0035064344879442346, 0.0007430258978457222, 0.00013120818473571466, 1.9859628186644942e-05, 2.6302035078294383e-06, 3.0963858168639124e-07, 3.2806756543752277e-08, 3.159940003304531e-09, 2.790010367804461e-10, 2.2738964890714184e-11, 1.720881166782246e-12, 1.215536065130584e-13], [0.12854960498889104, 0.1161837346101533, 0.05718187899066363, 0.020195071433970663, 0.005349259032172167, 0.0011335269513389166, 0.00020016531599423347, 3.029695715640615e-05, 4.012520387613557e-06, 4.7237071888543715e-07, 5.004851491203198e-08, 4.8206626024001545e-09, 4.256314558605083e-10, 3.468954396327884e-11, 2.6252990484650137e-12, 1.8543672490350552e-13], [0.09312155608562442, 0.09866393919122934, 0.04941944473067888, 0.015404347157340606, 0.004080294711288299, 0.0008646289134315509, 0.0001526816097935291, 2.3109838822520763e-05, 3.0606604798997375e-06, 3.6031378073928107e-07, 3.817588370187286e-08, 3.677093220421479e-09, 3.2466212009186443e-10, 2.6460405435422177e-11, 2.0025191822973265e-12, 1.4144697113221497e-13], [0.04735402174617554, 0.05017242535905253, 0.026579286970625685, 0.008875472397804922, 0.0020749048084150205, 0.0004396796841685341, 7.764140306843523e-05, 1.17517775277082e-05, 1.556402072894553e-06, 1.83226175826422e-07, 1.9413138085189605e-08, 1.8698694442181234e-09, 1.6509665152989168e-10, 1.3455602194291886e-11, 1.0183177868983244e-12, 7.192838294891403e-14], [0.018060292400038366, 0.019135199904679066, 0.01013704172893823, 0.0035801251280755285, 0.0008966183458017203, 0.0001676888966475496, 2.961155969563292e-05, 4.4819960489998145e-06, 5.935942817944842e-07, 6.988040695895648e-08, 7.403952975739836e-09, 7.131472189097422e-10, 6.296600987513583e-11, 5.131815653379763e-12, 3.8837497448733647e-13, 2.7432677944070015e-14], [0.005510394252437097, 0.0058383603785813806, 0.0030929231511078736, 0.001092335632877744, 0.00028933724099167065, 5.797005838982786e-05, 9.034813210010212e-06, 1.3675063903063876e-06, 1.8111215733544292e-07, 2.1321282310123683e-08, 2.2590276513321933e-09, 2.175890760336414e-10, 1.921162355677635e-11, 1.565773513217898e-12, 1.1849748496878581e-13, 8.37001237430908e-15], [0.0014010683467315318, 0.0014844567463796496, 0.000786404116905763, 0.0002777363667862952, 7.35666508262587e-05, 1.5589034094212038e-05, 2.6027794117375788e-06, 3.47701059060156e-07, 4.604942935593458e-08, 5.421131844283088e-09, 5.74378527502455e-10, 5.532402094286911e-11, 4.884731730913197e-12, 3.9811229596684194e-13, 3.01290738468729e-14, 2.1281525172557604e-15], [0.0003053438526152926, 0.0003235172238654383, 0.00017138611640802728, 6.0528876013606375e-05, 1.6032854242761748e-05, 3.397418648406558e-06, 5.999375458340307e-07, 8.585733589695662e-08, 1.003584885996366e-08, 1.1814621939967568e-09, 1.2517801351821184e-10, 1.2057120365521854e-11, 1.0645610609851307e-12, 8.676317790464528e-14, 6.566223200742717e-15, 4.6380199087912375e-16], [5.8227359128496665e-05, 6.169291903839586e-05, 3.268237059385534e-05, 1.1542516972591543e-05, 3.0573753290010545e-06, 6.478686702098444e-07, 1.144047231891037e-07, 1.7316261709649207e-08, 2.168370849362085e-09, 2.2529821012399631e-10, 2.3870744688939203e-11, 2.2992251901114275e-12, 2.0300582009847267e-13, 1.6545251118412092e-14, 1.2521419152630566e-15, 8.844443684103147e-17], [9.869893883137331e-06, 1.0457327506580168e-05, 5.5398619212467885e-06, 1.9565272986601177e-06, 5.182438377734064e-07, 1.0981770633061434e-07, 1.9392301050684922e-08, 2.9352123827169795e-09, 3.887386930253927e-10, 4.3269778000675235e-11, 4.046237379087827e-12, 3.897327472770436e-13, 3.4410729458114856e-14, 2.8045213668065382e-15, 2.1224572117381867e-16, 1.4991873566658193e-17], [1.505706699568398e-06, 1.5953229358564887e-06, 8.451364632963685e-07, 2.9847902078401783e-07, 7.906095321639014e-08, 1.6753296247262205e-08, 2.9584023858605133e-09, 4.477828233659015e-10, 5.930422975163128e-11, 6.98154250560363e-12, 6.993922132418443e-13, 5.945587820542089e-14, 5.249546397924349e-15, 4.278451887206139e-16, 3.237925433749044e-17, 2.287092924774612e-18], [2.088216856016857e-07, 2.2125027712241296e-07, 1.1720929506362868e-07, 4.139510852593363e-08, 1.096471279609435e-08, 2.32346150996107e-09, 4.102914419392061e-10, 6.210157926875972e-11, 8.224715493126974e-12, 9.682479825173549e-13, 1.0258758990376252e-13, 9.342681596946011e-15, 7.280429367638765e-16, 5.933649196807031e-17, 4.490576067183994e-18, 3.1718966237981374e-19], [2.654741570244722e-08, 2.8127457472275718e-08, 1.490076986630658e-08, 5.262543259908473e-09, 1.3939394647502517e-09, 2.95380713913145e-10, 5.2160183636735595e-11, 7.89494843830977e-12, 1.0456047253965721e-12, 1.2309297102396616e-13, 1.3041918454207594e-14, 1.2561948874258498e-15, 1.0486853035160036e-16, 7.54342401778107e-18, 5.708851035058962e-19, 4.032419238190377e-20], [3.1153496569147587e-09, 3.3007681790307343e-09, 1.7486111948171566e-09, 6.175615179651414e-10, 1.6357934353924037e-10, 3.466304276328202e-11, 6.121018031232907e-12, 9.264752993030791e-13, 1.2270212509733603e-13, 1.4445008483924902e-14, 1.5304742517020394e-15, 1.4741496330279101e-16, 1.3015730537737817e-17, 1.0029853806487689e-18, 6.699359106283524e-20, 4.732059809902635e-21], [3.3947411227482214e-10, 3.596788389111789e-10, 1.9054305244896386e-10, 6.729458044010637e-11, 1.78249501821494e-11, 3.777170130707847e-12, 6.669964502247287e-13, 1.0095636586967826e-13, 1.3370632378037449e-14, 1.5740468878023136e-15, 1.6677305765753364e-16, 1.6063546411930016e-17, 1.4183010116054326e-18, 1.1559346617317172e-19, 8.271316840927477e-21, 5.156441427473497e-22], [3.4525764324952424e-11, 3.658065924881692e-11, 1.937892842115812e-11, 6.84410604700471e-12, 1.8128629160231608e-12, 3.841520782665612e-13, 6.783598929451213e-14, 1.0267633286565334e-14, 1.359842431772778e-15, 1.6008635097539404e-16, 1.6961432628401223e-17, 1.6337216818237024e-18, 1.4424642321146616e-19, 1.1756280158907673e-20, 8.897133714798828e-22, 5.9419400371836e-23]] |
| Legacy trial inputs | {"lambda_home": 1.5255551046408828, "lambda_away": 1.059517724344176, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T07:27:32Z", "over": 1.85, "under": 1.99, "bookmaker": "pinnacle", "event_id": "fd5c6a92f2448c1cfe7a2d9b8075172b", "kickoff_utc": "2026-11-01T15:30:00Z", "home_team": "Arouca", "away_team": "Nacional"}} |
| Legacy p home | 0.5163 |
| Legacy p draw | 0.2450 |
| Legacy p away | 0.2387 |
| Legacy p over 1 5 | 0.7258 |
| Legacy p under 3 5 | 0.7375 |
| Legacy p btts yes | 0.5048 |
| Legacy p over 2 5 | 0.4790 |
| Legacy goal margin distribution | {"-1": 0.15098939596591396, "-10": 3.7965933613425455e-08, "-11": 3.6130776150653038e-09, "-12": 3.157650283089712e-10, "-13": 2.5505710910311414e-11, "-14": 1.9063178916857515e-12, "-15": 1.215536065130584e-13, "-2": 0.06222874243685771, "-3": 0.019534049180177034, "-4": 0.004805010328809983, "-5": 0.0009679296505753231, "-6": 0.0001647566550626608, "-7": 2.42526082566924e-05, "-8": 3.1426845422372307e-06, "-9": 3.635345389116654e-07, "0": 0.2449843537799289, "1": 0.25767850020353916, "10": 1.7424935171773432e-06, "11": 2.3876686171213475e-07, "12": 3.004557103997392e-08, "13": 3.494407424247096e-09, "14": 3.7605477152363904e-10, "15": 3.4525764324952424e-11, "2": 0.15460044027618883, "3": 0.06987658174009498, "4": 0.024748755986138626, "5": 0.00717831504764207, "6": 0.0017593059060044013, "7": 0.00037288637891256355, "8": 6.957264748667074e-05, "9": 1.1587856081667013e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4864 |
| Legacy raw p draw | 0.2441 |
| Legacy raw p away | 0.2695 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5256 |
| Legacy lambda away | 1.0595 |
| Legacy model home team | Arouca |
| Legacy model away team | Nacional |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,468.8191 |
| Elo away rating | 1,372.3854 |
| Elo rating diff | 156.4337 |
| Elo home expectancy | 0.7111 |

</details>


---

## 2026-11-01 — Braga vs Famalicão

The model's most likely 1X2 outcome is **Braga win** at **53.6%**. Expected goals are 1.54 for Braga and 0.97 for Famalicão (2.51 combined). The most likely exact score is 1-0 at 13.7%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 45.6%; Under 3.5 goals: 75.3%; Double Chance 1X: 79.9%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 89.0%; BTTS Yes (both teams score): 48.7%; BTTS No (at least one team does not score): 51.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Braga win | 53.6% | 1.87 |
| Draw | 26.3% | 3.80 |
| Famalicão win | 20.1% | 4.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Braga expected goals | 1.54 |
| Famalicão expected goals | 0.97 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 71.2% |
| Under 1.5 | 28.8% |
| Over 2.5 | 45.6% |
| Under 2.5 | 54.4% |
| Over 3.5 | 24.7% |
| Under 3.5 | 75.3% |
| Over 4.5 | 11.0% |
| Under 4.5 | 89.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.70% |
| 2 | 1-1 | 12.44% |
| 3 | 2-0 | 10.08% |
| 4 | 2-1 | 9.79% |
| 5 | 0-0 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Braga win | 53.6% | 54.6% | 1.78 | -4.6% |
| Draw | 26.3% | 27.2% | 3.46 | -8.9% |
| Famalicão win | 20.1% | 18.2% | 5.06 | +1.7% |

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
| Market best home last update utc | 2026-10-30T07:27:32Z |
| Market best draw last update utc | 2026-10-30T07:27:32Z |
| Market best away last update utc | 2026-10-30T07:27:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sp Braga |
| Matched away-team name | Famalicao |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5361 |
| Dc lambda away | 0.9608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5565 |
| Shot lambda away | 0.9962 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.7% |
| P btts no | 51.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.36 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.48 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.04 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 9.10 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.13188916934310776, "-10": 1.5732197830654862e-08, "-11": 1.3739361014028796e-09, "-12": 1.1017709297392145e-10, "-13": 8.165319668258232e-12, "-14": 5.602359409505132e-13, "-15": 3.2988228211945346e-14, "-2": 0.050373447922938526, "-3": 0.014609562864038807, "-4": 0.003311506888434626, "-5": 0.0006137771046078114, "-6": 9.603839475994089e-05, "-7": 1.2987720257226107e-05, "-8": 1.545493150829546e-06, "-9": 1.641248546122843e-07, "0": 0.2633827092109162, "1": 0.2626825871544232, "10": 2.0355928516529295e-06, "11": 2.822256721963934e-07, "12": 3.592938248392102e-08, "13": 4.2272710790713345e-09, "14": 4.6045409129214966e-10, "15": 4.3043028692521894e-11, "2": 0.16153829463321298, "3": 0.0743771443399754, "4": 0.02676433172375361, "5": 0.007875350438274604, "6": 0.001956286956335697, "7": 0.00041999977278050306, "8": 7.934355902314027e-05, "9": 1.3376651410221737e-05} |
| Raw goal margin distribution | {"-1": 0.16034034927945545, "-10": 1.9125953311135266e-08, "-11": 1.670322100622914e-09, "-12": 1.3394453584036294e-10, "-13": 9.926745418958463e-12, "-14": 6.810902434090117e-13, "-15": 4.010446088907839e-14, "-2": 0.061240026566264066, "-3": 0.017761143118174907, "-4": 0.004025866367780546, "-5": 0.0007461813265085378, "-6": 0.0001167558324670869, "-7": 1.578943602995947e-05, "-8": 1.8788874996123038e-06, "-9": 1.995299283864108e-07, "0": 0.2438981384755598, "1": 0.2509851852213716, "10": 1.9449467680439183e-06, "11": 2.696580057999672e-07, "12": 3.4329427067486427e-08, "13": 4.0390283431232776e-09, "14": 4.399498141114318e-10, "15": 4.112629864776898e-11, "2": 0.154344904388455, "3": 0.07106508867080444, "4": 0.025572501123051376, "5": 0.0075246566963023676, "6": 0.0018691724084224294, "7": 0.00040129694893814533, "8": 7.58103461415918e-05, "9": 1.2780981671474642e-05} |
| Unadjusted home-win probability | 51.2% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 70.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 48.2% |
| P home draw | 79.9% |
| P draw away | 46.4% |
| P home away | 73.7% |
| Raw p home draw | 75.6% |
| Raw p draw away | 48.8% |
| Raw p home away | 75.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4557 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.78 |
| Reference draw odds | 3.46 |
| Reference away odds | 5.06 |
| Market reference 1x2 last update utc | 2026-10-30T07:27:32Z |
| Market reference home last update utc | 2026-10-30T07:27:32Z |
| Market reference draw last update utc | 2026-10-30T07:27:32Z |
| Market reference away last update utc | 2026-10-30T07:27:32Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-30T07:27:10Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:27:10Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.8% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +2.8% |
| Under 2.5 probability edge | -2.8% |
| Raw edge prob home | -0.0341 |
| Raw ev home | -0.0889 |
| Raw edge prob draw | -0.0278 |
| Raw ev draw | -0.1561 |
| Raw edge prob away | 0.0619 |
| Raw ev away | 0.2359 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07665676970042948, 0.07105605392395747, 0.030845013436668862, 0.009650933997728125, 0.0022647224782315583, 0.00042515826174873236, 6.651276601241384e-05, 8.918926917961919e-06, 1.0464735474083539e-06, 1.0914186780025961e-07, 1.0244647466519233e-08, 8.74198324109291e-10, 6.838082875394012e-11, 4.937381030705073e-12, 3.310352524714663e-13, 2.0715175754959292e-14], [0.1318205542882064, 0.12011322696375208, 0.050070379180708606, 0.015666257552664098, 0.0036762996863967156, 0.0006901548420874666, 0.0001079694590322399, 1.4477998318408584e-05, 1.698729275281399e-06, 1.7716882232747512e-07, 1.6630026252849657e-08, 1.4190767547293808e-09, 1.1100186522631147e-10, 8.01479762278681e-12, 5.373659715681408e-13, 3.362672241902088e-14], [0.10219514989061786, 0.09592590859206314, 0.048162474410618245, 0.01271543385148943, 0.002983848907340318, 0.0005601604730643532, 8.7632831880265e-05, 1.1750989622176472e-05, 1.378764498082444e-06, 1.4379812366024852e-07, 1.3497671543813182e-08, 1.1517860308558034e-09, 9.009406809076041e-11, 6.505167469833281e-12, 4.361502064259182e-13, 2.7292948754614704e-14], [0.055297429906660436, 0.05190516587411269, 0.02436050146423394, 0.008153946072347972, 0.0016145499662392933, 0.0003031008274748033, 4.741781174163132e-05, 6.358418434355205e-06, 7.460445360871799e-07, 7.780865013968627e-08, 7.303541771757383e-09, 6.232272996995393e-10, 4.8749577847745707e-11, 3.5199228395790824e-12, 2.359993159599727e-13, 1.4768116904958308e-14], [0.022440931082993224, 0.021064274636243035, 0.009886035127288693, 0.003093189526682494, 0.0007765142056645799, 0.0001230050798390001, 1.9243206188722477e-05, 2.58038809621082e-06, 3.027615216011971e-07, 3.157648661778253e-08, 2.9639402380621047e-09, 2.5291954626471297e-10, 1.97836665945031e-11, 1.4284632394991978e-12, 9.577378901751445e-14, 5.9932314078459375e-15], [0.00728562450329714, 0.006838682177064241, 0.0032095789384788656, 0.0010042282704579378, 0.0002356557756914588, 4.732721506854033e-05, 6.2474580048420876e-06, 8.377432590583162e-07, 9.829390555478647e-08, 1.0251554348602608e-08, 9.622664739208918e-10, 8.21123168559371e-11, 6.4229227197799316e-12, 4.637618083343101e-13, 3.1093712710005054e-14, 1.94574964102195e-15], [0.00197111267378408, 0.0018501932270997877, 0.000868345839163559, 0.00027169216178738007, 6.375624847336549e-05, 1.1969014321667724e-05, 2.003133996673418e-06, 2.2664993983147623e-07, 2.6593240278454272e-08, 2.7735396867313354e-09, 2.603394728131557e-10, 2.2215340408398016e-11, 1.7377102498165337e-12, 1.2546992747307934e-13, 8.412348340208224e-15, 5.264190840048798e-16], [0.00045709800611883126, 0.0004290569718768503, 0.00020136806839218043, 6.300499564680412e-05, 1.4784976243313695e-05, 2.775596065312176e-06, 4.3422082609367444e-07, 6.228959034930025e-08, 6.166931636730985e-09, 6.431795998056765e-10, 6.03723244843571e-11, 5.1517033708861415e-12, 4.029723419506579e-13, 2.9096283758206614e-14, 1.9508106787747536e-15, 1.2207577825553101e-16], [9.275028578001587e-05, 8.706044704806827e-05, 4.0859827958840604e-05, 1.2784416631847108e-05, 3.0000366517932092e-06, 5.631994119892663e-07, 8.810825068738729e-08, 1.1814740174895284e-08, 1.4829860089242323e-09, 1.3050831745335655e-10, 1.2250218277417426e-11, 1.0453380970980254e-12, 8.176758458152025e-14, 5.903960633353808e-15, 3.958412540351943e-16, 2.4770537539984e-17], [1.6728949244762607e-05, 1.570269878572473e-05, 7.3697022313698765e-06, 2.3058673637440152e-06, 5.411030322786308e-07, 1.0158172881747182e-07, 1.589168638563596e-08, 2.1309712101012907e-09, 2.5003063957938033e-10, 2.7896748548166642e-11, 2.209516424415532e-12, 1.8854290122022957e-13, 1.4748049138904248e-14, 1.0648706572474292e-15, 7.139609535483217e-17, 4.467749741005794e-18], [2.7155923718428785e-06, 2.5490022365397897e-06, 1.196315851608376e-06, 3.743089737345637e-07, 8.783667433846365e-08, 1.6489652987721344e-08, 2.5796803907491756e-09, 3.4591826887032743e-10, 4.058720530707166e-11, 4.2330390548112275e-12, 4.2506479875732193e-13, 3.060596674827477e-14, 2.3940349842181993e-15, 1.7285931061843368e-16, 1.1589651512969268e-17, 7.252450191859314e-19], [4.007447222240156e-07, 3.761607242022535e-07, 1.7654242537131558e-07, 5.52374307943052e-08, 1.2962211863543112e-08, 2.433406970299568e-09, 3.806879531466487e-10, 5.104776475586315e-11, 5.989524968945747e-12, 6.246769867866917e-13, 5.863556890733299e-14, 5.3526805285089645e-15, 3.5329193537762955e-16, 2.5509151202471805e-17, 1.710305171127774e-18, 1.0702567762803872e-19], [5.4210383788675944e-08, 5.088480544936897e-08, 2.3881618655511187e-08, 7.47219403474969e-09, 1.753451613718321e-09, 3.291769509574176e-10, 5.1497222294718406e-11, 6.90544070951597e-12, 8.102276318860729e-13, 8.450262054538126e-14, 7.931874127981681e-15, 6.768442830647611e-16, 5.66383228152141e-17, 3.450727608176319e-18, 2.3136000196844875e-19, 1.447780279490701e-20], [6.769164156802688e-09, 6.353904493952293e-09, 2.982059629747276e-09, 9.330409507867805e-10, 2.189507062067563e-10, 4.1103800820757324e-11, 6.430376008611215e-12, 8.622713670502742e-13, 1.0117183206070576e-13, 1.0551707443753266e-14, 9.90440470827657e-16, 8.45164660430953e-17, 6.61097811788824e-18, 5.106522300632114e-19, 2.8889554420933094e-20, 1.807820142550147e-21], [7.848793933290126e-10, 7.367303538461265e-10, 3.457675274006811e-10, 1.0818538278004409e-10, 2.538716649142225e-11, 4.765954186425111e-12, 7.455971673318251e-13, 9.997970381251084e-14, 1.1730796348023341e-14, 1.2234623869647858e-15, 1.1484081311434689e-16, 9.799619429756768e-18, 7.665378434152733e-19, 5.534722927993279e-20, 3.9698190778072696e-21, 2.0961535927693234e-22], [8.493908621739371e-11, 7.972843162423995e-11, 3.7418714353671746e-11, 1.1707744697488711e-11, 2.747380988414254e-12, 5.157681511192597e-13, 8.068799183379128e-14, 1.0819731992327281e-14, 1.2694983851942727e-15, 1.324022239001225e-16, 1.2427990605056109e-17, 1.060507801219386e-18, 8.295417681255386e-20, 5.98963754133293e-21, 4.0158561054474106e-22, 2.688374388860899e-23]] |
| Legacy trial inputs | {"lambda_home": 1.6232892646817405, "lambda_away": 0.9386542188620022, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5431 |
| Legacy p draw | 0.2539 |
| Legacy p away | 0.2030 |
| Legacy p over 1 5 | 0.7205 |
| Legacy p under 3 5 | 0.7436 |
| Legacy p btts yes | 0.4874 |
| Legacy p over 2 5 | 0.4673 |
| Legacy goal margin distribution | {"-1": 0.1355859024098589, "-10": 1.1757435931717611e-08, "-11": 9.919473493528034e-10, "-12": 7.68465447000578e-11, "-13": 5.502039951027829e-12, "-14": 3.646619748904872e-13, "-15": 2.0715175754959292e-14, "-2": 0.049818328922456925, "-3": 0.013937493485904864, "-4": 0.003049181849283615, "-5": 0.0005456573163166164, "-6": 8.245038529880631e-05, "-7": 1.0769017328589818e-05, "-8": 1.2377835245421686e-06, "-9": 1.2697388974518412e-07, "0": 0.25391232550278114, "1": 0.2554482249510884, "10": 3.1165936585860723e-06, "11": 4.547225200669003e-07, "12": 6.092176355472641e-08, "13": 7.543313225002486e-09, "14": 8.646078249532526e-10, "15": 8.493908621739371e-11, "2": 0.16505720128745763, "3": 0.07985834006250471, "4": 0.030214068344797486, "5": 0.009350528195802024, "6": 0.00244342566343618, "7": 0.0005519157622924436, "8": 0.00010970633315997472, "9": 1.9462189898056845e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5402 |
| Legacy raw p draw | 0.2361 |
| Legacy raw p away | 0.2237 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6233 |
| Legacy lambda away | 0.9387 |
| Legacy model home team | Sp Braga |
| Legacy model away team | Famalicao |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,518.8201 |
| Elo away rating | 1,511.6518 |
| Elo rating diff | 67.1683 |
| Elo home expectancy | 0.5955 |

</details>


---

## 2026-11-01 — CS Maritimo vs Santa Clara

The model's most likely 1X2 outcome is **Santa Clara win** at **42.8%**. Expected goals are 1.03 for CS Maritimo and 1.32 for Santa Clara (2.35 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 40.9%; Under 3.5 goals: 78.9%; Double Chance 1X: 57.2%; Double Chance X2: 72.2%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 47.4%; BTTS No (at least one team does not score): 52.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CS Maritimo win | 27.8% | 3.59 |
| Draw | 29.4% | 3.40 |
| Santa Clara win | 42.8% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CS Maritimo expected goals | 1.03 |
| Santa Clara expected goals | 1.32 |
| Expected total goals | 2.35 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 67.5% |
| Under 1.5 | 32.5% |
| Over 2.5 | 40.9% |
| Under 2.5 | 59.1% |
| Over 3.5 | 21.1% |
| Under 3.5 | 78.9% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.76% |
| 2 | 0-1 | 12.85% |
| 3 | 0-0 | 9.89% |
| 4 | 1-0 | 9.77% |
| 5 | 1-2 | 8.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CS Maritimo win | 27.8% | 27.0% | 3.50 | -2.6% |
| Draw | 29.4% | 30.8% | 3.09 | -9.1% |
| Santa Clara win | 42.8% | 42.3% | 2.28 | -2.5% |

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
| Market best home last update utc | 2026-10-30T07:27:32Z |
| Market best draw last update utc | 2026-10-30T07:27:32Z |
| Market best away last update utc | 2026-10-30T07:27:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Maritimo |
| Matched away-team name | Santa Clara |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9841 |
| Dc lambda away | 1.3334 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.1414 |
| Shot lambda away | 1.2988 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.4% |
| P btts no | 52.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.11 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.08 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.73 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.40 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.2331898968696232, "-10": 4.733201703816456e-07, "-11": 5.635142830569421e-08, "-12": 6.1585920881076655e-09, "-13": 6.196522754347466e-10, "-14": 5.335855532386004e-11, "-2": 0.12450727801164908, "-3": 0.04961406100236721, "-4": 0.015403820176719374, "-5": 0.0039038753044630162, "-6": 0.0008343569240123504, "-7": 0.00015401419166417618, "-8": 2.5003975693059428e-05, "-9": 3.621452106914614e-06, "0": 0.2941755012976718, "1": 0.17610315022951922, "10": 3.7681656813565235e-08, "11": 3.496896442076284e-09, "12": 2.9789426870475793e-10, "13": 2.336316208636318e-11, "14": 1.5681604660590941e-12, "2": 0.0727355613916932, "3": 0.022592261069546107, "4": 0.0054674677105530445, "5": 0.0010800816536808003, "6": 0.00017993489362717104, "7": 2.58897062639604e-05, "8": 3.276259667594023e-06, "9": 3.698748982384162e-07} |
| Raw goal margin distribution | {"-1": 0.23968523990249233, "-10": 4.865041758307486e-07, "-11": 5.7921058303181876e-08, "-12": 6.330135404300898e-09, "-13": 6.369122602971993e-10, "-14": 5.4844820917778854e-11, "-2": 0.12797534198710778, "-3": 0.05099602630099353, "-4": 0.015832882916604552, "-5": 0.004012615046623505, "-6": 0.000857597358122323, "-7": 0.00015830415027824163, "-8": 2.570044411425671e-05, "-9": 3.722325146558646e-06, "0": 0.2630638541494749, "1": 0.18825753109738896, "10": 4.0282389441275245e-08, "11": 3.738247100239406e-09, "12": 3.184544937516931e-10, "13": 2.4975653230930062e-11, "14": 1.6763925989969599e-12, "2": 0.07775566304598357, "3": 0.02415154575779684, "4": 0.005844824304402902, "5": 0.0011546273036031629, "6": 0.00019235373579844334, "7": 2.7676575778102114e-05, "8": 3.5023822995292177e-06, "9": 3.9540312065121825e-07} |
| Unadjusted home-win probability | 29.7% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 78.8% |
| Raw p btts yes | 46.6% |
| P home draw | 57.2% |
| P draw away | 72.2% |
| P home away | 70.6% |
| Raw p home draw | 56.0% |
| Raw p draw away | 70.3% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4091 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:27:32Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.50 |
| Reference draw odds | 3.09 |
| Reference away odds | 2.28 |
| Market reference 1x2 last update utc | 2026-10-30T07:27:32Z |
| Market reference home last update utc | 2026-10-30T07:27:32Z |
| Market reference draw last update utc | 2026-10-30T07:27:32Z |
| Market reference away last update utc | 2026-10-30T07:27:32Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.46 |
| Reference Under 2.5 odds | 1.54 |
| Market reference over 2 5 last update utc | 2026-10-30T07:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:27:32Z |
| Home probability edge | +0.8% |
| Draw probability edge | -1.3% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | 0.0274 |
| Raw ev home | 0.0409 |
| Raw edge prob draw | -0.0444 |
| Raw ev draw | -0.1871 |
| Raw edge prob away | 0.0170 |
| Raw ev away | 0.0022 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.10352138079554367, 0.13589520242852918, 0.08038833474609536, 0.033326006413824244, 0.010361789807583368, 0.00257736703722174, 0.0005342401399688335, 9.491830439981922e-05, 1.4756096288140271e-05, 2.039109119894034e-06, 2.536015846927717e-07, 2.8672844131793927e-08, 2.9716730370669907e-09, 2.842949645307453e-10, 2.525530558620998e-11], [0.10530899300305163, 0.1338129336835462, 0.08234583273973205, 0.034137512099282584, 0.010614104808545802, 0.0026401272725240636, 0.0005472491667811468, 9.722961475360248e-05, 1.5115414950097593e-05, 2.088762493404085e-06, 2.5977691591199814e-07, 2.9371042882111625e-08, 3.0440348296849853e-09, 2.9121769560146166e-10, 2.5870285485592575e-11], [0.05077899906173724, 0.06315323935110724, 0.0448615820588496, 0.017484389186296974, 0.005436281905870376, 0.0013522078761895938, 0.0002802874850999876, 4.979860336165019e-05, 7.741741604697436e-06, 1.069812476263746e-06, 1.3305130983803513e-07, 1.5043121568576444e-08, 1.5590793348989843e-09, 1.491544993971464e-10, 1.3250120233577779e-11], [0.017338498081990793, 0.02156368458601155, 0.013409249484186064, 0.0063502696220955656, 0.0018562194044726425, 0.0004617116150568725, 9.570421065022658e-05, 1.700374179928258e-05, 2.643419020550551e-06, 3.652876565218808e-07, 4.543039293918314e-08, 5.136476482074906e-09, 5.323479106973304e-10, 5.0928829821429014e-11, 4.524255863663651e-12], [0.004440174894551874, 0.0055221928958364645, 0.0034339429305187755, 0.001423584709008215, 0.0005056293461514722, 0.00011823863358890979, 2.4508664558057757e-05, 4.354447951235001e-06, 6.769469140479207e-07, 9.354565050030639e-08, 1.1634161691762086e-08, 1.3153880926891945e-09, 1.363277151843148e-10, 1.3042243365755792e-11, 1.1586059650249651e-12], [0.0009096590950832837, 0.0011313322361841145, 0.0007035122473612856, 0.0002916499482395971, 9.068039607043003e-05, 2.5766317428790813e-05, 5.0210926715833e-06, 8.920962072390308e-07, 1.3868618508875244e-07, 1.9164707202749505e-08, 2.3834919227092765e-09, 2.6948369613709593e-10, 2.792947326950989e-11, 2.671965762543854e-12, 2.3736372524332135e-13], [0.00015530162829904546, 0.00019314679463575005, 0.00012010718975280023, 4.979196283503865e-05, 1.5481418523332408e-05, 3.8508113494320165e-06, 9.118217377325231e-07, 1.523032027409563e-07, 2.3677211037937377e-08, 3.2718963076920016e-09, 4.069218662629688e-10, 4.6007627512705186e-11, 4.7682617584254815e-12, 4.561715877137133e-13, 4.052394268211001e-14], [2.2726186309979328e-05, 2.82642885856616e-05, 1.7575980376935653e-05, 7.2863461672771774e-06, 2.265485594436487e-06, 5.635115171056631e-07, 1.168054326081143e-07, 2.3706855414406385e-08, 3.4648233585337824e-09, 4.787955277092152e-10, 5.95472323605609e-11, 6.732562472046503e-12, 6.977673465732308e-13, 6.675422920703943e-14, 5.93010312573919e-15], [2.9099476040341246e-06, 3.6190673493448917e-06, 2.2504955864044936e-06, 9.329715633951757e-07, 2.900814191868815e-07, 7.215416465749949e-08, 1.495621324757417e-08, 2.6572664528439817e-09, 4.719044432690622e-10, 6.130680615198005e-11, 7.624654826418833e-12, 8.620629861658302e-13, 8.934479329875161e-14, 8.547466200031601e-15, 7.593130297819743e-16], [3.31200705563975e-07, 4.119103924499791e-07, 2.5614403676975585e-07, 1.0618776765575857e-07, 3.301611705052806e-08, 8.212350700340245e-09, 1.702267206905952e-09, 3.024413645226195e-10, 4.701784260297851e-11, 7.422139917432514e-12, 8.67813239898484e-13, 9.811718563691428e-14, 1.016893174914603e-14, 9.728446080300956e-16, 8.642252213031954e-17], [3.3926561596024394e-08, 4.219406259325565e-08, 2.623812780267425e-08, 1.0877349533367891e-08, 3.382007676792003e-09, 8.412325734898819e-10, 1.7437183036686416e-10, 3.098059699235855e-11, 4.816275166038283e-12, 6.655493718132656e-13, 9.455602931726124e-14, 1.0050639042181457e-14, 1.0416550555522024e-15, 9.965338830269469e-17, 8.85269557426023e-18], [3.1593355558414298e-09, 3.929228189510738e-09, 2.4433672670033906e-09, 1.012928971207957e-09, 3.1494193931723784e-10, 7.833791151031389e-11, 1.6237988693783226e-11, 2.884999157433687e-12, 4.4850490774649894e-13, 6.197780428135038e-14, 7.708106068568662e-15, 9.9555199231251e-16, 9.700180917578436e-17, 9.28000003872097e-18, 8.243875764904467e-19], [2.6968891907815386e-10, 3.354089125738147e-10, 2.0857204481832533e-10, 8.6466193451004e-11, 2.6884245021014304e-11, 6.687123385483464e-12, 1.3861160175698284e-12, 2.4627086631272885e-13, 3.8285519734603146e-14, 5.2905830191320435e-15, 6.57983540218916e-16, 7.439330283696243e-17, 8.80768031891075e-18, 7.921644077535582e-19, 7.037182042727162e-20], [2.1250460407941084e-11, 2.6428945770125976e-11, 1.6434683322419717e-11, 6.813206960214249e-12, 2.118376188273765e-12, 5.269198720954956e-13, 1.0922066673286115e-13, 1.94052069773449e-14, 3.016753243324247e-15, 4.1687780635291976e-16, 5.184659873417704e-17, 5.861909128326886e-18, 6.075322427840368e-19, 6.639493164220315e-20, 5.545031619897996e-21], [1.554851445194649e-12, 1.9337503158423478e-12, 1.2024911754679727e-12, 4.985080080684121e-13, 1.5499712545392907e-13, 3.855361761118848e-14, 7.99144622067819e-15, 1.4198381368598938e-15, 2.2072948303866014e-16, 3.050207135442547e-17, 3.793506466341674e-18, 4.2890354866724697e-19, 4.445185504508458e-20, 4.252634255429785e-21, 4.315577759215526e-22]] |
| Legacy trial inputs | {"lambda_home": 1.0243505229934093, "lambda_away": 1.243688148998868, "rho": 0.05, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2901 |
| Legacy p draw | 0.2891 |
| Legacy p away | 0.4208 |
| Legacy p over 1 5 | 0.6553 |
| Legacy p under 3 5 | 0.8059 |
| Legacy p btts yes | 0.4543 |
| Legacy p over 2 5 | 0.3903 |
| Legacy goal margin distribution | {"-1": 0.23770505931550215, "-10": 2.8458379434556877e-07, "-11": 3.187055771673972e-08, "-12": 3.27614085290203e-09, "-13": 3.1016525001633786e-10, "-14": 2.525530558620998e-11, "-2": 0.12044926529080088, "-3": 0.045392519775662055, "-4": 0.013299904832372707, "-5": 0.0031771542022415392, "-6": 0.0006395886924648185, "-7": 0.00011115030599878739, "-8": 1.6983185608069357e-05, "-9": 2.3144747848923967e-06, "0": 0.28907849783163053, "1": 0.18338971726516326, "10": 3.807133003443913e-08, "11": 3.5116776597457325e-09, "12": 2.973203560237478e-10, "13": 2.3184210723783432e-11, "14": 1.554851445194649e-12, "2": 0.07608433672008111, "3": 0.02361633456148433, "4": 0.005699199137721489, "5": 0.0011213487154962953, "6": 0.00018592606199009757, "7": 2.6612596785330553e-05, "8": 3.3491364724143257e-06, "9": 3.759267585474908e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3103 |
| Legacy raw p draw | 0.2706 |
| Legacy raw p away | 0.4191 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0244 |
| Legacy lambda away | 1.2437 |
| Legacy model home team | Maritimo |
| Legacy model away team | Santa Clara |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,412.3721 |
| Elo away rating | 1,471.5616 |
| Elo rating diff | 0.8105 |
| Elo home expectancy | 0.5012 |

</details>


---
