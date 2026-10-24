# Premier League — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,971 |
| Training data through | 2026-10-23 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 3bc6190356fc96a5178adca6e1b39d19857b911e794cf07d102947fea0b2f137 |
| Training as of utc | 2026-10-24T14:46:21.720761+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 71, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 71, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 99, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-24T14:46:21.720761+00:00', 'observations': 300, 'observations_sha256': 'bfd2e41076e98c62f4d96c6d69a90179b5bf20c29a1a8a6f92fcd137b57cac68', 'eligible_training_matches': 147, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 138, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 9, 'retrospective_eligible_training_matches': 147, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'efe4297379d47966926eade2e8a06f319ef61ce48521665bd602e3f50ea0a236', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 83, 'tuning_matches': 24, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 34, 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 924.399 |
| Base scoring parameter | 0.210 |
| Home-advantage parameter | 0.186 |
| Dixon-Coles low-score adjustment | -0.095 |
| Xi per day | 0.0029 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1971, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-23'} |
| Training data health | {'training_end': '2026-10-23', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261024T144621720761Z_ffe2f97bca7d84a47cd66d7fd2b4f34449beeceb7ad066a25f4670cd166389d6.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **55.4%**. Expected goals are 2.14 for Chelsea and 1.19 for Tottenham Hotspur (3.33 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.7%; Double Chance 1X: 77.9%; Double Chance X2: 44.6%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 75.9%; BTTS Yes (both teams score): 62.5%; BTTS No (at least one team does not score): 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 55.4% | 1.81 |
| Draw | 22.5% | 4.45 |
| Tottenham Hotspur win | 22.1% | 4.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.14 |
| Tottenham Hotspur expected goals | 1.19 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.4% |
| Under 2.5 | 35.6% |
| Over 3.5 | 42.3% |
| Under 3.5 | 57.7% |
| Over 4.5 | 24.1% |
| Under 4.5 | 75.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.12% |
| 2 | 2-1 | 9.31% |
| 3 | 2-0 | 7.80% |
| 4 | 3-1 | 6.62% |
| 5 | 1-0 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 55.4% | 52.7% | 1.93 | +6.9% |
| Draw | 22.5% | 22.7% | 3.90 | -12.4% |
| Tottenham Hotspur win | 22.1% | 24.5% | 3.94 | -12.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0382a9faef0bb8df1bcc436536cffb05 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1354 |
| Dc lambda away | 1.1933 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:46:21.720761+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.5% |
| P btts no | 37.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.20 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.76 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.15 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.13148686838209503, "-10": 8.153290164574693e-08, "-11": 8.680139411383144e-09, "-12": 8.495012012484535e-10, "-13": 7.691535964177054e-11, "-14": 6.478171280308929e-12, "-15": 5.097642654842745e-13, "-16": 3.732816715420188e-14, "-17": 2.278714503870233e-15, "-2": 0.062090114364193025, "-3": 0.020755516105360278, "-4": 0.005538781229434839, "-5": 0.0012236859341598072, "-6": 0.00023000954047734968, "-7": 3.7558828231033095e-05, "-8": 5.415985295128823e-06, "-9": 6.987718355397406e-07, "0": 0.22471974652119878, "1": 0.20690337001483852, "10": 2.3372614316869542e-05, "11": 4.452608015378365e-06, "12": 7.797674995160254e-07, "13": 1.2633613226184065e-07, "14": 1.9040585445277807e-08, "15": 2.681085282246501e-09, "16": 3.513106179121744e-10, "17": 3.837584007899948e-11, "2": 0.1693128419777369, "3": 0.10127782033919273, "4": 0.04836246073130553, "5": 0.019119543360755633, "6": 0.006430826122807286, "7": 0.0018790845458520427, "8": 0.0004848697966489936, "9": 0.00011194286477524174} |
| Raw goal margin distribution | {"-1": 0.11732975990590425, "-10": 7.275430537084612e-08, "-11": 7.745554256626019e-09, "-12": 7.580359408410013e-10, "-13": 6.863393121220692e-11, "-14": 5.780670650237143e-12, "-15": 4.548782674181031e-13, "-16": 3.3309066858317284e-14, "-17": 2.0333667454628006e-15, "-2": 0.05540491077565985, "-3": 0.018520782731613557, "-4": 0.004942424135712498, "-5": 0.0010919324387434677, "-6": 0.00020524455782041954, "-7": 3.351489280198185e-05, "-8": 4.832849562473151e-06, "-9": 6.235355112012856e-07, "0": 0.22206844911237597, "1": 0.21679669802166543, "10": 2.449020336240933e-05, "11": 4.665514705002634e-06, "12": 8.170529997049397e-07, "13": 1.3237704302849765e-07, "14": 1.9951033434784396e-08, "15": 2.809284528636922e-09, "16": 3.6810894833587376e-10, "17": 4.021082601186199e-11, "2": 0.17740873467070592, "3": 0.10612053844649211, "4": 0.050674968677395425, "5": 0.02003376681586485, "6": 0.006738323638112332, "7": 0.0019689351836804187, "8": 0.0005080544163026412, "9": 0.00011729554452698242} |
| Unadjusted home-win probability | 58.0% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 19.8% |
| Raw p over 1 5 | 85.4% |
| Raw p under 3 5 | 57.4% |
| Raw p btts yes | 62.3% |
| P home draw | 77.9% |
| P draw away | 44.6% |
| P home away | 77.5% |
| Raw p home draw | 80.2% |
| Raw p draw away | 42.0% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 3.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.8, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.22, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.77, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.1, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 7.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.9, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.95, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.44, "price": 2.95, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.78 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.55 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:24Z |
| Market reference home last update utc | 2026-10-24T14:42:24Z |
| Market reference draw last update utc | 2026-10-24T14:42:24Z |
| Market reference away last update utc | 2026-10-24T14:42:24Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | +2.6% |
| Draw probability edge | -0.3% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | +2.5% |
| Under 2.5 probability edge | -2.5% |
| Raw edge prob home | 0.0530 |
| Raw ev home | 0.1202 |
| Raw edge prob draw | -0.0053 |
| Raw ev draw | -0.1339 |
| Raw edge prob away | -0.0477 |
| Raw ev away | -0.2217 |
| Market p home draw | 75.1% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:42:26Z |
| Market reference home draw last update utc | 2026-10-24T14:42:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.7% |
| Market draw away odds | 1.95 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:42:26Z |
| Market reference draw away last update utc | 2026-10-24T14:42:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.1% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:42:26Z |
| Market reference home away last update utc | 2026-10-24T14:42:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 84.8% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.96 |
| Market reference over 1 5 last update utc | 2026-10-24T14:42:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.1% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-10-24T14:42:23Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.1% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:42:26Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.58 |
| Market reference btts yes last update utc | 2026-10-24T14:42:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,507.4574 |
| Elo away rating | 1,444.7579 |
| Elo rating diff | 122.6995 |
| Elo home expectancy | 0.6696 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **40.2%**. Expected goals are 1.50 for Crystal Palace and 1.58 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 59.7%; Under 3.5 goals: 62.9%; Double Chance 1X: 59.8%; Double Chance X2: 65.4%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.6% | 2.89 |
| Draw | 25.2% | 3.96 |
| Newcastle United win | 40.2% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.50 |
| Newcastle United expected goals | 1.58 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 59.7% |
| Under 2.5 | 40.3% |
| Over 3.5 | 37.1% |
| Under 3.5 | 62.9% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.58% |
| 2 | 1-2 | 8.93% |
| 3 | 2-1 | 8.01% |
| 4 | 0-1 | 6.46% |
| 5 | 2-2 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.6% | 33.9% | 2.95 | +1.9% |
| Draw | 25.2% | 24.5% | 3.68 | -7.2% |
| Newcastle United win | 40.2% | 41.7% | 2.37 | -4.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | fe235b26408c477368c40672a4488694 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4996 |
| Dc lambda away | 1.5811 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:46:21.720761+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.30 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.66 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.19699988719083042, "-10": 1.58641197114165e-06, "-11": 2.2405631746818345e-07, "-12": 2.9083684771969684e-08, "-13": 3.490270493276212e-09, "-14": 3.859466186007958e-10, "-15": 3.512814355399299e-11, "-2": 0.12296106457163358, "-3": 0.05501351963638313, "-4": 0.01958523233571539, "-5": 0.005761238950228295, "-6": 0.0014400674555125755, "-7": 0.0003124477442276761, "-8": 5.982976246222398e-05, "-9": 1.024626404681093e-05, "0": 0.25230228938050686, "1": 0.1761602371017138, "10": 8.838319477316397e-07, "11": 1.1839572645963267e-07, "12": 1.4576504034179073e-08, "13": 1.6591595437088782e-09, "14": 1.7401288986166439e-10, "15": 1.5022232991163543e-11, "2": 0.10459728421378622, "3": 0.04438613609499778, "4": 0.014987588229894926, "5": 0.004181614841402523, "6": 0.0009913707281494493, "7": 0.0002040120241050931, "8": 3.705277721622709e-05, "9": 6.01858149524736e-06} |
| Raw goal margin distribution | {"-1": 0.1899662929792699, "-10": 1.5297714409541203e-06, "-11": 2.1605671279794723e-07, "-12": 2.8045294142513027e-08, "-13": 3.3656554658853195e-09, "-14": 3.7216695638234826e-10, "-15": 3.387394432227012e-11, "-2": 0.11857091874794293, "-3": 0.05304934199755428, "-4": 0.01888597012418369, "-5": 0.005555542299790675, "-6": 0.001388651943230894, "-7": 0.00030129225233094156, "-8": 5.769362788400618e-05, "-9": 9.8804361038743e-06, "0": 0.2598240486406071, "1": 0.1796453141007695, "10": 9.013172919997198e-07, "11": 1.2073801567233797e-07, "12": 1.4864879207668584e-08, "13": 1.6919836296585632e-09, "14": 1.7745548468313895e-10, "15": 1.5319426271175596e-11, "2": 0.106666591086748, "3": 0.045264251977030316, "4": 0.01528409611311925, "5": 0.004264342078504658, "6": 0.0010109835725634578, "7": 0.00020804810866331788, "8": 3.778581313711341e-05, "9": 6.1376504763132625e-06} |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 38.8% |
| Raw p over 1 5 | 82.3% |
| Raw p under 3 5 | 62.9% |
| Raw p btts yes | 62.7% |
| P home draw | 59.8% |
| P draw away | 65.4% |
| P home away | 74.8% |
| Raw p home draw | 61.2% |
| Raw p draw away | 64.8% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:25Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.17, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:25Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.74, "price": 2.17, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | +0.7% |
| Draw probability edge | +0.8% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | 0.0137 |
| Raw ev home | 0.0395 |
| Raw edge prob draw | 0.0150 |
| Raw ev draw | -0.0438 |
| Raw edge prob away | -0.0287 |
| Raw ev away | -0.0809 |
| Market p home draw | 59.0% |
| Market home draw odds | 1.64 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:42:25Z |
| Market reference home draw last update utc | 2026-10-24T14:42:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.2% |
| Market draw away odds | 1.44 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:42:25Z |
| Market reference draw away last update utc | 2026-10-24T14:42:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:42:25Z |
| Market reference home away last update utc | 2026-10-24T14:42:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.64 |
| Market reference dc draw away odds | 1.44 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-24T14:42:00Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.2% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.40 |
| Market reference under 3 5 last update utc | 2026-10-24T14:42:23Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.5% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:42:25Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.80 |
| Market reference btts yes last update utc | 2026-10-24T14:42:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,423.3950 |
| Elo away rating | 1,440.4285 |
| Elo rating diff | 42.9664 |
| Elo home expectancy | 0.5615 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **44.6%**. Expected goals are 1.19 for Hull City and 1.05 for Brentford (2.24 combined). The most likely exact score is 0-1 at 14.3%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 40.5%; Under 3.5 goals: 81.0%; Double Chance 1X: 55.4%; Double Chance X2: 71.0%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 91.9%; BTTS Yes (both teams score): 45.6%; BTTS No (at least one team does not score): 54.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 29.0% | 3.45 |
| Draw | 26.4% | 3.79 |
| Brentford win | 44.6% | 2.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.19 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.24 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 67.0% |
| Under 1.5 | 33.0% |
| Over 2.5 | 40.5% |
| Under 2.5 | 59.5% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.28% |
| 2 | 1-1 | 12.30% |
| 3 | 1-2 | 10.10% |
| 4 | 0-0 | 10.02% |
| 5 | 1-0 | 8.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 29.0% | 20.1% | 4.63 | +34.2% |
| Draw | 26.4% | 21.5% | 4.03 | +6.3% |
| Brentford win | 44.6% | 58.3% | 1.75 | -21.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 69493b5ebb84f24ab1d6023a30ee89f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1918 |
| Dc lambda away | 1.0531 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:46:21.720761+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.6% |
| P btts no | 54.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.98 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.03 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.26 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.38 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.26725918299636336, "-10": 7.915546767235479e-08, "-11": 7.506137777100268e-09, "-12": 6.509450047782887e-10, "-13": 4.8088285169456476e-11, "-2": 0.1262711820479963, "-3": 0.040345172543704746, "-4": 0.010017657290139462, "-5": 0.0020274817263708543, "-6": 0.00034574349073121524, "-7": 5.089267704076791e-05, "-8": 6.586059115149402e-06, "-9": 7.601505805320211e-07, "0": 0.2638216017874763, "1": 0.16180155475663022, "10": 1.4479298993864536e-07, "11": 1.5538952694250497e-08, "12": 1.5250641325839097e-09, "13": 1.2750337910313052e-10, "2": 0.0858345426448012, "3": 0.031037592314555232, "4": 0.008721701381673915, "5": 0.001997701460725789, "6": 0.00038553716251618126, "7": 6.422529770970784e-05, "8": 9.406218225521713e-06, "9": 1.2286484947043656e-06} |
| Raw goal margin distribution | {"-1": 0.18522822097096164, "-10": 5.4859953894546815e-08, "-11": 5.202247987243641e-09, "-12": 4.5114777285934157e-10, "-13": 3.332834970016317e-11, "-2": 0.08751424796119743, "-3": 0.02796186253079507, "-4": 0.006942896469808358, "-5": 0.0014051784077777317, "-6": 0.00023962301681250213, "-7": 3.5271978021572476e-05, "-8": 4.564572859318023e-06, "-9": 5.268344313688405e-07, "0": 0.31216166237097487, "1": 0.21128883550583882, "10": 1.890781722064471e-07, "11": 2.02915678077807e-08, "12": 1.991507591691867e-09, "13": 1.665005044870004e-10, "2": 0.11208718351856965, "3": 0.04053049271937618, "4": 0.011389248585004917, "5": 0.0026087018506091883, "6": 0.0005034543594763032, "7": 8.386871426242533e-05, "8": 1.2283126069917076e-05, "9": 1.6044327267593786e-06} |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 31.2% |
| Unadjusted away-win probability | 30.9% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 46.6% |
| P home draw | 55.4% |
| P draw away | 71.0% |
| P home away | 73.6% |
| Raw p home draw | 69.1% |
| Raw p draw away | 62.1% |
| Raw p home away | 68.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:25Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:25Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.85, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.42, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.78, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:35Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.20 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | +8.9% |
| Draw probability edge | +4.8% |
| Away probability edge | -13.7% |
| Over 2.5 probability edge | -18.5% |
| Under 2.5 probability edge | +18.5% |
| Raw edge prob home | 0.1773 |
| Raw ev home | 0.7525 |
| Raw edge prob draw | 0.0967 |
| Raw ev draw | 0.2580 |
| Raw edge prob away | -0.2740 |
| Raw ev away | -0.4587 |
| Market p home draw | 44.6% |
| Market home draw odds | 2.17 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:42:25Z |
| Market reference home draw last update utc | 2026-10-24T14:42:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.3% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:42:25Z |
| Market reference draw away last update utc | 2026-10-24T14:42:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.2% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:42:25Z |
| Market reference home away last update utc | 2026-10-24T14:42:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.17 |
| Market reference dc draw away odds | 1.22 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 81.2% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.34 |
| Market reference over 1 5 last update utc | 2026-10-24T14:42:35Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.0% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.64 |
| Market reference under 3 5 last update utc | 2026-10-24T14:42:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.2% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:42:25Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.28 |
| Market reference btts yes last update utc | 2026-10-24T14:42:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,401.6375 |
| Elo away rating | 1,497.6340 |
| Elo rating diff | -35.9965 |
| Elo home expectancy | 0.4484 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **43.5%**. Expected goals are 1.64 for Liverpool and 1.47 for Brighton and Hove Albion (3.12 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.7%; Under 3.5 goals: 62.0%; Double Chance 1X: 67.9%; Double Chance X2: 56.5%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 79.3%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 43.5% | 2.30 |
| Draw | 24.4% | 4.10 |
| Brighton and Hove Albion win | 32.1% | 3.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.64 |
| Brighton and Hove Albion expected goals | 1.47 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.7% |
| Under 2.5 | 39.3% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.7% |
| Under 4.5 | 79.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.14% |
| 2 | 2-1 | 9.41% |
| 3 | 1-2 | 7.57% |
| 4 | 1-0 | 6.69% |
| 5 | 2-0 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 43.5% | 46.3% | 2.12 | -7.7% |
| Draw | 24.4% | 23.0% | 3.99 | -2.7% |
| Brighton and Hove Albion win | 32.1% | 30.7% | 3.21 | +3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 290ba8cd3f3a2e9252effca673bf5549 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6416 |
| Dc lambda away | 1.4737 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:46:21.720761+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.34 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.83 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.1660484209670137, "-10": 7.034391123210963e-07, "-11": 9.257343361171555e-08, "-12": 1.1197443790589406e-08, "-13": 1.2521993484240566e-09, "-14": 1.2898848973018811e-10, "-15": 1.0912942944211439e-11, "-2": 0.09657711502064577, "-3": 0.04016392063991886, "-4": 0.013302891701832012, "-5": 0.0036426492843645076, "-6": 0.0008478460620269076, "-7": 0.00017133410498878745, "-8": 3.056226812120024e-05, "-9": 4.87625213710151e-06, "0": 0.2438671161207366, "1": 0.2075900442110362, "10": 2.308238044784486e-06, "11": 3.383718200257377e-07, "12": 4.559113858918112e-08, "13": 5.6792207912781125e-09, "14": 6.516583579420115e-10, "15": 6.141361029459541e-11, "2": 0.13368985502314804, "3": 0.06193185053637055, "4": 0.022849554896703244, "5": 0.006969518585098809, "6": 0.001806991713377751, "7": 0.00040675856464952235, "8": 8.08224850604535e-05, "9": 1.4364367383525215e-05} |
| Raw goal margin distribution | {"-1": 0.17343829113427978, "-10": 7.347451836487032e-07, "-11": 9.669335026822205e-08, "-12": 1.169577828444258e-08, "-13": 1.3079276146400134e-09, "-14": 1.3472903328144044e-10, "-15": 1.139861592460386e-11, "-2": 0.10087521275006334, "-3": 0.041951388158181745, "-4": 0.013894927699243083, "-5": 0.0038047628721937224, "-6": 0.0008855788648064734, "-7": 0.00017895921086885723, "-8": 3.1922420732815324e-05, "-9": 5.0932663669639686e-06, "0": 0.2573420977611633, "1": 0.19435691516565692, "10": 2.161096056207064e-06, "11": 3.1680181662437827e-07, "12": 4.268486520516917e-08, "13": 5.317190608694876e-09, "14": 6.101174489021738e-10, "15": 5.7498710457949954e-11, "2": 0.1251676009319025, "3": 0.0579839147223882, "4": 0.021392976814036815, "5": 0.006525236494542379, "6": 0.0016918024006246331, "7": 0.0003808291488300994, "8": 7.567033829619962e-05, "9": 1.3448689909858975e-05} |
| Unadjusted home-win probability | 40.8% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 33.5% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 63.2% |
| P home draw | 67.9% |
| P draw away | 56.5% |
| P home away | 75.6% |
| Raw p home draw | 66.5% |
| Raw p draw away | 59.2% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.03, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.33, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.43, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.47, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.64, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:41:50Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:25Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.42, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:25Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.6, "price": 2.42, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | -2.8% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | -0.0555 |
| Raw ev home | -0.1359 |
| Raw edge prob draw | 0.0269 |
| Raw ev draw | 0.0268 |
| Raw edge prob away | 0.0286 |
| Raw ev away | 0.0756 |
| Market p home draw | 69.5% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:42:25Z |
| Market reference home draw last update utc | 2026-10-24T14:42:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.9% |
| Market draw away odds | 1.76 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:42:25Z |
| Market reference draw away last update utc | 2026-10-24T14:42:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.5% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:42:25Z |
| Market reference home away last update utc | 2026-10-24T14:42:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.76 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-24T14:42:00Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 59.4% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market reference under 3 5 last update utc | 2026-10-24T14:42:23Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.0% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:42:25Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.69 |
| Market reference btts yes last update utc | 2026-10-24T14:42:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,558.0873 |
| Elo away rating | 1,540.2938 |
| Elo rating diff | 77.7935 |
| Elo home expectancy | 0.6101 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **46.0%**. Expected goals are 1.77 for Manchester United and 1.27 for Bournemouth (3.04 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.6%; Under 3.5 goals: 64.0%; Double Chance 1X: 71.1%; Double Chance X2: 54.0%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 46.0% | 2.18 |
| Draw | 25.1% | 3.98 |
| Bournemouth win | 28.9% | 3.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.77 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 58.6% |
| Under 2.5 | 41.4% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.67% |
| 2 | 2-1 | 9.10% |
| 3 | 1-2 | 7.44% |
| 4 | 2-0 | 7.16% |
| 5 | 1-0 | 7.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 46.0% | 43.9% | 2.21 | +1.6% |
| Draw | 25.1% | 24.9% | 3.71 | -6.8% |
| Bournemouth win | 28.9% | 31.3% | 3.21 | -7.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 33fb7467b23c91d57dc976d9ab05ea97 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7674 |
| Dc lambda away | 1.2712 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:46:21.720761+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.38 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.44 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.16332345918897623, "-10": 1.9384595615267568e-07, "-11": 2.203190543255846e-08, "-12": 2.301180369833649e-09, "-13": 2.2230204201180157e-10, "-14": 1.9965489206483804e-11, "-15": 1.6630294842567619e-12, "-16": 1.158592842780906e-13, "-2": 0.08398442181951869, "-3": 0.03043050644741157, "-4": 0.008752959314045182, "-5": 0.002077402137225099, "-6": 0.0004185819390601431, "-7": 7.316615109723197e-05, "-8": 1.128249778156498e-05, "-9": 1.5555301846726066e-06, "0": 0.25129537984502065, "1": 0.20337819417538205, "10": 4.597838409022427e-06, "11": 7.265527453504288e-07, "12": 1.0550763322604493e-07, "13": 1.4170814183158874e-08, "14": 1.769495401163949e-09, "15": 2.0492151700221172e-10, "16": 1.984890647987616e-11, "2": 0.1426759087184152, "3": 0.07187522576225572, "4": 0.028743727190996857, "5": 0.009484771607780721, "6": 0.0026570817713896955, "7": 0.0006457326930669516, "8": 0.00013844139067168283, "9": 2.653733276397869e-05} |
| Raw goal margin distribution | {"-1": 0.15007309674448438, "-10": 1.781193165739115e-07, "-11": 2.024446636058543e-08, "-12": 2.1144865898839785e-09, "-13": 2.0426677234855745e-10, "-14": 1.8345697599808376e-11, "-15": 1.5281086129275448e-12, "-16": 1.0645967005936521e-13, "-2": 0.07717080156970448, "-3": 0.02796169246441172, "-4": 0.00804283546564694, "-5": 0.0019088633896509066, "-6": 0.0003846225652334622, "-7": 6.723021252771497e-05, "-8": 1.0367153558345134e-05, "-9": 1.4293306855767007e-06, "0": 0.25381843750752253, "1": 0.21263904483362878, "10": 4.8072015368117735e-06, "11": 7.596364124432107e-07, "12": 1.1031193605985259e-07, "13": 1.481608392010437e-08, "14": 1.850069588170951e-09, "15": 2.1425264305195102e-10, "16": 2.075272883597951e-11, "2": 0.14917267347005556, "3": 0.07514807285636464, "4": 0.030052576283479494, "5": 0.009916661829558823, "6": 0.002778072311065596, "7": 0.000675136209308637, "8": 0.0001447453361321526, "9": 2.7745713419495157e-05} |
| Unadjusted home-win probability | 48.1% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 26.6% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.7% |
| P home draw | 71.1% |
| P draw away | 54.0% |
| P home away | 74.9% |
| Raw p home draw | 73.4% |
| Raw p draw away | 51.9% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.08, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.49, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.53, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:13Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.04, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:25Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.37, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:25Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.62, "price": 2.37, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.0419 |
| Raw ev home | 0.0620 |
| Raw edge prob draw | 0.0050 |
| Raw ev draw | -0.0583 |
| Raw edge prob away | -0.0469 |
| Raw ev away | -0.1474 |
| Market p home draw | 70.0% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:42:25Z |
| Market reference home draw last update utc | 2026-10-24T14:42:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.2% |
| Market draw away odds | 1.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:42:25Z |
| Market reference draw away last update utc | 2026-10-24T14:42:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:42:25Z |
| Market reference home away last update utc | 2026-10-24T14:42:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.38 |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 81.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.39 |
| Market reference over 1 5 last update utc | 2026-10-24T14:42:13Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.58 |
| Market reference under 3 5 last update utc | 2026-10-24T14:42:23Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.1% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:42:25Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-24T14:42:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,529.3488 |
| Elo away rating | 1,499.8325 |
| Elo rating diff | 89.5163 |
| Elo home expectancy | 0.6260 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **38.0%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 40.3%; Under 3.5 goals: 80.2%; Double Chance 1X: 62.0%; Double Chance X2: 67.8%; Double Chance 12 (either team wins): 70.2%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 47.2%; BTTS No (at least one team does not score): 52.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 32.2% | 3.10 |
| Draw | 29.8% | 3.36 |
| Leeds United win | 38.0% | 2.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 67.8% |
| Under 1.5 | 32.2% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 19.8% |
| Under 3.5 | 80.2% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.96% |
| 2 | 0-1 | 11.10% |
| 3 | 0-0 | 11.04% |
| 4 | 1-0 | 10.03% |
| 5 | 1-2 | 8.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 32.2% | 33.4% | 3.01 | -3.0% |
| Draw | 29.8% | 28.6% | 3.24 | -3.5% |
| Leeds United win | 38.0% | 38.0% | 2.55 | -3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | e82f6b60fa41b82c8510f5b67ce61849 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0710 |
| Dc lambda away | 1.2115 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:46:21.720761+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.2% |
| P btts no | 52.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.06 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.11 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.06 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.10 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2105256142804675, "-10": 2.1527682258530294e-07, "-11": 2.348038986766742e-08, "-12": 2.3507991192007748e-09, "-13": 2.1674088710643914e-10, "-14": 1.7164661258190196e-11, "-2": 0.11296252359544434, "-3": 0.041402835626756986, "-4": 0.01180467167003285, "-5": 0.002744978837913642, "-6": 0.0005379964080013342, "-7": 9.103761053745069e-05, "-8": 1.3545583186800848e-05, "-9": 1.7977347317095297e-06, "0": 0.2977943555909536, "1": 0.19154031515359823, "10": 6.512286394061938e-08, "11": 6.279526961857889e-09, "12": 5.558051342323433e-10, "13": 4.530366013605934e-11, "14": 3.171853281632516e-12, "2": 0.09157719351310517, "3": 0.02967347710557518, "4": 0.007479587970275115, "5": 0.0015376169998398892, "6": 0.00026642437545650787, "7": 3.9856654294635906e-05, "8": 5.242797772813145e-06, "9": 6.15143467763722e-07} |
| Raw goal margin distribution | {"-1": 0.21057180817533797, "-10": 2.1532405899852765e-07, "-11": 2.3485541975475162e-08, "-12": 2.3513149356145877e-09, "-13": 2.1678844476723655e-10, "-14": 1.7168427557888966e-11, "-2": 0.11298731002799842, "-3": 0.041411920308651005, "-4": 0.011807261871533836, "-5": 0.0027455811459239695, "-6": 0.0005381144561048718, "-7": 9.105758616761237e-05, "-8": 1.3548555382121729e-05, "-9": 1.798129193777651e-06, "0": 0.30920994640306426, "1": 0.18470274723317462, "10": 6.279812094847481e-08, "11": 6.055361662373009e-09, "12": 5.359641135428541e-10, "13": 4.368641912350442e-11, "14": 3.05862509659278e-12, "2": 0.08830808914671887, "3": 0.028614199245549726, "4": 0.007212583132559734, "5": 0.00148272745523633, "6": 0.00025691361130547537, "7": 3.8433859408860147e-05, "8": 5.055641424887598e-06, "9": 5.93184199093487e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 30.9% |
| Unadjusted away-win probability | 38.0% |
| Raw p over 1 5 | 67.8% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 47.4% |
| P home draw | 62.0% |
| P draw away | 67.8% |
| P home away | 70.2% |
| Raw p home draw | 62.0% |
| Raw p draw away | 68.9% |
| Raw p home away | 69.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.54, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.48, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:24Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:24Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:42:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.54, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | -1.1% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | -0.0230 |
| Raw ev home | -0.0650 |
| Raw edge prob draw | 0.0228 |
| Raw ev draw | 0.0018 |
| Raw edge prob away | 0.0002 |
| Raw ev away | -0.0306 |
| Market p home draw | 61.9% |
| Market home draw odds | 1.56 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:42:24Z |
| Market reference home draw last update utc | 2026-10-24T14:42:24Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.0% |
| Market draw away odds | 1.42 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:42:24Z |
| Market reference draw away last update utc | 2026-10-24T14:42:24Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.0% |
| Market home away odds | 1.38 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:42:24Z |
| Market reference home away last update utc | 2026-10-24T14:42:24Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.56 |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home away odds | 1.38 |
| Market p over 1 5 | 71.4% |
| Market over 1 5 odds | 1.37 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference over 1 5 odds | 1.37 |
| Market reference over 1 5 opposite odds | 3.23 |
| Market reference over 1 5 last update utc | 2026-10-24T14:42:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 77.0% |
| Market reference under 3 5 odds | 1.25 |
| Market reference under 3 5 opposite odds | 3.50 |
| Market reference under 3 5 last update utc | 2026-10-24T14:42:00Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 52.2% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:42:24Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.01 |
| Market reference btts yes last update utc | 2026-10-24T14:42:24Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,421.3554 |
| Elo away rating | 1,454.8163 |
| Elo rating diff | 26.5391 |
| Elo home expectancy | 0.5381 |

</details>


---
