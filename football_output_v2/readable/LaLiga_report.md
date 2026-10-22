# La Liga — football model report

Fixtures in this report: **14**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,989 |
| Training data through | 2026-10-21 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | bd1148bb20208c2eb5c4201b88879ac67e77ae684e242738ae03d728392d8441 |
| Training as of utc | 2026-10-22T10:55:16.518314+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 88, 'bbs_added_results': 0, 'bbs_result_conflicts': 1, 'bbs_rows_with_statistics': 88, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 33, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T10:55:16.518314+00:00', 'observations': 175, 'observations_sha256': 'f09615c52756f016971653905b2d8dbaa942f7078acb69766b415d480f4de733', 'eligible_training_matches': 84, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 104, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 10, 'retrospective_eligible_training_matches': 84, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '183a6b181c2ec3ca9e73814b86fc6c314a1761a6434080fe28945eacd3785f37', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2505.902 |
| Base scoring parameter | 0.095 |
| Home-advantage parameter | 0.284 |
| Dixon-Coles low-score adjustment | -0.022 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-21', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 14.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261022T105516518314Z_3352e6ee975d5361c38f611958c9f268ff8c76bfeed3440ab4fdcd5fe3644994.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.2%**. Expected goals are 1.34 for Levante and 1.39 for Athletic Bilbao (2.73 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.8%; Under 3.5 goals: 70.9%; Double Chance 1X: 58.8%; Double Chance X2: 68.8%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 31.2% | 3.20 |
| Draw | 27.6% | 3.62 |
| Athletic Bilbao win | 41.2% | 2.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.34 |
| Athletic Bilbao expected goals | 1.39 |
| Expected total goals | 2.73 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.8% |
| Under 2.5 | 49.2% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.10% |
| 2 | 0-1 | 9.54% |
| 3 | 1-2 | 9.12% |
| 4 | 1-0 | 7.42% |
| 5 | 0-0 | 7.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 31.2% | 26.7% | 3.49 | +8.9% |
| Draw | 27.6% | 29.0% | 3.24 | -10.5% |
| Athletic Bilbao win | 41.2% | 44.2% | 2.31 | -4.9% |
| Over 2.5 | 50.8% | 46.1% | 2.12 | +7.7% |
| Under 2.5 | 49.2% | 53.9% | 1.84 | -9.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T18:00:00+00:00 |
| Fixture id | a362cccad837f1ffae61ff43a3536688 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3362 |
| Dc lambda away | 1.3892 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.91 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.43 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.18 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.2196768123036952, "-10": 6.172476778956373e-07, "-11": 7.688241447314217e-08, "-12": 8.793754589808232e-09, "-13": 9.236670208978937e-10, "-14": 8.092371324779243e-11, "-2": 0.12165286278200639, "-3": 0.04931848149570231, "-4": 0.015748369900691932, "-5": 0.004130408056293788, "-6": 0.0009170564696790632, "-7": 0.00017629492205623322, "-8": 2.985881688311893e-05, "-9": 4.517186316717959e-06, "0": 0.2762211132851096, "1": 0.17103792292687128, "10": 3.3884267117252556e-07, "11": 4.059542246727354e-08, "12": 4.466175786345623e-09, "13": 4.5121998679036833e-10, "14": 3.8024202398707476e-11, "2": 0.09115271489267635, "3": 0.03554417109753202, "4": 0.010917060602200617, "5": 0.002754066945852198, "6": 0.0005881512609917937, "7": 0.00010875373376993886, "8": 1.771692668643861e-05, "9": 2.5780730336945774e-06} |
| Raw goal margin distribution | {"-1": 0.20338756000998512, "-10": 5.714781538047252e-07, "-11": 7.118150761288025e-08, "-12": 8.141689013927931e-09, "-13": 8.551762003101249e-10, "-14": 7.492314009756483e-11, "-2": 0.11263218302374105, "-3": 0.04566146745129077, "-4": 0.01458061274035769, "-5": 0.003824134225208109, "-6": 0.0008490558279839811, "-7": 0.00016322247971077574, "-8": 2.7644756162279556e-05, "-9": 4.182232496152727e-06, "0": 0.26205500298859224, "1": 0.1955276346629687, "10": 3.873591592057225e-07, "11": 4.640799418830461e-08, "12": 5.105655941966473e-09, "13": 5.158269886585239e-10, "14": 4.3468619284765634e-11, "2": 0.10420422810965313, "3": 0.040633489823936685, "4": 0.012480197376655658, "5": 0.003148402333301167, "6": 0.0006723644845414604, "7": 0.00012432541252207634, "8": 2.0253688241862573e-05, "9": 2.9472090963254426e-06} |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 70.8% |
| Raw p btts yes | 55.6% |
| P home draw | 58.8% |
| P draw away | 68.8% |
| P home away | 72.4% |
| Raw p home draw | 61.9% |
| Raw p draw away | 64.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.55 |
| Reference draw odds | 3.28 |
| Reference away odds | 2.19 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | +4.5% |
| Draw probability edge | -1.4% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | +4.7% |
| Under 2.5 probability edge | -4.7% |
| Raw edge prob home | 0.0894 |
| Raw ev home | 0.2453 |
| Raw edge prob draw | -0.0283 |
| Raw ev draw | -0.1509 |
| Raw edge prob away | -0.0610 |
| Raw ev away | -0.1196 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **59.8%**. Expected goals are 1.75 for Alavés and 0.59 for Málaga (2.34 combined). The most likely exact score is 1-0 at 15.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 40.3%; Under 3.5 goals: 79.9%; Double Chance 1X: 84.4%; Double Chance X2: 40.2%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 37.7%; BTTS No (at least one team does not score): 62.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 59.8% | 1.67 |
| Draw | 24.5% | 4.08 |
| Málaga win | 15.6% | 6.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.75 |
| Málaga expected goals | 0.59 |
| Expected total goals | 2.34 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 20.1% |
| Under 3.5 | 79.9% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.26% |
| 2 | 2-0 | 13.51% |
| 3 | 1-1 | 10.89% |
| 4 | 0-0 | 10.55% |
| 5 | 2-1 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 59.8% | 54.5% | 1.76 | +5.3% |
| Draw | 24.5% | 26.1% | 3.76 | -7.8% |
| Málaga win | 15.6% | 19.4% | 4.97 | -22.3% |
| Over 2.5 | 40.3% | 46.1% | 2.12 | -14.5% |
| Under 2.5 | 59.7% | 53.9% | 1.84 | +9.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | 903eb4941471ffe20d525b02dd3b77aa |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7467 |
| Dc lambda away | 0.5916 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 37.7% |
| P btts no | 62.3% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.48 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 4.97 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.83 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.1187925644560069, "-10": 2.0247046747240178e-10, "-11": 1.0804511655694102e-11, "-12": 5.291432901617215e-13, "-13": 2.3943263710818602e-14, "-14": 1.0067346422249523e-15, "-15": 3.946104340817506e-17, "-16": 1.370471687371261e-18, "-2": 0.03105493803286095, "-3": 0.005659508529647892, "-4": 0.000797143299986001, "-5": 9.124338661484744e-05, "-6": 8.783783093044823e-06, "-7": 7.290438581753515e-07, "-8": 5.315508693000523e-08, "-9": 3.4545426771617393e-09, "0": 0.24527639882456362, "1": 0.24752389560312982, "10": 7.083847052891132e-06, "11": 1.1161995114570848e-06, "12": 1.6141324730019251e-07, "13": 2.1566438225359005e-08, "14": 2.677560456761883e-09, "15": 3.099003255227957e-10, "16": 3.177991500725982e-11, "2": 0.18802023569284967, "3": 0.10117700981390798, "4": 0.04207932039185665, "5": 0.014222073171700845, "6": 0.004042707412184491, "7": 0.0009907716225753746, "8": 0.00021330151094161247, "9": 4.0932555272955776e-05} |
| Raw goal margin distribution | {"-1": 0.08990704668457014, "-10": 1.5323788870665704e-10, "-11": 8.177294077965766e-12, "-12": 4.004771738808212e-13, "-13": 1.8121236275076385e-14, "-14": 7.619377432584411e-16, "-15": 2.986572339916552e-17, "-16": 1.0372287402045308e-18, "-2": 0.023503640790083796, "-3": 0.004283346351826705, "-4": 0.0006033104867659893, "-5": 6.905670786387805e-05, "-6": 6.647924474313218e-06, "-7": 5.517700581027909e-07, "-8": 4.022993277418641e-08, "-9": 2.614538470246107e-09, "0": 0.22951544345295177, "1": 0.2697777143881598, "10": 7.720725558022069e-06, "11": 1.216552253544386e-06, "12": 1.7592522460310744e-07, "13": 2.3505384794280143e-08, "14": 2.918288508676026e-09, "15": 3.3776214334366427e-10, "16": 3.4637111755282683e-11, "2": 0.20492433395306786, "3": 0.11027340366357488, "4": 0.045862492793518526, "5": 0.015500719172077, "6": 0.004406170010138664, "7": 0.0010798476776060133, "8": 0.0002324785409390658, "9": 4.4612626909001334e-05} |
| Unadjusted home-win probability | 65.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 11.8% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 79.2% |
| Raw p btts yes | 37.1% |
| P home draw | 84.4% |
| P draw away | 40.2% |
| P home away | 75.5% |
| Raw p home draw | 88.2% |
| Raw p draw away | 34.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.55, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.36, "price": 3.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.32, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.32, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.79 |
| Reference draw odds | 3.62 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | +5.4% |
| Draw probability edge | -1.6% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.1076 |
| Raw ev home | 0.1477 |
| Raw edge prob draw | -0.0315 |
| Raw ev draw | -0.1370 |
| Raw edge prob away | -0.0761 |
| Raw ev away | -0.4117 |
| Market p home draw | 78.8% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:54:50Z |
| Market reference home draw last update utc | 2026-10-22T10:55:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.5% |
| Market draw away odds | 2.15 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:54:50Z |
| Market reference draw away last update utc | 2026-10-22T10:55:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.7% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:54:50Z |
| Market reference home away last update utc | 2026-10-22T10:55:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 74.1% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:55:09Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.25 |
| Market reference over 1 5 last update utc | 2026-10-22T10:55:11Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.3% |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.80 |
| Market reference under 3 5 last update utc | 2026-10-22T10:54:48Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.9% |
| Market btts yes odds | 1.99 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:54:50Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 1.91 |
| Market reference btts yes last update utc | 2026-10-22T10:55:11Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **72.2%**. Expected goals are 2.24 for Atlético Madrid and 0.87 for Deportivo La Coruña (3.11 combined). The most likely exact score is 2-0 at 11.8%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.6%; Double Chance 1X: 88.9%; Double Chance X2: 27.8%; Double Chance 12 (either team wins): 83.3%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 72.2% | 1.38 |
| Draw | 16.7% | 6.00 |
| Deportivo La Coruña win | 11.1% | 9.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.24 |
| Deportivo La Coruña expected goals | 0.87 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 82.4% |
| Under 1.5 | 17.6% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 38.4% |
| Under 3.5 | 61.6% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.82% |
| 2 | 1-0 | 10.36% |
| 3 | 2-1 | 10.34% |
| 4 | 3-0 | 8.81% |
| 5 | 1-1 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 72.2% | 76.4% | 1.29 | -6.8% |
| Draw | 16.7% | 14.5% | 5.86 | -2.3% |
| Deportivo La Coruña win | 11.1% | 9.1% | 10.25 | +13.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 70df1835c3b5ddff1c99e0189532136b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2372 |
| Dc lambda away | 0.8750 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.35 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.68 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.60 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.76 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.07621339655113249, "-10": 3.266416193644515e-09, "-11": 2.5607081665970806e-10, "-12": 1.8442358165330784e-11, "-13": 1.2281905444714024e-12, "-14": 7.605605391566569e-14, "-15": 4.39985758431495e-15, "-16": 2.375769654312522e-16, "-17": 1.0965289767010776e-17, "-2": 0.02652750993401059, "-3": 0.006731535862730146, "-4": 0.0013482775281135615, "-5": 0.0002220768274621323, "-6": 3.0988617957060565e-05, "-7": 3.7459297180713795e-06, "-8": 3.9907736992853407e-07, "-9": 3.7986201188289304e-08, "0": 0.16679383919924767, "1": 0.24683482717631094, "10": 4.8770824341128137e-05, "11": 9.775834187426992e-06, "12": 1.8001776115628152e-06, "13": 3.0652776419492115e-07, "14": 4.8533657455850576e-08, "15": 7.178819190545261e-09, "16": 9.911146381176654e-10, "17": 1.169620135660486e-10, "2": 0.21684217309218362, "3": 0.14069108952065462, "4": 0.072050481758832, "5": 0.030343522910948103, "6": 0.010826052491798101, "7": 0.0033460521806038673, "8": 0.0009114552479719392, "9": 0.0002218243800581627} |
| Raw goal margin distribution | {"-1": 0.08980253566409561, "-10": 3.848830651796771e-09, "-11": 3.017292193530484e-10, "-12": 2.173070092422659e-11, "-13": 1.4471816001298421e-12, "-14": 8.961713823697121e-14, "-15": 5.184368962841004e-15, "-16": 2.799378439562619e-16, "-17": 1.2920442729625276e-17, "-2": 0.03125746607199647, "-3": 0.007931794366117644, "-4": 0.0015886805506992933, "-5": 0.00026167397230429564, "-6": 3.6514006660271506e-05, "-7": 4.413843265423946e-06, "-8": 4.702343861777163e-07, "-9": 4.475928565480228e-08, "0": 0.18860619513803256, "1": 0.23260914331065605, "10": 4.5960044610888924e-05, "11": 9.212429386474557e-06, "12": 1.6964290526699068e-06, "13": 2.8886183301589726e-07, "14": 4.5736546222767755e-08, "15": 6.765086600611962e-09, "16": 9.339943213545291e-10, "17": 1.1022121183918138e-10, "2": 0.20434503790895583, "3": 0.13258272416098923, "4": 0.06789803946535788, "5": 0.028594752815417474, "6": 0.010202121087858496, "7": 0.0031532111578690325, "8": 0.0008589258931654579, "9": 0.00020904010832268225} |
| Unadjusted home-win probability | 68.1% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 13.1% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 52.3% |
| P home draw | 88.9% |
| P draw away | 27.8% |
| P home away | 83.3% |
| Raw p home draw | 86.9% |
| Raw p draw away | 31.9% |
| Raw p home away | 81.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.75, "market_key": "spreads", "opposite_price": 2.01, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.29 |
| Reference draw odds | 6.20 |
| Reference away odds | 9.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:53Z |
| Home probability edge | -4.2% |
| Draw probability edge | +2.2% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.0832 |
| Raw ev home | -0.1221 |
| Raw edge prob draw | 0.0436 |
| Raw ev draw | 0.1052 |
| Raw edge prob away | 0.0396 |
| Raw ev away | 0.3416 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **51.1%**. Expected goals are 1.40 for Rayo Vallecano and 0.97 for Elche CF (2.37 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 43.0%; Under 3.5 goals: 78.2%; Double Chance 1X: 77.1%; Double Chance X2: 48.9%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 90.5%; BTTS Yes (both teams score): 46.6%; BTTS No (at least one team does not score): 53.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 51.1% | 1.96 |
| Draw | 26.1% | 3.84 |
| Elche CF win | 22.9% | 4.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.40 |
| Elche CF expected goals | 0.97 |
| Expected total goals | 2.37 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 69.2% |
| Under 1.5 | 30.8% |
| Over 2.5 | 43.0% |
| Under 2.5 | 57.0% |
| Over 3.5 | 21.8% |
| Under 3.5 | 78.2% |
| Over 4.5 | 9.5% |
| Under 4.5 | 90.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.99% |
| 2 | 1-1 | 12.24% |
| 3 | 2-0 | 10.04% |
| 4 | 2-1 | 9.73% |
| 5 | 0-0 | 9.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 51.1% | 55.4% | 1.78 | -9.1% |
| Draw | 26.1% | 24.5% | 3.92 | +2.1% |
| Elche CF win | 22.9% | 20.1% | 4.55 | +4.1% |
| Over 2.5 | 43.0% | 52.7% | 1.85 | -20.5% |
| Under 2.5 | 57.0% | 47.3% | 2.04 | +16.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T12:00:00+00:00 |
| Fixture id | 734ad601156f5f4e6bc42317e5141516 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Vallecano |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4044 |
| Dc lambda away | 0.9691 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.6% |
| P btts no | 53.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.03 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.24 |
| Fair Over 2.5 odds | 2.33 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.58 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.56 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.14655762605610598, "-10": 1.8898239364620024e-08, "-11": 1.6481199648192092e-09, "-12": 1.319415818071358e-10, "-13": 9.724584606790096e-12, "-14": 6.135198714899277e-13, "-2": 0.05993756515252408, "-3": 0.017498982593470082, "-4": 0.003980210475235329, "-5": 0.0007389652952773653, "-6": 0.00011569613473478913, "-7": 1.5644403241590768e-05, "-8": 1.860516008838925e-06, "-9": 1.9739195831041458e-07, "0": 0.2605014991323642, "1": 0.2619349751915946, "10": 9.471308459834165e-07, "11": 1.1970121716442036e-07, "12": 1.3887131352041982e-08, "13": 1.4832796104293977e-09, "14": 1.356131213989902e-10, "2": 0.15442543948996995, "3": 0.06533616800219089, "4": 0.021536147115708525, "5": 0.005794382016991525, "6": 0.001314689039814876, "7": 0.0002576228051176797, "8": 4.439967847934142e-05, "9": 6.826482485840019e-06} |
| Raw goal margin distribution | {"-1": 0.16453385199214848, "-10": 2.1216228743635804e-08, "-11": 1.8502723717226236e-09, "-12": 1.4812505685889397e-10, "-13": 1.0917366823110227e-11, "-14": 6.887719898746275e-13, "-2": 0.06728928912781255, "-3": 0.019645344220743356, "-4": 0.00446840863115007, "-5": 0.0008296040935730941, "-6": 0.00012988700227192554, "-7": 1.7563288903656072e-05, "-8": 2.0887201428203857e-06, "-9": 2.2160333874849206e-07, "0": 0.27578549979780626, "1": 0.2396971154852555, "10": 8.667209547074639e-07, "11": 1.0953877561940204e-07, "12": 1.2708136151021869e-08, "13": 1.3573515481006648e-09, "14": 1.2409978467943382e-10, "2": 0.14131496710667782, "3": 0.05978923202420719, "4": 0.01970776273205034, "5": 0.00530244826784428, "6": 0.001203074046805714, "7": 0.00023575104174140672, "8": 4.0630216916188396e-05, "9": 6.246925060578841e-06} |
| Unadjusted home-win probability | 46.7% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 68.9% |
| Raw p under 3 5 | 78.4% |
| Raw p btts yes | 47.1% |
| P home draw | 77.1% |
| P draw away | 48.9% |
| P home away | 73.9% |
| Raw p home draw | 74.3% |
| Raw p draw away | 53.3% |
| Raw p home away | 72.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.13, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.44, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.76 |
| Reference draw odds | 3.84 |
| Reference away odds | 4.65 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:48Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:48Z |
| Home probability edge | -4.3% |
| Draw probability edge | +1.5% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.0867 |
| Raw ev home | -0.1682 |
| Raw edge prob draw | 0.0306 |
| Raw ev draw | 0.0811 |
| Raw edge prob away | 0.0561 |
| Raw ev away | 0.1690 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **38.2%**. Expected goals are 1.84 for Real Racing Club de Santander and 2.02 for Espanyol (3.86 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 73.4%; Under 3.5 goals: 46.3%; Double Chance 1X: 61.8%; Double Chance X2: 61.9%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 66.2%; BTTS Yes (both teams score): 73.6%; BTTS No (at least one team does not score): 26.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 38.1% | 2.62 |
| Draw | 23.6% | 4.23 |
| Espanyol win | 38.2% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.84 |
| Espanyol expected goals | 2.02 |
| Expected total goals | 3.86 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 89.9% |
| Under 1.5 | 10.1% |
| Over 2.5 | 73.4% |
| Under 2.5 | 26.6% |
| Over 3.5 | 53.7% |
| Under 3.5 | 46.3% |
| Over 4.5 | 33.8% |
| Under 4.5 | 66.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.86% |
| 2 | 2-2 | 8.04% |
| 3 | 2-1 | 7.67% |
| 4 | 1-2 | 7.07% |
| 5 | 1-3 | 4.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 38.1% | 40.4% | 2.43 | -7.4% |
| Draw | 23.6% | 25.9% | 3.68 | -13.0% |
| Espanyol win | 38.2% | 33.7% | 2.85 | +9.0% |
| Over 2.5 | 73.4% | 57.3% | 1.73 | +26.9% |
| Under 2.5 | 26.6% | 42.7% | 2.28 | -39.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:15:00+00:00 |
| Fixture id | 5960b1b6c20acfd78e78764fed47d505 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8409 |
| Dc lambda away | 2.0167 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 73.6% |
| P btts no | 26.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.58 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.87 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.75 |
| Fair Over 3.5 odds | 1.86 |
| Fair Under 3.5 odds | 2.16 |
| Fair Over 4.5 odds | 2.96 |
| Fair Under 4.5 odds | 1.51 |
| Goal margin distribution | {"-1": 0.16741455951443743, "-10": 8.080003252825012e-06, "-11": 1.4417065008375978e-06, "-12": 2.3676237447405673e-07, "-13": 3.600636972958934e-08, "-14": 5.097426971962637e-09, "-15": 6.740943199021198e-10, "-16": 8.232943458212356e-11, "-17": 8.015949509358204e-12, "-2": 0.11441609226534302, "-3": 0.060791173833965685, "-4": 0.02627206518927138, "-5": 0.00950985465934961, "-6": 0.0029510072172128977, "-7": 0.0007996598489889955, "-8": 0.000192057701365532, "-9": 4.138230290294235e-05, "0": 0.23645452367669764, "1": 0.18141697395649822, "10": 3.857621593946132e-06, "11": 6.283322065999246e-07, "12": 9.419536361209434e-08, "13": 1.3076772027833149e-08, "14": 1.6899606963242631e-09, "15": 2.040096144773489e-10, "16": 2.2745185131872098e-11, "17": 2.0215928462117334e-12, "2": 0.11328181353140487, "3": 0.05494371076825107, "4": 0.02167584549832947, "5": 0.00716242502869577, "6": 0.002028901003520484, "7": 0.0005018804187660494, "8": 0.00011003505468568373, "9": 2.1643045275485807e-05} |
| Raw goal margin distribution | {"-1": 0.18715488026090663, "-10": 9.032739121831228e-06, "-11": 1.6117021620951823e-06, "-12": 2.646796907837561e-07, "-13": 4.025198187610493e-08, "-14": 5.698478897793307e-09, "-15": 7.535786737530364e-10, "-16": 9.203712936231633e-11, "-17": 8.961132621634575e-12, "-2": 0.12790721493965687, "-3": 0.06795923181839304, "-4": 0.029369878157346246, "-5": 0.010631188322158529, "-6": 0.003298968763460043, "-7": 0.0008939499869130784, "-8": 0.00021470376415589672, "-9": 4.626180642343024e-05, "0": 0.2138906695843455, "1": 0.17069528295591924, "10": 3.629637266871151e-06, "11": 5.911979538453186e-07, "12": 8.86284447052768e-08, "13": 1.2303938560767041e-08, "14": 1.5900845050619348e-09, "15": 1.9195270491772918e-10, "16": 2.140095123017901e-11, "17": 1.9021172902405447e-12, "2": 0.10658689092201235, "3": 0.05169655325903349, "4": 0.02039480926152669, "5": 0.006739127768810356, "6": 0.001908993537553559, "7": 0.00047221943031553593, "8": 0.0001035320145905788, "9": 2.0363947522422504e-05} |
| Unadjusted home-win probability | 35.9% |
| Unadjusted draw probability | 21.4% |
| Unadjusted away-win probability | 42.7% |
| Raw p over 1 5 | 89.9% |
| Raw p under 3 5 | 46.2% |
| Raw p btts yes | 73.1% |
| P home draw | 61.8% |
| P draw away | 61.9% |
| P home away | 76.4% |
| Raw p home draw | 57.3% |
| Raw p draw away | 64.1% |
| Raw p home away | 78.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.39 |
| Reference draw odds | 3.66 |
| Reference away odds | 2.84 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | -2.3% |
| Draw probability edge | -2.3% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | +16.1% |
| Under 2.5 probability edge | -16.1% |
| Raw edge prob home | -0.0451 |
| Raw ev home | -0.1285 |
| Raw edge prob draw | -0.0451 |
| Raw ev draw | -0.2129 |
| Raw edge prob away | 0.0902 |
| Raw ev away | 0.2183 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **43.9%**. Expected goals are 1.26 for Valencia and 1.54 for Villarreal (2.80 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 52.9%; Under 3.5 goals: 69.2%; Double Chance 1X: 56.1%; Double Chance X2: 69.8%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 84.8%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.2% | 3.31 |
| Draw | 25.9% | 3.85 |
| Villarreal win | 43.9% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.26 |
| Villarreal expected goals | 1.54 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 52.9% |
| Under 2.5 | 47.1% |
| Over 3.5 | 30.8% |
| Under 3.5 | 69.2% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.26% |
| 2 | 0-1 | 9.17% |
| 3 | 1-2 | 9.15% |
| 4 | 2-1 | 7.26% |
| 5 | 0-2 | 7.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.2% | 29.4% | 3.21 | -3.0% |
| Draw | 25.9% | 26.4% | 3.74 | -3.0% |
| Villarreal win | 43.9% | 44.2% | 2.20 | -3.5% |
| Over 2.5 | 52.9% | 55.3% | 1.79 | -5.3% |
| Under 2.5 | 47.1% | 44.7% | 2.19 | +3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0dae715cc56fe201f9e667917c126691 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2620 |
| Dc lambda away | 1.5381 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.52 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.25 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.58 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.21814407747511155, "-10": 1.492209060797493e-06, "-11": 2.0566471377813727e-07, "-12": 2.6040245324342685e-08, "-13": 3.0477978979602755e-09, "-14": 3.295311040177646e-10, "-15": 2.9918715585566836e-11, "-2": 0.13246579487728927, "-3": 0.059149139726149005, "-4": 0.020839829722221002, "-5": 0.006036893825395344, "-6": 0.0014813396777377007, "-7": 0.00031486105147621033, "-8": 5.8979190976432136e-05, "-9": 9.870345201073764e-06, "0": 0.2594534095334598, "1": 0.17249130281871675, "10": 1.9930621898524852e-07, "11": 2.2537654188402394e-08, "12": 2.3412713174159153e-09, "13": 2.248280979471874e-10, "14": 1.994429009143857e-11, "15": 1.4856717391691302e-12, "2": 0.08616540714228127, "3": 0.031567150078701964, "4": 0.009125125716728327, "5": 0.0021687823784626017, "6": 0.00043663127655119724, "7": 7.614420827603786e-05, "8": 1.1702387986048599e-05, "9": 1.6068146082386425e-06} |
| Raw goal margin distribution | {"-1": 0.2162924167294663, "-10": 1.4795428221622035e-06, "-11": 2.0391898095020478e-07, "-12": 2.5819209297913956e-08, "-13": 3.021927437512148e-09, "-14": 3.2673396271170063e-10, "-15": 2.966475814674413e-11, "-2": 0.13134139253112442, "-3": 0.058647067236089805, "-4": 0.020662936106363057, "-5": 0.005985651181306653, "-6": 0.0014687657011072937, "-7": 0.0003121884331952137, "-8": 5.8478561053286795e-05, "-9": 9.78656327599775e-06, "0": 0.2552961157123705, "1": 0.17699107629015465, "10": 2.0450551206395503e-07, "11": 2.3125593039626674e-08, "12": 2.4023479652896857e-09, "13": 2.3069317922516837e-10, "14": 2.0464575960891577e-11, "15": 1.5244283962871082e-12, "2": 0.08841320054912902, "3": 0.03239064101518313, "4": 0.009363172493305951, "5": 0.0022253593145309934, "6": 0.0004480216585757915, "7": 7.813057908317509e-05, "8": 1.200766769668675e-05, "9": 1.6487315143638747e-06} |
| Unadjusted home-win probability | 31.0% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 43.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 56.6% |
| P home draw | 56.1% |
| P draw away | 69.8% |
| P home away | 74.1% |
| Raw p home draw | 56.5% |
| Raw p draw away | 69.0% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.24 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.19 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | +0.8% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.0158 |
| Raw ev home | -0.0051 |
| Raw edge prob draw | -0.0083 |
| Raw ev draw | -0.0452 |
| Raw edge prob away | -0.0074 |
| Raw ev away | -0.0435 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **55.0%**. Expected goals are 1.20 for Athletic Bilbao and 0.62 for Getafe (1.82 combined). The most likely exact score is 1-0 at 21.2%. Goal-market probabilities: at least one goal: 85.5%; Over 2.5 goals: 28.7%; Under 3.5 goals: 88.5%; Double Chance 1X: 82.5%; Double Chance X2: 45.0%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 31.8%; BTTS No (at least one team does not score): 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 55.0% | 1.82 |
| Draw | 27.5% | 3.63 |
| Getafe win | 17.5% | 5.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.20 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.82 |
| Over 0.5 | 85.5% |
| Under 0.5 | 14.5% |
| Over 1.5 | 55.3% |
| Under 1.5 | 44.7% |
| Over 2.5 | 28.7% |
| Under 2.5 | 71.3% |
| Over 3.5 | 11.5% |
| Under 3.5 | 88.5% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.16% |
| 2 | 0-0 | 14.49% |
| 3 | 2-0 | 12.84% |
| 4 | 1-1 | 10.88% |
| 5 | 0-1 | 9.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 55.0% | 60.3% | 1.64 | -9.8% |
| Draw | 27.5% | 23.8% | 4.08 | +12.3% |
| Getafe win | 17.5% | 15.9% | 5.51 | -3.8% |
| Over 2.5 | 28.7% | 41.1% | 2.36 | -32.2% |
| Under 2.5 | 71.3% | 58.9% | 1.69 | +20.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:00:00+00:00 |
| Fixture id | 9c4254cba9944a839b421db27260504d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1966 |
| Dc lambda away | 0.6241 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 31.8% |
| P btts no | 68.2% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.90 |
| Fair Over 1.5 odds | 1.81 |
| Fair Under 1.5 odds | 2.24 |
| Fair Over 2.5 odds | 3.48 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.66 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.92 |
| Fair Under 4.5 odds | 1.04 |
| Goal margin distribution | {"-1": 0.1293336171291296, "-10": 3.9247694547688416e-10, "-11": 2.2143521209766028e-11, "-12": 1.1445905884820326e-12, "-13": 5.196655208091722e-14, "-2": 0.03680344442533054, "-3": 0.007223011852456048, "-4": 0.0010873930927815917, "-5": 0.00013249394914172333, "-6": 1.3544584674703566e-05, "-7": 1.1919251303113114e-06, "-8": 9.204296201819537e-08, "-9": 6.330818046091689e-09, "0": 0.27530919004624166, "1": 0.3022873253192587, "10": 3.1820409130629394e-07, "11": 3.442041505079158e-08, "12": 3.41112318216481e-09, "13": 2.969264918445467e-10, "2": 0.16343970835335436, "3": 0.061498603224062885, "4": 0.01775052925019926, "5": 0.004146661585391936, "6": 0.000812729554670552, "7": 0.0001371220031108442, "8": 2.0301427223824755e-05, "9": 2.677155688401216e-06} |
| Raw goal margin distribution | {"-1": 0.14111235700514582, "-10": 4.282208143233731e-10, "-11": 2.416018773513252e-11, "-12": 1.2488313505168996e-12, "-13": 5.669927751457952e-14, "-2": 0.040155227264548385, "-3": 0.007880829824457236, "-4": 0.0011864247341070119, "-5": 0.00014456050845343217, "-6": 1.4778124284538515e-05, "-7": 1.300476768881865e-06, "-8": 1.0042554754464768e-07, "-9": 6.90738166986208e-09, "0": 0.3127077950691841, "1": 0.27299838095437956, "10": 2.8737295435040645e-07, "11": 3.108538398267139e-08, "12": 3.0806157849437805e-09, "13": 2.68156964406012e-10, "2": 0.14760385906685933, "3": 0.05553993735395072, "4": 0.016030661362562346, "5": 0.0037448870804693227, "6": 0.0007339833132087295, "7": 0.00012383610461651375, "8": 1.8334400085461425e-05, "9": 2.4177631917727523e-06} |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 31.3% |
| Unadjusted away-win probability | 19.0% |
| Raw p over 1 5 | 54.6% |
| Raw p under 3 5 | 88.8% |
| Raw p btts yes | 32.7% |
| P home draw | 82.5% |
| P draw away | 45.0% |
| P home away | 72.5% |
| Raw p home draw | 81.0% |
| Raw p draw away | 50.3% |
| Raw p home away | 68.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.08, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.62 |
| Reference draw odds | 3.94 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.29 |
| Reference Under 2.5 odds | 1.64 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | -5.3% |
| Draw probability edge | +3.7% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -12.4% |
| Under 2.5 probability edge | +12.4% |
| Raw edge prob home | -0.1066 |
| Raw ev home | -0.1853 |
| Raw edge prob draw | 0.0748 |
| Raw ev draw | 0.2758 |
| Raw edge prob away | 0.0318 |
| Raw ev away | 0.0496 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **56.6%**. Expected goals are 1.97 for Barcelona and 1.35 for Real Madrid (3.32 combined). The most likely exact score is 2-1 at 10.4%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 65.5%; Under 3.5 goals: 57.2%; Double Chance 1X: 76.4%; Double Chance X2: 43.4%; Double Chance 12 (either team wins): 80.2%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 56.6% | 1.77 |
| Draw | 19.8% | 5.06 |
| Real Madrid win | 23.6% | 4.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.97 |
| Real Madrid expected goals | 1.35 |
| Expected total goals | 3.32 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.37% |
| 2 | 1-1 | 8.71% |
| 3 | 2-0 | 7.67% |
| 4 | 1-0 | 7.55% |
| 5 | 3-1 | 6.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 56.6% | 61.5% | 1.62 | -8.3% |
| Draw | 19.8% | 17.3% | 5.84 | +15.5% |
| Real Madrid win | 23.6% | 21.2% | 4.04 | -4.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T20:00:00+00:00 |
| Fixture id | 72089d103a5fe6a922c35e17efba6ffc |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9720 |
| Dc lambda away | 1.3512 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.52 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.60 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.13392803155461172, "-10": 2.3241772409015852e-07, "-11": 2.7994332327094646e-08, "-12": 3.1000426072216656e-09, "-13": 3.1761973351257845e-10, "-14": 3.025624777078918e-11, "-15": 2.6663650185685706e-12, "-16": 1.9303254457579004e-13, "-2": 0.066958012241142, "-3": 0.02517955576352079, "-4": 0.007574663286304308, "-5": 0.0018888534777584795, "-6": 0.00040105371768470876, "-7": 7.401715548137903e-05, "-8": 1.2067759285076673e-05, "-9": 1.7608944116780815e-06, "0": 0.19771913680007927, "1": 0.23689602556691045, "10": 1.2291618710186008e-05, "11": 2.1606747300810318e-06, "12": 3.4919368794306065e-07, "13": 5.221384096345151e-08, "14": 7.2589311312239475e-09, "15": 9.335909951798029e-10, "16": 9.863862959564551e-11, "2": 0.17207066750003674, "3": 0.09443474192203735, "4": 0.04145973379599669, "5": 0.015088320145248897, "6": 0.004675462842705015, "7": 0.0012593136110288436, "8": 0.00029964538155407904, "9": 6.381072923810408e-05} |
| Raw goal margin distribution | {"-1": 0.14758661872389373, "-10": 2.561207361282105e-07, "-11": 3.08493211139608e-08, "-12": 3.416198991271555e-09, "-13": 3.5001203232043994e-10, "-14": 3.334191693799564e-11, "-15": 2.938292998159555e-12, "-16": 2.127188776458139e-13, "-2": 0.07378669355797725, "-3": 0.027747480889334406, "-4": 0.008347161751136594, "-5": 0.0020814873093506782, "-6": 0.0004419549920406118, "-7": 8.156576019414577e-05, "-8": 1.3298484027461317e-05, "-9": 1.940478398231332e-06, "0": 0.22272408032112545, "1": 0.2163654274409275, "10": 1.1226365363479416e-05, "11": 1.973419817474948e-06, "12": 3.1893081097780757e-07, "13": 4.7688727539242396e-08, "14": 6.629835740017171e-09, "15": 8.526813155420609e-10, "16": 9.009011106698027e-11, "2": 0.15715816014471556, "3": 0.08625055339083443, "4": 0.03786662525422664, "5": 0.013780690620621079, "6": 0.004270263775110568, "7": 0.0011501751752921448, "8": 0.00027367660941334074, "9": 5.828057129232038e-05} |
| Unadjusted home-win probability | 51.7% |
| Unadjusted draw probability | 22.3% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 64.0% |
| P home draw | 76.4% |
| P draw away | 43.4% |
| P home away | 80.2% |
| Raw p home draw | 74.0% |
| Raw p draw away | 48.3% |
| Raw p home away | 77.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.59 |
| Reference draw odds | 5.35 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.18 |
| Reference Under 2.5 odds | 4.97 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:53Z |
| Home probability edge | -4.9% |
| Draw probability edge | +2.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -17.7% |
| Under 2.5 probability edge | +17.7% |
| Raw edge prob home | -0.0982 |
| Raw ev home | -0.1622 |
| Raw edge prob draw | 0.0500 |
| Raw ev draw | 0.3007 |
| Raw edge prob away | 0.0481 |
| Raw ev away | 0.0508 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **37.7%**. Expected goals are 1.41 for Celta Vigo and 1.29 for Real Betis (2.70 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.5%; Double Chance 1X: 64.5%; Double Chance X2: 62.3%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 37.7% | 2.65 |
| Draw | 26.8% | 3.73 |
| Real Betis win | 35.5% | 2.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.41 |
| Real Betis expected goals | 1.29 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.5% |
| Under 3.5 | 71.5% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.74% |
| 2 | 0-1 | 8.76% |
| 3 | 1-0 | 8.75% |
| 4 | 1-2 | 8.22% |
| 5 | 2-1 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 37.7% | 35.6% | 2.87 | +8.3% |
| Draw | 26.8% | 27.4% | 3.54 | -5.0% |
| Real Betis win | 35.5% | 37.0% | 2.49 | -11.7% |
| Over 2.5 | 50.4% | 51.7% | 1.88 | -5.2% |
| Under 2.5 | 49.6% | 48.3% | 2.01 | -0.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:15:00+00:00 |
| Fixture id | 2013e3955186ebe5258e85eb741a7553 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4145 |
| Dc lambda away | 1.2853 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.02 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.34 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1988440855377819, "-10": 2.8110007085507837e-07, "-11": 3.240362125454673e-08, "-12": 3.4300131634368195e-09, "-13": 3.334936026691808e-10, "-14": 2.709811720484859e-11, "-2": 0.10238020462400671, "-3": 0.03849265238190236, "-4": 0.011390160961802183, "-5": 0.0027670186952354135, "-6": 0.0005688723340657471, "-7": 0.00010124542305280998, "-8": 1.587332041805858e-05, "-9": 2.2227038740148567e-06, "0": 0.26825106115464004, "1": 0.19827224031735616, "10": 6.627811083420655e-07, "11": 8.4080290853627e-08, "12": 9.794627791484386e-09, "13": 1.0480238103947877e-09, "14": 9.371610952619838e-11, "2": 0.11220009433442814, "3": 0.04642442770181795, "4": 0.015117851482302708, "5": 0.004041697434431036, "6": 0.0009144458864578676, "7": 0.00017910598105852184, "8": 3.0902524869708165e-05, "9": 4.762108434666918e-06} |
| Raw goal margin distribution | {"-1": 0.18998600701655316, "-10": 2.6857766420052323e-07, "-11": 3.0960109265398874e-08, "-12": 3.2772134165979902e-09, "-13": 3.186371762847522e-10, "-14": 2.5890954068319695e-11, "-2": 0.09781938558266486, "-3": 0.03677788708542857, "-4": 0.010882753663786738, "-5": 0.0026437539332697067, "-6": 0.0005435302888644498, "-7": 9.67351561022428e-05, "-8": 1.5166197959397013e-05, "-9": 2.1236871726017192e-06, "0": 0.2629687806502332, "1": 0.20935175532983746, "10": 6.998175246760474e-07, "11": 8.877872389334792e-08, "12": 1.0341954666309223e-08, "13": 1.1065877098197463e-09, "14": 9.89529951373404e-11, "2": 0.11846987081746156, "3": 0.04901863929111989, "4": 0.0159626417675516, "5": 0.004267548755468265, "6": 0.0009655454095726262, "7": 0.00018911447948869454, "8": 3.262936765753102e-05, "9": 5.028216548483077e-06} |
| Unadjusted home-win probability | 39.8% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 33.9% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 55.0% |
| P home draw | 64.5% |
| P draw away | 62.3% |
| P home away | 73.2% |
| Raw p home draw | 66.1% |
| Raw p draw away | 60.2% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.70 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:48Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:48Z |
| Home probability edge | +2.1% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | 0.0422 |
| Raw ev home | 0.1430 |
| Raw edge prob draw | -0.0106 |
| Raw ev draw | -0.0691 |
| Raw edge prob away | -0.0316 |
| Raw ev away | -0.1565 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **56.3%**. Expected goals are 1.97 for Real Sociedad and 1.18 for Levante (3.16 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.1%; Under 3.5 goals: 61.1%; Double Chance 1X: 78.7%; Double Chance X2: 43.7%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 56.3% | 1.78 |
| Draw | 22.4% | 4.46 |
| Levante win | 21.3% | 4.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.97 |
| Levante expected goals | 1.18 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 82.6% |
| Under 1.5 | 17.4% |
| Over 2.5 | 61.1% |
| Under 2.5 | 38.9% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.26% |
| 2 | 2-1 | 9.95% |
| 3 | 2-0 | 8.40% |
| 4 | 1-0 | 8.30% |
| 5 | 3-1 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 56.3% | 57.1% | 1.75 | -1.5% |
| Draw | 22.4% | 22.6% | 4.18 | -6.4% |
| Levante win | 21.3% | 20.3% | 4.43 | -5.5% |
| Over 2.5 | 61.1% | 58.1% | 1.71 | +4.4% |
| Under 2.5 | 38.9% | 41.9% | 2.32 | -9.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:30:00+00:00 |
| Fixture id | 3cb8660cd2375b60e81144a7572cfb89 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9725 |
| Dc lambda away | 1.1843 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.14 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.74 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.57 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.72 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.1288388341607328, "-10": 7.498861215698338e-08, "-11": 7.935340026628797e-09, "-12": 7.717571563709471e-10, "-13": 6.942598263621405e-11, "-14": 5.8065050448663895e-12, "-15": 4.501638164066371e-13, "-16": 2.907603902669192e-14, "-2": 0.05824464047460729, "-3": 0.019559368021075555, "-4": 0.0052230821616325905, "-5": 0.0011520126180591078, "-6": 0.00021585380502696887, "-7": 3.5100855251197803e-05, "-8": 5.036984754777005e-06, "-9": 6.463912689898695e-07, "0": 0.2240070040298794, "1": 0.22970283778647807, "10": 1.3098918089555979e-05, "11": 2.308628375571806e-06, "12": 3.739534392817445e-07, "13": 5.602827865334725e-08, "14": 7.804560118538545e-09, "15": 1.0077494846315238e-09, "16": 1.0840907076687908e-10, "2": 0.17183398215932894, "3": 0.09610727913370919, "4": 0.04274415141246623, "5": 0.015702017463877383, "6": 0.004900115387282171, "7": 0.001327127579887704, "8": 0.0003171859857932781, "9": 6.779336856557446e-05} |
| Raw goal margin distribution | {"-1": 0.1350330245174702, "-10": 7.859384299684355e-08, "-11": 8.316847721809085e-09, "-12": 8.088609594818339e-10, "-13": 7.276377868934942e-11, "-14": 6.085664646003328e-12, "-15": 4.718063622174711e-13, "-16": 3.047392904738683e-14, "-2": 0.06104487064363661, "-3": 0.02049972462682439, "-4": 0.00547419251487958, "-5": 0.001207397979903653, "-6": 0.00022623141800579404, "-7": 3.678840062931696e-05, "-8": 5.279148094722704e-06, "-9": 6.774678507607141e-07, "0": 0.22193802252769734, "1": 0.2263618526424854, "10": 1.290839675703216e-05, "11": 2.2750498043181274e-06, "12": 3.685143559111393e-07, "13": 5.521335773888159e-08, "14": 7.691044240098798e-09, "15": 9.930919554104444e-10, "16": 1.0683228095271549e-10, "2": 0.16933468878028468, "3": 0.09470941659570362, "4": 0.04212244566325659, "5": 0.015473634534075308, "6": 0.004828844118409223, "7": 0.0013078247555459814, "8": 0.0003125725744979285, "9": 6.680732660187288e-05} |
| Unadjusted home-win probability | 55.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 22.4% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.2% |
| Raw p btts yes | 60.0% |
| P home draw | 78.7% |
| P draw away | 43.7% |
| P home away | 77.6% |
| Raw p home draw | 77.6% |
| Raw p draw away | 44.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.71 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | -0.8% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0164 |
| Raw ev home | -0.0296 |
| Raw edge prob draw | -0.0041 |
| Raw ev draw | -0.0723 |
| Raw edge prob away | 0.0205 |
| Raw ev away | -0.0098 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **48.4%**. Expected goals are 1.51 for Sevilla and 1.06 for CA Osasuna (2.57 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 47.3%; Under 3.5 goals: 74.2%; Double Chance 1X: 75.1%; Double Chance X2: 51.6%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 48.4% | 2.07 |
| Draw | 26.7% | 3.74 |
| CA Osasuna win | 24.9% | 4.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.51 |
| CA Osasuna expected goals | 1.06 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 47.3% |
| Under 2.5 | 52.7% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.71% |
| 2 | 1-0 | 11.53% |
| 3 | 2-1 | 9.44% |
| 4 | 2-0 | 8.92% |
| 5 | 0-0 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 48.4% | 49.3% | 1.99 | -3.7% |
| Draw | 26.7% | 27.1% | 3.38 | -9.7% |
| CA Osasuna win | 24.9% | 23.6% | 4.22 | +5.2% |
| Over 2.5 | 47.3% | 44.7% | 2.19 | +3.6% |
| Under 2.5 | 52.7% | 55.3% | 1.79 | -5.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T20:00:00+00:00 |
| Fixture id | 85e464708d03287f24590e1478aeca31 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5109 |
| Dc lambda away | 1.0581 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.42 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.70 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.88 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.47 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.15454816883679365, "-10": 4.072191296078403e-08, "-11": 3.870849259265938e-09, "-12": 3.3789328329961813e-10, "-13": 2.7260590267819262e-11, "-14": 2.0352182622908203e-12, "-15": 1.2974280263950565e-13, "-2": 0.0671944500101443, "-3": 0.021089431608773006, "-4": 0.005184749656793966, "-5": 0.0010436185192330217, "-6": 0.00017747862204130378, "-7": 2.6099226500161297e-05, "-8": 3.3783854755191533e-06, "-9": 3.903678617287069e-07, "0": 0.26702532627479614, "1": 0.23849502974234257, "10": 1.5424056119699232e-06, "11": 2.09341711580753e-07, "12": 2.6092047263084276e-08, "13": 3.005681367205094e-09, "14": 3.204038757467578e-10, "15": 2.9164137096302405e-11, "2": 0.147323198790216, "3": 0.06602093910322117, "4": 0.02317521117694982, "5": 0.006660652434679884, "6": 0.0016173355365160379, "7": 0.0003395946216315332, "8": 6.276556671451345e-05, "9": 1.0355364614227894e-05} |
| Raw goal margin distribution | {"-1": 0.1629205067497993, "-10": 4.2927941141756685e-08, "-11": 4.080544775251673e-09, "-12": 3.561979760540614e-10, "-13": 2.873737821780265e-11, "-14": 2.145472140721518e-12, "-15": 1.3677135945550679e-13, "-2": 0.07083457493428742, "-3": 0.022231909382212874, "-4": 0.005465623098697112, "-5": 0.0011001544650229486, "-6": 0.0001870931713902097, "-7": 2.7513099891040324e-05, "-8": 3.5614027510671157e-06, "-9": 4.11515259807694e-07, "0": 0.2630798938458695, "1": 0.23378231619893505, "10": 1.5119273423606518e-06, "11": 2.0520507393076696e-07, "12": 2.5576462746942328e-08, "13": 2.946288451127564e-09, "14": 3.140726256313014e-10, "15": 2.8587847418383236e-11, "2": 0.1444120604115804, "3": 0.06471635101936732, "4": 0.022717263974851173, "5": 0.006529036497145431, "6": 0.0015853766353372256, "7": 0.00033288415821281853, "8": 6.152530549550735e-05, "9": 1.0150740362237748e-05} |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 72.9% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.2% |
| P home draw | 75.1% |
| P draw away | 51.6% |
| P home away | 73.3% |
| Raw p home draw | 73.7% |
| Raw p draw away | 52.6% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.48, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.96, "price": 1.48, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.97 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +2.6% |
| Under 2.5 probability edge | -2.6% |
| Raw edge prob home | -0.0191 |
| Raw ev home | -0.0564 |
| Raw edge prob draw | -0.0079 |
| Raw ev draw | -0.1108 |
| Raw edge prob away | 0.0270 |
| Raw ev away | 0.1089 |

</details>


---

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **63.6%**. Expected goals are 2.18 for Villarreal and 0.98 for Espanyol (3.16 combined). The most likely exact score is 2-0 at 9.9%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.0%; Under 3.5 goals: 61.3%; Double Chance 1X: 83.9%; Double Chance X2: 36.4%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 78.9%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 63.6% | 1.57 |
| Draw | 20.3% | 4.93 |
| Espanyol win | 16.1% | 6.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.18 |
| Espanyol expected goals | 0.98 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 82.5% |
| Under 1.5 | 17.5% |
| Over 2.5 | 61.0% |
| Under 2.5 | 39.0% |
| Over 3.5 | 38.7% |
| Under 3.5 | 61.3% |
| Over 4.5 | 21.1% |
| Under 4.5 | 78.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.95% |
| 2 | 2-1 | 9.74% |
| 3 | 1-1 | 9.45% |
| 4 | 1-0 | 8.93% |
| 5 | 3-0 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 63.6% | 62.7% | 1.56 | -0.7% |
| Draw | 20.3% | 20.7% | 4.31 | -12.7% |
| Espanyol win | 16.1% | 16.6% | 5.40 | -13.0% |
| Over 2.5 | 61.0% | 60.0% | 1.66 | +1.2% |
| Under 2.5 | 39.0% | 40.0% | 2.42 | -5.5% |

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
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1798 |
| Dc lambda away | 0.9795 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.05 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.70 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.58 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.74 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.10606830978184556, "-10": 1.1881655903762396e-08, "-11": 1.0413585426796116e-09, "-12": 8.386386701733707e-11, "-13": 6.246095854154134e-12, "-14": 4.3262677603416994e-13, "-15": 2.7994477015081923e-14, "-16": 1.6893802305273807e-15, "-17": 8.647477494312401e-17, "-2": 0.04053951924028911, "-3": 0.01139294505230561, "-4": 0.0025362194343489072, "-5": 0.00046526604468063884, "-6": 7.24034024438747e-05, "-7": 9.769049438316523e-06, "-8": 1.1623792706651513e-06, "-9": 1.2362426230943214e-07, "0": 0.2026603175050355, "1": 0.2283014228382327, "10": 3.3886184099811114e-05, "11": 6.609584969360512e-06, "12": 1.1846143820252892e-06, "13": 1.9635364716261333e-07, "14": 3.026717820744776e-08, "15": 4.358721372947527e-09, "16": 5.853860490246994e-10, "17": 6.66856842417847e-11, "2": 0.19213151266716666, "3": 0.12016672402175088, "4": 0.05953375225081704, "5": 0.024305580574266385, "6": 0.008417668661148877, "7": 0.0025276292349117875, "8": 0.0006693251278567843, "9": 0.0001584240812719594} |
| Raw goal margin distribution | {"-1": 0.10290377520174668, "-10": 1.1527168205658926e-08, "-11": 1.010289742532152e-09, "-12": 8.136179917310525e-11, "-13": 6.05974437592528e-12, "-14": 4.1971941099882033e-13, "-15": 2.7159265341131284e-14, "-16": 1.6389777854480273e-15, "-17": 8.389481099181173e-17, "-2": 0.03933002782140693, "-3": 0.01105303798052008, "-4": 0.002460551648945112, "-5": 0.0004513848912016596, "-6": 7.024325610778522e-05, "-7": 9.477591086374919e-06, "-8": 1.1276998324354347e-06, "-9": 1.199359481105726e-07, "0": 0.1986417435217241, "1": 0.2314678573786861, "10": 3.4356169711130905e-05, "11": 6.701256838439813e-06, "12": 1.2010444324810874e-06, "13": 1.990769809149406e-07, "14": 3.0686969890419565e-08, "15": 4.419174810932857e-09, "16": 5.935050812325922e-10, "17": 6.761058366339967e-11, "2": 0.19479628737796623, "3": 0.12183338058843032, "4": 0.060359457702435525, "5": 0.024642687671100654, "6": 0.008534417810003898, "7": 0.0025626862766743165, "8": 0.0006786083560438503, "9": 0.00016062134958830525} |
| Unadjusted home-win probability | 64.5% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 15.6% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.2% |
| Raw p btts yes | 55.6% |
| P home draw | 83.9% |
| P draw away | 36.4% |
| P home away | 79.7% |
| Raw p home draw | 84.4% |
| Raw p draw away | 35.5% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.55 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | 0.0176 |
| Raw ev home | 0.0063 |
| Raw edge prob draw | -0.0080 |
| Raw ev draw | -0.1439 |
| Raw edge prob away | -0.0096 |
| Raw ev away | -0.1561 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **58.1%**. Expected goals are 1.23 for Levante and 1.94 for Atlético Madrid (3.16 combined). The most likely exact score is 1-2 at 10.5%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 61.8%; Under 3.5 goals: 60.7%; Double Chance 1X: 41.9%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 78.4%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 20.4% | 4.89 |
| Draw | 21.4% | 4.67 |
| Atlético Madrid win | 58.1% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.23 |
| Atlético Madrid expected goals | 1.94 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.8% |
| Under 2.5 | 38.2% |
| Over 3.5 | 39.3% |
| Under 3.5 | 60.7% |
| Over 4.5 | 21.6% |
| Under 4.5 | 78.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.54% |
| 2 | 1-1 | 9.77% |
| 3 | 0-1 | 8.63% |
| 4 | 0-2 | 8.59% |
| 5 | 1-3 | 6.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 20.4% | 17.1% | 4.56 | -6.8% |
| Draw | 21.4% | 20.3% | 4.63 | -0.9% |
| Atlético Madrid win | 58.1% | 62.6% | 1.61 | -6.4% |

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
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Levante |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2270 |
| Dc lambda away | 1.9358 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.62 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.84 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.62 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.62 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.2426923011020759, "-10": 1.1559058840591171e-05, "-11": 1.9987450918297317e-06, "-12": 3.176547637152257e-07, "-13": 4.6697487471245355e-08, "-14": 6.382428980891005e-09, "-15": 8.084312744667042e-10, "-16": 8.516704931416221e-11, "-2": 0.1775708023292367, "-3": 0.09724691922267288, "-4": 0.042380998930471585, "-5": 0.015262104595065105, "-6": 0.004670358160712371, "-7": 0.0012405723289276268, "-8": 0.000290834071956982, "-9": 6.09791233815781e-05, "0": 0.21413538434727247, "1": 0.12128136256940217, "10": 9.591362802326627e-08, "11": 1.0511985463962904e-08, "12": 1.0588933258311272e-09, "13": 9.866425696012556e-11, "14": 8.547159790912008e-12, "15": 6.861963999545154e-13, "16": 4.581908658865655e-14, "2": 0.056568338847398605, "3": 0.019635737492796065, "4": 0.005423904716674611, "5": 0.001238011802866627, "6": 0.00024012094485618943, "7": 4.042699339120619e-05, "8": 6.007089939692715e-06, "9": 7.983062404831726e-07} |
| Raw goal margin distribution | {"-1": 0.22404929870269036, "-10": 1.0671121478255384e-05, "-11": 1.845206601430446e-06, "-12": 2.932533364955447e-07, "-13": 4.311030581357284e-08, "-14": 5.892147096116207e-09, "-15": 7.463296498120269e-10, "-16": 7.86247342201012e-11, "-2": 0.16393026705534508, "-3": 0.08977665939090916, "-4": 0.039125398892228845, "-5": 0.014089708720563103, "-6": 0.004311593181350585, "-7": 0.0011452747327542674, "-8": 0.00026849294174108535, "-9": 5.629486294829375e-05, "0": 0.22523271738819092, "1": 0.14119482586735296, "10": 1.1166190517773549e-07, "11": 1.2237972312151802e-08, "12": 1.2327554340203948e-09, "13": 1.1486416614790977e-10, "14": 9.950537434370208e-12, "15": 7.988645505770876e-13, "16": 5.3342226828829224e-14, "2": 0.06585642331148191, "3": 0.022859773977933963, "4": 0.00631446799217603, "5": 0.0014412837819780667, "6": 0.0002795469499831251, "7": 4.7064793561711415e-05, "8": 6.9934077259321934e-06, "9": 9.29381961299632e-07} |
| Unadjusted home-win probability | 23.8% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 82.6% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.7% |
| P home draw | 41.9% |
| P draw away | 79.6% |
| P home away | 78.6% |
| Raw p home draw | 46.3% |
| Raw p draw away | 76.2% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.10 |
| Reference draw odds | 4.35 |
| Reference away odds | 1.54 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:53Z |
| Home probability edge | +3.4% |
| Draw probability edge | +1.1% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | 0.0671 |
| Raw ev home | 0.0853 |
| Raw edge prob draw | 0.0222 |
| Raw ev draw | 0.0428 |
| Raw edge prob away | -0.0893 |
| Raw ev away | -0.1358 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **40.8%**. Expected goals are 1.21 for Rayo Vallecano and 1.09 for Celta Vigo (2.30 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 40.7%; Under 3.5 goals: 79.8%; Double Chance 1X: 69.1%; Double Chance X2: 59.2%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 46.8%; BTTS No (at least one team does not score): 53.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 40.8% | 2.45 |
| Draw | 28.3% | 3.53 |
| Celta Vigo win | 30.9% | 3.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.21 |
| Celta Vigo expected goals | 1.09 |
| Expected total goals | 2.30 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 67.3% |
| Under 1.5 | 32.7% |
| Over 2.5 | 40.7% |
| Under 2.5 | 59.3% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.27% |
| 2 | 1-0 | 12.49% |
| 3 | 0-0 | 10.11% |
| 4 | 0-1 | 10.08% |
| 5 | 2-1 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 40.8% | 42.8% | 2.32 | -5.4% |
| Draw | 28.3% | 27.8% | 3.46 | -1.9% |
| Celta Vigo win | 30.9% | 29.3% | 3.03 | -6.4% |
| Over 2.5 | 40.7% | 46.4% | 2.11 | -14.2% |
| Under 2.5 | 59.3% | 53.6% | 1.84 | +9.2% |

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
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Vallecano |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2149 |
| Dc lambda away | 1.0877 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:55:16.518314+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.8% |
| P btts no | 53.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.89 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.46 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.82 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.1861120646542221, "-10": 6.854502263012164e-08, "-11": 6.71102617094299e-09, "-12": 6.03132771605705e-10, "-13": 4.991236318572348e-11, "-14": 3.5432933195227386e-12, "-2": 0.08563683296155765, "-3": 0.02813472819055461, "-4": 0.007194469882455602, "-5": 0.0015009047001425249, "-6": 0.0002639648665436409, "-7": 4.008616535818509e-05, "-8": 5.353224733260769e-06, "-9": 6.376964910254998e-07, "0": 0.28345889290770326, "1": 0.23021766028756918, "10": 2.2908505877447278e-07, "11": 2.505227063523617e-08, "12": 2.5148287145323545e-09, "13": 2.32456095075287e-10, "14": 1.843220246430548e-11, "2": 0.11813616443673912, "3": 0.0433513188147478, "4": 0.01238214001219476, "5": 0.002885275917038375, "6": 0.0005667841296915844, "7": 9.613983884759394e-05, "8": 1.4340413477529142e-05, "9": 1.9080842487962555e-06} |
| Raw goal margin distribution | {"-1": 0.1954041066515254, "-10": 7.19672791623273e-08, "-11": 7.046088474084171e-09, "-12": 6.332454623338557e-10, "-13": 5.240434443244207e-11, "-14": 3.720199800007709e-12, "-2": 0.08991243459906165, "-3": 0.02953941453592968, "-4": 0.007553669144579283, "-5": 0.0015758405702785395, "-6": 0.00027714387581578615, "-7": 4.208755270892528e-05, "-8": 5.620495902031468e-06, "-9": 6.695348492058302e-07, "0": 0.2886086060907611, "1": 0.21860000618661704, "10": 2.1752456003074621e-07, "11": 2.3788038280863095e-08, "12": 2.3879209434600384e-09, "13": 2.207254810864672e-10, "14": 1.7502043794976925e-11, "2": 0.11217456664478488, "3": 0.04116364726000812, "4": 0.011757290382885043, "5": 0.0027396739786462957, "6": 0.0005381820582412841, "7": 9.128825886169076e-05, "8": 1.3616741960589652e-05, "9": 1.8117950989095782e-06} |
| Unadjusted home-win probability | 38.7% |
| Unadjusted draw probability | 28.9% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 67.3% |
| Raw p under 3 5 | 79.9% |
| Raw p btts yes | 46.9% |
| P home draw | 69.1% |
| P draw away | 59.2% |
| P home away | 71.7% |
| Raw p home draw | 67.6% |
| Raw p draw away | 61.3% |
| Raw p home away | 71.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.26 |
| Reference draw odds | 3.42 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | -2.1% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | -0.0411 |
| Raw ev home | -0.1020 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | -0.0014 |
| Raw edge prob away | 0.0308 |
| Raw ev away | -0.0173 |

</details>


---
