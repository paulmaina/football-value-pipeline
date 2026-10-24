# La Liga — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,990 |
| Training data through | 2026-10-23 |
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
| Training sha256 | f50d45c7f417ced1f4ddb0f2dce02d3f0ade03319a7628ccb532ba80ff33fe9a |
| Training as of utc | 2026-10-24T14:47:10.281252+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 90, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 90, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 53, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-24T14:47:10.281252+00:00', 'observations': 293, 'observations_sha256': '144acedd8910555c44175b462d9567ae5a6bca5687de967fed943cb0d0781656', 'eligible_training_matches': 98, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 121, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 11, 'retrospective_eligible_training_matches': 98, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '01acd0de412b2a43d29d76d8af8a65acc27b50d97f8fc315f3135669e080afbf', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5527.200 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.279 |
| Dixon-Coles low-score adjustment | -0.021 |
| Xi per day | 0 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1990, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-23'} |
| Training data health | {'training_end': '2026-10-23', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 6.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261024T144710281252Z_428f24d4218c3dc4396c2b6c019481e77c780f70570dde6dc15ea11df3cbbeff.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **71.5%**. Expected goals are 2.27 for Atlético Madrid and 0.89 for Deportivo La Coruña (3.16 combined). The most likely exact score is 2-0 at 11.4%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 62.0%; Under 3.5 goals: 60.6%; Double Chance 1X: 88.6%; Double Chance X2: 28.5%; Double Chance 12 (either team wins): 83.0%; Under 4.5 goals: 78.3%; BTTS Yes (both teams score): 52.5%; BTTS No (at least one team does not score): 47.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 71.5% | 1.40 |
| Draw | 17.0% | 5.87 |
| Deportivo La Coruña win | 11.4% | 8.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.27 |
| Deportivo La Coruña expected goals | 0.89 |
| Expected total goals | 3.16 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 39.4% |
| Under 3.5 | 60.6% |
| Over 4.5 | 21.7% |
| Under 4.5 | 78.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.44% |
| 2 | 2-1 | 10.21% |
| 3 | 1-0 | 9.90% |
| 4 | 3-0 | 8.64% |
| 5 | 1-1 | 8.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 71.5% | 74.8% | 1.28 | -8.4% |
| Draw | 17.0% | 15.4% | 6.01 | +2.3% |
| Deportivo La Coruña win | 11.4% | 9.8% | 11.15 | +27.7% |

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
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2675 |
| Dc lambda away | 0.8926 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:10.281252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.5% |
| P btts no | 47.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.76 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.86 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.61 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.07813068234045527, "-10": 3.924285087139948e-09, "-11": 3.136978110065033e-10, "-12": 2.3038892085557154e-11, "-13": 1.5646943012079177e-12, "-14": 9.881794242720198e-14, "-15": 5.830233260100141e-15, "-16": 3.2096911433778655e-16, "-17": 1.506014637767519e-17, "-2": 0.027528438971471673, "-3": 0.007097627976242091, "-4": 0.0014463688054201873, "-5": 0.00024257493417655972, "-6": 3.448277421557095e-05, "-7": 4.247751453432274e-06, "-8": 4.61269508029037e-07, "-9": 4.476027936196652e-08, "0": 0.17026881239573552, "1": 0.24191043359817732, "10": 5.287908141153918e-05, "11": 1.073795468759995e-05, "12": 2.0033572216586646e-06, "13": 3.456312745054628e-07, "14": 5.545057646018257e-08, "15": 8.310801621308237e-09, "16": 1.1622698059783704e-09, "17": 1.3853503902320586e-10, "2": 0.213900167388449, "3": 0.1400972137115554, "4": 0.07252404842653591, "5": 0.030898375122875302, "6": 0.011157801844275991, "7": 0.0034915821901642745, "8": 0.0009631737673073426, "9": 0.00023742662223209143} |
| Raw goal margin distribution | {"-1": 0.08971359149441813, "-10": 4.506062134222733e-09, "-11": 3.6020365401005196e-10, "-12": 2.6454418304464708e-11, "-13": 1.7966609422470995e-12, "-14": 1.1346774728783547e-13, "-15": 6.69456798975072e-15, "-16": 3.6855293136375765e-16, "-17": 1.729281992041822e-17, "-2": 0.03160954255594484, "-3": 0.008149854548374167, "-4": 0.001660793637950201, "-5": 0.00027853677837692413, "-6": 3.959486115953408e-05, "-7": 4.8774825362778646e-06, "-8": 5.296529221621939e-07, "-9": 5.139601111324557e-08, "0": 0.18646134091639754, "1": 0.23069338393298996, "10": 5.042715210191724e-05, "11": 1.0240050693787884e-05, "12": 1.910464339288061e-06, "13": 3.2960483399893396e-07, "14": 5.28794105089434e-08, "15": 7.92544133255533e-09, "16": 1.1083769748834438e-09, "17": 1.3211136233436511e-10, "2": 0.20398191473063476, "3": 0.1336011011595553, "4": 0.06916120937482238, "5": 0.02946566053023983, "6": 0.010640430122932814, "7": 0.0033296823900828463, "8": 0.0009185127420535171, "9": 0.00022641748065104343} |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 13.1% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 53.1% |
| P home draw | 88.6% |
| P draw away | 28.5% |
| P home away | 83.0% |
| Raw p home draw | 86.9% |
| Raw p draw away | 31.8% |
| Raw p home away | 81.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:17Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 9.14, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:17Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.09, "price": 9.14, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.32 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.30 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:14Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:14Z |
| Home probability edge | -3.3% |
| Draw probability edge | +1.6% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.0663 |
| Raw ev home | -0.1269 |
| Raw edge prob draw | 0.0324 |
| Raw ev draw | 0.1206 |
| Raw edge prob away | 0.0339 |
| Raw ev away | 0.4657 |
| Market p home draw | 89.3% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:43:17Z |
| Market reference home draw last update utc | 2026-10-24T14:43:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 26.8% |
| Market draw away odds | 3.92 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:43:17Z |
| Market reference draw away last update utc | 2026-10-24T14:43:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.9% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:43:17Z |
| Market reference home away last update utc | 2026-10-24T14:43:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.08 |
| Market reference dc draw away odds | 3.60 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 83.6% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-24T14:43:18Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.9% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:43:14Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.27 |
| Market reference under 3 5 last update utc | 2026-10-24T14:43:18Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.6% |
| Market btts yes odds | 2.10 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:43:17Z |
| Market reference btts yes odds | 2.10 |
| Market reference btts yes opposite odds | 1.78 |
| Market reference btts yes last update utc | 2026-10-24T14:43:17Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,646.3999 |
| Elo away rating | 1,445.4329 |
| Elo rating diff | 260.9670 |
| Elo home expectancy | 0.8179 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.2%**. Expected goals are 1.27 for Valencia and 1.51 for Villarreal (2.78 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.5%; Under 3.5 goals: 69.7%; Double Chance 1X: 55.8%; Double Chance X2: 70.1%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.9% | 3.34 |
| Draw | 25.9% | 3.86 |
| Villarreal win | 44.2% | 2.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.27 |
| Villarreal expected goals | 1.51 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.25% |
| 2 | 0-1 | 9.49% |
| 3 | 1-2 | 9.34% |
| 4 | 0-2 | 7.34% |
| 5 | 1-0 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.9% | 28.0% | 3.55 | +6.2% |
| Draw | 25.9% | 26.1% | 3.70 | -4.2% |
| Villarreal win | 44.2% | 46.0% | 2.10 | -7.2% |

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
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2719 |
| Dc lambda away | 1.5053 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:10.281252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.34 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.72 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.22331136516054592, "-10": 1.267906428190566e-06, "-11": 1.7105752649519576e-07, "-12": 2.1200206463625357e-08, "-13": 2.4287838045203025e-09, "-14": 2.570805961799239e-10, "-15": 2.2878960537854402e-11, "-2": 0.1330216011201575, "-3": 0.05822554125795065, "-4": 0.020098763036311938, "-5": 0.00570244736265621, "-6": 0.0013702161579212907, "-7": 0.0002851564384664715, "-8": 5.229418883514996e-05, "-9": 8.567398239676671e-06, "0": 0.25882146328580796, "1": 0.16979387014669473, "10": 2.11992262889349e-07, "11": 2.416487084017949e-08, "12": 2.530415645813285e-09, "13": 2.449345867862679e-10, "14": 2.1904837659253895e-11, "15": 1.6470869001069703e-12, "2": 0.08564048359375134, "3": 0.03167232591952981, "4": 0.00923730400439607, "5": 0.00221435208434008, "6": 0.00044955616532489883, "7": 7.904739070298328e-05, "8": 1.2248059038126217e-05, "9": 1.6954003887423298e-06} |
| Raw goal margin distribution | {"-1": 0.21442404722220332, "-10": 1.2174464458457501e-06, "-11": 1.642498003294616e-07, "-12": 2.0356483283368552e-08, "-13": 2.3321233687258643e-09, "-14": 2.4684933458521257e-10, "-15": 2.1968426511731178e-11, "-2": 0.12772762398212734, "-3": 0.05590828840823802, "-4": 0.01929887496459336, "-5": 0.005475502071707162, "-6": 0.001315684465676492, "-7": 0.0002738078179921173, "-8": 5.0212991211502023e-05, "-9": 8.226433990026132e-06, "0": 0.25706524345252363, "1": 0.18077846587475674, "10": 2.2570682928273342e-07, "11": 2.5728186033895704e-08, "12": 2.694117626745857e-09, "13": 2.6078031439317494e-10, "14": 2.332194291734036e-11, "15": 1.7536430655976954e-12, "2": 0.09118088437159057, "3": 0.03372132624971179, "4": 0.009834899488955289, "5": 0.002357606740265246, "6": 0.00047863962239484735, "7": 8.416125982841319e-05, "8": 1.304043144162356e-05, "9": 1.8050821331506753e-06} |
| Unadjusted home-win probability | 31.8% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 42.4% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.2% |
| P home draw | 55.8% |
| P draw away | 70.1% |
| P home away | 74.1% |
| Raw p home draw | 57.6% |
| Raw p draw away | 68.2% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.15, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.19, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.32, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 3.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 6.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:15Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.53, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:18Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.62, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:18Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.53, "price": 2.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.40 |
| Reference draw odds | 3.64 |
| Reference away odds | 2.11 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | +1.9% |
| Draw probability edge | -0.2% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | 0.0387 |
| Raw ev home | 0.1305 |
| Raw edge prob draw | -0.0035 |
| Raw ev draw | -0.0489 |
| Raw edge prob away | -0.0352 |
| Raw ev away | -0.1086 |
| Market p home draw | 54.7% |
| Market home draw odds | 1.81 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:43:18Z |
| Market reference home draw last update utc | 2026-10-24T14:43:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.8% |
| Market draw away odds | 1.33 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:43:18Z |
| Market reference draw away last update utc | 2026-10-24T14:43:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.5% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:43:18Z |
| Market reference home away last update utc | 2026-10-24T14:43:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.76 |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 80.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market reference over 1 5 last update utc | 2026-10-24T14:43:18Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.8% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:43:14Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market reference under 3 5 last update utc | 2026-10-24T14:43:18Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:43:18Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-24T14:43:18Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,465.9892 |
| Elo away rating | 1,546.8125 |
| Elo rating diff | -20.8233 |
| Elo home expectancy | 0.4701 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **56.8%**. Expected goals are 1.26 for Athletic Bilbao and 0.63 for Getafe (1.89 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 86.4%; Over 2.5 goals: 30.6%; Under 3.5 goals: 87.2%; Double Chance 1X: 83.5%; Double Chance X2: 43.2%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 95.4%; BTTS Yes (both teams score): 32.9%; BTTS No (at least one team does not score): 67.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 56.8% | 1.76 |
| Draw | 26.8% | 3.73 |
| Getafe win | 16.5% | 6.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.26 |
| Getafe expected goals | 0.63 |
| Expected total goals | 1.89 |
| Over 0.5 | 86.4% |
| Under 0.5 | 13.6% |
| Over 1.5 | 57.4% |
| Under 1.5 | 42.6% |
| Over 2.5 | 30.6% |
| Under 2.5 | 69.4% |
| Over 3.5 | 12.8% |
| Under 3.5 | 87.2% |
| Over 4.5 | 4.6% |
| Under 4.5 | 95.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.66% |
| 2 | 0-0 | 13.60% |
| 3 | 2-0 | 13.23% |
| 4 | 1-1 | 10.86% |
| 5 | 2-1 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 56.8% | 61.9% | 1.60 | -9.2% |
| Draw | 26.8% | 23.4% | 4.12 | +10.3% |
| Getafe win | 16.5% | 14.7% | 5.90 | -2.8% |

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
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2639 |
| Dc lambda away | 0.6294 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:10.281252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 32.9% |
| P btts no | 67.1% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.35 |
| Fair Over 1.5 odds | 1.74 |
| Fair Under 1.5 odds | 2.35 |
| Fair Over 2.5 odds | 3.26 |
| Fair Under 2.5 odds | 1.44 |
| Fair Over 3.5 odds | 7.83 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 21.80 |
| Fair Under 4.5 odds | 1.05 |
| Goal margin distribution | {"-1": 0.12191406606155393, "-10": 3.9183334247237634e-10, "-11": 2.228465462104238e-11, "-12": 1.1628036248906105e-12, "-13": 5.596975060705572e-14, "-14": 2.3807798539988413e-15, "-2": 0.03475027770599767, "-3": 0.006852759239306879, "-4": 0.00103796485478143, "-5": 0.0001273347098204047, "-6": 1.311151187712414e-05, "-7": 1.1624886705728214e-06, "-8": 9.046110147864675e-08, "-9": 6.270735802827103e-09, "0": 0.2677535640839769, "1": 0.301720204780621, "10": 5.104233596608466e-07, "11": 5.829754731045751e-08, "12": 6.108941636951683e-09, "13": 5.905112744995203e-10, "14": 5.0443972952387634e-11, "2": 0.1711061611548209, "3": 0.0677622885588056, "4": 0.020612015626972815, "5": 0.005078083530581766, "6": 0.0010500767270008884, "7": 0.00018697012253536717, "8": 2.9218679068455686e-05, "9": 4.067545628130928e-06} |
| Raw goal margin distribution | {"-1": 0.1352729849617656, "-10": 4.3476907592453155e-10, "-11": 2.4726529487650683e-11, "-12": 1.2902195976623073e-12, "-13": 6.210272101300723e-14, "-14": 2.6416574214221952e-15, "-2": 0.038558092149655644, "-3": 0.007603660738026113, "-4": 0.0011517014297660925, "-5": 0.00014128760399107333, "-6": 1.4548225699278408e-05, "-7": 1.2898701317469269e-06, "-8": 1.0037351402722756e-07, "-9": 6.957861199763052e-09, "0": 0.30145292215815045, "1": 0.2742109094066628, "10": 4.6388558478134287e-07, "11": 5.298227699335451e-08, "12": 5.551959780084109e-09, "13": 5.366714957426714e-10, "14": 4.584475112436269e-11, "2": 0.1555055820324035, "3": 0.061584071847946155, "4": 0.018732718128327292, "5": 0.004615090010217504, "6": 0.0009543361355831208, "7": 0.00016992314906313872, "8": 2.655467029411635e-05, "9": 3.696687752660956e-06} |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 18.3% |
| Raw p over 1 5 | 56.7% |
| Raw p under 3 5 | 87.6% |
| Raw p btts yes | 33.8% |
| P home draw | 83.5% |
| P draw away | 43.2% |
| P home away | 73.2% |
| Raw p home draw | 81.7% |
| Raw p draw away | 48.4% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.95, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:20Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.52, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:20Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.23, "price": 4.52, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.58 |
| Reference draw odds | 4.00 |
| Reference away odds | 6.25 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.31 |
| Reference Under 2.5 odds | 1.63 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | -5.2% |
| Draw probability edge | +3.4% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.1035 |
| Raw ev home | -0.1747 |
| Raw edge prob draw | 0.0674 |
| Raw ev draw | 0.2420 |
| Raw edge prob away | 0.0361 |
| Raw ev away | 0.0782 |
| Market p home draw | 85.1% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:43:20Z |
| Market reference home draw last update utc | 2026-10-24T14:43:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.2% |
| Market draw away odds | 2.45 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:43:20Z |
| Market reference draw away last update utc | 2026-10-24T14:43:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.7% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:43:20Z |
| Market reference home away last update utc | 2026-10-24T14:43:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.13 |
| Market reference dc draw away odds | 2.45 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 67.4% |
| Market over 1 5 odds | 1.45 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:43:14Z |
| Market reference over 1 5 odds | 1.41 |
| Market reference over 1 5 opposite odds | 2.65 |
| Market reference over 1 5 last update utc | 2026-10-24T14:43:18Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 81.1% |
| Market reference under 3 5 odds | 1.19 |
| Market reference under 3 5 opposite odds | 4.00 |
| Market reference under 3 5 last update utc | 2026-10-24T14:43:18Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 38.1% |
| Market btts yes odds | 2.48 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:43:20Z |
| Market reference btts yes odds | 2.48 |
| Market reference btts yes opposite odds | 1.57 |
| Market reference btts yes last update utc | 2026-10-24T14:43:20Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,491.3653 |
| Elo away rating | 1,456.5803 |
| Elo rating diff | 94.7851 |
| Elo home expectancy | 0.6331 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **54.4%**. Expected goals are 1.77 for Barcelona and 1.33 for Real Madrid (3.11 combined). The most likely exact score is 2-1 at 10.7%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.9%; Double Chance 1X: 74.6%; Double Chance X2: 45.6%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 54.4% | 1.84 |
| Draw | 20.2% | 4.95 |
| Real Madrid win | 25.4% | 3.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.77 |
| Real Madrid expected goals | 1.33 |
| Expected total goals | 3.11 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 38.1% |
| Under 3.5 | 61.9% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.71% |
| 2 | 1-1 | 9.21% |
| 3 | 1-0 | 8.80% |
| 4 | 2-0 | 8.04% |
| 5 | 3-1 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 54.4% | 61.1% | 1.64 | -10.8% |
| Draw | 20.2% | 16.7% | 6.01 | +21.3% |
| Real Madrid win | 25.4% | 22.2% | 3.83 | -2.7% |

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
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7748 |
| Dc lambda away | 1.3325 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:10.281252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.96 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.59 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.77 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.14339489687345203, "-10": 2.3853510310602644e-07, "-11": 2.839366139675636e-08, "-12": 3.1063386446651014e-09, "-13": 3.143494820284515e-10, "-14": 2.9575377307961445e-11, "-15": 2.5789222795889813e-12, "-16": 1.8711543844959345e-13, "-2": 0.07256505176906781, "-3": 0.027370933701019964, "-4": 0.008214102287058975, "-5": 0.0020367098641173617, "-6": 0.0004291008674079903, "-7": 7.847019968425595e-05, "-8": 1.2664461661998946e-05, "-9": 1.8279772141122417e-06, "0": 0.20183676968196984, "1": 0.24673324013108444, "10": 5.398235060721903e-06, "11": 8.558952642342602e-07, "12": 1.2472334685757992e-07, "13": 1.681169251022962e-08, "14": 2.1068262222904106e-09, "15": 2.4470137382545054e-10, "16": 2.3648712816795273e-11, "2": 0.1657406903605323, "3": 0.08327046291993487, "4": 0.03328596906591206, "5": 0.01099334854699603, "6": 0.0030850340058560526, "7": 0.0007514585897752252, "8": 0.00016154248572641374, "9": 3.105778919358543e-05} |
| Raw goal margin distribution | {"-1": 0.1617658981185477, "-10": 2.690949680085211e-07, "-11": 3.2031308204599e-08, "-12": 3.5043064409611815e-09, "-13": 3.5462228707001665e-10, "-14": 3.336441935335745e-11, "-15": 2.9093202605655664e-12, "-16": 2.1108768591226114e-13, "-2": 0.08186170517491703, "-3": 0.030877554006654855, "-4": 0.009266449941216264, "-5": 0.0022976424374893363, "-6": 0.00048407501740428124, "-7": 8.852338963406695e-05, "-8": 1.428696599118978e-05, "-9": 2.062168056385373e-06, "0": 0.23658428960977507, "1": 0.21621149004349413, "10": 4.7304548242613184e-06, "11": 7.5001807743028e-07, "12": 1.0929464004510332e-07, "13": 1.4732028347127677e-08, "14": 1.8462045752007585e-09, "15": 2.1443097258554288e-10, "16": 2.072328573569367e-11, "2": 0.14523799713670368, "3": 0.07296962036799529, "4": 0.029168380253341546, "5": 0.009633433535954458, "6": 0.0027034046928035007, "7": 0.0006585005786612502, "8": 0.00014155912484949983, "9": 2.7215833891835022e-05} |
| Unadjusted home-win probability | 47.7% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 28.7% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 61.4% |
| P home draw | 74.6% |
| P draw away | 45.6% |
| P home away | 79.8% |
| Raw p home draw | 71.3% |
| Raw p draw away | 52.3% |
| Raw p home away | 76.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.43, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.66, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.32, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.61 |
| Reference draw odds | 5.65 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.20 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:50Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:50Z |
| Home probability edge | -6.7% |
| Draw probability edge | +3.5% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -23.8% |
| Under 2.5 probability edge | +23.8% |
| Raw edge prob home | -0.1346 |
| Raw ev home | -0.2181 |
| Raw edge prob draw | 0.0695 |
| Raw ev draw | 0.4219 |
| Raw edge prob away | 0.0651 |
| Raw ev away | 0.0979 |
| Market p home draw | 77.2% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:46:49Z |
| Market reference home draw last update utc | 2026-10-24T14:47:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.9% |
| Market draw away odds | 2.35 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:46:49Z |
| Market reference draw away last update utc | 2026-10-24T14:47:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.9% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:46:49Z |
| Market reference home away last update utc | 2026-10-24T14:47:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.30 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 95.3% |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 12.00 |
| Market reference over 1 5 last update utc | 2026-10-24T14:47:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 34.4% |
| Market under 3 5 odds | 2.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:47:05Z |
| Market reference under 3 5 odds | 2.65 |
| Market reference under 3 5 opposite odds | 1.47 |
| Market reference under 3 5 last update utc | 2026-10-24T14:47:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 77.7% |
| Market btts yes odds | 1.28 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:46:49Z |
| Market reference btts yes odds | 1.25 |
| Market reference btts yes opposite odds | 3.75 |
| Market reference btts yes last update utc | 2026-10-24T14:47:05Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,739.3786 |
| Elo away rating | 1,656.5478 |
| Elo rating diff | 142.8309 |
| Elo home expectancy | 0.6947 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Real Betis win** at **38.8%**. Expected goals are 1.33 for Celta Vigo and 1.28 for Real Betis (2.61 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.3%; Under 3.5 goals: 73.4%; Double Chance 1X: 61.2%; Double Chance X2: 66.0%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 53.5%; BTTS No (at least one team does not score): 46.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 34.0% | 2.94 |
| Draw | 27.2% | 3.68 |
| Real Betis win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.33 |
| Real Betis expected goals | 1.28 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.3% |
| Under 2.5 | 51.7% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.95% |
| 2 | 0-1 | 10.01% |
| 3 | 1-2 | 8.76% |
| 4 | 1-0 | 8.59% |
| 5 | 0-0 | 7.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 34.0% | 30.4% | 3.17 | +7.8% |
| Draw | 27.2% | 27.6% | 3.62 | -1.5% |
| Real Betis win | 38.8% | 42.0% | 2.26 | -12.4% |

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
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3278 |
| Dc lambda away | 1.2822 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:10.281252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.5% |
| P btts no | 46.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.96 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.10 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.2164138925314693, "-10": 3.0989685406493933e-07, "-11": 3.566688211408863e-08, "-12": 3.769209332656485e-09, "-13": 3.6610346655555976e-10, "-14": 2.989414596542277e-11, "-2": 0.11239991792523786, "-3": 0.04246452983124079, "-4": 0.012595202157859735, "-5": 0.00306265605599387, "-6": 0.0006296939762288148, "-7": 0.00011201257714487852, "-8": 1.7545336753155427e-05, "-9": 2.4538781998563348e-06, "0": 0.2720889374145702, "1": 0.18560013010565585, "10": 3.638930895521574e-07, "11": 4.337170670333555e-08, "12": 4.746531296687252e-09, "13": 4.774354441228371e-10, "14": 4.037213269111085e-11, "2": 0.0997803065692765, "3": 0.039038209004252, "4": 0.011990945596189047, "5": 0.003019473638595889, "6": 0.000642905704225143, "7": 0.00011843205220743119, "8": 1.9210952523546848e-05, "9": 2.782434297792415e-06} |
| Raw goal margin distribution | {"-1": 0.19819791965175554, "-10": 2.838122408124205e-07, "-11": 3.2664732161078054e-08, "-12": 3.451947745710765e-09, "-13": 3.3528783480504486e-10, "-14": 2.7377898298516815e-11, "-2": 0.10293900100970087, "-3": 0.038890208817430647, "-4": 0.01153503980765977, "-5": 0.002804866415027254, "-6": 0.000576691425147972, "-7": 0.00010258426344657356, "-8": 1.6068512069109557e-05, "-9": 2.247330559980564e-06, "0": 0.26853018942897, "1": 0.20534438971931263, "10": 4.026042673279671e-07, "11": 4.798561638405909e-08, "12": 5.2514703079519e-09, "13": 5.282253296264548e-10, "14": 4.4666945785026894e-11, "2": 0.110394998897954, "3": 0.04319111844991545, "4": 0.013266549997595531, "5": 0.0033406871602841112, "6": 0.0007112984209980028, "7": 0.0001310309290726065, "8": 2.125462584335873e-05, "9": 3.07843142399207e-06} |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 53.4% |
| P home draw | 61.2% |
| P draw away | 66.0% |
| P home away | 72.8% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:17Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.31, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:17Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.65, "price": 2.31, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.14 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | +3.6% |
| Draw probability edge | -0.4% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | 0.0724 |
| Raw ev home | 0.1932 |
| Raw edge prob draw | -0.0071 |
| Raw ev draw | -0.0279 |
| Raw edge prob away | -0.0653 |
| Raw ev away | -0.1976 |
| Market p home draw | 58.3% |
| Market home draw odds | 1.68 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:43:17Z |
| Market reference home draw last update utc | 2026-10-24T14:43:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.3% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:43:17Z |
| Market reference draw away last update utc | 2026-10-24T14:43:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.4% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:43:17Z |
| Market reference home away last update utc | 2026-10-24T14:43:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.65 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 80.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market reference over 1 5 last update utc | 2026-10-24T14:43:18Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.1% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:43:14Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market reference under 3 5 last update utc | 2026-10-24T14:43:18Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.9% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:43:17Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.43 |
| Market reference btts yes last update utc | 2026-10-24T14:43:17Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,477.2163 |
| Elo away rating | 1,549.1815 |
| Elo rating diff | -11.9651 |
| Elo home expectancy | 0.4828 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **59.5%**. Expected goals are 2.00 for Real Sociedad and 1.06 for Levante (3.06 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 59.0%; Under 3.5 goals: 63.3%; Double Chance 1X: 81.2%; Double Chance X2: 40.5%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 59.5% | 1.68 |
| Draw | 21.8% | 4.60 |
| Levante win | 18.8% | 5.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 2.00 |
| Levante expected goals | 1.06 |
| Expected total goals | 3.06 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 59.0% |
| Under 2.5 | 41.0% |
| Over 3.5 | 36.7% |
| Under 3.5 | 63.3% |
| Over 4.5 | 19.5% |
| Under 4.5 | 80.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.16% |
| 2 | 2-1 | 10.03% |
| 3 | 2-0 | 9.46% |
| 4 | 1-0 | 9.26% |
| 5 | 3-1 | 6.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 59.5% | 60.0% | 1.61 | -4.3% |
| Draw | 21.8% | 21.8% | 4.49 | -2.3% |
| Levante win | 18.8% | 18.2% | 5.14 | -3.4% |

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
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9984 |
| Dc lambda away | 1.0605 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:10.281252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.38 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.32 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.13 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.1191155282787892, "-10": 2.733987771232674e-08, "-11": 2.5946119712516834e-09, "-12": 2.2625185512015487e-10, "-13": 1.82458947106634e-11, "-14": 1.368373151355945e-12, "-15": 9.58730977457742e-14, "-16": 6.2649638646667876e-15, "-17": 3.4748976181793695e-16, "-2": 0.04925166829596425, "-3": 0.01499998115632419, "-4": 0.0036175853750742993, "-5": 0.0007188381104364846, "-6": 0.00012115362903830221, "-7": 1.7702889688111324e-05, "-8": 2.2810296566270024e-06, "-9": 2.627007265377165e-07, "0": 0.21762661433896463, "1": 0.23532610837447723, "10": 1.6062003713354283e-05, "11": 2.872586010443684e-06, "12": 4.720524344526127e-07, "13": 7.173989332827303e-08, "14": 1.0139057262658143e-08, "15": 1.3387123219897315e-09, "16": 1.6485667658046338e-10, "17": 1.72316733245921e-11, "2": 0.18190487818321832, "3": 0.10440266451738975, "4": 0.04745009953406669, "5": 0.01776834187361811, "6": 0.005643515271901355, "7": 0.0015540139374856118, "8": 0.000377345475868243, "9": 8.189680494414731e-05} |
| Raw goal margin distribution | {"-1": 0.12271675194410842, "-10": 2.8166445130087146e-08, "-11": 2.673054959904876e-09, "-12": 2.3309213486163483e-10, "-13": 1.8797523442672006e-11, "-14": 1.4097432216302165e-12, "-15": 9.8771632248022e-14, "-16": 6.454372722250853e-15, "-17": 3.579954311609468e-16, "-2": 0.050740695595652294, "-3": 0.01545347607759984, "-4": 0.00372695595212903, "-5": 0.0007405707665581818, "-6": 0.00012481647067059455, "-7": 1.8238101731499578e-05, "-8": 2.3499921008980316e-06, "-9": 2.70642966201801e-07, "0": 0.2175242771466301, "1": 0.2331187052105155, "10": 1.5911339097084834e-05, "11": 2.8456406133009438e-06, "12": 4.676244938192326e-07, "13": 7.106695963379698e-08, "14": 1.004395099826709e-08, "15": 1.3261549485830706e-09, "16": 1.6331028994279865e-10, "17": 1.707003698734162e-11, "2": 0.18019857620756696, "3": 0.10342334788493607, "4": 0.047005008674555586, "5": 0.017601671484424555, "6": 0.005590578037044107, "7": 0.0015394369944250156, "8": 0.00037380590432179676, "9": 8.112859750808843e-05} |
| Unadjusted home-win probability | 58.9% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 56.7% |
| P home draw | 81.2% |
| P draw away | 40.5% |
| P home away | 78.2% |
| Raw p home draw | 80.6% |
| Raw p draw away | 41.1% |
| Raw p home away | 78.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:14Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 4.04, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:14Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.27, "price": 4.04, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.63 |
| Reference draw odds | 4.30 |
| Reference away odds | 5.10 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | -0.6% |
| Draw probability edge | -0.0% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0112 |
| Raw ev home | -0.0518 |
| Raw edge prob draw | -0.0002 |
| Raw ev draw | -0.0233 |
| Raw edge prob away | 0.0114 |
| Raw ev away | -0.0053 |
| Market p home draw | 81.3% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:47:14Z |
| Market reference home draw last update utc | 2026-10-24T14:47:14Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.1% |
| Market draw away odds | 2.41 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:47:14Z |
| Market reference draw away last update utc | 2026-10-24T14:47:14Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.6% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:47:14Z |
| Market reference home away last update utc | 2026-10-24T14:47:14Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.41 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 83.0% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-24T14:47:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.1% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:47:05Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.51 |
| Market reference under 3 5 last update utc | 2026-10-24T14:47:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:47:14Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.29 |
| Market reference btts yes last update utc | 2026-10-24T14:47:14Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,485.8012 |
| Elo away rating | 1,453.6938 |
| Elo rating diff | 92.1074 |
| Elo home expectancy | 0.6295 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **49.0%**. Expected goals are 1.48 for Sevilla and 0.98 for CA Osasuna (2.46 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.6%; Double Chance 1X: 75.9%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 49.0% | 2.04 |
| Draw | 26.9% | 3.72 |
| CA Osasuna win | 24.1% | 4.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.48 |
| CA Osasuna expected goals | 0.98 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.73% |
| 2 | 1-0 | 12.48% |
| 3 | 2-0 | 9.45% |
| 4 | 2-1 | 9.25% |
| 5 | 0-0 | 8.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 49.0% | 49.3% | 1.93 | -5.5% |
| Draw | 26.9% | 27.1% | 3.46 | -6.9% |
| CA Osasuna win | 24.1% | 23.6% | 4.38 | +5.7% |

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
| Market best home last update utc | 2026-10-24T14:43:14Z |
| Market best draw last update utc | 2026-10-24T14:43:14Z |
| Market best away last update utc | 2026-10-24T14:43:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.4829 |
| Dc lambda away | 0.9785 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:10.281252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.29 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.27 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.65 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.15447450355836786, "-10": 2.1088058670955208e-08, "-11": 1.8556401537198666e-09, "-12": 1.4992570483315326e-10, "-13": 1.1194458850330413e-11, "-14": 7.739876605474395e-13, "-15": 4.6035912686911383e-14, "-2": 0.06311395427949941, "-3": 0.018494092693674732, "-4": 0.004230828960975341, "-5": 0.0007909528331264934, "-6": 0.00012478519372689426, "-7": 1.701075298090217e-05, "-8": 2.0401279449597827e-06, "-9": 2.183294616648714e-07, "0": 0.26907721898677617, "1": 0.24255260300397163, "10": 1.3884310512558217e-06, "11": 1.8515456064978778e-07, "12": 2.267094834049534e-08, "13": 2.5653677341863137e-09, "14": 2.688026194346764e-10, "15": 2.4229762269144394e-11, "2": 0.14934463349429575, "3": 0.0663208671935735, "4": 0.0229929963605285, "5": 0.006514388030185581, "6": 0.0015575393627945931, "7": 0.0003217751099618452, "8": 5.848429374895556e-05, "9": 9.485213806056582e-06} |
| Raw goal margin distribution | {"-1": 0.1579860985314496, "-10": 2.1567443418050374e-08, "-11": 1.897823533407436e-09, "-12": 1.5333389414142257e-10, "-13": 1.1448937126807523e-11, "-14": 7.915823516802628e-13, "-15": 4.7082425061761036e-14, "-2": 0.06454869360200165, "-3": 0.018914510053425482, "-4": 0.004327006371286395, "-5": 0.0008089331854096927, "-6": 0.000127621875825962, "-7": 1.7397450288743012e-05, "-8": 2.086505197327889e-06, "-9": 2.232926408458831e-07, "0": 0.26718367926982933, "1": 0.2407740327348404, "10": 1.3782500754265838e-06, "11": 1.837968741410168e-07, "12": 2.2504708629224323e-08, "13": 2.5465566114652863e-09, "14": 2.668315651509041e-10, "15": 2.4052092212149328e-11, "2": 0.14824953114660872, "3": 0.06583455485904226, "4": 0.022824395161371684, "5": 0.006466619848238334, "6": 0.0015461183631047951, "7": 0.0003194156232491209, "8": 5.80554448115095e-05, "9": 9.415661391187095e-06} |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 48.5% |
| P home draw | 75.9% |
| P draw away | 51.0% |
| P home away | 73.1% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.48, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:43:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.96, "price": 1.48, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.97 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-24T14:43:20Z |
| Market reference home last update utc | 2026-10-24T14:43:20Z |
| Market reference draw last update utc | 2026-10-24T14:43:20Z |
| Market reference away last update utc | 2026-10-24T14:43:20Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-24T14:43:20Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:43:20Z |
| Home probability edge | -0.4% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0072 |
| Raw ev home | -0.0619 |
| Raw edge prob draw | -0.0038 |
| Raw ev draw | -0.0755 |
| Raw edge prob away | 0.0110 |
| Raw ev away | 0.0807 |
| Elo home rating | 1,440.7731 |
| Elo away rating | 1,423.7802 |
| Elo rating diff | 76.9929 |
| Elo home expectancy | 0.6090 |

</details>


---
