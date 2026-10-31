# Eredivisie — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Eredivisie |
| Training matches | 1,620 |
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
| Training sha256 | 173f00460382fe819ab1795f92939756d58effd9917931edff4bdbeeab528135 |
| Training as of utc | 2026-10-31T12:02:40.831876+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-31', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-01', 'audit_start_date': '2026-05-02', 'training_shot_matches': 1315, 'tuning_matches': 188, 'audit_matches': 111, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6977042483436141, 'audit_candidate_poisson_score': 0.6898503532995676, 'audit_gain': 0.007853895044046544, 'audit_gain_lower95': -0.003847173731557008, 'audit_baseline_briers': [0.618234730821842, 0.09079345116733593, 0.2827686416831054, 0.22261156699804835], 'audit_candidate_briers': [0.6174115106520035, 0.08936023992934143, 0.27916143628828854, 0.21698304613913946], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1612.417 |
| Base scoring parameter | 0.292 |
| Home-advantage parameter | 0.184 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 6, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 38.00 |
| Over 1 5 in window quote fixtures | 7 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 9} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 9} |
| Legacy comparison status | {'AVAILABLE': 9} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'UNRELIABLE_AUDIT', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'UNRELIABLE_AUDIT', 'draw': 'UNRELIABLE_AUDIT', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-31 — Ajax vs AZ Alkmaar

The model's most likely 1X2 outcome is **Ajax win** at **53.8%**. Expected goals are 1.87 for Ajax and 1.25 for AZ Alkmaar (3.12 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 69.2%; Under 3.5 goals: 52.0%; Double Chance 1X: 76.3%; Double Chance X2: 46.2%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 71.1%; BTTS Yes (both teams score): 68.0%; BTTS No (at least one team does not score): 32.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ajax win | 53.8% | 1.86 |
| Draw | 22.5% | 4.44 |
| AZ Alkmaar win | 23.7% | 4.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ajax expected goals | 1.87 |
| AZ Alkmaar expected goals | 1.25 |
| Expected total goals | 3.12 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 88.0% |
| Under 1.5 | 12.0% |
| Over 2.5 | 69.2% |
| Under 2.5 | 30.8% |
| Over 3.5 | 48.0% |
| Under 3.5 | 52.0% |
| Over 4.5 | 28.9% |
| Under 4.5 | 71.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.47% |
| 2 | 2-1 | 9.38% |
| 3 | 3-1 | 6.69% |
| 4 | 2-2 | 6.63% |
| 5 | 2-0 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ajax win | 53.8% | 55.1% | 1.78 | -4.2% |
| Draw | 22.5% | 21.6% | 4.41 | -0.8% |
| AZ Alkmaar win | 23.7% | 23.2% | 4.11 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:00:00+00:00 |
| Fixture id | 43ebf45469e32887fe9caff703c94ae6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ajax |
| Matched away-team name | AZ Alkmaar |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8680 |
| Dc lambda away | 1.2546 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.0% |
| P btts no | 32.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.44 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.34 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.25 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.92 |
| Fair Over 4.5 odds | 3.46 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.12895080647924104, "-10": 3.618590788115649e-07, "-11": 4.616972586958548e-08, "-12": 5.418219008701687e-09, "-13": 5.885139214833298e-10, "-14": 5.948289327934703e-11, "-15": 5.6169094813144345e-12, "-16": 4.920271940855963e-13, "-17": 3.519539015630427e-14, "-2": 0.0692679911355743, "-3": 0.027072971528552505, "-4": 0.008522520947697012, "-5": 0.0022332398568725978, "-6": 0.0004996281849171586, "-7": 9.733759913691267e-05, "-8": 1.6774145738589635e-05, "-9": 2.5895360021844875e-06, "0": 0.22502059012457457, "1": 0.20896191935331132, "10": 2.0668265982591637e-05, "11": 3.926278477741321e-06, "12": 6.860244492836789e-07, "13": 1.1094277221797327e-07, "14": 1.6695275597303305e-08, "15": 2.3472436228461455e-09, "16": 3.0613225050167424e-10, "17": 3.260355795361266e-11, "2": 0.16384126136741292, "3": 0.09534234983519077, "4": 0.04468659225060024, "5": 0.01743426988773647, "6": 0.005807303974280828, "7": 0.0016844863427520522, "8": 0.00043220174000214973, "9": 9.934071630492806e-05} |
| Raw goal margin distribution | {"-1": 0.14099963595912585, "-10": 1.4486551882702385e-07, "-11": 1.6238776372371114e-08, "-12": 1.6729769844821438e-09, "-13": 1.5942468289617048e-10, "-14": 1.4124501995153726e-11, "-15": 1.1599383231566066e-12, "-16": 7.933472626380817e-14, "-2": 0.07104374687229631, "-3": 0.025262539396081595, "-4": 0.00714434989465819, "-5": 0.001668950044053958, "-6": 0.0003312220743494602, "-7": 5.7051394415363325e-05, "-8": 8.671995795428155e-06, "-9": 1.1788311918275258e-06, "0": 0.2457506430414675, "1": 0.21475378076198717, "10": 7.754563815115725e-06, "11": 1.294210395970537e-06, "12": 1.9851840815192224e-07, "13": 2.8166028501101708e-08, "14": 3.7153730940823965e-09, "15": 4.5427979331633355e-10, "16": 4.626058118291849e-11, "2": 0.1574868613784513, "3": 0.08337862103569227, "4": 0.03510747984858592, "5": 0.012210670479190302, "6": 0.003608067731202506, "7": 0.0009252964742690341, "8": 0.0002094078399930614, "9": 4.238232057099349e-05} |
| Unadjusted home-win probability | 50.8% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 61.4% |
| P home draw | 76.3% |
| P draw away | 46.2% |
| P home away | 77.5% |
| Raw p home draw | 75.3% |
| Raw p draw away | 49.2% |
| Raw p home away | 75.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1442 |
| Totals anchor target over 2 5 | 0.6924 |
| Totals anchor reference over odds | 1.41 |
| Totals anchor reference under odds | 3.01 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6120 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.85, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.78 |
| Reference draw odds | 4.41 |
| Reference away odds | 4.11 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 2.94 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:15Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:15Z |
| Home probability edge | -1.3% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | -0.0437 |
| Raw ev home | -0.0962 |
| Raw edge prob draw | 0.0296 |
| Raw ev draw | 0.0838 |
| Raw edge prob away | 0.0141 |
| Raw ev away | 0.0132 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05224757965205832, 0.04416287960681854, 0.034018299483582384, 0.014113170999675231, 0.004391348157236696, 0.0010931030957399936, 0.00022674782609133953, 4.031608481331955e-05, 6.272224886811164e-06, 8.673859238486808e-07, 1.0795571252962502e-07, 1.2214795521433077e-08, 1.2668879730690988e-09, 1.2129087221684497e-10, 1.0782844483382214e-11, 8.946956806604758e-13, 6.959669497107352e-14], [0.0761346549521257, 0.1073725329187655, 0.06306569487096947, 0.026164063149508247, 0.008141013135889979, 0.002026477141566717, 0.000420362258843462, 7.474100533614287e-05, 1.1627924584079719e-05, 1.608025587381721e-06, 2.0013645976799023e-07, 2.264471119838765e-08, 2.348652682766699e-09, 2.2485818674013755e-10, 1.9990052129392543e-11, 1.658654478779548e-12, 1.2902361363453567e-13], [0.08102229336397156, 0.10084115006249264, 0.05612074302437871, 0.02425245894445721, 0.007546212746706716, 0.001878418248606449, 0.00038964966435620194, 6.928026251214469e-05, 1.077836274791052e-05, 1.4905396886089101e-06, 1.855140482606358e-07, 2.099023861507187e-08, 2.1770549336355364e-09, 2.0842955129248629e-10, 1.8529534797226786e-11, 1.5374695214491988e-12, 1.1959686363147685e-13], [0.05006841718140965, 0.06231564870301673, 0.03877933727371388, 0.014387811724645533, 0.004663246524564466, 0.001160784576781948, 0.00024078733320893325, 4.2812329074828404e-05, 6.6605811831403816e-06, 9.210917126162814e-07, 1.146399882758191e-07, 1.2971096967048839e-08, 1.3453296632131648e-09, 1.2880081880879857e-10, 1.1450484056744074e-11, 9.50092403060157e-13, 7.39059018607298e-14], [0.02320515405362252, 0.02888136493042245, 0.017973016647868812, 0.0074564649374610735, 0.002074859084640627, 0.0005379875467142886, 0.00011159743958011257, 1.984218290696532e-05, 3.0869722100745732e-06, 4.268973594937605e-07, 5.3132068845060384e-08, 6.0116999959128665e-09, 6.23518454251456e-10, 5.969517334373906e-11, 5.30694320858125e-12, 4.4033827748749763e-13, 3.42530867699752e-14], [0.008603893711300145, 0.01070849146376749, 0.006663947352056085, 0.0027646716602571448, 0.0008602344434793644, 0.0001914972057074198, 4.137755372714873e-05, 7.356987690631401e-06, 1.1445724826408858e-06, 1.5828291845128352e-07, 1.9700049047208015e-08, 2.2289887698885278e-09, 2.311851278822352e-10, 2.2133484886172934e-11, 1.9676824895463808e-12, 1.6326647639419505e-13, 1.2700192257797195e-14], [0.002658424748523846, 0.0033087018136041166, 0.002059021549777934, 0.000854226215453734, 0.0002657946054208762, 6.616212051821824e-05, 1.2273651385536755e-05, 2.273156643680153e-06, 3.536491635566841e-07, 4.89061396849693e-08, 6.086906660114649e-09, 6.88711310121236e-10, 7.143141071647586e-11, 6.8387878752153034e-12, 6.079730878796106e-13, 5.044595575147166e-14, 3.9240960595312974e-15], [0.000704055533861587, 0.0008762745016797496, 0.0005453099687197754, 0.0002262327321823933, 7.039287567610688e-05, 1.7522334272856305e-05, 3.634745176278411e-06, 5.779517017481984e-07, 9.366022144725433e-08, 1.2952271191475306e-08, 1.6120525211527261e-09, 1.8239786903622794e-10, 1.8917849765881224e-11, 1.8111802679855572e-12, 1.6101520917537348e-13, 1.336007510744169e-14, 1.039255125672283e-15], [0.00016315392062792969, 0.0002030629881015083, 0.00012636710468867066, 5.2425917352681875e-05, 1.6312454200649922e-05, 4.060528463556797e-06, 8.422956677020637e-07, 1.4976136337152308e-07, 2.083653097853737e-08, 3.0014874172423273e-09, 3.7356810142751113e-10, 4.226786953043206e-11, 4.383917476260438e-12, 4.197128599572684e-13, 3.7312770646942974e-14, 3.095989632674695e-15, 2.4083121306655185e-16], [3.360745223574998e-05, 4.1828168438766034e-05, 2.602987668729984e-05, 1.0799014247188239e-05, 3.3601400645860632e-06, 8.364127313991589e-07, 1.735012637865498e-07, 3.0848770577491486e-08, 4.799335735094621e-09, 5.935458056999061e-10, 7.694986474861148e-11, 8.706596819026946e-12, 9.030263975383194e-13, 8.645504710800833e-14, 7.68591494751959e-15, 6.377310658673825e-16, 4.960790067968696e-17], [6.230403518886561e-06, 7.754422025250914e-06, 4.825615288272897e-06, 2.002002885973492e-06, 6.229281629411666e-07, 1.5506051420962617e-07, 3.216497569777362e-08, 5.71897826146053e-09, 8.897371345645616e-10, 1.2304174043082187e-10, 1.3695190686959072e-11, 1.6140947275107088e-12, 1.6740985914086347e-13, 1.6027690107203343e-14, 1.4248730073013304e-15, 1.182274053091353e-16, 9.196687591525173e-18], [1.0500357246485802e-06, 1.3068848792590547e-06, 8.13280942516294e-07, 3.374058429360615e-07, 1.0498466479661185e-07, 2.6132991050888423e-08, 5.420896650230373e-09, 9.638431066011217e-10, 1.4995108647572993e-10, 2.0736734415941903e-11, 2.5809145362625785e-12, 2.6115392443320235e-13, 2.821427732945749e-14, 2.7012130346202315e-15, 2.4013975278141133e-16, 1.99253545666469e-17, 1.5499558720812227e-18], [1.622196328142542e-07, 2.0190016422046638e-07, 1.256434736198879e-07, 5.2125704550471186e-08, 1.6219042242713815e-08, 4.037276173657891e-09, 8.374723292568887e-10, 1.4890376696060675e-10, 2.3165888185692283e-11, 3.2036104712976464e-12, 3.987245372414412e-13, 4.511422858188928e-14, 4.184541772577106e-15, 4.173094079973536e-16, 3.709910206468801e-17, 3.0782606968701417e-18, 2.394521124807076e-19], [2.313346282724598e-08, 2.8792137318896765e-08, 1.7917489862647124e-08, 7.433428541556744e-09, 2.3129297256206296e-09, 5.757390561571659e-10, 1.1942842343808452e-10, 2.1234542934543078e-11, 3.3035903478925848e-12, 4.568534798472802e-13, 5.686043730075092e-14, 6.433551301857643e-15, 6.672718142636775e-16, 5.713142363394269e-17, 5.290547658435164e-18, 4.38977873197112e-19, 3.4147263477785593e-20], [3.0633258530164596e-09, 3.812645744877296e-09, 2.372628357772823e-09, 9.843322635244263e-10, 3.0627742494128947e-10, 7.623918427120777e-11, 1.581467417286075e-11, 2.811871479602337e-12, 4.3746039216212615e-13, 6.049639374388966e-14, 7.529441177827676e-15, 8.519288347301203e-16, 8.83599232370723e-17, 8.459510537837765e-18, 6.725627621997632e-19, 5.812931154790645e-20, 4.52176986223028e-21], [3.78601667277979e-10, 4.712113908252517e-10, 2.932371857206329e-10, 1.2165530342091637e-10, 3.785334936477462e-11, 9.42253082497562e-12, 1.954562556055607e-12, 3.475239923629249e-13, 5.406647604190399e-14, 7.4768524912843e-15, 9.305764781079304e-16, 1.0529133781618508e-16, 1.0920553628066828e-17, 1.045525336727474e-18, 9.29479432649547e-20, 6.897062208413196e-21, 5.588532500393137e-22], [4.386752422346347e-11, 5.459795581465718e-11, 3.3976578709505114e-11, 1.4095862303246258e-11, 4.385962513417224e-12, 1.0917624905953264e-12, 2.2646973768102868e-13, 4.026664029987501e-14, 6.264532495320793e-15, 8.663221430978482e-16, 1.0782331332210521e-16, 1.2199815033516693e-17, 1.2653342344134928e-18, 1.2114211848270152e-19, 1.0769620171014144e-20, 8.935984066365712e-22, 6.216386677805485e-23]] |
| Legacy trial inputs | {"lambda_home": 1.8538755854449953, "lambda_away": 1.2446099200067078, "rho": -0.10363035671928646, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5286 |
| Legacy p draw | 0.2324 |
| Legacy p away | 0.2389 |
| Legacy p over 1 5 | 0.8275 |
| Legacy p under 3 5 | 0.6230 |
| Legacy p btts yes | 0.6071 |
| Legacy p over 2 5 | 0.6050 |
| Legacy goal margin distribution | {"-1": 0.13672601494419626, "-10": 1.3291175361423806e-07, "-11": 1.478378127801875e-08, "-12": 1.5112600400962933e-09, "-13": 1.4289229976954742e-10, "-14": 1.2561095825793239e-11, "-15": 1.0237192942950115e-12, "-16": 6.959669497107352e-14, "-2": 0.06900868136772964, "-3": 0.024394427034149572, "-4": 0.006853538821139316, "-5": 0.00158985350374396, "-6": 0.00031324372022617487, "-7": 5.355543896235647e-05, "-8": 8.079381892933702e-06, "-9": 1.0899196662360002e-06, "0": 0.23240789665732078, "1": 0.22414179322133468, "10": 7.670681226732564e-06, "11": 1.2708766561070736e-06, "12": 1.935104397568581e-07, "13": 2.7253441620147156e-08, "14": 3.5685138225512163e-09, "15": 4.3319962309263617e-10, "16": 4.386752422346347e-11, "2": 0.16435982137012542, "3": 0.08654258845693605, "4": 0.03621608181873157, "5": 0.012513852184720961, "6": 0.003672515289445364, "7": 0.0009352595457725666, "8": 0.00021016192114766625, "9": 4.222967207180675e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5059 |
| Legacy raw p draw | 0.2487 |
| Legacy raw p away | 0.2455 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8539 |
| Legacy lambda away | 1.2446 |
| Legacy model home team | Ajax |
| Legacy model away team | AZ Alkmaar |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 77.0% |
| Market reference home draw last update utc | 2026-10-31T12:02:43Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.6% |
| Market reference draw away last update utc | 2026-10-31T12:02:43Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.3% |
| Market reference home away last update utc | 2026-10-31T12:02:43Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 2.09 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 88.2% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.80 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 53.3% |
| Market under 3 5 odds | 1.82 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.82 |
| Market reference under 3 5 opposite odds | 2.06 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.1% |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.98 |
| Market reference btts yes last update utc | 2026-10-31T12:02:36Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,582.8938 |
| Elo away rating | 1,549.1473 |
| Elo rating diff | 93.7465 |
| Elo home expectancy | 0.6317 |

</details>


---

## 2026-10-31 — Feyenoord vs Fortuna Sittard

The model's most likely 1X2 outcome is **Feyenoord win** at **82.7%**. Expected goals are 2.73 for Feyenoord and 0.83 for Fortuna Sittard (3.56 combined). The most likely exact score is 3-0 at 9.1%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 77.7%; Under 3.5 goals: 41.8%; Double Chance 1X: 93.9%; Double Chance X2: 17.3%; Double Chance 12 (either team wins): 88.8%; Under 4.5 goals: 61.2%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 82.7% | 1.21 |
| Draw | 11.2% | 8.90 |
| Fortuna Sittard win | 6.1% | 16.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 2.73 |
| Fortuna Sittard expected goals | 0.83 |
| Expected total goals | 3.56 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.7% |
| Under 2.5 | 22.3% |
| Over 3.5 | 58.2% |
| Under 3.5 | 41.8% |
| Over 4.5 | 38.8% |
| Under 4.5 | 61.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 9.07% |
| 2 | 2-0 | 8.78% |
| 3 | 3-1 | 8.57% |
| 4 | 2-1 | 8.29% |
| 5 | 4-0 | 7.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 82.7% | 85.3% | 1.16 | -4.1% |
| Draw | 11.2% | 9.5% | 8.94 | +0.4% |
| Fortuna Sittard win | 6.1% | 5.2% | 15.64 | -4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:30:00+00:00 |
| Fixture id | 1836e9e3241ea98ae062bab0f288ce2c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:36Z |
| Market best draw last update utc | 2026-10-31T12:02:36Z |
| Market best away last update utc | 2026-10-31T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Feyenoord |
| Matched away-team name | For Sittard |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7318 |
| Dc lambda away | 0.8329 |
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
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.95 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.47 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.49 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.39 |
| Fair Over 4.5 odds | 2.58 |
| Fair Under 4.5 odds | 1.63 |
| Goal margin distribution | {"-1": 0.04105817917173426, "-10": 2.8580394774923544e-09, "-11": 2.401912755518403e-10, "-12": 1.8563646180135836e-11, "-13": 1.3277601464479106e-12, "-14": 8.836624643601356e-14, "-15": 5.4982022741667085e-15, "-16": 3.2116648734318095e-16, "-17": 1.7676994163037857e-17, "-18": 9.193985442320725e-19, "-19": 4.496309742203316e-20, "-2": 0.015165728672789341, "-20": 1.852483113436758e-21, "-3": 0.003929937512099329, "-4": 0.0008183229999669683, "-5": 0.00014163600794680716, "-6": 2.091030081443438e-05, "-7": 2.686534932664179e-06, "-8": 3.0517949826874726e-07, "-9": 3.1045404079066596e-08, "0": 0.11230979994738216, "1": 0.18641431236742506, "10": 0.000534408022189791, "11": 0.00014730845083200578, "12": 3.734215731771263e-05, "13": 8.760349623417154e-06, "14": 1.9122906700472836e-06, "15": 3.9025987380628406e-07, "16": 7.477029543700125e-08, "17": 1.349811057824949e-08, "18": 2.3026825141291106e-09, "19": 3.6936195552696914e-10, "2": 0.21171056034459865, "20": 4.9913254202913075e-11, "3": 0.17994118365424236, "4": 0.12289532826295567, "5": 0.06976698929895646, "6": 0.03378331582756204, "7": 0.014236399706096341, "8": 0.005304307876850467, "9": 0.0017698496496577679} |
| Raw goal margin distribution | {"-1": 0.05657686018145146, "-10": 1.5382186512676926e-09, "-11": 1.1452249129886203e-10, "-12": 7.83574565984768e-12, "-13": 4.958852936569e-13, "-14": 2.918766893791584e-14, "-15": 1.605560814336236e-15, "-16": 8.288859648856482e-17, "-17": 4.030170441964861e-18, "-18": 1.841420122046172e-19, "-19": 7.208765543752382e-21, "-2": 0.01973533874532338, "-3": 0.004677300340735688, "-4": 0.0008804777058971286, "-5": 0.0001368050237408077, "-6": 1.804965918347273e-05, "-7": 2.066166129181535e-06, "-8": 2.0867396770530013e-07, "-9": 1.88442754164414e-08, "0": 0.15235959908041846, "1": 0.19960148629979327, "10": 0.00022165368465730897, "11": 5.412692528789475e-05, "12": 1.2146987636580629e-05, "13": 2.5213618397319642e-06, "14": 4.86764667363175e-07, "15": 8.78237714892675e-08, "16": 1.4871192573928925e-08, "17": 2.371592745754674e-09, "18": 3.554146068978798e-10, "19": 4.563614770147359e-11, "2": 0.21231269429031857, "3": 0.1650411809493027, "4": 0.10190162667548947, "5": 0.05193145454594527, "6": 0.02247310780976717, "7": 0.008437718948399767, "8": 0.002795077019323094, "9": 0.0008278861877378694} |
| Unadjusted home-win probability | 76.6% |
| Unadjusted draw probability | 15.2% |
| Unadjusted away-win probability | 8.2% |
| Raw p over 1 5 | 87.7% |
| Raw p under 3 5 | 52.3% |
| Raw p btts yes | 53.5% |
| P home draw | 93.9% |
| P draw away | 17.3% |
| P home away | 88.8% |
| Raw p home draw | 91.8% |
| Raw p draw away | 23.4% |
| Raw p home away | 84.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1341 |
| Totals anchor target over 2 5 | 0.7775 |
| Totals anchor reference over odds | 1.25 |
| Totals anchor reference under odds | 3.79 |
| Totals anchor reference last update utc | 2026-10-31T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7114 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:48:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 4.41, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:48:13Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:48:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:48:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.09, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.77, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:48:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:48:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:48:13Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:48:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.41, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.94 |
| Reference away odds | 15.64 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:36Z |
| Market reference home last update utc | 2026-10-31T12:02:36Z |
| Market reference draw last update utc | 2026-10-31T12:02:36Z |
| Market reference away last update utc | 2026-10-31T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.24 |
| Reference Under 2.5 odds | 3.89 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:15Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:15Z |
| Home probability edge | -2.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Raw edge prob home | -0.0871 |
| Raw ev home | -0.1119 |
| Raw edge prob draw | 0.0572 |
| Raw ev draw | 0.3621 |
| Raw edge prob away | 0.0298 |
| Raw ev away | 0.2829 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.028179234867898938, 0.014057670741986161, 0.008429053918924305, 0.0024268170268494445, 0.0005240304195276141, 9.052446148255038e-05, 1.3031492418087757e-05, 1.6079612250164792e-06, 1.736061239902033e-07, 1.6661035418572336e-08, 1.439068423134242e-09, 1.1299733858805924e-10, 8.133293128500078e-12, 5.403840583859021e-13, 3.333910593753283e-14, 1.9197388159421663e-15, 1.0363384692496046e-16, 5.265409520615228e-18, 2.5266152051528173e-19, 1.1485898141193483e-20], [0.07423597230397715, 0.05840122247681102, 0.0227541207287618, 0.006551160800095355, 0.001414613258636827, 0.0002443695989244504, 3.517834321730784e-05, 4.340670280806783e-06, 4.6864745943274235e-07, 4.4976247041109455e-08, 3.884746372713228e-09, 3.0503483652998134e-10, 2.1955718346136433e-11, 1.4587596926868711e-12, 8.999848011274937e-14, 5.1823098067467175e-15, 2.797582133413977e-16, 1.4213904083525014e-17, 6.820564676196698e-19, 3.1006031696654545e-20], [0.1100499752170567, 0.09505378286696105, 0.030846009722982973, 0.008842386416833178, 0.001909364988119408, 0.00032983626690785554, 4.748173853813676e-05, 5.8587913046492e-06, 6.32553841375889e-07, 6.070639510339161e-08, 5.243410993425993e-09, 4.117187743513145e-10, 2.963458715177103e-11, 1.9689513485686964e-12, 1.2147485955054297e-13, 6.994788746802181e-15, 3.776018176216173e-16, 1.918512401596093e-17, 9.20601253552745e-19, 4.1850188368205925e-20], [0.0990261558957069, 0.08553214757290978, 0.03693846439994535, 0.007991295016825757, 0.0017181019314397078, 0.0002967962284630568, 4.272544390312566e-05, 5.271910147642473e-06, 5.691902718285078e-07, 5.462537300456482e-08, 4.718173115769946e-09, 3.7047648083235135e-10, 2.6666060045975875e-11, 1.7717194648146221e-12, 1.0930659780282043e-13, 6.294113556429156e-15, 3.3977705478397134e-16, 1.726333039090555e-17, 8.283836781634082e-19, 3.7658011911776767e-20], [0.06682995292915556, 0.05772322821707107, 0.024928725292775483, 0.007177253293200013, 0.0011645492593189057, 0.00020029938351466282, 2.8834194148971824e-05, 3.5578631102750728e-06, 3.8413042220981073e-07, 3.686511986264931e-08, 3.184161642814843e-09, 2.5002410273767495e-10, 1.799617001750002e-11, 1.1956833764397698e-12, 7.376793252180881e-14, 4.24771929095105e-15, 2.2930592803718377e-16, 1.1650533608915902e-17, 5.590527241837666e-19, 2.5414327565336978e-20], [0.03608131664298422, 0.03116461980997088, 0.013458953528638478, 0.0038749802648128705, 0.0008367369733132704, 0.0001086121815920767, 1.556750594059533e-05, 1.9208809796755548e-06, 2.073910093973566e-07, 1.990338171053121e-08, 1.7191205356472012e-09, 1.3498735856987918e-10, 9.716085083147189e-12, 6.455463249511668e-13, 3.9827113663228326e-14, 2.29333252575813e-15, 1.2380167028388664e-16, 6.290092597381333e-18, 3.0183110233192086e-19, 1.3721128924413747e-20], [0.01623350700335614, 0.014021413878766115, 0.006055378148388074, 0.001743409751066774, 0.00037646008460972153, 6.5032191184036e-05, 7.034556441158062e-06, 8.642321771325932e-07, 9.33082192315096e-08, 8.95481973635804e-09, 7.734572308205556e-10, 6.073276794168118e-11, 4.371407418502363e-12, 2.904406424737067e-13, 1.791879534144418e-14, 1.0318035227563663e-15, 5.570016475469838e-17, 2.830003772913957e-18, 1.3579818502794773e-19, 6.173334656614696e-21], [0.0062603056685750415, 0.005407231891946012, 0.002335202007790555, 0.0006723302577191664, 0.00014517843871858618, 2.507907841633404e-05, 3.6102708028600994e-06, 3.3473515107152974e-07, 3.598347379028429e-08, 3.4533455244760114e-09, 2.9827681014984737e-10, 2.3421044592210114e-11, 1.6857938728854812e-12, 1.1200581612382437e-13, 6.9102219272081725e-15, 3.9790572924457725e-16, 2.148026653035054e-17, 1.091365449129336e-18, 5.236934615156815e-20, 2.380690872084867e-21], [0.002112451651630426, 0.001824593964832717, 0.0007879809069084457, 0.0002268683413478181, 4.898841189043897e-05, 8.462580491538945e-06, 1.2182348473202997e-06, 1.503185003381491e-07, 1.219500629834063e-08, 1.1652826304390928e-09, 1.0064929311790638e-10, 7.903100415699941e-12, 5.688473118751038e-13, 3.7794779326940215e-14, 2.3317567058329196e-15, 1.34267663503281e-16, 7.248212293734398e-18, 3.6826584317094717e-19, 1.767129556117449e-20, 8.033304811299846e-22], [0.0006336150649251458, 0.0005472741696110399, 0.00023634934939468081, 6.804756867292626e-05, 1.4693730744835383e-05, 2.5382916969684126e-06, 3.654010028031494e-07, 4.5086980465420794e-08, 4.867888478432369e-09, 3.5104087813873924e-10, 3.018904993368784e-11, 2.370479570095142e-12, 1.7062176365932565e-13, 1.1336279123163753e-14, 6.993940786363841e-16, 4.0272644470853315e-17, 2.174050468582858e-18, 1.104587581686797e-19, 5.300381230341124e-21, 2.4095334658412994e-22], [0.00017104355745667005, 0.00014773594577565158, 6.380219751847526e-05, 1.8369352097822022e-05, 3.966553382382099e-06, 6.852085213022767e-07, 9.863952244422868e-08, 1.2171171363635466e-08, 1.3140801233186802e-09, 1.2611269104014972e-10, 8.184994172111218e-12, 6.399078572971284e-13, 4.605912177809404e-14, 3.060213711580198e-15, 1.8880051611182839e-16, 1.0871547663242865e-17, 5.868820784440837e-19, 2.981819719145884e-20, 1.4308309756195765e-21, 6.504504053373237e-23], [4.197544041964896e-05, 3.625556835905559e-05, 1.5657563373925232e-05, 4.507984141554193e-06, 9.734235398823206e-07, 1.6815558497867226e-07, 2.4206918161353328e-08, 2.9869016173908832e-09, 3.2248564484506527e-10, 3.0949050801041855e-11, 2.673171301473245e-12, 1.5772251239710454e-13, 1.1303272398713482e-14, 7.510006236532366e-16, 4.6333138371836304e-17, 2.6679636929524666e-18, 1.4402549902138233e-19, 7.317621185167973e-21, 3.5113722645135283e-22, 1.5962566869605668e-23], [9.44267933406787e-06, 8.155952687245259e-06, 3.522282282560937e-06, 1.0141036822054014e-06, 2.1897867542181346e-07, 3.782781672596636e-08, 5.445521561619741e-09, 6.719251517901442e-10, 7.254548144506437e-11, 6.962213129542633e-12, 6.013492449987215e-13, 4.721864725431168e-14, 2.553829366179564e-15, 1.6894302949405012e-16, 1.0422975049511214e-17, 6.001777557453043e-19, 3.239957912511624e-20, 1.646151884266536e-21, 7.899086223957784e-23, 3.590895027935062e-24], [1.9607991746077628e-06, 1.6936067329526792e-06, 7.314119168977164e-07, 2.1058150898558855e-07, 4.5471543704197856e-08, 7.855053548825241e-09, 1.1307780139064522e-09, 1.3952716558688136e-10, 1.5064275202674437e-11, 1.4457233243744506e-12, 1.2487187815330928e-13, 9.805086171708812e-15, 7.057479492984944e-16, 3.5234316743858044e-17, 2.1643603633032147e-18, 1.2462861508359188e-19, 6.727864598447478e-21, 3.418281127373967e-22, 1.640267682522221e-23, 7.456595482889222e-25], [3.780822648241198e-07, 3.265620863208579e-07, 1.4103120688805734e-07, 4.060443051914208e-08, 8.767845504714241e-09, 1.5146153030427889e-09, 2.180371748660052e-10, 2.6903696948021583e-11, 2.904700981272246e-12, 2.7876508510765253e-13, 2.407785719029024e-14, 1.8906215560483895e-15, 1.360826679861947e-16, 9.041467366358486e-18, 4.19150959865486e-19, 2.4030951085097082e-20, 1.2972701731781776e-21, 6.591146544630835e-23, 3.1627722428528023e-24, 1.4377844220645443e-25], [6.804187501910935e-08, 5.877000518328965e-08, 2.538079313859202e-08, 7.307408581809049e-09, 1.577912278683978e-09, 2.725789457477173e-10, 3.9239233315145895e-11, 4.841745185114263e-12, 5.227468186786047e-13, 5.0168179904999944e-14, 4.333190689152833e-15, 3.4024720965137393e-16, 2.449022540555019e-17, 1.6271548542942214e-18, 1.003876543399917e-19, 4.343588045198702e-21, 2.3346425686079094e-22, 1.186180921845227e-23, 5.691908181998641e-25, 2.587520152420993e-26], [1.147988443964153e-08, 9.915553735575616e-09, 4.2821949297495565e-09, 1.2328908638812927e-09, 2.66222096467744e-10, 4.5988956021336774e-11, 6.620362296475458e-12, 8.168892346910239e-13, 8.819676218409981e-14, 8.464271563574623e-15, 7.310869718454199e-16, 5.740580556622328e-17, 4.1319401835638806e-18, 2.7453020198889756e-19, 1.6937197434170126e-20, 9.752809631000752e-22, 3.956118994302726e-23, 2.0012999205954146e-24, 9.603269773509813e-26, 4.365610490112779e-27], [1.822929281648621e-09, 1.5745239722034675e-09, 6.799840684991668e-10, 1.9577486765332393e-10, 4.227429793605906e-11, 7.30274028493298e-12, 1.051269492199215e-12, 1.297165762958063e-13, 1.4005059125579118e-14, 1.3440700176201208e-15, 1.1609174773630842e-16, 9.115660044620058e-18, 6.561246143410113e-19, 4.3593569825002426e-20, 2.6895142816243127e-21, 1.5486812910157753e-22, 8.360293520965828e-24, 3.1917743885324214e-25, 1.524935356426706e-26, 6.932299045814676e-28], [2.7338742977958067e-10, 2.3613371413823956e-10, 1.0197822737803966e-10, 2.9360649599514474e-11, 6.339939664594812e-12, 1.0952028786547635e-12, 1.5766045746881963e-13, 1.945378888271817e-14, 2.1003596556364705e-15, 2.015721900240937e-16, 1.741045297354902e-17, 1.3670891654608146e-18, 9.839998936633646e-20, 6.537792842186261e-21, 4.0335047783300406e-22, 2.322580486038494e-23, 1.2538057185809633e-24, 6.370313139488369e-26, 2.2969305155742817e-27, 1.0396472521878248e-28], [3.8842409915968066e-11, 3.354946687538808e-11, 1.4488888949704984e-11, 4.171509963215669e-12, 9.007675864733187e-13, 1.5560451769181488e-13, 2.2400123229807467e-14, 2.7639604454764873e-15, 2.98415442074165e-16, 2.863902571851182e-17, 2.473646837992938e-18, 1.942336478283603e-19, 1.3980499124541725e-20, 9.288782213821e-22, 5.730733345136892e-23, 3.2998819065774645e-24, 1.7813853297999786e-25, 9.050829968904662e-27, 4.3430552797753415e-28, 1.4835470963113125e-29]] |
| Legacy trial inputs | {"lambda_home": 2.6994869112980626, "lambda_away": 0.8637328875311605, "rho": -0.10363035671928646, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8033 |
| Legacy p draw | 0.1267 |
| Legacy p away | 0.0700 |
| Legacy p over 1 5 | 0.8835 |
| Legacy p under 3 5 | 0.5126 |
| Legacy p btts yes | 0.5346 |
| Legacy p over 2 5 | 0.7066 |
| Legacy goal margin distribution | {"-1": 0.047589048120250096, "-10": 1.775585684355299e-09, "-11": 1.3703568928470488e-10, "-12": 9.72005752849343e-12, "-13": 6.377290628382835e-13, "-14": 3.891685366614518e-14, "-15": 2.2195359513052537e-15, "-16": 1.1880601027395e-16, "-17": 5.989316176603104e-18, "-18": 2.836675522119363e-19, "-19": 1.1485898141193483e-20, "-2": 0.01721722787536212, "-3": 0.004217766511590301, "-4": 0.0008215584984004145, "-5": 0.00013216943297380122, "-6": 1.8062665548062233e-05, "-7": 2.1422932903435407e-06, "-8": 2.2421491854597477e-07, "-9": 2.0985403189830382e-08, "0": 0.12669830537141438, "1": 0.21431100761460634, "10": 0.00021104103678393056, "11": 5.090503442656748e-05, "12": 1.1284898367751586e-05, "13": 2.3140183368320322e-06, "14": 4.413367353489947e-07, "15": 7.86676742403701e-08, "16": 1.3160558149186253e-08, "17": 2.0735518847365655e-09, "18": 3.0693689665496874e-10, "19": 3.8842409915968066e-11, "2": 0.22478863217804912, "3": 0.17210576631344215, "4": 0.10477390954926077, "5": 0.05268020470434558, "6": 0.022500907667855223, "7": 0.008340630744469908, "8": 0.002728263059598944, "9": 0.0007980697039862668} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7539 |
| Legacy raw p draw | 0.1583 |
| Legacy raw p away | 0.0878 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.6995 |
| Legacy lambda away | 0.8637 |
| Legacy model home team | Feyenoord |
| Legacy model away team | For Sittard |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 92.2% |
| Market reference home draw last update utc | 2026-10-31T12:02:13Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.0% |
| Market reference draw away last update utc | 2026-10-31T12:02:13Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.8% |
| Market reference home away last update utc | 2026-10-31T12:02:13Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.03 |
| Market reference dc draw away odds | 5.00 |
| Market reference dc home away odds | 1.07 |
| Market p over 1 5 | 92.2% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 8.50 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:13Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 43.2% |
| Market under 3 5 odds | 2.20 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market reference under 3 5 odds | 2.20 |
| Market reference under 3 5 opposite odds | 1.70 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.2% |
| Market reference btts yes odds | 1.87 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-31T12:02:36Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,614.9048 |
| Elo away rating | 1,453.3704 |
| Elo rating diff | 221.5344 |
| Elo home expectancy | 0.7816 |

</details>


---

## 2026-10-31 — Heerenveen vs NEC Nijmegen

The model's most likely 1X2 outcome is **Heerenveen win** at **43.2%**. Expected goals are 1.62 for Heerenveen and 1.62 for NEC Nijmegen (3.24 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 71.4%; Under 3.5 goals: 49.0%; Double Chance 1X: 67.5%; Double Chance X2: 56.8%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 68.5%; BTTS Yes (both teams score): 72.4%; BTTS No (at least one team does not score): 27.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Heerenveen win | 43.2% | 2.32 |
| Draw | 24.4% | 4.10 |
| NEC Nijmegen win | 32.5% | 3.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Heerenveen expected goals | 1.62 |
| NEC Nijmegen expected goals | 1.62 |
| Expected total goals | 3.24 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 89.3% |
| Under 1.5 | 10.7% |
| Over 2.5 | 71.4% |
| Under 2.5 | 28.6% |
| Over 3.5 | 51.0% |
| Under 3.5 | 49.0% |
| Over 4.5 | 31.5% |
| Under 4.5 | 68.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.66% |
| 2 | 2-1 | 8.77% |
| 3 | 2-2 | 7.64% |
| 4 | 1-2 | 6.57% |
| 5 | 3-1 | 5.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Heerenveen win | 43.2% | 45.7% | 2.14 | -7.6% |
| Draw | 24.4% | 24.0% | 4.00 | -2.5% |
| NEC Nijmegen win | 32.5% | 30.3% | 3.19 | +3.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:45:00+00:00 |
| Fixture id | c27c8af8c7ee29d153de0b9999ea0434 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Heerenveen |
| Matched away-team name | Nijmegen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.6167 |
| Dc lambda away | 1.6241 |
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
| P btts yes | 72.4% |
| P btts no | 27.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.51 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.38 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.50 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.18 |
| Fair Under 4.5 odds | 1.46 |
| Goal margin distribution | {"-1": 0.147925391710701, "-10": 3.9065391283954605e-06, "-11": 6.45995212825075e-07, "-12": 9.82935542842708e-08, "-13": 1.3846241049268612e-08, "-14": 1.8132691787713977e-09, "-15": 2.1845241686392835e-10, "-16": 2.0938486270550896e-11, "-2": 0.09867235676395697, "-3": 0.04910418155671497, "-4": 0.01980447888097153, "-5": 0.006674676859753105, "-6": 0.0019255199078877937, "-7": 0.0004845575438931676, "-8": 0.0001079957096940772, "-9": 2.1581580062513023e-05, "0": 0.24369640872096635, "1": 0.19739224887928036, "10": 5.005478369840008e-06, "11": 8.239737985935452e-07, "12": 1.2480725556593698e-07, "13": 1.7501584688122254e-08, "14": 2.281594479363591e-09, "15": 2.736300081835462e-10, "16": 2.6108555408063826e-11, "2": 0.13110020690692842, "3": 0.06494669332440609, "4": 0.02607550203104778, "5": 0.008748431514072478, "6": 0.002512341407063233, "7": 0.0006293709514571164, "8": 0.00013963636330341397, "9": 2.7778318701425907e-05} |
| Raw goal margin distribution | {"-1": 0.18281958930441553, "-10": 1.743926445524299e-06, "-11": 2.52539719205202e-07, "-12": 3.361981109227242e-08, "-13": 4.138064560890987e-09, "-14": 4.68512325125596e-10, "-15": 4.3170230286768657e-11, "-2": 0.11450411037095812, "-3": 0.05186681435039453, "-4": 0.018781463843431025, "-5": 0.005635183407390889, "-6": 0.0014392619212783868, "-7": 0.0003194617303491118, "-8": 6.26335771917984e-05, "-9": 1.0989249362168736e-05, "0": 0.2522382820434992, "1": 0.18194804518612037, "10": 1.6666142152606071e-06, "11": 2.402521613454324e-07, "12": 3.183930437851188e-08, "13": 3.901182396541183e-09, "14": 4.3969416863325084e-10, "15": 4.0331534199579506e-11, "2": 0.11347036726844735, "3": 0.05116602162044598, "4": 0.01844387651335173, "5": 0.005508857198365806, "6": 0.0014006318127725017, "7": 0.0003094807797791851, "8": 6.0402199148552035e-05, "9": 1.0549800685695761e-05} |
| Unadjusted home-win probability | 37.2% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 37.5% |
| Raw p over 1 5 | 84.4% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 65.3% |
| P home draw | 67.5% |
| P draw away | 56.8% |
| P home away | 75.6% |
| Raw p home draw | 62.5% |
| Raw p draw away | 62.8% |
| Raw p home away | 74.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1488 |
| Totals anchor target over 2 5 | 0.7143 |
| Totals anchor reference over odds | 1.37 |
| Totals anchor reference under odds | 3.23 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6316 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.35, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.87, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.14 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.19 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.14 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:15Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:15Z |
| Home probability edge | -2.5% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Raw edge prob home | -0.0847 |
| Raw ev home | -0.2032 |
| Raw edge prob draw | 0.0122 |
| Raw ev draw | 0.0090 |
| Raw edge prob away | 0.0725 |
| Raw ev away | 0.1977 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.04747378050154189, 0.04673967947734426, 0.045688608853932514, 0.02470005640436851, 0.010014959992480827, 0.0032485569104450255, 0.0008781131767145814, 0.00020345282247120463, 4.1246300090352224e-05, 7.4328223471798895e-06, 1.2054939020310633e-06, 1.7773935414812842e-07, 2.4022246369824323e-08, 2.996964022886983e-09, 3.4718804219652365e-10, 3.753917854050964e-11], [0.05759994686328879, 0.10947975585678546, 0.07513419726113936, 0.04061885351292236, 0.016469443883553633, 0.005342200645761306, 0.0014440432810683044, 0.0003345749603748624, 6.78288905050331e-05, 1.2223159217331939e-05, 1.982415724713112e-06, 2.922895669318143e-07, 3.950420559260952e-08, 4.928460106982379e-09, 5.709452641138392e-10, 6.173258753622605e-11], [0.05692940510242329, 0.0923310789518142, 0.0661441092474473, 0.033398532248137734, 0.013541870463644865, 0.00439258238755357, 0.001187353209640025, 0.000275101624912783, 5.5771770765687615e-05, 1.0050396355089339e-05, 1.6300257093662778e-06, 2.4033279333846156e-07, 3.248202177843567e-08, 4.052387489576605e-09, 4.694552447020963e-10, 5.075913368489594e-11], [0.031206503183317535, 0.05061233476873771, 0.04104286237543218, 0.01960151521103963, 0.0074231308577967, 0.0024078441714533235, 0.0006508612139840632, 0.00015080009562951077, 3.057193270871896e-05, 5.509239474475871e-06, 8.935171972500188e-07, 1.317411637602559e-07, 1.780539097862792e-08, 2.2213624552371355e-09, 2.5733725061527965e-10, 2.7824198480035044e-11], [0.012829650676724109, 0.020807796733965638, 0.016873585097197014, 0.009122153510454393, 0.0032674627287869714, 0.0009899154487852569, 0.00026758275239591883, 6.199709520730528e-05, 1.256876539037729e-05, 2.264964374147813e-06, 3.6734373752236136e-07, 5.416156692918858e-08, 7.320171218043089e-09, 9.132488878894282e-10, 1.0579676332552359e-10, 1.1439113980880758e-11], [0.004219631671510307, 0.0068436187644829215, 0.005549668956866483, 0.0030002475386898667, 0.0012164894919917608, 0.0003485873435906325, 8.800712390464101e-05, 2.0390649213309905e-05, 4.133827323080366e-06, 7.449396440181935e-07, 1.2081819748938892e-07, 1.7813568658393487e-08, 2.407581242143358e-09, 3.0036468087950775e-10, 3.4796222011061656e-11, 3.762288534894518e-12], [0.0011565196312213763, 0.0018757038684579287, 0.0015210571905435247, 0.0008223099661626404, 0.0003334162998543021, 0.00010815038959315915, 2.582558067342701e-05, 5.588683549742384e-06, 1.1330023147519346e-06, 2.041735842014238e-07, 3.311393696958561e-08, 4.882355489612685e-09, 6.598715686723743e-10, 8.232416405158887e-11, 9.5369731248904e-12, 1.0311707010596104e-12], [0.00027169690116341893, 0.00044065220753931715, 0.0003573363685375315, 0.0001931822543870155, 7.832826440837745e-05, 2.5407373051718842e-05, 6.867833834365833e-06, 1.4057076109479616e-06, 2.6617206454505657e-07, 4.7965748811692026e-08, 7.779335358497709e-09, 1.1469938089205301e-09, 1.5502119941084706e-10, 1.934011292144178e-11, 2.2404860017594798e-12, 2.422491382636791e-13], [5.585015904214693e-05, 9.058070139173723e-05, 7.345425335698084e-05, 3.9710646626572414e-05, 1.6101199557193246e-05, 5.222753074125637e-06, 1.411755563946097e-06, 3.2709411695529027e-07, 5.858089511057024e-08, 9.859864754575838e-09, 1.5991243004754292e-09, 2.3577665543575386e-10, 3.1866239934744914e-11, 3.9755638652128825e-12, 4.605554903061164e-13, 4.9796861288866036e-14], [1.0204967379054059e-05, 1.655094844361936e-05, 1.3421595788027795e-05, 7.2559480648837325e-06, 2.9420187706323216e-06, 9.543039028785122e-07, 2.5795664192103573e-07, 5.976679119016016e-08, 1.2116612465357503e-08, 1.9289100044846876e-09, 2.921927457554664e-10, 4.3081221588797915e-11, 5.822614377548617e-12, 7.264169028995477e-13, 8.41529162212659e-14, 9.098905961013772e-15], [1.6781908036478664e-06, 2.721777389190107e-06, 2.207160276472635e-06, 1.1932292247428168e-06, 4.83810350552264e-07, 1.5693377295679663e-07, 4.2420563254352615e-08, 9.828554625734269e-09, 1.9925578255609183e-09, 3.590704693859704e-10, 5.144615794426626e-11, 7.0846389993005774e-12, 9.575197586271648e-13, 1.1945811493357132e-13, 1.3838814457412648e-14, 1.4963007464748482e-15], [2.5088712093367767e-07, 4.0690182040800403e-07, 3.299672993081139e-07, 1.7838605965359902e-07, 7.232895429061136e-08, 2.3461374230395133e-08, 6.34181343392861e-09, 1.4693548359518126e-09, 2.978845403408272e-10, 5.3680520761245386e-11, 8.70618688472833e-12, 1.1339882576910495e-12, 1.4314783215168098e-13, 1.7858817044344128e-14, 2.0688829356045842e-15, 2.2369481796585866e-16], [3.438165972393471e-08, 5.576196928026387e-08, 4.521883531772164e-08, 2.4446088662019763e-08, 9.911985459250468e-09, 3.215155016500717e-09, 8.69084354376449e-10, 2.0136090603378493e-10, 4.082220268981621e-11, 7.356397537459266e-12, 1.1930989277159492e-12, 1.7591182542671463e-13, 2.1003276345362325e-14, 2.4473785996091875e-15, 2.835204487017716e-16, 3.065521691463306e-17], [4.349238277013845e-09, 7.053821518295194e-09, 5.72012785260948e-09, 3.09240058175885e-09, 1.2538541451088286e-09, 4.067132121188274e-10, 1.0993811730899601e-10, 2.5471910519975938e-11, 5.163959154856284e-12, 9.305753709317056e-13, 1.5092556806017202e-13, 2.2252632673012998e-14, 3.007540040923174e-15, 3.314677825982372e-16, 3.5864993072206667e-17, 3.877847778897923e-18], [5.108752719735705e-10, 8.285641662029843e-10, 6.719042936483751e-10, 3.6324314457702707e-10, 1.472816701681075e-10, 4.77738191431329e-11, 1.2913678672730222e-11, 2.9920111030370515e-12, 6.065749608708355e-13, 1.0930832376538653e-13, 1.7728194161724596e-14, 2.613864553946417e-15, 3.5327515728408515e-16, 4.4073852222667305e-17, 4.510516052614998e-18, 4.555042544316033e-19], [5.600842226416591e-11, 9.083738094110391e-11, 7.366240149848393e-11, 3.982317513126004e-11, 1.6146825706948146e-11, 5.237552848083253e-12, 1.4157560715200277e-12, 3.2802100722275993e-13, 6.650019761590895e-14, 1.1983721057371232e-14, 1.943582394887103e-15, 2.8656393783400883e-16, 3.873036192996692e-17, 4.831917028513572e-18, 5.597610783360859e-19, 5.346686199021322e-20]] |
| Legacy trial inputs | {"lambda_home": 1.6444842411670935, "lambda_away": 1.6218521656022709, "rho": -0.10363035671928646, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4177 |
| Legacy p draw | 0.2463 |
| Legacy p away | 0.3359 |
| Legacy p over 1 5 | 0.8482 |
| Legacy p under 3 5 | 0.5873 |
| Legacy p btts yes | 0.6567 |
| Legacy p over 2 5 | 0.6361 |
| Legacy goal margin distribution | {"-1": 0.16377932743200999, "-10": 1.532596412248411e-06, "-11": 2.215647235949107e-07, "-12": 2.9447985919988833e-08, "-13": 3.618668420685718e-09, "-14": 4.089206297327497e-10, "-15": 3.753917854050964e-11, "-2": 0.10254633301480705, "-3": 0.046279287006630546, "-4": 0.016708661942083557, "-5": 0.005000664573144371, "-6": 0.0012743549843171238, "-7": 0.0002822822802911954, "-8": 5.5238856495931885e-05, "-9": 9.674325332490694e-06, "0": 0.24634250273988287, "1": 0.20142788899509387, "10": 2.1335563791783666e-06, "11": 3.1274860803683505e-07, "12": 4.214720871100954e-08, "13": 5.251464844715314e-09, "14": 6.017126529146744e-10, "15": 5.600842226416591e-11, "2": 0.1277758697497631, "3": 0.058470097948385875, "4": 0.021404608321286527, "5": 0.00649548805612548, "6": 0.001678390207082164, "7": 0.00037696808467386247, "8": 7.479698576226357e-05, "9": 1.3282461199934624e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3785 |
| Legacy raw p draw | 0.2526 |
| Legacy raw p away | 0.3689 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6445 |
| Legacy lambda away | 1.6219 |
| Legacy model home team | Heerenveen |
| Legacy model away team | Nijmegen |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Market p home draw | 68.6% |
| Market reference home draw last update utc | 2026-10-31T12:02:43Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.3% |
| Market reference draw away last update utc | 2026-10-31T12:02:43Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.1% |
| Market reference home away last update utc | 2026-10-31T12:02:43Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 89.8% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.56 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.1% |
| Market under 3 5 odds | 1.98 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.98 |
| Market reference under 3 5 opposite odds | 1.91 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.7% |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 3.30 |
| Market reference btts yes last update utc | 2026-10-31T12:02:36Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,510.9156 |
| Elo away rating | 1,535.4128 |
| Elo rating diff | 35.5028 |
| Elo home expectancy | 0.5509 |

</details>


---

## 2026-10-31 — PSV Eindhoven vs Willem II

The model's most likely 1X2 outcome is **PSV Eindhoven win** at **92.4%**. Expected goals are 4.46 for PSV Eindhoven and 0.68 for Willem II (5.14 combined). The most likely exact score is 4-0 at 9.6%. Goal-market probabilities: at least one goal: 99.2%; Over 2.5 goals: 88.2%; Under 3.5 goals: 25.5%; Double Chance 1X: 97.1%; Double Chance X2: 7.6%; Double Chance 12 (either team wins): 95.3%; Under 4.5 goals: 42.6%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PSV Eindhoven win | 92.4% | 1.08 |
| Draw | 4.7% | 21.14 |
| Willem II win | 2.9% | 34.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| PSV Eindhoven expected goals | 4.46 |
| Willem II expected goals | 0.68 |
| Expected total goals | 5.14 |
| Over 0.5 | 99.2% |
| Under 0.5 | 0.8% |
| Over 1.5 | 96.3% |
| Under 1.5 | 3.7% |
| Over 2.5 | 88.2% |
| Under 2.5 | 11.8% |
| Over 3.5 | 74.5% |
| Under 3.5 | 25.5% |
| Over 4.5 | 57.4% |
| Under 4.5 | 42.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-0 | 9.59% |
| 2 | 3-0 | 8.66% |
| 3 | 5-0 | 8.50% |
| 4 | 4-1 | 6.48% |
| 5 | 6-0 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 92.4% | 91.8% | 1.08 | -0.2% |
| Draw | 4.7% | 4.8% | 15.26 | -27.8% |
| Willem II win | 2.9% | 3.4% | 20.52 | -40.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:45:00+00:00 |
| Fixture id | 49a7de86105dbc67bec3e1390c7bcbb3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:36Z |
| Market best draw last update utc | 2026-10-31T12:02:36Z |
| Market best away last update utc | 2026-10-31T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | PSV Eindhoven |
| Matched away-team name | Willem II |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.4600 |
| Dc lambda away | 0.6806 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 24 |
| Score grid omitted mass | 0 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 126.74 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 27.18 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.48 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.91 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.35 |
| Goal margin distribution | {"-1": 0.021764015717352085, "-10": 7.61352121067357e-11, "-11": 4.5767493424204934e-12, "-12": 2.5303275448998135e-13, "-13": 1.294706613471319e-14, "-14": 6.164479712893077e-16, "-15": 2.7441347603058073e-17, "-16": 1.1468418364403955e-18, "-17": 4.5163674574548035e-20, "-18": 1.6814644866899014e-21, "-19": 5.935765987643369e-23, "-2": 0.005946986041371522, "-20": 1.9920885550602217e-24, "-21": 6.371232256343414e-26, "-22": 1.945613455303567e-27, "-23": 5.650110405930873e-29, "-24": 1.4148474084648805e-30, "-3": 0.0010988189696613678, "-4": 0.0001633285485546834, "-5": 2.0193427221150605e-05, "-6": 2.1305506611766102e-06, "-7": 1.9568279566620196e-07, "-8": 1.589418444032727e-08, "-9": 1.1563030338309372e-09, "0": 0.04730984479361005, "1": 0.08995233901044024, "10": 0.006274662765451813, "11": 0.002471887184139605, "12": 0.0008956017878084615, "13": 0.00030031447513536203, "14": 9.370613330880253e-05, "15": 2.733655074558307e-05, "16": 7.487011471313146e-06, "17": 1.9322393892981877e-06, "18": 4.714395911930665e-07, "19": 1.0906409846056384e-07, "2": 0.14406823041494388, "20": 2.3987245159099582e-08, "21": 5.02761323871144e-09, "22": 1.00614755391556e-09, "23": 1.914823458893317e-10, "24": 3.142303285449711e-11, "3": 0.17444725562164723, "4": 0.16992872016891497, "5": 0.137683344799787, "6": 0.09519846166064082, "7": 0.05730036653327133, "8": 0.030500692132587423, "9": 0.014541519900021952} |
| Raw goal margin distribution | {"-1": 0.01229549305157168, "-10": 4.5177717185242607e-11, "-11": 2.7334701324676276e-12, "-12": 1.5211464094448566e-13, "-13": 7.834612613901992e-15, "-14": 3.7549700227607156e-16, "-15": 1.6826322615468708e-17, "-16": 7.078955902154253e-19, "-17": 2.80636211882605e-20, "-18": 1.0518085772327092e-21, "-19": 3.7378796112481747e-23, "-2": 0.003367778849025108, "-20": 1.2628767615906451e-24, "-21": 4.066146740625996e-26, "-22": 1.2500345804018528e-27, "-23": 3.653946423330923e-29, "-24": 9.198197035750484e-31, "-3": 0.0006251312384976531, "-4": 9.34107125464488e-05, "-5": 1.161486568728693e-05, "-6": 1.2327719301803662e-06, "-7": 1.1392261151797364e-07, "-8": 9.31147103718038e-09, "-9": 6.817350357731856e-10, "0": 0.046028431285948475, "1": 0.09000792913054521, "10": 0.006600718143420809, "11": 0.0026172663980775644, "12": 0.0009544898266229459, "13": 0.0003221695609451631, "14": 0.00010119059338346774, "15": 2.9715946685845963e-05, "16": 8.192873636429317e-06, "17": 2.1285186003775643e-06, "18": 5.228018778483593e-07, "19": 1.2175657726274978e-07, "2": 0.1446361810596932, "20": 2.695844164225764e-08, "21": 5.688313847248798e-09, "22": 1.1460121459429766e-09, "23": 2.1953110274022722e-10, "24": 3.6216233604347786e-11, "3": 0.17594270854449476, "4": 0.17229133943848476, "5": 0.14039370816545427, "6": 0.09765239084388574, "7": 0.05913937986484518, "8": 0.03167756724839262, "9": 0.015199028496765583} |
| Unadjusted home-win probability | 93.8% |
| Unadjusted draw probability | 4.6% |
| Unadjusted away-win probability | 1.6% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 24.6% |
| Raw p btts yes | 49.0% |
| P home draw | 97.1% |
| P draw away | 7.6% |
| P home away | 95.3% |
| Raw p home draw | 98.4% |
| Raw p draw away | 6.2% |
| Raw p home away | 95.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9932 |
| Totals anchor target over 2 5 | 0.8820 |
| Totals anchor reference over odds | 1.11 |
| Totals anchor reference under odds | 5.91 |
| Totals anchor reference last update utc | 2026-10-31T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8844 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": -2.5, "market_key": "spreads", "opposite_price": 2.27, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.66, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.29, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.08 |
| Reference draw odds | 15.26 |
| Reference away odds | 20.52 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:36Z |
| Market reference home last update utc | 2026-10-31T12:02:36Z |
| Market reference draw last update utc | 2026-10-31T12:02:36Z |
| Market reference away last update utc | 2026-10-31T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.38 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:15Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:15Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | 0.0198 |
| Raw ev home | 0.0126 |
| Raw edge prob draw | -0.0018 |
| Raw ev draw | -0.2976 |
| Raw edge prob away | -0.0180 |
| Raw ev away | -0.6636 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.006783944103029177, 0.002846132949858404, 0.0019099484852278495, 0.000440028173800549, 7.603272885465314e-05, 1.0510192212747806e-05, 1.2107082262787942e-06, 1.195422809871242e-07, 1.0327890778512503e-08, 7.931388295948816e-10, 5.4818771310783e-11, 3.4444247175593043e-12, 1.9838806255555663e-13, 1.0547566420930508e-14, 5.207200717123386e-16, 2.3993474587304076e-17, 1.0364616723407795e-18, 4.2139017985081604e-20, 1.618050196391554e-21, 5.88597583329053e-23, 2.034082503001128e-24, 6.694672777660671e-26, 2.1032299557222967e-27, 6.320319133055529e-29, 1.8201528126708305e-30], [0.019894730770767477, 0.01813880653037166, 0.00893925792831392, 0.0020594928982384563, 0.00035586099807514857, 4.919154615560261e-05, 5.666557603173508e-06, 5.595016260113415e-07, 4.83383087233184e-08, 3.7121800014746735e-09, 2.56571912724591e-10, 1.6121168294886887e-11, 9.28528740329367e-13, 4.936647112839412e-14, 2.4371605126990685e-15, 1.122982423825789e-16, 4.851019958666851e-18, 1.9722602652791743e-19, 7.573067105408119e-21, 2.7548521093923425e-22, 9.520250563003155e-24, 3.1333518766623275e-25, 9.843885948847963e-27, 2.9581406701082147e-28, 8.51898131664507e-30], [0.050149272463325435, 0.03466129000358468, 0.013291836156291117, 0.004819590256301612, 0.0008327798558507924, 0.00011511721975188036, 1.3260781736313002e-05, 1.3093361901930436e-06, 1.1312048802317853e-07, 8.687180509361253e-09, 6.004252268438417e-10, 3.77264838838202e-11, 2.1729271673697598e-12, 1.155265761983973e-13, 5.7034015849699034e-15, 2.627984370569109e-16, 1.1352274409837941e-17, 4.615449932146237e-19, 1.7722362850953232e-20, 6.446858056823452e-22, 2.2279128464218348e-23, 7.332616775344478e-25, 2.303649449036303e-26, 6.922590489444036e-28, 1.9935975201680055e-29], [0.07823898304661632, 0.054075840939617245, 0.018687593188580234, 0.004777518413045055, 0.0012992381708253641, 0.00017959690663763088, 2.0688437269174973e-05, 2.0427241903010806e-06, 1.764817615478434e-07, 1.3553061394696472e-08, 9.367366032707753e-10, 5.885791733376076e-11, 3.390031469224256e-12, 1.8023555263399076e-13, 8.898002263957772e-15, 4.099976221311965e-16, 1.7710933009873427e-17, 7.200664959950858e-19, 2.7649048102457113e-20, 1.005788505866402e-21, 3.475815836570923e-23, 1.143977671845708e-24, 3.593974176201774e-26, 1.0800085690941334e-27, 3.1102553421142486e-29], [0.09154676878879901, 0.06327368167105937, 0.021866193887448263, 0.005037696795845648, 0.0009659225090659937, 0.00021014481332589077, 2.420736453277103e-05, 2.390174205579316e-06, 2.0649980854472664e-07, 1.5858321894872017e-08, 1.0960675343203272e-09, 6.886914859736376e-11, 3.966646996356217e-12, 2.1089208757575944e-13, 1.0411476788436882e-14, 4.797347314041462e-16, 2.0723412116984466e-17, 8.425436841650475e-19, 3.235191608201114e-20, 1.1768645783921046e-21, 4.067022555155334e-23, 1.3385585464679285e-24, 4.2052786236449876e-26, 1.2637088432741112e-27, 3.63928332898972e-29], [0.08569447658261488, 0.05922879752059416, 0.02046835802978245, 0.004715652947815771, 0.0008148204667377481, 0.0001249862326480143, 2.2659865121686106e-05, 2.2373780112427917e-06, 1.932989360714135e-07, 1.4844550083409962e-08, 1.0259994415474105e-09, 6.446656413790872e-11, 3.713071937306186e-12, 1.974104307483857e-13, 9.74590436824141e-15, 4.490668239861421e-16, 1.939863064383859e-17, 7.88682560485365e-19, 3.028376153273728e-20, 1.10163138894172e-21, 3.8070308075839784e-23, 1.252988778657905e-24, 3.936448607691421e-26, 1.1829239776559604e-27, 3.4066355824430586e-29], [0.06684691892029958, 0.04620207490023023, 0.015966567790742667, 0.003678496944374402, 0.0006356096664189097, 8.786189667233575e-05, 1.1231029724407119e-05, 1.7452913242012859e-06, 1.5078496097107107e-07, 1.1579654551917127e-08, 8.003421482512029e-10, 5.028785235466782e-11, 2.8964226008085684e-12, 1.5399217761178237e-13, 7.602399887240756e-15, 3.502995148568079e-16, 1.5132115178548053e-17, 6.152205051838213e-19, 2.3623181242363387e-20, 8.593396806111525e-22, 2.969716250922031e-23, 9.774076770775507e-25, 3.0706700292240134e-26, 9.22752858488063e-28, 2.6573835520313755e-29], [0.044695435098558924, 0.030891802845604423, 0.010675625832339887, 0.0024595302834160386, 0.00042498369487028185, 5.874654754150745e-05, 6.7672338368573275e-06, 7.414526067347702e-07, 1.0081840039563405e-07, 7.742431616123093e-09, 5.351277384445014e-10, 3.3623650535693186e-11, 1.936616832359735e-12, 1.029628214927805e-13, 5.083144836616774e-15, 2.3421856211512837e-16, 1.0117691028857995e-17, 4.1135101819024705e-19, 1.5795019143640966e-20, 5.74574887560128e-22, 1.9856227048022414e-23, 6.535179496864854e-25, 2.0531227948427466e-26, 6.169744419744472e-28, 1.7767896561307068e-29], [0.02614887427949196, 0.018073117916746866, 0.0062457295052432095, 0.0014389377354942193, 0.00024863490384402303, 3.436941787521842e-05, 3.959141385013873e-06, 3.9091564890886894e-07, 3.747687085282703e-08, 4.529676699670255e-09, 3.130742082541062e-10, 1.967137379324363e-11, 1.133009444146913e-12, 6.023796096266882e-14, 2.973872275413341e-15, 1.3702857397330359e-16, 5.919312120554378e-18, 2.406591643123883e-19, 9.240808796658366e-21, 3.361525951326389e-22, 1.1616801214684372e-23, 3.8233789799921283e-25, 1.2011707621665625e-26, 3.609582741788701e-28, 1.0395032342075042e-29], [0.013598477976840254, 0.009398756265254195, 0.0032480333271158045, 0.0007483061372744761, 0.00012930026080887303, 1.7873494937391157e-05, 2.0589145198320173e-06, 2.0329203413007314e-07, 1.756347551092132e-08, 1.4967118701650868e-09, 1.6281131954499102e-10, 1.0229914314568086e-11, 5.892109851117903e-13, 3.132618929462113e-14, 1.5465345165876038e-15, 7.126043077254786e-17, 3.078283013220643e-18, 1.2515255191667757e-19, 4.8055963544137664e-21, 1.7481301921107787e-22, 6.041209032203344e-24, 1.988312548403405e-25, 6.2465764228163826e-27, 1.877129810452015e-28, 5.405839534863373e-30], [0.006364585380582645, 0.004398961914956601, 0.0015201984710799157, 0.00035023465932060527, 6.0517254287666644e-05, 8.365449778436923e-06, 9.63647348998176e-07, 9.514811220908529e-08, 8.22034934052269e-09, 6.312884590499382e-10, 4.8417025241596355e-11, 4.787974301388834e-12, 2.7577230542329923e-13, 1.4661803089542362e-14, 7.238347550074164e-16, 3.3352489644901065e-17, 1.440749111526112e-18, 5.857597472512008e-20, 2.2491949727295878e-21, 8.18188909303853e-23, 2.8275069278260095e-24, 9.306030424250319e-26, 2.923626382824595e-27, 8.785654519135245e-29, 2.530130749335646e-30], [0.0027080535400369416, 0.0018717047024978976, 0.00064682592894839, 0.00014902058065092234, 2.574935442095188e-05, 3.5593969649007193e-06, 4.1002020693496123e-07, 4.048436256063825e-08, 3.497658496319036e-09, 2.6860554837244547e-10, 1.8565004737641673e-11, 1.2944123030619056e-12, 1.1733775623846653e-13, 6.238418590642738e-15, 3.0798286981581217e-16, 1.419107801232001e-17, 6.130211943855159e-19, 2.4923363617592692e-20, 9.570050590752007e-22, 3.481294129573649e-23, 1.2030697504253197e-24, 3.9596025706509596e-26, 1.2439674075090732e-27, 3.7381889627361257e-29, 1.0765398093956395e-30], [0.0010562234734473265, 0.0007300219190323158, 0.00025228183981190506, 5.812257142748646e-05, 1.0043033552856958e-05, 1.3882733742383929e-06, 1.5992038589699694e-07, 1.5790136129847317e-08, 1.3641934885320804e-09, 1.0476435605674847e-10, 7.240918061129054e-12, 4.54968189749787e-13, 2.907836875975631e-14, 2.4331735156673316e-15, 1.2012271238725043e-16, 5.5349532380110024e-18, 2.3909696232293313e-19, 9.720871947681423e-21, 3.7326116070411345e-22, 1.3578108864051143e-23, 4.692338950493221e-25, 1.5443657663381605e-26, 4.851852286482401e-28, 1.4580077063652695e-29, 4.198833590153739e-31], [0.00038027018618611626, 0.00026282844307967245, 9.082856479560465e-05, 2.092576203235493e-05, 3.615774819464646e-06, 4.998174986358023e-07, 5.757584114422667e-08, 5.684893544737719e-09, 4.911480618631149e-10, 3.7718117600001485e-11, 2.606934354788578e-12, 1.638013569801048e-13, 9.434444506681135e-15, 5.566000421860893e-16, 4.3247558261124946e-17, 1.9927389906231382e-18, 8.608163770714646e-20, 3.4997875718206666e-21, 1.3438452623452094e-22, 4.888501454087005e-24, 1.6893741250879403e-25, 5.560151542439316e-27, 1.7468034168057206e-28, 5.249238214245793e-30, 1.5116983017627542e-31], [0.00012712883182292077, 8.78666646829956e-05, 3.0365066097940826e-05, 6.995730348620315e-06, 1.2087963917010736e-06, 1.6709491575846224e-07, 1.9248286328461142e-08, 1.9005273135623903e-09, 1.6419662025828593e-10, 1.260961390936097e-11, 8.715290632884532e-13, 5.476073570936768e-14, 3.154046655778388e-15, 1.6768910471727625e-16, 9.186436202076297e-18, 6.661962709901109e-19, 2.8778112091483667e-20, 1.1700204796391215e-21, 4.4926340417625523e-23, 1.634283995428881e-24, 5.647777996700071e-26, 1.8588245832208467e-27, 5.839770927876797e-29, 1.754882571337555e-30, 5.053786653622458e-32], [3.9667297367089663e-05, 2.7416543255031573e-05, 9.47464150505303e-06, 2.1828385588033345e-06, 3.771739678428033e-07, 5.213769069436759e-08, 6.005934976744543e-09, 5.930108931258434e-10, 5.123335178229977e-11, 3.934507203869622e-12, 2.719383323342325e-13, 1.708668565797718e-14, 9.841395127323017e-16, 5.232309214723665e-17, 2.5831251691436844e-18, 1.3207616341226313e-19, 8.979473134673331e-21, 3.650749371792946e-22, 1.40181143758433e-23, 5.099364817514564e-25, 1.7622445360818273e-26, 5.7999862374715705e-28, 1.822151015077674e-29, 5.475661799404584e-31, 1.5769047441441767e-32], [1.1603591838539811e-05, 8.01996603426272e-06, 2.771549365305046e-06, 6.385302091892607e-07, 1.1033201315604358e-07, 1.5251467137345425e-08, 1.7568733618028904e-09, 1.7346925090362145e-10, 1.4986927319514275e-11, 1.1509333559330224e-12, 7.954818258623246e-14, 4.9982463996423724e-15, 2.8788331890237174e-16, 1.5305701303224088e-17, 7.556231989596106e-19, 3.4817221395357303e-20, 1.6689540484375457e-21, 1.0679276993102339e-22, 4.100619108429748e-24, 1.4916808531387567e-25, 5.1549683678111226e-27, 1.6966286446478442e-28, 5.3302085220164824e-30, 1.6017563278432376e-31, 4.6128070813533626e-33], [3.1946503867650388e-06, 2.2080221322593506e-06, 7.630509048415789e-07, 1.7579735724350765e-07, 3.037612951283151e-08, 4.198967532383156e-09, 4.836947251228965e-10, 4.775879893073116e-11, 4.126135581457228e-12, 3.168699607702596e-13, 2.190085930302275e-14, 1.3760954380289394e-15, 7.925878201093272e-17, 4.213899046815152e-18, 2.0803488940272186e-19, 9.585725811841307e-21, 4.140808105716526e-22, 1.868127167736827e-23, 1.1289646001862217e-24, 4.1068307819843193e-26, 1.4192434479892656e-27, 4.671084118814494e-29, 1.4674898043071012e-30, 4.409885786616633e-32, 1.2699779629936069e-33], [8.306740562479914e-07, 5.741306493154338e-07, 1.9840875010122756e-07, 4.571088730839642e-08, 7.898411300364272e-09, 1.0918169345317067e-09, 1.2577046332461321e-10, 1.2418258784647567e-11, 1.072879146424834e-12, 8.239263260438036e-14, 5.6946687211618495e-15, 3.5781279354620275e-16, 2.0608894863442568e-17, 1.0956994318811932e-18, 5.409330114405759e-20, 2.4924836142293426e-21, 1.076694301063464e-22, 4.377474028005412e-24, 1.8651824734179281e-25, 1.0678595060442622e-26, 3.690321534490143e-28, 1.2145768463823425e-29, 3.8157718706763974e-31, 1.1466599691581911e-32, 3.302200923881722e-34], [2.046241368230761e-07, 1.4142850334159207e-07, 4.887502976918365e-08, 1.1260193801099153e-08, 1.9456555582231446e-09, 2.6895278131892146e-10, 3.0981673620434026e-11, 3.0590524231991565e-12, 2.642877403012563e-13, 2.0296193435249028e-14, 1.4027965154279867e-15, 8.814183309679153e-17, 5.076693187406452e-18, 2.699091765053138e-19, 1.3325076149012405e-20, 6.139860806668518e-22, 2.652275466174694e-23, 1.078325292223435e-24, 4.140543691535032e-26, 1.6713754690533416e-27, 9.09055547016166e-29, 2.9919285058552917e-30, 9.399583621013326e-32, 2.824625431042975e-33, 8.134478362279966e-35], [4.788579251135838e-08, 3.3096857835803884e-08, 1.1437651348712522e-08, 2.6350914040181314e-09, 4.5531900491388005e-10, 6.293987249767207e-11, 7.250278572588318e-12, 7.158742457901636e-13, 6.184816753218193e-14, 4.749680671596729e-15, 3.2828005491611043e-16, 2.0626801885513215e-17, 1.188039106188946e-18, 6.316368647272647e-20, 3.1183116594957814e-21, 1.4368397844041313e-22, 6.2068099408048344e-24, 2.5234785106415707e-25, 9.689629932000306e-27, 3.5247934668820932e-28, 1.3516801377478042e-29, 7.001660208056545e-31, 2.1996745738660425e-32, 6.6101403975709515e-34, 1.9036167926810511e-35], [1.0672525455193573e-08, 7.376447986232144e-09, 2.5491616357358845e-09, 5.87294865788732e-10, 1.0147902781444319e-10, 1.4027697071500099e-11, 1.6159027253196096e-12, 1.5955016530426623e-13, 1.3784383795835061e-14, 1.0585830412983814e-15, 7.316527635401449e-17, 4.597189617988633e-18, 2.6478370593030153e-19, 1.4077579515137832e-20, 6.949923728484113e-22, 3.20235050311647e-23, 1.3833401018282324e-24, 5.624191900774737e-26, 2.159572112670989e-27, 7.855868312229802e-29, 2.7148402800788226e-30, 9.915057619602886e-32, 4.902515266330605e-33, 1.4732322042857666e-34, 4.24267775708285e-36], [2.2705147791909595e-09, 1.5692943756365771e-09, 5.423186098533366e-10, 1.2494340520568955e-10, 2.1589045010756984e-11, 2.984307102622603e-12, 3.4377346158380073e-13, 3.3943325772946273e-14, 2.932543685361135e-15, 2.252070937061348e-16, 1.5565466860005504e-17, 9.780240875702943e-19, 5.633112051385575e-20, 2.9949192886489686e-21, 1.4785539379617162e-22, 6.812805625061562e-24, 2.9429718008496986e-25, 1.196512567276282e-26, 4.594358119953709e-28, 1.6712881296165706e-29, 5.775657322102951e-31, 1.900912858270514e-32, 6.626890285152948e-34, 3.1342117730748834e-35, 9.02603848662045e-37], [4.620365281239594e-10, 3.1934226174997254e-10, 1.1035867721721341e-10, 2.542525496081196e-11, 4.39324486838899e-12, 6.072891069410882e-13, 6.995589639276946e-14, 6.907269019715811e-15, 5.967555531344741e-16, 4.582833137159614e-17, 3.1674818118506635e-18, 1.9902220323956619e-19, 1.1463054804174554e-20, 6.0944862496421e-22, 3.0087711139376995e-23, 1.386366249026774e-24, 5.988776138756637e-26, 2.4348333580898622e-27, 9.34925107802172e-29, 3.400973964053995e-30, 1.1753126124504012e-31, 3.868246907489663e-33, 1.2152666817578655e-34, 4.05241587660486e-36, 1.8367462406729413e-37], [9.010416880235967e-11, 6.227661084564094e-11, 2.1521624970130316e-11, 4.958312439351991e-12, 8.56749744048851e-13, 1.1843063669843328e-13, 1.3642466587843833e-14, 1.3470227911261743e-15, 1.1637643307489363e-16, 8.937223475822069e-18, 6.1770725577096715e-19, 3.881236461742317e-20, 2.235470492473566e-21, 1.1885177564447544e-22, 5.867562494218473e-24, 2.70362559928787e-25, 1.1679026727975484e-26, 4.7482963477746e-28, 1.8232465314597457e-29, 6.632417860852259e-31, 2.292038823375482e-32, 7.543671357259949e-34, 2.36995535131405e-35, 7.121843291858899e-37, 2.27589082221068e-38]] |
| Legacy trial inputs | {"lambda_home": 4.680365987592331, "lambda_away": 0.6911623698814923, "rho": -0.10363035671928646, "max_goals": 24, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.9317 |
| Legacy p draw | 0.0441 |
| Legacy p away | 0.0242 |
| Legacy p over 1 5 | 0.9705 |
| Legacy p under 3 5 | 0.2220 |
| Legacy p btts yes | 0.5004 |
| Legacy p over 2 5 | 0.9003 |
| Legacy goal margin distribution | {"-1": 0.01813887479086728, "-10": 7.330397842217076e-11, "-11": 4.497877801070887e-12, "-12": 2.53889469195304e-13, "-13": 1.326611001072664e-14, "-14": 6.451241389111039e-16, "-15": 2.933490452047975e-17, "-16": 1.2524578047739163e-18, "-17": 5.0392907918091074e-20, "-18": 1.9170017757509015e-21, "-19": 6.915050809040403e-23, "-2": 0.005008421739477586, "-20": 2.371570586560108e-24, "-21": 7.751397532782022e-26, "-22": 2.4189799979347984e-27, "-23": 7.172217264720037e-29, "-24": 1.8201528126708305e-30, "-3": 0.0009342904370962541, "-4": 0.00014074996042637067, "-5": 1.767950437528628e-05, "-6": 1.8980469382384903e-06, "-7": 1.7757724825909817e-07, "-8": 1.4703525824257083e-08, "-9": 1.0910482563272147e-09, "0": 0.04409502545010597, "1": 0.07919116948546742, "10": 0.008510760424732868, "11": 0.003536292676030558, "12": 0.0013517144810568699, "13": 0.0004782815222413622, "14": 0.00015750089657739033, "15": 4.849803543938483e-05, "16": 1.4021752612200583e-05, "17": 3.820395691891511e-06, "18": 9.84149715780669e-07, "19": 2.403996113753267e-07, "2": 0.1315054873819491, "20": 5.5830841112148715e-08, "21": 1.2357136820486716e-08, "22": 2.6113786659110624e-09, "23": 5.243131389696003e-10, "24": 9.010416880235967e-11, "3": 0.16612103047229562, "4": 0.16946917831684538, "5": 0.1441492070756443, "6": 0.10479699983316576, "7": 0.0663940181583124, "8": 0.037227412304135295, "9": 0.01870617744552213} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.9456 |
| Legacy raw p draw | 0.0403 |
| Legacy raw p away | 0.0141 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 4.6804 |
| Legacy lambda away | 0.6912 |
| Legacy model home team | PSV Eindhoven |
| Legacy model away team | Willem II |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 94.9% |
| Market reference home draw last update utc | 2026-10-31T12:02:13Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 12.1% |
| Market reference draw away last update utc | 2026-10-31T12:02:13Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 93.0% |
| Market reference home away last update utc | 2026-10-31T12:02:13Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.02 |
| Market reference dc draw away odds | 8.00 |
| Market reference dc home away odds | 1.04 |
| Market p over 1 5 | 96.3% |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 13.00 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:13Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 29.9% |
| Market under 3 5 odds | 2.92 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market reference under 3 5 odds | 2.92 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.6% |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 2.08 |
| Market reference btts yes last update utc | 2026-10-31T12:02:36Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,679.0337 |
| Elo away rating | 1,344.0120 |
| Elo rating diff | 395.0217 |
| Elo home expectancy | 0.9067 |

</details>


---

## 2026-10-31 — SC Cambuur vs Go Ahead Eagles

The model's most likely 1X2 outcome is **Go Ahead Eagles win** at **40.0%**. Expected goals are 1.77 for SC Cambuur and 2.02 for Go Ahead Eagles (3.79 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 67.2%; Under 3.5 goals: 54.5%; Double Chance 1X: 60.0%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 68.4%; BTTS No (at least one team does not score): 31.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Cambuur win | 36.1% | 2.77 |
| Draw | 23.9% | 4.18 |
| Go Ahead Eagles win | 40.0% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Cambuur expected goals | 1.77 |
| Go Ahead Eagles expected goals | 2.02 |
| Expected total goals | 3.79 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 86.9% |
| Under 1.5 | 13.1% |
| Over 2.5 | 67.2% |
| Under 2.5 | 32.8% |
| Over 3.5 | 45.5% |
| Under 3.5 | 54.5% |
| Over 4.5 | 26.7% |
| Under 4.5 | 73.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.19% |
| 2 | 2-1 | 8.20% |
| 3 | 1-2 | 8.09% |
| 4 | 2-2 | 6.94% |
| 5 | 0-2 | 5.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Cambuur win | 36.1% | 37.1% | 2.62 | -5.5% |
| Draw | 23.9% | 24.4% | 3.93 | -6.0% |
| Go Ahead Eagles win | 40.0% | 38.5% | 2.53 | +1.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:00:00+00:00 |
| Fixture id | 314c3b27fe569849986fdd2d013d1aca |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:36Z |
| Market best draw last update utc | 2026-10-31T12:02:36Z |
| Market best away last update utc | 2026-10-31T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Cambuur |
| Matched away-team name | Go Ahead Eagles |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7686 |
| Dc lambda away | 2.0173 |
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
| P btts yes | 68.4% |
| P btts no | 31.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.95 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.62 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.05 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.74 |
| Fair Under 4.5 odds | 1.36 |
| Goal margin distribution | {"-1": 0.1786967555152824, "-10": 4.833843304013235e-06, "-11": 7.92995713438932e-07, "-12": 1.1964404747859656e-07, "-13": 1.670563820214862e-08, "-14": 2.1687025336235574e-09, "-15": 2.599065920843862e-10, "-16": 2.525515789406272e-11, "-2": 0.1225513471785934, "-3": 0.06182782882729174, "-4": 0.025088510218381068, "-5": 0.008466954659752246, "-6": 0.0024382637145455672, "-7": 0.0006112104149977298, "-8": 0.0001354908199607022, "-9": 2.6900806337434028e-05, "0": 0.23927626221217257, "1": 0.17994807028720386, "10": 1.4995961960412856e-06, "11": 2.1568334172766613e-07, "12": 2.852994026911274e-08, "13": 3.49250341449645e-09, "14": 3.9750057075561034e-10, "15": 4.176563285301502e-11, "16": 3.558081254051749e-12, "2": 0.10891503527248166, "3": 0.04817455864889763, "4": 0.01713849269871358, "5": 0.0050709460096691784, "6": 0.0012802843302978954, "7": 0.00028137175688172655, "8": 5.468442240107491e-05, "9": 9.518818765484693e-06} |
| Raw goal margin distribution | {"-1": 0.18557484317408743, "-10": 9.610447456792904e-06, "-11": 1.717068551424799e-06, "-12": 2.8231750789134104e-07, "-13": 4.2980120910813486e-08, "-14": 6.090674372255603e-09, "-15": 8.062757104705276e-10, "-16": 9.867749393928562e-11, "-17": 9.678290321814093e-12, "-2": 0.13233688948934805, "-3": 0.07084108804199256, "-4": 0.0307804652231136, "-5": 0.011186850487392772, "-6": 0.0034823291452984084, "-7": 0.0009460258747568981, "-8": 0.0002276861526073086, "-9": 4.9145773627326064e-05, "0": 0.22732221627915553, "1": 0.16174468652141025, "10": 2.578597918738705e-06, "11": 4.0391655643169593e-07, "12": 5.822450897746647e-08, "13": 7.771407064763007e-09, "14": 9.65520297540077e-10, "15": 1.1205819052577197e-10, "16": 1.2023811028387905e-11, "17": 1.0339193853817425e-12, "2": 0.10172060308918145, "3": 0.04773942992332, "4": 0.01818574877321315, "5": 0.005794658457542626, "6": 0.0015814440411988436, "7": 0.0003766613237488032, "8": 7.947831183483229e-05, "9": 1.5040497199802973e-05} |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 43.5% |
| Raw p over 1 5 | 89.9% |
| Raw p under 3 5 | 47.6% |
| Raw p btts yes | 72.7% |
| P home draw | 60.0% |
| P draw away | 63.9% |
| P home away | 76.1% |
| Raw p home draw | 56.5% |
| Raw p draw away | 66.3% |
| Raw p home away | 77.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9144 |
| Totals anchor target over 2 5 | 0.6723 |
| Totals anchor reference over odds | 1.45 |
| Totals anchor reference under odds | 2.84 |
| Totals anchor reference last update utc | 2026-10-31T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7247 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.2, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.62 |
| Reference draw odds | 3.93 |
| Reference away odds | 2.53 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:36Z |
| Market reference home last update utc | 2026-10-31T12:02:36Z |
| Market reference draw last update utc | 2026-10-31T12:02:36Z |
| Market reference away last update utc | 2026-10-31T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:15Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:15Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.5% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0338 |
| Raw ev home | -0.1164 |
| Raw edge prob draw | -0.0171 |
| Raw ev draw | -0.1066 |
| Raw edge prob away | 0.0508 |
| Raw ev away | 0.1017 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.026970266516482124, 0.0289486092378263, 0.037803605452756614, 0.026360930686963532, 0.013786356982893763, 0.0057680403204816225, 0.0020110636176997147, 0.00060100286352136, 0.00015715757767885652, 3.652932008738987e-05, 7.641706630884627e-06, 1.4532704660954519e-06, 2.533459544885812e-07, 4.076799879135373e-08, 6.091722757548637e-09, 8.495670159113267e-10, 1.1107758581564014e-10, 1.3668670762512375e-11], [0.02776048163265519, 0.08443539510376377, 0.07260671881378404, 0.050629580409993574, 0.026478483545024533, 0.011078268240291338, 0.0038625080559956766, 0.0011543038129658728, 0.00030184147557682484, 7.015928878419791e-05, 1.4676886978398262e-05, 2.7911940892525404e-06, 4.865837070263048e-07, 7.830022002911007e-08, 1.1699942268776665e-08, 1.6317034499480875e-09, 2.1333888509414802e-10, 2.6252451921607896e-11], [0.03403779378486147, 0.07120494820166393, 0.0768481243208466, 0.048620332167552766, 0.025427677946903537, 0.010638624245400564, 0.003709223405795595, 0.0011084949619214225, 0.00028986281706558896, 6.737499891770076e-05, 1.4094430850438173e-05, 2.680424816176858e-06, 4.6727350436956003e-07, 7.519285516054475e-08, 1.1235626976217805e-08, 1.5669488684871346e-09, 2.0487247521185148e-10, 2.5210616448034808e-11], [0.021791329978366674, 0.04558610737706131, 0.04768165109371454, 0.03430703009286444, 0.01627904923059535, 0.006810951758879379, 0.0023746812648921464, 0.0007096693648026645, 0.00018557302318296802, 4.313413621891977e-05, 9.02339309828507e-06, 1.7160343005982654e-06, 2.991530881297478e-07, 4.813920459050782e-08, 7.193158772279014e-09, 1.0031760597720657e-09, 1.3116137135808704e-10, 1.6140084326543575e-11], [0.010463267652439477, 0.021888505345592005, 0.022894696101571462, 0.015964760233963635, 0.00861500436554967, 0.0032703286716210733, 0.001140220706513408, 0.00034075297451044114, 8.910425442427663e-05, 2.071117332734591e-05, 4.332648682492597e-06, 8.239665135515623e-07, 1.4364055949144862e-07, 2.3114393784411858e-08, 3.4538481852905026e-09, 4.816823767220787e-10, 6.297809888350549e-11, 7.749780413091918e-12], [0.004019212047186563, 0.00840794169681781, 0.008794445621073014, 0.006132477806570452, 0.0032071905667907246, 0.0013845474822864671, 0.00043798829890410014, 0.00013089204116342303, 3.422725144129641e-05, 7.955697982095482e-06, 1.664282551048119e-06, 3.1650687411906537e-07, 5.517605841212022e-08, 8.878837190030463e-09, 1.3267125239061006e-09, 1.850266738600983e-10, 2.419151857235318e-11, 2.976891333950292e-12], [0.0012865695192651205, 0.002691423438197594, 0.0028151452429158053, 0.001963036269516122, 0.0010266374546214728, 0.00042953234419513127, 0.00015452463075574444, 4.189918533736887e-05, 1.0956311315652038e-05, 2.546658003627337e-06, 5.327450197911681e-07, 1.0131540513382876e-07, 1.7662127330633624e-08, 2.842159398682884e-09, 4.246871959093865e-10, 5.92279471808523e-11, 7.74382392730745e-12, 9.529175389255474e-13], [0.000353003333944685, 0.000738461025629845, 0.0007724072748555597, 0.000538609330795697, 0.0002816843076158598, 0.00011785321140249398, 4.109026506611501e-05, 1.2670507068189389e-05, 3.006144918130969e-06, 6.987409170169491e-07, 1.4617225522032306e-07, 2.779847902243676e-08, 4.8460574721453655e-09, 7.798193011057438e-10, 1.1652382074562436e-10, 1.6250705853409985e-11, 2.1247166382284294e-12, 2.614573586410022e-13], [8.474857589999094e-05, 0.00017728875129996023, 0.00018543852214455034, 0.00012930861938696356, 6.762639790693832e-05, 2.829404391168448e-05, 9.864896766816572e-06, 2.9481072368962915e-06, 7.954380881317023e-07, 1.6775279989145773e-07, 3.509284268673098e-08, 6.673822263974567e-09, 1.163435101035576e-09, 1.872179916532856e-10, 2.797488555211469e-11, 3.901448077150318e-12, 5.100991746131549e-13, 6.277033861348817e-14], [1.8085623628704226e-05, 3.783400010635897e-05, 3.9573187893176504e-05, 2.759488283248237e-05, 1.443169477388243e-05, 6.0380416270901675e-06, 2.1052012752545243e-06, 6.291357387112296e-07, 1.6451410588585458e-07, 3.945606085266e-08, 7.488927550151436e-09, 1.4242155263298493e-09, 2.482808605372111e-10, 3.995293251368457e-11, 5.969932187989439e-12, 8.325817959883857e-13, 1.0885683431722634e-13, 1.3395395818208532e-14], [3.47357817767485e-06, 7.266509568131062e-06, 7.600543100354957e-06, 5.299954526880347e-06, 2.7717938326362153e-06, 1.1596840707480452e-06, 4.043311615603549e-07, 1.208336642212457e-07, 3.159706404692757e-08, 7.344343705465884e-09, 1.5852803839817416e-09, 2.735390315605894e-10, 4.7685553830038383e-11, 7.673477971386594e-12, 1.1466027711362102e-12, 1.599081135960693e-13, 2.0907364431434615e-14, 2.572759200937757e-15], [6.064960567639667e-07, 1.2687520401395316e-06, 1.3270751898595539e-06, 9.253862608421054e-07, 4.839626297922658e-07, 2.0248394595554484e-07, 7.05973041543285e-08, 2.10978815290642e-08, 5.5169320422803234e-09, 1.2823420890633174e-09, 2.6825799170678695e-10, 5.263966011912144e-11, 8.326025465154033e-12, 1.3398098137599393e-12, 2.0019991599389973e-13, 2.7920385084149603e-14, 3.650481847937052e-15, 4.492106498136874e-16], [9.707118348398872e-08, 2.0306688017264402e-07, 2.1240164353127828e-07, 1.4811034386448664e-07, 7.745940754606051e-08, 3.240805286564647e-08, 1.129927192207086e-08, 3.3767677566752547e-09, 8.829985233577652e-10, 2.0524200088105543e-10, 4.2935350434026017e-11, 8.165280316447498e-12, 1.468733313064555e-12, 2.1443985136370772e-13, 3.204248826053963e-14, 4.468726207237119e-15, 5.842685856141927e-16, 7.189726779707063e-17], [1.434136738207144e-08, 3.000124884814374e-08, 3.1380373588834214e-08, 2.1881930128068243e-08, 1.1443909314228998e-08, 4.787989345576393e-09, 1.6693626673571083e-09, 4.988861289653573e-10, 1.3045484526712348e-10, 3.0322602766578506e-11, 6.343299959394354e-12, 1.2063444638550762e-12, 2.1029980087499173e-13, 3.4917938992579535e-14, 4.733980564437098e-15, 6.602128661432162e-16, 8.632026658538157e-17, 1.0622154734675076e-17], [1.9674609196743817e-09, 4.11580591150181e-09, 4.305005027484058e-09, 3.001934280537298e-09, 1.5699649652787234e-09, 6.568538180686533e-10, 2.2901622427540815e-10, 6.844110020736407e-11, 1.789681576431115e-11, 4.159891754856958e-12, 8.702234898104862e-13, 1.6549576655204493e-13, 2.885057112155845e-14, 4.6425846861769116e-15, 7.157887882473317e-16, 9.057316350648949e-17, 1.184208915078239e-17, 1.457230246352482e-18], [2.5191756193806865e-10, 5.269958758862797e-10, 5.512213024462005e-10, 3.84373563657074e-10, 2.0102139891381265e-10, 8.410485349053484e-11, 2.932368734077375e-11, 8.763332947650976e-12, 2.2915434551788842e-12, 5.326407138919315e-13, 1.1142512550164272e-13, 2.1190403125142082e-14, 3.694083813703764e-15, 5.944456652416065e-16, 8.882452645299907e-17, 1.278187995637245e-17, 1.5162843628996112e-18, 1.8658662399468875e-19], [3.0240018387184046e-11, 6.326023820716818e-11, 6.61682424724265e-11, 4.613994968478969e-11, 2.4130476464620553e-11, 1.0095891276648855e-11, 3.519996135017504e-12, 1.051944721246269e-12, 2.750753686504656e-13, 6.393784084737453e-14, 1.337539875363006e-14, 2.5436820490255165e-15, 4.434353904935908e-16, 7.135686654314027e-17, 1.0662437713778557e-17, 1.4870104486633658e-18, 2.0060748359376284e-19, 2.239773558061469e-20], [3.4164629749960457e-12, 7.147028115426551e-12, 7.475569215374962e-12, 5.212808661289424e-12, 2.7262178995674375e-12, 1.1406156671146219e-12, 3.976828424321715e-13, 1.1884682561580548e-13, 3.10775211937699e-14, 7.223582444937334e-15, 1.511128532810413e-15, 2.8738063017649514e-16, 5.00985341353604e-17, 8.061770645605562e-18, 1.2046230662268481e-18, 1.679997702462947e-19, 2.1965317093346712e-20, 2.7889559088698638e-21]] |
| Legacy trial inputs | {"lambda_home": 1.9206294728824498, "lambda_away": 2.0919378221667464, "rho": -0.10363035671928646, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3638 |
| Legacy p draw | 0.2327 |
| Legacy p away | 0.4035 |
| Legacy p over 1 5 | 0.9163 |
| Legacy p under 3 5 | 0.4319 |
| Legacy p btts yes | 0.7577 |
| Legacy p over 2 5 | 0.7600 |
| Legacy goal margin distribution | {"-1": 0.17020810727435087, "-10": 1.0951960309237672e-05, "-11": 2.0227470138674137e-06, "-12": 3.439509325438986e-07, "-13": 5.4173801080388706e-08, "-14": 7.94443876703512e-09, "-15": 1.0881165174535096e-09, "-16": 1.3733003773724803e-10, "-17": 1.3668670762512375e-11, "-2": 0.12195461993455889, "-3": 0.06623039972847271, "-4": 0.0293811396942517, "-5": 0.010947098172274244, "-6": 0.0035030320102821632, "-7": 0.0009801248363822317, "-8": 0.0002432802924721687, "-9": 5.421028749183721e-05, "0": 0.2327283995531904, "1": 0.16629277458037403, "10": 4.978271500135458e-06, "11": 8.44156759779015e-07, "12": 1.3178708201540535e-07, "13": 1.9057260763603812e-08, "14": 2.565837846694377e-09, "15": 3.226533693606118e-10, "16": 3.73870465026106e-11, "17": 3.4164629749960457e-12, "2": 0.10980609269217147, "3": 0.05474952732970144, "4": 0.022299054705758905, "5": 0.007628016867271978, "6": 0.002241050044251761, "7": 0.00057568333850812, "8": 0.00013119099082629479, "9": 2.683944990040121e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3565 |
| Legacy raw p draw | 0.2211 |
| Legacy raw p away | 0.4224 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9206 |
| Legacy lambda away | 2.0919 |
| Legacy model home team | Cambuur |
| Legacy model away team | Go Ahead Eagles |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 61.4% |
| Market reference home draw last update utc | 2026-10-31T12:02:43Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.7% |
| Market reference draw away last update utc | 2026-10-31T12:02:43Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.9% |
| Market reference home away last update utc | 2026-10-31T12:02:43Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.52 |
| Market reference dc draw away odds | 1.49 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 86.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:36Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.30 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.7% |
| Market under 3 5 odds | 1.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.13 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.7% |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 3.00 |
| Market reference btts yes last update utc | 2026-10-31T12:02:36Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,402.1959 |
| Elo away rating | 1,431.3227 |
| Elo rating diff | 30.8732 |
| Elo home expectancy | 0.5443 |

</details>


---

## 2026-11-01 — Excelsior vs FC Twente Enschede

The model's most likely 1X2 outcome is **FC Twente Enschede win** at **59.8%**. Expected goals are 1.09 for Excelsior and 1.84 for FC Twente Enschede (2.93 combined). The most likely exact score is 1-2 at 10.3%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 65.8%; Under 3.5 goals: 56.2%; Double Chance 1X: 40.2%; Double Chance X2: 81.4%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 74.7%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Excelsior win | 18.6% | 5.37 |
| Draw | 21.6% | 4.64 |
| FC Twente Enschede win | 59.8% | 1.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Excelsior expected goals | 1.09 |
| FC Twente Enschede expected goals | 1.84 |
| Expected total goals | 2.93 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 86.0% |
| Under 1.5 | 14.0% |
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
| Over 3.5 | 43.8% |
| Under 3.5 | 56.2% |
| Over 4.5 | 25.3% |
| Under 4.5 | 74.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.27% |
| 2 | 1-1 | 9.59% |
| 3 | 0-2 | 8.20% |
| 4 | 1-3 | 7.24% |
| 5 | 0-1 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Excelsior win | 18.6% | 17.5% | 5.18 | -3.6% |
| Draw | 21.6% | 20.1% | 4.53 | -2.4% |
| FC Twente Enschede win | 59.8% | 62.4% | 1.56 | -6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:30:00+00:00 |
| Fixture id | c0c32575c239ac72913af247ce084ea2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Excelsior |
| Matched away-team name | Twente |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.0886 |
| Dc lambda away | 1.8371 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.12 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.14 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.28 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.95 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.2278046410876125, "-10": 2.2849528338199007e-05, "-11": 4.305538693266658e-06, "-12": 7.458763278525304e-07, "-13": 1.1955125695120726e-07, "-14": 1.7826240766711967e-08, "-15": 2.4833894982090463e-09, "-16": 3.2176223552034465e-10, "-17": 3.4614908481111476e-11, "-2": 0.18306591228393124, "-3": 0.10778881407586882, "-4": 0.05075454046269265, "-5": 0.019806786543039988, "-6": 0.006580667712392591, "-7": 0.0019002732056325655, "-8": 0.0004847319454625039, "-9": 0.00011065768449682914, "0": 0.21552458646893852, "1": 0.10809264457269033, "10": 1.0042867432478536e-07, "11": 1.1212914652059621e-08, "12": 1.1509815810246093e-09, "13": 1.0931159369651435e-10, "14": 9.657892725494395e-12, "15": 7.972196215868242e-13, "16": 6.120384961844816e-14, "17": 3.9013722111290194e-15, "2": 0.0529546054215552, "3": 0.01847483105447403, "4": 0.00515456726831881, "5": 0.0011919056065951778, "6": 0.00023464339463490997, "7": 4.0148095234967864e-05, "8": 6.068216581168946e-06, "9": 8.208268210458487e-07} |
| Raw goal margin distribution | {"-1": 0.22567653459295015, "-10": 7.751660587024237e-06, "-11": 1.2755362048515444e-06, "-12": 1.9283171051804228e-07, "-13": 2.6956824980365986e-08, "-14": 3.5032784898853975e-09, "-15": 4.228022055506263e-10, "-16": 4.31528013038767e-11, "-2": 0.16809348936971638, "-3": 0.08932886245570995, "-4": 0.037501978099502814, "-5": 0.012953686039497479, "-6": 0.0037917881596391096, "-7": 0.000961709054424762, "-8": 0.00021500383335886847, "-9": 4.295020356906162e-05, "0": 0.2485199427324271, "1": 0.12954389832234756, "10": 4.1352335823542695e-08, "11": 4.031889466393343e-09, "12": 3.6116429644187303e-10, "13": 2.9916144743509376e-11, "14": 2.3036796141547525e-12, "15": 1.647385315780044e-13, "16": 9.962709561924716e-15, "2": 0.059016296463984284, "3": 0.01858332374175286, "4": 0.004622706226959537, "5": 0.0009461195478622481, "6": 0.00016409949503307547, "7": 2.466138216133923e-05, "8": 3.266859382003334e-06, "9": 3.866873762702653e-07} |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 80.0% |
| Raw p under 3 5 | 66.4% |
| Raw p btts yes | 56.8% |
| P home draw | 40.2% |
| P draw away | 81.4% |
| P home away | 78.4% |
| Raw p home draw | 46.1% |
| Raw p draw away | 78.7% |
| Raw p home away | 75.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1505 |
| Totals anchor target over 2 5 | 0.6583 |
| Totals anchor reference over odds | 1.47 |
| Totals anchor reference under odds | 2.69 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5742 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.47, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.57, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.14, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.14, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.18 |
| Reference draw odds | 4.53 |
| Reference away odds | 1.56 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:15Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:15Z |
| Home probability edge | +1.1% |
| Draw probability edge | +1.4% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0382 |
| Raw ev home | 0.1028 |
| Raw edge prob draw | 0.0471 |
| Raw ev draw | 0.1258 |
| Raw edge prob away | -0.0854 |
| Raw ev away | -0.1598 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05987615382559232, 0.09660181501056832, 0.0980701341301038, 0.05887042860777816, 0.026504455677600045, 0.009546200866939856, 0.0028652399713613866, 0.0007371309464586462, 0.00016593436603941448, 3.320286152404918e-05, 5.979394357712434e-06, 9.789177318934306e-07, 1.4690840121587636e-07, 2.0350962931648666e-08, 2.617812943608912e-09, 3.1428889411081046e-10, 3.53745346386917e-11], [0.044379517841140595, 0.10785939422034826, 0.10698231121614933, 0.06422031101120058, 0.0289130625859443, 0.010413717092748848, 0.003125620221121341, 0.0008041181244483132, 0.00018101374232375886, 3.6220189727895696e-05, 6.522775090857335e-06, 1.0678774162732873e-06, 1.602587825391728e-07, 2.220036782058036e-08, 2.8557081268726944e-09, 3.4285006928751647e-10, 3.8589214824794324e-11], [0.029760259123508357, 0.05359427390265023, 0.04799889479622557, 0.035028183452281016, 0.015770276482328205, 0.0056800346650663445, 0.0017048313342565781, 0.00043859639944078, 9.873173258838152e-05, 1.975585964141279e-05, 3.5577679226852488e-06, 5.824606803172393e-07, 8.741119353411879e-08, 1.2108919195233701e-08, 1.5576110825252836e-09, 1.870033784410642e-10, 2.1048015415662312e-11], [0.010821579650336881, 0.019488227620349057, 0.017547854751996075, 0.010477209258964709, 0.005734469661473518, 0.0020654036407947727, 0.0006199196047817462, 0.00015948469572128648, 3.590134426541167e-05, 7.183728064435657e-06, 1.2936940096176577e-06, 2.1179737108751862e-07, 3.178491118759337e-08, 4.403107950333835e-09, 5.663866139014895e-10, 6.79991375842396e-11, 7.653588443461668e-12], [0.0029512491551882997, 0.005314807741481808, 0.0047856314129317715, 0.002872762181240449, 0.0012864192354056423, 0.0005632745816206837, 0.00016906378449470073, 4.3494488671832424e-05, 9.790974641130338e-06, 1.9591383204954013e-06, 3.528147901066754e-07, 5.7761143260973325e-08, 8.66834559473948e-09, 1.2008106984844011e-09, 1.5446432681708315e-10, 1.8544649102386154e-11, 2.087278119994433e-12], [0.0006438891073155677, 0.0011595587604660393, 0.0010441056570899292, 0.0006267652031876029, 0.00028218022088517564, 0.00010108795398885688, 3.68855096786089e-05, 9.489414824505524e-06, 2.1361469635133324e-06, 4.274352174142406e-07, 7.697540543133919e-08, 1.2602043750339259e-08, 1.891217248495416e-09, 2.619870055169139e-10, 3.370027140253634e-11, 4.0459808467963826e-12, 4.553921321891176e-13], [0.0001170671470278901, 0.00021082238285547995, 0.0001898315549719245, 0.00011395380564741931, 5.130391713636726e-05, 1.847830810796514e-05, 5.516375179044396e-06, 1.7252950979408026e-06, 3.883784145586371e-07, 7.771310443586575e-08, 1.3995097917917775e-08, 2.2912102283007526e-09, 3.438471084164305e-10, 4.763253632618749e-11, 6.1271336668644675e-12, 7.356102615846933e-13, 8.279602355223578e-14], [1.824366972184193e-05, 3.285442603184626e-05, 2.958322876755842e-05, 1.775848858162741e-05, 7.995169810106027e-06, 2.8796477807718008e-06, 8.643105293838626e-07, 2.2116408633249574e-07, 6.052464506213977e-08, 1.2110760758944379e-08, 2.1809871566999196e-09, 3.570607444500763e-10, 5.358491464104138e-11, 7.423024160156338e-12, 9.548486129351282e-13, 1.146370352149408e-13, 1.2902879640596112e-14], [2.4876966484483752e-06, 4.480011246216922e-06, 4.033952608077931e-06, 2.4215376182310616e-06, 1.09021690502125e-06, 3.9266716851167294e-07, 1.1785690269280933e-07, 3.032066113029861e-08, 6.788776662917159e-09, 1.651416595977722e-09, 2.9739819470287776e-10, 4.868860436546291e-11, 7.306809133927483e-12, 1.01219944266278e-12, 1.302026253704002e-13, 1.5631842312450824e-14, 1.7594294857692139e-15], [3.015297158013744e-07, 5.430149687669133e-07, 4.889489175573785e-07, 2.935106859925897e-07, 1.3214344029363406e-07, 4.759455691661763e-08, 1.4285245910653281e-08, 3.6751186440803064e-09, 8.273000682644794e-10, 1.646506283847753e-10, 3.604715759235845e-11, 5.901467546792913e-12, 8.856466012213473e-13, 1.2268706896830927e-13, 1.578165113058169e-14, 1.894710503736488e-15, 2.132576225270252e-16], [3.2893139366959975e-08, 5.9236175109723915e-08, 5.333824179084696e-08, 3.2018363014031924e-08, 1.4415204771629503e-08, 5.191973831190394e-09, 1.5583425447193412e-09, 4.0090970612487645e-10, 9.024814145231583e-11, 1.805832399258563e-11, 3.234597767256668e-12, 6.437766638367452e-13, 9.661302205795871e-14, 1.3383632347389468e-14, 1.7215817310056278e-15, 2.0668933572205882e-16, 2.3263752563176095e-17], [3.2620292182140707e-09, 5.8744813569621614e-09, 5.2895803355479495e-09, 3.1752772061662234e-09, 1.4295631264319856e-09, 5.148906630225122e-10, 1.5454161599323102e-10, 3.975841772520451e-11, 8.94995369772085e-12, 1.7908530967086816e-12, 3.2250885647900125e-13, 5.251601963402726e-14, 9.581162117033551e-15, 1.3272615689237668e-15, 1.7073012841470652e-16, 2.0497485651851482e-17, 2.307078073022389e-18], [2.965389923196702e-10, 5.340273386478072e-10, 4.808561535068367e-10, 2.8865268826980727e-10, 1.2995628812962963e-10, 4.6806802806964506e-11, 1.404880582374928e-11, 3.614290473741226e-12, 8.136071363220012e-13, 1.627998209596976e-13, 2.931808543603793e-14, 4.799816165576336e-15, 7.164505160607252e-16, 1.206564325039253e-16, 1.5520443519026283e-17, 1.863350489427788e-18, 2.097279212451153e-19], [2.4883625804726062e-11, 4.481210501342997e-11, 4.035032457676002e-11, 2.4221858401309732e-11, 1.0905087454073613e-11, 3.927722816662608e-12, 1.1788845183117745e-12, 3.032877767427317e-13, 6.827262537692412e-14, 1.3661103365018748e-14, 2.4601832682931277e-15, 4.027693911730949e-16, 6.044451478213984e-17, 8.328300465906425e-18, 1.3023747933779496e-18, 1.5636026803514103e-19, 1.759900467807832e-20], [1.938924207981122e-12, 3.4917449692813404e-12, 3.144084456812419e-12, 1.887359502394968e-12, 8.497209458453888e-13, 3.0604691258540516e-13, 9.18583066996103e-14, 2.363208709719344e-14, 5.319781253928151e-15, 1.0644688290215517e-15, 1.916966977560678e-16, 3.138366285153712e-17, 4.709817366266006e-18, 6.524427319501469e-19, 8.347514914511992e-20, 1.2183542351861423e-20, 1.371308846808739e-21], [1.4100833373496847e-13, 2.539372802294778e-13, 2.2865365678153885e-13, 1.37258288640731e-13, 6.179598677460333e-14, 2.225727287882709e-14, 6.6803987046583164e-15, 1.718644395968746e-15, 3.8688128569604876e-16, 7.741353441011009e-17, 1.394114933518957e-17, 2.282378025391266e-18, 3.4252163972138787e-19, 4.7448921474643125e-20, 6.103514669737596e-21, 7.28838952838124e-22, 9.972848589366008e-23], [9.613908949902742e-15, 1.7313373092548747e-14, 1.5589542682574684e-14, 9.35823191905582e-15, 4.213233179799642e-15, 1.5174946704381833e-15, 4.554677244562478e-16, 1.1717669659978848e-16, 2.63774583855021e-17, 5.278033231055737e-18, 9.505036817002826e-19, 1.5561189856063755e-19, 2.3353030068719926e-20, 3.2350542605921105e-21, 4.1613593150843184e-22, 4.996036941174812e-23, 5.5930474021602475e-24]] |
| Legacy trial inputs | {"lambda_home": 1.0908755470266032, "lambda_away": 1.8008671792885973, "rho": -0.10363035671928646, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1961 |
| Legacy p draw | 0.2276 |
| Legacy p away | 0.5763 |
| Legacy p over 1 5 | 0.7991 |
| Legacy p under 3 5 | 0.6668 |
| Legacy p btts yes | 0.5580 |
| Legacy p over 2 5 | 0.5635 |
| Legacy goal margin distribution | {"-1": 0.2449487269396317, "-10": 7.1392446685738614e-06, "-11": 1.1518708202829733e-06, "-12": 1.7073646653468624e-07, "-13": 2.3401328025405884e-08, "-14": 2.9817110283120907e-09, "-15": 3.528781089356048e-10, "-16": 3.53745346386917e-11, "-2": 0.18030507925631953, "-3": 0.09412915604288528, "-4": 0.0387927215697752, "-5": 0.013148357291316647, "-6": 0.0037756393246986277, "-7": 0.000939253943397175, "-8": 0.0002059330576372133, "-9": 4.034111746589438e-05, "0": 0.22760490378650586, "1": 0.11869596268289676, "10": 3.9273571169516734e-08, "11": 3.838357554422477e-09, "12": 3.4463665331173305e-10, "13": 2.8613382662707996e-11, "14": 2.2084510308931745e-12, "15": 1.5832170682751722e-13, "16": 9.613908949902742e-15, "2": 0.05471518854898399, "3": 0.01730284938680552, "4": 0.004319537369598253, "5": 0.0008868537501962195, "6": 0.00015426398080673327, "7": 2.3246125821468266e-05, "8": 3.0873591138265764e-06, "9": 3.6635534186685806e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2175 |
| Legacy raw p draw | 0.2538 |
| Legacy raw p away | 0.5287 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0909 |
| Legacy lambda away | 1.8009 |
| Legacy model home team | Excelsior |
| Legacy model away team | Twente |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Market p home draw | 40.0% |
| Market reference home draw last update utc | 2026-10-31T12:02:43Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.0% |
| Market reference draw away last update utc | 2026-10-31T12:02:43Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.0% |
| Market reference home away last update utc | 2026-10-31T12:02:43Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.33 |
| Market reference dc draw away odds | 1.15 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 85.6% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.70 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.5% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.71 |
| Market reference under 3 5 opposite odds | 2.19 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.2% |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.42 |
| Market reference btts yes last update utc | 2026-10-31T12:02:14Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,409.2021 |
| Elo away rating | 1,577.6366 |
| Elo rating diff | -108.4345 |
| Elo home expectancy | 0.3488 |

</details>


---

## 2026-11-01 — FC Zwolle vs ADO Den Haag

The model's most likely 1X2 outcome is **FC Zwolle win** at **43.0%**. Expected goals are 1.76 for FC Zwolle and 1.48 for ADO Den Haag (3.24 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 59.5%; Under 3.5 goals: 63.1%; Double Chance 1X: 68.3%; Double Chance X2: 57.0%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Zwolle win | 43.0% | 2.33 |
| Draw | 25.3% | 3.95 |
| ADO Den Haag win | 31.7% | 3.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Zwolle expected goals | 1.76 |
| ADO Den Haag expected goals | 1.48 |
| Expected total goals | 3.24 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 59.5% |
| Under 2.5 | 40.5% |
| Over 3.5 | 36.9% |
| Under 3.5 | 63.1% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.64% |
| 2 | 2-1 | 9.08% |
| 3 | 1-2 | 7.70% |
| 4 | 1-0 | 6.71% |
| 5 | 2-0 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Zwolle win | 43.0% | 42.8% | 2.27 | -2.4% |
| Draw | 25.3% | 25.4% | 3.76 | -4.9% |
| ADO Den Haag win | 31.7% | 31.8% | 3.03 | -3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T11:15:00+00:00 |
| Fixture id | 016bdfefaa570d0fcaeffc5a1cb3625f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:35Z |
| Market best draw last update utc | 2026-10-31T12:02:35Z |
| Market best away last update utc | 2026-10-31T12:02:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Zwolle |
| Matched away-team name | Den Haag |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.7584 |
| Dc lambda away | 1.4786 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.03 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.62 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.71 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.05 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.1690085026057456, "-10": 4.7359251467331703e-07, "-11": 5.9396797367493096e-08, "-12": 6.846361219493373e-09, "-13": 7.295770030547818e-10, "-14": 7.165025528074216e-11, "-15": 5.799214320691445e-12, "-2": 0.09457650706076784, "-3": 0.03762808787263038, "-4": 0.011906191071557479, "-5": 0.0031119084936628463, "-6": 0.0006909952506222334, "-7": 0.00013316609558308208, "-8": 2.26473602475116e-05, "-9": 3.4444582342298963e-06, "0": 0.25284984534726396, "1": 0.201256378584465, "10": 2.6564616454157314e-06, "11": 3.96205148618107e-07, "12": 5.430943203054623e-08, "13": 6.882479932224064e-09, "14": 8.038035601953991e-10, "15": 7.736770392952305e-11, "2": 0.13262184474434935, "3": 0.0627483498787871, "4": 0.023611380150975324, "5": 0.007338946291636522, "6": 0.0019379399675595042, "7": 0.000444137342303831, "8": 8.982548631260905e-05, "9": 1.6246554718602155e-05} |
| Raw goal margin distribution | {"-1": 0.1646431030584288, "-10": 6.833346881614023e-07, "-11": 9.010720588337114e-08, "-12": 1.0923266193750996e-08, "-13": 1.2250820225262342e-09, "-14": 1.2774499205059083e-10, "-15": 1.2328116909520184e-11, "-16": 9.800288141257647e-13, "-2": 0.09459169721881225, "-3": 0.03906540312627293, "-4": 0.012891514529208305, "-5": 0.0035239835556241687, "-6": 0.0008198600180085228, "-7": 0.00016574510402342268, "-8": 2.9594740417193057e-05, "-9": 4.728618201442057e-06, "0": 0.24996125640595823, "1": 0.19764191860806335, "10": 3.8656018912299865e-06, "11": 6.061799204730839e-07, "12": 8.738822264859596e-08, "13": 1.1655312489462465e-08, "14": 1.4453099894618247e-09, "15": 1.6587167518256412e-10, "16": 1.568096180543836e-11, "2": 0.1337733951173025, "3": 0.06570030831109445, "4": 0.02578323491103544, "5": 0.008381576282753416, "6": 0.0023189420849268737, "7": 0.0005575056446945725, "8": 0.00011838085195997879, "9": 2.249362970926243e-05} |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 84.3% |
| Raw p under 3 5 | 59.4% |
| Raw p btts yes | 64.9% |
| P home draw | 68.3% |
| P draw away | 57.0% |
| P home away | 74.7% |
| Raw p home draw | 68.4% |
| Raw p draw away | 56.6% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9494 |
| Totals anchor target over 2 5 | 0.5949 |
| Totals anchor reference over odds | 1.63 |
| Totals anchor reference under odds | 2.34 |
| Totals anchor reference last update utc | 2026-10-31T12:02:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6267 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.26, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.82, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.27 |
| Reference draw odds | 3.76 |
| Reference away odds | 3.03 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:35Z |
| Market reference home last update utc | 2026-10-31T12:02:35Z |
| Market reference draw last update utc | 2026-10-31T12:02:35Z |
| Market reference away last update utc | 2026-10-31T12:02:35Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:14Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:14Z |
| Home probability edge | +0.2% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.0060 |
| Raw ev home | -0.0141 |
| Raw edge prob draw | -0.0041 |
| Raw ev draw | -0.0601 |
| Raw edge prob away | -0.0019 |
| Raw ev away | -0.0433 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05021524898908894, 0.048095246763151654, 0.044095027002664954, 0.02212733783452542, 0.008327794191173115, 0.002507383639520381, 0.0006291154427581618, 0.0001352985412746259, 2.5460324566088724e-05, 4.258750864101324e-06, 6.411254887133989e-07, 8.774273477119737e-08, 1.1007551569761544e-08, 1.2747005843696838e-09, 1.3706954074359643e-10, 1.3756580916362721e-11, 1.294348822059115e-12], [0.058025469096288765, 0.11351734216050627, 0.07616487490072654, 0.03822031717887114, 0.014384511040924483, 0.004330977305460236, 0.0010866644665597927, 0.00023369974282609843, 4.3977349994384734e-05, 7.3560954340278495e-06, 1.1074092922218189e-06, 1.515571000079438e-07, 1.9013227687183737e-08, 2.201776870179314e-09, 2.367587715232629e-10, 2.3761597072911762e-11, 2.2357150638342315e-12], [0.059376641199612896, 0.08938742678786636, 0.06686587217210684, 0.033008775302698835, 0.012423107075928532, 0.0037404257020675884, 0.0009384920339156306, 0.0002018335500237476, 3.7980806322959585e-05, 6.353053014988241e-06, 9.564081931606415e-07, 1.308914898920949e-07, 1.6420673788972386e-08, 1.9015529785976273e-09, 2.0447546402034385e-10, 2.0521577959238087e-11, 1.9308635205089316e-12], [0.034186881956254175, 0.05146598639180053, 0.03873924154110277, 0.01931914637226039, 0.007152767259213772, 0.0021535992834764367, 0.0005403491294244466, 0.00011620832047870309, 2.186794867700998e-05, 3.657853814180443e-06, 5.506645937020492e-07, 7.536249649042892e-08, 9.454418861089364e-09, 1.0948441322966652e-09, 1.1772943720264472e-10, 1.1815568362817967e-11, 1.1117200622272074e-12], [0.014762660125407322, 0.022224163820883224, 0.016728470795293982, 0.00839451860909601, 0.003139741395589534, 0.0009299723299997284, 0.00023333483752511453, 5.0181351465943276e-05, 9.443069255969116e-06, 1.5795430749218114e-06, 2.377892856775051e-07, 3.254321126196985e-08, 4.082629486599593e-09, 4.727781795389889e-10, 5.0838203682982493e-11, 5.102226642137126e-12, 4.800655834673021e-13], [0.0050998774151363516, 0.00767751273670168, 0.005778982220952126, 0.0028999526848003856, 0.0010914195509536535, 0.0003265726413778434, 8.060736059423494e-05, 1.733554378602362e-05, 3.2621827786444797e-06, 5.456656175511939e-07, 8.214618485329749e-08, 1.1242309090710148e-08, 1.4103765673806367e-09, 1.6332495225914734e-10, 1.7562458566849276e-11, 1.7626044492048594e-12, 1.6584244344252946e-13], [0.0014681607418353753, 0.0022102144576087064, 0.0016636625028250162, 0.0008348429459044536, 0.00031419957915574846, 9.460114722267587e-05, 2.358865761787708e-05, 4.990583646083107e-06, 9.391223157800576e-07, 1.570870773247007e-07, 2.3648373063872678e-08, 3.23645364603696e-09, 4.060214273557052e-10, 4.701824446943221e-11, 5.0559082305450075e-12, 5.07421344682998e-13, 4.7742983795987077e-14], [0.0003622769369994977, 0.0005453828732768769, 0.0004105180982914107, 0.0002060022017342675, 7.753051685660672e-05, 2.3343366210450307e-05, 5.856970563851357e-06, 1.2517946047145171e-06, 2.3173372392682012e-07, 3.876212160819175e-08, 5.835369326039278e-09, 7.986131764845936e-10, 1.00188075370212e-10, 1.1602016798368696e-11, 1.2475738489115496e-12, 1.252090764190556e-13, 1.1780850311529626e-14], [7.821964136771449e-05, 0.00011775426034329685, 8.863544748186619e-05, 4.4478178694097554e-05, 1.673970546898416e-05, 5.040093770305835e-06, 1.264585432349366e-06, 2.7196370123087655e-07, 5.086031317668858e-08, 8.369175459956756e-09, 1.2599214835792518e-09, 1.7242951420957503e-10, 2.1631725689428578e-11, 2.5050051505538068e-12, 2.693651432791483e-13, 2.7034039579215242e-14, 2.5436173056079824e-15], [1.501199569433841e-05, 2.2599521275652558e-05, 1.701100813935389e-05, 8.536298752750428e-06, 3.212701848676681e-06, 9.67300088007343e-07, 2.4270056386869947e-07, 5.2195559075772194e-08, 9.822100537508494e-09, 1.6327509300515712e-09, 2.418054539240447e-10, 3.3092853401389074e-11, 4.151583505531737e-12, 4.80763218507046e-13, 5.169684110544238e-14, 5.188401259165879e-15, 4.88173703844066e-16], [2.5930061773188705e-06, 3.903591465478294e-06, 2.9382934878139903e-06, 1.4744658770232024e-06, 5.549266006413893e-07, 1.6708072361558626e-07, 4.192141232678694e-08, 9.015683848292898e-09, 1.6965610626714846e-09, 2.8378392714114573e-10, 4.2456664160946834e-11, 5.716093652176562e-12, 7.170986386279635e-13, 8.304172348561359e-14, 8.929540819468764e-15, 8.961870752800693e-16, 8.432172879916896e-17], [4.071702010551963e-07, 6.129665774570534e-07, 4.613893945402942e-07, 2.315299411347047e-07, 8.713807839349603e-08, 2.62360700958099e-08, 6.582764836782946e-09, 1.4156995988938133e-09, 2.6640472939583644e-10, 4.456154392573362e-11, 6.708432246655563e-12, 9.124024163927998e-13, 1.1260335568057137e-13, 1.303973571037479e-14, 1.4021728766389157e-15, 1.4072495268875752e-16, 1.3240730226095905e-17], [5.860839935683777e-08, 8.823089182581658e-08, 6.641275276075866e-08, 3.332660203993761e-08, 1.2542723618866054e-08, 3.776440588590053e-09, 9.475283540556147e-10, 2.0377691502536043e-10, 3.834650652360704e-11, 6.414223721648587e-12, 9.65617019986635e-13, 1.3215178551903763e-13, 1.647592716218405e-14, 1.8769498259958954e-15, 2.0182986797267936e-16, 2.025606050069647e-17, 1.9058811348573715e-18], [7.787205372258308e-09, 1.1723099118300367e-08, 8.82415747163218e-09, 4.428052929144513e-09, 1.6665318592460342e-09, 5.017696910716228e-10, 1.2589659451615965e-10, 2.7075516561476873e-11, 5.095039702242481e-12, 8.522477660578029e-13, 1.2830000696319473e-13, 1.7558798831575917e-14, 2.2027964383107763e-15, 2.5350649304113436e-16, 2.6816815497549784e-17, 2.6913907372119654e-18, 2.532314135024325e-19], [9.607684055497302e-10, 1.4463703870088817e-09, 1.0887052927282896e-09, 5.463235074780389e-10, 2.0561306407940568e-10, 6.190724952002365e-11, 1.5532847099209567e-11, 3.34051814902392e-12, 6.286148800409092e-13, 1.051484695967659e-13, 1.5829374882185785e-14, 2.1663662829389767e-15, 2.7177621760509885e-16, 3.1472330718002414e-17, 3.3632484030003536e-18, 3.3205791599054283e-19, 3.124313919504089e-20], [1.1063500866411863e-10, 1.6655335393412816e-10, 1.2536727768930736e-10, 6.291058868516878e-11, 2.3676885079151957e-11, 7.12878259469894e-12, 1.7886481939590905e-12, 3.8466945022868697e-13, 7.23866566573104e-14, 1.2108122808431453e-14, 1.8227941480196375e-15, 2.4946277489783907e-16, 3.129574621288393e-17, 3.624121652578609e-18, 3.89704607190959e-19, 3.8868909399159316e-20, 3.597729645949204e-21], [1.1943667698108744e-11, 1.7980365685458475e-11, 1.353409850116667e-11, 6.791549754646027e-12, 2.556052111590016e-12, 7.695919350595178e-13, 1.9309457210173503e-13, 4.152721767387245e-14, 7.814544268864896e-15, 1.3071395484845154e-15, 1.9678081873793498e-16, 2.693090118945515e-17, 3.3785507647567788e-18, 3.9124419330350715e-19, 4.2070791017349754e-20, 4.222311081702489e-21, 3.9481015843817786e-22]] |
| Legacy trial inputs | {"lambda_home": 1.7272894491282065, "lambda_away": 1.5054308391638886, "rho": -0.10363035671928646, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4245 |
| Legacy p draw | 0.2534 |
| Legacy p away | 0.3221 |
| Legacy p over 1 5 | 0.8437 |
| Legacy p under 3 5 | 0.5952 |
| Legacy p btts yes | 0.6505 |
| Legacy p over 2 5 | 0.6267 |
| Legacy goal margin distribution | {"-1": 0.16543747485056629, "-10": 8.102507551937278e-07, "-11": 1.0878051294326696e-07, "-12": 1.3426099537907486e-08, "-13": 1.533092653914412e-09, "-14": 1.6276200133701714e-10, "-15": 1.5992295980196952e-11, "-16": 1.294348822059115e-12, "-2": 0.09714370010043427, "-3": 0.040846230340298745, "-4": 0.013723485055009008, "-5": 0.003819414633240039, "-6": 0.0009047032952142506, "-7": 0.00018621361075887082, "-8": 3.385244182786743e-05, "-9": 5.506996924916628e-06, "0": 0.25340881671960236, "1": 0.1957388157795226, "10": 3.2770264954070732e-06, "11": 5.047960203371373e-07, "12": 7.148567040866318e-08, "13": 9.36573458671114e-09, "14": 1.140855857985025e-09, "15": 1.2861537434957712e-10, "16": 1.1943667698108744e-11, "2": 0.13080991253997148, "3": 0.06310769354381807, "4": 0.024327587948552044, "5": 0.007768474724046649, "6": 0.0021112974992623964, "7": 0.0004986077151889602, "8": 0.00010400204649095678, "9": 1.941203342568111e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4207 |
| Legacy raw p draw | 0.2527 |
| Legacy raw p away | 0.3265 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7273 |
| Legacy lambda away | 1.5054 |
| Legacy model home team | Zwolle |
| Legacy model away team | Den Haag |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Market p home draw | 68.6% |
| Market reference home draw last update utc | 2026-10-31T12:02:43Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.9% |
| Market reference draw away last update utc | 2026-10-31T12:02:43Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market reference home away last update utc | 2026-10-31T12:02:43Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.64 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.6% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.88 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.1% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.2% |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.42 |
| Market reference btts yes last update utc | 2026-10-31T12:02:14Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,408.9706 |
| Elo away rating | 1,360.6524 |
| Elo rating diff | 108.3181 |
| Elo home expectancy | 0.6510 |

</details>


---

## 2026-11-01 — Groningen vs Sparta Rotterdam

The model's most likely 1X2 outcome is **Groningen win** at **53.0%**. Expected goals are 1.67 for Groningen and 1.21 for Sparta Rotterdam (2.89 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 67.4%; Under 3.5 goals: 54.2%; Double Chance 1X: 76.2%; Double Chance X2: 47.0%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 73.0%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Groningen win | 53.0% | 1.89 |
| Draw | 23.2% | 4.30 |
| Sparta Rotterdam win | 23.8% | 4.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Groningen expected goals | 1.67 |
| Sparta Rotterdam expected goals | 1.21 |
| Expected total goals | 2.89 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 45.8% |
| Under 3.5 | 54.2% |
| Over 4.5 | 27.0% |
| Under 4.5 | 73.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.98% |
| 2 | 2-1 | 9.81% |
| 3 | 2-0 | 6.73% |
| 4 | 2-2 | 6.67% |
| 5 | 3-1 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Groningen win | 53.0% | 55.5% | 1.75 | -7.3% |
| Draw | 23.2% | 21.9% | 4.23 | -1.7% |
| Sparta Rotterdam win | 23.8% | 22.6% | 4.12 | -2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:45:00+00:00 |
| Fixture id | 961d9c9f07b1f911e211cd6a750cddba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:36Z |
| Market best draw last update utc | 2026-10-31T12:02:36Z |
| Market best away last update utc | 2026-10-31T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Groningen |
| Matched away-team name | Sparta Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6733 |
| Dc lambda away | 1.2144 |
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
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.14 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.71 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.18 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.71 |
| Fair Under 4.5 odds | 1.37 |
| Goal margin distribution | {"-1": 0.1274271596751879, "-10": 4.267043247551484e-07, "-11": 5.5355750799101566e-08, "-12": 6.604149497553267e-09, "-13": 7.291584036557371e-10, "-14": 7.49072838710412e-11, "-15": 7.1895628139419026e-12, "-16": 6.406904640596858e-13, "-17": 4.687504539683807e-14, "-2": 0.07026227428024868, "-3": 0.028101398185774562, "-4": 0.009031772838906002, "-5": 0.002412913788163969, "-6": 0.0005498665653611266, "-7": 0.00010904972085669284, "-8": 1.912171234028406e-05, "-9": 3.0026952544679777e-06, "0": 0.23240529705856983, "1": 0.2173044824034488, "10": 1.2816424752449271e-05, "11": 2.29096459081779e-06, "12": 3.7660693303092075e-07, "13": 5.7293992146430563e-08, "14": 8.110115371523305e-09, "15": 1.0725591412327406e-09, "16": 1.316991008899294e-10, "17": 1.3276757870579605e-11, "2": 0.16241860670241742, "3": 0.0895070595323717, "4": 0.039638585740090784, "5": 0.014591593886466773, "6": 0.004581777821830571, "7": 0.0012520366862890258, "8": 0.00030250674357674246, "9": 6.545386875791935e-05} |
| Raw goal margin distribution | {"-1": 0.15320825258431695, "-10": 1.2863136620922914e-07, "-11": 1.3988242415298274e-08, "-12": 1.39757960521088e-09, "-13": 1.2908083678136326e-10, "-14": 1.100768080231959e-11, "-15": 7.848539551884223e-13, "-2": 0.07700748056078081, "-3": 0.026998857808695164, "-4": 0.007482760522607578, "-5": 0.0017069475615707425, "-6": 0.0003300604745801668, "-7": 5.530755754595256e-05, "-8": 8.170074156951094e-06, "-9": 1.0784957064820666e-06, "0": 0.26281150543529064, "1": 0.2151926602911428, "10": 3.1732531501129246e-06, "11": 4.7548494561275736e-07, "12": 6.5458486476676e-08, "13": 8.330421204442345e-09, "14": 9.788514759683142e-10, "15": 9.61668979890792e-11, "2": 0.1462057599111551, "3": 0.07063057517207849, "4": 0.026972734736420135, "5": 0.008478110999978685, "6": 0.002258854316664622, "7": 0.0005215488187681362, "8": 0.00010615788770371214, "9": 1.9309030753626412e-05} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 58.2% |
| P home draw | 76.2% |
| P draw away | 47.0% |
| P home away | 76.8% |
| Raw p home draw | 73.3% |
| Raw p draw away | 53.0% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2007 |
| Totals anchor target over 2 5 | 0.6741 |
| Totals anchor reference over odds | 1.44 |
| Totals anchor reference under odds | 2.82 |
| Totals anchor reference last update utc | 2026-10-31T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5636 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 8.5, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.8, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.07, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.89, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.22, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.81, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 4.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:01:49Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.66, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.75 |
| Reference draw odds | 4.23 |
| Reference away odds | 4.12 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:36Z |
| Market reference home last update utc | 2026-10-31T12:02:36Z |
| Market reference draw last update utc | 2026-10-31T12:02:36Z |
| Market reference away last update utc | 2026-10-31T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-31T12:02:15Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:02:15Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0847 |
| Raw ev home | -0.1768 |
| Raw edge prob draw | 0.0434 |
| Raw ev draw | 0.1117 |
| Raw edge prob away | 0.0413 |
| Raw ev away | 0.0992 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.056563786579602655, 0.046765971187780114, 0.03475569226051957, 0.014017269169420386, 0.004239963776908656, 0.0010260082823388282, 0.0002068989757964761, 3.576177162016396e-05, 5.408636105753154e-06, 7.271164635469732e-07, 8.797569426029843e-08, 9.676732643883945e-09, 9.756773446857733e-10, 9.080747358392854e-11, 7.847878703147782e-12, 6.330233756612254e-13, 4.7869455710306274e-14], [0.08209361015239515, 0.1106533414706026, 0.06237569529000263, 0.0251566535908971, 0.007609420828297704, 0.0018413668617063826, 0.00037131953446240164, 6.418129591232213e-05, 9.706825435619214e-06, 1.3049486866952794e-06, 1.5788910366030424e-07, 1.7366735850730634e-08, 1.7510384283903446e-09, 1.629712698532627e-10, 1.408450986938072e-11, 1.1360807575266286e-12, 8.591083615031708e-14], [0.08422711266759864, 0.10190855363562641, 0.054428840812613954, 0.02257419802114582, 0.006828275946303962, 0.0016523413980934574, 0.00033320173805259363, 5.7592766778121e-05, 8.710371542407883e-06, 1.1709892158133787e-06, 1.4168100214643158e-07, 1.558395406840538e-08, 1.571285627569434e-09, 1.462414587112002e-10, 1.2638664903237827e-11, 1.01945641918365e-12, 7.70916616716155e-14], [0.05038718718390364, 0.06096475594437103, 0.03688141445355413, 0.013132117404093034, 0.004084879646861268, 0.0009884802254354872, 0.0001993312819770524, 3.445372194510044e-05, 5.210805730462735e-06, 7.005209004418252e-07, 8.475782855965773e-08, 9.322789133340073e-09, 9.399902303213528e-10, 8.748603057555632e-11, 7.560828741064741e-12, 6.098694326844628e-13, 4.6118546201336955e-14], [0.02260734594742694, 0.02735321031524331, 0.016547676942925034, 0.006673820221992154, 0.0017822267391489409, 0.0004435039077900626, 8.943446740442182e-05, 1.5458438041926764e-05, 2.3379453070767596e-06, 3.1430447351406274e-07, 3.8028508021440136e-08, 4.1828792379912935e-09, 4.217477797781288e-10, 3.9252577278626013e-11, 3.392336039212431e-12, 2.7363165157715187e-13, 2.069212406639529e-14], [0.008114635792964625, 0.009818106910591385, 0.005939590251935694, 0.0023954877576132464, 0.0007245905887621825, 0.00015480006104715298, 3.2101429863209945e-05, 5.548621007085615e-06, 8.391774388252773e-07, 1.1281582263558001e-07, 1.364987703826165e-08, 1.5013943547900607e-09, 1.5138130930315952e-10, 1.4089242023011604e-11, 1.2176383512497232e-12, 9.821680081950089e-14, 7.427189859973219e-15], [0.0024272093609745836, 0.0029367431402279012, 0.0017766205936624896, 0.0007165263429838608, 0.00021673592072271093, 5.2446874889097386e-05, 9.33720315131561e-06, 1.6596758243388893e-06, 2.5101056744916915e-07, 3.374490584094189e-08, 4.082883097741159e-09, 4.4908958645073666e-10, 4.5280421745580035e-11, 4.214303759256756e-12, 3.6421390680249223e-13, 2.93781192941222e-14, 2.2215839643095473e-15], [0.0006222983577166757, 0.0007529348158354737, 0.00045549761610917336, 0.00018370610037551734, 5.556768595758847e-05, 1.3446554976103287e-05, 2.7115555502192603e-06, 4.1377944142000126e-07, 6.435516705094994e-08, 8.651663850575388e-09, 1.0467870993433033e-09, 1.1513951643781625e-10, 1.1609188948446865e-11, 1.0804812928257957e-12, 9.337872525745367e-14, 7.532088365956278e-15, 5.695792356224396e-16], [0.00013960408430886532, 0.0001689105783512801, 0.00010218463027142295, 4.121193894674063e-05, 1.2465846678007161e-05, 3.016549812915267e-06, 6.083002227901228e-07, 1.0514258739160824e-07, 1.4039030453287578e-08, 1.9408818850805778e-09, 2.348322997450185e-10, 2.5829968150719666e-11, 2.6043619955275584e-12, 2.4239112899359365e-13, 2.0948233707907483e-14, 1.6897205114295399e-15, 1.2777727378579479e-16], [2.783845132096953e-05, 3.3682459480380075e-05, 2.037663775845297e-05, 8.218073001885314e-06, 2.4858145636526655e-06, 6.015302169693658e-07, 1.2130115121282576e-07, 2.0966484006200353e-08, 3.170986147193324e-09, 3.763572428793921e-10, 4.682791035382247e-11, 5.150754109708662e-12, 5.193358417384992e-13, 4.8335216541329324e-14, 4.1772874140820706e-15, 3.369471777015039e-16, 2.5480066960950325e-17], [4.996139176070618e-06, 6.044957509169275e-06, 3.6569749160191836e-06, 1.4748893896119769e-06, 4.461266678494039e-07, 1.0795602987897249e-07, 2.1769796986528573e-08, 3.762834035560404e-09, 5.690937306141081e-10, 7.650679630502942e-11, 8.172378252091614e-12, 9.244007181691871e-13, 9.320468709022143e-14, 8.674673248223697e-15, 7.49693618318539e-16, 6.047157492244734e-17, 4.572882280150956e-18], [8.151382997981544e-07, 9.862568300692755e-07, 5.966487742626971e-07, 2.406335746603812e-07, 7.278719041037358e-08, 1.7613419391914185e-08, 3.5518216521154544e-09, 6.139200750971998e-10, 9.284971447961444e-11, 1.2482362413317191e-11, 1.5102731878237713e-12, 1.4665986138109527e-13, 1.5206684099560046e-14, 1.4153045288908205e-15, 1.2231524380518233e-16, 9.866157653191784e-18, 7.460823959573922e-19], [1.219100500773158e-07, 1.4750211046715968e-07, 8.923330184208724e-08, 3.598855696560291e-08, 1.0885870569586818e-08, 2.6342190529297043e-09, 5.312015833169785e-10, 9.181635449726976e-11, 1.3886371606728789e-11, 1.8668309749002284e-12, 2.258726893382568e-13, 2.4844471472022595e-14, 2.2115510010069624e-15, 2.1166941368655638e-16, 1.8293162646389286e-17, 1.4755579192747268e-18, 1.1158222141628215e-19], [1.6830058046346726e-08, 2.0363120838245523e-08, 1.231893226782417e-08, 4.968331178202472e-09, 1.502827974026516e-09, 3.6366205689754536e-10, 7.333401533233854e-11, 1.2675530645857168e-11, 1.9170563874444136e-12, 2.5772176822471103e-13, 3.1182420729352576e-14, 3.429855838298512e-15, 3.458225787689979e-16, 2.841570501232228e-17, 2.525427468816049e-18, 2.0370531729246778e-19, 1.540426947725268e-20], [2.1574812727140627e-09, 2.6103921769933928e-09, 1.5791903744166136e-09, 6.369010400377082e-10, 1.9265074434944267e-10, 4.6618619804667904e-11, 9.40084486320534e-12, 1.624903486062916e-12, 2.4575157395526593e-13, 3.303790676088991e-14, 3.99734145754015e-15, 4.3968058332658603e-16, 4.4331738804534465e-17, 4.126008687553246e-18, 3.148114686220966e-19, 2.6113421950209778e-20, 1.974706375075613e-21], [2.5813401241244175e-10, 3.123229921572803e-10, 1.8894381743506918e-10, 7.620266421491204e-11, 2.3049891677903798e-11, 5.577731559250447e-12, 1.1247735196113108e-12, 1.9441320856182212e-13, 2.940319373523164e-14, 3.9528535156962704e-15, 4.782659309572561e-16, 5.260602471471676e-17, 5.304115386567931e-18, 4.936604508399217e-19, 4.266374986363041e-20, 3.0381989433383085e-21, 2.3626572632700356e-22], [2.8954409074802007e-11, 3.503268551816849e-11, 2.119347439355891e-11, 8.54751023178995e-12, 2.585463211665219e-12, 6.256437102830492e-13, 1.2616374068247752e-13, 2.1806965760287708e-14, 3.2981012132383315e-15, 4.4338418109493066e-16, 5.364619440134638e-17, 5.9007193401362046e-18, 5.949526962655978e-19, 5.537296888575906e-20, 4.785512977045575e-21, 3.8600769629440395e-22, 2.5770593714308058e-23]] |
| Legacy trial inputs | {"lambda_home": 1.7946900560187593, "lambda_away": 1.209925763902265, "rho": -0.10363035671928646, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5274 |
| Legacy p draw | 0.2367 |
| Legacy p away | 0.2358 |
| Legacy p over 1 5 | 0.8146 |
| Legacy p under 3 5 | 0.6437 |
| Legacy p btts yes | 0.5917 |
| Legacy p over 2 5 | 0.5849 |
| Legacy goal margin distribution | {"-1": 0.1362780755030841, "-10": 1.0700469454359804e-07, "-11": 1.1581854418567992e-08, "-12": 1.1519178409990247e-09, "-13": 1.0595755841869424e-10, "-14": 9.061051122346026e-12, "-15": 7.189342118115424e-13, "-16": 4.7869455710306274e-14, "-2": 0.06782434501387662, "-3": 0.023494695111320386, "-4": 0.006451441060418516, "-5": 0.0014604598046057708, "-6": 0.000280530740436217, "-7": 4.672868267010119e-05, "-8": 6.865024792623778e-06, "-9": 9.015700116693326e-07, "0": 0.23672487847341003, "1": 0.22833725587438516, "10": 6.076795993799833e-06, "11": 9.756199191085644e-07, "12": 1.4393114941740453e-07, "13": 1.9637941551006977e-08, "14": 2.490997739264902e-09, "15": 2.931666979306102e-10, "16": 2.8954409074802007e-11, "2": 0.16436584563671905, "3": 0.08445522348857043, "4": 0.03439886932681652, "5": 0.011550685904430556, "6": 0.0032910111642974796, "7": 0.0008131359596142495, "8": 0.0001771954114111076, "9": 3.451759675454142e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4998 |
| Legacy raw p draw | 0.2541 |
| Legacy raw p away | 0.2461 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7947 |
| Legacy lambda away | 1.2099 |
| Legacy model home team | Groningen |
| Legacy model away team | Sparta Rotterdam |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 77.6% |
| Market reference home draw last update utc | 2026-10-31T12:02:43Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.8% |
| Market reference draw away last update utc | 2026-10-31T12:02:43Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.6% |
| Market reference home away last update utc | 2026-10-31T12:02:43Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.08 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 87.0% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:36Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.01 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.2% |
| Market under 3 5 odds | 1.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.09 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.1% |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.53 |
| Market reference btts yes last update utc | 2026-10-31T12:02:14Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,487.9195 |
| Elo away rating | 1,450.6913 |
| Elo rating diff | 97.2282 |
| Elo home expectancy | 0.6364 |

</details>


---

## 2026-11-01 — SC Telstar vs FC Utrecht

The model's most likely 1X2 outcome is **FC Utrecht win** at **41.0%**. Expected goals are 1.46 for SC Telstar and 1.60 for FC Utrecht (3.06 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 62.5%; Under 3.5 goals: 59.5%; Double Chance 1X: 59.0%; Double Chance X2: 66.8%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 65.3%; BTTS No (at least one team does not score): 34.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Telstar win | 33.2% | 3.01 |
| Draw | 25.8% | 3.88 |
| FC Utrecht win | 41.0% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Telstar expected goals | 1.46 |
| FC Utrecht expected goals | 1.60 |
| Expected total goals | 3.06 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 84.3% |
| Under 1.5 | 15.7% |
| Over 2.5 | 62.5% |
| Under 2.5 | 37.5% |
| Over 3.5 | 40.5% |
| Under 3.5 | 59.5% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.53% |
| 2 | 1-2 | 8.80% |
| 3 | 2-1 | 7.67% |
| 4 | 2-2 | 6.87% |
| 5 | 0-1 | 5.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Telstar win | 33.2% | 32.8% | 2.90 | -3.7% |
| Draw | 25.8% | 25.7% | 3.67 | -5.4% |
| FC Utrecht win | 41.0% | 41.5% | 2.32 | -4.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:30:00+00:00 |
| Fixture id | d7d5552edc5c81a14b6933537ba2043c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T12:02:36Z |
| Market best draw last update utc | 2026-10-31T12:02:36Z |
| Market best away last update utc | 2026-10-31T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Telstar |
| Matched away-team name | Utrecht |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4645 |
| Dc lambda away | 1.5984 |
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
| P btts yes | 65.3% |
| P btts no | 34.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.86 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.37 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.47 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.45 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.19331357813099417, "-10": 2.6198569378475522e-06, "-11": 3.9443987097592794e-07, "-12": 5.4593628032163574e-08, "-13": 6.986164935223595e-09, "-14": 8.224305643046497e-10, "-15": 7.884327689524821e-11, "-2": 0.1257636559861064, "-3": 0.05926811357327308, "-4": 0.02232291128302617, "-5": 0.006965530197951235, "-6": 0.0018499879583430763, "-7": 0.0004269752362687771, "-8": 8.704144133051148e-05, "-9": 1.587842902308137e-05, "0": 0.2578849571218426, "1": 0.16772309527835152, "10": 1.0391108467077476e-06, "11": 1.4333931206445826e-07, "12": 1.8177186794488057e-08, "13": 2.1311977767250897e-09, "14": 2.2987109661976713e-10, "15": 2.01906359427976e-11, "2": 0.10044719356130612, "3": 0.04337145220249098, "4": 0.014966970363740334, "5": 0.004278952356077507, "6": 0.0010412436816728593, "7": 0.00022018431127825524, "8": 4.1125383758627506e-05, "9": 6.873716684028233e-06} |
| Raw goal margin distribution | {"-1": 0.1933582508311533, "-10": 1.7317594886727598e-06, "-11": 2.4731639802907163e-07, "-12": 3.2460538293432906e-08, "-13": 3.938880492293969e-09, "-14": 4.404858890005182e-10, "-15": 4.060175635872086e-11, "-2": 0.12231009790369382, "-3": 0.055418273003796974, "-4": 0.019968950668689037, "-5": 0.005943451362161014, "-6": 0.001502826341527288, "-7": 0.0003297950398505029, "-8": 6.386768545346698e-05, "-9": 1.1061016928379632e-05, "0": 0.260495535886142, "1": 0.17628262606059844, "10": 7.219209353560928e-07, "11": 9.446157427913044e-08, "12": 1.1359473165904081e-08, "13": 1.2629189586594727e-09, "14": 1.2940018132556682e-10, "15": 1.0928181803425152e-11, "2": 0.10267453056092521, "3": 0.042623941381392846, "4": 0.014072007835421316, "5": 0.0038374236099555405, "6": 0.0008890169371247471, "7": 0.00017874979887664877, "8": 3.171632256191512e-05, "9": 5.032652124209612e-06} |
| Unadjusted home-win probability | 34.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 39.9% |
| Raw p over 1 5 | 82.1% |
| Raw p under 3 5 | 63.3% |
| Raw p btts yes | 62.4% |
| P home draw | 59.0% |
| P draw away | 66.8% |
| P home away | 74.2% |
| Raw p home draw | 60.1% |
| Raw p draw away | 65.9% |
| Raw p home away | 74.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0563 |
| Totals anchor target over 2 5 | 0.6253 |
| Totals anchor reference over odds | 1.55 |
| Totals anchor reference under odds | 2.50 |
| Totals anchor reference last update utc | 2026-10-31T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5918 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T12:02:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T12:02:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.92, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.90 |
| Reference draw odds | 3.67 |
| Reference away odds | 2.32 |
| Market reference 1x2 last update utc | 2026-10-31T12:02:36Z |
| Market reference home last update utc | 2026-10-31T12:02:36Z |
| Market reference draw last update utc | 2026-10-31T12:02:36Z |
| Market reference away last update utc | 2026-10-31T12:02:36Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-31T12:01:50Z |
| Market reference under 2 5 last update utc | 2026-10-31T12:01:50Z |
| Home probability edge | +0.4% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | 0.0121 |
| Raw ev home | -0.0123 |
| Raw edge prob draw | 0.0037 |
| Raw ev draw | -0.0440 |
| Raw edge prob away | -0.0159 |
| Raw ev away | -0.0745 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.056154941386368964, 0.06318339488524248, 0.06010127290292499, 0.03225571341001497, 0.012983473527293425, 0.004180855222543991, 0.0011219102471004417, 0.00025805026597605, 5.193481158551621e-05, 9.290953516693365e-06, 1.4959067560396686e-06, 2.1895560888092176e-07, 2.9377786145169315e-08, 3.638479640278998e-09, 4.184428484136911e-10, 4.491476451323366e-11], [0.05493301833273966, 0.11862410469183643, 0.08912918946346947, 0.04783468723606153, 0.019254275592085795, 0.00620013885315437, 0.0016637742620914872, 0.0003826842583588393, 7.70184629705203e-05, 1.3778329747244827e-05, 2.218404872956606e-06, 3.2470753122913024e-07, 4.356676890320325e-08, 5.3958048732378905e-09, 6.205437940746614e-10, 6.660784976173593e-11], [0.04888972111828163, 0.07871577873070809, 0.06416081055021014, 0.03546902333062933, 0.014276885449670328, 0.004597351469037853, 0.0012336747981187878, 0.000283757199477653, 5.71085506738962e-05, 1.0216517082058136e-05, 1.6449287900091257e-06, 2.4076793779294564e-07, 3.230439733079108e-08, 4.000944502718897e-09, 4.601280698479927e-10, 4.938916743707725e-11], [0.02416754812833834, 0.03891139747619987, 0.031324999240932856, 0.0170218929774233, 0.007057461330018901, 0.0022725986229713323, 0.0006098397449664533, 0.0001402690712542096, 2.8230344035137864e-05, 5.050308380513607e-06, 8.131340247177127e-07, 1.1901828423799163e-07, 1.596896156065246e-08, 1.977778081293097e-09, 2.274540950304697e-10, 2.441443832674655e-11], [0.008960018115911456, 0.014426239039671818, 0.011613613395500407, 0.0062329026865209835, 0.0025402028341476534, 0.0008425565027898676, 0.00022609555316433072, 5.200417571801919e-05, 1.046628282811408e-05, 1.8723808613121657e-06, 3.0146606322846837e-07, 4.4125534672946796e-08, 5.920426189529945e-09, 7.332530111674663e-10, 8.432766125834454e-11, 9.05155163179115e-12], [0.0026575116089107825, 0.00427877457666835, 0.003444559153863333, 0.0018486582317535575, 0.0007441163959974013, 0.00024261011899139945, 6.705919000211667e-05, 1.542426576538385e-05, 3.1042647188919598e-06, 5.553419436064701e-07, 8.941383291397396e-08, 1.3087487003459329e-08, 1.755978740761146e-09, 2.1748040732037126e-10, 2.5011304201314102e-11, 2.6846601456556725e-12], [0.0006568409293497984, 0.001057558604821689, 0.000851370668800681, 0.000456921575402957, 0.000183918709311559, 5.922432812238935e-05, 1.6091144443537605e-05, 3.8123216568094146e-06, 7.672621696431651e-07, 1.3726047973687072e-07, 2.2099871515524185e-08, 3.234754308271483e-09, 4.340145511058656e-10, 5.375330530286353e-11, 6.181891450918287e-12, 6.63551067528013e-13], [0.0001391548840617232, 0.0002240488350628771, 0.00018036693728538716, 9.680101529823755e-05, 3.896405587326335e-05, 1.2546956417077409e-05, 3.366908975546014e-06, 7.840998604752097e-07, 1.6254815053521394e-07, 2.9079287374719704e-08, 4.681963198557018e-09, 6.852981302204474e-10, 9.194805293272806e-11, 1.1387894135584413e-11, 1.3096631919485243e-12, 1.405764588426247e-13], [2.5795547721462684e-05, 4.153258763263418e-05, 3.343514652389454e-05, 1.7944287233958294e-05, 7.222880960862888e-06, 2.325865995995318e-06, 6.241337610111817e-07, 1.4355683393553028e-07, 2.9253102026837686e-08, 5.390512523067389e-09, 8.679092073041396e-10, 1.270357180829503e-10, 1.704467941110649e-11, 2.1110072319929117e-12, 2.427760951025362e-13, 2.6059069195018067e-14], [4.2504854244449175e-06, 6.843570847116049e-06, 5.509307439351225e-06, 2.956786658053093e-06, 1.1901569440645932e-06, 3.832467378455645e-07, 1.0284222233725805e-07, 2.365471114671225e-08, 4.760711878624181e-09, 8.62317957520195e-10, 1.4301054876684778e-10, 2.093242887981819e-11, 2.808552940357434e-12, 3.4784318469880883e-13, 4.0003657405514104e-14, 4.293907420925475e-15], [6.303399286051213e-07, 1.014890189804278e-06, 8.170211425763984e-07, 4.384865503170519e-07, 1.7649829801464053e-07, 5.683485466916213e-08, 1.525133075691584e-08, 3.5079543737855705e-09, 7.060056642997218e-10, 1.263019082822718e-10, 2.0589602085121735e-11, 3.10424443517754e-12, 4.1650373619144973e-13, 5.158456654099898e-14, 5.93247594919785e-15, 6.367793385614607e-16], [8.498033131780412e-08, 1.3682411769727123e-07, 1.1014807128502301e-07, 5.9115297371059335e-08, 2.379491312806996e-08, 7.662285952394931e-09, 2.0561336541509937e-09, 4.729307337260371e-10, 9.518133397832368e-11, 1.7027602924742223e-11, 2.7415599710532235e-12, 4.0629652368232447e-13, 5.6151647532431305e-14, 6.954459580626654e-15, 7.997966633866225e-16, 8.584847113688846e-17], [1.0502034988685982e-08, 1.6908991163838658e-08, 1.3612313351021664e-08, 7.305583677188749e-09, 2.9406217456271435e-09, 9.469202333941661e-10, 2.541010048143276e-10, 5.844570191473473e-11, 1.1762694781359798e-11, 2.1043043597975395e-12, 3.3880732509629224e-13, 4.959116860744217e-14, 6.736916082332992e-15, 8.594456706694656e-16, 9.884043063222143e-17, 1.0609321399714426e-17], [1.1980264195971347e-09, 1.9289040804793423e-09, 1.5528334312280949e-09, 8.333891731725029e-10, 3.3545332357952413e-10, 1.0802053678924536e-10, 2.898673612701725e-11, 6.667231168167332e-12, 1.3418369991061685e-12, 2.400498780119106e-13, 3.864966428465307e-14, 5.657144566211863e-15, 7.590323175912017e-16, 9.518202853109044e-17, 1.127528591833183e-17, 1.2102651861804019e-18], [1.269038058323696e-10, 2.0432376523109634e-10, 1.644875847669943e-10, 8.827873583175803e-11, 3.553369336852711e-11, 1.1442332992306171e-11, 3.070489158673248e-12, 7.062423630767262e-13, 1.4213728446032172e-13, 2.5427855856093314e-14, 4.0940578702055966e-15, 5.992465306713442e-16, 8.040230856050626e-17, 9.957937650006873e-18, 1.1595231083912741e-18, 1.282002263726052e-19], [1.2546415749449846e-11, 2.020058334159459e-11, 1.6262157076956504e-11, 8.727726598240273e-12, 3.513058471263702e-12, 1.1312526517506657e-12, 3.035656282033013e-13, 6.982304627442756e-14, 1.4052482135111347e-14, 2.513939192722417e-15, 4.0476132141976026e-16, 5.924484345370516e-17, 7.94901921025252e-18, 9.844970759121082e-19, 1.1322195021765292e-19, 1.2304880868323627e-20]] |
| Legacy trial inputs | {"lambda_home": 1.4829833905087186, "lambda_away": 1.6100680660514837, "rho": -0.10363035671928646, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3353 |
| Legacy p draw | 0.2588 |
| Legacy p away | 0.4060 |
| Legacy p over 1 5 | 0.8257 |
| Legacy p under 3 5 | 0.6262 |
| Legacy p btts yes | 0.6293 |
| Legacy p over 2 5 | 0.5981 |
| Legacy goal margin distribution | {"-1": 0.19575266510864384, "-10": 1.8549834750022869e-06, "-11": 2.6675982793350617e-07, "-12": 3.5258133526581944e-08, "-13": 4.308412601790737e-09, "-14": 4.85050698175427e-10, "-15": 4.491476451323366e-11, "-2": 0.12472776126128009, "-3": 0.056772430728881586, "-4": 0.0205686006771607, "-5": 0.0061585821516965044, "-6": 0.0015670683637134379, "-7": 0.0003461443166557874, "-8": 6.748323263607291e-05, "-9": 1.1766854216870004e-05, "0": 0.2587614679397046, "1": 0.17201355507063656, "10": 7.81646413772607e-07, "11": 1.035339477071739e-07, "12": 1.260415438053056e-08, "13": 1.4186123419051876e-09, "14": 1.471043891739642e-10, "15": 1.2546415749449846e-11, "2": 0.1014605043993141, "3": 0.04253666426664731, "4": 0.014194586240645821, "5": 0.003914630545997577, "6": 0.0009174661190914773, "7": 0.00018666003722441808, "8": 3.3518306791120814e-05, "9": 5.383176468433607e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3421 |
| Legacy raw p draw | 0.2608 |
| Legacy raw p away | 0.3972 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4830 |
| Legacy lambda away | 1.6101 |
| Legacy model home team | Telstar |
| Legacy model away team | Utrecht |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 58.8% |
| Market reference home draw last update utc | 2026-10-31T12:02:43Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.8% |
| Market reference draw away last update utc | 2026-10-31T12:02:43Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market reference home away last update utc | 2026-10-31T12:02:43Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.59 |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 84.7% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T12:02:36Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.32 |
| Market reference over 1 5 last update utc | 2026-10-31T12:02:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.0% |
| Market under 3 5 odds | 1.61 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market reference under 3 5 last update utc | 2026-10-31T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.6% |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 2.69 |
| Market reference btts yes last update utc | 2026-10-31T12:02:14Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,388.0800 |
| Elo away rating | 1,522.9291 |
| Elo rating diff | -74.8492 |
| Elo home expectancy | 0.3939 |

</details>


---
