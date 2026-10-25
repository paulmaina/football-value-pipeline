# Bundesliga — football model report

Fixtures in this report: **3**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,593 |
| Training data through | 2026-10-24 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 00f21cba46dbb1e9f6978e0767d92712f9e0dbcd3b9d8cd1b973ed7ec1f88ea1 |
| Training as of utc | 2026-10-25T10:19:57.059078+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 61, 'bbs_added_results': 7, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 61, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 33, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-25T10:19:57.059078+00:00', 'observations': 206, 'observations_sha256': '11d23036f1854ca7d6c47763ce21072bd8077289227da2c34579e74b829b4d38', 'eligible_training_matches': 39, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 80, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 12, 'retrospective_eligible_training_matches': 39, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '7fdec82063bf85734f51efeecfeb698b7d443615685d596d965671a49e6fd057', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 4848.895 |
| Base scoring parameter | 0.226 |
| Home-advantage parameter | 0.236 |
| Dixon-Coles low-score adjustment | -0.111 |
| Xi per day | 0 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1593, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-24'} |
| Training data health | {'training_end': '2026-10-24', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 3.00 |
| Additional event odds calls used before this league | 10.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261025T101957059078Z_82d0ecc2fd4d0c8fa43bf04a90896ddebf38361b0d9534719f30100086c32fcd.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **64.0%**. Expected goals are 2.40 for Borussia Dortmund and 1.21 for Eintracht Frankfurt (3.61 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 70.3%; Under 3.5 goals: 51.1%; Double Chance 1X: 83.4%; Double Chance X2: 36.0%; Double Chance 12 (either team wins): 80.7%; Under 4.5 goals: 70.2%; BTTS Yes (both teams score): 64.4%; BTTS No (at least one team does not score): 35.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 64.0% | 1.56 |
| Draw | 19.3% | 5.17 |
| Eintracht Frankfurt win | 16.6% | 6.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.40 |
| Eintracht Frankfurt expected goals | 1.21 |
| Expected total goals | 3.61 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 70.3% |
| Under 2.5 | 29.7% |
| Over 3.5 | 48.9% |
| Under 3.5 | 51.1% |
| Over 4.5 | 29.8% |
| Under 4.5 | 70.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.61% |
| 2 | 1-1 | 8.35% |
| 3 | 2-0 | 7.94% |
| 4 | 3-1 | 7.69% |
| 5 | 3-0 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 64.0% | 65.2% | 1.51 | -3.3% |
| Draw | 19.3% | 18.5% | 5.07 | -1.9% |
| Eintracht Frankfurt win | 16.6% | 16.3% | 5.72 | -4.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 3ed4d1e775910625c50518a384e9c547 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:47:46Z |
| Market best draw last update utc | 2026-10-24T14:47:46Z |
| Market best away last update utc | 2026-10-24T14:47:46Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4004 |
| Dc lambda away | 1.2100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:19:57.059078+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.4% |
| P btts no | 35.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.24 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.69 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.36 |
| Fair Over 3.5 odds | 2.05 |
| Fair Under 3.5 odds | 1.96 |
| Fair Over 4.5 odds | 3.36 |
| Fair Under 4.5 odds | 1.42 |
| Goal margin distribution | {"-1": 0.09905853683207201, "-10": 6.386618476267121e-08, "-11": 6.876867708724833e-09, "-12": 6.80953455824343e-10, "-13": 6.240027523949099e-11, "-14": 5.320582110265768e-12, "-15": 4.2411441638675107e-13, "-16": 3.172008239097603e-14, "-17": 2.213419614208928e-15, "-18": 1.2812106080482997e-16, "-2": 0.04653719485772788, "-3": 0.015466728748514725, "-4": 0.004129091273337393, "-5": 0.0009160569578067119, "-6": 0.00017332640525263355, "-7": 2.8537080247109933e-05, "-8": 4.153886345145772e-06, "-9": 5.414478391438823e-07, "0": 0.1934302429748721, "1": 0.21290908013796375, "10": 6.261697668562051e-05, "11": 1.3374883449513393e-05, "12": 2.6272111533629648e-06, "13": 4.775757547921218e-07, "14": 8.07780062606472e-08, "15": 1.2773068159094464e-08, "16": 1.895067640172838e-09, "17": 2.623205883365963e-10, "18": 3.0120859752001126e-11, "2": 0.19028107974637057, "3": 0.12545041119174496, "4": 0.06643643463946323, "5": 0.029238327534913584, "6": 0.010974203105349042, "7": 0.003584231189850089, "8": 0.001034949841490796, "9": 0.00026760827102737547} |
| Raw goal margin distribution | {"-1": 0.10099482671791615, "-10": 6.511457234801433e-08, "-11": 7.011289332711319e-09, "-12": 6.942640026122338e-10, "-13": 6.362000879991038e-11, "-14": 5.424583134875849e-12, "-15": 4.3240454948535023e-13, "-16": 3.2340112493135824e-14, "-17": 2.2566851635415146e-15, "-18": 1.3062543369518035e-16, "-2": 0.047446853960318246, "-3": 0.015769055750311785, "-4": 0.004209802314767816, "-5": 0.0009339630553424069, "-6": 0.00017671440366421248, "-7": 2.9094892442011163e-05, "-8": 4.235082054009179e-06, "-9": 5.520314799705558e-07, "0": 0.20220063148996284, "1": 0.20891153814791866, "10": 6.144129177153305e-05, "11": 1.3123759081465104e-05, "12": 2.5778831167405817e-06, "13": 4.6860887967354114e-07, "14": 7.926133317329078e-08, "15": 1.253324336498704e-08, "16": 1.8594861963910248e-09, "17": 2.573953048961279e-10, "18": 2.955531599239792e-11, "2": 0.18670839695752786, "3": 0.12309497719107922, "4": 0.06518903628065184, "5": 0.02868935403897921, "6": 0.010768153472836947, "7": 0.003516934319870798, "8": 0.0010155178123529636, "9": 0.0002625837070227679} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 20.2% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.4% |
| Raw p under 3 5 | 51.3% |
| Raw p btts yes | 64.7% |
| P home draw | 83.4% |
| P draw away | 36.0% |
| P home away | 80.7% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.2% |
| Raw p home away | 79.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.51 |
| Reference draw odds | 5.10 |
| Reference away odds | 5.75 |
| Market reference 1x2 last update utc | 2026-10-24T14:47:49Z |
| Market reference home last update utc | 2026-10-24T14:47:49Z |
| Market reference draw last update utc | 2026-10-24T14:47:49Z |
| Market reference away last update utc | 2026-10-24T14:47:49Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-24T14:47:46Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:47:46Z |
| Home probability edge | -1.2% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.0240 |
| Raw ev home | -0.0514 |
| Raw edge prob draw | 0.0175 |
| Raw ev draw | 0.0252 |
| Raw edge prob away | 0.0065 |
| Raw ev away | -0.0301 |
| Count model | {"corners": {"alpha": 0.011997044198649347, "mu": 9.679474550411486, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,637.3721 |
| Elo away rating | 1,478.3501 |
| Elo rating diff | 219.0220 |
| Elo home expectancy | 0.7792 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **67.0%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.69 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 72.1%; Under 3.5 goals: 49.1%; Double Chance 1X: 33.0%; Double Chance X2: 84.9%; Double Chance 12 (either team wins): 82.2%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 65.1%; BTTS No (at least one team does not score): 34.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 15.1% | 6.62 |
| Draw | 17.8% | 5.60 |
| Bayern Munich win | 67.0% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.24 |
| Bayern Munich expected goals | 2.45 |
| Expected total goals | 3.69 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 50.9% |
| Under 3.5 | 49.1% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.88% |
| 2 | 1-3 | 8.06% |
| 3 | 0-2 | 7.97% |
| 4 | 1-1 | 7.57% |
| 5 | 0-3 | 6.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 15.1% | 13.2% | 6.75 | +2.0% |
| Draw | 17.8% | 15.8% | 6.03 | +7.6% |
| Bayern Munich win | 67.0% | 71.0% | 1.38 | -7.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | f2bd909f25eea6b4ce42d2f52275e5c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:47:46Z |
| Market best draw last update utc | 2026-10-24T14:47:46Z |
| Market best away last update utc | 2026-10-24T14:47:46Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Freiburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2397 |
| Dc lambda away | 2.4477 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:19:57.059078+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 65.1% |
| P btts no | 34.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.34 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.41 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.16 |
| Fair Under 4.5 odds | 1.46 |
| Goal margin distribution | {"-1": 0.2197345279901418, "-10": 7.435021990750536e-05, "-11": 1.617917594634122e-05, "-12": 3.238148054643673e-06, "-13": 5.998275922018863e-07, "-14": 1.0339458384540094e-07, "-15": 1.6662865934335983e-08, "-16": 2.5195534231975535e-09, "-17": 3.551809671618659e-10, "-18": 4.133087293700975e-11, "-2": 0.19795747838279779, "-3": 0.13216130333278509, "-4": 0.07102761458575067, "-5": 0.031764178783141965, "-6": 0.012125401209573679, "-7": 0.004030057495491506, "-8": 0.0011846937960902693, "-9": 0.00031195280847045703, "0": 0.17847768840262662, "1": 0.0893346347121471, "10": 6.902580490881809e-08, "11": 7.607511532842477e-09, "12": 7.711518812546097e-10, "13": 7.234802158190564e-11, "14": 6.316187425680826e-12, "15": 5.155418414981133e-13, "16": 3.948160406560273e-14, "17": 2.818888529034162e-15, "18": 1.6613448673318098e-16, "2": 0.04244681822636337, "3": 0.014352730841043724, "4": 0.003906739524615193, "5": 0.0008848748625613947, "6": 0.00017107925207968005, "7": 2.879847341132508e-05, "8": 4.287669856233708e-06, "9": 5.718223459345106e-07} |
| Raw goal margin distribution | {"-1": 0.20675320134851125, "-10": 6.99578083037191e-05, "-11": 1.5223353619859643e-05, "-12": 3.046846951463493e-06, "-13": 5.643913866393959e-07, "-14": 9.728630910974888e-08, "-15": 1.5678468500497005e-08, "-16": 2.3707049637554697e-09, "-17": 3.3419782812681496e-10, "-18": 3.888915580276345e-11, "-2": 0.18626268143146968, "-3": 0.12435356795483175, "-4": 0.06683149359399265, "-5": 0.029887636284069544, "-6": 0.011409065023349178, "-7": 0.003791972506245419, "-8": 0.0011147052636642182, "-9": 0.00029352347312398515, "0": 0.19909646598780711, "1": 0.10055752454195015, "10": 7.769734653879475e-08, "11": 8.563224444045977e-09, "12": 8.680297901782028e-10, "13": 8.143692509882498e-11, "14": 7.1096744741386914e-12, "15": 5.803080915469355e-13, "16": 4.4441580609525543e-14, "17": 3.1730185426149334e-15, "18": 1.8700555255826841e-16, "2": 0.04777930731209282, "3": 0.01615582901797003, "4": 0.004397533575766461, "5": 0.0009960395091476568, "6": 0.00019257151657980324, "7": 3.241635459932378e-05, "8": 4.826319245444625e-06, "9": 6.436589769491323e-07} |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 33.0% |
| P draw away | 84.9% |
| P home away | 82.2% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:00Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.41, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:00Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.24, "price": 4.41, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 7.00 |
| Reference draw odds | 5.90 |
| Reference away odds | 1.39 |
| Market reference 1x2 last update utc | 2026-10-24T14:47:49Z |
| Market reference home last update utc | 2026-10-24T14:47:49Z |
| Market reference draw last update utc | 2026-10-24T14:47:49Z |
| Market reference away last update utc | 2026-10-24T14:47:49Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.24 |
| Reference Under 2.5 odds | 4.12 |
| Market reference over 2 5 last update utc | 2026-10-24T14:47:46Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:47:46Z |
| Home probability edge | +1.9% |
| Draw probability edge | +2.1% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | 0.0380 |
| Raw ev home | 0.1483 |
| Raw edge prob draw | 0.0412 |
| Raw ev draw | 0.2006 |
| Raw edge prob away | -0.0792 |
| Raw ev away | -0.1295 |
| Count model | {"corners": {"alpha": 0.011997044198649347, "mu": 9.347747937525346, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,530.2364 |
| Elo away rating | 1,716.2990 |
| Elo rating diff | -126.0626 |
| Elo home expectancy | 0.3261 |
| Market p home draw | 36.0% |
| Market home draw odds | 2.67 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:20:00Z |
| Market reference home draw last update utc | 2026-10-25T10:20:03Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.1% |
| Market draw away odds | 1.18 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:20:00Z |
| Market reference draw away last update utc | 2026-10-25T10:20:03Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.0% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:20:00Z |
| Market reference home away last update utc | 2026-10-25T10:20:03Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home draw odds | 2.68 |
| Market reference dc home away odds | 1.19 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:00Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.55, "price": 1.49, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:00Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.49, "price": 2.55, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:00Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.99, "price": 1.83, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:00Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.83, "price": 1.99, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:00Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.62, "price": 2.26, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:00Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.26, "price": 1.62, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 90.4% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market reference over 1 5 last update utc | 2026-10-25T10:19:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 47.5% |
| Market under 3 5 odds | 1.99 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:19:53Z |
| Market reference under 3 5 odds | 2.00 |
| Market reference under 3 5 opposite odds | 1.82 |
| Market reference under 3 5 last update utc | 2026-10-25T10:19:54Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.0% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:20:00Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.85 |
| Market reference btts yes last update utc | 2026-10-25T10:20:00Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.6%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.5%; Double Chance 1X: 53.4%; Double Chance X2: 69.3%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 70.0%; BTTS No (at least one team does not score): 30.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.7% | 3.25 |
| Draw | 22.6% | 4.42 |
| Bayer Leverkusen win | 46.6% | 2.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.50 |
| Bayer Leverkusen expected goals | 2.16 |
| Expected total goals | 3.66 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.31% |
| 2 | 1-2 | 8.10% |
| 3 | 2-1 | 7.48% |
| 4 | 2-2 | 6.80% |
| 5 | 1-3 | 5.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.7% | 35.7% | 2.83 | -13.0% |
| Draw | 22.6% | 22.8% | 3.99 | -9.7% |
| Bayer Leverkusen win | 46.6% | 41.5% | 2.33 | +8.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:30:00+00:00 |
| Fixture id | 2fd479cbb110c8f057e363bb06195f2b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:47:47Z |
| Market best draw last update utc | 2026-10-24T14:47:47Z |
| Market best away last update utc | 2026-10-24T14:47:47Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5029 |
| Dc lambda away | 2.1596 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:19:57.059078+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 70.0% |
| P btts no | 30.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.48 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.95 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.18051972078082498, "-10": 1.882069601975089e-05, "-11": 3.6080368840738833e-06, "-12": 6.363089457963255e-07, "-13": 1.0387951288691709e-07, "-14": 1.5782468419075638e-08, "-15": 2.2401506728770134e-09, "-16": 2.946184053507137e-10, "-17": 3.1426450330875606e-11, "-2": 0.14182459440452866, "-3": 0.08261846287429489, "-4": 0.03887423117123427, "-5": 0.015252748020173405, "-6": 0.005115401114220583, "-7": 0.0014951181048033753, "-8": 0.0003867584292170569, "-9": 8.966090805834964e-05, "0": 0.22637902554000638, "1": 0.16313809531896453, "10": 6.6476365492979e-07, "11": 8.869033122001349e-08, "12": 1.0885466830242144e-08, "13": 1.2367520981978085e-09, "14": 1.3076797601439263e-10, "15": 1.2917468898007114e-11, "16": 1.1823166092360445e-12, "17": 8.776936719773985e-14, "2": 0.09103184905566364, "3": 0.03690563194401244, "4": 0.0120851228667755, "5": 0.0032999782268995576, "6": 0.0007702228420520534, "7": 0.0001566700285051474, "8": 2.8204858886549548e-05, "9": 4.550519691483028e-06} |
| Raw goal margin distribution | {"-1": 0.20036250501511113, "-10": 2.0889472819557876e-05, "-11": 4.004633428154229e-06, "-12": 7.062522243653876e-07, "-13": 1.152979814711915e-07, "-14": 1.7517282289657572e-08, "-15": 2.486388736297014e-09, "-16": 3.270029527205911e-10, "-17": 3.4880855591795515e-11, "-2": 0.15741399823094504, "-3": 0.091699910183719, "-4": 0.04314729883424662, "-5": 0.0169293348586369, "-6": 0.005677687606478928, "-7": 0.0016594619550490128, "-8": 0.0004292710368620863, "-9": 9.951646314760271e-05, "0": 0.22508263818780577, "1": 0.13663212292765722, "10": 5.567557304173524e-07, "11": 7.428030966068799e-08, "12": 9.11684324355161e-09, "13": 1.0358099644452407e-09, "14": 1.0952136065378229e-10, "15": 1.081869440081372e-11, "16": 9.902189183752906e-13, "17": 7.350897989091707e-14, "2": 0.07624138780207697, "3": 0.03090936442918614, "4": 0.010121584354044868, "5": 0.002763812032221994, "6": 0.0006450803647743216, "7": 0.00013121495964472273, "8": 2.3622255359850814e-05, "9": 3.8111709264216033e-06} |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 89.0% |
| Raw p under 3 5 | 50.2% |
| Raw p btts yes | 69.7% |
| P home draw | 53.4% |
| P draw away | 69.3% |
| P home away | 77.4% |
| Raw p home draw | 48.3% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.34, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.9, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.65, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.16, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:18:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.08, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:19:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:01Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:01Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.69 |
| Reference draw odds | 4.15 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-24T14:47:49Z |
| Market reference home last update utc | 2026-10-24T14:47:49Z |
| Market reference draw last update utc | 2026-10-24T14:47:49Z |
| Market reference away last update utc | 2026-10-24T14:47:49Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-24T14:47:46Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:47:46Z |
| Home probability edge | -5.0% |
| Draw probability edge | -0.1% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | -0.0999 |
| Raw ev home | -0.2714 |
| Raw edge prob draw | -0.0026 |
| Raw ev draw | -0.1019 |
| Raw edge prob away | 0.1025 |
| Raw ev away | 0.2056 |
| Count model | {"corners": {"alpha": 0.011997044198649347, "mu": 10.130502221134883, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,478.1782 |
| Elo away rating | 1,602.6506 |
| Elo rating diff | -64.4724 |
| Elo home expectancy | 0.4083 |
| Market p home draw | 53.0% |
| Market home draw odds | 1.85 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:20:01Z |
| Market reference home draw last update utc | 2026-10-25T10:20:03Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.3% |
| Market draw away odds | 1.37 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:20:01Z |
| Market reference draw away last update utc | 2026-10-25T10:20:03Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.7% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:20:01Z |
| Market reference home away last update utc | 2026-10-25T10:20:03Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home draw odds | 1.82 |
| Market reference dc home away odds | 1.24 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.76, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.05, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.69, "price": 2.15, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:20:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.15, "price": 1.69, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 89.6% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.10 |
| Market reference over 1 5 last update utc | 2026-10-25T10:19:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 49.3% |
| Market under 3 5 odds | 2.12 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:19:53Z |
| Market reference under 3 5 odds | 1.93 |
| Market reference under 3 5 opposite odds | 1.88 |
| Market reference under 3 5 last update utc | 2026-10-25T10:19:54Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 74.5% |
| Market btts yes odds | 1.32 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:20:01Z |
| Market reference btts yes odds | 1.32 |
| Market reference btts yes opposite odds | 3.63 |
| Market reference btts yes last update utc | 2026-10-25T10:20:01Z |
| Market btts yes bookmakers | 1 |

</details>


---
