# Bundesliga — football model report

Fixtures in this report: **3**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,587 |
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
| Training sha256 | 42233672382c0d6893d68f382922beed281707a6b76091a46319d593ec3d12cd |
| Training as of utc | 2026-10-24T14:47:45.769331+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 55, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 55, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 31, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-24T14:47:45.769331+00:00', 'observations': 194, 'observations_sha256': '5ba4f0a2ece559868a6f405768949e44fe4ef012073648a9d483ab985d7f4453', 'eligible_training_matches': 34, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 72, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 34, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '9f24301b8ec6079a5a306b31646009248d772c3738f2975750609685b4eb7d46', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 4832.609 |
| Base scoring parameter | 0.233 |
| Home-advantage parameter | 0.235 |
| Dixon-Coles low-score adjustment | -0.111 |
| Xi per day | 0 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1587, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-23'} |
| Training data health | {'training_end': '2026-10-23', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 3.00 |
| Additional event odds calls used before this league | 12.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261024T144745769331Z_4c010b027b9911b5024af4379c6ae425592fb3e5993781b99a84363c25a04c66.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
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

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **64.1%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.8%; Under 3.5 goals: 50.5%; Double Chance 1X: 83.3%; Double Chance X2: 35.9%; Double Chance 12 (either team wins): 80.7%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 64.1% | 1.56 |
| Draw | 19.3% | 5.19 |
| Eintracht Frankfurt win | 16.7% | 6.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.42 |
| Eintracht Frankfurt expected goals | 1.22 |
| Expected total goals | 3.64 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 70.8% |
| Under 2.5 | 29.2% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.4% |
| Under 4.5 | 69.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.55% |
| 2 | 1-1 | 8.26% |
| 3 | 2-0 | 7.81% |
| 4 | 3-1 | 7.70% |
| 5 | 3-0 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 64.1% | 65.2% | 1.51 | -3.3% |
| Draw | 19.3% | 18.5% | 5.07 | -2.2% |
| Eintracht Frankfurt win | 16.7% | 16.3% | 5.72 | -4.7% |

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
| Dc lambda home | 2.4188 |
| Dc lambda away | 1.2231 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:45.769331+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.94 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.92 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.29 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.09884272143146772, "-10": 6.912055373074699e-08, "-11": 7.519904330738445e-09, "-12": 7.524004615069328e-10, "-13": 6.967030196761301e-11, "-14": 6.002963636585446e-12, "-15": 4.835564552616675e-13, "-16": 3.6547197631163697e-14, "-17": 2.576351234599624e-15, "-18": 1.5034747744955149e-16, "-2": 0.0466930455965893, "-3": 0.01564020131377984, "-4": 0.004211922675414806, "-5": 0.0009431280745788351, "-6": 0.00018017356330372593, "-7": 2.9958485374763924e-05, "-8": 4.404773860543486e-06, "-9": 5.800144541269921e-07, "0": 0.19286396507938683, "1": 0.2118612141975243, "10": 6.579362245936987e-05, "11": 1.4156244649775984e-05, "12": 2.801198929357572e-06, "13": 5.129815501906502e-07, "14": 8.741358254970065e-08, "15": 1.39257805398407e-08, "16": 2.0815440094186836e-09, "17": 2.90198885559022e-10, "18": 3.3492376936219936e-11, "2": 0.18991337734434685, "3": 0.12580701214723114, "4": 0.0670042041721625, "5": 0.029672319111839793, "6": 0.011210656353468434, "7": 0.0036865402462314344, "8": 0.0010719681893874209, "9": 0.00027916196835590414} |
| Raw goal margin distribution | {"-1": 0.1009097750930616, "-10": 7.05660409817187e-08, "-11": 7.677164729446365e-09, "-12": 7.681350761191088e-10, "-13": 7.112728585778599e-11, "-14": 6.128500932460306e-12, "-15": 4.93668855314604e-13, "-16": 3.731149284269195e-14, "-17": 2.630229316626366e-15, "-18": 1.5349162705685434e-16, "-2": 0.04766951639255296, "-3": 0.015967277854424554, "-4": 0.004300004732064801, "-5": 0.0009628512905291549, "-6": 0.00018394145251555432, "-7": 3.0584993791295605e-05, "-8": 4.49688892784505e-06, "-9": 5.921440372042027e-07, "0": 0.20106807569899232, "1": 0.2079959863073187, "10": 6.459327370515893e-05, "11": 1.389797599098375e-05, "12": 2.750093434334437e-06, "13": 5.0362263755311e-07, "14": 8.581879598844321e-08, "15": 1.3671716502969418e-08, "16": 2.0435680071080656e-09, "17": 2.849044533977697e-10, "18": 3.288133696869449e-11, "2": 0.18644856909421512, "3": 0.12351177007577983, "4": 0.065781769382915, "5": 0.029130972854420373, "6": 0.011006127451049617, "7": 0.003619282450923916, "8": 0.0010524110403418649, "9": 0.00027406889537385306} |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.1% |
| P home draw | 83.3% |
| P draw away | 35.9% |
| P home away | 80.7% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.1% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 6.5, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:39Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.62, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:39Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.23, "price": 4.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.65, "quote_source": "The Odds API", "side": "home"}] |
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
| Draw probability edge | +0.8% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | -0.0234 |
| Raw ev home | -0.0504 |
| Raw edge prob draw | 0.0164 |
| Raw ev draw | 0.0194 |
| Raw edge prob away | 0.0070 |
| Raw ev away | -0.0274 |
| Market p home draw | 83.1% |
| Market home draw odds | 1.17 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:47:39Z |
| Market reference home draw last update utc | 2026-10-24T14:47:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.0% |
| Market draw away odds | 2.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:47:39Z |
| Market reference draw away last update utc | 2026-10-24T14:47:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.0% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:47:39Z |
| Market reference home away last update utc | 2026-10-24T14:47:49Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.16 |
| Market reference dc draw away odds | 2.68 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 89.5% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-24T14:47:46Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 50.3% |
| Market under 3 5 odds | 1.94 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:47:46Z |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 1.96 |
| Market reference under 3 5 last update utc | 2026-10-24T14:47:46Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.8% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:47:39Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 2.59 |
| Market reference btts yes last update utc | 2026-10-24T14:47:46Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,632.5902 |
| Elo away rating | 1,482.6947 |
| Elo rating diff | 209.8955 |
| Elo home expectancy | 0.7700 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **67.1%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 72.1%; Under 3.5 goals: 49.2%; Double Chance 1X: 32.9%; Double Chance X2: 84.9%; Double Chance 12 (either team wins): 82.2%; Under 4.5 goals: 68.4%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 15.1% | 6.63 |
| Draw | 17.8% | 5.60 |
| Bayern Munich win | 67.1% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.24 |
| Bayern Munich expected goals | 2.45 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 89.3% |
| Under 1.5 | 10.7% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.6% |
| Under 4.5 | 68.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.88% |
| 2 | 1-3 | 8.06% |
| 3 | 0-2 | 7.99% |
| 4 | 1-1 | 7.57% |
| 5 | 0-3 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 15.1% | 13.2% | 6.75 | +1.8% |
| Draw | 17.8% | 15.8% | 6.03 | +7.6% |
| Bayern Munich win | 67.1% | 71.0% | 1.38 | -7.5% |

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
| Dc lambda home | 1.2369 |
| Dc lambda away | 2.4473 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:45.769331+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.23 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.39 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.58 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.16 |
| Fair Under 4.5 odds | 1.46 |
| Goal margin distribution | {"-1": 0.21970840246682358, "-10": 7.439265857220664e-05, "-11": 1.618682463971628e-05, "-12": 3.239337065094444e-06, "-13": 5.999809311297452e-07, "-14": 1.0340898215316866e-07, "-15": 1.6663185309013165e-08, "-16": 2.5193012880030135e-09, "-17": 3.551180572925831e-10, "-18": 4.1331516341964676e-11, "-2": 0.19804506762148147, "-3": 0.13225064996750593, "-4": 0.0710838704093544, "-5": 0.03179070838102872, "-6": 0.012135477205540618, "-7": 0.004033259359904708, "-8": 0.001185564780047924, "-9": 0.0003121584614038913, "0": 0.17847577072456916, "1": 0.08926141545445355, "10": 6.776106649695596e-08, "11": 7.451913052788317e-09, "12": 7.537341998163525e-10, "13": 7.05594996490265e-11, "14": 6.146562075835904e-12, "15": 5.005967163060762e-13, "16": 3.825304795716146e-14, "17": 2.7253021335465454e-15, "18": 1.6031686163371226e-16, "2": 0.04236102631532613, "3": 0.014297372156216773, "4": 0.003884055589589794, "5": 0.000877951529198133, "6": 0.00016938820155636594, "7": 2.8453677991162097e-05, "8": 4.227304334054415e-06, "9": 5.625605854885934e-07} |
| Raw goal margin distribution | {"-1": 0.20681466704779627, "-10": 7.002687535236412e-05, "-11": 1.5236889945205865e-05, "-12": 3.0492343899967846e-06, "-13": 5.647706465180006e-07, "-14": 9.734035646173562e-08, "-15": 1.568529506812863e-08, "-16": 2.371454396925507e-09, "-17": 3.3427771517621383e-10, "-18": 3.8905948497507894e-11, "-2": 0.186422659582989, "-3": 0.12448943159565551, "-4": 0.06691226564900829, "-5": 0.029925049270834538, "-6": 0.011423298560959624, "-7": 0.0037965648207835666, "-8": 0.0011159891132804071, "-9": 0.0002938392320755537, "0": 0.1990926306316923, "1": 0.1003478155565481, "10": 7.617709139086111e-08, "11": 8.377451699118515e-09, "12": 8.473491046131512e-10, "13": 7.932309408823703e-11, "14": 6.9099741960464385e-12, "15": 5.627715704522749e-13, "16": 4.3004133211843516e-14, "17": 3.0637886979569633e-15, "18": 1.802284534691607e-16, "2": 0.04762232857090929, "3": 0.016073126969484836, "4": 0.004366461050737127, "5": 0.0009869944104182135, "6": 0.00019042646725568518, "7": 3.198766697150879e-05, "8": 4.752341798025164e-06, "9": 6.324314440296782e-07} |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 32.9% |
| P draw away | 84.9% |
| P home away | 82.2% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:37Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 5.64, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:37Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.17, "price": 5.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:46Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.21, "quote_source": "The Odds API", "side": "home"}] |
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
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | 0.0375 |
| Raw ev home | 0.1450 |
| Raw edge prob draw | 0.0412 |
| Raw ev draw | 0.2005 |
| Raw edge prob away | -0.0787 |
| Raw ev away | -0.1288 |
| Market p home draw | 30.4% |
| Market home draw odds | 3.25 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:47:37Z |
| Market reference home draw last update utc | 2026-10-24T14:47:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 85.9% |
| Market draw away odds | 1.13 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:47:37Z |
| Market reference draw away last update utc | 2026-10-24T14:47:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.7% |
| Market home away odds | 1.15 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:47:37Z |
| Market reference home away last update utc | 2026-10-24T14:47:49Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.16 |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 92.5% |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market reference over 1 5 last update utc | 2026-10-24T14:47:46Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 42.5% |
| Market under 3 5 odds | 2.23 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:47:46Z |
| Market reference under 3 5 odds | 2.23 |
| Market reference under 3 5 opposite odds | 1.68 |
| Market reference under 3 5 last update utc | 2026-10-24T14:47:46Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.9% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:47:37Z |
| Market reference btts yes odds | 1.39 |
| Market reference btts yes opposite odds | 2.81 |
| Market reference btts yes last update utc | 2026-10-24T14:47:46Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,530.0224 |
| Elo away rating | 1,716.0474 |
| Elo rating diff | -126.0250 |
| Elo home expectancy | 0.3262 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.6%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.4%; Double Chance X2: 69.3%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 69.9%; BTTS No (at least one team does not score): 30.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.7% | 3.26 |
| Draw | 22.6% | 4.42 |
| Bayer Leverkusen win | 46.6% | 2.14 |

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
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 49.4% |
| Under 3.5 | 50.6% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.32% |
| 2 | 1-2 | 8.11% |
| 3 | 2-1 | 7.48% |
| 4 | 2-2 | 6.79% |
| 5 | 1-3 | 5.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.7% | 35.7% | 2.83 | -13.1% |
| Draw | 22.6% | 22.8% | 3.99 | -9.7% |
| Bayer Leverkusen win | 46.6% | 41.5% | 2.33 | +8.7% |

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
| Dc lambda home | 1.4998 |
| Dc lambda away | 2.1591 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:47:45.769331+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 69.9% |
| P btts no | 30.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.39 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.92 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.40 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.18055224133250075, "-10": 1.88277367490382e-05, "-11": 3.608822254253352e-06, "-12": 6.363430342928468e-07, "-13": 1.0386739787451206e-07, "-14": 1.5777869899644422e-08, "-15": 2.239109868347087e-09, "-16": 2.9444507142407963e-10, "-17": 3.1412905491982046e-11, "-2": 0.14192444732034687, "-3": 0.0826911730575009, "-4": 0.03891075890645014, "-5": 0.015266877229835293, "-6": 0.005119827300693897, "-7": 0.0014962716223878053, "-8": 0.00038701160210639684, "-9": 8.970759638030059e-05, "0": 0.22642601349713865, "1": 0.16313103137106222, "10": 6.538965017386251e-07, "11": 8.70638553917156e-08, "12": 1.066412441126809e-08, "13": 1.2091346481781829e-09, "14": 1.2758666666925922e-10, "15": 1.2577485650936258e-11, "16": 1.1489052706217905e-12, "17": 8.514311719608573e-14, "2": 0.0909234822822783, "3": 0.036799295768116726, "4": 0.012028502477564398, "5": 0.003278336883837098, "6": 0.0007636954172511619, "7": 0.0001550375218978878, "8": 2.7855558437378886e-05, "9": 4.485166926373869e-06} |
| Raw goal margin distribution | {"-1": 0.20048873663120353, "-10": 2.090668676600953e-05, "-11": 4.007306744807417e-06, "-12": 7.066077389451616e-07, "-13": 1.1533638809103479e-07, "-14": 1.7520055024328234e-08, "-15": 2.4863513483427455e-09, "-16": 3.2695756054550764e-10, "-17": 3.48815040429476e-11, "-2": 0.15759567940193808, "-3": 0.09182189428664982, "-4": 0.04320726697681415, "-5": 0.016952638779358056, "-6": 0.0056851562722821354, "-7": 0.001661489245526484, "-8": 0.00042974524489584664, "-9": 9.961306783994428e-05, "0": 0.22517661410207024, "1": 0.13643564247141088, "10": 5.468903652155978e-07, "11": 7.281639150179412e-08, "12": 8.91900610949312e-09, "13": 1.0112672075455137e-09, "14": 1.0670789420935406e-10, "15": 1.051925756269597e-11, "16": 9.608939967989456e-13, "17": 7.120997028605341e-14, "2": 0.07604441421511873, "3": 0.03077731758587474, "4": 0.010060112105602571, "5": 0.0027418572372453036, "6": 0.0006387213642273192, "7": 0.0001296665859924552, "8": 2.3297167803463583e-05, "9": 3.751196973673356e-06} |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.6% |
| P home draw | 53.4% |
| P draw away | 69.3% |
| P home away | 77.4% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.45, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.15, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.39, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.99, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:46Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:46Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:46:09Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:47:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.79, "quote_source": "The Odds API", "side": "away"}] |
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
| Away probability edge | +5.2% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.1005 |
| Raw ev home | -0.2731 |
| Raw edge prob draw | -0.0025 |
| Raw ev draw | -0.1015 |
| Raw edge prob away | 0.1030 |
| Raw ev away | 0.2069 |
| Market p home draw | 58.7% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:47:37Z |
| Market reference home draw last update utc | 2026-10-24T14:47:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.2% |
| Market draw away odds | 1.47 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:47:37Z |
| Market reference draw away last update utc | 2026-10-24T14:47:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.1% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:47:37Z |
| Market reference home away last update utc | 2026-10-24T14:47:49Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.64 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 88.7% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market reference over 1 5 last update utc | 2026-10-24T14:47:46Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.89 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:47:47Z |
| Market reference under 3 5 odds | 1.89 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market reference under 3 5 last update utc | 2026-10-24T14:47:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 72.9% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:47:37Z |
| Market reference btts yes odds | 1.32 |
| Market reference btts yes opposite odds | 3.15 |
| Market reference btts yes last update utc | 2026-10-24T14:47:46Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,477.9861 |
| Elo away rating | 1,602.4119 |
| Elo rating diff | -64.4258 |
| Elo home expectancy | 0.4083 |

</details>


---
