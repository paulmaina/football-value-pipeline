# La Liga — football model report

Fixtures in this report: **19**.

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
| Training sha256 | 4972947ab4b48973d535eea5e43b21c734ac5552b9636820b9db06ffb0d0407d |
| Training as of utc | 2026-10-23T14:31:28.066301+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 89, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 89, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 43, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-23T14:31:28.066301+00:00', 'observations': 199, 'observations_sha256': '87d09381dff61c3e75741469708ebd3588bcddcf650fa5b2071c4e6ea565bddf', 'eligible_training_matches': 92, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 113, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 10, 'retrospective_eligible_training_matches': 92, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '7b4484ef5cfeae70288d3a8f98146b7a8cdb760229ee0be6fb0fa002df12e2a8', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2503.167 |
| Base scoring parameter | 0.095 |
| Home-advantage parameter | 0.284 |
| Dixon-Coles low-score adjustment | -0.022 |
| Xi per day | 0.0009 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1989, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-21'} |
| Training data health | {'training_end': '2026-10-21', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 19.00 |
| Additional event odds calls used before this league | 9.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261023T143128066301Z_f2b2adc91ff0e8b17f51391122de4955a2c047b89720534be24329f4f61a833c.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
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

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **62.9%**. Expected goals are 1.75 for Alavés and 0.59 for Málaga (2.34 combined). The most likely exact score is 1-0 at 16.1%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.5%; Double Chance 1X: 86.3%; Double Chance X2: 37.1%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 37.3%; BTTS No (at least one team does not score): 62.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 62.9% | 1.59 |
| Draw | 23.3% | 4.29 |
| Málaga win | 13.7% | 7.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.75 |
| Málaga expected goals | 0.59 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 67.5% |
| Under 1.5 | 32.5% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.5% |
| Under 3.5 | 79.5% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.06% |
| 2 | 2-0 | 14.21% |
| 3 | 1-1 | 10.35% |
| 4 | 0-0 | 10.03% |
| 5 | 2-1 | 8.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 62.9% | 60.7% | 1.65 | +3.9% |
| Draw | 23.3% | 23.7% | 3.75 | -12.6% |
| Málaga win | 13.7% | 15.7% | 6.15 | -15.5% |
| Over 2.5 | 41.0% | 47.5% | 2.10 | -13.9% |
| Under 2.5 | 59.0% | 52.5% | 1.86 | +9.7% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
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
| Dc lambda home | 1.7471 |
| Dc lambda away | 0.5910 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 37.3% |
| P btts no | 62.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.97 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.08 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.87 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.52 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.10440367170319889, "-10": 1.7649003439493023e-10, "-11": 9.409283313182578e-12, "-12": 4.603808238894313e-13, "-13": 2.081227320321121e-14, "-14": 8.742652612579777e-16, "-15": 3.42365281670526e-17, "-16": 1.1879580220119339e-18, "-2": 0.027270525598164768, "-3": 0.0049654105341957935, "-4": 0.000698743932377692, "-5": 7.9906787303789e-05, "-6": 7.685316271660493e-06, "-7": 6.372794090505182e-07, "-8": 4.642115479111579e-08, "-9": 3.014086307132039e-09, "0": 0.23314317676031385, "1": 0.2603225135237367, "10": 7.465810808874976e-06, "11": 1.1766336809987144e-06, "12": 1.7018837608951008e-07, "13": 2.274364797816908e-08, "14": 2.824306117327483e-09, "15": 3.2695365763676165e-10, "16": 3.3537100718876945e-11, "2": 0.19780023209698822, "3": 0.10646733608491375, "4": 0.04429015642589088, "5": 0.014972722392585918, "6": 0.004257030728952421, "7": 0.001043525016380767, "8": 0.0002247071318447927, "9": 4.31305045377064e-05} |
| Raw goal margin distribution | {"-1": 0.0898095885577296, "-10": 1.5181934806477288e-10, "-11": 8.094005212597768e-12, "-12": 3.9602642032475143e-13, "-13": 1.7903026424636652e-14, "-14": 7.520559585979504e-16, "-15": 2.9450769864388826e-17, "-16": 1.0218991290272516e-18, "-2": 0.023458511025232165, "-3": 0.004271319866642937, "-4": 0.0006010699053999628, "-5": 6.873700487397148e-05, "-6": 6.61102316646499e-06, "-7": 5.48197209824628e-07, "-8": 3.993216660058373e-08, "-9": 2.5927617937666947e-09, "0": 0.22943893937820226, "1": 0.2697995685797539, "10": 7.737604051479272e-06, "11": 1.219469093213541e-06, "12": 1.7638409304177208e-07, "13": 2.357163170169029e-08, "14": 2.927125132888802e-09, "15": 3.388564230651051e-10, "16": 3.4758020667865574e-11, "2": 0.2050011601469751, "3": 0.11034328516087494, "4": 0.04590254194417035, "5": 0.015517805153705082, "6": 0.004412008160782422, "7": 0.0010815146005266276, "8": 0.00023288760702209102, "9": 4.470067286684853e-05} |
| Unadjusted home-win probability | 65.2% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 11.8% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 79.2% |
| Raw p btts yes | 37.1% |
| P home draw | 86.3% |
| P draw away | 37.1% |
| P home away | 76.7% |
| Raw p home draw | 88.2% |
| Raw p draw away | 34.8% |
| Raw p home away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 5.35, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 5.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:22Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.58, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:22Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.23, "price": 4.58, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.60 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.80 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:35Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:35Z |
| Home probability edge | +2.3% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | 0.0458 |
| Raw ev home | 0.0764 |
| Raw edge prob draw | -0.0074 |
| Raw ev draw | -0.1396 |
| Raw edge prob away | -0.0384 |
| Raw ev away | -0.2730 |
| Market p home draw | 84.1% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:31:22Z |
| Market reference home draw last update utc | 2026-10-23T14:31:22Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.5% |
| Market draw away odds | 2.35 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:31:22Z |
| Market reference draw away last update utc | 2026-10-23T14:31:22Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:31:22Z |
| Market reference home away last update utc | 2026-10-23T14:31:22Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.16 |
| Market reference dc draw away odds | 2.35 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 72.4% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T14:31:19Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-23T14:31:20Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.2% |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.75 |
| Market reference under 3 5 last update utc | 2026-10-23T14:31:20Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 47.3% |
| Market btts yes odds | 2.07 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:31:22Z |
| Market reference btts yes odds | 2.10 |
| Market reference btts yes opposite odds | 1.89 |
| Market reference btts yes last update utc | 2026-10-23T14:31:42Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,466.1423 |
| Elo away rating | 1,401.2778 |
| Elo rating diff | 124.8645 |
| Elo home expectancy | 0.6723 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **73.2%**. Expected goals are 2.24 for Atlético Madrid and 0.88 for Deportivo La Coruña (3.11 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 61.5%; Under 3.5 goals: 61.4%; Double Chance 1X: 89.4%; Double Chance X2: 26.8%; Double Chance 12 (either team wins): 83.8%; Under 4.5 goals: 78.9%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 73.2% | 1.37 |
| Draw | 16.2% | 6.16 |
| Deportivo La Coruña win | 10.6% | 9.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.24 |
| Deportivo La Coruña expected goals | 0.88 |
| Expected total goals | 3.11 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 82.5% |
| Under 1.5 | 17.5% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 38.6% |
| Under 3.5 | 61.4% |
| Over 4.5 | 21.1% |
| Under 4.5 | 78.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.98% |
| 2 | 1-0 | 10.50% |
| 3 | 2-1 | 10.48% |
| 4 | 3-0 | 8.93% |
| 5 | 3-1 | 7.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 73.2% | 78.3% | 1.28 | -6.3% |
| Draw | 16.2% | 13.6% | 6.00 | -2.6% |
| Deportivo La Coruña win | 10.6% | 8.1% | 10.34 | +9.4% |
| Over 2.5 | 61.5% | 62.2% | 1.65 | +1.5% |
| Under 2.5 | 38.5% | 37.8% | 2.44 | -6.1% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2371 |
| Dc lambda away | 0.8752 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.03 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.72 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.59 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.73 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.07256135007353101, "-10": 3.1153059600094843e-09, "-11": 2.442737232317748e-10, "-12": 1.7596274831464213e-11, "-13": 1.1720813710654108e-12, "-14": 7.25961550425564e-14, "-15": 4.200551362538037e-15, "-16": 2.2686070376804773e-16, "-17": 1.047265265450053e-17, "-2": 0.0252606245419236, "-3": 0.006411244389478531, "-4": 0.001284371494900559, "-5": 0.00021159204123573762, "-6": 2.9531395397773282e-05, "-7": 3.570488967291418e-06, "-8": 3.8046255607584467e-07, "-9": 3.622160994922089e-08, "0": 0.1622883724951524, "1": 0.2502155258958227, "10": 4.941104488444441e-05, "11": 9.903620733535312e-06, "12": 1.8236097322221799e-06, "13": 3.105008865872706e-07, "14": 4.916008409218197e-08, "15": 7.271084863479987e-09, "16": 1.003797490188876e-09, "17": 1.1845064950269448e-10, "2": 0.21979412737679646, "3": 0.14259629743831123, "4": 0.07302145659821735, "5": 0.030750563467150428, "6": 0.010970631682896706, "7": 0.0033905431681948007, "8": 0.0009235223718001384, "9": 0.00022474868797838684} |
| Raw goal margin distribution | {"-1": 0.08982615561096696, "-10": 3.856542879315355e-09, "-11": 3.023947246358053e-10, "-12": 2.1783025254942438e-11, "-13": 1.4509592712834946e-12, "-14": 8.986924186226384e-14, "-15": 5.200004960779249e-15, "-16": 2.808385574142679e-16, "-17": 1.2964451819728844e-17, "-2": 0.03127098363844737, "-3": 0.007936696817322777, "-4": 0.0015899670230269418, "-5": 0.0002619369623473518, "-6": 3.655791569094614e-05, "-7": 4.420029358028075e-06, "-8": 4.709874986006033e-07, "-9": 4.4839959130878045e-08, "0": 0.18862613308002954, "1": 0.23260955203784675, "10": 4.593432391992281e-05, "11": 9.20676994016557e-06, "12": 1.695294652021994e-06, "13": 2.886530397258017e-07, "14": 4.570102154087087e-08, "15": 6.759467810272617e-09, "16": 9.331670514593252e-10, "17": 1.1011607861170596e-10, "2": 0.2043287015329036, "3": 0.1325627606465602, "4": 0.06788343068501003, "5": 0.028586854342457304, "6": 0.010198702547312291, "7": 0.003151973582355311, "8": 0.0008585403500932248, "9": 0.0002089346432223898} |
| Unadjusted home-win probability | 68.0% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 13.1% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 52.3% |
| P home draw | 89.4% |
| P draw away | 26.8% |
| P home away | 83.8% |
| Raw p home draw | 86.9% |
| Raw p draw away | 32.0% |
| Raw p home away | 81.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 8.45, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.09, "price": 8.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.52, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.25 |
| Reference draw odds | 6.20 |
| Reference away odds | 10.00 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:35Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:35Z |
| Home probability edge | -5.2% |
| Draw probability edge | +2.6% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Raw edge prob home | -0.1030 |
| Raw ev home | -0.1290 |
| Raw edge prob draw | 0.0527 |
| Raw ev draw | 0.1318 |
| Raw edge prob away | 0.0503 |
| Raw ev away | 0.3538 |
| Market p home draw | 90.5% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:31:03Z |
| Market reference home draw last update utc | 2026-10-23T14:31:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 25.3% |
| Market draw away odds | 3.91 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:31:03Z |
| Market reference draw away last update utc | 2026-10-23T14:31:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.1% |
| Market home away odds | 1.15 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:31:03Z |
| Market reference home away last update utc | 2026-10-23T14:31:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 3.75 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 84.2% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-23T14:31:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.8% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:31:43Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.39 |
| Market reference under 3 5 last update utc | 2026-10-23T14:31:43Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.8% |
| Market btts yes odds | 2.09 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:31:03Z |
| Market reference btts yes odds | 2.09 |
| Market reference btts yes opposite odds | 1.78 |
| Market reference btts yes last update utc | 2026-10-23T14:31:03Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,646.3999 |
| Elo away rating | 1,445.4329 |
| Elo rating diff | 260.9670 |
| Elo home expectancy | 0.8179 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **51.0%**. Expected goals are 1.40 for Rayo Vallecano and 0.97 for Elche CF (2.37 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 43.1%; Under 3.5 goals: 78.2%; Double Chance 1X: 76.8%; Double Chance X2: 49.0%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 90.5%; BTTS Yes (both teams score): 46.6%; BTTS No (at least one team does not score): 53.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 51.0% | 1.96 |
| Draw | 25.8% | 3.88 |
| Elche CF win | 23.2% | 4.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.40 |
| Elche CF expected goals | 0.97 |
| Expected total goals | 2.37 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 69.2% |
| Under 1.5 | 30.8% |
| Over 2.5 | 43.1% |
| Under 2.5 | 56.9% |
| Over 3.5 | 21.8% |
| Under 3.5 | 78.2% |
| Over 4.5 | 9.5% |
| Under 4.5 | 90.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.98% |
| 2 | 1-1 | 12.11% |
| 3 | 2-0 | 10.03% |
| 4 | 2-1 | 9.72% |
| 5 | 0-0 | 8.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 51.0% | 55.3% | 1.81 | -7.6% |
| Draw | 25.8% | 24.0% | 3.83 | -1.3% |
| Elche CF win | 23.2% | 20.7% | 4.50 | +4.4% |
| Over 2.5 | 43.1% | 53.4% | 1.90 | -18.2% |
| Under 2.5 | 56.9% | 46.6% | 1.99 | +13.3% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.6% |
| P btts no | 53.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.15 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.24 |
| Fair Over 2.5 odds | 2.32 |
| Fair Under 2.5 odds | 1.76 |
| Fair Over 3.5 odds | 4.58 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.54 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.1486170095106484, "-10": 1.91607584793803e-08, "-11": 1.670981300907411e-09, "-12": 1.3376911252797773e-10, "-13": 9.859088397335953e-12, "-14": 6.219962278848027e-13, "-2": 0.06077903958495282, "-3": 0.017744387044321908, "-4": 0.0040359603998672555, "-5": 0.0007493023636489601, "-6": 0.00011731237709800646, "-7": 1.5862649616538278e-05, "-8": 1.8864346380660846e-06, "-9": 2.001379003720401e-07, "0": 0.2576725309578625, "1": 0.26174342593962413, "10": 9.461369358605573e-07, "11": 1.1957110691391122e-07, "12": 1.3871514010678206e-08, "13": 1.4815562295402393e-09, "14": 1.354510851228794e-10, "2": 0.1543079348685274, "3": 0.06528430529087324, "4": 0.021518304106629544, "5": 0.0057893740001730256, "6": 0.0013135049026331853, "7": 0.0002573812785083273, "8": 4.4356405386678416e-05, "9": 6.819574535510929e-06} |
| Raw goal margin distribution | {"-1": 0.1645373078852345, "-10": 2.121331621203511e-08, "-11": 1.8499818135431732e-09, "-12": 1.480988597874689e-10, "-13": 1.0915223421878764e-11, "-14": 6.886263233792461e-13, "-2": 0.0672898720145604, "-3": 0.019645218834370162, "-4": 0.004468304544090511, "-5": 0.0008295698730097868, "-6": 0.00012987922965803194, "-7": 1.7561904067548536e-05, "-8": 2.088515156312649e-06, "-9": 2.2157727060615697e-07, "0": 0.27579132854630795, "1": 0.23969774282846293, "10": 8.664473123566673e-07, "11": 1.095000737148466e-07, "12": 1.2703167562038134e-08, "13": 1.3567702142637942e-09, "14": 1.240425399456235e-10, "2": 0.14131114680618287, "3": 0.05978564911103517, "4": 0.01970589673967706, "5": 0.005301756387002291, "6": 0.0012028732306266932, "7": 0.00023570300298193846, "8": 4.0620429006012864e-05, "9": 6.245186931989999e-06} |
| Unadjusted home-win probability | 46.7% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 68.9% |
| Raw p under 3 5 | 78.4% |
| Raw p btts yes | 47.1% |
| P home draw | 76.8% |
| P draw away | 49.0% |
| P home away | 74.2% |
| Raw p home draw | 74.3% |
| Raw p draw away | 53.3% |
| Raw p home away | 72.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.13, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.44, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.17, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:23Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:23Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.70 |
| Reference draw odds | 3.60 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:31:19Z |
| Market best under 2 5 last update utc | 2026-10-23T14:31:19Z |
| Home probability edge | -4.3% |
| Draw probability edge | +1.8% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | -0.0860 |
| Raw ev home | -0.1542 |
| Raw edge prob draw | 0.0362 |
| Raw ev draw | 0.0563 |
| Raw edge prob away | 0.0497 |
| Raw ev away | 0.1561 |
| Market p home draw | 77.8% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:31:23Z |
| Market reference home draw last update utc | 2026-10-23T14:31:42Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.5% |
| Market draw away odds | 2.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:31:23Z |
| Market reference draw away last update utc | 2026-10-23T14:31:42Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.7% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:31:23Z |
| Market reference home away last update utc | 2026-10-23T14:31:42Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.00 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 76.7% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T14:31:19Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-23T14:31:42Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:31:19Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-10-23T14:31:42Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.2% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:31:23Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-23T14:31:42Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,498.4715 |
| Elo away rating | 1,425.5500 |
| Elo rating diff | 132.9215 |
| Elo home expectancy | 0.6825 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **38.2%**. Expected goals are 1.84 for Real Racing Club de Santander and 2.02 for Espanyol (3.86 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 73.3%; Under 3.5 goals: 46.3%; Double Chance 1X: 61.8%; Double Chance X2: 62.2%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 66.2%; BTTS Yes (both teams score): 73.7%; BTTS No (at least one team does not score): 26.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 37.8% | 2.65 |
| Draw | 24.0% | 4.17 |
| Espanyol win | 38.2% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.84 |
| Espanyol expected goals | 2.02 |
| Expected total goals | 3.86 |
| Over 0.5 | 97.4% |
| Under 0.5 | 2.6% |
| Over 1.5 | 89.9% |
| Under 1.5 | 10.1% |
| Over 2.5 | 73.3% |
| Under 2.5 | 26.7% |
| Over 3.5 | 53.7% |
| Under 3.5 | 46.3% |
| Over 4.5 | 33.8% |
| Under 4.5 | 66.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.99% |
| 2 | 2-2 | 8.17% |
| 3 | 2-1 | 7.60% |
| 4 | 1-2 | 7.07% |
| 5 | 1-3 | 4.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 37.8% | 39.7% | 2.42 | -8.6% |
| Draw | 24.0% | 26.6% | 3.72 | -10.7% |
| Espanyol win | 38.2% | 33.7% | 2.85 | +9.0% |
| Over 2.5 | 73.3% | 59.3% | 1.73 | +26.8% |
| Under 2.5 | 26.7% | 40.7% | 2.28 | -39.1% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
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
| Dc lambda home | 1.8411 |
| Dc lambda away | 2.0172 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 73.7% |
| P btts no | 26.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.01 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.88 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.74 |
| Fair Over 3.5 odds | 1.86 |
| Fair Under 3.5 odds | 2.16 |
| Fair Over 4.5 odds | 2.96 |
| Fair Under 4.5 odds | 1.51 |
| Goal margin distribution | {"-1": 0.1673462102257077, "-10": 8.093848738333179e-06, "-11": 1.4445607879847944e-06, "-12": 2.3729452278061997e-07, "-13": 3.609698580211933e-08, "-14": 5.111631747098273e-09, "-15": 6.761544544169771e-10, "-16": 8.260236590043485e-11, "-17": 8.044178566834192e-12, "-2": 0.11438846721337692, "-3": 0.06078892703405955, "-4": 0.026277016063183552, "-5": 0.009513917906180992, "-6": 0.0029529992753459956, "-7": 0.0008004027614651533, "-8": 0.00019228576883022466, "-9": 4.144227673752086e-05, "0": 0.24007425978426863, "1": 0.1797310798337891, "10": 3.824365862353568e-06, "11": 6.22981130621223e-07, "12": 9.340314639902279e-08, "13": 1.296819261702637e-08, "14": 1.6761110692369802e-09, "15": 2.0235962713218944e-10, "16": 2.256343235034203e-11, "17": 2.005529723165531e-12, "2": 0.11222996223573771, "3": 0.054435946137526024, "4": 0.021476923291120418, "5": 0.0070972506079546175, "6": 0.002010614466578068, "7": 0.0004974034148837313, "8": 0.00010906415750864894, "9": 2.1454244906330714e-05} |
| Raw goal margin distribution | {"-1": 0.18715463794852286, "-10": 9.051901015205368e-06, "-11": 1.6155504860569289e-06, "-12": 2.65382588815579e-07, "-13": 4.036971198640744e-08, "-14": 5.716685114434637e-09, "-15": 7.561894705772696e-10, "-16": 9.237983855706355e-11, "-17": 8.99635148736607e-12, "-2": 0.12792839549776241, "-3": 0.06798438766551086, "-4": 0.02938737256756325, "-5": 0.010640060858275359, "-6": 0.003302539743769647, "-7": 0.0008951447949312242, "-8": 0.0002150462409607989, "-9": 4.634771404809329e-05, "0": 0.21386342962047772, "1": 0.17066747488543865, "10": 3.631508058425692e-06, "11": 5.91565001238096e-07, "12": 8.869294702406454e-08, "13": 1.231422350448591e-08, "14": 1.5915869646960735e-09, "15": 1.9215489393013113e-10, "16": 2.142558775890324e-11, "17": 1.9043934637063606e-12, "2": 0.10657035098756794, "3": 0.05169081206702199, "4": 0.02039386994054378, "5": 0.006739345476636047, "6": 0.0019092217901119026, "7": 0.0004723200066238147, "8": 0.00010356419368159569, "9": 2.0372335197247753e-05} |
| Unadjusted home-win probability | 35.9% |
| Unadjusted draw probability | 21.4% |
| Unadjusted away-win probability | 42.8% |
| Raw p over 1 5 | 89.9% |
| Raw p under 3 5 | 46.2% |
| Raw p btts yes | 73.1% |
| P home draw | 61.8% |
| P draw away | 62.2% |
| P home away | 76.0% |
| Raw p home draw | 57.2% |
| Raw p draw away | 64.1% |
| Raw p home away | 78.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.24, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.40 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:35Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:35Z |
| Home probability edge | -1.9% |
| Draw probability edge | -2.6% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | +13.9% |
| Under 2.5 probability edge | -13.9% |
| Raw edge prob home | -0.0381 |
| Raw ev home | -0.1323 |
| Raw edge prob draw | -0.0524 |
| Raw ev draw | -0.2044 |
| Raw edge prob away | 0.0905 |
| Raw ev away | 0.2186 |
| Market p home draw | 65.9% |
| Market home draw odds | 1.46 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:31:23Z |
| Market reference home draw last update utc | 2026-10-23T14:31:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.5% |
| Market draw away odds | 1.61 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:31:23Z |
| Market reference draw away last update utc | 2026-10-23T14:31:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:31:23Z |
| Market reference home away last update utc | 2026-10-23T14:31:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.44 |
| Market reference dc draw away odds | 1.57 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 82.0% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-23T14:31:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.1% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:31:43Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.63 |
| Market reference under 3 5 last update utc | 2026-10-23T14:31:43Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.9% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:31:23Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.55 |
| Market reference btts yes last update utc | 2026-10-23T14:31:23Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,429.4672 |
| Elo away rating | 1,440.6093 |
| Elo rating diff | 48.8579 |
| Elo home expectancy | 0.5699 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.6%**. Expected goals are 1.26 for Valencia and 1.54 for Villarreal (2.80 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.1%; Under 3.5 goals: 69.2%; Double Chance 1X: 55.4%; Double Chance X2: 69.9%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 84.7%; BTTS Yes (both teams score): 56.5%; BTTS No (at least one team does not score): 43.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.1% | 3.32 |
| Draw | 25.3% | 3.95 |
| Villarreal win | 44.6% | 2.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.26 |
| Villarreal expected goals | 1.54 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 53.1% |
| Under 2.5 | 46.9% |
| Over 3.5 | 30.8% |
| Under 3.5 | 69.2% |
| Over 4.5 | 15.3% |
| Under 4.5 | 84.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.96% |
| 2 | 0-1 | 9.32% |
| 3 | 1-2 | 9.30% |
| 4 | 0-2 | 7.37% |
| 5 | 2-1 | 7.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.1% | 29.3% | 3.30 | -0.6% |
| Draw | 25.3% | 25.1% | 3.73 | -5.6% |
| Villarreal win | 44.6% | 45.7% | 2.16 | -3.7% |
| Over 2.5 | 53.1% | 56.9% | 1.79 | -4.9% |
| Under 2.5 | 46.9% | 43.1% | 2.19 | +2.6% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
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
| Dc lambda home | 1.2619 |
| Dc lambda away | 1.5381 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.90 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.24 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.55 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.22170820177810113, "-10": 1.5168494004125062e-06, "-11": 2.0906443845326252e-07, "-12": 2.6471162348811398e-08, "-13": 3.0982870581831323e-09, "-14": 3.349959849288838e-10, "-15": 3.041551490865029e-11, "-2": 0.13463309714403787, "-3": 0.06011815179195991, "-4": 0.021181654539467673, "-5": 0.006136029578543718, "-6": 0.0015056933957487018, "-7": 0.00032004325307615015, "-8": 5.995098106454884e-05, "-9": 1.003315461407216e-05, "0": 0.25310895060784244, "1": 0.17202345934397598, "10": 1.9867958211289726e-07, "11": 2.2465675356989278e-08, "12": 2.333677628770934e-09, "13": 2.2408771242765597e-10, "14": 1.987762672997191e-11, "15": 1.4806371473509955e-12, "2": 0.08592791999357421, "3": 0.03147868793117195, "4": 0.00909912059670959, "5": 0.002162497050144631, "6": 0.00043534460180049713, "7": 7.591609020358293e-05, "8": 1.1666752649980907e-05, "9": 1.6018422326472062e-06} |
| Raw goal margin distribution | {"-1": 0.21629892177347332, "-10": 1.4798410125140053e-06, "-11": 2.03963643455449e-07, "-12": 2.5825313760241837e-08, "-13": 3.0226944454695932e-09, "-14": 3.268226874668438e-10, "-15": 2.96734312360287e-11, "-2": 0.1313482925472677, "-3": 0.05865137738399774, "-4": 0.02066486039542445, "-5": 0.005986321530574247, "-6": 0.0014689571942306573, "-7": 0.00031223477528598905, "-8": 5.8488285320641015e-05, "-9": 9.788363748411901e-06, "0": 0.2552959747378403, "1": 0.1769843589223313, "10": 2.0440920444981845e-07, "11": 2.3113551872384207e-08, "12": 2.4009774052591946e-09, "13": 2.3055006728516456e-10, "14": 2.0450867789298837e-11, "15": 1.5233365107285409e-12, "2": 0.08840595283683131, "3": 0.03238648626449502, "4": 0.009361525641368997, "5": 0.002224860234475239, "6": 0.00044789928974682465, "7": 7.810539683256006e-05, "8": 1.200320436722219e-05, "9": 1.6480369696141072e-06} |
| Unadjusted home-win probability | 31.0% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 43.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 56.6% |
| P home draw | 55.4% |
| P draw away | 69.9% |
| P home away | 74.7% |
| Raw p home draw | 56.5% |
| Raw p draw away | 69.0% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.18, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.20 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.10 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:35Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:35Z |
| Home probability edge | +0.9% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | 0.0174 |
| Raw ev home | 0.0227 |
| Raw edge prob draw | 0.0044 |
| Raw ev draw | -0.0477 |
| Raw edge prob away | -0.0217 |
| Raw ev away | -0.0608 |
| Market p home draw | 56.7% |
| Market home draw odds | 1.75 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:31:22Z |
| Market reference home draw last update utc | 2026-10-23T14:31:42Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.0% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:31:22Z |
| Market reference draw away last update utc | 2026-10-23T14:31:42Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.3% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:31:22Z |
| Market reference home away last update utc | 2026-10-23T14:31:42Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.68 |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.4% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-10-23T14:31:42Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:31:43Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.87 |
| Market reference under 3 5 last update utc | 2026-10-23T14:31:43Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.0% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:31:22Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-23T14:31:42Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,465.9892 |
| Elo away rating | 1,546.8125 |
| Elo rating diff | -20.8233 |
| Elo home expectancy | 0.4701 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **56.1%**. Expected goals are 1.20 for Athletic Bilbao and 0.62 for Getafe (1.82 combined). The most likely exact score is 1-0 at 21.6%. Goal-market probabilities: at least one goal: 85.8%; Over 2.5 goals: 28.9%; Under 3.5 goals: 88.4%; Double Chance 1X: 83.1%; Double Chance X2: 43.9%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 95.9%; BTTS Yes (both teams score): 31.7%; BTTS No (at least one team does not score): 68.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 56.1% | 1.78 |
| Draw | 27.0% | 3.71 |
| Getafe win | 16.9% | 5.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.20 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.82 |
| Over 0.5 | 85.8% |
| Under 0.5 | 14.2% |
| Over 1.5 | 55.5% |
| Under 1.5 | 44.5% |
| Over 2.5 | 28.9% |
| Under 2.5 | 71.1% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.1% |
| Under 4.5 | 95.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.59% |
| 2 | 0-0 | 14.20% |
| 3 | 2-0 | 13.10% |
| 4 | 1-1 | 10.67% |
| 5 | 0-1 | 8.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 56.1% | 62.6% | 1.58 | -11.3% |
| Draw | 27.0% | 22.7% | 4.21 | +13.6% |
| Getafe win | 16.9% | 14.7% | 5.90 | -0.4% |
| Over 2.5 | 28.9% | 42.2% | 2.38 | -31.1% |
| Under 2.5 | 71.1% | 57.8% | 1.68 | +19.4% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
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
| Dc lambda away | 0.6242 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 31.7% |
| P btts no | 68.3% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.04 |
| Fair Over 1.5 odds | 1.80 |
| Fair Under 1.5 odds | 2.25 |
| Fair Over 2.5 odds | 3.46 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.61 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.68 |
| Fair Under 4.5 odds | 1.04 |
| Goal margin distribution | {"-1": 0.12506118636578445, "-10": 3.7964946399011357e-10, "-11": 2.14206800223022e-11, "-12": 1.1072728342056478e-12, "-13": 5.0274247260578354e-14, "-2": 0.035588975971038224, "-3": 0.006984937863842162, "-4": 0.0010515944600009138, "-5": 0.00012813725843267157, "-6": 1.3099744817267677e-05, "-7": 1.1528264759176183e-06, "-8": 8.90273438138751e-08, "-9": 6.123652754695418e-09, "0": 0.26987330174374347, "1": 0.3084447584295052, "10": 3.2466260814866183e-07, "11": 3.5118790618292286e-08, "12": 3.480308632346512e-09, "13": 3.0294619779970666e-10, "2": 0.16676712743037486, "3": 0.06275008508568816, "4": 0.018111602463849085, "5": 0.004230978624382746, "6": 0.0008292491878611819, "7": 0.00013990813805092145, "8": 2.0713775586430098e-05, "9": 2.7315126881803527e-06} |
| Raw goal margin distribution | {"-1": 0.14111754920795466, "-10": 4.283919213727858e-10, "-11": 2.4170839530290106e-11, "-12": 1.2494334430078377e-12, "-13": 5.672886023115924e-14, "-2": 0.04015817548031621, "-3": 0.007881720471067983, "-4": 0.0011866066304692582, "-5": 0.00014458855219361732, "-6": 1.4781595613970447e-05, "-7": 1.3008356283116655e-06, "-8": 1.0045739159040329e-07, "-9": 6.909856639418399e-09, "0": 0.3127081054675405, "1": 0.2729949108188291, "10": 2.873488277415776e-07, "11": 3.108255482025639e-08, "12": 3.080313471841938e-09, "13": 2.681283049591388e-10, "2": 0.14760042385603567, "3": 0.055538158498992705, "4": 0.01603001887462646, "5": 0.003744708252203035, "6": 0.000733942794941315, "7": 0.00012382836351154585, "8": 1.833312178080378e-05, "9": 2.4175773532579646e-06} |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 31.3% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 54.6% |
| Raw p under 3 5 | 88.8% |
| Raw p btts yes | 32.7% |
| P home draw | 83.1% |
| P draw away | 43.9% |
| P home away | 73.0% |
| Raw p home draw | 80.9% |
| Raw p draw away | 50.3% |
| Raw p home away | 68.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.85, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.56, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.55 |
| Reference draw odds | 4.00 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.65 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:35Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:35Z |
| Home probability edge | -6.5% |
| Draw probability edge | +4.3% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -13.3% |
| Under 2.5 probability edge | +13.3% |
| Raw edge prob home | -0.1290 |
| Raw ev home | -0.2151 |
| Raw edge prob draw | 0.0857 |
| Raw ev draw | 0.3165 |
| Raw edge prob away | 0.0434 |
| Raw ev away | 0.1240 |
| Market p home draw | 84.6% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:31:24Z |
| Market reference home draw last update utc | 2026-10-23T14:31:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.6% |
| Market draw away odds | 2.49 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:31:24Z |
| Market reference draw away last update utc | 2026-10-23T14:31:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:31:24Z |
| Market reference home away last update utc | 2026-10-23T14:31:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 2.39 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 67.7% |
| Market over 1 5 odds | 1.44 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T14:31:43Z |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.87 |
| Market reference over 1 5 last update utc | 2026-10-23T14:31:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 81.1% |
| Market reference under 3 5 odds | 1.19 |
| Market reference under 3 5 opposite odds | 4.00 |
| Market reference under 3 5 last update utc | 2026-10-23T14:31:43Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 39.4% |
| Market btts yes odds | 2.50 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:31:24Z |
| Market reference btts yes odds | 2.48 |
| Market reference btts yes opposite odds | 1.63 |
| Market reference btts yes last update utc | 2026-10-23T14:31:42Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,491.3653 |
| Elo away rating | 1,456.5803 |
| Elo rating diff | 94.7851 |
| Elo home expectancy | 0.6331 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **57.2%**. Expected goals are 1.97 for Barcelona and 1.35 for Real Madrid (3.32 combined). The most likely exact score is 2-1 at 10.5%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 65.7%; Under 3.5 goals: 57.1%; Double Chance 1X: 76.2%; Double Chance X2: 42.8%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 57.2% | 1.75 |
| Draw | 19.0% | 5.27 |
| Real Madrid win | 23.8% | 4.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.97 |
| Real Madrid expected goals | 1.35 |
| Expected total goals | 3.32 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 84.9% |
| Under 1.5 | 15.1% |
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 42.9% |
| Under 3.5 | 57.1% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.47% |
| 2 | 1-1 | 8.36% |
| 3 | 2-0 | 7.75% |
| 4 | 1-0 | 7.63% |
| 5 | 3-1 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 57.2% | 62.7% | 1.62 | -7.3% |
| Draw | 19.0% | 15.6% | 5.98 | +13.4% |
| Real Madrid win | 23.8% | 21.7% | 3.97 | -5.4% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9719 |
| Dc lambda away | 1.3512 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.78 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.60 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.92 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.1352717048551723, "-10": 2.3472463056049423e-07, "-11": 2.827172713065487e-08, "-12": 3.130708274515948e-09, "-13": 3.207561963952019e-10, "-14": 3.055450702963149e-11, "-15": 2.692607323345995e-12, "-16": 1.9493100718513347e-13, "-2": 0.06762973705076158, "-3": 0.025431991485860637, "-4": 0.007650524643866116, "-5": 0.00190774699756811, "-6": 0.0004050597231869233, "-7": 7.475538748905997e-05, "-8": 1.2187932598786816e-05, "-9": 1.7784014636876314e-06, "0": 0.18960642370411407, "1": 0.23931059450178316, "10": 1.2410957498245568e-05, "11": 2.1815259928431316e-06, "12": 3.5254298697489335e-07, "13": 5.271157110492952e-08, "14": 7.327698880299349e-09, "15": 9.423815680103156e-10, "16": 9.956257368201778e-11, "2": 0.173817262123767, "3": 0.09538871597311133, "4": 0.0418763941652753, "5": 0.015239133251250933, "6": 0.004721934697613155, "7": 0.0012717590573682635, "8": 0.0003025894719569696, "9": 6.443398683628703e-05} |
| Raw goal margin distribution | {"-1": 0.1475938384653806, "-10": 2.5610610322301317e-07, "-11": 3.0847047664008526e-08, "-12": 3.415889907248917e-09, "-13": 3.4997443322097055e-10, "-14": 3.33377699331061e-11, "-15": 2.9378815825387602e-12, "-16": 2.126876098529223e-13, "-2": 0.07379024679561144, "-3": 0.027748635586694364, "-4": 0.008347424168795149, "-5": 0.002081526971906988, "-6": 0.00044195731411007355, "-7": 8.156498505944107e-05, "-8": 1.329815246387431e-05, "-9": 1.9403991295824374e-06, "0": 0.22273218579186937, "1": 0.21636690769284717, "10": 1.1221068172904228e-05, "11": 1.9723741613099354e-06, "12": 3.1874324694801174e-07, "13": 4.765789689900358e-08, "14": 6.625162377518122e-09, "15": 8.520315874925012e-10, "16": 9.001710197731727e-11, "2": 0.1571526893226463, "3": 0.08624340910130333, "4": 0.03786153274881397, "5": 0.013778095133468234, "6": 0.0042692234791239245, "7": 0.0011498303079560946, "8": 0.00027357898000313215, "9": 5.825643662418448e-05} |
| Unadjusted home-win probability | 51.7% |
| Unadjusted draw probability | 22.3% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 64.0% |
| P home draw | 76.2% |
| P draw away | 42.8% |
| P home away | 81.0% |
| Raw p home draw | 74.0% |
| Raw p draw away | 48.3% |
| Raw p home away | 77.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.47, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.64, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.55 |
| Reference draw odds | 5.70 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.16 |
| Reference Under 2.5 odds | 5.10 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Home probability edge | -5.5% |
| Draw probability edge | +3.3% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -18.7% |
| Under 2.5 probability edge | +18.7% |
| Raw edge prob home | -0.1097 |
| Raw ev home | -0.1622 |
| Raw edge prob draw | 0.0663 |
| Raw ev draw | 0.3319 |
| Raw edge prob away | 0.0434 |
| Raw ev away | 0.0326 |
| Elo home rating | 1,739.3786 |
| Elo away rating | 1,656.5478 |
| Elo rating diff | 142.8309 |
| Elo home expectancy | 0.6947 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Real Betis win** at **38.2%**. Expected goals are 1.41 for Celta Vigo and 1.29 for Real Betis (2.70 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 50.2%; Under 3.5 goals: 71.5%; Double Chance 1X: 61.8%; Double Chance X2: 65.5%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 34.5% | 2.90 |
| Draw | 27.3% | 3.66 |
| Real Betis win | 38.2% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.41 |
| Real Betis expected goals | 1.29 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.2% |
| Under 2.5 | 49.8% |
| Over 3.5 | 28.5% |
| Under 3.5 | 71.5% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.97% |
| 2 | 0-1 | 9.43% |
| 3 | 1-2 | 8.85% |
| 4 | 1-0 | 8.01% |
| 5 | 2-1 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 34.5% | 29.2% | 3.15 | +8.8% |
| Draw | 27.3% | 28.3% | 3.53 | -3.6% |
| Real Betis win | 38.2% | 42.4% | 2.31 | -11.9% |
| Over 2.5 | 50.2% | 52.2% | 1.90 | -4.5% |
| Under 2.5 | 49.8% | 47.8% | 1.98 | -1.5% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
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
| Dc lambda home | 1.4143 |
| Dc lambda away | 1.2851 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.77 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.51 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.38 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.21400524379896438, "-10": 3.0225525885816493e-07, "-11": 3.483835075329253e-08, "-12": 3.6873201761025243e-09, "-13": 3.584714506136247e-10, "-14": 2.912506428783843e-11, "-2": 0.11017806770126175, "-3": 0.04142071088712313, "-4": 0.01225537232778262, "-5": 0.0029768955363920447, "-6": 0.0006119555395419299, "-7": 0.00010890132307250848, "-8": 1.70717344547872e-05, "-9": 2.3902490350557302e-06, "0": 0.2730534406310353, "1": 0.18155633610186128, "10": 6.064211107382512e-07, "11": 7.692287017281421e-08, "12": 8.959962461182247e-09, "13": 9.586219322988655e-10, "14": 8.571505884956331e-11, "2": 0.10273443074059936, "3": 0.04250459309028404, "4": 0.013840197002584811, "5": 0.003699787699221191, "6": 0.0008370097694120704, "7": 0.00016392351574834253, "8": 2.8280246981944144e-05, "9": 4.357587836623535e-06} |
| Raw goal margin distribution | {"-1": 0.1899899799867601, "-10": 2.6833674522153774e-07, "-11": 3.092885690505592e-08, "-12": 3.273536078025232e-09, "-13": 3.182444622332989e-10, "-14": 2.585670464391819e-11, "-2": 0.09781409327150291, "-3": 0.03677255703077301, "-4": 0.01088009761794903, "-5": 0.0026428339480928974, "-6": 0.0005432830459966556, "-7": 9.668062251088499e-05, "-8": 1.5155976693969216e-05, "-9": 2.122019807889439e-06, "0": 0.2629849671365445, "1": 0.2093590404189306, "10": 6.992856573328965e-07, "11": 8.870248558340052e-08, "12": 1.0332050003533448e-08, "13": 1.1054208967845219e-09, "14": 9.884106969491092e-11, "2": 0.11846671011123404, "3": 0.04901355146199027, "4": 0.0159596212717382, "5": 0.004266356212587014, "6": 0.000965185605238621, "7": 0.0001890260108571261, "8": 3.261095425294545e-05, "9": 5.024888844996662e-06} |
| Unadjusted home-win probability | 39.8% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 33.9% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 55.0% |
| P home draw | 61.8% |
| P draw away | 65.5% |
| P home away | 72.7% |
| Raw p home draw | 66.1% |
| Raw p draw away | 60.2% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.20 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:31:19Z |
| Market best under 2 5 last update utc | 2026-10-23T14:31:19Z |
| Home probability edge | +5.3% |
| Draw probability edge | -1.0% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | 0.1058 |
| Raw ev home | 0.2545 |
| Raw edge prob draw | -0.0201 |
| Raw ev draw | -0.0717 |
| Raw edge prob away | -0.0856 |
| Raw ev away | -0.2175 |
| Elo home rating | 1,477.2163 |
| Elo away rating | 1,549.1815 |
| Elo rating diff | -11.9651 |
| Elo home expectancy | 0.4828 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **59.1%**. Expected goals are 1.97 for Real Sociedad and 1.18 for Levante (3.16 combined). The most likely exact score is 2-1 at 10.4%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 61.6%; Under 3.5 goals: 60.9%; Double Chance 1X: 80.2%; Double Chance X2: 40.9%; Double Chance 12 (either team wins): 78.8%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 59.6%; BTTS No (at least one team does not score): 40.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 59.1% | 1.69 |
| Draw | 21.2% | 4.73 |
| Levante win | 19.8% | 5.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.97 |
| Levante expected goals | 1.18 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.5% |
| Under 4.5 | 78.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.44% |
| 2 | 1-1 | 9.68% |
| 3 | 2-0 | 8.82% |
| 4 | 1-0 | 8.71% |
| 5 | 3-1 | 6.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 59.1% | 62.7% | 1.63 | -3.7% |
| Draw | 21.2% | 20.1% | 4.48 | -5.2% |
| Levante win | 19.8% | 17.2% | 5.01 | -0.8% |
| Over 2.5 | 61.6% | 61.8% | 1.66 | +2.3% |
| Under 2.5 | 38.4% | 38.2% | 2.42 | -7.1% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9723 |
| Dc lambda away | 1.1843 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.6% |
| P btts no | 40.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.44 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.80 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.65 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.1195750777786497, "-10": 6.958496303972936e-08, "-11": 7.363319438402013e-09, "-12": 7.161048508230367e-10, "-13": 6.441777308402009e-11, "-14": 5.3874862289804246e-12, "-15": 4.17667361784456e-13, "-16": 2.6976808351840508e-14, "-2": 0.05405685000232792, "-3": 0.018152878565373797, "-4": 0.0048474186893576006, "-5": 0.0010691340447061416, "-6": 0.0002003202127505638, "-7": 3.257408030855441e-05, "-8": 4.674272030872808e-06, "-9": 5.998288321691852e-07, "0": 0.21150716205237358, "1": 0.2410895063296119, "10": 1.3734447678791286e-05, "11": 2.4203462319949436e-06, "12": 3.920022204459985e-07, "13": 5.8725358296941124e-08, "14": 8.179263463851674e-09, "15": 1.0560065697629567e-09, "16": 1.1358858885418477e-10, "2": 0.18033585407265595, "3": 0.100852090544342, "4": 0.044849539902626565, "5": 0.016473568071136997, "6": 0.005140298565695949, "7": 0.0013920146037352122, "8": 0.00033265470387728945, "9": 7.109107462166781e-05} |
| Raw goal margin distribution | {"-1": 0.13504849086228665, "-10": 7.858948887843713e-08, "-11": 8.316157483367193e-09, "-12": 8.087712021549821e-10, "-13": 7.275364734288681e-11, "-14": 6.084644879863645e-12, "-15": 4.717149086520998e-13, "-16": 3.046769714790589e-14, "-2": 0.06105198632692722, "-3": 0.0205019214756288, "-4": 0.00547469080293815, "-5": 0.0012074835488238924, "-6": 0.0002262423150688193, "-7": 3.678927472696709e-05, "-8": 5.279138390507321e-06, "-9": 6.774486796495316e-07, "0": 0.22195741924080334, "1": 0.22636649063150263, "10": 1.2895703214719738e-05, "11": 2.272538904703799e-06, "12": 3.6806316588827114e-07, "13": 5.513907872282779e-08, "14": 7.679766715898572e-09, "15": 9.915176521795001e-10, "16": 1.0665188471352498e-10, "2": 0.16932298316481276, "3": 0.09469318742625504, "4": 0.042110638114273416, "5": 0.015467549165512687, "6": 0.004826387364715508, "7": 0.001307006122135142, "8": 0.0003123399232723666, "9": 6.674963718797343e-05} |
| Unadjusted home-win probability | 55.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 22.4% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.2% |
| Raw p btts yes | 60.0% |
| P home draw | 80.2% |
| P draw away | 40.9% |
| P home away | 78.8% |
| Raw p home draw | 77.6% |
| Raw p draw away | 44.6% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.55 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:35Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:35Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.0% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0721 |
| Raw ev home | -0.0962 |
| Raw edge prob draw | 0.0209 |
| Raw ev draw | -0.0056 |
| Raw edge prob away | 0.0512 |
| Raw ev away | 0.1200 |
| Elo home rating | 1,485.8012 |
| Elo away rating | 1,453.6938 |
| Elo rating diff | 92.1074 |
| Elo home expectancy | 0.6295 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **49.5%**. Expected goals are 1.51 for Sevilla and 1.06 for CA Osasuna (2.57 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.2%; Double Chance 1X: 76.1%; Double Chance X2: 50.5%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 49.5% | 2.02 |
| Draw | 26.6% | 3.76 |
| CA Osasuna win | 23.9% | 4.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.51 |
| CA Osasuna expected goals | 1.06 |
| Expected total goals | 2.57 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 11.80% |
| 3 | 2-1 | 9.65% |
| 4 | 2-0 | 9.12% |
| 5 | 0-0 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 49.5% | 51.5% | 1.93 | -4.5% |
| Draw | 26.6% | 26.9% | 3.48 | -7.4% |
| CA Osasuna win | 23.9% | 21.5% | 4.31 | +3.1% |
| Over 2.5 | 47.4% | 45.2% | 2.19 | +3.7% |
| Under 2.5 | 52.6% | 54.8% | 1.79 | -5.8% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
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
| Dc lambda home | 1.5108 |
| Dc lambda away | 1.0581 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.46 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.44 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.14824346210077208, "-10": 3.905570903112297e-08, "-11": 3.7124090428803122e-09, "-12": 3.240576677804637e-10, "-13": 2.6143947634131353e-11, "-14": 1.9518218803561063e-12, "-15": 1.2442481167373264e-13, "-2": 0.0644525952366149, "-3": 0.020228631674721904, "-4": 0.004973057688695642, "-5": 0.0010009934662629713, "-6": 0.00017022724878989332, "-7": 2.5032493252491108e-05, "-8": 3.2402537697872477e-06, "-9": 3.744011450154189e-07, "0": 0.2661808118889286, "1": 0.24392882636142876, "10": 1.5772934234383547e-06, "11": 2.1407267715503141e-07, "12": 2.6681188615001145e-08, "13": 3.073487762854104e-09, "14": 3.276256971059782e-10, "15": 2.9821001207994717e-11, "2": 0.15067762132622237, "3": 0.0675230895733102, "4": 0.02370209576093559, "5": 0.006811957762086876, "6": 0.0016540446781203636, "7": 0.00034729594805977897, "8": 6.418774012341393e-05, "9": 1.0589798139821737e-05} |
| Raw goal margin distribution | {"-1": 0.16292190484848657, "-10": 4.29228407134297e-08, "-11": 4.0799961379184295e-09, "-12": 3.5614449209005754e-10, "-13": 2.8732611128012635e-11, "-14": 2.1450830557128184e-12, "-15": 1.3674483205551866e-13, "-2": 0.07083441953912041, "-3": 0.022231585516289412, "-4": 0.0054654688988101125, "-5": 0.0011001076199474646, "-6": 0.00018708243343044673, "-7": 2.7511105218457365e-05, "-8": 3.5610900398924115e-06, "-9": 4.114727682351448e-07, "0": 0.263082763678371, "1": 0.23378337010948877, "10": 1.5116908390178658e-06, "11": 2.051689940061034e-07, "12": 2.5571468062981732e-08, "13": 2.9456556566449472e-09, "14": 3.1399913141228274e-10, "15": 2.8580689975994295e-11, "2": 0.14441065715427773, "3": 0.06471467794980326, "4": 0.02271628125426649, "5": 0.006528635694350139, "6": 0.001585249865424631, "7": 0.0003328512598280741, "8": 6.151805192359418e-05, "9": 1.0149348622857944e-05} |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 72.9% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.1% |
| P home draw | 76.1% |
| P draw away | 50.5% |
| P home away | 73.4% |
| Raw p home draw | 73.7% |
| Raw p draw away | 52.6% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.48, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.96, "price": 1.48, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.80 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:35Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:35Z |
| Home probability edge | -2.1% |
| Draw probability edge | -0.3% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | +2.2% |
| Under 2.5 probability edge | -2.2% |
| Raw edge prob home | -0.0412 |
| Raw ev home | -0.0849 |
| Raw edge prob draw | -0.0062 |
| Raw ev draw | -0.0845 |
| Raw edge prob away | 0.0473 |
| Raw ev away | 0.1325 |
| Elo home rating | 1,440.7731 |
| Elo away rating | 1,423.7802 |
| Elo rating diff | 76.9929 |
| Elo home expectancy | 0.6090 |

</details>


---

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **63.8%**. Expected goals are 2.18 for Villarreal and 0.98 for Espanyol (3.16 combined). The most likely exact score is 2-0 at 10.0%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.0%; Under 3.5 goals: 61.3%; Double Chance 1X: 84.0%; Double Chance X2: 36.2%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 78.9%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 63.8% | 1.57 |
| Draw | 20.2% | 4.94 |
| Espanyol win | 16.0% | 6.25 |

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
| 1 | 2-0 | 9.97% |
| 2 | 2-1 | 9.77% |
| 3 | 1-1 | 9.44% |
| 4 | 1-0 | 8.95% |
| 5 | 3-0 | 7.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 63.8% | 63.0% | 1.56 | -0.5% |
| Draw | 20.2% | 20.6% | 4.31 | -12.8% |
| Espanyol win | 16.0% | 16.4% | 5.40 | -13.6% |
| Over 2.5 | 61.0% | 60.9% | 1.66 | +1.2% |
| Under 2.5 | 39.0% | 39.1% | 2.42 | -5.6% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
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
| Dc lambda away | 0.9794 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.07 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.70 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.58 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.74 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.10532872196001253, "-10": 1.1794222684024048e-08, "-11": 1.0336483219543087e-09, "-12": 8.323912855617857e-11, "-13": 6.199281670423893e-12, "-14": 4.293645402479567e-13, "-15": 2.778210730039751e-14, "-16": 1.6764881620835549e-15, "-17": 8.581133005270586e-17, "-2": 0.04025534863671359, "-3": 0.011312625996266432, "-4": 0.00251823254529523, "-5": 0.00046194624946761375, "-6": 7.188360151607191e-05, "-7": 9.69848093708257e-06, "-8": 1.1539305626655534e-06, "-9": 1.2272013894310843e-07, "0": 0.20242093740071343, "1": 0.22878942890152495, "10": 3.395953993693845e-05, "11": 6.623896941657865e-06, "12": 1.187180011901269e-06, "13": 1.967789816180842e-07, "14": 3.0332751146662274e-08, "15": 4.368165655743004e-09, "16": 5.866548898939833e-10, "17": 6.683056387541178e-11, "2": 0.19254389879836395, "3": 0.12042534155015674, "4": 0.059662105817876065, "5": 0.024358047848470555, "6": 0.0084358558505215, "7": 0.0025330941193546716, "8": 0.000670773002205433, "9": 0.00015876692185989166} |
| Raw goal margin distribution | {"-1": 0.10289983595500858, "-10": 1.1522247273290384e-08, "-11": 1.0098123359424042e-09, "-12": 8.131962976556771e-11, "-13": 6.056325900998659e-12, "-14": 4.1946337080958505e-13, "-15": 2.7141450408756198e-14, "-16": 1.637828254712938e-15, "-17": 8.38325161569584e-17, "-2": 0.03932705812762159, "-3": 0.011051756231107724, "-4": 0.002460161967082621, "-5": 0.000451293744058672, "-6": 7.022596179100288e-05, "-7": 9.474833443981679e-06, "-8": 1.1273208617003334e-06, "-9": 1.1989020592517796e-07, "0": 0.19863977993787668, "1": 0.231469742835065, "10": 3.43573827415934e-05, "11": 6.7014972195741175e-06, "12": 1.2010880632600963e-06, "13": 1.9908428675736055e-07, "14": 3.0688105395026594e-08, "15": 4.419339590340036e-09, "16": 5.935276693012829e-10, "17": 6.761349730201999e-11, "2": 0.19479958909509312, "3": 0.12183614851994522, "4": 0.060361059324145025, "5": 0.024643407252336158, "6": 0.008534683589574165, "7": 0.0025627698237596906, "8": 0.0006786312421279932, "9": 0.00016062690811401837} |
| Unadjusted home-win probability | 64.5% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 15.6% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.2% |
| Raw p btts yes | 55.6% |
| P home draw | 84.0% |
| P draw away | 36.2% |
| P home away | 79.8% |
| Raw p home draw | 84.4% |
| Raw p draw away | 35.5% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.50 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:35Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:35Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.0149 |
| Raw ev home | 0.0063 |
| Raw edge prob draw | -0.0076 |
| Raw ev draw | -0.1439 |
| Raw edge prob away | -0.0074 |
| Raw ev away | -0.1561 |
| Elo home rating | 1,558.8984 |
| Elo away rating | 1,440.6093 |
| Elo rating diff | 178.2890 |
| Elo home expectancy | 0.7362 |

</details>


---

## 2026-10-31 — Barcelona vs Alavés

The model's most likely 1X2 outcome is **Barcelona win** at **85.2%**. Expected goals are 2.84 for Barcelona and 0.70 for Alavés (3.54 combined). The most likely exact score is 2-0 at 12.3%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 70.2%; Under 3.5 goals: 51.8%; Double Chance 1X: 95.0%; Double Chance X2: 14.8%; Double Chance 12 (either team wins): 90.2%; Under 4.5 goals: 70.8%; BTTS Yes (both teams score): 46.6%; BTTS No (at least one team does not score): 53.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 85.2% | 1.17 |
| Draw | 9.8% | 10.18 |
| Alavés win | 5.0% | 20.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.84 |
| Alavés expected goals | 0.70 |
| Expected total goals | 3.54 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 87.6% |
| Under 1.5 | 12.4% |
| Over 2.5 | 70.2% |
| Under 2.5 | 29.8% |
| Over 3.5 | 48.2% |
| Under 3.5 | 51.8% |
| Over 4.5 | 29.2% |
| Under 4.5 | 70.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.27% |
| 2 | 3-0 | 11.61% |
| 3 | 2-1 | 8.62% |
| 4 | 1-0 | 8.51% |
| 5 | 4-0 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 85.2% | 89.4% | 1.16 | -1.1% |
| Draw | 9.8% | 7.1% | 6.48 | -36.4% |
| Alavés win | 5.0% | 3.5% | 23.04 | +14.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:00:00+00:00 |
| Fixture id | 2db2b55e71574a19ff0557898d3e9933 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8383 |
| Dc lambda away | 0.7026 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.6% |
| P btts no | 53.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.19 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.09 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.35 |
| Fair Over 3.5 odds | 2.07 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.43 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.03678141931332425, "-10": 2.1754209306199452e-10, "-11": 1.3690367205039309e-11, "-12": 7.915383272239534e-13, "-13": 4.2319011112198877e-14, "-14": 2.1039330805536755e-15, "-15": 9.773912747254732e-17, "-16": 4.260787188225131e-18, "-17": 1.7492703861268542e-19, "-18": 6.7565845358870624e-21, "-19": 2.2611298350191116e-22, "-2": 0.0102981208582897, "-3": 0.002093656870794425, "-4": 0.00033622048318880947, "-5": 4.442119953747426e-05, "-6": 4.9733555059494786e-06, "-7": 4.824423932287156e-07, "-8": 4.125112608597068e-08, "-9": 3.151639785427943e-09, "0": 0.09822087880909271, "1": 0.20531031943612302, "10": 0.0003410378217559151, "11": 8.670213328065371e-05, "12": 2.0250795048313105e-05, "13": 4.373821787612248e-06, "14": 8.784416889792556e-07, "15": 1.6485606036475783e-07, "16": 2.9032320253111604e-08, "17": 4.815088678632488e-09, "18": 7.513287438000751e-10, "19": 1.0157427540968841e-10, "2": 0.22760074600289118, "3": 0.18692898455950133, "4": 0.12126926666383782, "5": 0.06472503718062547, "6": 0.029274330698743994, "7": 0.011471979872973263, "8": 0.003962635856750503, "9": 0.0012230391916586703} |
| Raw goal margin distribution | {"-1": 0.04738700906524371, "-10": 2.802683889978781e-10, "-11": 1.763786082655874e-11, "-12": 1.0197712483069304e-12, "-13": 5.452131539903524e-14, "-14": 2.7105831646019883e-15, "-15": 1.2592132130944722e-16, "-16": 5.4893466560806986e-18, "-17": 2.2536566884173314e-19, "-18": 8.704784606726173e-21, "-19": 2.91310618214585e-22, "-2": 0.013267490911911874, "-3": 0.0026973439026564457, "-4": 0.0004331666200552819, "-5": 5.722965085278127e-05, "-6": 6.407377606544241e-06, "-7": 6.21550295997015e-07, "-8": 5.314551537926322e-08, "-9": 4.060386626471345e-09, "0": 0.12541811345007195, "1": 0.19531553288623194, "10": 0.0003244356351573468, "11": 8.248135510476689e-05, "12": 1.9264958707843853e-05, "13": 4.160898173765119e-06, "14": 8.356779486958301e-07, "15": 1.5683064235689996e-07, "16": 2.761898728098007e-08, "17": 4.580683590306171e-09, "18": 7.147530351669009e-10, "19": 9.66295010580244e-11, "2": 0.21652083106660067, "3": 0.17782902647755322, "4": 0.11536571325894439, "5": 0.06157413403639561, "6": 0.027849216327832393, "7": 0.010913508236233702, "8": 0.0037697293351886957, "9": 0.0011634999746512032} |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 12.5% |
| Unadjusted away-win probability | 6.4% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 52.8% |
| Raw p btts yes | 47.6% |
| P home draw | 95.0% |
| P draw away | 14.8% |
| P home away | 90.2% |
| Raw p home draw | 93.6% |
| Raw p draw away | 18.9% |
| Raw p home away | 87.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.09 |
| Reference draw odds | 7.60 |
| Reference away odds | 13.00 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.23 |
| Reference Under 2.5 odds | 4.05 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Home probability edge | -4.1% |
| Draw probability edge | +2.7% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | -0.0830 |
| Raw ev home | -0.0596 |
| Raw edge prob draw | 0.0544 |
| Raw ev draw | -0.1873 |
| Raw edge prob away | 0.0286 |
| Raw ev away | 0.4711 |
| Elo home rating | 1,739.3786 |
| Elo away rating | 1,440.0805 |
| Elo rating diff | 359.2981 |
| Elo home expectancy | 0.8878 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **57.1%**. Expected goals are 1.23 for Levante and 1.94 for Atlético Madrid (3.16 combined). The most likely exact score is 1-2 at 10.4%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.8%; Double Chance 1X: 42.9%; Double Chance X2: 78.7%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 78.4%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 21.3% | 4.70 |
| Draw | 21.6% | 4.64 |
| Atlético Madrid win | 57.1% | 1.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.23 |
| Atlético Madrid expected goals | 1.94 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.2% |
| Under 3.5 | 60.8% |
| Over 4.5 | 21.6% |
| Under 4.5 | 78.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.35% |
| 2 | 1-1 | 9.84% |
| 3 | 0-1 | 8.48% |
| 4 | 0-2 | 8.44% |
| 5 | 1-3 | 6.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 21.3% | 18.8% | 4.52 | -3.7% |
| Draw | 21.6% | 20.6% | 4.59 | -1.0% |
| Atlético Madrid win | 57.1% | 60.6% | 1.62 | -7.4% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Levante |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2269 |
| Dc lambda away | 1.9354 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.44 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.81 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.64 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.23851204206396487, "-10": 1.1341319040364653e-05, "-11": 1.9607113469285937e-06, "-12": 3.1154912866824184e-07, "-13": 4.579092462087116e-08, "-14": 6.257294313453233e-09, "-15": 7.9242782035264e-10, "-16": 8.346685805604901e-11, "-2": 0.17448600722094082, "-3": 0.09554138149965698, "-4": 0.04163027097324572, "-5": 0.014988988647895688, "-6": 0.004585918597799637, "-7": 0.0012179106200287722, "-8": 0.0002854664222129538, "-9": 5.984209656596869e-05, "0": 0.21570696134123865, "1": 0.12634430515078268, "10": 9.991378535976615e-08, "11": 1.0950211787707633e-08, "12": 1.1030175158897868e-09, "13": 1.02773771092517e-10, "14": 8.903002050856394e-12, "15": 7.147540360373846e-13, "16": 4.7726323334715204e-14, "2": 0.05893134584130501, "3": 0.020456168046062637, "4": 0.005650527788445574, "5": 0.0012897309426257828, "6": 0.0002501497893779853, "7": 4.2114944126071455e-05, "8": 6.257816942089904e-06, "9": 8.316136988459466e-07} |
| Raw goal margin distribution | {"-1": 0.22405268639914203, "-10": 1.0653772347569658e-05, "-11": 1.8418468129790196e-06, "-12": 2.9266203341092294e-07, "-13": 4.3014933691504576e-08, "-14": 5.87795730725952e-09, "-15": 7.443883352430946e-10, "-16": 7.840683267362396e-11, "-2": 0.16390811264123736, "-3": 0.08974936025050939, "-4": 0.039106512050148326, "-5": 0.014080308666623333, "-6": 0.00430790568288892, "-7": 0.0011440770195506962, "-8": 0.00026816054325848733, "-9": 5.621427907512702e-05, "0": 0.22526299870432176, "1": 0.14122246383399836, "10": 1.1167951671939716e-07, "11": 1.2239696014146661e-08, "12": 1.2329075779087236e-09, "13": 1.148762910514665e-10, "14": 9.951409235585096e-12, "15": 7.989226414600185e-13, "16": 5.3346519758233655e-14, "2": 0.06587103270567152, "3": 0.022865062644648836, "4": 0.006315927380299614, "5": 0.0014416081609945832, "6": 0.00027960713814013954, "7": 4.7074351049040094e-05, "8": 6.9947301995874666e-06, "9": 9.295435624816666e-07} |
| Unadjusted home-win probability | 23.8% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 82.6% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.7% |
| P home draw | 42.9% |
| P draw away | 78.7% |
| P home away | 78.4% |
| Raw p home draw | 46.3% |
| Raw p draw away | 76.2% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 4.80 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.60 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Home probability edge | +2.5% |
| Draw probability edge | +1.0% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.0502 |
| Raw ev home | 0.0760 |
| Raw edge prob draw | 0.0191 |
| Raw ev draw | 0.0340 |
| Raw edge prob away | -0.0693 |
| Raw ev away | -0.1306 |
| Elo home rating | 1,479.7866 |
| Elo away rating | 1,584.7626 |
| Elo rating diff | -44.9761 |
| Elo home expectancy | 0.4356 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **40.7%**. Expected goals are 1.21 for Rayo Vallecano and 1.09 for Celta Vigo (2.30 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 40.7%; Under 3.5 goals: 79.8%; Double Chance 1X: 68.8%; Double Chance X2: 59.3%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 46.7%; BTTS No (at least one team does not score): 53.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 40.7% | 2.46 |
| Draw | 28.1% | 3.56 |
| Celta Vigo win | 31.2% | 3.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.21 |
| Celta Vigo expected goals | 1.09 |
| Expected total goals | 2.30 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
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
| 1 | 1-1 | 13.16% |
| 2 | 1-0 | 12.46% |
| 3 | 0-1 | 10.18% |
| 4 | 0-0 | 10.03% |
| 5 | 2-1 | 8.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 40.7% | 42.6% | 2.35 | -4.4% |
| Draw | 28.1% | 27.4% | 3.46 | -2.7% |
| Celta Vigo win | 31.2% | 30.0% | 2.99 | -6.7% |
| Over 2.5 | 40.7% | 47.5% | 2.11 | -14.1% |
| Under 2.5 | 59.3% | 52.5% | 1.84 | +9.1% |

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
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
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
| Dc lambda away | 1.0876 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.7% |
| P btts no | 53.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.97 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.46 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.80 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.18801352038762922, "-10": 6.919531299955303e-08, "-11": 6.774140956782303e-09, "-12": 6.087552915759061e-10, "-13": 5.037355105468329e-11, "-14": 3.5757508505062964e-12, "-2": 0.08650514203684923, "-3": 0.028417756865221862, "-4": 0.007266263397632748, "-5": 0.001515760050944065, "-6": 0.00026655590309248006, "-7": 4.0476357715887e-05, "-8": 5.404892354337092e-06, "-9": 6.43798869594696e-07, "0": 0.2812173503955158, "1": 0.22970158124008805, "10": 2.286709735376968e-07, "11": 2.5008166701359428e-08, "12": 2.5105197344269403e-09, "13": 2.3206878119570038e-10, "14": 1.8402408565542334e-11, "2": 0.11787729880847701, "3": 0.043258485432242685, "4": 0.01235622807888824, "5": 0.002879376792855047, "6": 0.0005656523710751923, "7": 9.595243412337175e-05, "8": 1.4313138828242835e-05, "9": 1.9045453070336163e-06} |
| Raw goal margin distribution | {"-1": 0.19539058250086402, "-10": 7.191032052076751e-08, "-11": 7.039937046866464e-09, "-12": 6.326409439931206e-10, "-13": 5.2350051543735636e-11, "-14": 3.716052122836351e-12, "-2": 0.089899333074836, "-3": 0.029532780705429366, "-4": 0.007551368832098025, "-5": 0.001575233731461937, "-6": 0.0002770147224885983, "-7": 4.206452331361629e-05, "-8": 5.616963414604927e-06, "-9": 6.690595223373213e-07, "0": 0.28860891521476634, "1": 0.21861341431345194, "10": 2.1763255616079515e-07, "11": 2.380097115043293e-08, "12": 2.3893317924996083e-09, "13": 2.2086634466711004e-10, "14": 1.7514086522109746e-11, "2": 0.11218711958118115, "3": 0.04117030952645814, "4": 0.011759767580955932, "5": 0.0027403833634171877, "6": 0.0005383471697828529, "7": 9.132061312835232e-05, "8": 1.362221423070691e-05, "9": 1.8126089948422892e-06} |
| Unadjusted home-win probability | 38.7% |
| Unadjusted draw probability | 28.9% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 67.3% |
| Raw p under 3 5 | 79.9% |
| Raw p btts yes | 46.9% |
| P home draw | 68.8% |
| P draw away | 59.3% |
| P home away | 71.9% |
| Raw p home draw | 67.6% |
| Raw p draw away | 61.3% |
| Raw p home away | 71.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.04, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.80 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:35Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:35Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | -0.0393 |
| Raw ev home | -0.0903 |
| Raw edge prob draw | 0.0148 |
| Raw ev draw | -0.0014 |
| Raw edge prob away | 0.0245 |
| Raw ev away | -0.0304 |
| Elo home rating | 1,498.4715 |
| Elo away rating | 1,513.3163 |
| Elo rating diff | 45.1552 |
| Elo home expectancy | 0.5646 |

</details>


---

## 2026-10-31 — Real Betis vs Málaga

The model's most likely 1X2 outcome is **Real Betis win** at **74.4%**. Expected goals are 2.42 for Real Betis and 0.55 for Málaga (2.97 combined). The most likely exact score is 2-0 at 14.2%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.8%; Under 3.5 goals: 66.5%; Double Chance 1X: 90.4%; Double Chance X2: 25.6%; Double Chance 12 (either team wins): 83.9%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 39.4%; BTTS No (at least one team does not score): 60.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 74.4% | 1.34 |
| Draw | 16.1% | 6.22 |
| Málaga win | 9.6% | 10.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 2.42 |
| Málaga expected goals | 0.55 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 33.5% |
| Under 3.5 | 66.5% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.21% |
| 2 | 1-0 | 11.62% |
| 3 | 3-0 | 11.44% |
| 4 | 2-1 | 7.83% |
| 5 | 1-1 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 74.4% | 70.1% | 1.38 | +2.6% |
| Draw | 16.1% | 17.2% | 5.27 | -15.3% |
| Málaga win | 9.6% | 12.7% | 6.89 | -34.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:30:00+00:00 |
| Fixture id | 8f0b7ef29a47f675429758e83a426d7e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Betis |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4153 |
| Dc lambda away | 0.5511 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 39.4% |
| P btts no | 60.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.55 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.70 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.78 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.07461694850290816, "-10": 6.122788186926939e-11, "-11": 3.0373729733801943e-12, "-12": 1.3832992313088207e-13, "-13": 5.8222458314893176e-15, "-14": 2.2776981799260004e-16, "-15": 8.322939309703242e-18, "-16": 2.852866837191419e-19, "-17": 9.187032747306968e-21, "-18": 2.6192665731733186e-22, "-2": 0.017636377022583808, "-3": 0.0029340848329108857, "-4": 0.00038002345391004166, "-5": 4.016080827420266e-05, "-6": 3.5782224885109774e-06, "-7": 2.753023118860361e-07, "-8": 1.8626883458151814e-08, "-9": 1.1242399414686825e-09, "0": 0.16076422407380916, "1": 0.21399781270184823, "10": 0.00010232653160974334, "11": 2.224591878338688e-05, "12": 4.439985620046646e-06, "13": 8.189722217627203e-07, "14": 1.404067582783552e-07, "15": 2.2484424204200887e-08, "16": 3.377534143927987e-09, "17": 4.766578137505329e-10, "18": 5.955584044092165e-11, "2": 0.2166420485463705, "3": 0.15794986190375804, "4": 0.0896541071405467, "5": 0.04152172986746963, "6": 0.0162126325429005, "7": 0.005466498862331682, "8": 0.0016208872490119154, "9": 0.0004287309378680311} |
| Raw goal margin distribution | {"-1": 0.050434615180018655, "-10": 4.138476207243839e-11, "-11": 2.0530019002941226e-12, "-12": 9.349908540840006e-14, "-13": 3.935335522105771e-15, "-14": 1.5395273259709824e-16, "-15": 5.625588417558687e-18, "-16": 1.9282916814532877e-19, "-17": 6.2096409804080625e-21, "-18": 1.770398070710891e-22, "-2": 0.011920668241600235, "-3": 0.0019831880346543843, "-4": 0.0002568630457541092, "-5": 2.714523913489947e-05, "-6": 2.4185694786152547e-06, "-7": 1.8608059478069594e-07, "-8": 1.2590165077285728e-08, "-9": 7.598891398751025e-10, "0": 0.14952819939422257, "1": 0.22614843775453494, "10": 0.00010813655042645037, "11": 2.3509024301507534e-05, "12": 4.692084460812234e-06, "13": 8.654728110424287e-07, "14": 1.4837894198044025e-07, "15": 2.3761071869807797e-08, "16": 3.5693078376278096e-09, "17": 5.037220640818452e-10, "18": 6.293737354053087e-11, "2": 0.22894281120042811, "3": 0.1669181290317502, "4": 0.09474459580743752, "5": 0.043879300558444315, "6": 0.01713317288234889, "7": 0.005776882305921698, "8": 0.0017129199336770825, "9": 0.0004530739384284111} |
| Unadjusted home-win probability | 78.6% |
| Unadjusted draw probability | 15.0% |
| Unadjusted away-win probability | 6.5% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.5% |
| Raw p btts yes | 38.7% |
| P home draw | 90.4% |
| P draw away | 25.6% |
| P home away | 83.9% |
| Raw p home draw | 93.5% |
| Raw p draw away | 21.4% |
| Raw p home away | 85.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.36 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Home probability edge | +4.2% |
| Draw probability edge | -1.1% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | 0.0844 |
| Raw ev home | 0.0845 |
| Raw edge prob draw | -0.0225 |
| Raw ev draw | -0.2120 |
| Raw edge prob away | -0.0620 |
| Raw ev away | -0.5547 |
| Elo home rating | 1,565.6917 |
| Elo away rating | 1,401.2778 |
| Elo rating diff | 224.4139 |
| Elo home expectancy | 0.7845 |

</details>


---

## 2026-11-01 — Athletic Bilbao vs Real Sociedad

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **47.6%**. Expected goals are 1.44 for Athletic Bilbao and 0.99 for Real Sociedad (2.43 combined). The most likely exact score is 1-0 at 12.5%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.0%; Under 3.5 goals: 77.3%; Double Chance 1X: 74.0%; Double Chance X2: 52.4%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 47.6% | 2.10 |
| Draw | 26.4% | 3.79 |
| Real Sociedad win | 26.0% | 3.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.44 |
| Real Sociedad expected goals | 0.99 |
| Expected total goals | 2.43 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.0% |
| Under 2.5 | 56.0% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.51% |
| 2 | 1-1 | 12.46% |
| 3 | 2-0 | 9.23% |
| 4 | 2-1 | 9.09% |
| 5 | 0-0 | 8.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 47.6% | 47.9% | 2.06 | -1.9% |
| Draw | 26.4% | 25.6% | 3.58 | -5.5% |
| Real Sociedad win | 26.0% | 26.5% | 3.50 | -9.0% |
| Over 2.5 | 44.0% | 52.2% | 1.87 | -17.7% |
| Under 2.5 | 56.0% | 47.8% | 1.97 | +10.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T20:00:00+00:00 |
| Fixture id | 3757bcd765c7da1538cdf2785e784038 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4429 |
| Dc lambda away | 0.9857 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.31 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 9.98 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.16564302909002904, "-10": 2.4384314480109447e-08, "-11": 2.161857454418696e-09, "-12": 1.7595053805971356e-10, "-13": 1.3180483146967993e-11, "-14": 8.423804308004334e-13, "-2": 0.06842643189488248, "-3": 0.02023591741250374, "-4": 0.00466895025238015, "-5": 0.000880008046183261, "-6": 0.0001399401830845433, "-7": 1.9225675467675157e-05, "-8": 2.3235379218337715e-06, "-9": 2.505574086534125e-07, "0": 0.2638902262941642, "1": 0.2403125638937814, "10": 1.086552855750194e-06, "11": 1.4102210949412032e-07, "12": 1.6802372042717526e-08, "13": 1.84260045029432e-09, "14": 1.7239630663242078e-10, "2": 0.14454578718873312, "3": 0.06257837593873287, "4": 0.021136860519566113, "5": 0.005832137082159529, "6": 0.0013576985787525718, "7": 0.00027306269865620285, "8": 4.8311484339891367e-05, "9": 7.626542773378909e-06} |
| Raw goal margin distribution | {"-1": 0.16243270066006188, "-10": 2.3911721951158476e-08, "-11": 2.119958483568044e-09, "-12": 1.7254043974344748e-10, "-13": 1.292503213282108e-11, "-14": 8.260542511796973e-13, "-2": 0.0671002588534926, "-3": 0.019843724989238403, "-4": 0.004578461302644922, "-5": 0.0008629526055481678, "-6": 0.00013722800165005052, "-7": 1.885306254892894e-05, "-8": 2.2785054209821017e-06, "-9": 2.457013541803821e-07, "0": 0.2713805624821833, "1": 0.239075418416681, "10": 1.080959207505835e-06, "11": 1.402961180515384e-07, "12": 1.6715872284900476e-08, "13": 1.8331146174429324e-09, "14": 1.7150879868209412e-10, "2": 0.14380165561293465, "3": 0.062256218189248286, "4": 0.021028046519298356, "5": 0.005802112842493839, "6": 0.0013507090538240633, "7": 0.000271656953250579, "8": 4.806277352188553e-05, "9": 7.587280810770211e-06} |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 25.5% |
| Raw p over 1 5 | 70.1% |
| Raw p under 3 5 | 77.3% |
| Raw p btts yes | 48.2% |
| P home draw | 74.0% |
| P draw away | 52.4% |
| P home away | 73.6% |
| Raw p home draw | 74.5% |
| Raw p draw away | 52.6% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.52, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.79, "price": 1.52, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.94 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:31:19Z |
| Market best under 2 5 last update utc | 2026-10-23T14:31:19Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | -0.0049 |
| Raw ev home | -0.0243 |
| Raw edge prob draw | 0.0150 |
| Raw ev draw | -0.0285 |
| Raw edge prob away | -0.0101 |
| Raw ev away | -0.1076 |
| Elo home rating | 1,491.3653 |
| Elo away rating | 1,506.9598 |
| Elo rating diff | 44.4055 |
| Elo home expectancy | 0.5636 |

</details>


---

## 2026-11-01 — Elche CF vs Valencia

The model's most likely 1X2 outcome is **Elche CF win** at **40.9%**. Expected goals are 1.37 for Elche CF and 1.10 for Valencia (2.47 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 44.9%; Under 3.5 goals: 76.4%; Double Chance 1X: 68.2%; Double Chance X2: 59.1%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 40.9% | 2.44 |
| Draw | 27.3% | 3.66 |
| Valencia win | 31.8% | 3.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elche CF expected goals | 1.37 |
| Valencia expected goals | 1.10 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 44.9% |
| Under 2.5 | 55.1% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.96% |
| 2 | 1-0 | 10.84% |
| 3 | 0-1 | 9.59% |
| 4 | 0-0 | 8.68% |
| 5 | 2-1 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 40.9% | 39.3% | 2.48 | +1.4% |
| Draw | 27.3% | 27.1% | 3.37 | -8.0% |
| Valencia win | 31.8% | 33.5% | 2.86 | -9.1% |
| Over 2.5 | 44.9% | 50.0% | 1.97 | -11.6% |
| Under 2.5 | 55.1% | 50.0% | 1.87 | +3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T17:30:00+00:00 |
| Fixture id | 5262991e389930615bec34b642428c93 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Elche |
| Matched away-team name | Valencia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3658 |
| Dc lambda away | 1.1047 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.52 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.54 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.19174682101059112, "-10": 7.65255323938177e-08, "-11": 7.599449512457793e-09, "-12": 6.928423597328464e-10, "-13": 5.8114754584702753e-11, "-14": 4.139680312358814e-12, "-2": 0.08780142543677844, "-3": 0.028938176000465925, "-4": 0.007455869335448097, "-5": 0.0015710178534997692, "-6": 0.0002794791650190424, "-7": 4.297296618052258e-05, "-8": 5.814383710248262e-06, "-9": 7.020965640575119e-07, "0": 0.2731062399995154, "1": 0.2162091348121016, "10": 5.805445298698486e-07, "11": 7.127572890994193e-08, "12": 8.033861143453245e-09, "13": 8.331182590510667e-10, "14": 7.336981166464243e-11, "2": 0.12203598161504293, "3": 0.04972649416470477, "4": 0.0158396409154055, "5": 0.004126278335929318, "6": 0.0009075220627628509, "7": 0.00017251761366798886, "8": 2.885839377851259e-05, "9": 4.3081981471437456e-06} |
| Raw goal margin distribution | {"-1": 0.1811559604464714, "-10": 7.22987544013253e-08, "-11": 7.179704821378599e-09, "-12": 6.545742059967228e-10, "-13": 5.4904869491011276e-11, "-14": 3.91103100940217e-12, "-2": 0.08295183966930168, "-3": 0.027339817365962346, "-4": 0.007044055089455118, "-5": 0.0014842449362619926, "-6": 0.00026404253430103015, "-7": 4.059941604578835e-05, "-8": 5.493234567764552e-06, "-9": 6.633172676222925e-07, "0": 0.2747251575757744, "1": 0.22463264636650057, "10": 6.031625545867582e-07, "11": 7.405263251553138e-08, "12": 8.346860509678576e-09, "13": 8.655765605349343e-10, "14": 7.622830076982429e-11, "2": 0.12679050552579302, "3": 0.051663839219621914, "4": 0.016456753593759272, "5": 0.004287038209787439, "6": 0.0009428791376995707, "7": 0.00017923890281857245, "8": 2.9982717288922793e-05, "9": 4.4760456199281105e-06} |
| Unadjusted home-win probability | 42.5% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 30.0% |
| Raw p over 1 5 | 70.9% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 50.1% |
| P home draw | 68.2% |
| P draw away | 59.1% |
| P home away | 72.7% |
| Raw p home draw | 70.0% |
| Raw p draw away | 57.5% |
| Raw p home away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.65 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market best over 2 5 last update utc | 2026-10-23T14:31:19Z |
| Market best under 2 5 last update utc | 2026-10-23T14:31:19Z |
| Home probability edge | +1.6% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.0319 |
| Raw ev home | 0.0540 |
| Raw edge prob draw | 0.0032 |
| Raw ev draw | -0.0742 |
| Raw edge prob away | -0.0351 |
| Raw ev away | -0.1412 |
| Elo home rating | 1,460.0313 |
| Elo away rating | 1,451.1044 |
| Elo rating diff | 68.9269 |
| Elo home expectancy | 0.5979 |

</details>


---

## 2026-11-01 — Getafe vs Sevilla

The model's most likely 1X2 outcome is **Getafe win** at **35.4%**. Expected goals are 1.05 for Getafe and 0.90 for Sevilla (1.95 combined). The most likely exact score is 0-0 at 14.3%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 31.1%; Under 3.5 goals: 86.6%; Double Chance 1X: 66.6%; Double Chance X2: 64.6%; Double Chance 12 (either team wins): 68.8%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.7%; BTTS No (at least one team does not score): 61.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.4% | 2.83 |
| Draw | 31.2% | 3.21 |
| Sevilla win | 33.4% | 2.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 1.05 |
| Sevilla expected goals | 0.90 |
| Expected total goals | 1.95 |
| Over 0.5 | 85.7% |
| Under 0.5 | 14.3% |
| Over 1.5 | 58.3% |
| Under 1.5 | 41.7% |
| Over 2.5 | 31.1% |
| Under 2.5 | 68.9% |
| Over 3.5 | 13.4% |
| Under 3.5 | 86.6% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 14.26% |
| 2 | 0-1 | 13.91% |
| 3 | 1-0 | 13.58% |
| 4 | 1-1 | 13.48% |
| 5 | 2-0 | 7.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.4% | 32.5% | 3.00 | +6.1% |
| Draw | 31.2% | 30.6% | 3.00 | -6.4% |
| Sevilla win | 33.4% | 36.9% | 2.61 | -12.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:00:00+00:00 |
| Fixture id | ddcc9a51a2d7368e055d1abefacdb74e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Getafe |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0536 |
| Dc lambda away | 0.8964 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 38.7% |
| P btts no | 61.3% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.01 |
| Fair Over 1.5 odds | 1.72 |
| Fair Under 1.5 odds | 2.40 |
| Fair Over 2.5 odds | 3.22 |
| Fair Under 2.5 odds | 1.45 |
| Fair Over 3.5 odds | 7.48 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.66 |
| Fair Under 4.5 odds | 1.05 |
| Goal margin distribution | {"-1": 0.21773585846776844, "-10": 1.5965670032392005e-08, "-11": 1.2917506206080953e-09, "-12": 9.569544921594171e-11, "-13": 6.15144701969644e-12, "-2": 0.08642046672996216, "-3": 0.02401433974559717, "-4": 0.005145703612997811, "-5": 0.0008949273188126784, "-6": 0.00013080454179715295, "-7": 1.647560522950787e-05, "-8": 1.822372723981847e-06, "-9": 1.7963327931249974e-07, "0": 0.31196281357081496, "1": 0.21238875757444, "10": 6.657006280377015e-08, "11": 6.331096846645316e-09, "12": 5.513152735777927e-10, "13": 4.1657623211551544e-11, "2": 0.0988645829937027, "3": 0.032292617071229365, "4": 0.008133656373030677, "5": 0.0016627895226075738, "6": 0.00028568063216029147, "7": 4.22968292888981e-05, "8": 5.49935939163825e-06, "9": 6.371917657177401e-07} |
| Raw goal margin distribution | {"-1": 0.19504269898276655, "-10": 1.4301674497253176e-08, "-11": 1.1571200500874887e-09, "-12": 8.57217494021936e-11, "-13": 5.510322635022909e-12, "-2": 0.0774134366152526, "-3": 0.021511484930552882, "-4": 0.004609401170331502, "-5": 0.0008016550001591683, "-6": 0.00011717165491644287, "-7": 1.4758462542418043e-05, "-8": 1.632438942943391e-06, "-9": 1.6091129807827008e-07, "0": 0.31784011440115123, "1": 0.229786258903576, "10": 7.202304802453137e-08, "11": 6.849698994246259e-09, "12": 5.964754238342435e-10, "13": 4.506994391754561e-11, "2": 0.10696292460876952, "3": 0.034937817574467324, "4": 0.00879991243656521, "5": 0.0017989943917353552, "6": 0.00030908172567615285, "7": 4.576150958636598e-05, "8": 5.949831033442973e-06, "9": 6.893863579249267e-07} |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 31.8% |
| Unadjusted away-win probability | 30.0% |
| Raw p over 1 5 | 58.3% |
| Raw p under 3 5 | 86.6% |
| Raw p btts yes | 38.9% |
| P home draw | 66.6% |
| P draw away | 64.6% |
| P home away | 68.8% |
| Raw p home draw | 70.0% |
| Raw p draw away | 61.7% |
| Raw p home away | 68.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.75 |
| Reference draw odds | 2.90 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.68 |
| Reference Under 2.5 odds | 1.46 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Home probability edge | +2.9% |
| Draw probability edge | +0.6% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | 0.0579 |
| Raw ev home | 0.1479 |
| Raw edge prob draw | 0.0118 |
| Raw ev draw | -0.0465 |
| Raw edge prob away | -0.0697 |
| Raw ev away | -0.2183 |
| Market p over 1 5 | 62.5% |
| Market over 1 5 odds | 1.63 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:29:35Z |
| Market reference over 1 5 odds | 1.52 |
| Market reference over 1 5 opposite odds | 2.40 |
| Market reference over 1 5 last update utc | 2026-10-23T14:31:21Z |
| Market over 1 5 bookmakers | 1 |
| Elo home rating | 1,456.2995 |
| Elo away rating | 1,476.0418 |
| Elo rating diff | 40.2576 |
| Elo home expectancy | 0.5577 |

</details>


---

## 2026-11-01 — Real Racing Club de Santander vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **80.1%**. Expected goals are 1.19 for Real Racing Club de Santander and 3.66 for Real Madrid (4.85 combined). The most likely exact score is 1-3 at 7.5%. Goal-market probabilities: at least one goal: 99.1%; Over 2.5 goals: 85.8%; Under 3.5 goals: 29.1%; Double Chance 1X: 19.9%; Double Chance X2: 91.5%; Double Chance 12 (either team wins): 88.5%; Under 4.5 goals: 47.3%; BTTS Yes (both teams score): 68.2%; BTTS No (at least one team does not score): 31.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 8.5% | 11.80 |
| Draw | 11.5% | 8.73 |
| Real Madrid win | 80.1% | 1.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.19 |
| Real Madrid expected goals | 3.66 |
| Expected total goals | 4.85 |
| Over 0.5 | 99.1% |
| Under 0.5 | 0.9% |
| Over 1.5 | 95.4% |
| Under 1.5 | 4.6% |
| Over 2.5 | 85.8% |
| Under 2.5 | 14.2% |
| Over 3.5 | 70.9% |
| Under 3.5 | 29.1% |
| Over 4.5 | 52.7% |
| Under 4.5 | 47.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-3 | 7.45% |
| 2 | 1-4 | 6.82% |
| 3 | 0-3 | 6.28% |
| 4 | 1-2 | 6.11% |
| 5 | 0-4 | 5.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 8.5% | 9.2% | 8.07 | -31.6% |
| Draw | 11.5% | 12.5% | 6.84 | -21.6% |
| Real Madrid win | 80.1% | 78.3% | 1.26 | +0.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:15:00+00:00 |
| Fixture id | 6c520ed959578ca3aebe351ee3765d53 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T14:31:19Z |
| Market best draw last update utc | 2026-10-23T14:31:19Z |
| Market best away last update utc | 2026-10-23T14:31:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santander |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1865 |
| Dc lambda away | 3.6594 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:31:28.066301+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 68.2% |
| P btts no | 31.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 105.56 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.61 |
| Fair Over 2.5 odds | 1.17 |
| Fair Under 2.5 odds | 7.03 |
| Fair Over 3.5 odds | 1.41 |
| Fair Under 3.5 odds | 3.44 |
| Fair Over 4.5 odds | 1.90 |
| Fair Under 4.5 odds | 2.11 |
| Goal margin distribution | {"-1": 0.15270755364866867, "-10": 0.00134563272316413, "-11": 0.00043376804618438397, "-12": 0.0001287761568490108, "-13": 3.542153022650828e-05, "-14": 9.074408384255893e-06, "-15": 2.17506798358343e-06, "-16": 4.897587426889239e-07, "-17": 1.0396866392590828e-07, "-18": 2.087486721135024e-08, "-19": 3.975341742584669e-09, "-2": 0.18053939933949137, "-20": 7.192529784226363e-10, "-21": 1.2229209531558243e-10, "-22": 1.6988819386650776e-11, "-3": 0.16893424725347372, "-4": 0.12968046371477585, "-5": 0.08384260784899446, "-6": 0.046643334078559855, "-7": 0.0227184751960895, "-8": 0.009825835915798952, "-9": 0.0038178117550732634, "0": 0.11460629408835134, "1": 0.05496891604153106, "10": 1.9378543447125516e-08, "11": 2.0254076676659814e-09, "12": 1.949623072644484e-10, "13": 1.7387727170630972e-11, "14": 1.4442890570866515e-12, "15": 1.122454998960861e-13, "16": 8.19480459612899e-15, "17": 5.640520348628458e-16, "18": 3.6719835855335903e-17, "19": 2.267314580622943e-18, "2": 0.02128551518092044, "20": 1.3300846552924696e-19, "21": 7.33257143515017e-21, "22": 3.302793476015455e-22, "3": 0.006457883054077041, "4": 0.001607338444059427, "5": 0.0003369441013675762, "6": 6.077751908372182e-05, "7": 9.598267814898302e-06, "8": 1.3459951471124891e-06, "9": 1.695699139300962e-07} |
| Raw goal margin distribution | {"-1": 0.15611712933984012, "-10": 0.0013756773182907133, "-11": 0.00044345299594973614, "-12": 0.00013165140462493308, "-13": 3.621240392933935e-05, "-14": 9.27701710595609e-06, "-15": 2.223631782467494e-06, "-16": 5.006938239191077e-07, "-17": 1.0629002276308087e-07, "-18": 2.13409505065093e-08, "-19": 4.064101127734663e-09, "-2": 0.18457039016200713, "-20": 7.353120888755122e-10, "-21": 1.2502257030157904e-10, "-22": 1.7368137005317448e-11, "-3": 0.17270612421096176, "-4": 0.13257590238913894, "-5": 0.08571460246076096, "-6": 0.04768476244427993, "-7": 0.0232257216218117, "-8": 0.010045222124820574, "-9": 0.0039030538917098996, "0": 0.10422049377932195, "1": 0.05010898915461531, "10": 1.7665242346976566e-08, "11": 1.8463367692400745e-09, "12": 1.777252462626679e-10, "13": 1.585043866534083e-11, "14": 1.316596176701119e-12, "15": 1.0232161996241343e-13, "16": 7.470283283762964e-15, "17": 5.141829115972832e-16, "18": 3.347335165285226e-17, "19": 2.0668561418365518e-18, "2": 0.01940361437262633, "20": 1.2124888458126894e-19, "21": 6.684282117583991e-21, "22": 3.0107859930247035e-22, "3": 0.0058869269256470345, "4": 0.001465229996536907, "5": 0.00030715410702992655, "6": 5.540404039093027e-05, "7": 8.749663127365465e-06, "8": 1.2269926548645463e-06, "9": 1.5457785217471745e-07} |
| Unadjusted home-win probability | 7.7% |
| Unadjusted draw probability | 10.4% |
| Unadjusted away-win probability | 81.9% |
| Raw p over 1 5 | 95.5% |
| Raw p under 3 5 | 28.7% |
| Raw p btts yes | 67.8% |
| P home draw | 19.9% |
| P draw away | 91.5% |
| P home away | 88.5% |
| Raw p home draw | 18.1% |
| Raw p draw away | 92.3% |
| Raw p home away | 89.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.26, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.75, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:31:19Z", "line": 1.75, "market_key": "spreads", "opposite_price": 1.86, "price": 1.98, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 7.50 |
| Reference draw odds | 5.80 |
| Reference away odds | 1.23 |
| Market reference 1x2 last update utc | 2026-10-23T14:31:21Z |
| Market reference home last update utc | 2026-10-23T14:31:21Z |
| Market reference draw last update utc | 2026-10-23T14:31:21Z |
| Market reference away last update utc | 2026-10-23T14:31:21Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.23 |
| Reference Under 2.5 odds | 4.23 |
| Market reference over 2 5 last update utc | 2026-10-23T14:31:21Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:31:21Z |
| Home probability edge | -0.7% |
| Draw probability edge | -1.0% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | +6.2% |
| Under 2.5 probability edge | -6.2% |
| Raw edge prob home | -0.0150 |
| Raw ev home | -0.3767 |
| Raw edge prob draw | -0.0208 |
| Raw ev draw | -0.2871 |
| Raw edge prob away | 0.0358 |
| Raw ev away | 0.0314 |
| Elo home rating | 1,429.4672 |
| Elo away rating | 1,656.5478 |
| Elo rating diff | -167.0806 |
| Elo home expectancy | 0.2765 |

</details>


---
