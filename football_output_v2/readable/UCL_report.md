# UEFA Champions League — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 557 |
| Training data through | 2026-10-21 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 480 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 70.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 4 |
| Training seasons loaded | ['2023', '2024', '2025', '2026'] |
| Training sha256 | f4d768cacebcc149dd9b123db36bf00d03ede4db9280d27315ff432c3b29a900 |
| Training as of utc | 2026-11-03T13:57:37.532944+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 42, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 52, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-03T13:57:37.532944+00:00', 'observations': 374, 'observations_sha256': '4ab292c318d16afacb99c2ad5969866fad1f388eaf1d9178bac3caf4e828ecf9', 'eligible_training_matches': 14, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 94, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 14, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': '496d0fec6c65cf75a381038f7e09e49fa52bf8862cd08e37d45ab19b62b2f869', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 809.711 |
| Base scoring parameter | 0.213 |
| Home-advantage parameter | 0.300 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 71, 'matches': 557, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-21'} |
| Training data health | {'completed_matches': 54, 'latest_completed_utc': '2026-10-21T19:00:00+00:00', 'latest_completed_date': '2026-10-21', 'next_fixture_utc': '2026-11-03T17:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-11-03T13:57:37.532944+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '1d99ce3362b1915aff584e4ae4678057ee29bc6190f9a1d419b1135011f76902', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0, 'training_end': '2026-10-21', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261103T135737532944Z_1310e5e7908f1350cd19fd70a506043451326682bd05fd7b347cb2b6db2f11cb.json |
| Over 1 5 in window quote fixtures | 12 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 18.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 18.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2, 'ANCHORED_ALTERNATE': 16} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 18} |
| Legacy comparison status | {'None': 18} |
| Bbs statistics applied fixtures | 0 |
| Goal market validation | SKIPPED: not required by 48h-ah-price-edge-cagey-v28 |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-03 — Atlético Madrid vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **41.8%**. Expected goals are 1.85 for Atlético Madrid and 2.03 for Bayern Munich (3.89 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.0%; Double Chance 1X: 58.2%; Double Chance X2: 65.5%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 76.5%; BTTS Yes (both teams score): 65.1%; BTTS No (at least one team does not score): 34.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 34.5% | 2.89 |
| Draw | 23.6% | 4.23 |
| Bayern Munich win | 41.8% | 2.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 1.85 |
| Bayern Munich expected goals | 2.03 |
| Expected total goals | 3.89 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 83.7% |
| Under 1.5 | 16.3% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 42.0% |
| Under 3.5 | 58.0% |
| Over 4.5 | 23.5% |
| Under 4.5 | 76.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.24% |
| 2 | 1-2 | 8.57% |
| 3 | 2-1 | 7.60% |
| 4 | 2-2 | 7.33% |
| 5 | 0-1 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 34.5% | 33.7% | 2.89 | -0.2% |
| Draw | 23.6% | 25.1% | 3.96 | -6.5% |
| Bayern Munich win | 41.8% | 41.2% | 2.42 | +1.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | 61b42fd619617a7a2a3770c2444e8a40 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:37Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8536 |
| Dc lambda away | 2.0328 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.1% |
| P btts no | 34.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.22 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.14 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.38 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.25 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.20254884340389448, "-10": 3.0317330677448883e-06, "-11": 4.665647120557058e-07, "-12": 6.601686200192997e-08, "-13": 8.642897743494848e-09, "-14": 1.0520406182153414e-09, "-15": 1.1842639875693243e-10, "-16": 1.092612971121352e-11, "-2": 0.12388517744802037, "-3": 0.05936414008915646, "-4": 0.022778182118187718, "-5": 0.007249183589056448, "-6": 0.001965136921979083, "-7": 0.0004631621414253386, "-8": 9.645299012869636e-05, "-9": 1.7979080890682836e-05, "0": 0.23618764303001927, "1": 0.18020166279835959, "10": 1.1726953495947143e-06, "11": 1.6456121001552747e-07, "12": 2.1232043827755485e-08, "13": 2.5346479184260812e-09, "14": 2.8132745376020607e-10, "15": 2.8876827067162014e-11, "16": 2.429341909674452e-12, "2": 0.1002634994437894, "3": 0.043809574377166184, "4": 0.015327991642480289, "5": 0.004448121423481049, "6": 0.0010995163510829425, "7": 0.00023629975498920403, "8": 4.487115568269287e-05, "9": 7.626765392487528e-06} |
| Raw goal margin distribution | {"-1": 0.1923273704610196, "-10": 9.552454790464014e-06, "-11": 1.7174364150389387e-06, "-12": 2.842114020690325e-07, "-13": 4.355647664555304e-08, "-14": 6.2141695012900995e-09, "-15": 8.281362621905462e-10, "-16": 1.0188469416320556e-10, "-17": 9.972742534826692e-12, "-2": 0.12812847671950267, "-3": 0.0684361636603847, "-4": 0.029755753076665416, "-5": 0.010841847210955135, "-6": 0.0033876585629517312, "-7": 0.000924562990092813, "-8": 0.00022368542964408433, "-9": 4.85566908899239e-05, "0": 0.2018106305242638, "1": 0.17571365377549797, "10": 3.796019237256605e-06, "11": 6.223223839350434e-07, "12": 9.390691933527247e-08, "13": 1.3122910881862744e-08, "14": 1.7071900635228163e-09, "15": 2.0745405222509542e-10, "16": 2.3272894889498853e-11, "17": 2.0771956782731585e-12, "2": 0.10653402749150986, "3": 0.05188593895140504, "4": 0.02057104298155493, "5": 0.0068345510146666675, "6": 0.00194727675753445, "7": 0.0004846027724024407, "8": 0.0001069075623325202, "9": 2.116124203317905e-05} |
| Unadjusted home-win probability | 36.4% |
| Unadjusted draw probability | 20.2% |
| Unadjusted away-win probability | 43.4% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 45.6% |
| Raw p btts yes | 72.9% |
| P home draw | 58.2% |
| P draw away | 65.5% |
| P home away | 76.4% |
| Raw p home draw | 56.6% |
| Raw p draw away | 63.6% |
| Raw p home away | 79.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8496 |
| Totals anchor target over 2 5 | 0.6363 |
| Totals anchor reference over odds | 1.53 |
| Totals anchor reference under odds | 2.59 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7366 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.47, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.17, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.46, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 4.01, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.47, "under": 2.67}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.47, "home_away": 1.29, "home_draw": 1.65}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.38, "draw": 3.86, "home": 2.89}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.53, "under": 2.59}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.42, "draw": 3.96, "home": 2.86}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.48, "home_away": 1.29, "home_draw": 1.63}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.89 |
| Reference draw odds | 3.86 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.57 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | +0.8% |
| Draw probability edge | -1.5% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0267 |
| Raw ev home | 0.0523 |
| Raw edge prob draw | -0.0491 |
| Raw ev draw | -0.2008 |
| Raw edge prob away | 0.0224 |
| Raw ev away | 0.0505 |
| Market p home draw | 59.4% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:14Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.5% |
| Market draw away odds | 1.48 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:57:38Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.1% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.63 |
| Market reference dc draw away odds | 1.48 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:57:03Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.6% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:57:03Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.31 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,542.1549 |
| Elo away rating | 1,571.2653 |
| Elo rating diff | 30.8896 |
| Elo home expectancy | 0.5443 |

</details>


---

## 2026-11-03 — Barcelona vs Aston Villa

The model's most likely 1X2 outcome is **Barcelona win** at **65.9%**. Expected goals are 1.89 for Barcelona and 1.89 for Aston Villa (3.78 combined). The most likely exact score is 2-1 at 12.8%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 74.2%; Under 3.5 goals: 47.8%; Double Chance 1X: 80.9%; Double Chance X2: 34.1%; Double Chance 12 (either team wins): 85.0%; Under 4.5 goals: 66.1%; BTTS Yes (both teams score): 70.3%; BTTS No (at least one team does not score): 29.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 65.9% | 1.52 |
| Draw | 15.0% | 6.67 |
| Aston Villa win | 19.1% | 5.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.89 |
| Aston Villa expected goals | 1.89 |
| Expected total goals | 3.78 |
| Over 0.5 | 98.6% |
| Under 0.5 | 1.4% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 74.2% |
| Under 2.5 | 25.8% |
| Over 3.5 | 52.2% |
| Under 3.5 | 47.8% |
| Over 4.5 | 33.9% |
| Under 4.5 | 66.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 12.75% |
| 2 | 3-1 | 8.05% |
| 3 | 1-0 | 7.81% |
| 4 | 3-2 | 7.60% |
| 5 | 2-0 | 6.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 65.9% | 77.1% | 1.32 | -13.0% |
| Draw | 15.0% | 12.6% | 7.11 | +6.7% |
| Aston Villa win | 19.1% | 10.3% | 8.63 | +64.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | bd680c6ad693dae859030f86e1be2769 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:37Z |
| Market best away last update utc | 2026-11-03T13:57:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FC Barcelona |
| Matched away-team name | Aston Villa FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8946 |
| Dc lambda away | 1.8865 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 70.3% |
| P btts no | 29.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 73.11 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.74 |
| Fair Over 2.5 odds | 1.35 |
| Fair Under 2.5 odds | 3.87 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.09 |
| Fair Over 4.5 odds | 2.95 |
| Fair Under 4.5 odds | 1.51 |
| Goal margin distribution | {"-1": 0.08972886257111108, "-10": 2.3828097468331796e-06, "-11": 3.9810691927619685e-07, "-12": 6.12092564087796e-08, "-13": 8.713255740455821e-09, "-14": 1.1530591512737157e-09, "-15": 1.4025706461883388e-10, "-16": 1.351749613256497e-11, "-2": 0.056159918212458, "-3": 0.028104706235340574, "-4": 0.011417154750432054, "-5": 0.003879763295745904, "-6": 0.0011292731575241566, "-7": 0.00028686382263720135, "-8": 6.455968076802712e-05, "-9": 1.303074072499355e-05, "0": 0.15001118951498307, "1": 0.3088261163764155, "10": 8.52480573275191e-06, "11": 1.4304031772350604e-06, "12": 2.2087138835122576e-07, "13": 3.1576677809767844e-08, "14": 4.196634812692266e-09, "15": 5.126700593557363e-10, "16": 4.9621864734383765e-11, "2": 0.19413893886458497, "3": 0.0975728189618868, "4": 0.03980808692449946, "5": 0.013585707711275373, "6": 0.003971363675148563, "7": 0.0010131647059494666, "8": 0.00022899672044667847, "9": 4.641951615321275e-05} |
| Raw goal margin distribution | {"-1": 0.18611381685684658, "-10": 4.942376445208603e-06, "-11": 8.257454306287887e-07, "-12": 1.2695901865666891e-07, "-13": 1.807286124708069e-08, "-14": 2.3916522906461043e-09, "-15": 2.909184056207223e-10, "-16": 2.803772083464823e-11, "-2": 0.11648578209275147, "-3": 0.05829422104792964, "-4": 0.023681234636895004, "-5": 0.008047327635521006, "-6": 0.0023423158568876236, "-7": 0.000595007218628715, "-8": 0.00013390840202922119, "-9": 2.7028102477934615e-05, "0": 0.20533498441190817, "1": 0.18689665256209909, "10": 5.159076809590702e-06, "11": 8.656572467905433e-07, "12": 1.3366785041998473e-07, "13": 1.9109703061784898e-08, "14": 2.539736625000199e-09, "15": 3.1025976393011137e-10, "16": 3.0030363110358535e-11, "2": 0.117489797273246, "3": 0.05904951776422044, "4": 0.024091220905753025, "5": 0.008221854173853712, "6": 0.0024034061163638854, "7": 0.0006131511617534936, "8": 0.00013858517213944882, "9": 2.8092352694722726e-05} |
| Unadjusted home-win probability | 39.9% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 39.6% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 47.7% |
| Raw p btts yes | 71.7% |
| P home draw | 80.9% |
| P draw away | 34.1% |
| P home away | 85.0% |
| Raw p home draw | 60.4% |
| Raw p draw away | 60.1% |
| Raw p home away | 79.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7418 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.95, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:34Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 7.33, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:34Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.12, "price": 7.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.57, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:44Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.17, "under": 4.68}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:34Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 4.01, "home_away": 1.12, "home_draw": 1.1}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 8.63, "draw": 7.11, "home": 1.28}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 8.6, "draw": 7.01, "home": 1.32}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.72, "home_away": 1.13, "home_draw": 1.09}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.28 |
| Reference draw odds | 7.11 |
| Reference away odds | 8.63 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 5.14 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | -11.2% |
| Draw probability edge | +2.4% |
| Away probability edge | +8.8% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.3718 |
| Raw ev home | -0.4734 |
| Raw edge prob draw | 0.0790 |
| Raw ev draw | 0.4599 |
| Raw edge prob away | 0.2928 |
| Raw ev away | 2.4151 |
| Market p home draw | 88.6% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:34Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 26.0% |
| Market draw away odds | 4.01 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:34Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 85.5% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.09 |
| Market reference dc draw away odds | 3.72 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 94.5% |
| Market over 1 5 odds | 1.02 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:56:44Z |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 12.00 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 35.2% |
| Market under 3 5 odds | 2.66 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:57:37Z |
| Market reference under 3 5 odds | 2.69 |
| Market reference under 3 5 opposite odds | 1.51 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,563.5732 |
| Elo away rating | 1,514.0790 |
| Elo rating diff | 109.4942 |
| Elo home expectancy | 0.6526 |

</details>


---

## 2026-11-03 — Bodø/Glimt vs Lille

The model's most likely 1X2 outcome is **Bodø/Glimt win** at **58.4%**. Expected goals are 2.82 for Bodø/Glimt and 1.81 for Lille (4.63 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 65.5%; Under 3.5 goals: 56.3%; Double Chance 1X: 78.9%; Double Chance X2: 41.6%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 58.4% | 1.71 |
| Draw | 20.5% | 4.88 |
| Lille win | 21.1% | 4.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 2.82 |
| Lille expected goals | 1.81 |
| Expected total goals | 4.63 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.15% |
| 2 | 1-1 | 8.91% |
| 3 | 1-0 | 8.02% |
| 4 | 2-0 | 7.72% |
| 5 | 3-1 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 58.4% | 58.0% | 1.73 | +1.0% |
| Draw | 20.5% | 22.1% | 4.42 | -9.4% |
| Lille win | 21.1% | 20.0% | 4.79 | +1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | 1a5a84045050d0d7baf1301909d3b465 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8232 |
| Dc lambda away | 1.8089 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.26 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.53 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.98 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.12463086658441123, "-10": 1.598006319424576e-07, "-11": 1.8722420111039794e-08, "-12": 2.0167763651701366e-09, "-13": 2.010110477246015e-10, "-14": 1.863865744232961e-11, "-15": 1.6146899205363278e-12, "-16": 1.300591937371884e-13, "-17": 8.680533431627834e-15, "-2": 0.05769318580849766, "-3": 0.021069934237277096, "-4": 0.006159158989633572, "-5": 0.0014929700221490226, "-6": 0.0003082106792073918, "-7": 5.5314082135374564e-05, "-8": 8.770703628205376e-06, "-9": 1.2447417288739215e-06, "0": 0.20488509394952345, "1": 0.23911144944961574, "10": 1.7040967043215873e-05, "11": 3.1160434281105318e-06, "12": 5.238718112723574e-07, "13": 8.149162649783282e-08, "14": 1.1793248691736175e-08, "15": 1.594533824015523e-09, "16": 2.0045247866845097e-10, "17": 2.088058005378125e-11, "2": 0.17475680374064156, "3": 0.099608986974557, "4": 0.04544462558924636, "5": 0.01719245806893763, "6": 0.005539369563594552, "7": 0.0015515798814417661, "8": 0.0003839711875373321, "9": 8.504900198014788e-05} |
| Raw goal margin distribution | {"-1": 0.12457268902506224, "-10": 1.5871233366040037e-06, "-11": 2.51564841824257e-07, "-12": 3.67505713422499e-08, "-13": 4.977322232369345e-09, "-14": 6.281466418435762e-10, "-15": 7.419973717353859e-11, "-16": 8.235190239081497e-12, "-17": 8.60017789904057e-13, "-18": 8.29581932278977e-14, "-19": 6.2249345031557465e-15, "-2": 0.06769298755052904, "-3": 0.030270136868993377, "-4": 0.011207204127410407, "-5": 0.0035162879618183805, "-6": 0.0009533173008960973, "-7": 0.00022695957228337186, "-8": 4.808388099427488e-05, "-9": 9.166529807709104e-06, "0": 0.1681708458646942, "1": 0.19302972208008914, "10": 0.000136103217769014, "11": 3.36692491979791e-05, "12": 7.67667852075186e-06, "13": 1.622672171345868e-06, "14": 3.196110928207714e-07, "15": 5.8923554899194046e-08, "16": 1.0206714830387468e-08, "17": 1.6635871279821333e-09, "18": 2.5045123225199337e-10, "19": 2.933083628322571e-11, "2": 0.16489034424933008, "3": 0.11507783938844923, "4": 0.06649674212533152, "5": 0.03256216642212771, "6": 0.013778187928167115, "7": 0.005119516006826435, "8": 0.0016928001391264174, "9": 0.0005036593480694821} |
| Unadjusted home-win probability | 59.3% |
| Unadjusted draw probability | 16.8% |
| Unadjusted away-win probability | 23.8% |
| Raw p over 1 5 | 94.3% |
| Raw p under 3 5 | 32.0% |
| Raw p btts yes | 78.4% |
| P home draw | 78.9% |
| P draw away | 41.6% |
| P home away | 79.5% |
| Raw p home draw | 76.2% |
| Raw p draw away | 40.7% |
| Raw p home away | 83.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7268 |
| Totals anchor target over 2 5 | 0.6552 |
| Totals anchor reference over odds | 1.49 |
| Totals anchor reference under odds | 2.73 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8341 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.3, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.09, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.43, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.78, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.52, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:43:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.46, "under": 2.69}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.28, "home_away": 1.25, "home_draw": 1.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.79, "draw": 4.35, "home": 1.7}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.49, "under": 2.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.78, "draw": 4.42, "home": 1.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.24, "home_away": 1.25, "home_draw": 1.23}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.70 |
| Reference draw odds | 4.35 |
| Reference away odds | 4.79 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | +0.4% |
| Draw probability edge | -1.6% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0138 |
| Raw ev home | 0.0265 |
| Raw edge prob draw | -0.0524 |
| Raw ev draw | -0.2567 |
| Raw edge prob away | 0.0387 |
| Raw ev away | 0.1424 |
| Market p home draw | 79.0% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:57:38Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.4% |
| Market draw away odds | 2.28 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:14Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.7% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.23 |
| Market reference dc draw away odds | 2.24 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 85.9% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:43:23Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 6.10 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.8% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:43:23Z |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.17 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,472.3301 |
| Elo away rating | 1,454.8649 |
| Elo rating diff | 77.4652 |
| Elo home expectancy | 0.6097 |

</details>


---

## 2026-11-03 — Feyenoord vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **48.5%**. Expected goals are 1.38 for Feyenoord and 1.58 for Inter Milan (2.96 combined). The most likely exact score is 1-1 at 9.8%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 67.4%; Under 3.5 goals: 53.4%; Double Chance 1X: 51.5%; Double Chance X2: 72.2%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 72.8%; BTTS Yes (both teams score): 68.2%; BTTS No (at least one team does not score): 31.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 27.8% | 3.60 |
| Draw | 23.7% | 4.22 |
| Inter Milan win | 48.5% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.38 |
| Inter Milan expected goals | 1.58 |
| Expected total goals | 2.96 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 46.6% |
| Under 3.5 | 53.4% |
| Over 4.5 | 27.2% |
| Under 4.5 | 72.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.75% |
| 2 | 1-2 | 9.42% |
| 3 | 2-2 | 7.83% |
| 4 | 0-1 | 6.67% |
| 5 | 2-1 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 27.8% | 25.2% | 3.83 | +6.5% |
| Draw | 23.7% | 23.9% | 4.26 | +0.8% |
| Inter Milan win | 48.5% | 50.9% | 1.97 | -4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | f6f3cf01c2b20b7f746b5a06097a0569 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:37Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | FC Internazionale Milano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3782 |
| Dc lambda away | 1.5824 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 68.2% |
| P btts no | 31.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.08 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.22 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.68 |
| Fair Under 4.5 odds | 1.37 |
| Goal margin distribution | {"-1": 0.22304395353848672, "-10": 6.316218844889089e-06, "-11": 1.0510645227656026e-06, "-12": 1.6086992883090326e-07, "-13": 2.2787433385657125e-08, "-14": 3.001081235566799e-09, "-15": 3.6469707409655617e-10, "-16": 3.5834000939045187e-11, "-2": 0.14412581489036996, "-3": 0.07352185168434129, "-4": 0.030200054185742682, "-5": 0.010324394749989734, "-6": 0.0030131477606818798, "-7": 0.0007657156610295269, "-8": 0.00017211506014465583, "-9": 3.465580738695152e-05, "0": 0.23669290831896003, "1": 0.14376327517275375, "10": 1.1700312378117677e-06, "11": 1.6957509409419785e-07, "12": 2.260476314085571e-08, "13": 2.788771328569919e-09, "14": 3.198804112963699e-10, "15": 3.3855916512236727e-11, "16": 2.8972768639510244e-12, "2": 0.0806385760741225, "3": 0.035826956186375866, "4": 0.012817212953002586, "5": 0.0038163032816028834, "6": 0.0009700432780239234, "7": 0.00021469929210667587, "8": 4.2031448533313075e-05, "9": 7.370957502772453e-06} |
| Raw goal margin distribution | {"-1": 0.21603229600359466, "-10": 1.710336508879566e-06, "-11": 2.4209743124924847e-07, "-12": 3.148937066652588e-08, "-13": 3.786451443842723e-09, "-14": 4.20021864107853e-10, "-15": 3.86854830390405e-11, "-2": 0.1268719318533313, "-3": 0.05744727272472718, "-4": 0.0206232009251883, "-5": 0.006104300917929749, "-6": 0.0015332168527971103, "-7": 0.0003339668282292921, "-8": 6.416119003303707e-05, "-9": 1.1019204923387815e-05, "0": 0.23215625136829118, "1": 0.18888173383959572, "10": 4.295419484427425e-07, "11": 5.295495454707068e-08, "12": 5.998916278542277e-09, "13": 6.282516146525062e-10, "14": 6.069676170234545e-11, "15": 4.868935806895921e-12, "2": 0.09623883478679751, "3": 0.03795304458146437, "4": 0.01186658295559091, "5": 0.0030591300683019506, "6": 0.0006692031771786137, "7": 0.0001269550975593478, "8": 2.124279331880149e-05, "9": 3.1774730413618017e-06} |
| Unadjusted home-win probability | 33.9% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 42.9% |
| Raw p over 1 5 | 78.9% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 58.9% |
| P home draw | 51.5% |
| P draw away | 72.2% |
| P home away | 76.3% |
| Raw p home draw | 57.1% |
| Raw p draw away | 66.1% |
| Raw p home away | 76.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1830 |
| Totals anchor target over 2 5 | 0.6738 |
| Totals anchor reference over odds | 1.45 |
| Totals anchor reference under odds | 2.87 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5676 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.76, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.53, "price": 2.76, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.3, "home_away": 1.28, "home_draw": 1.96}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.93, "draw": 4.04, "home": 3.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.45, "under": 2.87}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.97, "draw": 4.26, "home": 3.65}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.33, "home_away": 1.26, "home_draw": 1.93}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.83 |
| Reference draw odds | 4.04 |
| Reference away odds | 1.93 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | +2.6% |
| Draw probability edge | -0.2% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0867 |
| Raw ev home | 0.2977 |
| Raw edge prob draw | -0.0065 |
| Raw ev draw | -0.0110 |
| Raw edge prob away | -0.0803 |
| Raw ev away | -0.1548 |
| Market p home draw | 50.2% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:14Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.9% |
| Market draw away odds | 1.33 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:57:38Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.9% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-03T13:57:14Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.93 |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 86.7% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.9% |
| Market under 3 5 odds | 1.80 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:57:37Z |
| Market reference under 3 5 odds | 1.80 |
| Market reference under 3 5 opposite odds | 2.09 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,466.8088 |
| Elo away rating | 1,507.3319 |
| Elo rating diff | 19.4769 |
| Elo home expectancy | 0.5280 |

</details>


---

## 2026-11-03 — Galatasaray vs VfB Stuttgart

The model's most likely 1X2 outcome is **Galatasaray win** at **46.0%**. Expected goals are 1.65 for Galatasaray and 1.43 for VfB Stuttgart (3.08 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 59.5%; Under 3.5 goals: 62.9%; Double Chance 1X: 68.8%; Double Chance X2: 54.0%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 46.0% | 2.17 |
| Draw | 22.8% | 4.39 |
| VfB Stuttgart win | 31.2% | 3.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.65 |
| VfB Stuttgart expected goals | 1.43 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 80.8% |
| Under 1.5 | 19.2% |
| Over 2.5 | 59.5% |
| Under 2.5 | 40.5% |
| Over 3.5 | 37.1% |
| Under 3.5 | 62.9% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.35% |
| 2 | 2-1 | 9.51% |
| 3 | 1-0 | 8.64% |
| 4 | 1-2 | 7.12% |
| 5 | 2-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 46.0% | 47.2% | 2.13 | -1.9% |
| Draw | 22.8% | 22.8% | 4.32 | -1.5% |
| VfB Stuttgart win | 31.2% | 29.9% | 3.25 | +1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T17:45:00+00:00 |
| Fixture id | 9b8076d3ffa027df6f6cb3189de46706 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6456 |
| Dc lambda away | 1.4339 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.56 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.20 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.04 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.17067436605507533, "-10": 5.269556297867866e-07, "-11": 6.750170188468156e-08, "-12": 7.94696495095167e-09, "-13": 8.649761432599274e-10, "-14": 8.67555281636057e-11, "-15": 7.165956668795666e-12, "-2": 0.08905460862626186, "-3": 0.03615834872587908, "-4": 0.011679533519575501, "-5": 0.0031168429288362643, "-6": 0.0007067225427761335, "-7": 0.00013908715546335097, "-8": 2.4157610126022542e-05, "-9": 3.752471205459684e-06, "0": 0.22802815381709454, "1": 0.22710148591939738, "10": 2.4303789952929715e-06, "11": 3.5728677088655696e-07, "12": 4.8273164566978726e-08, "13": 6.029910428596501e-09, "14": 6.940745954815315e-10, "15": 6.579386923413605e-11, "2": 0.13650176957650761, "3": 0.06360521575606257, "4": 0.023578267883720635, "5": 0.00722110360507123, "6": 0.0018790566038039067, "7": 0.0004244047173809758, "8": 8.459591737423174e-05, "9": 1.5080476483931722e-05} |
| Raw goal margin distribution | {"-1": 0.1865269070543215, "-10": 5.75900213083396e-07, "-11": 7.377138093127315e-08, "-12": 8.685093298028004e-09, "-13": 9.4531667764324e-10, "-14": 9.481353710140377e-11, "-15": 7.831543566913967e-12, "-2": 0.09732616027780912, "-3": 0.0395168009579915, "-4": 0.01276434952475928, "-5": 0.0034063408860259413, "-6": 0.0007723641991267711, "-7": 0.00015200581973271054, "-8": 2.6401412249435726e-05, "-9": 4.101007456145653e-06, "0": 0.22714523111839005, "1": 0.21326314145272907, "10": 2.2822847563439745e-06, "11": 3.355156345644169e-07, "12": 4.5331657262129504e-08, "13": 5.662480082307662e-09, "14": 6.517814184952485e-10, "15": 6.178474431550803e-11, "2": 0.12818408508376974, "3": 0.05972945562201592, "4": 0.02214153491131678, "5": 0.006781088346201709, "6": 0.0017645569894551242, "7": 0.0003985437739854692, "8": 7.944109665450328e-05, "9": 1.4161553265700529e-05} |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 34.0% |
| Raw p over 1 5 | 80.7% |
| Raw p under 3 5 | 62.9% |
| Raw p btts yes | 60.9% |
| P home draw | 68.8% |
| P draw away | 54.0% |
| P home away | 77.2% |
| Raw p home draw | 66.0% |
| Raw p draw away | 56.8% |
| Raw p home away | 77.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5946 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.3, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.23, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.58, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.57, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.92, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.95, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:44:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.31, "under": 3.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.83, "home_away": 1.26, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.25, "draw": 4.23, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.17, "draw": 4.32, "home": 2.13}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.79, "home_away": 1.26, "home_draw": 1.41}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 4.23 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.57 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | -1.2% |
| Draw probability edge | -0.0% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -15.6% |
| Under 2.5 probability edge | +15.6% |
| Raw edge prob home | -0.0401 |
| Raw ev home | -0.0791 |
| Raw edge prob draw | -0.0013 |
| Raw ev draw | -0.0187 |
| Raw edge prob away | 0.0413 |
| Raw ev away | 0.1066 |
| Market p home draw | 68.8% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:57:38Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.2% |
| Market draw away odds | 1.83 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:14Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.41 |
| Market reference dc draw away odds | 1.79 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 90.0% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:44:37Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 8.10 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 46.5% |
| Market under 3 5 odds | 2.10 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:44:37Z |
| Market reference under 3 5 odds | 2.07 |
| Market reference under 3 5 opposite odds | 1.81 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,464.0831 |
| Elo away rating | 1,479.0805 |
| Elo rating diff | 45.0026 |
| Elo home expectancy | 0.5644 |

</details>


---

## 2026-11-03 — LASK vs ŠK Slovan Bratislava

The model's most likely 1X2 outcome is **LASK win** at **78.8%**. Expected goals are 5.26 for LASK and 1.09 for ŠK Slovan Bratislava (6.35 combined). The most likely exact score is 3-0 at 10.2%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 72.9%; Under 3.5 goals: 46.7%; Double Chance 1X: 90.9%; Double Chance X2: 21.2%; Double Chance 12 (either team wins): 87.9%; Under 4.5 goals: 66.0%; BTTS Yes (both teams score): 49.0%; BTTS No (at least one team does not score): 51.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 78.8% | 1.27 |
| Draw | 12.1% | 8.25 |
| ŠK Slovan Bratislava win | 9.1% | 11.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 5.26 |
| ŠK Slovan Bratislava expected goals | 1.09 |
| Expected total goals | 6.35 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 88.7% |
| Under 1.5 | 11.3% |
| Over 2.5 | 72.9% |
| Under 2.5 | 27.1% |
| Over 3.5 | 53.3% |
| Under 3.5 | 46.7% |
| Over 4.5 | 34.0% |
| Under 4.5 | 66.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.24% |
| 2 | 2-0 | 9.41% |
| 3 | 4-0 | 8.36% |
| 4 | 3-1 | 6.96% |
| 5 | 2-1 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 78.8% | 72.4% | 1.43 | +12.7% |
| Draw | 12.1% | 15.7% | 5.84 | -29.2% |
| ŠK Slovan Bratislava win | 9.1% | 12.0% | 7.55 | -31.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | adf608a0e9be02eb1d8b0a6f464a12b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:37Z |
| Market best away last update utc | 2026-11-03T13:57:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | LASK Linz |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.2582 |
| Dc lambda away | 1.0938 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 26 |
| Score grid omitted mass | 0 |
| P btts yes | 49.0% |
| P btts no | 51.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.47 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.89 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.69 |
| Fair Over 3.5 odds | 1.88 |
| Fair Under 3.5 odds | 2.14 |
| Fair Over 4.5 odds | 2.94 |
| Fair Under 4.5 odds | 1.52 |
| Goal margin distribution | {"-1": 0.06988258447247564, "-10": 2.617502338844276e-10, "-11": 1.590048670571697e-11, "-12": 8.876137085703515e-13, "-13": 4.582767385924506e-14, "-14": 2.2005531432781715e-15, "-15": 9.87486611479982e-17, "-16": 4.15875374822388e-18, "-17": 1.6498772851794622e-19, "-18": 6.186423107524037e-21, "-19": 2.198616695572652e-22, "-2": 0.01696303037492596, "-20": 7.39298877996067e-24, "-21": 2.162936832629549e-25, "-3": 0.003289871749868743, "-4": 0.0005062350720212821, "-5": 6.425468292909031e-05, "-6": 6.922495028200532e-06, "-7": 6.468908105956748e-07, "-8": 5.332406513996425e-08, "-9": 3.929739339923752e-09, "0": 0.12117396498061708, "1": 0.152040209901765, "10": 0.0008193721536093329, "11": 0.00023928637866578513, "12": 6.421625836503025e-05, "13": 1.5939043180917952e-05, "14": 3.6794231110213147e-06, "15": 7.937660574987961e-07, "16": 1.607081679923049e-07, "17": 3.06506596477458e-08, "18": 5.5251139425203274e-09, "19": 9.439838800416667e-10, "2": 0.18611872306662172, "20": 1.5259789431109964e-10, "21": 2.146276978519702e-11, "3": 0.17353178324815668, "4": 0.1283706465828498, "5": 0.07833064828505819, "6": 0.04056981485136319, "7": 0.018225724123127857, "8": 0.007222549015712842, "9": 0.0025588476493016215} |
| Raw goal margin distribution | {"-1": 0.016550236820250183, "-10": 1.964388860177009e-09, "-11": 1.8744132457863496e-10, "-12": 1.6494835001512738e-11, "-13": 1.3463737932764817e-12, "-14": 1.0244596512024817e-13, "-15": 7.298800862114175e-15, "-16": 4.888024166588226e-16, "-17": 3.08783377785352e-17, "-18": 1.845738499729653e-18, "-19": 1.0468993271769093e-19, "-2": 0.00518662816350559, "-20": 5.648918390598992e-21, "-21": 2.906417714827805e-22, "-22": 1.4288961965910418e-23, "-23": 6.7251580697129965e-25, "-24": 3.031729909774502e-26, "-25": 1.2901761818410168e-27, "-26": 4.4444029582743984e-29, "-3": 0.0013655893374807135, "-4": 0.0002997601724880811, "-5": 5.6026309748839095e-05, "-6": 9.078521940200729e-06, "-7": 1.2948710234520334e-06, "-8": 1.64639391337503e-07, "-9": 1.886092273345083e-08, "0": 0.03860483010498497, "1": 0.07765551813139931, "10": 0.012952745560144351, "11": 0.005941733291757911, "12": 0.0025136755555628105, "13": 0.0009863710858791013, "14": 0.00036081366637027664, "15": 0.00012358138906604253, "16": 3.978765461762692e-05, "17": 1.2083210622936533e-05, "18": 3.4722584256397242e-06, "19": 9.46804312014768e-07, "2": 0.11987040931899463, "20": 2.4560321313694997e-07, "21": 6.074915098964099e-08, "22": 1.4358077667850095e-08, "23": 3.248714536876365e-09, "24": 7.040653975305996e-10, "25": 1.4404060924059092e-10, "26": 2.3854086773520243e-11, "3": 0.15172614678974902, "4": 0.16011339958543322, "5": 0.14386634289459976, "6": 0.11207165118596209, "7": 0.07684587723245012, "8": 0.04697223763357329, "9": 0.02586925194844574} |
| Unadjusted home-win probability | 93.8% |
| Unadjusted draw probability | 3.9% |
| Unadjusted away-win probability | 2.3% |
| Raw p over 1 5 | 98.7% |
| Raw p under 3 5 | 12.2% |
| Raw p btts yes | 66.1% |
| P home draw | 90.9% |
| P draw away | 21.2% |
| P home away | 87.9% |
| Raw p home draw | 97.7% |
| Raw p draw away | 6.2% |
| Raw p home away | 96.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.6211 |
| Totals anchor target over 2 5 | 0.7290 |
| Totals anchor reference over odds | 1.34 |
| Totals anchor reference under odds | 3.35 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.9245 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.34, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.15, "price": 6.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.38, "home_away": 1.17, "home_draw": 1.12}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.55, "draw": 5.84, "home": 1.36}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.34, "under": 3.35}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.4, "draw": 5.55, "home": 1.43}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.07, "home_away": 1.18, "home_draw": 1.11}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.36 |
| Reference draw odds | 5.84 |
| Reference away odds | 7.55 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | +6.4% |
| Draw probability edge | -3.5% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.2140 |
| Raw ev home | 0.3412 |
| Raw edge prob draw | -0.1180 |
| Raw ev draw | -0.7745 |
| Raw edge prob away | -0.0961 |
| Raw ev away | -0.8228 |
| Market p home draw | 86.9% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:14Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 31.4% |
| Market draw away odds | 3.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:14Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.7% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 3.07 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 89.9% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.70 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 48.4% |
| Market under 3 5 odds | 2.01 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:57:37Z |
| Market reference under 3 5 odds | 1.99 |
| Market reference under 3 5 opposite odds | 1.87 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,423.1110 |
| Elo away rating | 1,382.3668 |
| Elo rating diff | 100.7442 |
| Elo home expectancy | 0.6411 |

</details>


---

## 2026-11-03 — Manchester United vs AS Roma

The model's most likely 1X2 outcome is **Manchester United win** at **49.7%**. Expected goals are 2.49 for Manchester United and 1.45 for AS Roma (3.94 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 63.1%; Under 3.5 goals: 58.8%; Double Chance 1X: 71.5%; Double Chance X2: 50.3%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 49.7% | 2.01 |
| Draw | 21.8% | 4.58 |
| AS Roma win | 28.5% | 3.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 2.49 |
| AS Roma expected goals | 1.45 |
| Expected total goals | 3.94 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 63.1% |
| Under 2.5 | 36.9% |
| Over 3.5 | 41.2% |
| Under 3.5 | 58.8% |
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.71% |
| 2 | 2-1 | 8.35% |
| 3 | 1-2 | 7.29% |
| 4 | 1-0 | 6.98% |
| 5 | 2-0 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 49.7% | 45.0% | 2.23 | +10.8% |
| Draw | 21.8% | 23.6% | 4.12 | -10.0% |
| AS Roma win | 28.5% | 31.4% | 3.09 | -12.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | bc0b6614c9714816038d5a0ff8963144 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester United FC |
| Matched away-team name | AS Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4913 |
| Dc lambda away | 1.4455 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.43 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.94 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.71 |
| Fair Over 3.5 odds | 2.42 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.34 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.17459479491108335, "-10": 1.1321067984799725e-07, "-11": 1.2253021444062693e-08, "-12": 1.2190933130235662e-09, "-13": 1.1221168610116495e-10, "-14": 9.607847250463262e-12, "-15": 7.68584067349247e-13, "-16": 5.72184671370869e-14, "-17": 3.552877478778128e-15, "-2": 0.07543745827095115, "-3": 0.025651740230622923, "-4": 0.00696181345948521, "-5": 0.0015640349277175462, "-6": 0.0002989196405670459, "-7": 4.9628187756913695e-05, "-8": 7.2758640032070395e-06, "-9": 9.543788722609687e-07, "0": 0.21848399515220235, "1": 0.19702910447991098, "10": 1.739664596322141e-05, "11": 3.245181536240197e-06, "12": 5.56481111489514e-07, "13": 8.828140629977622e-08, "14": 1.3027915119160804e-08, "15": 1.7962132005482854e-09, "16": 2.3047318381431264e-10, "17": 2.466505505902868e-11, "2": 0.14887568298661644, "3": 0.08725116386613574, "4": 0.04081261794890472, "5": 0.015802878271812586, "6": 0.005205493094015789, "7": 0.0014895446150313698, "8": 0.0003763807019935955, "9": 8.50905375893666e-05} |
| Raw goal margin distribution | {"-1": 0.12398306129094722, "-10": 2.957147250296939e-07, "-11": 3.784866382787582e-08, "-12": 4.458093502055519e-09, "-13": 4.862288353412684e-10, "-14": 4.936716262534155e-11, "-15": 4.687486270821136e-12, "-16": 4.1755267314265293e-13, "-17": 3.455415363126945e-14, "-18": 2.312223933929764e-15, "-2": 0.05894868340549178, "-3": 0.02257326205204611, "-4": 0.0070195983906265495, "-5": 0.0018264500686329165, "-6": 0.00040711969119352765, "-7": 7.920804356591793e-05, "-8": 1.3654030677497613e-05, "-9": 2.111060941358439e-06, "0": 0.17791732418703304, "1": 0.2111460965984907, "10": 6.839899327588148e-05, "11": 1.508846247490931e-05, "12": 3.063100764880909e-06, "13": 5.757984578877938e-07, "14": 1.0075941317756627e-07, "15": 1.6489411162529266e-08, "16": 2.5315941461124873e-09, "17": 3.6107776878760143e-10, "18": 4.1643580075108196e-11, "2": 0.1751094006454397, "3": 0.11557059548637155, "4": 0.06194167844466643, "5": 0.027777693622922747, "6": 0.010671566225226557, "7": 0.0035784340503289777, "8": 0.001063168942652961, "9": 0.0002833086624107448} |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 21.5% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 44.6% |
| Raw p btts yes | 69.8% |
| P home draw | 71.5% |
| P draw away | 50.3% |
| P home away | 78.2% |
| Raw p home draw | 78.5% |
| Raw p draw away | 39.3% |
| Raw p home away | 82.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8392 |
| Totals anchor target over 2 5 | 0.6308 |
| Totals anchor reference over odds | 1.55 |
| Totals anchor reference under odds | 2.58 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7372 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.43, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.74, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.78, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.01, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 5.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:38Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.35, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:38Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.65, "price": 2.35, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:55:47Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.5, "under": 2.58}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.09, "draw": 4.09, "home": 2.18}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.55, "under": 2.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.09, "draw": 4.12, "home": 2.23}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.73, "home_away": 1.28, "home_draw": 1.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.75, "home_away": 1.28, "home_draw": 1.42}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.18 |
| Reference draw odds | 4.09 |
| Reference away odds | 3.09 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | +4.7% |
| Draw probability edge | -1.7% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | 0.1575 |
| Raw ev home | 0.3541 |
| Raw edge prob draw | -0.0580 |
| Raw ev draw | -0.2670 |
| Raw edge prob away | -0.0996 |
| Raw ev away | -0.3361 |
| Market p home draw | 68.3% |
| Market home draw odds | 1.42 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:57:38Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.0% |
| Market draw away odds | 1.75 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:38Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.7% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.42 |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 84.3% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:55:47Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.1% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:55:47Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.34 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,468.3262 |
| Elo away rating | 1,438.9525 |
| Elo rating diff | 89.3736 |
| Elo home expectancy | 0.6259 |

</details>


---

## 2026-11-03 — Shakhtar Donetsk vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **46.5%**. Expected goals are 1.08 for Shakhtar Donetsk and 1.38 for Sporting Lisbon (2.46 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 56.9%; Under 3.5 goals: 64.7%; Double Chance 1X: 53.5%; Double Chance X2: 71.9%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 28.1% | 3.56 |
| Draw | 25.4% | 3.93 |
| Sporting Lisbon win | 46.5% | 2.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.08 |
| Sporting Lisbon expected goals | 1.38 |
| Expected total goals | 2.46 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 56.9% |
| Under 2.5 | 43.1% |
| Over 3.5 | 35.3% |
| Under 3.5 | 64.7% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.71% |
| 2 | 1-2 | 9.28% |
| 3 | 0-1 | 8.92% |
| 4 | 0-2 | 7.03% |
| 5 | 2-2 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 28.1% | 27.2% | 3.63 | +1.9% |
| Draw | 25.4% | 25.4% | 3.87 | -1.6% |
| Sporting Lisbon win | 46.5% | 47.5% | 2.08 | -3.3% |
| Over 2.5 | 56.9% | 56.5% | 1.75 | -0.4% |
| Under 2.5 | 43.1% | 43.5% | 2.26 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T17:45:00+00:00 |
| Fixture id | 55e0f74a61f7d72defa7ea0c83532ea5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0835 |
| Dc lambda away | 1.3789 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.23 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.83 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.52 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.22338694521705096, "-10": 2.99935318992609e-06, "-11": 4.505580524664283e-07, "-12": 6.21950110228142e-08, "-13": 7.937063535693319e-09, "-14": 9.342004541454308e-10, "-15": 9.114431980815878e-11, "-2": 0.138986837061541, "-3": 0.06666153630654877, "-4": 0.02536675950214154, "-5": 0.007962110781729275, "-6": 0.002121256197319949, "-7": 0.0004901918352348563, "-8": 9.992203586646168e-05, "-9": 1.820972892136222e-05, "0": 0.2542901890264358, "1": 0.16124527078206935, "10": 2.455745847089499e-07, "11": 2.8986809400467862e-08, "12": 3.144119601035683e-09, "13": 3.1528057631823354e-10, "14": 2.915890983385904e-11, "15": 2.23539701708957e-12, "2": 0.07830305042060888, "3": 0.029510337580352545, "4": 0.008823841545937603, "5": 0.0021762800208388897, "6": 0.00045558931848061016, "7": 8.272567745522617e-05, "8": 1.3250412028159159e-05, "9": 1.897428588395227e-06} |
| Raw goal margin distribution | {"-1": 0.23648226970853314, "-10": 6.678895570571017e-07, "-11": 8.279155323573952e-08, "-12": 9.421909968300461e-09, "-13": 9.865585094584218e-10, "-14": 8.779697659948609e-11, "-2": 0.1297131848794592, "-3": 0.05341145774874208, "-4": 0.017186808229379007, "-5": 0.00452198031853662, "-6": 0.0010043766209806204, "-7": 0.0001928007558747355, "-8": 3.2565697364354764e-05, "-9": 4.9088573325951155e-06, "0": 0.2560792443776158, "1": 0.1871840023961597, "10": 5.992984475370267e-08, "11": 5.8373855674733526e-09, "12": 5.219935655116002e-10, "13": 4.2947995255476435e-11, "14": 3.003263653955963e-12, "2": 0.08008880667905437, "3": 0.025912897737575935, "4": 0.0065519508519797185, "5": 0.0013545589733230839, "6": 0.00023640665324293293, "7": 3.5658714436161235e-05, "8": 4.7327240442756796e-06, "9": 5.605638147658888e-07} |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 44.3% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 48.9% |
| P home draw | 53.5% |
| P draw away | 71.9% |
| P home away | 74.6% |
| Raw p home draw | 55.7% |
| Raw p draw away | 69.9% |
| Raw p home away | 74.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2182 |
| Totals anchor target over 2 5 | 0.5693 |
| Totals anchor reference over odds | 1.71 |
| Totals anchor reference under odds | 2.23 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4477 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.69, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.69, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.33, "home_away": 1.3, "home_draw": 1.84}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.07, "draw": 3.82, "home": 3.57}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.23}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.08, "draw": 3.87, "home": 3.63}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.75, "under": 2.26}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.33, "home_away": 1.3, "home_draw": 1.84}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.57 |
| Reference draw odds | 3.82 |
| Reference away odds | 2.07 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.26 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market best over 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market best under 2 5 last update utc | 2026-11-03T13:57:38Z |
| Home probability edge | +0.9% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0297 |
| Raw ev home | 0.0940 |
| Raw edge prob draw | 0.0026 |
| Raw ev draw | -0.0090 |
| Raw edge prob away | -0.0322 |
| Raw ev away | -0.0795 |
| Market p home draw | 52.6% |
| Market home draw odds | 1.84 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:57:38Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.8% |
| Market draw away odds | 1.33 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:57:38Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.84 |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.5% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:57:37Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.73 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,464.4999 |
| Elo away rating | 1,487.5305 |
| Elo rating diff | 36.9694 |
| Elo home expectancy | 0.5530 |

</details>


---

## 2026-11-03 — Villarreal vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **65.6%**. Expected goals are 1.05 for Villarreal and 3.84 for Paris Saint Germain (4.88 combined). The most likely exact score is 1-1 at 7.9%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 69.9%; Under 3.5 goals: 49.9%; Double Chance 1X: 34.4%; Double Chance X2: 83.4%; Double Chance 12 (either team wins): 82.3%; Under 4.5 goals: 69.1%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 16.6% | 6.02 |
| Draw | 17.7% | 5.64 |
| Paris Saint Germain win | 65.6% | 1.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 1.05 |
| Paris Saint Germain expected goals | 3.84 |
| Expected total goals | 4.88 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 87.2% |
| Under 1.5 | 12.8% |
| Over 2.5 | 69.9% |
| Under 2.5 | 30.1% |
| Over 3.5 | 50.1% |
| Under 3.5 | 49.9% |
| Over 4.5 | 30.9% |
| Under 4.5 | 69.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.91% |
| 2 | 0-3 | 7.89% |
| 3 | 0-2 | 7.80% |
| 4 | 1-3 | 6.54% |
| 5 | 1-2 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 16.6% | 21.2% | 4.46 | -25.9% |
| Draw | 17.7% | 21.8% | 4.37 | -22.5% |
| Paris Saint Germain win | 65.6% | 57.0% | 1.78 | +16.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | a341241606cb5b1b59e425d00be64883 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0481 |
| Dc lambda away | 3.8351 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.56 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.81 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.32 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.24 |
| Fair Under 4.5 odds | 1.45 |
| Goal margin distribution | {"-1": 0.1517526220414927, "-10": 0.0003861015515666613, "-11": 0.00010450155174143952, "-12": 2.5999903486357323e-05, "-13": 5.984395994625359e-06, "-14": 1.2813195977228782e-06, "-15": 2.564261069777572e-07, "-16": 4.8168094152208884e-08, "-17": 8.52430906511545e-09, "-18": 1.425548073901997e-09, "-19": 2.245876152529672e-10, "-2": 0.16772658800306647, "-20": 3.025588416633229e-11, "-3": 0.14278068651076314, "-4": 0.09697056705969678, "-5": 0.054503554441240505, "-6": 0.026057161358577014, "-7": 0.010820581340624377, "-8": 0.003967572870397001, "-9": 0.0013015371209007562, "0": 0.17745032436351316, "1": 0.12094386205941089, "10": 2.52352112801819e-09, "11": 1.8666830741756555e-10, "12": 1.2692934474422594e-11, "13": 7.98459840708736e-13, "14": 4.672321028080331e-14, "15": 2.555523606632972e-15, "16": 1.31195691560607e-16, "17": 6.345440110225632e-18, "18": 2.9001928771462785e-19, "19": 1.2487435831952386e-20, "2": 0.035218243763216646, "20": 4.597690858761536e-22, "3": 0.008193655504542074, "4": 0.0015208648472782487, "5": 0.00023362427369163594, "6": 3.0525493431980906e-05, "7": 3.46440483898152e-06, "8": 3.471725716050612e-07, "9": 3.1125727103443177e-08} |
| Raw goal margin distribution | {"-1": 0.1441573616250619, "-10": 0.0020587390078974453, "-11": 0.0006970616886272097, "-12": 0.00021729377776986768, "-13": 6.274288768023036e-05, "-14": 1.6869768439168766e-05, "-15": 4.2430848421872035e-06, "-16": 1.002411994424337e-06, "-17": 2.232383494661512e-07, "-18": 4.701622494529328e-08, "-19": 9.391253088171374e-09, "-2": 0.17973735586536255, "-20": 1.7823945360523383e-09, "-21": 3.184549217255412e-10, "-22": 4.6937567498960114e-11, "-3": 0.17893084598386122, "-4": 0.14551075814688166, "-5": 0.09938736163051577, "-6": 0.05830243331231817, "-7": 0.029904579234295105, "-8": 0.013607530918562018, "-9": 0.005558683703669431, "0": 0.0832708563569209, "1": 0.04050448024229147, "10": 4.786585412100482e-09, "11": 4.42933150538405e-10, "12": 3.7736073909662965e-11, "13": 2.9779429820690963e-12, "14": 2.1882828093833888e-13, "15": 1.5042447174057835e-14, "16": 9.712375970971552e-16, "17": 5.91140188893147e-17, "18": 3.4026077800218986e-18, "19": 1.8575055999510132e-19, "2": 0.013425276913827711, "20": 9.635025783799473e-21, "21": 4.704781473992705e-22, "22": 1.895197705055454e-23, "3": 0.0036526879434093085, "4": 0.0008118296547499022, "5": 0.0001515456314324771, "6": 2.4296369995013213e-05, "7": 3.4059232702270233e-06, "8": 4.2356390676350364e-07, "9": 4.7288335805907265e-08} |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 8.3% |
| Unadjusted away-win probability | 85.8% |
| Raw p over 1 5 | 95.4% |
| Raw p under 3 5 | 28.2% |
| Raw p btts yes | 63.4% |
| P home draw | 34.4% |
| P draw away | 83.4% |
| P home away | 82.3% |
| Raw p home draw | 14.2% |
| Raw p draw away | 94.1% |
| Raw p home away | 91.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7909 |
| Totals anchor target over 2 5 | 0.6986 |
| Totals anchor reference over odds | 1.40 |
| Totals anchor reference under odds | 3.08 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8209 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.85, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.85, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:34Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.24, "home_away": 1.25, "home_draw": 2.24}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.72, "draw": 4.35, "home": 4.46}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.4, "under": 3.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.78, "draw": 4.37, "home": 4.46}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.25, "home_away": 1.25, "home_draw": 2.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.46 |
| Reference draw odds | 4.35 |
| Reference away odds | 1.72 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.08 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | -4.6% |
| Draw probability edge | -4.0% |
| Away probability edge | +8.6% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | -0.1537 |
| Raw ev home | -0.7388 |
| Raw edge prob draw | -0.1345 |
| Raw ev draw | -0.6361 |
| Raw edge prob away | 0.2882 |
| Raw ev away | 0.5275 |
| Market p home draw | 44.9% |
| Market home draw odds | 2.24 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:34Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 77.6% |
| Market draw away odds | 1.25 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:57:38Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.6% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.16 |
| Market reference dc draw away odds | 1.25 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 88.2% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.80 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.0% |
| Market under 3 5 odds | 1.89 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:57:37Z |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 2.01 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,415.1608 |
| Elo away rating | 1,614.2424 |
| Elo rating diff | -139.0817 |
| Elo home expectancy | 0.3099 |

</details>


---

## 2026-11-04 — AEK Athens vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **80.5%**. Expected goals are 0.81 for AEK Athens and 3.13 for Real Madrid (3.94 combined). The most likely exact score is 0-3 at 9.6%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 75.0%; Under 3.5 goals: 44.5%; Double Chance 1X: 19.5%; Double Chance X2: 92.3%; Double Chance 12 (either team wins): 88.2%; Under 4.5 goals: 64.1%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AEK Athens win | 7.7% | 12.98 |
| Draw | 11.8% | 8.50 |
| Real Madrid win | 80.5% | 1.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AEK Athens expected goals | 0.81 |
| Real Madrid expected goals | 3.13 |
| Expected total goals | 3.94 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 90.0% |
| Under 1.5 | 10.0% |
| Over 2.5 | 75.0% |
| Under 2.5 | 25.0% |
| Over 3.5 | 55.5% |
| Under 3.5 | 44.5% |
| Over 4.5 | 35.9% |
| Under 4.5 | 64.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 9.60% |
| 2 | 0-2 | 9.11% |
| 3 | 1-3 | 7.79% |
| 4 | 0-4 | 7.58% |
| 5 | 1-2 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AEK Athens win | 7.7% | 8.2% | 10.90 | -16.0% |
| Draw | 11.8% | 12.3% | 7.12 | -16.3% |
| Real Madrid win | 80.5% | 79.5% | 1.28 | +3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T17:45:00+00:00 |
| Fixture id | f43ef699c987e112e115f7035114854e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:37Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | PAE AEK |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8053 |
| Dc lambda away | 3.1348 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 53.75 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.05 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.00 |
| Fair Over 3.5 odds | 1.80 |
| Fair Under 3.5 odds | 2.25 |
| Fair Over 4.5 odds | 2.78 |
| Fair Under 4.5 odds | 1.56 |
| Goal margin distribution | {"-1": 0.17326490278199394, "-10": 0.0006303157362858695, "-11": 0.0001777256243037178, "-12": 4.606743156761933e-05, "-13": 1.104731747552201e-05, "-14": 2.464471611482786e-06, "-15": 5.138912273812793e-07, "-16": 1.0058231370342332e-07, "-17": 1.8547401387491166e-08, "-18": 3.2319728394048318e-09, "-19": 5.304372830439954e-10, "-2": 0.19876204060484737, "-20": 7.429879796305122e-11, "-3": 0.17581132307605804, "-4": 0.12418649231100344, "-5": 0.0726380468365189, "-6": 0.03615179758729021, "-7": 0.015632322094435505, "-8": 0.005969565083043695, "-9": 0.002039733752799303, "0": 0.11762413718968144, "1": 0.056582152594804806, "10": 9.65138604065617e-10, "11": 6.990792233816853e-11, "12": 4.654951445071584e-12, "13": 2.867627919421845e-13, "14": 1.643367123147753e-14, "15": 8.802920661663271e-16, "16": 4.426108079219215e-17, "17": 2.0966612708216237e-18, "18": 9.38550648377032e-20, "19": 3.9570256260140005e-21, "2": 0.016047467687499595, "20": 1.4238407487832156e-22, "3": 0.0036464034152391077, "4": 0.0006616632931260663, "5": 9.941951698541656e-05, "6": 1.2711072533055902e-05, "7": 1.4119541828785259e-06, "8": 1.385111101882592e-07, "9": 1.2157946012666977e-08} |
| Raw goal margin distribution | {"-1": 0.1804837068861962, "-10": 0.0006164249557494259, "-11": 0.00017242238402223937, "-12": 4.433427159794044e-05, "-13": 1.0546025952554901e-05, "-14": 2.3336174826832097e-06, "-15": 4.826592142130428e-07, "-16": 9.370139033141135e-08, "-17": 1.713782175326333e-08, "-18": 2.962021652413417e-09, "-19": 4.822619070465147e-10, "-2": 0.20607829063264976, "-20": 6.711741180046487e-11, "-3": 0.18120648770252015, "-4": 0.12714464248321997, "-5": 0.0738388484862604, "-6": 0.036477066259304566, "-7": 0.01565297081703399, "-8": 0.005931150763652609, "-9": 0.0020107079378322975, "0": 0.1048217722920886, "1": 0.048188252682102466, "10": 7.71486454931754e-10, "11": 5.543531858732104e-11, "12": 3.661653871196159e-12, "13": 2.2375428264974472e-13, "14": 1.271911809523221e-14, "15": 6.757915245857855e-16, "16": 3.370256721525031e-17, "17": 1.5834974901886655e-18, "18": 7.03063895301306e-20, "19": 2.940589049290983e-21, "2": 0.013599466197629858, "20": 1.0513114307630824e-22, "3": 0.003071907755896827, "4": 0.0005537035425380151, "5": 8.260549950929413e-05, "6": 1.0483076565423299e-05, "7": 1.1556077361761376e-06, "8": 1.124857317234477e-07, "9": 9.796078936349713e-09} |
| Unadjusted home-win probability | 6.6% |
| Unadjusted draw probability | 10.5% |
| Unadjusted away-win probability | 83.0% |
| Raw p over 1 5 | 90.1% |
| Raw p under 3 5 | 44.5% |
| Raw p btts yes | 52.7% |
| P home draw | 19.5% |
| P draw away | 92.3% |
| P home away | 88.2% |
| Raw p home draw | 17.0% |
| Raw p draw away | 93.4% |
| Raw p home away | 89.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0083 |
| Totals anchor target over 2 5 | 0.7500 |
| Totals anchor reference over odds | 1.30 |
| Totals anchor reference under odds | 3.54 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7456 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 7.0, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 8.84, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.09, "price": 8.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.88, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:45Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.32, "under": 3.38}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.07, "home_away": 1.12, "home_draw": 4.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.24, "draw": 7.12, "home": 10.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.3, "under": 3.54}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.28, "draw": 7.01, "home": 10.9}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.06, "home_away": 1.13, "home_draw": 4.08}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.42 |
| Reference draw odds | 7.12 |
| Reference away odds | 1.24 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.51 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.5% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | -0.0165 |
| Raw ev home | -0.2860 |
| Raw edge prob draw | -0.0183 |
| Raw ev draw | -0.2537 |
| Raw edge prob away | 0.0348 |
| Raw ev away | 0.0620 |
| Market p home draw | 23.6% |
| Market home draw odds | 4.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:14Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 91.0% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:14Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 85.4% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.08 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 90.0% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:56:45Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 8.00 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 46.7% |
| Market under 3 5 odds | 2.08 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:56:45Z |
| Market reference under 3 5 odds | 2.06 |
| Market reference under 3 5 opposite odds | 1.82 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,433.0433 |
| Elo away rating | 1,551.6935 |
| Elo rating diff | -58.6502 |
| Elo home expectancy | 0.4164 |

</details>


---

## 2026-11-04 — Borussia Dortmund vs Real Betis

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **54.0%**. Expected goals are 1.91 for Borussia Dortmund and 1.44 for Real Betis (3.35 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 63.9%; Under 3.5 goals: 57.9%; Double Chance 1X: 76.1%; Double Chance X2: 46.0%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 76.4%; BTTS Yes (both teams score): 63.6%; BTTS No (at least one team does not score): 36.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 54.0% | 1.85 |
| Draw | 22.1% | 4.53 |
| Real Betis win | 23.9% | 4.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 1.91 |
| Real Betis expected goals | 1.44 |
| Expected total goals | 3.35 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 83.8% |
| Under 1.5 | 16.2% |
| Over 2.5 | 63.9% |
| Under 2.5 | 36.1% |
| Over 3.5 | 42.1% |
| Under 3.5 | 57.9% |
| Over 4.5 | 23.6% |
| Under 4.5 | 76.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.24% |
| 2 | 1-1 | 9.65% |
| 3 | 1-0 | 8.26% |
| 4 | 2-0 | 7.23% |
| 5 | 2-2 | 6.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 54.0% | 56.1% | 1.80 | -2.8% |
| Draw | 22.1% | 22.4% | 4.26 | -6.0% |
| Real Betis win | 23.9% | 21.5% | 4.57 | +9.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T20:00:00+00:00 |
| Fixture id | 6d386ed81fabf67aa19fbd442c0d8c60 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:37Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Borussia Dortmund |
| Matched away-team name | Real Betis Balompié |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9111 |
| Dc lambda away | 1.4422 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.6% |
| P btts no | 36.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.13 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.16 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.77 |
| Fair Over 3.5 odds | 2.38 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.23 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.13426666631922002, "-10": 3.387670031856908e-07, "-11": 4.273583900511374e-08, "-12": 4.956497951470882e-09, "-13": 5.318583826839896e-10, "-14": 5.306212307867633e-11, "-15": 4.89779849369525e-12, "-16": 3.715579835170683e-13, "-2": 0.0673092852607638, "-3": 0.026524394568914592, "-4": 0.008359890122428335, "-5": 0.002183854251662493, "-6": 0.000485716512946524, "-7": 9.38956033353153e-05, "-8": 1.6034532867658285e-05, "-9": 2.4505770275451204e-06, "0": 0.22055701306173084, "1": 0.24172019788150367, "10": 7.738663957503873e-06, "11": 1.2936188942564118e-06, "12": 1.98810023214922e-07, "13": 2.8268878749515193e-08, "14": 3.737200743492851e-09, "15": 4.571007635350829e-10, "16": 4.5950142244220634e-11, "2": 0.161750648011134, "3": 0.08446285542926435, "4": 0.03527524823501017, "5": 0.012210751395319455, "6": 0.003598743029212351, "7": 0.0009218546581881614, "8": 0.00020860405164145295, "9": 4.224584629389953e-05} |
| Raw goal margin distribution | {"-1": 0.16512054023869635, "-10": 4.808250883192567e-07, "-11": 6.177453014370696e-08, "-12": 7.297438782572249e-09, "-13": 7.976374776021377e-10, "-14": 8.10605480719014e-11, "-15": 7.616476969234289e-12, "-16": 5.856595796210361e-13, "-2": 0.08366889622743727, "-3": 0.033412879503306826, "-4": 0.010691211181381464, "-5": 0.002838451628755128, "-6": 0.0006420620422614335, "-7": 0.0001262936431194836, "-8": 2.195226738890216e-05, "-9": 3.4157299396601144e-06, "0": 0.21237946926034562, "1": 0.21723487738558858, "10": 8.025635190224696e-06, "11": 1.366315436613754e-06, "12": 2.1387558678026378e-07, "13": 3.0977440718809955e-08, "14": 4.1715624388403264e-09, "15": 5.193887938943489e-10, "16": 5.2921594763659383e-11, "2": 0.14691376838933376, "3": 0.07774305324571808, "4": 0.032962779555424565, "5": 0.011596519029218945, "6": 0.0034759408115753107, "7": 0.0009059956188676446, "8": 0.0002086763442066037, "9": 4.302556594990053e-05} |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 29.7% |
| Raw p over 1 5 | 84.3% |
| Raw p under 3 5 | 56.9% |
| Raw p btts yes | 64.6% |
| P home draw | 76.1% |
| P draw away | 46.0% |
| P home away | 77.9% |
| Raw p home draw | 70.3% |
| Raw p draw away | 50.9% |
| Raw p home away | 78.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9812 |
| Totals anchor target over 2 5 | 0.6387 |
| Totals anchor reference over odds | 1.51 |
| Totals anchor reference under odds | 2.55 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6506 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.2, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.27, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.99, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.84, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.18, "home_away": 1.25, "home_draw": 1.24}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:21Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.5, "under": 2.57}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.44, "draw": 4.26, "home": 1.75}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.51, "under": 2.55}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.57, "draw": 4.16, "home": 1.8}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.13, "home_away": 1.27, "home_draw": 1.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.75 |
| Reference draw odds | 4.26 |
| Reference away odds | 4.44 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.57 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | -2.1% |
| Draw probability edge | -0.4% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.0702 |
| Raw ev home | -0.1160 |
| Raw edge prob draw | -0.0117 |
| Raw ev draw | -0.0953 |
| Raw edge prob away | 0.0818 |
| Raw ev away | 0.3551 |
| Market p home draw | 78.2% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:57:38Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.5% |
| Market draw away odds | 2.18 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:15Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.24 |
| Market reference dc draw away odds | 2.13 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:57:21Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.6% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:57:21Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.31 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,519.5879 |
| Elo away rating | 1,456.8479 |
| Elo rating diff | 122.7400 |
| Elo home expectancy | 0.6696 |

</details>


---

## 2026-11-04 — Fenerbahce vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **71.8%**. Expected goals are 0.59 for Fenerbahce and 3.45 for Liverpool (4.05 combined). The most likely exact score is 0-3 at 10.0%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 68.7%; Under 3.5 goals: 50.6%; Double Chance 1X: 28.2%; Double Chance X2: 87.4%; Double Chance 12 (either team wins): 84.4%; Under 4.5 goals: 69.2%; BTTS Yes (both teams score): 46.1%; BTTS No (at least one team does not score): 53.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 12.6% | 7.96 |
| Draw | 15.6% | 6.41 |
| Liverpool win | 71.8% | 1.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 0.59 |
| Liverpool expected goals | 3.45 |
| Expected total goals | 4.05 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 86.2% |
| Under 1.5 | 13.8% |
| Over 2.5 | 68.7% |
| Under 2.5 | 31.3% |
| Over 3.5 | 49.4% |
| Under 3.5 | 50.6% |
| Over 4.5 | 30.8% |
| Under 4.5 | 69.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 10.01% |
| 2 | 0-2 | 8.96% |
| 3 | 0-4 | 8.40% |
| 4 | 1-1 | 7.34% |
| 5 | 1-3 | 5.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 12.6% | 16.5% | 5.89 | -26.0% |
| Draw | 15.6% | 19.2% | 4.93 | -23.1% |
| Liverpool win | 71.8% | 64.3% | 1.55 | +11.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T17:45:00+00:00 |
| Fixture id | e901dbcdd6e2255fb24d84032b9d437a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Fenerbahçe SK |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.5908 |
| Dc lambda away | 3.4543 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 46.1% |
| P btts no | 53.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.54 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.23 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.24 |
| Fair Under 4.5 odds | 1.45 |
| Goal margin distribution | {"-1": 0.12571123089140568, "-10": 0.0009399618087832673, "-11": 0.00028251656874255464, "-12": 7.800628293971864e-05, "-13": 1.991570491555874e-05, "-14": 4.727956233960102e-06, "-15": 1.0487550504601352e-06, "-16": 2.182967708013862e-07, "-17": 4.279832677711716e-08, "-18": 7.929836636872662e-09, "-19": 1.3925543894642395e-09, "-2": 0.16274065319123188, "-20": 2.3160963801947413e-10, "-21": 3.388470341655795e-11, "-3": 0.1586157163776433, "-4": 0.12193952318840505, "-5": 0.07705973674245178, "-6": 0.0412455164906271, "-7": 0.019121077403274817, "-8": 0.007811565018343816, "-9": 0.0028510119936062906, "0": 0.1558860884943001, "1": 0.10062869323914264, "10": 8.902520898778042e-11, "11": 4.57672888460783e-12, "12": 2.1614705244678814e-13, "13": 9.438954367001328e-15, "14": 3.832746726087953e-16, "15": 1.4541834878163053e-17, "16": 5.177271318433463e-19, "17": 1.736156513940849e-20, "18": 5.502180003937757e-22, "19": 1.652689204860184e-23, "2": 0.02103929040036357, "20": 4.701583154219656e-25, "21": 1.1765209164761235e-26, "3": 0.0035074357185824988, "4": 0.0004612076113550284, "5": 4.985261734476399e-05, "6": 4.56400025280041e-06, "7": 3.6190096655818697e-07, "8": 2.5288548660719587e-08, "9": 1.5786773130243727e-09} |
| Raw goal margin distribution | {"-1": 0.14892476861927156, "-10": 0.0014030118555686843, "-11": 0.0004339657613004008, "-12": 0.00012332658791088503, "-13": 3.241023575529557e-05, "-14": 7.920537244388166e-06, "-15": 1.808751154242947e-06, "-16": 3.876140771422563e-07, "-17": 7.824318147659787e-08, "-18": 1.4926845347636637e-08, "-19": 2.6990154962847607e-09, "-2": 0.19632360722512088, "-20": 4.6203221021728e-10, "-21": 6.926872101214614e-11, "-3": 0.19568450565812642, "-4": 0.15421344249535954, "-5": 0.10004041268761416, "-6": 0.05501388593047852, "-7": 0.02621837544748275, "-8": 0.011015468799110905, "-9": 0.004135810251747381, "0": 0.07260210099642306, "1": 0.02695366172896803, "10": 3.007087332320283e-11, "11": 1.590921080596665e-12, "12": 7.73318422439653e-14, "13": 3.4761003106069064e-15, "14": 1.4530254491152664e-16, "15": 5.675522786723911e-18, "16": 2.0803435540098225e-19, "17": 7.182745713063819e-21, "18": 2.3437996967483723e-22, "19": 7.248803190575649e-24, "2": 0.00574366980725664, "20": 2.1224704555407877e-25, "21": 5.44270805321707e-27, "3": 0.0009792235500058486, "4": 0.00013199458415115797, "5": 1.46459593613509e-05, "6": 1.377600027496748e-06, "7": 1.1229620208832777e-07, "8": 8.069948160214894e-09, "9": 5.182470464008928e-10} |
| Unadjusted home-win probability | 3.4% |
| Unadjusted draw probability | 7.3% |
| Unadjusted away-win probability | 89.4% |
| Raw p over 1 5 | 91.0% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 43.0% |
| P home draw | 28.2% |
| P draw away | 87.4% |
| P home away | 84.4% |
| Raw p home draw | 10.6% |
| Raw p draw away | 96.6% |
| Raw p home away | 92.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9709 |
| Totals anchor target over 2 5 | 0.6870 |
| Totals anchor reference over odds | 1.42 |
| Totals anchor reference under odds | 2.96 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7029 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.53, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.35, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.7, "price": 2.35, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:35Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.17, "home_away": 1.21, "home_draw": 2.66}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.53, "draw": 4.92, "home": 5.68}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.42, "under": 2.96}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.55, "draw": 4.93, "home": 5.89}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.17, "home_away": 1.22, "home_draw": 2.61}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.68 |
| Reference draw odds | 4.92 |
| Reference away odds | 1.53 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.96 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | -3.9% |
| Draw probability edge | -3.6% |
| Away probability edge | +7.5% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.1312 |
| Raw ev home | -0.8008 |
| Raw edge prob draw | -0.1190 |
| Raw ev draw | -0.6421 |
| Raw edge prob away | 0.2502 |
| Raw ev away | 0.3850 |
| Market p home draw | 37.2% |
| Market home draw odds | 2.66 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:35Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.1% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:57:38Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.7% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.61 |
| Market reference dc draw away odds | 1.17 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 87.4% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.5% |
| Market under 3 5 odds | 1.83 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:57:37Z |
| Market reference under 3 5 odds | 1.81 |
| Market reference under 3 5 opposite odds | 2.07 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,423.6387 |
| Elo away rating | 1,539.8399 |
| Elo rating diff | -56.2012 |
| Elo home expectancy | 0.4198 |

</details>


---

## 2026-11-04 — PSV Eindhoven vs Club Brugge

The model's most likely 1X2 outcome is **PSV Eindhoven win** at **47.9%**. Expected goals are 2.41 for PSV Eindhoven and 1.90 for Club Brugge (4.30 combined). The most likely exact score is 2-1 at 8.4%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 72.0%; Under 3.5 goals: 48.6%; Double Chance 1X: 68.5%; Double Chance X2: 52.1%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 68.1%; BTTS Yes (both teams score): 70.5%; BTTS No (at least one team does not score): 29.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PSV Eindhoven win | 47.9% | 2.09 |
| Draw | 20.5% | 4.87 |
| Club Brugge win | 31.5% | 3.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| PSV Eindhoven expected goals | 2.41 |
| Club Brugge expected goals | 1.90 |
| Expected total goals | 4.30 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 88.3% |
| Under 1.5 | 11.7% |
| Over 2.5 | 72.0% |
| Under 2.5 | 28.0% |
| Over 3.5 | 51.4% |
| Under 3.5 | 48.6% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.44% |
| 2 | 1-1 | 7.92% |
| 3 | 2-2 | 7.19% |
| 4 | 1-2 | 6.83% |
| 5 | 3-1 | 5.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 47.9% | 47.1% | 2.13 | +2.1% |
| Draw | 20.5% | 21.3% | 4.49 | -7.7% |
| Club Brugge win | 31.5% | 31.6% | 3.16 | -0.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T20:00:00+00:00 |
| Fixture id | 449d718632202f0e5997d2e4b7273483 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:37Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | PSV |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.4050 |
| Dc lambda away | 1.8982 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 70.5% |
| P btts no | 29.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 49.91 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.56 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.57 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.13 |
| Fair Under 4.5 odds | 1.47 |
| Goal margin distribution | {"-1": 0.16467002197454514, "-10": 1.3422496393799438e-06, "-11": 1.962207317982314e-07, "-12": 2.639418311276068e-08, "-13": 3.2870622494973285e-09, "-14": 3.8101655659608527e-10, "-15": 4.125876839134567e-11, "-16": 4.1340563314675024e-12, "-17": 3.3344948289303855e-13, "-2": 0.0906628427101469, "-3": 0.039919868986411505, "-4": 0.014241164256075047, "-5": 0.004244675714550539, "-6": 0.0010827848098909094, "-7": 0.00024092585054677604, "-8": 4.747476552671656e-05, "-9": 8.387625713588301e-06, "0": 0.20548924243091682, "1": 0.20263125391019174, "10": 1.3974959113877241e-05, "11": 2.5885292317154266e-06, "12": 4.4117139003923196e-07, "13": 6.96142224569869e-08, "14": 1.022409387702678e-08, "15": 1.4027755031723998e-09, "16": 1.7808987789764518e-10, "17": 1.8200521288515408e-11, "2": 0.14210819418306925, "3": 0.07928112946079256, "4": 0.03583580374797512, "5": 0.013533405763505861, "6": 0.004374170162933519, "7": 0.0012331839191568972, "8": 0.00030789186417898165, "9": 6.892318839499203e-05} |
| Raw goal margin distribution | {"-1": 0.15343991706098858, "-10": 3.403640282581856e-06, "-11": 5.682242036160088e-07, "-12": 8.738547246830898e-08, "-13": 1.2453459579202406e-08, "-14": 1.6531774387216844e-09, "-15": 2.053267039144114e-10, "-16": 2.391313508733412e-11, "-17": 2.5696649098039007e-12, "-18": 2.1615729528665123e-13, "-2": 0.09044165784269469, "-3": 0.04345422743930794, "-4": 0.01717621016340083, "-5": 0.005728784284257063, "-6": 0.0016461941280461027, "-7": 0.0004145242412268777, "-8": 9.274669534668138e-05, "-9": 1.865128623235463e-05, "0": 0.18762884311562839, "1": 0.19359036203552807, "10": 3.6295516558785266e-05, "11": 7.677502879984504e-06, "12": 1.4959959946145538e-06, "13": 2.7012957805854713e-07, "14": 4.543520868787317e-08, "15": 7.1500557095014265e-09, "16": 1.0550946963587122e-09, "17": 1.4365553022994596e-10, "18": 1.5311110317008883e-11, "2": 0.1451945716889787, "3": 0.08839034543302164, "4": 0.044268119746738874, "5": 0.018707559392200326, "6": 0.0068112472295477474, "7": 0.002173133775136491, "8": 0.0006160641053785198, "9": 0.00015697380338159202} |
| Unadjusted home-win probability | 50.0% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 31.2% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 37.7% |
| Raw p btts yes | 77.0% |
| P home draw | 68.5% |
| P draw away | 52.1% |
| P home away | 79.5% |
| Raw p home draw | 68.8% |
| Raw p draw away | 50.0% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8688 |
| Totals anchor target over 2 5 | 0.7200 |
| Totals anchor reference over odds | 1.35 |
| Totals anchor reference under odds | 3.20 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7991 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.55, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.13, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.86, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.63, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:48:21Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.35, "under": 3.17}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:35Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.81, "home_away": 1.24, "home_draw": 1.41}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.06, "draw": 4.49, "home": 2.08}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.35, "under": 3.2}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.16, "draw": 4.37, "home": 2.13}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.8, "home_away": 1.25, "home_draw": 1.41}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 4.49 |
| Reference away odds | 3.06 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.26 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.8% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.0294 |
| Raw ev home | 0.0649 |
| Raw edge prob draw | -0.0255 |
| Raw ev draw | -0.1575 |
| Raw edge prob away | -0.0039 |
| Raw ev away | -0.0128 |
| Market p home draw | 68.7% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:57:38Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.8% |
| Market draw away odds | 1.81 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:35Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.5% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.41 |
| Market reference dc draw away odds | 1.80 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 89.2% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:48:21Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 7.60 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.0% |
| Market under 3 5 odds | 1.99 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:48:21Z |
| Market reference under 3 5 odds | 1.97 |
| Market reference under 3 5 opposite odds | 1.90 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,466.2523 |
| Elo away rating | 1,460.9610 |
| Elo rating diff | 65.2913 |
| Elo home expectancy | 0.5929 |

</details>


---

## 2026-11-04 — Porto vs Napoli

The model's most likely 1X2 outcome is **Porto win** at **51.6%**. Expected goals are 1.64 for Porto and 0.98 for Napoli (2.62 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 55.3%; Under 3.5 goals: 66.4%; Double Chance 1X: 75.8%; Double Chance X2: 48.4%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 51.6% | 1.94 |
| Draw | 24.2% | 4.12 |
| Napoli win | 24.2% | 4.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 1.64 |
| Napoli expected goals | 0.98 |
| Expected total goals | 2.62 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 55.3% |
| Under 2.5 | 44.7% |
| Over 3.5 | 33.6% |
| Under 3.5 | 66.4% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.36% |
| 2 | 1-0 | 9.59% |
| 3 | 2-1 | 9.17% |
| 4 | 2-0 | 8.38% |
| 5 | 0-1 | 6.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 51.6% | 50.7% | 2.05 | +5.7% |
| Draw | 24.2% | 24.6% | 3.89 | -5.7% |
| Napoli win | 24.2% | 24.7% | 3.88 | -6.2% |
| Over 2.5 | 55.3% | 54.6% | 1.81 | +0.1% |
| Under 2.5 | 44.7% | 45.4% | 2.17 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T20:00:00+00:00 |
| Fixture id | ba82ee37f64a66a30d85f8b90082ec2f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:37Z |
| Market best away last update utc | 2026-11-03T13:57:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6422 |
| Dc lambda away | 0.9753 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.76 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.63 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.89 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.15321631260188578, "-10": 4.559961081900096e-08, "-11": 4.469543697249564e-09, "-12": 4.024953086024858e-10, "-13": 3.351731834690896e-11, "-14": 2.5947503543789102e-12, "-15": 1.8652669940039407e-13, "-16": 1.1330840275647903e-14, "-2": 0.06253511803101883, "-3": 0.0197777281257127, "-4": 0.004943093648859088, "-5": 0.0010166813082828942, "-6": 0.00017722979079615357, "-7": 2.6771556780386883e-05, "-8": 3.56482684056007e-06, "-9": 4.2416793101265846e-07, "0": 0.24249720084271154, "1": 0.22420635917358123, "10": 7.36450772983356e-06, "11": 1.215349328529967e-06, "12": 1.842697777438113e-07, "13": 2.583556152480548e-08, "14": 3.367437720377989e-09, "15": 4.075682544313029e-10, "16": 4.1684712745396165e-11, "2": 0.15640972334423497, "3": 0.08328590861468631, "4": 0.035046876279718656, "5": 0.012136421961797568, "6": 0.003562032723888106, "7": 0.0009059206473578272, "8": 0.00020310018653426037, "9": 4.068788033401302e-05} |
| Raw goal margin distribution | {"-1": 0.15145931925967146, "-10": 1.8110005573248267e-08, "-11": 1.5867167001131617e-09, "-12": 1.2766645691575277e-10, "-13": 9.493739985644702e-12, "-14": 6.53298974602266e-13, "-15": 3.8381258817596953e-14, "-2": 0.05738411658857121, "-3": 0.016597893615675846, "-4": 0.003760746654401984, "-5": 0.0006976898202036886, "-6": 0.00010935809331353987, "-7": 1.4822563459477442e-05, "-8": 1.7684801207600498e-06, "-9": 1.883491045595804e-07, "0": 0.2342208021424298, "1": 0.2510106193462273, "10": 3.31491272912731e-06, "11": 4.889993249480026e-07, "12": 6.624315736437726e-08, "13": 8.293863873941673e-09, "14": 9.609192597269748e-10, "15": 9.504942359804186e-11, "2": 0.16266810345544705, "3": 0.0792171167192958, "4": 0.030220071251986128, "5": 0.009439285980516774, "6": 0.0024910534076020706, "7": 0.0005684742261010213, "8": 0.00011419392345476991, "9": 2.0476782798928978e-05} |
| Unadjusted home-win probability | 53.6% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 73.0% |
| Raw p under 3 5 | 73.2% |
| Raw p btts yes | 49.7% |
| P home draw | 75.8% |
| P draw away | 48.4% |
| P home away | 75.8% |
| Raw p home draw | 77.0% |
| Raw p draw away | 46.4% |
| Raw p home away | 76.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1221 |
| Totals anchor target over 2 5 | 0.5530 |
| Totals anchor reference over odds | 1.75 |
| Totals anchor reference under odds | 2.14 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4823 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.75, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.53, "price": 2.75, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.94, "home_away": 1.29, "home_draw": 1.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.88, "draw": 3.89, "home": 1.93}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.75, "under": 2.14}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.73, "draw": 3.84, "home": 2.05}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.17}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.86, "home_away": 1.31, "home_draw": 1.32}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.93 |
| Reference draw odds | 3.89 |
| Reference away odds | 3.88 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market best over 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market best under 2 5 last update utc | 2026-11-03T13:57:38Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0285 |
| Raw ev home | 0.0983 |
| Raw edge prob draw | -0.0118 |
| Raw ev draw | -0.0889 |
| Raw edge prob away | -0.0167 |
| Raw ev away | -0.1075 |
| Market p home draw | 73.6% |
| Market home draw odds | 1.32 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:57:38Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.2% |
| Market draw away odds | 1.94 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:14Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.32 |
| Market reference dc draw away odds | 1.86 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 79.4% |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.35 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.0% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:57:37Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,455.3450 |
| Elo away rating | 1,429.9005 |
| Elo rating diff | 85.4445 |
| Elo home expectancy | 0.6205 |

</details>


---

## 2026-11-04 — RB Leipzig vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **59.0%**. Expected goals are 1.26 for RB Leipzig and 1.75 for Manchester City (3.01 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 72.5%; Under 3.5 goals: 47.8%; Double Chance 1X: 41.0%; Double Chance X2: 79.2%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 67.4%; BTTS Yes (both teams score): 69.8%; BTTS No (at least one team does not score): 30.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 20.8% | 4.80 |
| Draw | 20.1% | 4.96 |
| Manchester City win | 59.0% | 1.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.26 |
| Manchester City expected goals | 1.75 |
| Expected total goals | 3.01 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 72.5% |
| Under 2.5 | 27.5% |
| Over 3.5 | 52.2% |
| Under 3.5 | 47.8% |
| Over 4.5 | 32.6% |
| Under 4.5 | 67.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.90% |
| 2 | 1-1 | 7.79% |
| 3 | 1-3 | 7.22% |
| 4 | 2-2 | 7.04% |
| 5 | 0-2 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 20.8% | 17.7% | 5.58 | +16.2% |
| Draw | 20.1% | 19.2% | 4.92 | -0.9% |
| Manchester City win | 59.0% | 63.1% | 1.58 | -6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T20:00:00+00:00 |
| Fixture id | df7d2d81b9e2f3f11c6aeddaee6b7085 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:37Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Manchester City FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2555 |
| Dc lambda away | 1.7512 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 69.8% |
| P btts no | 30.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 50.56 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.91 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.64 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.09 |
| Fair Over 4.5 odds | 3.07 |
| Fair Under 4.5 odds | 1.48 |
| Goal margin distribution | {"-1": 0.23723812781353873, "-10": 2.4893798296047868e-05, "-11": 4.8293015615273565e-06, "-12": 8.620321667083208e-07, "-13": 1.4246048310960521e-07, "-14": 2.191281639536554e-08, "-15": 3.1487633430062248e-09, "-16": 4.18705101742665e-10, "-17": 4.484116817915719e-11, "-2": 0.17456422951612363, "-3": 0.10205634255321382, "-4": 0.048332258390943135, "-5": 0.01912157117253755, "-6": 0.006474012696831418, "-7": 0.0019118023312954158, "-8": 0.0004999578834511904, "-9": 0.00011722170282912267, "0": 0.2014822622676428, "1": 0.11281934502932012, "10": 5.880245784512387e-07, "11": 8.1784966622841e-08, "12": 1.0466403404963372e-08, "13": 1.2400901362456346e-09, "14": 1.3675458081451353e-10, "15": 1.4088622941228129e-11, "16": 1.343141043285445e-12, "17": 1.0312765161793969e-13, "2": 0.05907188493761919, "3": 0.024759987203045737, "4": 0.00840683157536057, "5": 0.0023845348547712375, "6": 0.0005788132840837126, "7": 0.0001225442032177082, "8": 2.2975662804429552e-05, "9": 3.862135408958967e-06} |
| Raw goal margin distribution | {"-1": 0.22928396627762923, "-10": 4.5066776882081515e-06, "-11": 7.05859449763689e-07, "-12": 1.0159230042855598e-07, "-13": 1.3523222781335495e-08, "-14": 1.6735497584623687e-09, "-15": 1.9213056288332453e-10, "-16": 1.8487968926948435e-11, "-2": 0.14913594181312162, "-3": 0.07465170635034567, "-4": 0.029636660077028944, "-5": 0.009702868655236159, "-6": 0.002695966532345965, "-7": 0.000649677825596791, "-8": 0.00013809462486672543, "-9": 2.6241155357568957e-05, "0": 0.22387523530703216, "1": 0.1659225022728211, "10": 1.616981025398404e-07, "11": 1.8157309666947434e-08, "12": 1.8736087419886736e-09, "13": 1.7880643924829715e-10, "14": 1.586450127714559e-11, "15": 1.3057772328808883e-12, "16": 9.008379674472824e-14, "2": 0.07665703303276983, "3": 0.02751023285816702, "4": 0.007830123803675062, "5": 0.0018379105251647293, "6": 0.00036612008235498074, "7": 6.325457487034889e-05, "8": 9.639522344287316e-06, "9": 1.3132473546300733e-06} |
| Unadjusted home-win probability | 28.0% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 49.6% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 58.6% |
| P home draw | 41.0% |
| P draw away | 79.2% |
| P home away | 79.9% |
| Raw p home draw | 50.4% |
| Raw p draw away | 72.0% |
| Raw p home away | 77.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2496 |
| Totals anchor target over 2 5 | 0.7254 |
| Totals anchor reference over odds | 1.34 |
| Totals anchor reference under odds | 3.25 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5885 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 6.73, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.21, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 3.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.18, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:02Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.36, "under": 3.08}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:34Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.19, "home_away": 1.21, "home_draw": 2.56}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.56, "draw": 4.92, "home": 5.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.34, "under": 3.25}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.58, "draw": 4.88, "home": 5.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.18, "home_away": 1.22, "home_draw": 2.54}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.31 |
| Reference draw odds | 4.92 |
| Reference away odds | 1.56 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.32 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | +3.1% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.1029 |
| Raw ev home | 0.5635 |
| Raw edge prob draw | 0.0320 |
| Raw ev draw | 0.1015 |
| Raw edge prob away | -0.1349 |
| Raw ev away | -0.2164 |
| Market p home draw | 38.2% |
| Market home draw odds | 2.56 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:34Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 82.2% |
| Market draw away odds | 1.19 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:34Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.54 |
| Market reference dc draw away odds | 1.18 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 89.0% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:57:02Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 7.20 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 50.3% |
| Market under 3 5 odds | 1.99 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:57:37Z |
| Market reference under 3 5 odds | 1.92 |
| Market reference under 3 5 opposite odds | 1.94 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,451.6737 |
| Elo away rating | 1,506.6178 |
| Elo rating diff | 5.0559 |
| Elo home expectancy | 0.5073 |

</details>


---

## 2026-11-04 — RC Lens vs Como

The model's most likely 1X2 outcome is **Como win** at **54.3%**. Expected goals are 1.32 for RC Lens and 3.30 for Como (4.62 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 62.6%; Under 3.5 goals: 59.1%; Double Chance 1X: 45.7%; Double Chance X2: 74.8%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 77.1%; BTTS Yes (both teams score): 57.8%; BTTS No (at least one team does not score): 42.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 25.2% | 3.97 |
| Draw | 20.5% | 4.87 |
| Como win | 54.3% | 1.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.32 |
| Como expected goals | 3.30 |
| Expected total goals | 4.62 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 82.6% |
| Under 1.5 | 17.4% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 40.9% |
| Under 3.5 | 59.1% |
| Over 4.5 | 22.9% |
| Under 4.5 | 77.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.37% |
| 2 | 0-2 | 7.77% |
| 3 | 1-2 | 7.46% |
| 4 | 2-1 | 7.05% |
| 5 | 1-0 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 25.2% | 31.0% | 3.12 | -21.4% |
| Draw | 20.5% | 24.0% | 4.00 | -17.9% |
| Como win | 54.3% | 45.0% | 2.27 | +23.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T20:00:00+00:00 |
| Fixture id | 013cecbf40f5b4530342632a80f35b00 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:37Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3151 |
| Dc lambda away | 3.3046 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 57.8% |
| P btts no | 42.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.50 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.76 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.45 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.36 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.1771118499674491, "-10": 6.000878271955558e-05, "-11": 1.292319201933641e-05, "-12": 2.5577508680085707e-06, "-13": 4.682429568516548e-07, "-14": 7.972822317440913e-08, "-15": 1.2687214928031078e-08, "-16": 1.8942768984339912e-09, "-17": 2.646984774937819e-10, "-18": 3.140498177589981e-11, "-2": 0.1578724555708099, "-3": 0.10803046854769269, "-4": 0.05875612360725472, "-5": 0.026387339434392452, "-6": 0.01006542870699257, "-7": 0.0033317496908540885, "-8": 0.0009731303430633609, "-9": 0.0002541647017736299, "0": 0.20532684473812557, "1": 0.17196309640886592, "10": 1.4210232321107228e-08, "11": 1.21784628903816e-09, "12": 9.592178219527219e-11, "13": 6.988220032567696e-12, "14": 4.735258817610083e-13, "15": 2.998708507604209e-14, "16": 1.7817539747496233e-15, "17": 9.908137741650952e-17, "18": 4.678164151068369e-18, "2": 0.05942951352906998, "3": 0.01618372125456008, "4": 0.003502850356513743, "5": 0.0006260375325240233, "6": 9.503276453146302e-05, "7": 1.2518427282450659e-05, "8": 1.4550728522462886e-06, "9": 1.5123951576280358e-07} |
| Raw goal margin distribution | {"-1": 0.17998829444005124, "-10": 0.000622333674866339, "-11": 0.00018115673760156598, "-12": 4.8566220547945245e-05, "-13": 1.2063392976476793e-05, "-14": 2.790775627562079e-06, "-15": 6.040665884131117e-07, "-16": 1.2282882009430987e-07, "-17": 2.354648162614268e-08, "-18": 4.269005901080516e-09, "-19": 7.333245361307514e-10, "-2": 0.18891310967307462, "-20": 1.1796012325761304e-10, "-21": 1.537983010673165e-11, "-3": 0.1596026805869523, "-4": 0.11062460711205373, "-5": 0.06458198033634603, "-6": 0.0324425904789178, "-7": 0.01426893170499953, "-8": 0.005572796353250296, "-9": 0.0019552995639333082, "0": 0.12471344152717838, "1": 0.07291691599561727, "10": 6.199925756304751e-08, "11": 7.182142159111594e-09, "12": 7.662493736273813e-10, "13": 7.574284593456582e-11, "14": 6.973220267864824e-12, "15": 6.00661223053702e-13, "16": 4.8605048373886624e-14, "17": 3.708031726546175e-15, "18": 2.6753492982384123e-16, "19": 1.8288844699200045e-17, "2": 0.029918149941107947, "20": 1.1707430607597728e-18, "21": 6.074551682679634e-20, "3": 0.010058868656875566, "4": 0.00277457849732566, "5": 0.0006446039340592307, "6": 0.0001288645426938001, "7": 2.2555148481915667e-05, "8": 3.5056109984721186e-06, "9": 4.894858840546691e-07} |
| Unadjusted home-win probability | 11.6% |
| Unadjusted draw probability | 12.5% |
| Unadjusted away-win probability | 75.9% |
| Raw p over 1 5 | 94.2% |
| Raw p under 3 5 | 32.2% |
| Raw p btts yes | 70.3% |
| P home draw | 45.7% |
| P draw away | 74.8% |
| P home away | 79.5% |
| Raw p home draw | 24.1% |
| Raw p draw away | 88.4% |
| Raw p home away | 87.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7292 |
| Totals anchor target over 2 5 | 0.6256 |
| Totals anchor reference over odds | 1.54 |
| Totals anchor reference under odds | 2.47 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8059 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.6, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.93, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.76, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.99, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 3.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.76, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:03Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.54, "under": 2.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:34Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.4, "home_away": 1.28, "home_draw": 1.75}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.17, "draw": 4.0, "home": 3.12}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.54, "under": 2.47}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.27, "draw": 4.0, "home": 3.07}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.43, "home_away": 1.29, "home_draw": 1.71}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.12 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.17 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | -5.8% |
| Draw probability edge | -3.5% |
| Away probability edge | +9.3% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.1934 |
| Raw ev home | -0.6366 |
| Raw edge prob draw | -0.1152 |
| Raw ev draw | -0.5011 |
| Raw edge prob away | 0.3085 |
| Raw ev away | 0.7225 |
| Market p home draw | 56.8% |
| Market home draw odds | 1.75 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:34Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.9% |
| Market draw away odds | 1.43 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:57:38Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.3% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.71 |
| Market reference dc draw away odds | 1.43 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:57:03Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.2% |
| Market under 3 5 odds | 1.67 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:57:03Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.40 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,454.3293 |
| Elo away rating | 1,441.4088 |
| Elo rating diff | 72.9205 |
| Elo home expectancy | 0.6034 |

</details>


---

## 2026-11-04 — Slavia Praha vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **81.9%**. Expected goals are 0.32 for Slavia Praha and 3.01 for Arsenal (3.33 combined). The most likely exact score is 0-3 at 14.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 64.3%; Under 3.5 goals: 56.0%; Double Chance 1X: 18.1%; Double Chance X2: 93.8%; Double Chance 12 (either team wins): 88.1%; Under 4.5 goals: 74.0%; BTTS Yes (both teams score): 29.8%; BTTS No (at least one team does not score): 70.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Slavia Praha win | 6.2% | 16.14 |
| Draw | 11.9% | 8.37 |
| Arsenal win | 81.9% | 1.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Slavia Praha expected goals | 0.32 |
| Arsenal expected goals | 3.01 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 44.0% |
| Under 3.5 | 56.0% |
| Over 4.5 | 26.0% |
| Under 4.5 | 74.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 14.17% |
| 2 | 0-2 | 13.19% |
| 3 | 0-4 | 11.43% |
| 4 | 0-1 | 8.32% |
| 5 | 0-5 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Slavia Praha win | 6.2% | 7.9% | 11.60 | -28.2% |
| Draw | 11.9% | 13.8% | 6.90 | -17.6% |
| Arsenal win | 81.9% | 78.3% | 1.27 | +4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T20:00:00+00:00 |
| Fixture id | a5910ae3b314876faea7f5c03b8aeaad |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | SK Slavia Praha |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.3172 |
| Dc lambda away | 3.0128 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 29.8% |
| P btts no | 70.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.58 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.01 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.84 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.13691372072306873, "-10": 0.0009376254638240136, "-11": 0.0002725955569258968, "-12": 7.273822347949222e-05, "-13": 1.793380368267946e-05, "-14": 4.109041675059005e-06, "-15": 8.792750170105661e-07, "-16": 1.7648611208674053e-07, "-17": 3.3354883270405e-08, "-18": 5.955739866442997e-09, "-19": 1.0064555013804419e-09, "-2": 0.18708260681615235, "-20": 1.5383929989029e-10, "-3": 0.18504247606365798, "-4": 0.14167363353135443, "-5": 0.08822274661019595, "-6": 0.04622832099428166, "-7": 0.02089152704825795, "-8": 0.008295616307672596, "-9": 0.002936641091917051, "0": 0.1194678503013669, "1": 0.053980409185919974, "10": 5.409902317803176e-13, "11": 1.6559319089401074e-14, "12": 4.652110946873207e-16, "13": 1.2076009799100464e-17, "14": 2.9130991280142734e-19, "15": 6.563010855477812e-21, "16": 1.3869237864513503e-22, "17": 2.7597208680960955e-24, "18": 5.188061608170636e-26, "19": 9.230551592880932e-28, "2": 0.007149638258301457, "20": 1.4854705374974534e-29, "3": 0.0007445360982033681, "4": 6.001599797006946e-05, "5": 3.934796222581836e-06, "6": 2.1707682623258107e-07, "7": 1.0328546294036362e-08, "8": 4.3179871277225797e-10, "9": 1.6093378661118955e-11} |
| Raw goal margin distribution | {"-1": 0.16996521266030234, "-10": 0.000662791705890757, "-11": 0.00018023818887610304, "-12": 4.497833506681667e-05, "-13": 1.036984460633009e-05, "-14": 2.221552397684879e-06, "-15": 4.444489560287248e-07, "-16": 8.339881894606683e-08, "-17": 1.4734550678951974e-08, "-18": 2.459373692862205e-09, "-19": 3.886061085581952e-10, "-2": 0.2207834834015659, "-20": 5.5870710250598444e-11, "-3": 0.20604577568468288, "-4": 0.14832255308198072, "-5": 0.08667384272622038, "-6": 0.042569839225008066, "-7": 0.018018801168357274, "-8": 0.006697998274451298, "-9": 0.0022188641270776514, "0": 0.07567039559682898, "1": 0.019424877829373677, "10": 1.1092100162093666e-13, "11": 3.1757565613032743e-15, "12": 8.34386822171171e-17, "13": 2.0253495195838094e-18, "14": 4.568230042564099e-20, "15": 9.62225732121318e-22, "16": 1.9009848182883096e-23, "17": 3.536057485413728e-25, "18": 6.213990927092903e-27, "19": 1.0337591971619568e-28, "2": 0.0024473378369045478, "20": 1.5647956402268856e-30, "3": 0.0002404665820203809, "4": 1.82247625836103e-05, "5": 1.1212602093339478e-06, "6": 5.798077826341401e-08, "7": 2.5838755670600805e-09, "8": 1.0112403851194693e-10, "9": 3.526986153386452e-12} |
| Unadjusted home-win probability | 2.2% |
| Unadjusted draw probability | 7.6% |
| Unadjusted away-win probability | 90.2% |
| Raw p over 1 5 | 84.3% |
| Raw p under 3 5 | 57.4% |
| Raw p btts yes | 25.7% |
| P home draw | 18.1% |
| P draw away | 93.8% |
| P home away | 88.1% |
| Raw p home draw | 9.8% |
| Raw p draw away | 97.8% |
| Raw p home away | 92.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0702 |
| Totals anchor target over 2 5 | 0.6434 |
| Totals anchor reference over odds | 1.50 |
| Totals anchor reference under odds | 2.58 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6065 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 9.26, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.08, "price": 9.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 7.14, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.17, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.14, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.07, "home_away": 1.14, "home_draw": 4.17}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.26, "draw": 6.47, "home": 10.97}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.5, "under": 2.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.27, "draw": 6.9, "home": 11.6}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.06, "home_away": 1.14, "home_draw": 4.14}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:41Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.5, "under": 2.59}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.97 |
| Reference draw odds | 6.47 |
| Reference away odds | 1.26 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.66 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:57Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:57Z |
| Home probability edge | -1.7% |
| Draw probability edge | -1.9% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0569 |
| Raw ev home | -0.7433 |
| Raw edge prob draw | -0.0626 |
| Raw ev draw | -0.4779 |
| Raw edge prob away | 0.1194 |
| Raw ev away | 0.1458 |
| Market p home draw | 23.4% |
| Market home draw odds | 4.17 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:14Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 91.5% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:14Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 85.1% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.14 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 85.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:57:41Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.15 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:41Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.7% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:57:41Z |
| Market reference under 3 5 odds | 1.71 |
| Market reference under 3 5 opposite odds | 2.32 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:41Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,396.3129 |
| Elo away rating | 1,607.4181 |
| Elo rating diff | -151.1051 |
| Elo home expectancy | 0.2953 |

</details>


---

## 2026-11-04 — Viking FK vs Sabah FK

The model's most likely 1X2 outcome is **Viking FK win** at **74.6%**. Expected goals are 3.85 for Viking FK and 0.91 for Sabah FK (4.76 combined). The most likely exact score is 3-0 at 9.3%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 72.1%; Under 3.5 goals: 47.5%; Double Chance 1X: 88.9%; Double Chance X2: 25.4%; Double Chance 12 (either team wins): 85.6%; Under 4.5 goals: 66.8%; BTTS Yes (both teams score): 52.5%; BTTS No (at least one team does not score): 47.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 74.6% | 1.34 |
| Draw | 14.4% | 6.97 |
| Sabah FK win | 11.1% | 9.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 3.85 |
| Sabah FK expected goals | 0.91 |
| Expected total goals | 4.76 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 52.5% |
| Under 3.5 | 47.5% |
| Over 4.5 | 33.2% |
| Under 4.5 | 66.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 9.32% |
| 2 | 2-0 | 8.79% |
| 3 | 4-0 | 7.40% |
| 4 | 3-1 | 6.97% |
| 5 | 2-1 | 6.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 74.6% | 68.9% | 1.45 | +8.1% |
| Draw | 14.4% | 17.3% | 5.49 | -21.2% |
| Sabah FK win | 11.1% | 13.8% | 6.98 | -22.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T20:00:00+00:00 |
| Fixture id | 6277e639c064e641265fcb98a0e200b9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-03T13:57:38Z |
| Market best draw last update utc | 2026-11-03T13:57:38Z |
| Market best away last update utc | 2026-11-03T13:57:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Viking FK |
| Matched away-team name | Sabah FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.8518 |
| Dc lambda away | 0.9066 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:57:37.532944+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 52.5% |
| P btts no | 47.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.46 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.65 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.58 |
| Fair Over 3.5 odds | 1.90 |
| Fair Under 3.5 odds | 2.11 |
| Fair Over 4.5 odds | 3.01 |
| Fair Under 4.5 odds | 1.50 |
| Goal margin distribution | {"-1": 0.08314819715003723, "-10": 7.134853893870433e-10, "-11": 4.7686071944923006e-11, "-12": 2.9292938872370375e-12, "-13": 1.6645004927801286e-13, "-14": 8.797374322104233e-15, "-15": 4.3456701013178294e-16, "-16": 2.0147700693592398e-17, "-17": 8.799835428315113e-19, "-18": 3.631990769077833e-20, "-19": 1.4130119236901074e-21, "-2": 0.022012339674355036, "-20": 4.7244835231504944e-23, "-3": 0.004658713455830274, "-4": 0.0007846661488987544, "-5": 0.00010921153306260994, "-6": 1.29168101596028e-05, "-7": 1.3261276583798045e-06, "-8": 1.2016325195176306e-07, "-9": 9.738102192581742e-09, "0": 0.1435204261709183, "1": 0.1550874840609029, "10": 0.0006261472373266374, "11": 0.000177795403497404, "12": 4.640123283859448e-05, "13": 1.1201807290941036e-05, "14": 2.5153292150249837e-06, "15": 5.278810995629109e-07, "16": 1.0397823566519935e-07, "17": 1.9294303174653738e-08, "18": 3.3832717236442e-09, "19": 5.592108181951436e-10, "2": 0.18199390012570366, "20": 7.943678727040923e-11, "3": 0.16364178949201919, "4": 0.1170983385170633, "5": 0.06924236838254605, "6": 0.03479335290703653, "7": 0.015176231167871687, "8": 0.005842353997506219, "9": 0.002011537427073403} |
| Raw goal margin distribution | {"-1": 0.03351410977870573, "-10": 1.2135276060040046e-09, "-11": 9.749532996329918e-11, "-12": 7.2075954032595495e-12, "-13": 4.933454327761994e-13, "-14": 3.143311379503406e-14, "-15": 1.8729527302048827e-15, "-16": 1.0479831853959534e-16, "-17": 5.526530309022177e-18, "-18": 2.755710125407227e-19, "-19": 1.3030322015132225e-20, "-2": 0.009905998310480621, "-20": 5.855148813193175e-22, "-21": 2.4833282125571307e-23, "-22": 8.831903207653581e-25, "-3": 0.0023922679748875466, "-4": 0.00046840224492404706, "-5": 7.665864374441605e-05, "-6": 1.0740578433015453e-05, "-7": 1.3128777721523562e-06, "-8": 1.4214143631723035e-07, "-9": 1.3799365511186406e-08, "0": 0.07440354173309441, "1": 0.13751915662762693, "10": 0.002325014192897746, "11": 0.000793592137216838, "12": 0.00024925365603759177, "13": 7.248361491399498e-05, "14": 1.962066541669981e-05, "15": 4.966960871504766e-06, "16": 1.1807442283832605e-06, "17": 2.6454019403755164e-07, "18": 5.604156288600529e-08, "19": 1.1258212704916041e-08, "2": 0.17880243923529038, "20": 2.1492643421460084e-09, "21": 3.872787013181452e-10, "22": 5.851691018595862e-11, "3": 0.18345206760029364, "4": 0.15260520515444884, "5": 0.10610823862333653, "6": 0.06316161697711657, "7": 0.03280102831637996, "8": 0.015087645037910533, "9": 0.006222966619383301} |
| Unadjusted home-win probability | 87.9% |
| Unadjusted draw probability | 7.4% |
| Unadjusted away-win probability | 4.6% |
| Raw p over 1 5 | 94.9% |
| Raw p under 3 5 | 30.1% |
| Raw p btts yes | 58.2% |
| P home draw | 88.9% |
| P draw away | 25.4% |
| P home away | 85.6% |
| Raw p home draw | 95.4% |
| Raw p draw away | 12.1% |
| Raw p home away | 92.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8253 |
| Totals anchor target over 2 5 | 0.7208 |
| Totals anchor reference over odds | 1.35 |
| Totals anchor reference under odds | 3.22 |
| Totals anchor reference last update utc | 2026-11-03T13:57:37Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8176 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.42, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.34, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:35Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.44, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:35Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.17, "price": 5.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.72, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:50:52Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.35, "under": 3.17}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:35Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.01, "home_away": 1.18, "home_draw": 1.14}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.66, "draw": 5.37, "home": 1.43}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:37Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.35, "under": 3.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.98, "draw": 5.49, "home": 1.45}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:57:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.98, "home_away": 1.19, "home_draw": 1.13}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.43 |
| Reference draw odds | 5.37 |
| Reference away odds | 6.66 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:37Z |
| Market reference home last update utc | 2026-11-03T13:57:37Z |
| Market reference draw last update utc | 2026-11-03T13:57:37Z |
| Market reference away last update utc | 2026-11-03T13:57:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.21 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:56Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:56Z |
| Home probability edge | +5.7% |
| Draw probability edge | -3.0% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.1907 |
| Raw ev home | 0.2749 |
| Raw edge prob draw | -0.0987 |
| Raw ev draw | -0.5915 |
| Raw edge prob away | -0.0919 |
| Raw ev away | -0.6763 |
| Market p home draw | 85.9% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:35Z |
| Market reference home draw last update utc | 2026-11-03T13:57:38Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 32.6% |
| Market draw away odds | 3.01 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:57:35Z |
| Market reference draw away last update utc | 2026-11-03T13:57:38Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.6% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:57:38Z |
| Market reference home away last update utc | 2026-11-03T13:57:38Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.13 |
| Market reference dc draw away odds | 2.98 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 88.2% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:50:52Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.90 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:50:52Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:39Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,427.8588 |
| Elo away rating | 1,421.2723 |
| Elo rating diff | 66.5865 |
| Elo home expectancy | 0.5947 |

</details>


---
