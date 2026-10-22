# Ligue 1 — football model report

Fixtures in this report: **17**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,743 |
| Training data through | 2026-10-18 |
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
| Training sha256 | 8caa20e50a4813882f03ec6f03d057338c361d3233edfb7fd435c2ab1f1f9c64 |
| Training as of utc | 2026-10-22T15:07:20.245787+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 36, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T15:07:20.245787+00:00', 'observations': 149, 'observations_sha256': 'c4ddc37d8f3b65882bd0552bd9a71ad609ba58fac0fc97de7b6ed359b88ed993', 'eligible_training_matches': 63, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 76, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 63, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '4fac31d3821e1026173f800b8714379c8b3676bcc932dd282546b2575ddaa845', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5079.453 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.187 |
| Dixon-Coles low-score adjustment | -0.057 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 16.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261022T150720245787Z_af3f4d6f610fedb658632dcb8c3c21ce8400d397ccbaa9cc8d57f2ade936c4b7.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **38.8%**. Expected goals are 1.22 for Brest and 1.24 for Nice (2.46 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.6%; Double Chance 1X: 67.5%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 38.8% | 2.58 |
| Draw | 28.6% | 3.49 |
| Nice win | 32.5% | 3.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.22 |
| Nice expected goals | 1.24 |
| Expected total goals | 2.46 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.62% |
| 2 | 1-0 | 10.72% |
| 3 | 0-0 | 9.26% |
| 4 | 0-1 | 8.89% |
| 5 | 2-1 | 8.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 38.8% | 42.5% | 2.29 | -11.1% |
| Draw | 28.6% | 28.6% | 3.37 | -3.5% |
| Nice win | 32.5% | 28.9% | 3.33 | +8.3% |
| Over 2.5 | 44.6% | 55.4% | 1.76 | -21.6% |
| Under 2.5 | 55.4% | 44.6% | 2.23 | +23.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 8aa36b30d655d6c81ed98bf9ec1b4039 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brest |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2187 |
| Dc lambda away | 1.2397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.80 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.67 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.18161291417251585, "-10": 2.086633742519982e-07, "-11": 2.3253487399094445e-08, "-12": 2.379069555682025e-09, "-13": 2.2393486801951424e-10, "-14": 1.7898615841673214e-11, "-2": 0.09522266712391354, "-3": 0.03521492094390046, "-4": 0.01018098878391879, "-5": 0.002407242348497042, "-6": 0.0004805536278848713, "-7": 8.291743747474811e-05, "-8": 1.2589699527890514e-05, "-9": 1.705971692138185e-06, "0": 0.28647875472849155, "1": 0.21916022591982576, "10": 2.1592115650201457e-07, "11": 2.3653106153215913e-08, "12": 2.3788022480945894e-09, "13": 2.2010202411476518e-10, "14": 1.7293100950573812e-11, "2": 0.11302653061552366, "3": 0.04108827300668599, "4": 0.011677025899445956, "5": 0.002714021063970515, "6": 0.0005325818645775211, "7": 9.033197383153233e-05, "8": 1.3482241674325831e-05, "9": 1.7958484230029551e-06} |
| Raw goal margin distribution | {"-1": 0.20179260406865548, "-10": 2.318487419020521e-07, "-11": 2.583726932261875e-08, "-12": 2.643416868722803e-09, "-13": 2.488171084381344e-10, "-14": 1.9887397966010482e-11, "-2": 0.10580321368030325, "-3": 0.039127782469210025, "-4": 0.011312236511711973, "-5": 0.0026747200458780832, "-6": 0.0005339497381414907, "-7": 9.213070395883486e-05, "-8": 1.3988588111975873e-05, "-9": 1.8955285850265381e-06, "0": 0.2874159863399137, "1": 0.19823595654784693, "10": 1.9530613649646777e-07, "11": 2.1394831584659135e-08, "12": 2.151686680874793e-09, "13": 1.990878367887313e-10, "14": 1.5642046334947517e-11, "2": 0.10223535004042875, "3": 0.03716538011490817, "4": 0.010562164686111725, "5": 0.002454900561674088, "6": 0.00048173374033289875, "7": 8.170755055664037e-05, "8": 1.2195027923072835e-05, "9": 1.6243902307308607e-06} |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 50.8% |
| P home draw | 67.5% |
| P draw away | 61.2% |
| P home away | 71.4% |
| Raw p home draw | 63.9% |
| Raw p draw away | 64.9% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.24, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.4, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.68, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.4, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:49Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.02, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.29 |
| Reference draw odds | 3.37 |
| Reference away odds | 3.33 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:15Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:15Z |
| Home probability edge | -3.7% |
| Draw probability edge | +0.1% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -10.8% |
| Under 2.5 probability edge | +10.8% |
| Raw edge prob home | -0.0741 |
| Raw ev home | -0.1957 |
| Raw edge prob draw | 0.0019 |
| Raw ev draw | -0.0314 |
| Raw edge prob away | 0.0723 |
| Raw ev away | 0.2033 |
| Market p home draw | 70.9% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:20Z |
| Market reference home draw last update utc | 2026-10-22T15:07:20Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.7% |
| Market draw away odds | 1.67 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:20Z |
| Market reference draw away last update utc | 2026-10-22T15:07:20Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.4% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:20Z |
| Market reference home away last update utc | 2026-10-22T15:07:20Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 79.6% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T14:59:49Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.45 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.4% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:22Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.81 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:26Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 62.3% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:20Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-22T15:07:20Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **46.2%**. Expected goals are 1.68 for RC Lens and 1.03 for Paris FC (2.70 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.3%; Under 3.5 goals: 71.8%; Double Chance 1X: 72.1%; Double Chance X2: 53.8%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 46.2% | 2.16 |
| Draw | 25.9% | 3.87 |
| Paris FC win | 27.9% | 3.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.68 |
| Paris FC expected goals | 1.03 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.3% |
| Under 2.5 | 49.7% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.32% |
| 2 | 1-0 | 9.42% |
| 3 | 2-1 | 8.60% |
| 4 | 2-0 | 8.39% |
| 5 | 0-1 | 7.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 46.2% | 40.5% | 2.40 | +11.0% |
| Draw | 25.9% | 26.1% | 3.67 | -5.1% |
| Paris FC win | 27.9% | 33.3% | 2.90 | -19.1% |
| Over 2.5 | 50.3% | 60.5% | 1.71 | -14.0% |
| Under 2.5 | 49.7% | 39.5% | 2.32 | +15.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | fc6c50376190b578cfeb38c029db8487 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6770 |
| Dc lambda away | 1.0253 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.43 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.40 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1749261824010279, "-10": 3.4413199482835963e-08, "-11": 3.1669135106165845e-09, "-12": 2.676698161867112e-10, "-13": 2.09109234520264e-11, "-14": 1.510833106919898e-12, "-15": 9.265244943245108e-14, "-2": 0.07489982575137417, "-3": 0.0226040737923113, "-4": 0.0053576074992740235, "-5": 0.0010412640287999508, "-6": 0.00017113772540552105, "-7": 2.4337384102919224e-05, "-8": 3.047793026784549e-06, "-9": 3.4080967709106444e-07, "0": 0.2585040159049283, "1": 0.20874756667800576, "10": 3.379354412192663e-06, "11": 5.086580577991406e-07, "12": 7.031859152183531e-08, "13": 8.985143375086316e-09, "14": 1.0618161557983704e-09, "15": 1.0650519156639615e-10, "2": 0.14359562320038813, "3": 0.07088072459309765, "4": 0.02747852157509595, "5": 0.008735029403488172, "6": 0.002348174122877761, "7": 0.0005461846309399007, "8": 0.00011187475230834178, "9": 2.046159904673782e-05} |
| Raw goal margin distribution | {"-1": 0.14087603146324465, "-10": 2.771451881331647e-08, "-11": 2.550459863922435e-09, "-12": 2.1556670893572568e-10, "-13": 1.6840520210974787e-11, "-14": 1.2167427962168149e-12, "-15": 7.461724255474273e-14, "-2": 0.06032024517034294, "-3": 0.018204091389034047, "-4": 0.004314725630409733, "-5": 0.0008385774048762681, "-6": 0.00013782501428805346, "-7": 1.960000522252164e-05, "-8": 2.4545267063018864e-06, "-9": 2.7446957415893926e-07, "0": 0.25557051520342666, "1": 0.23458778270912847, "10": 3.7976742491442617e-06, "11": 5.716232664895755e-07, "12": 7.902311260845142e-08, "13": 1.0097386500013263e-08, "14": 1.19325509560402e-09, "15": 1.1968914001814958e-10, "2": 0.16137088153595125, "3": 0.07965483039502717, "4": 0.030880002823553344, "5": 0.009816311692984317, "6": 0.002638847339238883, "7": 0.0006137951381231353, "8": 0.00012572338208679127, "9": 2.299447714502719e-05} |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 52.8% |
| P home draw | 72.1% |
| P draw away | 53.8% |
| P home away | 74.1% |
| Raw p home draw | 77.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.40 |
| Reference draw odds | 3.67 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:15Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:15Z |
| Home probability edge | +5.7% |
| Draw probability edge | -0.3% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | 0.1145 |
| Raw ev home | 0.2473 |
| Raw edge prob draw | -0.0059 |
| Raw ev draw | -0.0621 |
| Raw edge prob away | -0.1086 |
| Raw ev away | -0.3483 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **60.3%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.8%; Double Chance 1X: 82.8%; Double Chance X2: 39.7%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 60.3% | 1.66 |
| Draw | 22.4% | 4.46 |
| Troyes win | 17.2% | 5.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.7% |
| Under 2.5 | 46.3% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.90% |
| 2 | 1-0 | 10.83% |
| 3 | 1-1 | 10.70% |
| 4 | 2-1 | 9.92% |
| 5 | 3-0 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 60.3% | 60.5% | 1.62 | -2.2% |
| Draw | 22.4% | 21.9% | 4.30 | -3.5% |
| Troyes win | 17.2% | 17.6% | 5.30 | -8.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T15:15:00+00:00 |
| Fixture id | 0bbce95e5764e706e6c428bb52dc5536 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 0.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9080 |
| Dc lambda away | 0.9104 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.62 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.51 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.42 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.11404621167706099, "-10": 7.700205277979275e-09, "-11": 6.291022796769447e-10, "-12": 4.720669474491712e-11, "-13": 3.274867428498871e-12, "-14": 2.1118311505710347e-13, "-15": 1.2662799873197347e-14, "-16": 6.499439305003747e-16, "-2": 0.04354189264929608, "-3": 0.011654567627826809, "-4": 0.0024509088032044725, "-5": 0.0004227249775586906, "-6": 6.16654398151727e-05, "-7": 7.784081287822846e-06, "-8": 8.653321106279082e-07, "-9": 8.589980339862359e-08, "0": 0.22441692966948298, "1": 0.24077121496661297, "10": 1.2342927845895423e-05, "11": 2.1134784379830285e-06, "12": 3.32384552274764e-07, "13": 4.8327200393483846e-08, "14": 6.53157292821937e-09, "15": 8.208220362950723e-10, "16": 8.829900950364544e-11, "2": 0.18747259319606993, "3": 0.10516889859761432, "4": 0.046353121597903425, "5": 0.01675600263347001, "6": 0.005122889861290223, "7": 0.0013553180539077477, "8": 0.0003157747181012615, "9": 6.569727883890428e-05} |
| Raw goal margin distribution | {"-1": 0.1114811551989134, "-10": 7.527017048919318e-09, "-11": 6.149529023835354e-10, "-12": 4.614495112023397e-11, "-13": 3.2012111466371636e-12, "-14": 2.0643331574867484e-13, "-15": 1.2377996052284773e-14, "-16": 6.353257957561585e-16, "-2": 0.042562575474542876, "-3": 0.011392440339649824, "-4": 0.00239578448639849, "-5": 0.00041321731021738413, "-6": 6.027849908693856e-05, "-7": 7.609006571704299e-06, "-8": 8.458695988664438e-07, "-9": 8.39677984338014e-08, "0": 0.2299387075106929, "1": 0.24011319558451788, "10": 1.230919505206653e-05, "11": 2.107702374693961e-06, "12": 3.314761568183713e-07, "13": 4.819512383048724e-08, "14": 6.513722365879797e-09, "15": 8.185787581307459e-10, "16": 8.805769137231793e-11, "2": 0.18696023709921775, "3": 0.104881475644333, "4": 0.0462264401238067, "5": 0.01671020905926394, "6": 0.005108889180928432, "7": 0.001351614016660196, "8": 0.00031491171674574204, "9": 6.551773045379979e-05} |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.8% |
| P draw away | 39.7% |
| P home away | 77.6% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.62 |
| Reference draw odds | 4.30 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Home probability edge | -0.2% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.4% |
| Raw edge prob home | -0.0033 |
| Raw ev home | -0.0252 |
| Raw edge prob draw | 0.0110 |
| Raw ev draw | -0.0113 |
| Raw edge prob away | -0.0077 |
| Raw ev away | -0.1079 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **44.8%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 53.1%; Under 3.5 goals: 68.7%; Double Chance 1X: 72.5%; Double Chance X2: 55.2%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 44.8% | 2.23 |
| Draw | 27.7% | 3.61 |
| Lille win | 27.5% | 3.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.56 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 53.1% |
| Under 2.5 | 46.9% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.11% |
| 2 | 2-1 | 9.39% |
| 3 | 1-0 | 8.85% |
| 4 | 2-0 | 7.43% |
| 5 | 0-0 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 44.8% | 46.1% | 2.12 | -5.0% |
| Draw | 27.7% | 29.3% | 3.29 | -8.8% |
| Lille win | 27.5% | 24.7% | 3.88 | +6.6% |
| Over 2.5 | 53.1% | 52.7% | 1.85 | -1.8% |
| Under 2.5 | 46.9% | 47.3% | 2.05 | -3.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | c177a3c900d7febf9870ca8de90a9e35 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5580 |
| Dc lambda away | 1.2640 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.28 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.49 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.1554391865941412, "-10": 1.8504866651658963e-07, "-11": 2.0955586196942585e-08, "-12": 2.1801277436333316e-09, "-13": 2.0966456049104207e-10, "-14": 1.8623852578930376e-11, "-15": 1.3872766928117654e-12, "-2": 0.07940378252026847, "-3": 0.029087507035530907, "-4": 0.008412493313890127, "-5": 0.0020010742097701486, "-6": 0.00040328781653422874, "-7": 7.041268884891655e-05, "-8": 1.0835388434926118e-05, "-9": 1.4897797004837284e-06, "0": 0.27728594332746936, "1": 0.21883912373521447, "10": 1.6981225249336993e-06, "11": 2.3702464070826064e-07, "12": 3.0393887008736524e-08, "13": 3.6027983159419495e-09, "14": 3.944528227552899e-10, "15": 3.621589755381093e-11, "2": 0.13678525796968488, "3": 0.061761128665306704, "4": 0.02201628683694322, "5": 0.0064549540856274935, "6": 0.001603450970298449, "7": 0.00034506597003162363, "8": 6.544949616553969e-05, "9": 1.1091607562946192e-05} |
| Raw goal margin distribution | {"-1": 0.17127431241421598, "-10": 2.0390021213602427e-07, "-11": 2.3090404007900667e-08, "-12": 2.402224872939661e-09, "-13": 2.3102381209376167e-10, "-14": 2.0521128647492894e-11, "-15": 1.5286033521907179e-12, "-2": 0.08749291959277104, "-3": 0.032050751657381644, "-4": 0.009269503010124667, "-5": 0.0022049305382888643, "-6": 0.000444372136752638, "-7": 7.758587221202612e-05, "-8": 1.1939226810151547e-05, "-9": 1.6415486946367281e-06, "0": 0.26194044564291324, "1": 0.21265706827548078, "10": 1.6501517258947433e-06, "11": 2.303288568412275e-07, "12": 2.9535280504022885e-08, "13": 3.5010217294740873e-09, "14": 3.8330980049811703e-10, "15": 3.5192823236109915e-11, "2": 0.1329211680555536, "3": 0.06001641905329671, "4": 0.021394341802982705, "5": 0.0062726060508415974, "6": 0.0015581545778794107, "7": 0.00033531809256075884, "8": 6.360059269617395e-05, "9": 1.0778277241012072e-05} |
| Unadjusted home-win probability | 43.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 72.5% |
| P draw away | 55.2% |
| P home away | 72.3% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.82, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.11, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.12 |
| Reference draw odds | 3.29 |
| Reference away odds | 3.88 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:22Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:22Z |
| Market best over 2 5 last update utc | 2026-10-22T15:07:22Z |
| Market best under 2 5 last update utc | 2026-10-22T15:07:22Z |
| Home probability edge | -1.3% |
| Draw probability edge | -1.5% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.0253 |
| Raw ev home | -0.0773 |
| Raw edge prob draw | -0.0307 |
| Raw ev draw | -0.1382 |
| Raw edge prob away | 0.0560 |
| Raw ev away | 0.1750 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **38.9%**. Expected goals are 1.19 for Angers and 1.30 for Lorient (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.0%; Double Chance 1X: 61.1%; Double Chance X2: 67.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 32.4% | 3.08 |
| Draw | 28.7% | 3.49 |
| Lorient win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.19 |
| Lorient expected goals | 1.30 |
| Expected total goals | 2.49 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.65% |
| 2 | 0-1 | 10.18% |
| 3 | 0-0 | 9.09% |
| 4 | 1-0 | 8.94% |
| 5 | 1-2 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 32.4% | 31.7% | 3.05 | -1.1% |
| Draw | 28.7% | 28.9% | 3.34 | -4.2% |
| Lorient win | 38.9% | 39.4% | 2.47 | -4.0% |
| Over 2.5 | 45.3% | 45.8% | 2.08 | -5.8% |
| Under 2.5 | 54.7% | 54.2% | 1.87 | +2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 1a83b5ebabe7cb572ae6e029b3149c42 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1904 |
| Dc lambda away | 1.2991 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.00 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.16 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.32 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21112159538672676, "-10": 3.648037817673472e-07, "-11": 4.258818592018182e-08, "-12": 4.564653224930174e-09, "-13": 4.500349951710385e-10, "-14": 3.76055436036123e-11, "-2": 0.11538566234379502, "-3": 0.04461057811791169, "-4": 0.013494235914519944, "-5": 0.003339812210826448, "-6": 0.0006980859229549786, "-7": 0.00012614116747263068, "-8": 2.0059715574678107e-05, "-9": 2.847204492673932e-06, "0": 0.28681559205529167, "1": 0.1860572654636396, "10": 1.4687670536637866e-07, "11": 1.5711794034023986e-08, "12": 1.543076550595036e-09, "13": 1.3940200285058903e-10, "14": 1.0673765171002301e-11, "2": 0.0934762050702433, "3": 0.03311540892768534, "4": 0.009178751560599456, "5": 0.0020816150080938236, "6": 0.0003986853599299941, "7": 6.601175811941295e-05, "8": 9.619051944147804e-06, "9": 1.2510342653130505e-06} |
| Raw goal margin distribution | {"-1": 0.2082607250213176, "-10": 3.598603920277251e-07, "-11": 4.201108115364953e-08, "-12": 4.502798438755169e-09, "-13": 4.439366527502952e-10, "-14": 3.709595771746169e-11, "-2": 0.11382209220598986, "-3": 0.04400606828230002, "-4": 0.013311377976368359, "-5": 0.0032945550226052105, "-6": 0.0006886262874978246, "-7": 0.00012443185143975628, "-8": 1.9787890014999998e-05, "-9": 2.8086225421044984e-06, "0": 0.28482498877724616, "1": 0.1902208931868067, "10": 1.501635424636938e-07, "11": 1.6063395789847596e-08, "12": 1.577607834761857e-09, "13": 1.4252156951888002e-10, "14": 1.091262488156408e-11, "2": 0.0955680347975967, "3": 0.03385647235421555, "4": 0.009384155549347451, "5": 0.0021281978165375716, "6": 0.0004076072228483211, "7": 6.748898280868317e-05, "8": 9.834309065364956e-06, "9": 1.2790301672022319e-06} |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 51.3% |
| P home draw | 61.1% |
| P draw away | 67.6% |
| P home away | 71.3% |
| Raw p home draw | 61.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.05 |
| Reference draw odds | 3.34 |
| Reference away odds | 2.47 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.75 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:16Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:16Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0145 |
| Raw ev home | 0.0115 |
| Raw edge prob draw | -0.0040 |
| Raw ev draw | -0.0487 |
| Raw edge prob away | -0.0105 |
| Raw ev away | -0.0527 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **44.4%**. Expected goals are 1.73 for Auxerre and 1.52 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.3%; Double Chance 1X: 69.3%; Double Chance X2: 55.6%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 77.3%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 44.4% | 2.25 |
| Draw | 24.9% | 4.02 |
| Le Mans FC win | 30.7% | 3.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.73 |
| Le Mans FC expected goals | 1.52 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.7% |
| Under 3.5 | 59.3% |
| Over 4.5 | 22.7% |
| Under 4.5 | 77.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.06% |
| 2 | 2-1 | 9.26% |
| 3 | 1-2 | 7.13% |
| 4 | 2-2 | 6.85% |
| 5 | 1-0 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 44.4% | 46.5% | 2.10 | -6.7% |
| Draw | 24.9% | 25.4% | 3.77 | -6.3% |
| Le Mans FC win | 30.7% | 28.0% | 3.43 | +5.4% |
| Over 2.5 | 62.7% | 54.2% | 1.78 | +11.7% |
| Under 2.5 | 37.3% | 45.8% | 2.20 | -18.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 8eab078a37a63df32ffa443302a2a7ba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7273 |
| Dc lambda away | 1.5165 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.79 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.27 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.45 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.41 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.1592551162383249, "-10": 8.05593781201165e-07, "-11": 1.089368664819051e-07, "-12": 1.3542833537771693e-08, "-13": 1.5576528255980743e-09, "-14": 1.6657064016779453e-10, "-15": 1.648342458283653e-11, "-16": 1.3425457792881588e-12, "-2": 0.09140977286685505, "-3": 0.03867691745162205, "-4": 0.013080780485367063, "-5": 0.0036654278262900947, "-6": 0.0008742786948470081, "-7": 0.0001812214359346754, "-8": 3.317948505158591e-05, "-9": 5.436202613569206e-06, "0": 0.24859117419822765, "1": 0.20779020711661841, "10": 3.3763489649177864e-06, "11": 5.200133366158677e-07, "12": 7.363046184429332e-08, "13": 9.645550797635302e-09, "14": 1.174798007359583e-09, "15": 1.3240993515252723e-10, "16": 1.2283174230018028e-11, "2": 0.135287229547618, "3": 0.06519651896168005, "4": 0.025113925016145993, "5": 0.00801519308978797, "6": 0.002177447000652706, "7": 0.000514062171114055, "8": 0.00010719736282732398, "9": 2.0004075085779676e-05} |
| Raw goal margin distribution | {"-1": 0.17312274799097302, "-10": 8.757433510473403e-07, "-11": 1.184228810247453e-07, "-12": 1.4722117650114922e-08, "-13": 1.693290262523744e-09, "-14": 1.810752937903068e-10, "-15": 1.7918769754386597e-11, "-16": 1.4594521049246836e-12, "-2": 0.09936956152955481, "-3": 0.04204482964945694, "-4": 0.014219829899244807, "-5": 0.003984606289824241, "-6": 0.0009504092159611954, "-7": 0.0001970018529070716, "-8": 3.606869132204141e-05, "-9": 5.909576767935113e-06, "0": 0.24279842564706522, "1": 0.1979877901884055, "10": 3.2170711014009106e-06, "11": 4.954819229151294e-07, "12": 7.01569753136718e-08, "13": 9.190525935142079e-09, "14": 1.1193773981096517e-09, "15": 1.2616355132234866e-10, "16": 1.1703720574933398e-11, "2": 0.12890511054648376, "3": 0.06212090019215906, "4": 0.023929186008816467, "5": 0.007637079676665777, "6": 0.002074726840565925, "7": 0.0004898115011801532, "8": 0.00010214037165040772, "9": 1.906039113178064e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.8% |
| P home draw | 69.3% |
| P draw away | 55.6% |
| P home away | 75.1% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.7% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.65, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.45, "price": 1.65, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.10 |
| Reference draw odds | 3.77 |
| Reference away odds | 3.43 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:16Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:16Z |
| Home probability edge | -2.1% |
| Draw probability edge | -0.6% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | +8.6% |
| Under 2.5 probability edge | -8.6% |
| Raw edge prob home | -0.0419 |
| Raw ev home | -0.1111 |
| Raw edge prob draw | -0.0116 |
| Raw ev draw | -0.0846 |
| Raw edge prob away | 0.0535 |
| Raw ev away | 0.1454 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **64.5%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.6%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.8%; Double Chance 1X: 84.3%; Double Chance X2: 35.5%; Double Chance 12 (either team wins): 80.2%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 64.5% | 1.55 |
| Draw | 19.8% | 5.06 |
| Le Havre win | 15.7% | 6.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.57% |
| 2 | 1-0 | 10.45% |
| 3 | 1-1 | 9.42% |
| 4 | 2-1 | 9.37% |
| 5 | 3-0 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 64.5% | 62.1% | 1.58 | +1.9% |
| Draw | 19.8% | 19.1% | 4.90 | -3.2% |
| Le Havre win | 15.7% | 18.8% | 4.99 | -21.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | fcc34b753fc61a0cc0e11d7cb0a0c36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1127 |
| Dc lambda away | 0.8099 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.49 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.10898009397466771, "-10": 2.6057040665252297e-09, "-11": 1.8942689807563506e-10, "-12": 1.2647634725256759e-11, "-13": 7.806878503872389e-13, "-14": 4.48013323733078e-14, "-15": 2.4016532635510125e-15, "-16": 1.2029614176327258e-16, "-17": 5.207086379180313e-18, "-2": 0.03735126491567422, "-3": 0.008908825117937426, "-4": 0.0016685341455081792, "-5": 0.0002562184767629377, "-6": 3.3269997118381714e-05, "-7": 3.7378333740693476e-06, "-8": 3.697922810582149e-07, "-9": 3.266641680696723e-08, "0": 0.19762220737301636, "1": 0.2291540366789849, "10": 2.9553456346761357e-05, "11": 5.604305696596771e-06, "12": 9.760823575351992e-07, "13": 1.571634483481173e-07, "14": 2.3526755452317322e-08, "15": 3.2898674077298216e-09, "16": 4.298498370041548e-10, "17": 4.853520069685162e-11, "2": 0.1976117048493386, "3": 0.12294893311070725, "4": 0.060067064619565486, "5": 0.024060726433549076, "6": 0.008149820309696458, "7": 0.002388428183834654, "8": 0.0006163779175640759, "9": 0.00014203249253853827} |
| Raw goal margin distribution | {"-1": 0.08788880786121878, "-10": 2.1014133470949834e-09, "-11": 1.5276646992602231e-10, "-12": 1.0199895207700559e-11, "-13": 6.295986907317325e-13, "-14": 3.6130779019143854e-14, "-15": 1.9368531860375238e-15, "-16": 9.701482265500529e-17, "-17": 4.199341343960731e-18, "-2": 0.030122548309696323, "-3": 0.007184670066825287, "-4": 0.0013456170900214013, "-5": 0.00020663164852790852, "-6": 2.6831142070408265e-05, "-7": 3.01443784134738e-06, "-8": 2.9822513041732165e-07, "-9": 2.634437469772594e-08, "0": 0.20402941033691457, "1": 0.2376843111489209, "10": 3.0653585752407854e-05, "11": 5.812926354117052e-06, "12": 1.0124170891231983e-06, "13": 1.630138683122619e-07, "14": 2.4402540510716582e-08, "15": 3.412332943857146e-09, "16": 4.4585102617648144e-10, "17": 5.034192681609324e-11, "2": 0.2049678138896444, "3": 0.12752571543765068, "4": 0.0623030651510598, "5": 0.024956388597736648, "6": 0.008453197920363465, "7": 0.002477337584057796, "8": 0.0006393226271150351, "9": 0.00014731966165221238} |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 84.3% |
| P draw away | 35.5% |
| P home away | 80.2% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.58 |
| Reference draw odds | 4.90 |
| Reference away odds | 4.99 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Home probability edge | +2.4% |
| Draw probability edge | +0.6% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | 0.0480 |
| Raw ev home | 0.0573 |
| Raw edge prob draw | 0.0128 |
| Raw ev draw | -0.0003 |
| Raw edge prob away | -0.0608 |
| Raw ev away | -0.3674 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **67.0%**. Expected goals are 2.42 for Paris Saint Germain and 1.10 for Lyon (3.52 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 68.6%; Under 3.5 goals: 53.1%; Double Chance 1X: 85.0%; Double Chance X2: 33.0%; Double Chance 12 (either team wins): 82.0%; Under 4.5 goals: 72.0%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 67.0% | 1.49 |
| Draw | 18.0% | 5.56 |
| Lyon win | 15.0% | 6.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.42 |
| Lyon expected goals | 1.10 |
| Expected total goals | 3.52 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 87.1% |
| Under 1.5 | 12.9% |
| Over 2.5 | 68.6% |
| Under 2.5 | 31.4% |
| Over 3.5 | 46.9% |
| Under 3.5 | 53.1% |
| Over 4.5 | 28.0% |
| Under 4.5 | 72.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.65% |
| 2 | 2-0 | 8.81% |
| 3 | 1-1 | 7.96% |
| 4 | 3-1 | 7.80% |
| 5 | 3-0 | 7.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 67.0% | 67.8% | 1.45 | -2.9% |
| Draw | 18.0% | 17.2% | 5.39 | -3.1% |
| Lyon win | 15.0% | 15.0% | 6.13 | -7.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4238 |
| Dc lambda away | 1.0958 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.63 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.77 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.18 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.88 |
| Fair Over 4.5 odds | 3.57 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.09484460479800304, "-10": 2.5827642517290968e-08, "-11": 2.522867412790905e-09, "-12": 2.2656730920671224e-10, "-13": 1.8825722859238153e-11, "-14": 1.4552459452310644e-12, "-15": 1.0515147337369923e-13, "-16": 7.12894973818858e-15, "-17": 4.515530841671459e-16, "-18": 2.3953944798139774e-17, "-2": 0.03972345439858588, "-3": 0.01211952948732333, "-4": 0.002957517620695493, "-5": 0.0005982021628857336, "-6": 0.00010301770292832588, "-7": 1.5419976425795943e-05, "-8": 2.038954774759832e-06, "-9": 2.412875506625025e-07, "0": 0.17973805050235345, "1": 0.21815272564128316, "10": 7.342592651352688e-05, "11": 1.5865229152907622e-05, "12": 3.151638684679381e-06, "13": 5.792660692159234e-07, "14": 9.904899667517736e-08, "15": 1.5831289790646636e-08, "16": 2.374180549259557e-09, "17": 3.32647494222721e-10, "18": 3.903370192216338e-11, "2": 0.19702151241005555, "3": 0.1329657089652529, "4": 0.07177422110259887, "5": 0.03211266730257648, "6": 0.012232846222457312, "7": 0.004050294644908178, "8": 0.0011846709923693504, "9": 0.00031010754293235744} |
| Raw goal margin distribution | {"-1": 0.0949704709250108, "-10": 2.586191779673692e-08, "-11": 2.5262154529970757e-09, "-12": 2.2686798155151407e-10, "-13": 1.885070604968383e-11, "-14": 1.4571771691668916e-12, "-15": 1.0529101751256612e-13, "-16": 7.13841040593125e-15, "-17": 4.521523300384696e-16, "-18": 2.3985733535777734e-17, "-2": 0.03977617049527022, "-3": 0.012135613040425527, "-4": 0.002961442475348712, "-5": 0.0005989960234281487, "-6": 0.00010315441538875987, "-7": 1.54404399272824e-05, "-8": 2.0416606254636176e-06, "-9": 2.416077579063596e-07, "0": 0.18768870131594392, "1": 0.21549860866712944, "10": 7.253260282330189e-05, "11": 1.5672207617789102e-05, "12": 3.1132948239514546e-06, "13": 5.722185299182235e-07, "14": 9.784393438418055e-08, "15": 1.563868117284191e-08, "16": 2.3452954969322398e-09, "17": 3.286003966756659e-10, "18": 3.855880521605473e-11, "2": 0.19462448464510881, "3": 0.13134800492737, "4": 0.07090099259731626, "5": 0.03172197415344175, "6": 0.012084017438834306, "7": 0.0040010174436457425, "8": 0.0011702578999800981, "9": 0.0003063346737596693} |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.2% |
| Raw p btts yes | 61.1% |
| P home draw | 85.0% |
| P draw away | 33.0% |
| P home away | 82.0% |
| Raw p home draw | 84.9% |
| Raw p draw away | 33.8% |
| Raw p home away | 81.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.45 |
| Reference draw odds | 5.39 |
| Reference away odds | 6.13 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:58Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:58Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | -0.0163 |
| Raw ev home | -0.0405 |
| Raw edge prob draw | 0.0159 |
| Raw ev draw | 0.0116 |
| Raw edge prob away | 0.0004 |
| Raw ev away | -0.0770 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **53.7%**. Expected goals are 1.90 for Rennes and 1.25 for Strasbourg (3.16 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 61.5%; Under 3.5 goals: 61.1%; Double Chance 1X: 76.1%; Double Chance X2: 46.3%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 53.7% | 1.86 |
| Draw | 22.4% | 4.47 |
| Strasbourg win | 23.9% | 4.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.90 |
| Strasbourg expected goals | 1.25 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.23% |
| 2 | 2-1 | 9.97% |
| 3 | 2-0 | 7.97% |
| 4 | 1-0 | 7.77% |
| 5 | 3-1 | 6.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 53.7% | 55.3% | 1.77 | -5.0% |
| Draw | 22.4% | 21.3% | 4.45 | -0.4% |
| Strasbourg win | 23.9% | 23.4% | 4.06 | -2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 31dcb6d13ed240fc4a5c7a696149967e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9036 |
| Dc lambda away | 1.2515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.68 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.1389473316938095, "-10": 1.3428525406543685e-07, "-11": 1.5011215499010955e-08, "-12": 1.5423033748626485e-09, "-13": 1.4657723996745177e-10, "-14": 1.2951442008805825e-11, "-15": 1.060512540174684e-12, "-16": 7.220167687632843e-14, "-2": 0.06768414799937551, "-3": 0.02395430948812619, "-4": 0.00674730840188291, "-5": 0.001570582313332214, "-6": 0.00031067466483903364, "-7": 5.3346037712878665e-05, "-8": 8.084633014570799e-06, "-9": 1.095818867554268e-06, "0": 0.2238222043093162, "1": 0.22593221985225392, "10": 9.386601689279648e-06, "11": 1.5960533068149733e-06, "12": 2.494323681313733e-07, "13": 3.605794809076819e-08, "14": 4.846230462486071e-09, "15": 6.036055363563346e-10, "16": 6.250807992914069e-11, "2": 0.1651031211740885, "3": 0.08887987634169614, "4": 0.03808042746843439, "5": 0.013482903452465146, "6": 0.004056766666837019, "7": 0.0010595655431048796, "8": 0.00024425161175609887, "9": 5.03578719966656e-05} |
| Raw goal margin distribution | {"-1": 0.1420259237425069, "-10": 1.372605506068211e-07, "-11": 1.534381208876322e-08, "-12": 1.5764754805709784e-09, "-13": 1.498248843805032e-10, "-14": 1.3238401145778237e-11, "-15": 1.0840098282040811e-12, "-16": 7.3801416184917e-14, "-2": 0.06918379450077729, "-3": 0.02448505409346118, "-4": 0.006896805407280033, "-5": 0.0016053809824589035, "-6": 0.00031755814033471874, "-7": 5.4528001306784044e-05, "-8": 8.263760505627201e-06, "-9": 1.1200984216222746e-06, "0": 0.2348910711449787, "1": 0.2190434145144674, "10": 9.100398721579551e-06, "11": 1.5473887093238817e-06, "12": 2.418270295474219e-07, "13": 3.495852019403107e-08, "14": 4.698466065270175e-09, "15": 5.852012510202804e-10, "16": 6.060217206459512e-11, "2": 0.1600690305819054, "3": 0.08616987700222667, "4": 0.03691933299425408, "5": 0.013071801851582632, "6": 0.003933073481832523, "7": 0.001027258770862086, "8": 0.00023680423745982239, "9": 4.882243106824445e-05} |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 61.3% |
| Raw p btts yes | 61.3% |
| P home draw | 76.1% |
| P draw away | 46.3% |
| P home away | 77.6% |
| Raw p home draw | 75.5% |
| Raw p draw away | 47.9% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.77 |
| Reference draw odds | 4.45 |
| Reference away odds | 4.06 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:58Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:58Z |
| Home probability edge | -1.6% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0327 |
| Raw ev home | -0.0787 |
| Raw edge prob draw | 0.0221 |
| Raw ev draw | 0.0453 |
| Raw edge prob away | 0.0106 |
| Raw ev away | -0.0070 |

</details>


---

## 2026-10-25 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **60.0%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.8%; Double Chance 1X: 82.2%; Double Chance X2: 40.0%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 60.0% | 1.67 |
| Draw | 22.2% | 4.51 |
| Troyes win | 17.8% | 5.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.7% |
| Under 2.5 | 46.3% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.84% |
| 2 | 1-0 | 10.78% |
| 3 | 1-1 | 10.57% |
| 4 | 2-1 | 9.87% |
| 5 | 3-0 | 6.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 60.0% | 59.9% | 1.71 | +2.7% |
| Draw | 22.2% | 21.4% | 4.26 | -5.5% |
| Troyes win | 17.8% | 18.7% | 5.13 | -8.8% |
| Over 2.5 | 53.7% | 60.7% | 1.67 | -10.2% |
| Under 2.5 | 46.3% | 39.3% | 2.40 | +11.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 18e4425261f7dd6b245f82056d424411 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:06:16Z |
| Market best draw last update utc | 2026-10-22T15:06:16Z |
| Market best away last update utc | 2026-10-22T15:06:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9080 |
| Dc lambda away | 0.9104 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.80 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.11772395091766062, "-10": 7.948519945297532e-09, "-11": 6.493894431547646e-10, "-12": 4.872900671941747e-11, "-13": 3.380474693066823e-12, "-14": 2.1799330557353075e-13, "-15": 1.3071147290482803e-14, "-16": 6.709031913319345e-16, "-2": 0.044946022824700255, "-3": 0.012030401774939494, "-4": 0.0025299452161473258, "-5": 0.0004363569274068054, "-6": 6.365401448558161e-05, "-7": 8.03510077179578e-06, "-8": 8.932371660664772e-07, "-9": 8.866988293983166e-08, "0": 0.22179430949293624, "1": 0.23960205804349274, "10": 1.2282992028631705e-05, "11": 2.1032156333202046e-06, "12": 3.307705316764788e-07, "13": 4.809252914790785e-08, "14": 6.499856372280772e-09, "15": 8.16836220272517e-10, "16": 8.787023981753424e-11, "2": 0.18656224816059347, "3": 0.10465821069869173, "4": 0.04612803624859397, "5": 0.01667463744002088, "6": 0.005098013705938594, "7": 0.001348736787596591, "8": 0.00031424135291944095, "9": 6.537826051939582e-05} |
| Raw goal margin distribution | {"-1": 0.1114811551989134, "-10": 7.527017048919318e-09, "-11": 6.149529023835354e-10, "-12": 4.614495112023397e-11, "-13": 3.2012111466371636e-12, "-14": 2.0643331574867484e-13, "-15": 1.2377996052284773e-14, "-16": 6.353257957561585e-16, "-2": 0.042562575474542876, "-3": 0.011392440339649824, "-4": 0.00239578448639849, "-5": 0.00041321731021738413, "-6": 6.027849908693856e-05, "-7": 7.609006571704299e-06, "-8": 8.458695988664438e-07, "-9": 8.39677984338014e-08, "0": 0.2299387075106929, "1": 0.24011319558451788, "10": 1.230919505206653e-05, "11": 2.107702374693961e-06, "12": 3.314761568183713e-07, "13": 4.819512383048724e-08, "14": 6.513722365879797e-09, "15": 8.185787581307459e-10, "16": 8.805769137231793e-11, "2": 0.18696023709921775, "3": 0.104881475644333, "4": 0.0462264401238067, "5": 0.01671020905926394, "6": 0.005108889180928432, "7": 0.001351614016660196, "8": 0.00031491171674574204, "9": 6.551773045379979e-05} |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.2% |
| P draw away | 40.0% |
| P home away | 77.8% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.61 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.75 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:59Z |
| Market reference home last update utc | 2026-10-22T15:06:59Z |
| Market reference draw last update utc | 2026-10-22T15:06:59Z |
| Market reference away last update utc | 2026-10-22T15:06:59Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.32 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:16Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:16Z |
| Home probability edge | +0.1% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | 0.0026 |
| Raw ev home | 0.0290 |
| Raw edge prob draw | 0.0163 |
| Raw ev draw | -0.0205 |
| Raw edge prob away | -0.0189 |
| Raw ev away | -0.1365 |

</details>


---

## 2026-10-30 — Le Havre vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **75.3%**. Expected goals are 0.82 for Le Havre and 2.31 for Paris Saint Germain (3.13 combined). The most likely exact score is 0-2 at 12.5%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 62.1%; Under 3.5 goals: 61.0%; Double Chance 1X: 24.7%; Double Chance X2: 90.4%; Double Chance 12 (either team wins): 84.9%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 9.6% | 10.42 |
| Draw | 15.1% | 6.61 |
| Paris Saint Germain win | 75.3% | 1.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 0.82 |
| Paris Saint Germain expected goals | 2.31 |
| Expected total goals | 3.13 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 39.0% |
| Under 3.5 | 61.0% |
| Over 4.5 | 21.5% |
| Under 4.5 | 78.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.49% |
| 2 | 0-1 | 10.32% |
| 3 | 1-2 | 10.25% |
| 4 | 0-3 | 9.60% |
| 5 | 1-3 | 7.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 9.6% | 8.0% | 9.87 | -5.3% |
| Draw | 15.1% | 11.8% | 6.94 | +4.9% |
| Paris Saint Germain win | 75.3% | 80.3% | 1.22 | -8.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T18:00:00+00:00 |
| Fixture id | 9a9f6c78276f74f15f42b013b033aa5d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Le Havre |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8210 |
| Dc lambda away | 2.3072 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.19 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.90 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.65 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.2436482332244873, "-10": 6.554753300870164e-05, "-11": 1.3555948629747193e-05, "-12": 2.5753801606832616e-06, "-13": 4.5239942687179054e-07, "-14": 7.389334976689285e-08, "-15": 1.1277218590856522e-08, "-16": 1.614701024510824e-09, "-17": 2.1677732801785995e-10, "-18": 2.5140311774184435e-11, "-2": 0.22489188612001662, "-3": 0.15106559095698646, "-4": 0.07999043480912411, "-5": 0.03480488080375277, "-6": 0.012823647203680082, "-7": 0.004091713857084912, "-8": 0.0011503886664711407, "-9": 0.00028892641962321487, "0": 0.15119401090547033, "1": 0.06660221624032439, "10": 1.7023411947680933e-09, "11": 1.252731184616461e-10, "12": 8.468510617431368e-12, "13": 5.293287135239166e-13, "14": 3.076426034644488e-14, "15": 1.6706321635826523e-15, "16": 8.511550435823918e-17, "17": 4.06600708810835e-18, "18": 1.6778867638908948e-19, "2": 0.02272805718854759, "3": 0.005432400706633514, "4": 0.0010235333948930894, "5": 0.0001584680911590926, "6": 2.0775474600428758e-05, "7": 2.358752445944869e-06, "8": 2.3597142731020806e-07, "9": 2.108821386129628e-08} |
| Raw goal margin distribution | {"-1": 0.22749698724683598, "-10": 6.120243961384683e-05, "-11": 1.2657335666780518e-05, "-12": 2.4046602752538677e-06, "-13": 4.224102316830752e-07, "-14": 6.8995018872377e-08, "-15": 1.0529660814655248e-08, "-16": 1.5076637885657907e-09, "-17": 2.0240733279622998e-10, "-18": 2.3473780668885665e-11, "-2": 0.20998398334956758, "-3": 0.14105157408514019, "-4": 0.07468793303694378, "-5": 0.032497693168345984, "-6": 0.011973577914950915, "-7": 0.0038204774270014894, "-8": 0.0010741303243679222, "-9": 0.0002697737189817244, "0": 0.18480684145309592, "1": 0.07790906101239974, "10": 1.9913422029162027e-09, "11": 1.4654033424690777e-10, "12": 9.90618252096774e-12, "13": 6.191911525698055e-13, "14": 3.5987010217257154e-14, "15": 1.9542500311428722e-15, "16": 9.956529071373938e-17, "17": 4.756280078747427e-18, "18": 1.9627362216923879e-19, "2": 0.02658652660756023, "3": 0.006354641962209461, "4": 0.0011972953786284688, "5": 0.00018537071105987165, "6": 2.4302460332038972e-05, "7": 2.759190288220518e-06, "8": 2.7603154016912796e-07, "9": 2.4668292334805694e-08} |
| Unadjusted home-win probability | 11.2% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 70.3% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 61.9% |
| Raw p btts yes | 50.9% |
| P home draw | 24.7% |
| P draw away | 90.4% |
| P home away | 84.9% |
| Raw p home draw | 29.7% |
| Raw p draw away | 88.8% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.26, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.75, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 2.0, "market_key": "spreads", "opposite_price": 2.03, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 9.87 |
| Reference draw odds | 6.94 |
| Reference away odds | 1.22 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:58Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:58Z |
| Home probability edge | +1.6% |
| Draw probability edge | +3.4% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0326 |
| Raw ev home | 0.1080 |
| Raw edge prob draw | 0.0672 |
| Raw ev draw | 0.2826 |
| Raw edge prob away | -0.0998 |
| Raw ev away | -0.1424 |

</details>


---

## 2026-10-30 — Lille vs RC Lens

The model's most likely 1X2 outcome is **Lille win** at **40.0%**. Expected goals are 1.25 for Lille and 1.12 for RC Lens (2.37 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 42.6%; Under 3.5 goals: 78.4%; Double Chance 1X: 68.1%; Double Chance X2: 60.0%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 40.0% | 2.50 |
| Draw | 28.1% | 3.56 |
| RC Lens win | 31.9% | 3.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.25 |
| RC Lens expected goals | 1.12 |
| Expected total goals | 2.37 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 69.3% |
| Under 1.5 | 30.7% |
| Over 2.5 | 42.6% |
| Under 2.5 | 57.4% |
| Over 3.5 | 21.6% |
| Under 3.5 | 78.4% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.28% |
| 2 | 1-0 | 11.37% |
| 3 | 0-0 | 9.69% |
| 4 | 0-1 | 9.62% |
| 5 | 2-1 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 40.0% | 41.6% | 2.31 | -7.7% |
| Draw | 28.1% | 26.9% | 3.50 | -1.6% |
| RC Lens win | 31.9% | 31.4% | 3.02 | -3.6% |
| Over 2.5 | 42.6% | 57.2% | 1.75 | -25.4% |
| Under 2.5 | 57.4% | 42.8% | 2.25 | +29.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:05:00+00:00 |
| Fixture id | 7932d9a82dcdb164a3e4ef5e03694ee3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2461 |
| Dc lambda away | 1.1238 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.32 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.26 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.64 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.72 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.18775358012931395, "-10": 9.257990539755294e-08, "-11": 9.359655621566556e-09, "-12": 8.686450710605667e-10, "-13": 7.420709227260427e-11, "-14": 5.414981159985938e-12, "-2": 0.09056815984436194, "-3": 0.030581607819938298, "-4": 0.008052334966263433, "-5": 0.0017315322385536638, "-6": 0.00031408847933167734, "-7": 4.921612115830347e-05, "-8": 6.783562252612534e-06, "-9": 8.342060190656539e-07, "0": 0.28116808863347853, "1": 0.22113799559036076, "10": 2.7518798870333336e-07, "11": 3.0848087011501355e-08, "12": 3.1744343757497783e-09, "13": 3.0069418842647327e-10, "14": 2.4329444669338668e-11, "2": 0.11782658099375387, "3": 0.04411473479529564, "4": 0.012879553782313188, "5": 0.003070896591413461, "6": 0.000617649712460569, "7": 0.00010731322480075472, "8": 1.640058366045286e-05, "9": 2.236301907890309e-06} |
| Raw goal margin distribution | {"-1": 0.19050361479651243, "-10": 9.393592720631887e-08, "-11": 9.496746895216942e-09, "-12": 8.813681523315731e-10, "-13": 7.529400670673175e-11, "-14": 5.49429461915903e-12, "-2": 0.09189471553051627, "-3": 0.03102953792931664, "-4": 0.008170277858717828, "-5": 0.0017568940648374281, "-6": 0.0003186889466364014, "-7": 4.993699177646775e-05, "-8": 6.882921377210505e-06, "-9": 8.464246700785196e-07, "0": 0.2929385942239756, "1": 0.2120419956837209, "10": 2.638687673597939e-07, "11": 2.9579222310853486e-08, "12": 3.0438613608846975e-09, "13": 2.883258285589048e-10, "14": 2.3328709242348345e-11, "2": 0.1129800571439845, "3": 0.04230017722680449, "4": 0.012349783130785268, "5": 0.00294458236380085, "6": 0.0005922441203013429, "7": 0.00010289914353822455, "8": 1.5725983589822474e-05, "9": 2.1443168019790238e-06} |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 69.2% |
| Raw p under 3 5 | 78.5% |
| Raw p btts yes | 48.8% |
| P home draw | 68.1% |
| P draw away | 60.0% |
| P home away | 71.9% |
| Raw p home draw | 67.6% |
| Raw p draw away | 61.7% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.31 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.02 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:16Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:16Z |
| Home probability edge | -1.6% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -14.6% |
| Under 2.5 probability edge | +14.6% |
| Raw edge prob home | -0.0329 |
| Raw ev home | -0.1145 |
| Raw edge prob draw | 0.0235 |
| Raw ev draw | 0.0253 |
| Raw edge prob away | 0.0093 |
| Raw ev away | -0.0223 |

</details>


---

## 2026-10-31 — Lorient vs Brest

The model's most likely 1X2 outcome is **Brest win** at **36.6%**. Expected goals are 1.38 for Lorient and 1.40 for Brest (2.78 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 52.5%; Under 3.5 goals: 69.7%; Double Chance 1X: 63.4%; Double Chance X2: 63.5%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 36.5% | 2.74 |
| Draw | 26.8% | 3.73 |
| Brest win | 36.6% | 2.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.38 |
| Brest expected goals | 1.40 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.70% |
| 2 | 2-1 | 8.34% |
| 3 | 1-2 | 8.30% |
| 4 | 1-0 | 7.97% |
| 5 | 0-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 36.5% | 36.8% | 2.60 | -5.0% |
| Draw | 26.8% | 26.9% | 3.51 | -5.9% |
| Brest win | 36.6% | 36.3% | 2.63 | -3.6% |
| Over 2.5 | 52.5% | 50.3% | 1.91 | +0.2% |
| Under 2.5 | 47.5% | 49.7% | 1.93 | -8.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | c1a1e850def721bbfc43ff80c133a5e6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lorient |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3813 |
| Dc lambda away | 1.3951 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.45 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.73 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.19382586884054984, "-10": 5.655915796140159e-07, "-11": 7.070969361304127e-08, "-12": 8.118068164094798e-09, "-13": 8.555362556164526e-10, "-14": 7.493716123482851e-11, "-2": 0.1093188168637498, "-3": 0.04431182095185328, "-4": 0.014168394189747543, "-5": 0.003724112800932098, "-6": 0.000829089608082243, "-7": 0.00015987232501582028, "-8": 2.7166888149038167e-05, "-9": 4.124251860790785e-06, "0": 0.26819076174245576, "1": 0.1946593810649874, "10": 5.198172167230524e-07, "11": 6.434730667622003e-08, "12": 7.314890104508196e-09, "13": 7.63303449224499e-10, "14": 6.620026643434697e-11, "2": 0.10874595098599074, "3": 0.04364570008435825, "4": 0.013818031929131124, "5": 0.0035962682732798438, "6": 0.0007927466587598934, "7": 0.00015135958679718612, "8": 2.5467143250047663e-05, "9": 3.828152317111771e-06} |
| Raw goal margin distribution | {"-1": 0.19536622433044015, "-10": 5.700863980812602e-07, "-11": 7.127163132237209e-08, "-12": 8.182583344337092e-09, "-13": 8.623352963018997e-10, "-14": 7.553269509413922e-11, "-2": 0.11018758552043989, "-3": 0.044663971864827526, "-4": 0.014280991976119711, "-5": 0.00375370873480925, "-6": 0.000835678474352055, "-7": 0.00016114284795990796, "-8": 2.7382786396026202e-05, "-9": 4.157027743769985e-06, "0": 0.2676887359334664, "1": 0.19337587740874518, "10": 5.163897564352848e-07, "11": 6.392302708108101e-08, "12": 7.266658736758127e-09, "13": 7.582705411645743e-10, "14": 6.576376918696117e-11, "2": 0.10802892504596964, "3": 0.04335791834308772, "4": 0.013726921526919426, "5": 0.0035725559638482146, "6": 0.000787519614322449, "7": 0.00015036158412195605, "8": 2.5299223413373738e-05, "9": 3.8029110599538396e-06} |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 36.9% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 57.0% |
| P home draw | 63.4% |
| P draw away | 63.5% |
| P home away | 73.2% |
| Raw p home draw | 63.1% |
| Raw p draw away | 63.7% |
| Raw p home away | 73.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.60 |
| Reference draw odds | 3.51 |
| Reference away odds | 2.63 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:22Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:22Z |
| Market best over 2 5 last update utc | 2026-10-22T15:07:22Z |
| Market best under 2 5 last update utc | 2026-10-22T15:07:22Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +2.2% |
| Under 2.5 probability edge | -2.2% |
| Raw edge prob home | -0.0048 |
| Raw ev home | -0.0561 |
| Raw edge prob draw | -0.0010 |
| Raw ev draw | -0.0604 |
| Raw edge prob away | 0.0058 |
| Raw ev away | -0.0288 |

</details>


---

## 2026-10-31 — Lyon vs Angers

The model's most likely 1X2 outcome is **Lyon win** at **68.4%**. Expected goals are 2.14 for Lyon and 0.83 for Angers (2.98 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 57.7%; Under 3.5 goals: 65.0%; Double Chance 1X: 87.4%; Double Chance X2: 31.6%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 81.7%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 68.4% | 1.46 |
| Draw | 19.0% | 5.26 |
| Angers win | 12.6% | 7.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 2.14 |
| Angers expected goals | 0.83 |
| Expected total goals | 2.98 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.0% |
| Under 3.5 | 65.0% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.95% |
| 2 | 1-0 | 10.62% |
| 3 | 2-1 | 9.96% |
| 4 | 1-1 | 9.05% |
| 5 | 3-0 | 8.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 68.4% | 69.8% | 1.40 | -4.3% |
| Draw | 19.0% | 17.8% | 5.03 | -4.4% |
| Angers win | 12.6% | 12.4% | 7.06 | -10.9% |
| Over 2.5 | 57.7% | 63.0% | 1.64 | -5.3% |
| Under 2.5 | 42.3% | 37.0% | 2.46 | +4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | 961df571fad52d969150e9ced52b16f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lyon |
| Matched away-team name | Angers |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1443 |
| Dc lambda away | 0.8338 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.96 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.12 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.86 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.45 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.0867652372745792, "-10": 2.6280781926527218e-09, "-11": 1.9656632985866377e-10, "-12": 1.3504158985531936e-11, "-13": 8.577392483196464e-13, "-14": 5.0653723191682114e-14, "-15": 2.7943691126439752e-15, "-16": 1.439926501494893e-16, "-17": 6.3900466951054435e-18, "-2": 0.030341290232715274, "-3": 0.00741397116701213, "-4": 0.0014248884856347811, "-5": 0.00022474052539850443, "-6": 2.9991840873351036e-05, "-7": 3.4643137731847687e-06, "-8": 3.5246646708887083e-07, "-9": 3.2026337272276296e-08, "0": 0.18998220425230586, "1": 0.24030871111813837, "10": 3.459838427376129e-05, "11": 6.655483089324544e-06, "12": 1.17595558120333e-06, "13": 1.9210186371065563e-07, "14": 2.9176996821372504e-08, "15": 4.139671767826552e-09, "16": 5.486247300580733e-10, "17": 6.261696402030773e-11, "2": 0.2086547233220536, "3": 0.1311287702165546, "4": 0.06481580100444266, "5": 0.02629264800440561, "6": 0.009024205543824493, "7": 0.00268087148829211, "8": 0.0007015029486647217, "9": 0.00016393507674896751} |
| Raw goal margin distribution | {"-1": 0.08832832362846425, "-10": 2.6754233424951447e-09, "-11": 2.001074963152599e-10, "-12": 1.3747438060124676e-11, "-13": 8.731915257103852e-13, "-14": 5.156625620584108e-14, "-15": 2.844710013733995e-15, "-16": 1.465866953406082e-16, "-17": 6.505164167304578e-18, "-2": 0.030887892284547826, "-3": 0.007547534763715959, "-4": 0.0014505580258523149, "-5": 0.00022878925343118025, "-6": 3.05321475522652e-05, "-7": 3.5267238092145745e-06, "-8": 3.5881619357166925e-07, "-9": 3.260329565247175e-08, "0": 0.20194044862144742, "1": 0.235307303951837, "10": 3.3878307975885554e-05, "11": 6.516966342830984e-06, "12": 1.1514810931844952e-06, "13": 1.8810375796845474e-07, "14": 2.8569752746388364e-08, "15": 4.053515157234251e-09, "16": 5.372065186925532e-10, "17": 6.131375311660793e-11, "2": 0.20431211242105918, "3": 0.12839966244506412, "4": 0.06346682696964864, "5": 0.025745434224520504, "6": 0.008836389937527674, "7": 0.0026250760499532738, "8": 0.0006869029707516925, "9": 0.0001605231901642262} |
| Unadjusted home-win probability | 67.0% |
| Unadjusted draw probability | 20.2% |
| Unadjusted away-win probability | 12.8% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 50.5% |
| P home draw | 87.4% |
| P draw away | 31.6% |
| P home away | 81.0% |
| Raw p home draw | 87.2% |
| Raw p draw away | 33.0% |
| Raw p home away | 79.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.17, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.40 |
| Reference draw odds | 5.03 |
| Reference away odds | 7.06 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:58Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:58Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:16Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:16Z |
| Home probability edge | -1.4% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0285 |
| Raw ev home | -0.0626 |
| Raw edge prob draw | 0.0239 |
| Raw ev draw | 0.0158 |
| Raw edge prob away | 0.0045 |
| Raw ev away | -0.0929 |

</details>


---

## 2026-10-31 — Nice vs Rennes

The model's most likely 1X2 outcome is **Rennes win** at **38.0%**. Expected goals are 1.34 for Nice and 1.30 for Rennes (2.64 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.6%; Double Chance 1X: 62.0%; Double Chance X2: 64.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 54.1%; BTTS No (at least one team does not score): 45.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 35.8% | 2.79 |
| Draw | 26.2% | 3.82 |
| Rennes win | 38.0% | 2.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nice expected goals | 1.34 |
| Rennes expected goals | 1.30 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.48% |
| 2 | 0-1 | 9.24% |
| 3 | 1-2 | 8.72% |
| 4 | 1-0 | 8.51% |
| 5 | 2-1 | 8.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 35.8% | 34.3% | 2.78 | -0.5% |
| Draw | 26.2% | 24.8% | 3.79 | -0.8% |
| Rennes win | 38.0% | 40.9% | 2.35 | -10.6% |
| Over 2.5 | 49.7% | 61.1% | 1.65 | -18.0% |
| Under 2.5 | 50.3% | 38.9% | 2.45 | +23.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T16:15:00+00:00 |
| Fixture id | a547720e6b4661d6319c4f11dbdf8e1f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nice |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3432 |
| Dc lambda away | 1.2983 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.1% |
| P btts no | 45.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.44 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.97 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.66 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.69 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.20897980094116125, "-10": 3.3825265283480554e-07, "-11": 3.940869854438521e-08, "-12": 4.215917191261514e-09, "-13": 4.144407307594584e-10, "-14": 3.4177228383150403e-11, "-2": 0.11194024598207257, "-3": 0.04271171245107913, "-4": 0.012805991592378744, "-5": 0.0031493113159817, "-6": 0.0006550790347012311, "-7": 0.00011791478751084956, "-8": 1.8692312809686116e-05, "-9": 2.646056230871023e-06, "0": 0.26178057857109976, "1": 0.19223272703599859, "10": 4.2180624700953847e-07, "11": 5.084004856313353e-08, "12": 5.626625419276303e-09, "13": 5.722165712617409e-10, "14": 4.8817654385998264e-11, "2": 0.10639507115255438, "3": 0.041997583712933925, "4": 0.01302664568131632, "5": 0.003314187309212903, "6": 0.0007131768291114858, "7": 0.00013280482836889446, "8": 2.177964017069961e-05, "9": 3.1895454653157372e-06} |
| Raw goal margin distribution | {"-1": 0.19327493237061608, "-10": 3.12832906847467e-07, "-11": 3.6447127960106306e-08, "-12": 3.899090277392905e-09, "-13": 3.832954373983524e-10, "-14": 3.1608803695952966e-11, "-2": 0.10352791692928569, "-3": 0.039501919794343004, "-4": 0.011843619085715098, "-5": 0.002912640020083831, "-6": 0.000605849730735155, "-7": 0.000109053470617821, "-8": 1.7287582234608707e-05, "-9": 2.4472046425885657e-06, "0": 0.2755496870992788, "1": 0.20019232767441128, "10": 4.392715835562901e-07, "11": 5.294513487824504e-08, "12": 5.859601832657744e-09, "13": 5.959098073519324e-10, "14": 5.0839001317958683e-11, "2": 0.11080047230004603, "3": 0.04373653836070655, "4": 0.013566027808803715, "5": 0.0034514147617334613, "6": 0.0007427066746888927, "7": 0.00013830375361938724, "8": 2.268144935002127e-05, "9": 3.321611989644964e-06} |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 54.4% |
| P home draw | 62.0% |
| P draw away | 64.2% |
| P home away | 73.8% |
| Raw p home draw | 64.8% |
| Raw p draw away | 62.7% |
| Raw p home away | 72.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.78 |
| Reference draw odds | 3.79 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:16Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:16Z |
| Home probability edge | +1.5% |
| Draw probability edge | +1.4% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | 0.0296 |
| Raw ev home | 0.0360 |
| Raw edge prob draw | 0.0275 |
| Raw ev draw | 0.0443 |
| Raw edge prob away | -0.0572 |
| Raw ev away | -0.1733 |

</details>


---

## 2026-10-31 — Troyes vs Le Mans FC

The model's most likely 1X2 outcome is **Troyes win** at **38.6%**. Expected goals are 1.54 for Troyes and 1.80 for Le Mans FC (3.34 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.3%; Double Chance 1X: 63.9%; Double Chance X2: 61.4%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 66.7%; BTTS No (at least one team does not score): 33.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 38.6% | 2.59 |
| Draw | 25.3% | 3.95 |
| Le Mans FC win | 36.1% | 2.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 1.54 |
| Le Mans FC expected goals | 1.80 |
| Expected total goals | 3.34 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.03% |
| 2 | 2-1 | 8.95% |
| 3 | 1-2 | 7.31% |
| 4 | 2-2 | 7.25% |
| 5 | 1-0 | 5.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 38.6% | 44.7% | 2.16 | -16.6% |
| Draw | 25.3% | 26.9% | 3.51 | -11.1% |
| Le Mans FC win | 36.1% | 28.5% | 3.32 | +19.7% |
| Over 2.5 | 64.3% | 54.4% | 1.88 | +21.0% |
| Under 2.5 | 35.7% | 45.6% | 2.07 | -26.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | 75cf0c0e471877a0bfa95d689d0f0325 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5400 |
| Dc lambda away | 1.8048 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 66.7% |
| P btts no | 33.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.99 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.70 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.14 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.16395762481970433, "-10": 3.7816486300845033e-06, "-11": 6.078993249174904e-07, "-12": 8.985275657164412e-08, "-13": 1.2288906006547017e-08, "-14": 1.56265811132517e-09, "-15": 1.8369175209183865e-10, "-16": 1.7654105727872962e-11, "-2": 0.10988577188933812, "-3": 0.054845306540545403, "-4": 0.021941868400395196, "-5": 0.007285425572832786, "-6": 0.0020613192660095857, "-7": 0.0005072133358787214, "-8": 0.00011029654053944598, "-9": 2.1471528991661955e-05, "0": 0.25316391586685266, "1": 0.1997247713321631, "10": 1.109658461587609e-06, "11": 1.5220118120016735e-07, "12": 1.919534728626366e-08, "13": 2.2400411571150573e-09, "14": 2.4304402719963885e-10, "15": 2.437748206145949e-11, "16": 1.999047524298998e-12, "2": 0.11476883255874548, "3": 0.04887650864198129, "4": 0.016684474031061658, "5": 0.004726852461549201, "6": 0.0011411443656382896, "7": 0.00023958752345035355, "8": 4.445428530326955e-05, "9": 7.3840209461999e-06} |
| Raw goal margin distribution | {"-1": 0.1984455636005781, "-10": 4.577105789143418e-06, "-11": 7.357689175987901e-07, "-12": 1.0875298381842966e-07, "-13": 1.487383634146592e-08, "-14": 1.8913580259408002e-09, "-15": 2.2233069863464939e-10, "-16": 2.1367587905011603e-11, "-2": 0.13299987700019178, "-3": 0.066381833594219, "-4": 0.02655726713505578, "-5": 0.0088178905095795, "-6": 0.0024949108890411405, "-7": 0.0006139039670455485, "-8": 0.00013349704946392894, "-9": 2.5987993402576017e-05, "0": 0.23767725851762733, "1": 0.16850609781507842, "10": 9.36209444739515e-07, "11": 1.2841084736671206e-07, "12": 1.6194951912270205e-08, "13": 1.889903750110571e-09, "14": 2.050541870570551e-10, "15": 2.056707512711074e-11, "16": 1.6865794634271872e-12, "2": 0.09682949188662798, "3": 0.04123669633541808, "4": 0.014076549415072316, "5": 0.003988005383261076, "6": 0.000962773835287428, "7": 0.000202137964121911, "8": 3.750570396275047e-05, "9": 6.229835926359012e-06} |
| Unadjusted home-win probability | 32.6% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 43.6% |
| Raw p over 1 5 | 85.2% |
| Raw p under 3 5 | 57.0% |
| Raw p btts yes | 66.2% |
| P home draw | 63.9% |
| P draw away | 61.4% |
| P home away | 74.7% |
| Raw p home draw | 56.4% |
| Raw p draw away | 67.4% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.16 |
| Reference draw odds | 3.51 |
| Reference away odds | 3.32 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:16Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:16Z |
| Home probability edge | -6.0% |
| Draw probability edge | -1.5% |
| Away probability edge | +7.6% |
| Over 2.5 probability edge | +10.0% |
| Under 2.5 probability edge | -10.0% |
| Raw edge prob home | -0.1207 |
| Raw ev home | -0.2962 |
| Raw edge prob draw | -0.0310 |
| Raw ev draw | -0.1658 |
| Raw edge prob away | 0.1517 |
| Raw ev away | 0.4491 |

</details>


---

## 2026-11-01 — Strasbourg vs Auxerre

The model's most likely 1X2 outcome is **Strasbourg win** at **53.8%**. Expected goals are 1.77 for Strasbourg and 1.04 for Auxerre (2.81 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.4%; Under 3.5 goals: 69.1%; Double Chance 1X: 77.7%; Double Chance X2: 46.2%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 54.0%; BTTS No (at least one team does not score): 46.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 53.8% | 1.86 |
| Draw | 24.0% | 4.17 |
| Auxerre win | 22.3% | 4.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.77 |
| Auxerre expected goals | 1.04 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 30.9% |
| Under 3.5 | 69.1% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.39% |
| 2 | 1-0 | 10.03% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 9.44% |
| 5 | 0-0 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 53.8% | 53.5% | 1.81 | -2.7% |
| Draw | 24.0% | 23.3% | 3.99 | -4.4% |
| Auxerre win | 22.3% | 23.2% | 4.01 | -10.7% |
| Over 2.5 | 53.4% | 61.1% | 1.66 | -11.3% |
| Under 2.5 | 46.6% | 38.9% | 2.42 | +12.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | 448a1083448ea9dff55bfebf15ff20b4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:07:22Z |
| Market best draw last update utc | 2026-10-22T15:07:22Z |
| Market best away last update utc | 2026-10-22T15:07:22Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Strasbourg |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7708 |
| Dc lambda away | 1.0354 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:07:20.245787+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 54.0% |
| P btts no | 46.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.40 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.23 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.50 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.13968639831188417, "-10": 2.8979149375270465e-08, "-11": 2.6906927653304282e-09, "-12": 2.2948361465805495e-10, "-13": 1.8096006284563413e-11, "-14": 1.3264934573518336e-12, "-15": 9.037307536649014e-14, "-16": 5.246831590981149e-15, "-2": 0.05971469859839885, "-3": 0.018068236305976614, "-4": 0.00430409151420142, "-5": 0.0008418967832150194, "-6": 0.00013938221143616864, "-7": 1.9977777139480164e-05, "-8": 2.522562419451409e-06, "-9": 2.8449508184488554e-07, "0": 0.23958651523080704, "1": 0.23285848412903262, "10": 5.934289535054145e-06, "11": 9.423879127630236e-07, "12": 1.3746741810329705e-07, "13": 1.8540153698182976e-08, "14": 2.324439258280871e-09, "15": 2.708536227337382e-10, "16": 2.6895226735426168e-11, "2": 0.16699534314716474, "3": 0.08642141554404215, "4": 0.0352102905088277, "5": 0.011779570600836701, "6": 0.0033354962588099005, "7": 0.0008176788585209238, "8": 0.00017658752682730923, "9": 3.406240932627011e-05} |
| Raw goal margin distribution | {"-1": 0.1340971410203925, "-10": 2.7819609692778872e-08, "-11": 2.583030356251709e-09, "-12": 2.2030131071145603e-10, "-13": 1.7371932671848108e-11, "-14": 1.2734166129473705e-12, "-15": 8.675698692444383e-14, "-16": 5.036890665583079e-15, "-2": 0.05732534058943132, "-3": 0.017345273850519104, "-4": 0.004131872349202367, "-5": 0.000808210055007155, "-6": 0.00013380512554241945, "-7": 1.9178408425746665e-05, "-8": 2.421627392372526e-06, "-9": 2.731116097974158e-07, "0": 0.2462585018677081, "1": 0.23382952353763747, "10": 5.959036020122799e-06, "11": 9.463177493970998e-07, "12": 1.3804066876614808e-07, "13": 1.8617467694062765e-08, "14": 2.3341323649380807e-09, "15": 2.7198310505696804e-10, "16": 2.7007382086609287e-11, "2": 0.16769172773394894, "3": 0.08678180009500476, "4": 0.03535712037332836, "5": 0.011828692398192026, "6": 0.0033494055579564317, "7": 0.0008210886479394911, "8": 0.00017732391162453382, "9": 3.420445242996698e-05} |
| Unadjusted home-win probability | 54.0% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 21.4% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 54.1% |
| P home draw | 77.7% |
| P draw away | 46.2% |
| P home away | 76.0% |
| Raw p home draw | 78.6% |
| Raw p draw away | 46.0% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:06:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:22Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.81 |
| Reference draw odds | 3.99 |
| Reference away odds | 4.01 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:22Z |
| Market reference home last update utc | 2026-10-22T15:07:22Z |
| Market reference draw last update utc | 2026-10-22T15:07:22Z |
| Market reference away last update utc | 2026-10-22T15:07:22Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:59Z |
| Market best over 2 5 last update utc | 2026-10-22T15:06:16Z |
| Market best under 2 5 last update utc | 2026-10-22T15:06:16Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0045 |
| Raw ev home | -0.0228 |
| Raw edge prob draw | 0.0133 |
| Raw ev draw | -0.0174 |
| Raw edge prob away | -0.0178 |
| Raw ev away | -0.1424 |

</details>


---
