# Serie A — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,970 |
| Training data through | 2026-10-19 |
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
| Training sha256 | d2ec277b623a04eed75eb74efb01e8c2a1c5e5333cd552e8ff7109978cfa82c7 |
| Training as of utc | 2026-10-22T15:06:43.013252+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 48, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T15:06:43.013252+00:00', 'observations': 178, 'observations_sha256': '867f9cbbaa7f0997a3c1ae2a2b00d1dd82e5a8303d991a584cb08e3bb9006b00', 'eligible_training_matches': 77, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 87, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 77, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '83fb22b26466242592f59aac353967091cb183d04079c98f63a0d50526975d1b', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2439.087 |
| Base scoring parameter | 0.132 |
| Home-advantage parameter | 0.126 |
| Dixon-Coles low-score adjustment | -0.034 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 13.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261022T150643013252Z_ceb4ef44a7515c07fbc4902e153b13f93e074bfdd5fbef48304d56579f6fe21c.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **46.9%**. Expected goals are 1.51 for Torino and 1.00 for Monza (2.51 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 45.7%; Under 3.5 goals: 75.7%; Double Chance 1X: 73.9%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 46.9% | 2.13 |
| Draw | 27.0% | 3.70 |
| Monza win | 26.1% | 3.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.51 |
| Monza expected goals | 1.00 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 71.7% |
| Under 1.5 | 28.3% |
| Over 2.5 | 45.7% |
| Under 2.5 | 54.3% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.82% |
| 2 | 1-0 | 11.43% |
| 3 | 2-0 | 8.95% |
| 4 | 2-1 | 8.91% |
| 5 | 0-0 | 8.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 46.9% | 45.0% | 2.18 | +2.3% |
| Draw | 27.0% | 27.3% | 3.40 | -8.2% |
| Monza win | 26.1% | 27.7% | 3.55 | -7.5% |
| Over 2.5 | 45.7% | 48.9% | 1.97 | -10.0% |
| Under 2.5 | 54.3% | 51.1% | 1.92 | +4.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 124c70f8f3248a845bdb983a54e74720 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5140 |
| Dc lambda away | 0.9959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.57 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.15 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.16535169138677214, "-10": 2.6227537338921493e-08, "-11": 2.3478866106182818e-09, "-12": 1.929962451288244e-10, "-13": 1.466155930687903e-11, "-14": 1.0311204164065307e-12, "-15": 6.220435167242401e-14, "-2": 0.06899955528946623, "-3": 0.020501533639022972, "-4": 0.004761815422812097, "-5": 0.0009044988529469457, "-6": 0.00014505243115270385, "-7": 2.0105597912374303e-05, "-8": 2.4522777381069275e-06, "-9": 2.6693519998663036e-07, "0": 0.2700700499032688, "1": 0.22881231975015623, "10": 1.5602376553456583e-06, "11": 2.1233981827844547e-07, "12": 2.6535315937976612e-08, "13": 3.064620100656522e-09, "14": 3.27662659130914e-10, "15": 3.005103362317475e-11, "2": 0.14385033722050306, "3": 0.06497885044003704, "4": 0.022944537719759607, "5": 0.006625762373408591, "6": 0.0016153771266645839, "7": 0.0003403979930699399, "8": 6.31190908251951e-05, "9": 1.0445229985343758e-05} |
| Raw goal margin distribution | {"-1": 0.15525754463302907, "-10": 2.46264372312178e-08, "-11": 2.2045562835441352e-09, "-12": 1.8121449433502775e-10, "-13": 1.3766522007646517e-11, "-14": 9.681740944385124e-13, "-15": 5.840699194034739e-14, "-2": 0.06478737196558526, "-3": 0.019249986179825634, "-4": 0.0044711231215179385, "-5": 0.000849282337871315, "-6": 0.00013619748376896197, "-7": 1.8878220954829063e-05, "-8": 2.302574695085205e-06, "-9": 2.506397326720435e-07, "0": 0.2667778417997532, "1": 0.23817767168780984, "10": 1.624098616873634e-06, "11": 2.210309461457145e-07, "12": 2.7621413805466154e-08, "13": 3.1900558544183604e-09, "14": 3.4107398297457404e-10, "15": 3.128103079412516e-11, "2": 0.14973817156391256, "3": 0.06763845287551601, "4": 0.02388366403527859, "5": 0.006896956671643892, "6": 0.0016814949621018042, "7": 0.0003543305776766251, "8": 6.570257278197146e-05, "9": 1.0872756156090557e-05} |
| Unadjusted home-win probability | 48.8% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 71.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 49.6% |
| P home draw | 73.9% |
| P draw away | 53.1% |
| P home away | 73.0% |
| Raw p home draw | 75.5% |
| Raw p draw away | 51.2% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.31, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.75, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.49, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:42Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.57, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:47Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.53, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:47Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.55, "price": 2.53, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.52 |
| Reference away odds | 3.48 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:18Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:18Z |
| Home probability edge | +1.9% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.0384 |
| Raw ev home | 0.0648 |
| Raw edge prob draw | -0.0066 |
| Raw ev draw | -0.0930 |
| Raw edge prob away | -0.0318 |
| Raw ev away | -0.1311 |
| Market p home draw | 72.7% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:06:47Z |
| Market reference home draw last update utc | 2026-10-22T15:06:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.6% |
| Market draw away odds | 1.74 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:06:47Z |
| Market reference draw away last update utc | 2026-10-22T15:06:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.7% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:06:47Z |
| Market reference home away last update utc | 2026-10-22T15:06:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.74 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 74.6% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:06:18Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-22T15:06:39Z |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 72.5% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:06:18Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.34 |
| Market reference under 3 5 last update utc | 2026-10-22T15:06:18Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 55.3% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:06:47Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.14 |
| Market reference btts yes last update utc | 2026-10-22T15:06:47Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **42.5%**. Expected goals are 1.04 for Cagliari and 1.43 for Bologna (2.47 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 44.0%; Under 3.5 goals: 76.6%; Double Chance 1X: 57.5%; Double Chance X2: 71.8%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 28.2% | 3.55 |
| Draw | 29.4% | 3.40 |
| Bologna win | 42.5% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.04 |
| Bologna expected goals | 1.43 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.0% |
| Under 2.5 | 56.0% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.94% |
| 2 | 0-1 | 10.91% |
| 3 | 0-0 | 9.54% |
| 4 | 1-0 | 8.74% |
| 5 | 1-2 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 28.2% | 29.2% | 3.27 | -7.9% |
| Draw | 29.4% | 31.3% | 2.97 | -12.7% |
| Bologna win | 42.5% | 39.4% | 2.56 | +8.7% |
| Over 2.5 | 44.0% | 43.5% | 2.24 | -1.4% |
| Under 2.5 | 56.0% | 56.5% | 1.76 | -1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | b7f0880e3da978f9481f7cb5697e2aa5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0400 |
| Dc lambda away | 1.4267 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.48 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.80 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.21639016260477784, "-10": 8.719439478716377e-07, "-11": 1.1184195040178586e-07, "-12": 1.3170098367157229e-08, "-13": 1.4270048623430754e-09, "-14": 1.31483083760933e-10, "-2": 0.12865507191595948, "-3": 0.05484893962568533, "-4": 0.01826919933170667, "-5": 0.004974926779228521, "-6": 0.0011435457624701295, "-7": 0.00022716522124057687, "-8": 3.970580359832204e-05, "-9": 6.193317019590994e-06, "0": 0.2939250533579676, "1": 0.17455852953093506, "10": 4.117410764566917e-08, "11": 3.8499898411714614e-09, "12": 3.304936303081753e-10, "13": 2.6104702687768616e-11, "14": 1.7534056561164964e-12, "2": 0.07617434915686873, "3": 0.023673872251025997, "4": 0.005748304976565993, "5": 0.0011411065649094558, "6": 0.0001912107403683364, "7": 2.7689798777526872e-05, "8": 3.528183553129657e-06, "9": 4.0118040782135153e-07} |
| Raw goal margin distribution | {"-1": 0.23183725394047502, "-10": 9.341879872505526e-07, "-11": 1.1982582916144235e-07, "-12": 1.4110250682441375e-08, "-13": 1.528872129226911e-09, "-14": 1.4086905204852008e-10, "-2": 0.13783916153798295, "-3": 0.05876435135173295, "-4": 0.019573352844555414, "-5": 0.005330063756908542, "-6": 0.0012251781972665696, "-7": 0.00024338149409955194, "-8": 4.2540216990121003e-05, "-9": 6.635429232646088e-06, "0": 0.27442340362840417, "1": 0.1678585209657324, "10": 3.959373873083095e-08, "11": 3.7022172574936153e-09, "12": 3.1780842861817555e-10, "13": 2.5102736573193153e-11, "14": 1.6861054047576918e-12, "2": 0.0732505803031141, "3": 0.02276520770578945, "4": 0.0055276701403200595, "5": 0.0010973079388598055, "6": 0.00018387157681288522, "7": 2.6626992568763016e-05, "8": 3.3927627284406725e-06, "9": 3.857820644930859e-07} |
| Unadjusted home-win probability | 27.1% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 49.6% |
| P home draw | 57.5% |
| P draw away | 71.8% |
| P home away | 70.6% |
| Raw p home draw | 54.5% |
| Raw p draw away | 72.9% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.7, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.48, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.79, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.64, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:03:29Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.97, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:45Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.2, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:45Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.71, "price": 2.2, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.25 |
| Reference draw odds | 3.04 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:24Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:24Z |
| Home probability edge | -1.1% |
| Draw probability edge | -2.0% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | -0.0216 |
| Raw ev home | -0.1148 |
| Raw edge prob draw | -0.0390 |
| Raw ev draw | -0.1850 |
| Raw edge prob away | 0.0606 |
| Raw ev away | 0.1644 |
| Market p home draw | 61.9% |
| Market home draw odds | 1.56 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:06:45Z |
| Market reference home draw last update utc | 2026-10-22T15:06:45Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.5% |
| Market draw away odds | 1.37 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:06:45Z |
| Market reference draw away last update utc | 2026-10-22T15:06:45Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 67.6% |
| Market home away odds | 1.43 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:06:45Z |
| Market reference home away last update utc | 2026-10-22T15:06:45Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.37 |
| Market reference dc home draw odds | 1.56 |
| Market reference dc home away odds | 1.43 |
| Market p over 1 5 | 70.8% |
| Market over 1 5 odds | 1.38 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:06:18Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 3.00 |
| Market reference over 1 5 last update utc | 2026-10-22T15:06:39Z |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 77.6% |
| Market under 3 5 odds | 1.27 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-22T15:03:29Z |
| Market reference under 3 5 odds | 1.27 |
| Market reference under 3 5 opposite odds | 4.10 |
| Market reference under 3 5 last update utc | 2026-10-22T15:06:17Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.1% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:06:45Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-22T15:06:45Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **64.0%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 59.5%; Under 3.5 goals: 62.9%; Double Chance 1X: 84.5%; Double Chance X2: 36.0%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 54.6%; BTTS No (at least one team does not score): 45.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 64.0% | 1.56 |
| Draw | 20.6% | 4.86 |
| Sassuolo win | 15.5% | 6.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 59.5% |
| Under 2.5 | 40.5% |
| Over 3.5 | 37.1% |
| Under 3.5 | 62.9% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.37% |
| 2 | 2-1 | 9.98% |
| 3 | 1-1 | 9.68% |
| 4 | 1-0 | 9.48% |
| 5 | 3-0 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 64.0% | 64.4% | 1.52 | -2.8% |
| Draw | 20.6% | 20.6% | 4.71 | -3.1% |
| Sassuolo win | 15.5% | 15.1% | 5.93 | -8.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | 08ffd99b2249c81d8a7410598f32b9b0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1169 |
| Dc lambda away | 0.9623 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.6% |
| P btts no | 45.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.37 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.43 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.04 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.1018043518226519, "-10": 1.0116986513842032e-08, "-11": 8.717766970763381e-10, "-12": 6.901835740213641e-11, "-13": 5.05296907267989e-12, "-14": 3.4400985533647265e-13, "-15": 2.1879643932403864e-14, "-16": 1.2984052750227975e-15, "-17": 6.563323411308854e-17, "-2": 0.03899804846177395, "-3": 0.010831216625181049, "-4": 0.0023782598758968388, "-5": 0.0004298419804691179, "-6": 6.585509840433332e-05, "-7": 8.743760466394179e-06, "-8": 1.0234463016301395e-06, "-9": 1.0705035455757047e-07, "0": 0.20580402393665992, "1": 0.23492061362272532, "10": 2.7702507172392774e-05, "11": 5.251114540010653e-06, "12": 9.145115295170697e-07, "13": 1.472819537623897e-07, "14": 2.2057287894826052e-08, "15": 3.0860276129136943e-09, "16": 4.0285444454484667e-10, "17": 4.479608124258691e-11, "2": 0.1947529905225887, "3": 0.1189862652170564, "4": 0.05747212172912731, "5": 0.022849940879651844, "6": 0.007700944363357627, "7": 0.002249216003813125, "8": 0.0005791303227242463, "9": 0.00013325321143221384} |
| Raw goal margin distribution | {"-1": 0.10438554954979683, "-10": 1.0373497577736202e-08, "-11": 8.938801532526652e-10, "-12": 7.076828286276915e-11, "-13": 5.181084541736223e-12, "-14": 3.527320508105602e-13, "-15": 2.2434391211650283e-14, "-16": 1.3313256824985032e-15, "-17": 6.72973314889355e-17, "-2": 0.03998682420908166, "-3": 0.011105836631443992, "-4": 0.0024385594493072068, "-5": 0.00044074040596031084, "-6": 6.752482103680282e-05, "-7": 8.965454080060846e-06, "-8": 1.0493952637356552e-06, "-9": 1.0976456202441255e-07, "0": 0.20601266051850287, "1": 0.23340522069081746, "10": 2.7523807726150946e-05, "11": 5.217241387136337e-06, "12": 9.086123268604478e-07, "13": 1.4633188800065312e-07, "14": 2.1915003837001495e-08, "15": 3.066120698998544e-09, "16": 4.0025576761975e-10, "17": 4.450711696718618e-11, "2": 0.19349670525772977, "3": 0.11821872531273103, "4": 0.05710138863037108, "5": 0.0227025436871724, "6": 0.007651268192002185, "7": 0.002234707076810293, "8": 0.0005753945500980124, "9": 0.00013239364031308377} |
| Unadjusted home-win probability | 63.6% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 54.7% |
| P home draw | 84.5% |
| P draw away | 36.0% |
| P home away | 79.4% |
| Raw p home draw | 84.2% |
| Raw p draw away | 36.4% |
| Raw p home away | 79.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.71, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.21, "price": 4.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.44, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:33Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.52 |
| Reference draw odds | 4.50 |
| Reference away odds | 6.05 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:39Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:39Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.0% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | -0.0083 |
| Raw ev home | -0.0340 |
| Raw edge prob draw | 0.0004 |
| Raw ev draw | -0.0297 |
| Raw edge prob away | 0.0078 |
| Raw ev away | -0.0605 |
| Market p home draw | 84.2% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:06:26Z |
| Market reference home draw last update utc | 2026-10-22T15:06:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 37.1% |
| Market draw away odds | 2.65 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:06:26Z |
| Market reference draw away last update utc | 2026-10-22T15:06:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.7% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:06:26Z |
| Market reference home away last update utc | 2026-10-22T15:06:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.59 |
| Market reference dc home draw odds | 1.14 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T15:06:33Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-22T15:06:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.8% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:06:18Z |
| Market reference under 3 5 odds | 1.77 |
| Market reference under 3 5 opposite odds | 2.22 |
| Market reference under 3 5 last update utc | 2026-10-22T15:06:33Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 61.2% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:06:26Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-22T15:06:39Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **64.3%**. Expected goals are 1.60 for Lazio and 0.71 for Parma (2.31 combined). The most likely exact score is 1-0 at 17.1%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 42.1%; Under 3.5 goals: 79.1%; Double Chance 1X: 86.7%; Double Chance X2: 35.7%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 64.3% | 1.56 |
| Draw | 22.4% | 4.46 |
| Parma win | 13.3% | 7.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.60 |
| Parma expected goals | 0.71 |
| Expected total goals | 2.31 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 42.1% |
| Under 2.5 | 57.9% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.07% |
| 2 | 2-0 | 14.01% |
| 3 | 1-1 | 10.20% |
| 4 | 2-1 | 9.90% |
| 5 | 0-0 | 9.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 64.3% | 70.1% | 1.41 | -9.3% |
| Draw | 22.4% | 19.3% | 4.79 | +7.3% |
| Parma win | 13.3% | 10.7% | 8.40 | +11.7% |
| Over 2.5 | 42.1% | 51.3% | 1.88 | -20.9% |
| Under 2.5 | 57.9% | 48.7% | 2.01 | +16.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | b27cb3ea731fa3f18d05e6a627bdf984 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6029 |
| Dc lambda away | 0.7068 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.06 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.79 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.22 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.09556245046985364, "-10": 7.877746624729389e-10, "-11": 5.0189242267618233e-11, "-12": 2.9348898626070005e-12, "-13": 1.5857158335597004e-13, "-14": 7.94300146116644e-15, "-15": 3.4798371530045524e-16, "-2": 0.029734582572570056, "-3": 0.006429735907838337, "-4": 0.0010772526332823887, "-5": 0.0001468733831933657, "-6": 1.6855504347611983e-05, "-7": 1.668643862615207e-06, "-8": 1.451652032487966e-07, "-9": 1.125973699752432e-08, "0": 0.22404858415492657, "1": 0.29029948612965606, "10": 3.7283592524231948e-06, "11": 5.386898079400915e-07, "12": 7.14384960587467e-08, "13": 8.75342938977019e-09, "14": 9.943742919566867e-10, "15": 9.879535841036477e-11, "2": 0.20113080378103465, "3": 0.09863300246304452, "4": 0.03747650287519183, "5": 0.011587692649924354, "6": 0.0030158379077163447, "7": 0.0006770835685348884, "8": 0.00013358371609912826, "9": 2.349803876234499e-05} |
| Raw goal margin distribution | {"-1": 0.11440692270209227, "-10": 9.431201740126996e-10, "-11": 6.00863281797003e-11, "-12": 3.5136365381961048e-12, "-13": 1.898411645008817e-13, "-14": 9.50932452780652e-15, "-15": 4.1660449080389766e-16, "-2": 0.03559810441478952, "-3": 0.007697650022432019, "-4": 0.0012896818587280032, "-5": 0.00017583613349574987, "-6": 2.0179331667623556e-05, "-7": 1.9976926969632473e-06, "-8": 1.7379110838474944e-07, "-9": 1.3480104936488936e-08, "0": 0.2555185817434857, "1": 0.2642526193334776, "10": 3.3938354883239588e-06, "11": 4.903563373613398e-07, "12": 6.502873965245934e-08, "13": 7.96803561465594e-09, "14": 9.051549306913615e-10, "15": 8.993103152193837e-11, "2": 0.18308451880637538, "3": 0.08978324281960294, "4": 0.03411395652214475, "5": 0.010547997089482222, "6": 0.002745244496379512, "7": 0.0006163328391600774, "8": 0.00012159803432696523, "9": 2.1389697842509955e-05} |
| Unadjusted home-win probability | 58.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 15.9% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 79.7% |
| Raw p btts yes | 40.9% |
| P home draw | 86.7% |
| P draw away | 35.7% |
| P home away | 77.6% |
| Raw p home draw | 84.1% |
| Raw p draw away | 41.5% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.26, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.74, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.40 |
| Reference draw odds | 4.75 |
| Reference away odds | 8.30 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:18Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:18Z |
| Home probability edge | -5.8% |
| Draw probability edge | +3.1% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | -0.1154 |
| Raw ev home | -0.1747 |
| Raw edge prob draw | 0.0629 |
| Raw ev draw | 0.2239 |
| Raw edge prob away | 0.0524 |
| Raw ev away | 0.3372 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.4%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.26 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.7%; Double Chance 1X: 64.9%; Double Chance X2: 63.6%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.4% | 2.75 |
| Draw | 28.5% | 3.51 |
| AS Roma win | 35.1% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.20 |
| AS Roma expected goals | 1.06 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.28% |
| 2 | 0-1 | 11.71% |
| 3 | 1-0 | 11.30% |
| 4 | 0-0 | 10.50% |
| 5 | 1-2 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 36.4% | 33.9% | 2.83 | +2.9% |
| Draw | 28.5% | 27.6% | 3.45 | -1.6% |
| AS Roma win | 35.1% | 38.5% | 2.56 | -10.1% |
| Over 2.5 | 39.7% | 50.7% | 1.92 | -23.8% |
| Under 2.5 | 60.3% | 49.3% | 1.97 | +18.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:00:00+00:00 |
| Fixture id | 0b4894e9fb123ef3045269f97e339eba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2023 |
| Dc lambda away | 1.0610 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.52 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.49 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.21330455135320364, "-10": 6.430744745693285e-08, "-11": 6.143139782397941e-09, "-12": 5.366251959398352e-10, "-13": 3.988422801498965e-11, "-2": 0.09702700199963891, "-3": 0.03119163818518061, "-4": 0.007796245661250999, "-5": 0.0015887961435344423, "-6": 0.0002728534987558736, "-7": 4.04522011092964e-05, "-8": 5.272979109660545e-06, "-9": 6.130509926310639e-07, "0": 0.28514199695146664, "1": 0.20550700477419198, "10": 1.9031833001461312e-07, "11": 2.060133876723711e-08, "12": 2.039209312722312e-09, "13": 1.7174244274254576e-10, "2": 0.10563950630518025, "3": 0.03848199992959927, "4": 0.010899100691967185, "5": 0.0025168598108917094, "6": 0.0004897856712154744, "7": 8.228191784448234e-05, "8": 1.215357368485985e-05, "9": 1.6011434649148343e-06} |
| Raw goal margin distribution | {"-1": 0.19293700032187494, "-10": 5.816700080699362e-08, "-11": 5.556557301073421e-09, "-12": 4.853851216251376e-10, "-13": 3.6075851474090996e-11, "-2": 0.08776230322923079, "-3": 0.028213280346789053, "-4": 0.00705181507901101, "-5": 0.0014370887077271655, "-6": 0.0002467998701542757, "-7": 3.6589591215619645e-05, "-8": 4.769484597134624e-06, "-9": 5.545133416620313e-07, "0": 0.29441546848255246, "1": 0.21921974993259638, "10": 2.0301758939670133e-07, "11": 2.197599219448884e-08, "12": 2.1752784343599497e-09, "13": 1.832021998092117e-10, "2": 0.1126884515721034, "3": 0.041049765728143006, "4": 0.011626358579886658, "5": 0.0026848008366689596, "6": 0.0005224673119167033, "7": 8.777229503033997e-05, "8": 1.296453805508896e-05, "9": 1.7079820241189196e-06} |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.8% |
| Raw p over 1 5 | 66.5% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 46.2% |
| P home draw | 64.9% |
| P draw away | 63.6% |
| P home away | 71.5% |
| Raw p home draw | 68.2% |
| Raw p draw away | 61.2% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.09, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.82 |
| Reference draw odds | 3.44 |
| Reference away odds | 2.50 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:18Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:18Z |
| Home probability edge | +2.4% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0485 |
| Raw ev home | 0.0977 |
| Raw edge prob draw | 0.0185 |
| Raw ev draw | 0.0157 |
| Raw edge prob away | -0.0671 |
| Raw ev away | -0.1867 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **58.4%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.35 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.4%; Double Chance 1X: 79.9%; Double Chance X2: 41.6%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 58.4% | 1.71 |
| Draw | 21.5% | 4.65 |
| Frosinone win | 20.1% | 4.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.35 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 42.6% |
| Under 3.5 | 57.4% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.70% |
| 2 | 2-1 | 9.08% |
| 3 | 2-0 | 8.20% |
| 4 | 1-0 | 7.03% |
| 5 | 3-1 | 6.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 58.4% | 54.0% | 1.84 | +7.5% |
| Draw | 21.5% | 23.1% | 4.20 | -9.6% |
| Frosinone win | 20.1% | 22.8% | 3.95 | -20.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 63aa6e3f679ee4c68de5b4bd8d3361bb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2476 |
| Dc lambda away | 1.1074 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.47 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.55 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.13 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.1259082130049323, "-10": 3.873255934667625e-08, "-11": 3.8281271430470296e-09, "-12": 3.477864061581431e-10, "-13": 2.9230003134310454e-11, "-14": 2.2851698751465947e-12, "-15": 1.6691059725157073e-13, "-16": 1.1348625747456223e-14, "-17": 6.4483138427602785e-16, "-2": 0.05303872502368029, "-3": 0.01650801598298358, "-4": 0.004097318967731029, "-5": 0.0008413930225995676, "-6": 0.00014693953253663413, "-7": 2.2286816164335568e-05, "-8": 2.9845034823930153e-06, "-9": 3.5754216089755117e-07, "0": 0.21523974950211455, "1": 0.20768548517291696, "10": 3.6847863179837125e-05, "11": 7.391851952913249e-06, "12": 1.3630453417792965e-06, "13": 2.3251841588119428e-07, "14": 3.6895871859971134e-08, "15": 5.469832051639483e-09, "16": 7.548560640765755e-10, "17": 8.705582473990006e-11, "2": 0.17517932182044196, "3": 0.11066631252451077, "4": 0.055750802889337814, "5": 0.02323705317200056, "6": 0.008236668605485869, "7": 0.0025356643414748093, "8": 0.0006892021380001776, "9": 0.00016758401077226608} |
| Raw goal margin distribution | {"-1": 0.10850140132230696, "-10": 3.337778263717525e-08, "-11": 3.298888527981023e-09, "-12": 2.997049320962827e-10, "-13": 2.5188954914353917e-11, "-14": 1.9692451174985215e-12, "-15": 1.4383520554476603e-13, "-16": 9.779678126582396e-15, "-17": 5.556834390764584e-16, "-2": 0.04570612076904295, "-3": 0.01422578261145358, "-4": 0.0035308645802626846, "-5": 0.0007250704289742269, "-6": 0.00012662514072251166, "-7": 1.9205663611065015e-05, "-8": 2.571895846685251e-06, "-9": 3.081119536472998e-07, "0": 0.19923353210160638, "1": 0.22323344144395288, "10": 3.960640436977258e-05, "11": 7.945228087168269e-06, "12": 1.4650869907264002e-06, "13": 2.499254395801368e-07, "14": 3.965800712321766e-08, "15": 5.879320030435854e-09, "16": 8.113668455855347e-10, "17": 9.35730840229356e-11, "2": 0.18829376952961263, "3": 0.11895112350383993, "4": 0.05992447465401057, "5": 0.02497664843685595, "6": 0.008853290239831111, "7": 0.0027254917541437843, "8": 0.0007407978703384748, "9": 0.00018012985079109367} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 60.2% |
| P home draw | 79.9% |
| P draw away | 41.6% |
| P home away | 78.5% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.80 |
| Reference draw odds | 4.05 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:39Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:39Z |
| Home probability edge | +4.4% |
| Draw probability edge | -1.6% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | 0.0875 |
| Raw ev home | 0.1554 |
| Raw edge prob draw | -0.0320 |
| Raw ev draw | -0.1632 |
| Raw edge prob away | -0.0555 |
| Raw ev away | -0.3173 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **47.2%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.6%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 39.0%; Under 3.5 goals: 80.9%; Double Chance 1X: 75.9%; Double Chance X2: 52.8%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 44.0%; BTTS No (at least one team does not score): 56.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 47.2% | 2.12 |
| Draw | 28.7% | 3.48 |
| Venezia win | 24.1% | 4.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.64% |
| 2 | 1-1 | 13.23% |
| 3 | 0-0 | 11.09% |
| 4 | 2-0 | 9.82% |
| 5 | 0-1 | 9.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 47.2% | 45.2% | 2.16 | +1.9% |
| Draw | 28.7% | 29.2% | 3.22 | -7.5% |
| Venezia win | 24.1% | 25.5% | 3.83 | -7.7% |
| Over 2.5 | 39.0% | 48.0% | 2.02 | -21.2% |
| Under 2.5 | 61.0% | 52.0% | 1.87 | +14.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 95cfaecfe96bb7ced1fb6af974a4110b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3977 |
| Dc lambda away | 0.8590 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.0% |
| P btts no | 56.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.01 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.83 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.16127561567733267, "-10": 7.485189680179776e-09, "-11": 5.793223996103915e-10, "-12": 4.115317043559311e-11, "-13": 2.693217437793455e-12, "-14": 1.5220276856405297e-13, "-2": 0.06019688456079948, "-3": 0.015747627082602293, "-4": 0.0031972170346707945, "-5": 0.000528723714799654, "-6": 7.363761730917611e-05, "-7": 8.850141410247037e-06, "-8": 9.349415256511647e-07, "-9": 8.807681537102863e-08, "0": 0.2872103058437041, "1": 0.23945278183014967, "10": 8.786003266604567e-07, "11": 1.1063853061515709e-07, "12": 1.2787537060491385e-08, "13": 1.3616094360287489e-09, "14": 1.2519910237188826e-10, "2": 0.14387400736469294, "3": 0.06123799668660294, "4": 0.020229050544468264, "5": 0.005442891783511935, "6": 0.0012333835880899136, "7": 0.00024118271283747608, "8": 4.145509774029128e-05, "9": 6.354079223606582e-06} |
| Raw goal margin distribution | {"-1": 0.15165164826148242, "-10": 7.038518177603498e-09, "-11": 5.447518920125329e-10, "-12": 3.869739452881576e-11, "-13": 2.5325022747710342e-12, "-14": 1.4312021458271658e-13, "-2": 0.056604693310338454, "-3": 0.014807902566385636, "-4": 0.0030064261799352906, "-5": 0.0004971726351038886, "-6": 6.924336324548529e-05, "-7": 8.32201772459147e-06, "-8": 8.791497883770423e-07, "-9": 8.282091603582759e-08, "0": 0.28200881419534585, "1": 0.24939345079782801, "10": 9.150746366913207e-07, "11": 1.1523159067280034e-07, "12": 1.3318400272264099e-08, "13": 1.4181354390401903e-09, "14": 1.3039663159755505e-10, "2": 0.1498468086382243, "3": 0.06378023757707256, "4": 0.0210688415607014, "5": 0.005668848588161497, "6": 0.0012845864092292647, "7": 0.0002511951983501506, "8": 4.3176069200757735e-05, "9": 6.617863163277326e-06} |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 66.3% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.8% |
| P home draw | 75.9% |
| P draw away | 52.8% |
| P home away | 71.3% |
| Raw p home draw | 77.3% |
| Raw p draw away | 50.9% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.69, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.14 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.70 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.84 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:18Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:18Z |
| Home probability edge | +2.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | 0.0392 |
| Raw ev home | 0.0613 |
| Raw edge prob draw | -0.0104 |
| Raw ev draw | -0.0919 |
| Raw edge prob away | -0.0288 |
| Raw ev away | -0.1319 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **70.6%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.34 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.2%; Under 3.5 goals: 56.9%; Double Chance 1X: 87.9%; Double Chance X2: 29.4%; Double Chance 12 (either team wins): 82.7%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.6% | 1.42 |
| Draw | 17.3% | 5.78 |
| Fiorentina win | 12.1% | 8.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 65.2% |
| Under 2.5 | 34.8% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.37% |
| 2 | 2-1 | 9.73% |
| 3 | 1-0 | 8.35% |
| 4 | 3-0 | 8.32% |
| 5 | 1-1 | 8.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.6% | 71.7% | 1.35 | -4.7% |
| Draw | 17.3% | 16.8% | 5.75 | -0.4% |
| Fiorentina win | 12.1% | 11.5% | 8.03 | -2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T11:30:00+00:00 |
| Fixture id | c9b6c7048d8dc33dae618f67f462f67a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4052 |
| Dc lambda away | 0.9383 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.11 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.69 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.87 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.05 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.0811702533276145, "-10": 6.032903046652747e-09, "-11": 5.060700530745887e-10, "-12": 3.901244246430634e-11, "-13": 2.7816350198018696e-12, "-14": 1.844627934431603e-13, "-15": 1.1431887276333492e-14, "-16": 6.64733203770219e-16, "-17": 3.61842054581158e-17, "-18": 1.6760421099142433e-18, "-2": 0.029727460686533806, "-3": 0.007945702138810252, "-4": 0.0016862649309709733, "-5": 0.0002953173250137407, "-6": 4.39114434573827e-05, "-7": 5.664444086194679e-06, "-8": 6.446393801237807e-07, "-9": 6.559414721401211e-08, "0": 0.17313496295644146, "1": 0.22517025341851948, "10": 7.847178895384986e-05, "11": 1.687389486089639e-05, "12": 3.3344586339345096e-06, "13": 6.094524551298111e-07, "14": 1.0360147996160422e-07, "15": 1.645858915556999e-08, "16": 2.453237169398441e-09, "17": 3.4231718093147797e-10, "18": 4.064546297938829e-11, "2": 0.20739824625292974, "3": 0.14210096902609257, "4": 0.0773050845908922, "5": 0.03470473001628579, "6": 0.013228023274927638, "7": 0.004374133400261802, "8": 0.001276054004274436, "9": 0.000332839457224225} |
| Raw goal margin distribution | {"-1": 0.08487139691842309, "-10": 6.30798707718998e-09, "-11": 5.291454761101352e-10, "-12": 4.0791304121985e-11, "-13": 2.908470038832246e-12, "-14": 1.9287379695375966e-13, "-15": 1.1953150357192371e-14, "-16": 6.950432365207858e-16, "-17": 3.783410717247013e-17, "-18": 1.7524650882681133e-18, "-2": 0.031082952336250618, "-3": 0.008308004624510723, "-4": 0.001763154042262502, "-5": 0.0003087829947624575, "-6": 4.5913686284684e-05, "-7": 5.9227273866113444e-06, "-8": 6.740331889677439e-07, "-9": 6.858506257528158e-08, "0": 0.17834781259217433, "1": 0.22174977338984153, "10": 7.727975233775038e-05, "11": 1.6617569615880875e-05, "12": 3.2838060766332277e-06, "13": 6.001944829085621e-07, "14": 1.020277072817312e-07, "15": 1.6208572669590353e-08, "16": 2.415970929226205e-09, "17": 3.371171642193542e-10, "18": 4.002803242510029e-11, "2": 0.20424773436905122, "3": 0.13994236450693295, "4": 0.07613077095956661, "5": 0.03417754299171587, "6": 0.0130270811489414, "7": 0.004307687518928802, "8": 0.0012566699285767348, "9": 0.0003277834131912887} |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 55.6% |
| P home draw | 87.9% |
| P draw away | 29.4% |
| P home away | 82.7% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.9, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.37 |
| Reference draw odds | 5.40 |
| Reference away odds | 7.70 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:39Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:39Z |
| Home probability edge | -1.1% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | -0.0214 |
| Raw ev home | -0.0614 |
| Raw edge prob draw | 0.0104 |
| Raw ev draw | 0.0255 |
| Raw edge prob away | 0.0110 |
| Raw ev away | 0.0149 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **62.4%**. Expected goals are 0.62 for Lecce and 1.48 for Juventus (2.11 combined). The most likely exact score is 0-1 at 19.1%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 36.5%; Under 3.5 goals: 83.3%; Double Chance 1X: 37.6%; Double Chance X2: 86.4%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 35.4%; BTTS No (at least one team does not score): 64.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.6% | 7.37 |
| Draw | 24.0% | 4.17 |
| Juventus win | 62.4% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.11 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 63.4% |
| Under 1.5 | 36.6% |
| Over 2.5 | 36.5% |
| Under 2.5 | 63.5% |
| Over 3.5 | 16.7% |
| Under 3.5 | 83.3% |
| Over 4.5 | 6.6% |
| Under 4.5 | 93.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.09% |
| 2 | 0-2 | 14.46% |
| 3 | 0-0 | 11.13% |
| 4 | 1-1 | 10.32% |
| 5 | 1-2 | 9.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.6% | 11.9% | 8.05 | +9.3% |
| Draw | 24.0% | 21.0% | 4.31 | +3.5% |
| Juventus win | 62.4% | 67.1% | 1.47 | -8.3% |
| Over 2.5 | 36.5% | 51.3% | 1.92 | -30.0% |
| Under 2.5 | 63.5% | 48.7% | 2.02 | +28.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:00:00+00:00 |
| Fixture id | 63af660d4d0d52f8ac7685172ef939c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6239 |
| Dc lambda away | 1.4832 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.4% |
| P btts no | 64.6% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.99 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.73 |
| Fair Over 2.5 odds | 2.74 |
| Fair Under 2.5 odds | 1.57 |
| Fair Over 3.5 odds | 5.98 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.19 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.29610719346809167, "-10": 2.029530841639021e-06, "-11": 2.717610188889455e-07, "-12": 3.339260839848683e-08, "-13": 3.790517261653995e-09, "-14": 3.9915567260719434e-10, "-15": 3.717531238766737e-11, "-2": 0.1946683795973423, "-3": 0.08962991356302294, "-4": 0.03180639405831374, "-5": 0.009158569258454026, "-6": 0.0022159643227469454, "-7": 0.00046199390512724784, "-8": 8.457778435091287e-05, "-9": 1.3797752149492093e-05, "0": 0.24007915286024556, "1": 0.10089122385855233, "10": 2.904848459364399e-10, "11": 1.636069314145288e-11, "12": 8.455739460873377e-13, "13": 4.0372573954327257e-14, "14": 1.788203650644657e-15, "15": 7.005126941715751e-17, "2": 0.028439997076217215, "3": 0.005507744971479095, "4": 0.0008220949715263939, "5": 9.956848566564017e-05, "6": 1.0133133012856222e-05, "7": 8.885951472940536e-07, "8": 6.84243540905053e-08, "9": 4.6951498036208076e-09} |
| Raw goal margin distribution | {"-1": 0.27391305196386756, "-10": 1.8774112860181022e-06, "-11": 2.5139169777279585e-07, "-12": 3.0889730074894124e-08, "-13": 3.5064063777067663e-09, "-14": 3.692377318226438e-10, "-15": 3.4388908808841333e-11, "-2": 0.18007738802912493, "-3": 0.08291187689079511, "-4": 0.029422407360113517, "-5": 0.008472106428160544, "-6": 0.002049871006433583, "-7": 0.0004273660462617113, "-8": 7.823842024424456e-05, "-9": 1.2763568345784404e-05, "0": 0.27053865783885306, "1": 0.11302029813228294, "10": 3.2540673643403055e-10, "11": 1.832756453713152e-11, "12": 9.472282704555658e-13, "13": 4.522613732075289e-14, "14": 2.003180276615943e-15, "15": 7.847278535516437e-17, "2": 0.03185903417071946, "3": 0.006169882323817035, "4": 0.0009209266695508287, "5": 0.00011153854125396933, "6": 1.1351331367857206e-05, "7": 9.954214511945444e-07, "8": 7.665028337509124e-08, "9": 5.25959751786648e-09} |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 57.7% |
| Raw p over 1 5 | 62.6% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 37.6% |
| P draw away | 86.4% |
| P home away | 76.0% |
| Raw p home draw | 42.3% |
| Raw p draw away | 84.8% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.87, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.05, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 7.50 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.46 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:24Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:24Z |
| Home probability edge | +1.6% |
| Draw probability edge | +3.0% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -14.8% |
| Under 2.5 probability edge | +14.8% |
| Raw edge prob home | 0.0326 |
| Raw ev home | 0.2244 |
| Raw edge prob draw | 0.0609 |
| Raw ev draw | 0.1660 |
| Raw edge prob away | -0.0936 |
| Raw ev away | -0.1513 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **55.7%**. Expected goals are 1.04 for Udinese and 1.69 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 52.0%; Under 3.5 goals: 70.3%; Double Chance 1X: 44.3%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 20.4% | 4.91 |
| Draw | 24.0% | 4.17 |
| AC Milan win | 55.7% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.69 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 52.0% |
| Under 2.5 | 48.0% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.41% |
| 2 | 0-1 | 11.28% |
| 3 | 1-2 | 10.34% |
| 4 | 0-2 | 9.90% |
| 5 | 0-0 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 20.4% | 17.8% | 5.21 | +6.1% |
| Draw | 24.0% | 23.1% | 4.03 | -3.4% |
| AC Milan win | 55.7% | 59.2% | 1.68 | -6.5% |
| Over 2.5 | 52.0% | 51.0% | 1.90 | -1.2% |
| Under 2.5 | 48.0% | 49.0% | 1.99 | -4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 3564688383b255192409c9deb8e526ed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0448 |
| Dc lambda away | 1.6924 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.12 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.25 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.90 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.25163229681537047, "-10": 4.306298202538642e-06, "-11": 6.538759050497711e-07, "-12": 9.119297874195545e-08, "-13": 1.1755707065252447e-08, "-14": 1.401199835861168e-09, "-15": 1.4142058345618723e-10, "-2": 0.17182948160071734, "-3": 0.08533111789798822, "-4": 0.03331568246523332, "-5": 0.010672250692202042, "-6": 0.0028921421467209473, "-7": 0.0006783171857308879, "-8": 0.00014012089542884482, "-9": 2.584881343834014e-05, "0": 0.239743516052657, "1": 0.12770483691116588, "10": 2.8759585836022635e-08, "11": 2.6959345515752398e-09, "12": 2.3211910963286743e-10, "13": 1.847284275345461e-11, "14": 1.3593163455033014e-12, "15": 8.469710570772848e-14, "2": 0.054386653632632134, "3": 0.016673914754976565, "4": 0.004018966067011102, "5": 0.0007947986617086607, "6": 0.00013297078323835953, "7": 1.925328752366023e-05, "8": 2.4553333553624903e-06, "9": 2.796299309287524e-07} |
| Raw goal margin distribution | {"-1": 0.2357746045052883, "-10": 4.03491828527221e-06, "-11": 6.126691003490863e-07, "-12": 8.544606065539982e-08, "-13": 1.1014870583260582e-08, "-14": 1.312897196878672e-09, "-15": 1.32508356658822e-10, "-2": 0.16100090719468882, "-3": 0.07995361020431374, "-4": 0.03121615133063616, "-5": 0.009999692877188437, "-6": 0.0027098813604063353, "-7": 0.0006355701085230143, "-8": 0.00013129057406690076, "-9": 2.4219839195869706e-05, "0": 0.248685407284834, "1": 0.14408351650920156, "10": 3.244812303769566e-08, "11": 3.0416994364890413e-09, "12": 2.6188935653355985e-10, "13": 2.0842062119313062e-11, "14": 1.5336543536310484e-12, "15": 9.555986385237757e-14, "2": 0.06136196949226456, "3": 0.018812414079060064, "4": 0.004534415278795791, "5": 0.0008967349151814182, "6": 0.00015002484248339765, "7": 2.172260219635543e-05, "8": 2.77024013028619e-06, "9": 3.1549363942625286e-07} |
| Unadjusted home-win probability | 23.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 53.3% |
| P home draw | 44.3% |
| P draw away | 79.6% |
| P home away | 76.0% |
| Raw p home draw | 47.9% |
| Raw p draw away | 77.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.20 |
| Reference draw odds | 4.05 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:18Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:18Z |
| Home probability edge | +2.6% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | 0.0523 |
| Raw ev home | 0.1976 |
| Raw edge prob draw | 0.0179 |
| Raw ev draw | 0.0022 |
| Raw edge prob away | -0.0701 |
| Raw ev away | -0.1240 |

</details>


---

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **69.0%**. Expected goals are 1.92 for AS Roma and 0.71 for Cagliari (2.63 combined). The most likely exact score is 1-0 at 14.2%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 49.8%; Under 3.5 goals: 72.4%; Double Chance 1X: 88.8%; Double Chance X2: 31.0%; Double Chance 12 (either team wins): 80.1%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 43.1%; BTTS No (at least one team does not score): 56.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 69.0% | 1.45 |
| Draw | 19.9% | 5.04 |
| Cagliari win | 11.2% | 8.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.92 |
| Cagliari expected goals | 0.71 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.15% |
| 2 | 2-0 | 13.93% |
| 3 | 2-1 | 9.89% |
| 4 | 1-1 | 9.34% |
| 5 | 3-0 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 69.0% | 72.2% | 1.34 | -7.6% |
| Draw | 19.9% | 18.1% | 4.80 | -4.7% |
| Cagliari win | 11.2% | 9.7% | 9.84 | +10.1% |
| Over 2.5 | 49.8% | 55.7% | 1.78 | -11.3% |
| Under 2.5 | 50.2% | 44.3% | 2.21 | +10.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7eecf109ae6a5f87441a79b0e4111982 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9214 |
| Dc lambda away | 0.7103 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 43.1% |
| P btts no | 56.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.44 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.95 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.63 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.66 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.0809132107684967, "-10": 6.480491944349798e-10, "-11": 4.142258866625057e-11, "-12": 2.4308143027574077e-12, "-13": 1.3183616257212834e-13, "-14": 6.6453657587603e-15, "-15": 3.119370457822851e-16, "-16": 1.2759947762861182e-17, "-2": 0.024697301534457185, "-3": 0.005283579419497587, "-4": 0.000880692188316667, "-5": 0.00011983008400021531, "-6": 1.3749826966394134e-05, "-7": 1.3626437222212373e-06, "-8": 1.1877017823388689e-07, "-9": 9.235453685409575e-09, "0": 0.19853627475721253, "1": 0.2657230603082371, "10": 1.6131101732411403e-05, "11": 2.7890064877929963e-06, "12": 4.4271099144123086e-07, "13": 6.494703184473057e-08, "14": 8.855230645890089e-09, "15": 1.1243568656255506e-09, "16": 1.2440629347973765e-10, "2": 0.2145140256586785, "3": 0.12413397486560362, "4": 0.05596838814307712, "5": 0.020598744580126845, "6": 0.0063933481535545225, "7": 0.0017138376330214221, "8": 0.00040406477959432544, "9": 8.498808752632493e-05} |
| Raw goal margin distribution | {"-1": 0.09158956692542622, "-10": 7.335581483040177e-10, "-11": 4.688822654345949e-11, "-12": 2.7515559838884302e-12, "-13": 1.4923171284895563e-13, "-14": 7.522210107905974e-15, "-15": 3.5309659151877406e-16, "-16": 1.4443600476259163e-17, "-2": 0.027956067127771267, "-3": 0.00598073845113426, "-4": 0.0009968979769362338, "-5": 0.00013564145328033775, "-6": 1.556409250344452e-05, "-7": 1.5424421699068945e-06, "-8": 1.344416948082938e-07, "-9": 1.0454055590831057e-08, "0": 0.21581582527381946, "1": 0.25337402678596377, "10": 1.5381435836596133e-05, "11": 2.659392089360124e-06, "12": 4.22136740686912e-07, "13": 6.192872747742279e-08, "14": 8.443698654776068e-09, "15": 1.0721042662143364e-09, "16": 1.186247196608114e-10, "2": 0.2045448461272371, "3": 0.11836505659750074, "4": 0.053367351181645414, "5": 0.019641452476680265, "6": 0.00609622802187974, "7": 0.001634189903699906, "8": 0.0003852865467130986, "9": 8.103840871170094e-05} |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 43.7% |
| P home draw | 88.8% |
| P draw away | 31.0% |
| P home away | 80.1% |
| Raw p home draw | 87.3% |
| Raw p draw away | 34.2% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.36 |
| Reference draw odds | 5.00 |
| Reference away odds | 9.00 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:24Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:24Z |
| Home probability edge | -3.2% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0641 |
| Raw ev home | -0.1189 |
| Raw edge prob draw | 0.0346 |
| Raw ev draw | 0.0359 |
| Raw edge prob away | 0.0295 |
| Raw ev away | 0.2465 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **43.9%**. Expected goals are 1.17 for Sassuolo and 1.67 for Lazio (2.84 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.4%; Under 3.5 goals: 68.6%; Double Chance 1X: 56.1%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 29.8% | 3.36 |
| Draw | 26.3% | 3.80 |
| Lazio win | 43.9% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.17 |
| Lazio expected goals | 1.67 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.42% |
| 2 | 1-2 | 8.60% |
| 3 | 0-1 | 8.47% |
| 4 | 2-1 | 7.55% |
| 5 | 0-2 | 7.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 29.8% | 33.2% | 2.94 | -12.5% |
| Draw | 26.3% | 27.6% | 3.30 | -13.2% |
| Lazio win | 43.9% | 39.2% | 2.47 | +8.5% |
| Over 2.5 | 53.4% | 54.5% | 1.82 | -2.9% |
| Under 2.5 | 46.6% | 45.5% | 2.15 | +0.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T17:30:00+00:00 |
| Fixture id | c7445242bf16a8f37afef7863af45a78 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sassuolo |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1681 |
| Dc lambda away | 1.6709 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.24 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.2036520716583532, "-10": 2.9399529879700404e-06, "-11": 4.401473758450382e-07, "-12": 6.053631677681856e-08, "-13": 7.69647121403398e-09, "-14": 9.03880168616369e-10, "-15": 8.909295117763162e-11, "-2": 0.13485231920762414, "-3": 0.06537005315955248, "-4": 0.025008983285933033, "-5": 0.007867605188231042, "-6": 0.0020967451476055746, "-7": 0.0004840552859002659, "-8": 9.84863105534085e-05, "-9": 1.7902840813620923e-05, "0": 0.2629127736077312, "1": 0.1773769755680024, "10": 1.0288502507019891e-07, "11": 1.0768242673285154e-08, "12": 1.0353749329219276e-09, "13": 9.20255109436896e-11, "14": 7.555485585105355e-12, "15": 5.206307362511898e-13, "2": 0.08271622750378996, "3": 0.028031482870206376, "4": 0.007497184629526344, "5": 0.0016488443607118404, "6": 0.00030719750715949636, "7": 4.9579477192957296e-05, "8": 7.052088919734534e-06, "9": 8.961873237556678e-07} |
| Raw goal margin distribution | {"-1": 0.22584029637500222, "-10": 3.2602656517316785e-06, "-11": 4.881021489252586e-07, "-12": 6.713184703204546e-08, "-13": 8.535014281293773e-09, "-14": 1.0023593843438072e-09, "-15": 9.87997732359657e-11, "-2": 0.14954469890096542, "-3": 0.07249222686214422, "-4": 0.027733752725126917, "-5": 0.008724793580555376, "-6": 0.0023251889445666148, "-7": 0.0005367938972552974, "-8": 0.00010921655440645741, "-9": 1.9853384462916145e-05, "0": 0.24968192771119269, "1": 0.1567282988972836, "10": 9.090804998574737e-08, "11": 9.514698009100386e-09, "12": 9.14845635619326e-10, "13": 8.13127055480116e-11, "14": 6.675942011665035e-12, "15": 4.600234578642176e-13, "2": 0.07308712749417469, "3": 0.024768302716557965, "4": 0.006624427943603359, "5": 0.0014569003162514355, "6": 0.0002714362592349853, "7": 4.3807867936556545e-05, "8": 6.2311463848285245e-06, "9": 7.918610309808024e-07} |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 48.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 56.3% |
| P home draw | 56.1% |
| P draw away | 70.2% |
| P home away | 73.7% |
| Raw p home draw | 51.3% |
| Raw p draw away | 73.7% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.13, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.88 |
| Reference draw odds | 3.44 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:24Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:24Z |
| Home probability edge | -3.5% |
| Draw probability edge | -1.3% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.0693 |
| Raw ev home | -0.2268 |
| Raw edge prob draw | -0.0265 |
| Raw ev draw | -0.1760 |
| Raw edge prob away | 0.0958 |
| Raw ev away | 0.2037 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **52.0%**. Expected goals are 0.94 for Torino and 1.48 for Como (2.41 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 43.8%; Under 3.5 goals: 77.4%; Double Chance 1X: 48.0%; Double Chance X2: 78.1%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 21.9% | 4.57 |
| Draw | 26.1% | 3.83 |
| Como win | 52.0% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 0.94 |
| Como expected goals | 1.48 |
| Expected total goals | 2.41 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 43.8% |
| Under 2.5 | 56.2% |
| Over 3.5 | 22.6% |
| Under 3.5 | 77.4% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.50% |
| 2 | 1-1 | 12.30% |
| 3 | 0-2 | 10.30% |
| 4 | 1-2 | 9.64% |
| 5 | 0-0 | 9.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 21.9% | 20.2% | 4.89 | +6.9% |
| Draw | 26.1% | 25.1% | 3.55 | -7.3% |
| Como win | 52.0% | 54.7% | 1.76 | -8.4% |
| Over 2.5 | 43.8% | 54.5% | 1.82 | -20.2% |
| Under 2.5 | 56.2% | 45.5% | 2.15 | +20.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7d989a0a7bae47eb957731e97c5bd9c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9359 |
| Dc lambda away | 1.4781 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.11 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.42 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.08 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.2563025400125152, "-10": 1.4656092174674856e-06, "-11": 1.949148686386048e-07, "-12": 2.3799327962980778e-08, "-13": 2.68541055583544e-09, "-14": 2.806609323837813e-10, "-15": 2.5321332271367915e-11, "-2": 0.15948075826213373, "-3": 0.07090996444542412, "-4": 0.024576056147386654, "-5": 0.006954543193358772, "-6": 0.0016598895969203529, "-7": 0.00034220439807001725, "-8": 6.2052721891795e-05, "-9": 1.0038814838266572e-05, "0": 0.2611026378291195, "1": 0.1419731588521352, "10": 1.3412661949415693e-08, "11": 1.129447024398854e-09, "12": 8.731918925096068e-11, "13": 6.2384945137318535e-12, "14": 4.128337307725657e-13, "15": 2.3583261557585097e-14, "2": 0.05649529022514055, "3": 0.01590506047119781, "4": 0.0034903128201592567, "5": 0.000625381277867046, "6": 9.451039422707773e-05, "7": 1.2337014165413663e-05, "8": 1.4164766430344253e-06, "9": 1.4509589650068465e-07} |
| Raw goal margin distribution | {"-1": 0.24321526631679574, "-10": 1.3907725460906448e-06, "-11": 1.8496216105672105e-07, "-12": 2.258409100586553e-08, "-13": 2.5482886103101385e-09, "-14": 2.66329874885783e-10, "-15": 2.402837900699736e-11, "-2": 0.15133738078145992, "-3": 0.06728917273416879, "-4": 0.02332115803694845, "-5": 0.006599431573334465, "-6": 0.001575132616133064, "-7": 0.0003247308193173347, "-8": 5.8884197089338374e-05, "-9": 9.526214700309963e-06, "0": 0.27150581179879035, "1": 0.15247141275641032, "10": 1.4404465835556088e-08, "11": 1.2129643718287046e-09, "12": 9.377603663594263e-11, "13": 6.699802129305831e-12, "14": 4.433608625271914e-13, "15": 2.532713391855944e-14, "2": 0.06067285382923666, "3": 0.017081165620505562, "4": 0.0037484051982371517, "5": 0.0006716253108596916, "6": 0.0001014989977293944, "7": 1.3249278907399456e-05, "8": 1.5212184940172457e-06, "9": 1.5582506231095638e-07} |
| Unadjusted home-win probability | 23.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.6% |
| Raw p btts yes | 47.3% |
| P home draw | 48.0% |
| P draw away | 78.1% |
| P home away | 73.9% |
| Raw p home draw | 50.6% |
| Raw p draw away | 76.5% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.60 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:24Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:24Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | 0.0323 |
| Raw ev home | 0.1480 |
| Raw edge prob draw | 0.0208 |
| Raw ev draw | -0.0362 |
| Raw edge prob away | -0.0531 |
| Raw ev away | -0.1310 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **55.7%**. Expected goals are 1.62 for AC Milan and 1.04 for Bologna (2.66 combined). The most likely exact score is 1-0 at 12.1%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.9%; Double Chance 1X: 79.7%; Double Chance X2: 44.3%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 55.7% | 1.80 |
| Draw | 24.0% | 4.16 |
| Bologna win | 20.3% | 4.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.62 |
| Bologna expected goals | 1.04 |
| Expected total goals | 2.66 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.08% |
| 2 | 1-1 | 11.44% |
| 3 | 2-1 | 10.55% |
| 4 | 2-0 | 10.12% |
| 5 | 0-0 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 55.7% | 61.0% | 1.62 | -9.8% |
| Draw | 24.0% | 22.4% | 4.03 | -3.2% |
| Bologna win | 20.3% | 16.5% | 5.26 | +6.8% |
| Over 2.5 | 50.4% | 52.5% | 1.84 | -7.3% |
| Under 2.5 | 49.6% | 47.5% | 2.00 | -0.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 3d0b0fbec194258530882514714c74be |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6166 |
| Dc lambda away | 1.0433 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.42 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.56 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.44 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.12690887031826217, "-10": 2.892286002014809e-08, "-11": 2.708958920563025e-09, "-12": 2.3302375242959117e-10, "-13": 1.852683037337473e-11, "-14": 1.3625155261634018e-12, "-15": 8.518903417211362e-14, "-2": 0.05441311880326402, "-3": 0.016744057570049407, "-4": 0.004043770293089094, "-5": 0.0008004620981193679, "-6": 0.00013396157053580988, "-7": 1.9395041695240356e-05, "-8": 2.4724913097314047e-06, "-9": 2.814219160402249e-07, "0": 0.24015759523081723, "1": 0.26048699052618174, "10": 3.028303823366597e-06, "11": 4.3949110847401803e-07, "12": 5.857837635060446e-08, "13": 7.216518483285697e-09, "14": 8.223515730933351e-10, "15": 7.966897446578699e-11, "2": 0.1714534037441822, "3": 0.08175092311377219, "4": 0.030592001991568488, "5": 0.009383214813979803, "6": 0.00243321553809093, "7": 0.0005458590724134687, "8": 0.00010782365606807224, "9": 1.9016328020652076e-05} |
| Raw goal margin distribution | {"-1": 0.1505151653766754, "-10": 3.4302795763461914e-08, "-11": 3.2128518590121753e-09, "-12": 2.7636845671760957e-10, "-13": 2.1973002600692403e-11, "-14": 1.6159567824886816e-12, "-15": 1.0103503036895137e-13, "-2": 0.0645344927804895, "-3": 0.019858616564092903, "-4": 0.004795951243464877, "-5": 0.0009493559021844032, "-6": 0.00015887973703296844, "-7": 2.300270974696823e-05, "-8": 2.932398952439994e-06, "-9": 3.3376915362329835e-07, "0": 0.2560022696847446, "1": 0.23540233003779243, "10": 2.736680916935087e-06, "11": 3.971685140846889e-07, "12": 5.293733193703206e-08, "13": 6.521574310850287e-09, "14": 7.43159863858759e-10, "15": 7.199692461832425e-11, "2": 0.15494259675987232, "3": 0.0738783835033333, "4": 0.02764601999811652, "5": 0.008479619753731866, "6": 0.0021988990927867273, "7": 0.000493293339751197, "8": 9.744033596590154e-05, "9": 1.718507291201756e-05} |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.3% |
| Raw p btts yes | 52.3% |
| P home draw | 79.7% |
| P draw away | 44.3% |
| P home away | 76.0% |
| Raw p home draw | 75.9% |
| Raw p draw away | 49.7% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.76, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.60 |
| Reference draw odds | 4.15 |
| Reference away odds | 5.55 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:18Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:18Z |
| Home probability edge | -5.4% |
| Draw probability edge | +1.6% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.1072 |
| Raw ev home | -0.1849 |
| Raw edge prob draw | 0.0317 |
| Raw ev draw | 0.0317 |
| Raw edge prob away | 0.0755 |
| Raw ev away | 0.2668 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **55.6%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.21 combined). The most likely exact score is 0-1 at 16.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 38.9%; Under 3.5 goals: 81.4%; Double Chance 1X: 44.4%; Double Chance X2: 81.5%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.5% | 5.41 |
| Draw | 25.9% | 3.86 |
| Juventus win | 55.6% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.21 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 18.6% |
| Under 3.5 | 81.4% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.26% |
| 2 | 0-2 | 11.96% |
| 3 | 1-1 | 11.77% |
| 4 | 0-0 | 10.54% |
| 5 | 1-2 | 9.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.5% | 16.9% | 5.59 | +3.3% |
| Draw | 25.9% | 24.0% | 3.81 | -1.2% |
| Juventus win | 55.6% | 59.1% | 1.63 | -9.4% |
| Over 2.5 | 38.9% | 46.5% | 2.12 | -17.5% |
| Under 2.5 | 61.1% | 53.5% | 1.75 | +6.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | 34848497b90b1392f6a767fc183d3ac1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7826 |
| Dc lambda away | 1.4324 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.49 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.37 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.11 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.27538056967436664, "-10": 1.2925859272451025e-06, "-11": 1.6690725013808557e-07, "-12": 1.9779944485458284e-08, "-13": 2.1601800467700432e-09, "-14": 2.0462821443651516e-10, "-2": 0.17102003650147077, "-3": 0.07500737876077014, "-4": 0.02548156851328646, "-5": 0.0070433467785818655, "-6": 0.0016385609849626592, "-7": 0.0003288076316256133, "-8": 5.798015263732783e-05, "-9": 9.11528596856966e-06, "0": 0.2592285049644672, "1": 0.1279609678345322, "10": 2.641332532742951e-09, "11": 1.8635058914413992e-10, "12": 1.2066256338562565e-11, "13": 7.199947672824582e-13, "14": 3.726463016553191e-14, "2": 0.04400229870341737, "3": 0.01054445820255551, "4": 0.001957214160565434, "5": 0.00029558553284194283, "6": 3.757150772994589e-05, "7": 4.119360625112282e-06, "8": 3.9687997780580093e-07, "9": 3.4091180833756244e-08} |
| Raw goal margin distribution | {"-1": 0.2578612441731747, "-10": 1.2103534239699273e-06, "-11": 1.5628884504459734e-07, "-12": 1.852157216730229e-08, "-13": 2.0227524227902703e-09, "-14": 1.9161005451448376e-10, "-2": 0.1601399817095226, "-3": 0.0702355145546099, "-4": 0.023860466873497296, "-5": 0.006595258937897753, "-6": 0.001534318033896578, "-7": 0.0003078893513978658, "-8": 5.429153666902159e-05, "-9": 8.535384263417928e-06, "0": 0.2786229733002302, "1": 0.139022709251076, "10": 2.8696657343961997e-09, "11": 2.0245989235446445e-10, "12": 1.3109338535748722e-11, "13": 7.822355901812191e-13, "14": 4.048601641987226e-14, "2": 0.047806130904969116, "3": 0.011455986709944197, "4": 0.0021264079179068806, "5": 0.0003211377835485563, "6": 4.081942238838894e-05, "7": 4.475463761932941e-06, "8": 4.311887499430075e-07, "9": 3.70382344028984e-08} |
| Unadjusted home-win probability | 20.1% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 41.7% |
| P home draw | 44.4% |
| P draw away | 81.5% |
| P home away | 74.1% |
| Raw p home draw | 47.9% |
| Raw p draw away | 79.9% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.45 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:18Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:18Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.9% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | 0.0320 |
| Raw ev home | 0.1223 |
| Raw edge prob draw | 0.0388 |
| Raw ev draw | 0.0616 |
| Raw edge prob away | -0.0707 |
| Raw ev away | -0.1514 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **56.6%**. Expected goals are 0.81 for Monza and 1.88 for Napoli (2.69 combined). The most likely exact score is 0-1 at 11.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.3%; Double Chance 1X: 43.4%; Double Chance X2: 80.3%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 19.7% | 5.07 |
| Draw | 23.6% | 4.23 |
| Napoli win | 56.6% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.81 |
| Napoli expected goals | 1.88 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.7% |
| Under 3.5 | 72.3% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 11.26% |
| 2 | 1-1 | 11.24% |
| 3 | 0-2 | 10.88% |
| 4 | 1-2 | 8.86% |
| 5 | 0-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 19.7% | 24.1% | 3.79 | -25.3% |
| Draw | 23.6% | 24.8% | 3.85 | -9.0% |
| Napoli win | 56.6% | 51.1% | 1.89 | +7.0% |
| Over 2.5 | 49.6% | 55.0% | 1.80 | -10.7% |
| Under 2.5 | 50.4% | 45.0% | 2.17 | +9.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | abec89862e33762414fcb8b2232aba08 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8150 |
| Dc lambda away | 1.8784 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.39 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.61 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.58 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.22700855041144383, "-10": 1.0668021504535942e-05, "-11": 1.8009867865045158e-06, "-12": 2.791914877188858e-07, "-13": 4.0005951712488866e-08, "-14": 5.328239925032824e-09, "-15": 6.604362374686746e-10, "-16": 7.076332576183599e-11, "-2": 0.176041469405086, "-3": 0.09851082007978906, "-4": 0.04311469523337584, "-5": 0.015436325663633227, "-6": 0.004666837701615405, "-7": 0.001219629516184737, "-8": 0.00028049766555549195, "-9": 5.757573042627776e-05, "0": 0.23647829232350298, "1": 0.13649572325761533, "10": 3.559415550221165e-09, "11": 2.607133806230935e-10, "12": 1.7535289938205098e-11, "13": 1.090167845217573e-12, "14": 6.299564368490901e-14, "15": 3.3877833060658006e-15, "16": 1.5748926224353987e-16, "2": 0.04677846071986329, "3": 0.011357241484229279, "4": 0.0021566130544973697, "5": 0.00033500309953840487, "6": 4.3942582239519205e-05, "7": 4.98251696676028e-06, "8": 4.971736405702491e-07, "9": 4.427680590185794e-08} |
| Raw goal margin distribution | {"-1": 0.24910431324972607, "-10": 1.1706388000822936e-05, "-11": 1.976284927642189e-06, "-12": 3.063664504589355e-07, "-13": 4.389991085877115e-08, "-14": 5.846861472615981e-09, "-15": 7.247194657720417e-10, "-16": 7.76510384089928e-11, "-2": 0.19317637710185537, "-3": 0.10809932110119368, "-4": 0.04731124236340617, "-5": 0.016938812641942812, "-6": 0.005121081997139744, "-7": 0.0013383415404293897, "-8": 0.0003077997644569328, "-9": 6.317983512821136e-05, "0": 0.2252508077955468, "1": 0.10610677169613937, "10": 2.76695917018729e-09, "11": 2.0266902504844503e-10, "12": 1.363129160162116e-11, "13": 8.474565202651471e-13, "14": 4.897050415059841e-14, "15": 2.6335385551551394e-15, "16": 1.2242637933739353e-16, "2": 0.036363860591671925, "3": 0.008828703204060317, "4": 0.0016764719329599893, "5": 0.0002604191292728829, "6": 3.415935261669349e-05, "7": 3.873226044352842e-06, "8": 3.8648456313727507e-07, "9": 3.44191658400594e-08} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 62.1% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.6% |
| Raw p btts yes | 47.6% |
| P home draw | 43.4% |
| P draw away | 80.3% |
| P home away | 76.4% |
| Raw p home draw | 37.9% |
| Raw p draw away | 84.7% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.90 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.90 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:24Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:24Z |
| Home probability edge | -4.4% |
| Draw probability edge | -1.1% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.0878 |
| Raw ev home | -0.4191 |
| Raw edge prob draw | -0.0225 |
| Raw ev draw | -0.1328 |
| Raw edge prob away | 0.1103 |
| Raw ev away | 0.1746 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **39.0%**. Expected goals are 1.05 for Parma and 1.17 for Udinese (2.22 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 38.3%; Under 3.5 goals: 81.6%; Double Chance 1X: 61.0%; Double Chance X2: 68.3%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 92.5%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.7% | 3.15 |
| Draw | 29.3% | 3.41 |
| Udinese win | 39.0% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.05 |
| Udinese expected goals | 1.17 |
| Expected total goals | 2.22 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 38.3% |
| Under 2.5 | 61.7% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.56% |
| 2 | 0-1 | 12.56% |
| 3 | 0-0 | 11.16% |
| 4 | 1-0 | 10.86% |
| 5 | 1-2 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.7% | 31.4% | 2.96 | -6.1% |
| Draw | 29.3% | 28.8% | 3.21 | -5.9% |
| Udinese win | 39.0% | 39.8% | 2.50 | -2.6% |
| Over 2.5 | 38.3% | 43.9% | 2.22 | -14.9% |
| Under 2.5 | 61.7% | 56.1% | 1.77 | +9.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 482c18a8081afdfa310324fa8f37e95a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0479 |
| Dc lambda away | 1.1680 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.96 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.61 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.43 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.39 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.22337248014308367, "-10": 1.6224004005667454e-07, "-11": 1.7068217034770793e-08, "-12": 1.64236761135873e-09, "-13": 1.3486619120086933e-10, "-2": 0.11224682989943612, "-3": 0.03986265186950482, "-4": 0.010993103448836859, "-5": 0.0024700759684436425, "-6": 0.0004675167114960138, "-7": 7.636899920547093e-05, "-8": 1.0966232811277609e-05, "-9": 1.4043223998727521e-06, "0": 0.2932272595020065, "1": 0.1934439724169455, "10": 5.304080058584967e-08, "11": 5.006315927343753e-09, "12": 4.321938057131447e-10, "13": 3.184119286243385e-11, "2": 0.08741813714865886, "3": 0.027852983400262408, "4": 0.006891343828984347, "5": 0.0013892230628702925, "6": 0.00023590485770884353, "7": 3.4572828678818986e-05, "8": 4.454032141752988e-06, "9": 5.117298827504906e-07} |
| Raw goal margin distribution | {"-1": 0.2184643270295078, "-10": 1.5867514720487486e-07, "-11": 1.6693177895980122e-08, "-12": 1.6062799442469941e-09, "-13": 1.3190278265638505e-10, "-2": 0.10978043552844183, "-3": 0.03898675167462238, "-4": 0.010751552498219717, "-5": 0.0024158011041115653, "-6": 0.0004572439885459528, "-7": 7.469094673906637e-05, "-8": 1.072527228792938e-05, "-9": 1.3734652891177272e-06, "0": 0.29834866443965885, "1": 0.19553960988830696, "10": 5.361540773349001e-08, "11": 5.060550872582586e-09, "12": 4.3687589284579836e-10, "13": 3.21861382027391e-11, "2": 0.08836516445375618, "3": 0.028154723252755663, "4": 0.00696599985561374, "5": 0.0014042729394327712, "6": 0.00023846048688308985, "7": 3.4947366661910716e-05, "8": 4.5022840285307646e-06, "9": 5.172736084303784e-07} |
| Unadjusted home-win probability | 32.1% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 45.2% |
| P home draw | 61.0% |
| P draw away | 68.3% |
| P home away | 70.7% |
| Raw p home draw | 61.9% |
| Raw p draw away | 67.9% |
| Raw p home away | 70.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.04 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.71 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:24Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:24Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | 0.0069 |
| Raw ev home | -0.0507 |
| Raw edge prob draw | 0.0102 |
| Raw ev draw | -0.0423 |
| Raw edge prob away | -0.0171 |
| Raw ev away | -0.0476 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **76.8%**. Expected goals are 0.69 for Venezia and 2.67 for Inter Milan (3.36 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 64.8%; Under 3.5 goals: 57.2%; Double Chance 1X: 23.2%; Double Chance X2: 91.2%; Double Chance 12 (either team wins): 85.6%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 8.8% | 11.34 |
| Draw | 14.4% | 6.95 |
| Inter Milan win | 76.8% | 1.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.69 |
| Inter Milan expected goals | 2.67 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.8% |
| Under 2.5 | 35.2% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.01% |
| 2 | 0-3 | 10.71% |
| 3 | 0-1 | 8.77% |
| 4 | 1-2 | 8.27% |
| 5 | 1-3 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 8.8% | 10.7% | 7.76 | -31.6% |
| Draw | 14.4% | 14.9% | 5.92 | -14.9% |
| Inter Milan win | 76.8% | 74.4% | 1.32 | +1.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 33320ad169692216a91dec030e7ef6a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6888 |
| Dc lambda away | 2.6747 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.26 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.52 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.84 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.08 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.20016727605499768, "-10": 0.00020480261921724887, "-11": 4.9121112881179934e-05, "-12": 1.0822167628469993e-05, "-13": 2.204500260828322e-06, "-14": 4.1753515896253884e-07, "-15": 7.388879759125806e-08, "-16": 1.226926421575585e-08, "-17": 1.9186372852507115e-09, "-18": 2.824347418607496e-10, "-19": 3.624501244311931e-11, "-2": 0.21313311096998513, "-3": 0.16650566836536798, "-4": 0.10242806790285398, "-5": 0.05174485109164351, "-6": 0.022126639094230193, "-7": 0.008191703601858655, "-8": 0.0026717831742078396, "-9": 0.0007783515746308601, "0": 0.14381465527302242, "1": 0.0653181492276077, "10": 3.431355314837412e-10, "11": 2.1193700148573335e-11, "12": 1.202433999957601e-12, "13": 6.307620398899004e-14, "14": 3.076499502891539e-15, "15": 1.4020089955751675e-16, "16": 5.995137153895731e-18, "17": 2.4142480389402253e-19, "18": 9.151989815162057e-21, "19": 3.024503329904345e-22, "2": 0.018463493724449172, "3": 0.0037145001913247186, "4": 0.000588435338187489, "5": 7.655178294587975e-05, "6": 8.429698156986867e-06, "7": 8.036726797998375e-07, "8": 6.7501681098274e-08, "9": 5.064045392685111e-09} |
| Raw goal margin distribution | {"-1": 0.2063213358919773, "-10": 0.00021109919075617916, "-11": 5.063132111245323e-05, "-12": 1.1154890681228774e-05, "-13": 2.2722767065249057e-06, "-14": 4.30372104156279e-07, "-15": 7.616047801085941e-08, "-16": 1.2646477652575206e-08, "-17": 1.977624992390458e-09, "-18": 2.91118080794609e-10, "-19": 3.735935030974313e-11, "-2": 0.21968580002086935, "-3": 0.17162481604280966, "-4": 0.10557717634497107, "-5": 0.05333572506539974, "-6": 0.022806913431078997, "-7": 0.008443554129708113, "-8": 0.0027539260391634115, "-9": 0.0008022816707928798, "0": 0.13880184752103022, "1": 0.051539331360035544, "10": 2.707513312558407e-10, "11": 1.6722903934345936e-11, "12": 9.487813891731349e-13, "13": 4.9770322900510305e-14, "14": 2.427514085801647e-15, "15": 1.1062561791349406e-16, "16": 4.730467166894177e-18, "17": 1.9049641047034533e-19, "18": 7.221383968545483e-21, "19": 2.3864864691173086e-22, "2": 0.014568632644694046, "3": 0.0029309289755056916, "4": 0.00046430531540506614, "5": 6.040323790713929e-05, "6": 6.65145923017665e-06, "7": 6.341384904351278e-07, "8": 5.326224871069899e-08, "9": 3.995788561099411e-09} |
| Unadjusted home-win probability | 7.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 79.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 46.6% |
| P home draw | 23.2% |
| P draw away | 91.2% |
| P home away | 85.6% |
| Raw p home draw | 20.8% |
| Raw p draw away | 93.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 8.20 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.32 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:39Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:39Z |
| Home probability edge | -1.9% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.0372 |
| Raw ev home | -0.4601 |
| Raw edge prob draw | -0.0100 |
| Raw ev draw | -0.1783 |
| Raw edge prob away | 0.0472 |
| Raw ev away | 0.0449 |

</details>


---

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Atalanta BC win** at **38.5%**. Expected goals are 1.25 for Fiorentina and 1.59 for Atalanta BC (2.84 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.5%; Double Chance 1X: 61.5%; Double Chance X2: 64.5%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 35.5% | 2.81 |
| Draw | 25.9% | 3.85 |
| Atalanta BC win | 38.5% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.25 |
| Atalanta BC expected goals | 1.59 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.7% |
| Under 2.5 | 46.3% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.23% |
| 2 | 2-1 | 8.70% |
| 3 | 1-0 | 8.27% |
| 4 | 1-2 | 7.92% |
| 5 | 0-1 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 35.5% | 41.4% | 2.25 | -20.0% |
| Draw | 25.9% | 26.5% | 3.54 | -8.1% |
| Atalanta BC win | 38.5% | 32.1% | 3.09 | +19.0% |
| Over 2.5 | 53.7% | 55.7% | 1.78 | -4.3% |
| Under 2.5 | 46.3% | 44.3% | 2.21 | +2.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T19:45:00+00:00 |
| Fixture id | da159a6b84dbb548b4d7b94c722caac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2523 |
| Dc lambda away | 1.5904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.77 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.36 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.18651089898003412, "-10": 1.7072354655126364e-06, "-11": 2.4320382662615245e-07, "-12": 3.1829214372227896e-08, "-13": 3.8507589274122586e-09, "-14": 4.3024361218683233e-10, "-15": 4.0269139532031843e-11, "-2": 0.11719625372861159, "-3": 0.05394160659350752, "-4": 0.019610265398278134, "-5": 0.00586513296532402, "-6": 0.0014864743974606612, "-7": 0.0003264137783411588, "-8": 6.317863933963291e-05, "-9": 1.0926469163186127e-05, "0": 0.25949107222240614, "1": 0.20382990255515154, "10": 2.182624873390327e-07, "11": 2.448384340023861e-08, "12": 2.5232403522767664e-09, "13": 2.403823331447955e-10, "14": 2.1149210475002763e-11, "15": 1.5587468575877465e-12, "2": 0.10134709420457015, "3": 0.03673203269738367, "4": 0.010515455001151194, "5": 0.002476543571375686, "6": 0.0004942527079774139, "7": 8.546407954788627e-05, "8": 1.3025935352370206e-05, "9": 1.7739525844027201e-06} |
| Raw goal margin distribution | {"-1": 0.2173053295303522, "-10": 1.989113598443606e-06, "-11": 2.8335870974326394e-07, "-12": 3.708447042866717e-08, "-13": 4.486549806147492e-09, "-14": 5.012802492287443e-10, "-15": 4.6917894255866884e-11, "-2": 0.13654628590335074, "-3": 0.06284779420560072, "-4": 0.022848075945452795, "-5": 0.006833512994355921, "-6": 0.0017319031249385575, "-7": 0.00038030728527701764, "-8": 7.360993441165006e-05, "-9": 1.2730515991795037e-05, "0": 0.25442249258173405, "1": 0.17028779162304997, "10": 1.823453600143932e-07, "11": 2.0454798686581854e-08, "12": 2.1080176261533404e-09, "13": 2.0082517895208094e-10, "14": 1.766891070060159e-11, "15": 1.3022405287475698e-12, "2": 0.08466948491446101, "3": 0.030687434235370206, "4": 0.00878503883684625, "5": 0.0020690052359403845, "6": 0.0004129188165726221, "7": 7.14001684093844e-05, "8": 1.088239623908743e-05, "9": 1.4820321466827226e-06} |
| Unadjusted home-win probability | 29.7% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 57.2% |
| P home draw | 61.5% |
| P draw away | 64.5% |
| P home away | 74.1% |
| Raw p home draw | 55.1% |
| Raw p draw away | 70.3% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.33 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.97 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:24Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:24Z |
| Home probability edge | -5.9% |
| Draw probability edge | -0.5% |
| Away probability edge | +6.4% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.1170 |
| Raw ev home | -0.3318 |
| Raw edge prob draw | -0.0101 |
| Raw ev draw | -0.0993 |
| Raw edge prob away | 0.1271 |
| Raw ev away | 0.3861 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **50.8%**. Expected goals are 1.56 for Frosinone and 0.97 for Lecce (2.53 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 46.7%; Under 3.5 goals: 75.0%; Double Chance 1X: 76.3%; Double Chance X2: 49.2%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 50.8% | 1.97 |
| Draw | 25.6% | 3.91 |
| Lecce win | 23.7% | 4.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.56 |
| Lecce expected goals | 0.97 |
| Expected total goals | 2.53 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 72.4% |
| Under 1.5 | 27.6% |
| Over 2.5 | 46.7% |
| Under 2.5 | 53.3% |
| Over 3.5 | 25.0% |
| Under 3.5 | 75.0% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.14% |
| 2 | 1-0 | 12.02% |
| 3 | 2-0 | 9.70% |
| 4 | 2-1 | 9.42% |
| 5 | 0-0 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 50.8% | 50.8% | 1.88 | -4.5% |
| Draw | 25.6% | 24.9% | 3.68 | -5.9% |
| Lecce win | 23.7% | 24.2% | 4.05 | -4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T17:30:00+00:00 |
| Fixture id | 667cf69986b200753742c90cb9c5126c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:18Z |
| Market best draw last update utc | 2026-10-22T15:06:18Z |
| Market best away last update utc | 2026-10-22T15:06:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Frosinone |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5624 |
| Dc lambda away | 0.9710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:43.013252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.29 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.62 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.00 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.78 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.15200083594850375, "-10": 1.9167723139888468e-08, "-11": 1.673016481245343e-09, "-12": 1.3408696087841088e-10, "-13": 9.931958117530661e-12, "-14": 6.810249673963632e-13, "-15": 4.003734011357032e-14, "-2": 0.0618294031977085, "-3": 0.017902235788224218, "-4": 0.00405283401463629, "-5": 0.0007504336274669153, "-6": 0.00011732204797631526, "-7": 1.5854156767628397e-05, "-8": 1.885306260932849e-06, "-9": 2.0008504370841768e-07, "0": 0.25559940444011614, "1": 0.24145998815632652, "10": 2.178661137746774e-06, "11": 3.059739674025533e-07, "12": 3.9458076054121275e-08, "13": 4.702722334181452e-09, "14": 5.188509202781525e-10, "15": 4.908060124082338e-11, "2": 0.15642040883734146, "3": 0.07287368560029545, "4": 0.02654528416202457, "5": 0.007908715405639125, "6": 0.001989474586947478, "7": 0.00043258056978693303, "8": 8.276960249669589e-05, "9": 1.4134117122657732e-05} |
| Raw goal margin distribution | {"-1": 0.14831367408912632, "-10": 1.870276189640921e-08, "-11": 1.6324332665461324e-09, "-12": 1.3083434502991514e-10, "-13": 9.691033540166496e-12, "-14": 6.645049971646316e-13, "-15": 3.9066133919232735e-14, "-2": 0.060329575806391436, "-3": 0.017467972117343588, "-4": 0.00395452235136217, "-5": 0.000732229975941422, "-6": 0.00011447610717695762, "-7": 1.5469574394897277e-05, "-8": 1.83957342469429e-06, "-9": 1.9523147867905511e-07, "0": 0.2620798862799748, "1": 0.24110833789068564, "10": 2.17548824449154e-06, "11": 3.055283622000605e-07, "12": 3.940061128311694e-08, "13": 4.695873524278506e-09, "14": 5.180952917148573e-10, "15": 4.900912270478959e-11, "2": 0.1561926059672291, "3": 0.07276755600468315, "4": 0.026506624936128122, "5": 0.007897197547568697, "6": 0.001986577215534816, "7": 0.00043195058105282365, "8": 8.264906098202427e-05, "9": 1.4113532900490188e-05} |
| Unadjusted home-win probability | 50.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.0% |
| Raw p btts yes | 49.5% |
| P home draw | 76.3% |
| P draw away | 49.2% |
| P home away | 74.4% |
| Raw p home draw | 76.9% |
| Raw p draw away | 49.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:18Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:24Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.91 |
| Reference draw odds | 3.78 |
| Reference away odds | 3.88 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:43Z |
| Market reference home last update utc | 2026-10-22T15:06:43Z |
| Market reference draw last update utc | 2026-10-22T15:06:43Z |
| Market reference away last update utc | 2026-10-22T15:06:43Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:43Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:43Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -14.8% |
| Under 2.5 probability edge | +14.8% |
| Raw edge prob home | -0.0015 |
| Raw ev home | -0.0469 |
| Raw edge prob draw | 0.0130 |
| Raw ev draw | -0.0355 |
| Raw edge prob away | -0.0115 |
| Raw ev away | -0.0647 |

</details>


---
