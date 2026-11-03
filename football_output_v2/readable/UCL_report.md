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
| Training as of utc | 2026-11-03T13:22:17.761945+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 42, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 52, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-03T13:22:17.761945+00:00', 'observations': 374, 'observations_sha256': '4ab292c318d16afacb99c2ad5969866fad1f388eaf1d9178bac3caf4e828ecf9', 'eligible_training_matches': 14, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 94, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 14, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': '496d0fec6c65cf75a381038f7e09e49fa52bf8862cd08e37d45ab19b62b2f869', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 809.740 |
| Base scoring parameter | 0.213 |
| Home-advantage parameter | 0.300 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 71, 'matches': 557, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-21'} |
| Training data health | {'completed_matches': 54, 'latest_completed_utc': '2026-10-21T19:00:00+00:00', 'latest_completed_date': '2026-10-21', 'next_fixture_utc': '2026-11-03T17:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-11-03T13:22:17.761945+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '1d99ce3362b1915aff584e4ae4678057ee29bc6190f9a1d419b1135011f76902', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0, 'training_end': '2026-10-21', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261103T132217761945Z_06dc4d82820cf037264df643206a1c8df28bd24d65b3bdbaa39eb4b47a061d8d.json |
| Over 1 5 in window quote fixtures | 15 |
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
| Atlético Madrid win | 34.5% | 2.90 |
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
| Bayern Munich win | 41.8% | 41.2% | 2.42 | +1.3% |

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
| Market best home last update utc | 2026-11-03T13:22:17Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8531 |
| Dc lambda away | 2.0331 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Goal margin distribution | {"-1": 0.20253637447280065, "-10": 3.0368299196066214e-06, "-11": 4.67438977246615e-07, "-12": 6.615328651967997e-08, "-13": 8.662423785761169e-09, "-14": 1.054620146054328e-09, "-15": 1.1873962094680593e-10, "-16": 1.0957148771910049e-11, "-2": 0.12390222513773501, "-3": 0.05938380658767598, "-4": 0.022790129910020277, "-5": 0.00725438502014933, "-6": 0.001966925910291771, "-7": 0.00046367306427397384, "-8": 9.657797616838344e-05, "-9": 1.8005842770709832e-05, "0": 0.23618835124061996, "1": 0.18020591725644733, "10": 1.170594127358614e-06, "11": 1.6423318583494856e-07, "12": 2.1185442639371917e-08, "13": 2.5285739941611803e-09, "14": 2.8059661438878545e-10, "15": 2.8795998650775688e-11, "16": 2.4220559303869305e-12, "2": 0.10024529391501051, "3": 0.04379283326825853, "4": 0.01531905355286472, "5": 0.004444632506694138, "6": 0.0010984325170114747, "7": 0.0002360192196384528, "8": 4.4808842548435726e-05, "9": 7.614636951582858e-06} |
| Raw goal margin distribution | {"-1": 0.1923648853846631, "-10": 9.564867130956598e-06, "-11": 1.7198539611019948e-06, "-12": 2.8464203840154875e-07, "-13": 4.3627133221554554e-08, "-14": 6.224912358255956e-09, "-15": 8.296564346863697e-10, "-16": 1.0208314090168538e-10, "-17": 9.99353839745207e-12, "-2": 0.1281733348951539, "-3": 0.06846955364470901, "-4": 0.029774071969274972, "-5": 0.010849836978069013, "-6": 0.0033905514136092314, "-7": 0.0009254579374840841, "-8": 0.00022392698191022584, "-9": 4.861448403215161e-05, "0": 0.2018129912262662, "1": 0.1756801598176188, "10": 3.7859961782480127e-06, "11": 6.205016257814755e-07, "12": 9.360531661244538e-08, "13": 1.3077004546840092e-08, "14": 1.700728396222057e-09, "15": 2.0660942569434298e-10, "16": 2.3171598332123182e-11, "17": 2.0676231023924614e-12, "2": 0.1064873280962338, "3": 0.05184989313523261, "4": 0.020551272873172943, "5": 0.006826118569914473, "6": 0.0019443349023603753, "7": 0.0004837350380450439, "8": 0.00010668599464132273, "9": 2.1111387997403962e-05} |
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
| Totals anchor scale | 0.8497 |
| Totals anchor target over 2 5 | 0.6363 |
| Totals anchor reference over odds | 1.53 |
| Totals anchor reference under odds | 2.59 |
| Totals anchor reference last update utc | 2026-11-03T13:22:17Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7365 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 4.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.47, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.17, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.46, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.42, "draw": 3.96, "home": 2.86}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.48, "home_away": 1.29, "home_draw": 1.63}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.38, "draw": 3.86, "home": 2.89}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.53, "under": 2.59}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.47, "home_away": 1.29, "home_draw": 1.65}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:22Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.47, "under": 2.67}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.89 |
| Reference draw odds | 3.86 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.57 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | +0.8% |
| Draw probability edge | -1.5% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0265 |
| Raw ev home | 0.0518 |
| Raw edge prob draw | -0.0491 |
| Raw ev draw | -0.2008 |
| Raw edge prob away | 0.0226 |
| Raw ev away | 0.0508 |
| Market p home draw | 58.8% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:22:17Z |
| Market reference home draw last update utc | 2026-11-03T13:22:17Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 66.0% |
| Market draw away odds | 1.48 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:21:54Z |
| Market reference draw away last update utc | 2026-11-03T13:22:17Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:17Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.65 |
| Market reference dc draw away odds | 1.47 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 87.2% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:22:22Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.46 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:22Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.0% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:22:22Z |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:22Z |
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
| Aston Villa win | 19.1% | 10.3% | 8.63 | +64.7% |

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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:22:17Z |
| Market best away last update utc | 2026-11-03T13:22:17Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FC Barcelona |
| Matched away-team name | Aston Villa FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8945 |
| Dc lambda away | 1.8869 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Fair Under 0.5 odds | 73.13 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.74 |
| Fair Over 2.5 odds | 1.35 |
| Fair Under 2.5 odds | 3.87 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.09 |
| Fair Over 4.5 odds | 2.95 |
| Fair Under 4.5 odds | 1.51 |
| Goal margin distribution | {"-1": 0.08972854674848173, "-10": 2.387232033632945e-06, "-11": 3.989332501937475e-07, "-12": 6.134979915824786e-08, "-13": 8.735187713413869e-09, "-14": 1.156216082045569e-09, "-15": 1.4067133804208434e-10, "-16": 1.3560007251784042e-11, "-2": 0.05616991585059596, "-3": 0.028115089966652712, "-4": 0.011423668726554608, "-5": 0.0038827808287325606, "-6": 0.0011303900870776107, "-7": 0.00028720898009172946, "-8": 6.465131593643537e-05, "-9": 1.3052073012183869e-05, "0": 0.15000844233155383, "1": 0.3088354647745342, "10": 8.520470039997216e-06, "11": 1.4296094169777412e-06, "12": 2.2073873786900488e-07, "13": 3.155628695308637e-08, "14": 4.193734235960606e-09, "15": 5.122898631510653e-10, "16": 4.9581345778002017e-11, "2": 0.19412735411841997, "3": 0.0975597512681127, "4": 0.039800181461476486, "5": 0.013582214128246178, "6": 0.003970125920045498, "7": 0.0010127965205276395, "8": 0.0002289021119874486, "9": 4.6398097155258724e-05} |
| Raw goal margin distribution | {"-1": 0.18613162176122022, "-10": 4.9520401928046875e-06, "-11": 8.275414628209531e-07, "-12": 1.2726315120269166e-07, "-13": 1.8120149210083127e-08, "-14": 2.3984382034047293e-09, "-15": 2.9180662379932093e-10, "-16": 2.8128686269079438e-11, "-2": 0.11651807490841373, "-3": 0.05832154293242499, "-4": 0.02369709600331314, "-5": 0.008054385352090805, "-6": 0.002344865126594985, "-7": 0.0005957822252344033, "-8": 0.00013411177067179406, "-9": 2.7075034703431715e-05, "0": 0.2053258271338106, "1": 0.18686597066838653, "10": 5.1554503487394605e-06, "11": 8.650086594661064e-07, "12": 1.3356159904148216e-07, "13": 1.9093649741565758e-08, "14": 2.5374877826940625e-09, "15": 3.0996939619996756e-10, "16": 3.000000765007747e-11, "2": 0.1174599442039707, "3": 0.059030129950235835, "4": 0.024081753522077972, "5": 0.008218141749858635, "6": 0.0024021898983221848, "7": 0.0006128091702037178, "8": 0.000138500982637488, "9": 2.8073930785161725e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.95, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 7.33, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.12, "price": 7.33, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 8.6, "draw": 7.01, "home": 1.32}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.72, "home_away": 1.13, "home_draw": 1.09}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:04Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.17, "under": 4.68}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 8.63, "draw": 7.11, "home": 1.28}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 4.01, "home_away": 1.12, "home_draw": 1.1}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.28 |
| Reference draw odds | 7.11 |
| Reference away odds | 8.63 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.18 |
| Reference Under 2.5 odds | 5.07 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | -11.2% |
| Draw probability edge | +2.4% |
| Away probability edge | +8.8% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | -0.3719 |
| Raw ev home | -0.4735 |
| Raw edge prob draw | 0.0790 |
| Raw ev draw | 0.4599 |
| Raw edge prob away | 0.2929 |
| Raw ev away | 2.4160 |
| Market p home draw | 88.6% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:22:17Z |
| Market reference home draw last update utc | 2026-11-03T13:22:17Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 24.3% |
| Market draw away odds | 4.01 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:22:17Z |
| Market reference draw away last update utc | 2026-11-03T13:22:17Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.1% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:17Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.10 |
| Market reference dc draw away odds | 4.01 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 94.6% |
| Market over 1 5 odds | 1.02 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:22:04Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 8.00 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 34.3% |
| Market under 3 5 odds | 2.66 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:22:17Z |
| Market reference under 3 5 odds | 2.66 |
| Market reference under 3 5 opposite odds | 1.47 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:17Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,563.5732 |
| Elo away rating | 1,514.0790 |
| Elo rating diff | 109.4942 |
| Elo home expectancy | 0.6526 |

</details>


---

## 2026-11-03 — Bodø/Glimt vs Lille

The model's most likely 1X2 outcome is **Bodø/Glimt win** at **58.4%**. Expected goals are 2.82 for Bodø/Glimt and 1.81 for Lille (4.63 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 65.5%; Under 3.5 goals: 56.2%; Double Chance 1X: 78.9%; Double Chance X2: 41.6%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

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
| Over 3.5 | 43.8% |
| Under 3.5 | 56.2% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.15% |
| 2 | 1-1 | 8.92% |
| 3 | 1-0 | 8.02% |
| 4 | 2-0 | 7.72% |
| 5 | 3-1 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 58.4% | 57.9% | 1.79 | +4.5% |
| Draw | 20.5% | 22.1% | 4.34 | -11.0% |
| Lille win | 21.1% | 20.0% | 4.79 | +1.2% |

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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:22:17Z |
| Market best away last update utc | 2026-11-03T13:22:17Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8231 |
| Dc lambda away | 1.8090 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Fair Under 0.5 odds | 33.23 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.54 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.98 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.12455531433325524, "-10": 1.5988406016635985e-07, "-11": 1.8734806402505517e-08, "-12": 2.018393321930114e-09, "-13": 2.0120049563664945e-10, "-14": 1.8658854684525365e-11, "-15": 1.6166675788810355e-12, "-16": 1.302363754540773e-13, "-17": 8.693334833057192e-15, "-2": 0.057663677486222246, "-3": 0.021061460295816868, "-4": 0.0061574221211269054, "-5": 0.001492738342841146, "-6": 0.00030820325519513575, "-7": 5.532016107883256e-05, "-8": 8.772860565565092e-06, "-9": 1.2452190142716273e-06, "0": 0.20512675775532457, "1": 0.23904827525346808, "10": 1.704694243466502e-05, "11": 3.117393750524829e-06, "12": 5.241425002039903e-07, "13": 8.154057059889282e-08, "14": 1.180132598643381e-08, "15": 1.5957603800463375e-09, "16": 2.0062284040032681e-10, "17": 2.0899486017202424e-11, "2": 0.17471679943468688, "3": 0.09959142207865537, "4": 0.04543949606150958, "5": 0.01719172246941811, "6": 0.005539544419985724, "7": 0.0015517486936098492, "8": 0.00038404339815443724, "9": 8.507186333177804e-05} |
| Raw goal margin distribution | {"-1": 0.12457980549775724, "-10": 1.587609651804451e-06, "-11": 2.5164883459324595e-07, "-12": 3.676385080601948e-08, "-13": 4.9792573770928456e-09, "-14": 6.284081007507394e-10, "-15": 7.423265814882412e-11, "-16": 8.239070000485715e-12, "-17": 8.604465670892019e-13, "-18": 8.30018368237068e-14, "-19": 6.22838258370226e-15, "-2": 0.06769878483078577, "-3": 0.030273571378113033, "-4": 0.011208786250109088, "-5": 0.003516881518349673, "-6": 0.0009535045145399168, "-7": 0.00022701039380323762, "-8": 4.80959711187393e-05, "-9": 9.169086656798851e-06, "0": 0.16817578398055333, "1": 0.19302997116740364, "10": 0.00013606767888502136, "11": 3.365947160136748e-05, "12": 7.674224328283703e-06, "13": 1.6221058671987102e-06, "14": 3.194901837532019e-07, "15": 5.889953702415831e-08, "16": 1.020225527877305e-08, "17": 1.662811518547573e-09, "18": 2.5032714487529e-10, "19": 2.93154556523444e-11, "2": 0.16488574942196166, "3": 0.11507130319158701, "4": 0.06649103384243393, "5": 0.03255842293680983, "6": 0.013776201967467008, "7": 0.0051186285442553735, "8": 0.0016924572003008545, "9": 0.000503542577457837} |
| Unadjusted home-win probability | 59.3% |
| Unadjusted draw probability | 16.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 94.3% |
| Raw p under 3 5 | 32.1% |
| Raw p btts yes | 78.4% |
| P home draw | 78.9% |
| P draw away | 41.6% |
| P home away | 79.5% |
| Raw p home draw | 76.1% |
| Raw p draw away | 40.7% |
| Raw p home away | 83.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7269 |
| Totals anchor target over 2 5 | 0.6552 |
| Totals anchor reference over odds | 1.49 |
| Totals anchor reference under odds | 2.73 |
| Totals anchor reference last update utc | 2026-11-03T13:22:17Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8340 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.97, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.45, "draw": 4.32, "home": 1.79}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.14, "home_away": 1.26, "home_draw": 1.25}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:21:58Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.28, "home_away": 1.25, "home_draw": 1.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.79, "draw": 4.34, "home": 1.7}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.49, "under": 2.73}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.70 |
| Reference draw odds | 4.34 |
| Reference away odds | 4.79 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | +0.4% |
| Draw probability edge | -1.6% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0139 |
| Raw ev home | 0.0620 |
| Raw edge prob draw | -0.0528 |
| Raw ev draw | -0.2701 |
| Raw edge prob away | 0.0389 |
| Raw ev away | 0.1425 |
| Market p home draw | 79.3% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:21:54Z |
| Market reference home draw last update utc | 2026-11-03T13:22:15Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.9% |
| Market draw away odds | 2.28 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:21:58Z |
| Market reference draw away last update utc | 2026-11-03T13:22:15Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:15Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.17 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 86.0% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.5% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:22:17Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.21 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:17Z |
| Market under 3 5 bookmakers | 1 |
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
| Market best home last update utc | 2026-11-03T13:22:17Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | FC Internazionale Milano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3781 |
| Dc lambda away | 1.5826 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Goal margin distribution | {"-1": 0.22303237972935233, "-10": 6.3219869635903405e-06, "-11": 1.052135797839076e-06, "-12": 1.610509392084197e-07, "-13": 2.2815487929687947e-08, "-14": 3.0050939863681967e-09, "-15": 3.652234764555891e-10, "-16": 3.588959920205458e-11, "-2": 0.14413442703559173, "-3": 0.07353418765376671, "-4": 0.030208361622488952, "-5": 0.010328337849821154, "-6": 0.0030146195922734777, "-7": 0.000766171127059645, "-8": 0.00017223572030145002, "-9": 3.468378044081882e-05, "0": 0.23669009402758834, "1": 0.1437656024509804, "10": 1.1687907116615785e-06, "11": 1.693749179603666e-07, "12": 2.257536118577274e-08, "13": 2.7848085997399344e-09, "14": 3.1938741159743953e-10, "15": 3.3799678269641807e-11, "16": 2.892122163002592e-12, "2": 0.08063019726073016, "3": 0.03581899861865208, "4": 0.012812841614876702, "5": 0.003814546090053735, "6": 0.0009694805337956493, "7": 0.00021454900391553418, "8": 4.199698290247436e-05, "9": 7.364028134587592e-06} |
| Raw goal margin distribution | {"-1": 0.21604899560936727, "-10": 1.7126255498019225e-06, "-11": 2.4245611688550636e-07, "-12": 3.154053950139251e-08, "-13": 3.793147403235772e-09, "-14": 4.20824548373806e-10, "-15": 3.87646907568963e-11, "-2": 0.1268988312873058, "-3": 0.05746726839056472, "-4": 0.020633239481347935, "-5": 0.006108128424493905, "-6": 0.0015343947809939066, "-7": 0.0003342708041758455, "-8": 6.422872594290469e-05, "-9": 1.1032376675941264e-05, "0": 0.2321468703970517, "1": 0.18885478537789907, "10": 4.291448133461609e-07, "11": 5.2901591729668484e-08, "12": 5.992373251485458e-09, "13": 6.275142664734884e-10, "14": 6.062044149103394e-11, "15": 4.862375535376265e-12, "2": 0.09621569299046294, "3": 0.03794049467014781, "4": 0.011861619774893842, "5": 0.003057587429495455, "6": 0.0006688088052293771, "7": 0.00012686956787712601, "8": 2.1226699252983254e-05, "9": 3.1748001032592142e-06} |
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
| Totals anchor reference last update utc | 2026-11-03T13:22:17Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5676 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.62, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.83, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.01, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.15, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.76, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.53, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 6.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:20Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.41, "under": 2.89}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.97, "draw": 4.26, "home": 3.65}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.33, "home_away": 1.26, "home_draw": 1.93}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:21:58Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.3, "home_away": 1.28, "home_draw": 1.96}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.93, "draw": 4.04, "home": 3.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.45, "under": 2.87}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.83 |
| Reference draw odds | 4.04 |
| Reference away odds | 1.93 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | +2.6% |
| Draw probability edge | -0.2% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0867 |
| Raw ev home | 0.2974 |
| Raw edge prob draw | -0.0065 |
| Raw ev draw | -0.0111 |
| Raw edge prob away | -0.0802 |
| Raw ev away | -0.1547 |
| Market p home draw | 49.9% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:21:58Z |
| Market reference home draw last update utc | 2026-11-03T13:22:15Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.5% |
| Market draw away odds | 1.33 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:21:54Z |
| Market reference draw away last update utc | 2026-11-03T13:22:15Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.6% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-03T13:21:58Z |
| Market reference home away last update utc | 2026-11-03T13:22:15Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.91 |
| Market reference dc draw away odds | 1.28 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:10:20Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.2% |
| Market under 3 5 odds | 1.87 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:10:20Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:17Z |
| Market under 3 5 bookmakers | 2 |
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
| 3 | 1-0 | 8.63% |
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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:22:17Z |
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
| Dc lambda away | 1.4341 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Goal margin distribution | {"-1": 0.1706694694768578, "-10": 5.275117192184508e-07, "-11": 6.758148244479756e-08, "-12": 7.957366027232641e-09, "-13": 8.66218073256887e-10, "-14": 8.689096303989283e-11, "-15": 7.177955779878611e-12, "-2": 0.08906163060615238, "-3": 0.0361652895850148, "-4": 0.011683154507774199, "-5": 0.003118186498793418, "-6": 0.0007071140660343157, "-7": 0.00013918148459907115, "-8": 2.4177015904303183e-05, "-9": 3.7559574304239583e-06, "0": 0.22802709611560829, "1": 0.22710169715503012, "10": 2.429836833043793e-06, "11": 3.572005170326729e-07, "12": 4.8260638811357344e-08, "13": 6.028237269820866e-09, "14": 6.938683427403122e-10, "15": 6.577223615337531e-11, "2": 0.1364962476670621, "3": 0.06360062498723525, "4": 0.023575934847348722, "5": 0.007220217083492039, "6": 0.0018787846831784963, "7": 0.0004243345217368274, "8": 8.458024967340652e-05, "9": 1.5077394352682069e-05} |
| Raw goal margin distribution | {"-1": 0.18653940011201361, "-10": 5.765631073717593e-07, "-11": 7.386563767131487e-08, "-12": 8.697292431631822e-09, "-13": 9.467645282241541e-10, "-14": 9.497063634345322e-11, "-15": 7.845407671995352e-12, "-2": 0.09734314635882865, "-3": 0.03952816777801423, "-4": 0.012769528375382228, "-5": 0.0034081352728478243, "-6": 0.0007728660204612274, "-7": 0.00015212346252315893, "-8": 2.6425148312181653e-05, "-9": 4.105210194097128e-06, "0": 0.22714170544676923, "1": 0.2132474166943941, "10": 2.281605263750007e-06, "11": 3.354095916206247e-07, "12": 4.531651098810479e-08, "13": 5.660486209984688e-09, "14": 6.515390834546863e-10, "15": 6.17598178508824e-11, "2": 0.12816932928338753, "3": 0.05972068526382849, "4": 0.022137691022715927, "5": 0.006779749602559528, "6": 0.0017641699081592977, "7": 0.0003984481036830747, "8": 7.942045335710657e-05, "9": 1.415760179897398e-05} |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 34.1% |
| Raw p over 1 5 | 80.7% |
| Raw p under 3 5 | 62.9% |
| Raw p btts yes | 60.9% |
| P home draw | 68.8% |
| P draw away | 54.0% |
| P home away | 77.2% |
| Raw p home draw | 65.9% |
| Raw p draw away | 56.8% |
| Raw p home away | 77.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5946 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.23, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.57, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.62, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.94, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.95, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.31, "under": 3.42}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.17, "draw": 4.32, "home": 2.13}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.79, "home_away": 1.26, "home_draw": 1.41}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:21:59Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.83, "home_away": 1.26, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.25, "draw": 4.23, "home": 2.08}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 4.23 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.46 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | -1.2% |
| Draw probability edge | -0.0% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -14.5% |
| Under 2.5 probability edge | +14.5% |
| Raw edge prob home | -0.0401 |
| Raw ev home | -0.0792 |
| Raw edge prob draw | -0.0013 |
| Raw ev draw | -0.0187 |
| Raw edge prob away | 0.0414 |
| Raw ev away | 0.1068 |
| Market p home draw | 69.5% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:21:54Z |
| Market reference home draw last update utc | 2026-11-03T13:22:15Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.8% |
| Market draw away odds | 1.83 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:21:59Z |
| Market reference draw away last update utc | 2026-11-03T13:22:15Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:15Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.37 |
| Market reference dc draw away odds | 1.77 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 91.3% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:16:13Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.20 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 46.7% |
| Market under 3 5 odds | 2.10 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:16:13Z |
| Market reference under 3 5 odds | 2.06 |
| Market reference under 3 5 opposite odds | 1.82 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:17Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,464.0831 |
| Elo away rating | 1,479.0805 |
| Elo rating diff | 45.0026 |
| Elo home expectancy | 0.5644 |

</details>


---

## 2026-11-03 — LASK vs ŠK Slovan Bratislava

The model's most likely 1X2 outcome is **LASK win** at **78.5%**. Expected goals are 5.26 for LASK and 1.09 for ŠK Slovan Bratislava (6.35 combined). The most likely exact score is 3-0 at 10.2%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 72.9%; Under 3.5 goals: 46.7%; Double Chance 1X: 90.7%; Double Chance X2: 21.5%; Double Chance 12 (either team wins): 87.7%; Under 4.5 goals: 65.9%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 78.5% | 1.27 |
| Draw | 12.3% | 8.16 |
| ŠK Slovan Bratislava win | 9.3% | 10.78 |

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
| Over 4.5 | 34.1% |
| Under 4.5 | 65.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.17% |
| 2 | 2-0 | 9.33% |
| 3 | 4-0 | 8.32% |
| 4 | 3-1 | 6.92% |
| 5 | 2-1 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 78.5% | 71.9% | 1.43 | +12.2% |
| Draw | 12.3% | 15.9% | 5.79 | -29.0% |
| ŠK Slovan Bratislava win | 9.3% | 12.2% | 7.41 | -31.3% |

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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:22:17Z |
| Market best away last update utc | 2026-11-03T13:22:17Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | LASK Linz |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.2604 |
| Dc lambda away | 1.0940 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 26 |
| Score grid omitted mass | 0 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.21 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.88 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.69 |
| Fair Over 3.5 odds | 1.88 |
| Fair Under 3.5 odds | 2.14 |
| Fair Over 4.5 odds | 2.93 |
| Fair Under 4.5 odds | 1.52 |
| Goal margin distribution | {"-1": 0.0714416759927393, "-10": 2.7169171579879147e-10, "-11": 1.6535969706129387e-11, "-12": 9.248631424470491e-13, "-13": 4.784305618414693e-14, "-14": 2.301777507302624e-15, "-15": 1.0349165406242076e-16, "-16": 4.3669861448119065e-18, "-17": 1.7358664526802123e-19, "-18": 6.521562048711312e-21, "-19": 2.3222508331011413e-22, "-2": 0.017362156380921277, "-20": 7.82371118776205e-24, "-21": 2.292575945664046e-25, "-3": 0.003372119673495015, "-4": 0.0005197289930394365, "-5": 6.60808644064088e-05, "-6": 7.131954561334341e-06, "-7": 6.676841637536368e-07, "-8": 5.514052595737867e-08, "-9": 4.0712580449996536e-09, "0": 0.12261315262224289, "1": 0.15087441853931044, "10": 0.0008268071038365782, "11": 0.00024196191237303886, "12": 6.50705309047045e-05, "13": 1.6185097857207243e-05, "14": 3.744115991140193e-06, "15": 8.094328358959946e-07, "16": 1.642278629486589e-07, "17": 3.138852262197666e-08, "18": 5.670165472417669e-09, "19": 9.70829058947236e-10, "2": 0.1849333202734439, "20": 1.572664151927732e-10, "21": 2.2158300414013776e-11, "3": 0.17270464557877682, "4": 0.127987490235794, "5": 0.0782448623925624, "6": 0.04060487900664515, "7": 0.018278067056708196, "8": 0.0072580445961925, "9": 0.002576718023406925} |
| Raw goal margin distribution | {"-1": 0.016532066644137134, "-10": 1.964874857910786e-09, "-11": 1.8752659909207612e-10, "-12": 1.6505821131957177e-11, "-13": 1.347558618928345e-12, "-14": 1.0255828251965887e-13, "-15": 7.308396377704417e-15, "-16": 4.895525507055027e-16, "-17": 3.0932560354214847e-17, "-18": 1.84939044189594e-18, "-19": 1.0492048023616114e-19, "-2": 0.005181200471557487, "-20": 5.662626692740136e-21, "-21": 2.9141256092279834e-22, "-22": 1.4330086005279594e-23, "-23": 6.746036080904795e-25, "-24": 3.041822921817775e-26, "-25": 1.2947369172505486e-27, "-26": 4.4606332748749743e-29, "-3": 0.0013642763207749246, "-4": 0.00029950869262280387, "-5": 5.598763409963132e-05, "-6": 9.073770989281872e-06, "-7": 1.294426781055888e-06, "-8": 1.646141909931539e-07, "-9": 1.8861758808054843e-08, "0": 0.03856564916469224, "1": 0.07758502524481965, "10": 0.012978672386670356, "11": 0.005955905375899255, "12": 0.002520644410732145, "13": 0.000989490554351725, "14": 0.0003620964470667834, "15": 0.00012406953519968436, "16": 3.996059229401092e-05, "17": 1.2140540033947616e-05, "18": 3.4901193824638577e-06, "19": 9.520537786201367e-07, "2": 0.11978694011178817, "20": 2.4706355178818587e-07, "21": 6.113480814858971e-08, "22": 1.4455017458256908e-08, "23": 3.271960263458857e-09, "24": 7.093863486500165e-10, "25": 1.4518440439846773e-10, "26": 2.405052123797453e-11, "3": 0.1516599657680215, "4": 0.16009124466683045, "5": 0.1438930449379414, "6": 0.11213083046318847, "7": 0.07691379701386582, "8": 0.04703093051985781, "9": 0.02591122968234932} |
| Unadjusted home-win probability | 93.8% |
| Unadjusted draw probability | 3.9% |
| Unadjusted away-win probability | 2.3% |
| Raw p over 1 5 | 98.7% |
| Raw p under 3 5 | 12.2% |
| Raw p btts yes | 66.1% |
| P home draw | 90.7% |
| P draw away | 21.5% |
| P home away | 87.7% |
| Raw p home draw | 97.7% |
| Raw p draw away | 6.2% |
| Raw p home away | 96.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.6221 |
| Totals anchor target over 2 5 | 0.7290 |
| Totals anchor reference over odds | 1.34 |
| Totals anchor reference under odds | 3.35 |
| Totals anchor reference last update utc | 2026-11-03T13:22:17Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.9240 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 5.33, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.64, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.15, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.15, "price": 6.15, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:57Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.34, "under": 3.23}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.4, "draw": 5.55, "home": 1.43}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.07, "home_away": 1.18, "home_draw": 1.11}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.41, "draw": 5.79, "home": 1.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.34, "under": 3.35}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.32, "home_away": 1.17, "home_draw": 1.12}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.37 |
| Reference draw odds | 5.79 |
| Reference away odds | 7.41 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | +6.6% |
| Draw probability edge | -3.6% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.2191 |
| Raw ev home | 0.3413 |
| Raw edge prob draw | -0.1201 |
| Raw ev draw | -0.7767 |
| Raw edge prob away | -0.0990 |
| Raw ev away | -0.8263 |
| Market p home draw | 87.2% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:22:35Z |
| Market reference home draw last update utc | 2026-11-03T13:22:35Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 29.4% |
| Market draw away odds | 3.32 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:22:35Z |
| Market reference draw away last update utc | 2026-11-03T13:22:35Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.4% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:35Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 3.32 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 90.4% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:10:57Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.7% |
| Market under 3 5 odds | 2.03 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:10:57Z |
| Market reference under 3 5 odds | 2.00 |
| Market reference under 3 5 opposite odds | 1.90 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:17Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,423.1110 |
| Elo away rating | 1,382.3668 |
| Elo rating diff | 100.7442 |
| Elo home expectancy | 0.6411 |

</details>


---

## 2026-11-03 — Manchester United vs AS Roma

The model's most likely 1X2 outcome is **Manchester United win** at **49.3%**. Expected goals are 2.49 for Manchester United and 1.45 for AS Roma (3.94 combined). The most likely exact score is 1-1 at 9.8%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 63.0%; Under 3.5 goals: 58.8%; Double Chance 1X: 71.3%; Double Chance X2: 50.7%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 77.0%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 49.3% | 2.03 |
| Draw | 22.0% | 4.55 |
| AS Roma win | 28.7% | 3.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 2.49 |
| AS Roma expected goals | 1.45 |
| Expected total goals | 3.94 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 63.0% |
| Under 2.5 | 37.0% |
| Over 3.5 | 41.2% |
| Under 3.5 | 58.8% |
| Over 4.5 | 23.0% |
| Under 4.5 | 77.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.76% |
| 2 | 2-1 | 8.28% |
| 3 | 1-2 | 7.36% |
| 4 | 1-0 | 6.93% |
| 5 | 2-0 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 49.3% | 44.4% | 2.23 | +9.9% |
| Draw | 22.0% | 23.8% | 4.12 | -9.5% |
| AS Roma win | 28.7% | 31.8% | 3.09 | -11.2% |

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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester United FC |
| Matched away-team name | AS Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4916 |
| Dc lambda away | 1.4458 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Fair Under 0.5 odds | 28.26 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.93 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.70 |
| Fair Over 3.5 odds | 2.43 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.34 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.17623909750061995, "-10": 1.1422759939665131e-07, "-11": 1.236231523066156e-08, "-12": 1.2298899616915717e-09, "-13": 1.1319828845020344e-10, "-14": 9.69170426255879e-12, "-15": 7.752427530000076e-13, "-16": 5.771069602286833e-14, "-17": 3.583314341161767e-15, "-2": 0.07614680835060895, "-3": 0.02589211340227325, "-4": 0.007026746571347297, "-5": 0.0015785441131251044, "-6": 0.00030167634408524035, "-7": 5.008302070329117e-05, "-8": 7.34211357064891e-06, "-9": 9.63010759987972e-07, "0": 0.21974067725578766, "1": 0.1954980686869207, "10": 1.7237460822614254e-05, "11": 3.2149444052633815e-06, "12": 5.51202681608368e-07, "13": 8.742916620199596e-08, "14": 1.2899950413033717e-08, "15": 1.778267183125953e-09, "16": 2.2813242777434146e-10, "17": 2.441108197166436e-11, "2": 0.14770073513835014, "3": 0.08655055633466884, "4": 0.04047884061453571, "5": 0.0156711875736846, "6": 0.005161285149729381, "7": 0.0014766532428435084, "8": 0.0003730615736374404, "9": 8.432609138057772e-05} |
| Raw goal margin distribution | {"-1": 0.12398449181541463, "-10": 2.9624154369510986e-07, "-11": 3.792451176839661e-08, "-12": 4.468025308985536e-09, "-13": 4.874214345945398e-10, "-14": 4.9499397097154073e-11, "-15": 4.701103927225916e-12, "-16": 4.18860145598045e-13, "-17": 3.466987663666404e-14, "-18": 2.3203662361571353e-15, "-2": 0.05895794561741082, "-3": 0.022580586808009655, "-4": 0.007023183030153289, "-5": 0.0018277447078000873, "-6": 0.00040749219275270623, "-7": 7.929728125751126e-05, "-8": 1.3672357565936125e-05, "-9": 2.114355806544906e-06, "0": 0.17790692523928153, "1": 0.21112717797498742, "10": 6.844789158432635e-05, "11": 1.5100993570357816e-05, "12": 3.066002890494713e-06, "13": 5.764119425992832e-07, "14": 1.0087874421194191e-07, "15": 1.6510910435669665e-08, "16": 2.5351964611702257e-09, "17": 3.6163152952456203e-10, "18": 4.1710168141201395e-11, "2": 0.17509960434422864, "3": 0.11557115610743156, "4": 0.06194690768571207, "5": 0.02778258114847911, "6": 0.010674505372103392, "7": 0.0035797951606963657, "8": 0.00106368907341147, "9": 0.0002834789231581829} |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 21.5% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 44.6% |
| Raw p btts yes | 69.8% |
| P home draw | 71.3% |
| P draw away | 50.7% |
| P home away | 78.0% |
| Raw p home draw | 78.5% |
| Raw p draw away | 39.3% |
| Raw p home away | 82.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8390 |
| Totals anchor target over 2 5 | 0.6301 |
| Totals anchor reference over odds | 1.55 |
| Totals anchor reference under odds | 2.57 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7368 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.72, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.09, "draw": 4.12, "home": 2.23}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.73, "home_away": 1.28, "home_draw": 1.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.06, "draw": 4.07, "home": 2.21}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.72, "home_away": 1.28, "home_draw": 1.43}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.55, "under": 2.57}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.21 |
| Reference draw odds | 4.07 |
| Reference away odds | 3.06 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.53 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | +4.9% |
| Draw probability edge | -1.8% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.1631 |
| Raw ev home | 0.3541 |
| Raw edge prob draw | -0.0598 |
| Raw ev draw | -0.2670 |
| Raw edge prob away | -0.1034 |
| Raw ev away | -0.3360 |
| Market p home draw | 67.8% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:22:17Z |
| Market reference home draw last update utc | 2026-11-03T13:22:17Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.4% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:21:54Z |
| Market reference draw away last update utc | 2026-11-03T13:22:17Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:17Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.43 |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 84.4% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 59.2% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market under 3 5 bookmakers | 1 |
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
| Draw | 25.4% | 3.94 |
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
| 1 | 1-1 | 11.70% |
| 2 | 1-2 | 9.27% |
| 3 | 0-1 | 8.92% |
| 4 | 0-2 | 7.03% |
| 5 | 2-2 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 28.1% | 27.2% | 3.63 | +2.0% |
| Draw | 25.4% | 25.3% | 3.87 | -1.7% |
| Sporting Lisbon win | 46.5% | 47.4% | 2.08 | -3.3% |
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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
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
| Dc lambda home | 1.0834 |
| Dc lambda away | 1.3791 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Fair Under 0.5 odds | 20.24 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.83 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.52 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.22329745801364426, "-10": 2.999503236741612e-06, "-11": 4.505989789405081e-07, "-12": 6.220317508810864e-08, "-13": 7.93842543594205e-09, "-14": 9.344004890295851e-10, "-15": 9.11692413281001e-11, "-2": 0.1389414455404749, "-3": 0.06664373873152295, "-4": 0.025361320910315416, "-5": 0.00796078936131276, "-6": 0.0021210013249136333, "-7": 0.0004901545370746055, "-8": 9.991871395006527e-05, "-9": 1.8209887678619325e-05, "0": 0.2541055473420149, "1": 0.16146095818170872, "10": 2.4548055989922554e-07, "11": 2.896992919995148e-08, "12": 3.141660445510379e-09, "13": 3.149709650228919e-10, "14": 2.9124512758671704e-11, "15": 2.2323557873600982e-12, "2": 0.07839419425814992, "3": 0.029539347728966363, "4": 0.008830857521970754, "5": 0.002177592447335458, "6": 0.00045577538735349, "7": 8.274321973912947e-05, "8": 1.3250604309960652e-05, "9": 1.8970797005472388e-06} |
| Raw goal margin distribution | {"-1": 0.2364994644739082, "-10": 6.688533937194719e-07, "-11": 8.292386025105579e-08, "-12": 9.438427945913211e-09, "-13": 9.884405996536133e-10, "-14": 8.797755071285901e-11, "-2": 0.12974172920005528, "-3": 0.05343115167341828, "-4": 0.017195742016208174, "-5": 0.004525020290306375, "-6": 0.001005205814886772, "-7": 0.00019298959708578464, "-8": 3.260261849833615e-05, "-9": 4.915181485194273e-06, "0": 0.2560645894608786, "1": 0.18715398237897968, "10": 5.987224431824998e-08, "11": 5.83127569001562e-09, "12": 5.214025950673041e-10, "13": 4.2895680258853845e-11, "14": 2.999330413613277e-12, "2": 0.08006793031498373, "3": 0.025903766469531717, "4": 0.006549056875473113, "5": 0.001353841530658073, "6": 0.0002362608456184542, "7": 3.5633634540593256e-05, "8": 4.728987483182421e-06, "9": 5.600730826920231e-07} |
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
| Totals anchor scale | 1.2181 |
| Totals anchor target over 2 5 | 0.5693 |
| Totals anchor reference over odds | 1.71 |
| Totals anchor reference under odds | 2.23 |
| Totals anchor reference last update utc | 2026-11-03T13:22:17Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4478 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.44, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.39, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.62, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.58, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.69, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.77, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:18:59Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.75, "under": 2.26}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.08, "draw": 3.87, "home": 3.63}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.75, "under": 2.26}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.33, "home_away": 1.3, "home_draw": 1.84}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:21:58Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.34, "home_away": 1.3, "home_draw": 1.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.07, "draw": 3.82, "home": 3.56}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.23}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.56 |
| Reference draw odds | 3.82 |
| Reference away odds | 2.07 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.26 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:54Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:54Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:54Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:54Z |
| Home probability edge | +0.9% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0291 |
| Raw ev home | 0.0937 |
| Raw edge prob draw | 0.0028 |
| Raw ev draw | -0.0090 |
| Raw edge prob away | -0.0319 |
| Raw ev away | -0.0793 |
| Market p home draw | 51.8% |
| Market home draw odds | 1.84 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:21:54Z |
| Market reference home draw last update utc | 2026-11-03T13:22:15Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.8% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:21:58Z |
| Market reference draw away last update utc | 2026-11-03T13:22:15Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:15Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.84 |
| Market reference dc draw away odds | 1.29 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:18:59Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 3.95 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.5% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:22:17Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.73 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:17Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,464.4999 |
| Elo away rating | 1,487.5305 |
| Elo rating diff | 36.9694 |
| Elo home expectancy | 0.5530 |

</details>


---

## 2026-11-03 — Villarreal vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **64.7%**. Expected goals are 1.05 for Villarreal and 3.83 for Paris Saint Germain (4.88 combined). The most likely exact score is 1-1 at 8.0%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 69.4%; Under 3.5 goals: 50.4%; Double Chance 1X: 35.3%; Double Chance X2: 82.7%; Double Chance 12 (either team wins): 82.0%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 17.3% | 5.78 |
| Draw | 18.0% | 5.55 |
| Paris Saint Germain win | 64.7% | 1.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 1.05 |
| Paris Saint Germain expected goals | 3.83 |
| Expected total goals | 4.88 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 86.9% |
| Under 1.5 | 13.1% |
| Over 2.5 | 69.4% |
| Under 2.5 | 30.6% |
| Over 3.5 | 49.6% |
| Under 3.5 | 50.4% |
| Over 4.5 | 30.4% |
| Under 4.5 | 69.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.04% |
| 2 | 0-3 | 7.80% |
| 3 | 0-2 | 7.74% |
| 4 | 1-3 | 6.44% |
| 5 | 1-2 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 17.3% | 22.2% | 4.41 | -23.7% |
| Draw | 18.0% | 22.2% | 4.42 | -20.4% |
| Paris Saint Germain win | 64.7% | 55.6% | 1.78 | +15.1% |

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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0480 |
| Dc lambda away | 3.8340 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Fair Under 0.5 odds | 33.68 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.64 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.27 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.29 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.1502289891434939, "-10": 0.0003714283820111851, "-11": 0.00010016680992970279, "-12": 2.4830866519349686e-05, "-13": 5.6944622080450355e-06, "-14": 1.2147771947722387e-06, "-15": 2.42216475291529e-07, "-16": 4.533143471851537e-08, "-17": 7.992722702578785e-09, "-18": 1.331719745556896e-09, "-19": 2.090483613352851e-10, "-2": 0.1656848959455752, "-20": 2.8079955071535162e-11, "-3": 0.14066147547896807, "-4": 0.09524119396144616, "-5": 0.05335822666369425, "-6": 0.025423738462403315, "-7": 0.010521098214640983, "-8": 0.0038442111430872596, "-9": 0.0012565842755582685, "0": 0.18015488631641818, "1": 0.1261187620889224, "10": 2.5603016153141427e-09, "11": 1.8873247823952736e-10, "12": 1.2788553697343857e-11, "13": 8.016578086448663e-13, "14": 4.674548806364204e-14, "15": 2.547730607095252e-15, "16": 1.303334961170854e-16, "17": 6.281423611633101e-18, "18": 2.8607699288387887e-19, "19": 1.2275059803101511e-20, "2": 0.03664754729046306, "20": 4.506921707815988e-22, "3": 0.00850440471089176, "4": 0.0015739840895453864, "5": 0.00024103696514684293, "6": 3.1392682767866435e-05, "7": 3.5510505127138567e-06, "8": 3.5465800330356865e-07, "9": 3.1688443553383854e-08} |
| Raw goal margin distribution | {"-1": 0.14421355037518746, "-10": 0.00205519666039001, "-11": 0.0006956769105426018, "-12": 0.00021680396946438887, "-13": 6.258459253018304e-05, "-14": 1.6822656078345185e-05, "-15": 4.230086945230485e-06, "-16": 9.99069371802701e-07, "-17": 2.2243326460220127e-07, "-18": 4.683386541778037e-08, "-19": 9.35226788526966e-09, "-2": 0.17977700015050616, "-20": 1.7745106043371295e-09, "-21": 3.1696245670293124e-10, "-22": 4.6707550396322957e-11, "-3": 0.17893451807084573, "-4": 0.14548140257903042, "-5": 0.09934379098226341, "-6": 0.058262514483758916, "-7": 0.02987653870566481, "-8": 0.013591264036310013, "-9": 0.005550586292411097, "0": 0.08331122686671015, "1": 0.040526489923451245, "10": 4.785429770123121e-09, "11": 4.427737921438282e-10, "12": 3.7717969343292456e-11, "13": 2.9761530340491484e-12, "14": 2.1866997352126489e-13, "15": 1.5029711219512388e-14, "16": 9.702948883442746e-16, "17": 5.90492778072885e-17, "18": 3.3984557087293987e-18, "19": 1.8550059415107214e-19, "2": 0.013432215215135773, "20": 9.620856166470574e-21, "21": 4.697315201353529e-22, "22": 1.8920635806028863e-23, "3": 0.0036543858143409003, "4": 0.0008121467374378436, "5": 0.00015159138102690642, "6": 2.4301314209444924e-05, "7": 3.4062582747742e-06, "8": 4.2355898481796657e-07, "9": 4.7282416484391944e-08} |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 8.3% |
| Unadjusted away-win probability | 85.8% |
| Raw p over 1 5 | 95.4% |
| Raw p under 3 5 | 28.2% |
| Raw p btts yes | 63.4% |
| P home draw | 35.3% |
| P draw away | 82.7% |
| P home away | 82.0% |
| Raw p home draw | 14.2% |
| Raw p draw away | 94.1% |
| Raw p home away | 91.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7881 |
| Totals anchor target over 2 5 | 0.6942 |
| Totals anchor reference over odds | 1.41 |
| Totals anchor reference under odds | 3.05 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8190 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 8.55, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 8.9, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.7, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.98, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.33, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.85, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:00Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.38, "under": 3.04}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.78, "draw": 4.42, "home": 4.41}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.25, "home_away": 1.25, "home_draw": 2.16}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.76, "draw": 4.27, "home": 4.26}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:20Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.26, "home_away": 1.26, "home_draw": 2.15}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.41, "under": 3.05}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.26 |
| Reference draw odds | 4.27 |
| Reference away odds | 1.76 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.03 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | -4.9% |
| Draw probability edge | -4.2% |
| Away probability edge | +9.1% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.1636 |
| Raw ev home | -0.7416 |
| Raw edge prob draw | -0.1383 |
| Raw ev draw | -0.6318 |
| Raw edge prob away | 0.3019 |
| Raw ev away | 0.5274 |
| Market p home draw | 45.3% |
| Market home draw odds | 2.16 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:21:54Z |
| Market reference home draw last update utc | 2026-11-03T13:22:20Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 77.3% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:22:20Z |
| Market reference draw away last update utc | 2026-11-03T13:22:20Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.3% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-03T13:22:20Z |
| Market reference home away last update utc | 2026-11-03T13:22:20Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.15 |
| Market reference dc draw away odds | 1.26 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 89.4% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:10:00Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.9% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:10:00Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 2.02 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market under 3 5 bookmakers | 2 |
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
| 5 | 1-2 | 7.39% |

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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:22:17Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | PAE AEK |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8052 |
| Dc lambda away | 3.1349 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Fair Under 0.5 odds | 53.74 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.05 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.00 |
| Fair Over 3.5 odds | 1.80 |
| Fair Under 3.5 odds | 2.25 |
| Fair Over 4.5 odds | 2.78 |
| Fair Under 4.5 odds | 1.56 |
| Goal margin distribution | {"-1": 0.1732502196020141, "-10": 0.0006305155458577562, "-11": 0.00017778919752150518, "-12": 4.608577735038618e-05, "-13": 1.1052163209953082e-05, "-14": 2.4656518997824844e-06, "-15": 5.141579978764337e-07, "-16": 1.0063856352287472e-07, "-17": 1.855851694379585e-08, "-18": 3.2340392656769225e-09, "-19": 5.307980625828916e-10, "-2": 0.198756021242824, "-20": 7.435280826842481e-11, "-3": 0.17581456287853522, "-4": 0.12419446689985811, "-5": 0.07264590891557562, "-6": 0.03615726115165427, "-7": 0.015635343207116712, "-8": 0.005970967097088518, "-9": 0.002040296869917864, "0": 0.11761974082037543, "1": 0.05658046818405863, "10": 9.642539419723779e-10, "11": 6.98367266568461e-11, "12": 4.649736094385373e-12, "13": 2.8641222954369145e-13, "14": 1.6411901917052754e-14, "15": 8.790359302253895e-16, "16": 4.419339255091602e-17, "17": 2.093240177164688e-18, "18": 9.369231376249288e-20, "19": 3.949761625572112e-21, "2": 0.01604548566528983, "20": 1.4210907569720901e-22, "3": 0.0036456107753020358, "4": 0.0006614554255046638, "5": 9.937848659415692e-05, "6": 1.270455987410982e-05, "7": 1.4110889744421147e-06, "8": 1.384122534110553e-07, "9": 1.2148036997937734e-08} |
| Raw goal margin distribution | {"-1": 0.18047039590294128, "-10": 0.0006166808930738423, "-11": 0.00017250290750468744, "-12": 4.4357268825314605e-05, "-13": 1.0552040879575285e-05, "-14": 2.335068781395071e-06, "-15": 4.829842437226436e-07, "-16": 9.376931202341323e-08, "-17": 1.7151125810828866e-08, "-18": 2.9644733871866047e-09, "-19": 4.826861026557468e-10, "-2": 0.20607563322005568, "-20": 6.718018272045079e-11, "-3": 0.181214452486153, "-4": 0.12715722432529575, "-5": 0.07385013465258451, "-6": 0.03648458166409388, "-7": 0.015657020822941094, "-8": 0.005932996007094633, "-9": 0.002011438313410486, "0": 0.10480711772773534, "1": 0.048178081510654856, "10": 7.707070063303894e-10, "11": 5.537428291779205e-11, "12": 3.657289802992076e-12, "13": 2.2346727016483808e-13, "14": 1.270164638470023e-14, "15": 6.748017259299556e-16, "16": 3.3650136688571e-17, "17": 1.5808898720700346e-18, "18": 7.018421097635856e-20, "19": 2.9352124597601073e-21, "2": 0.013595413025181384, "20": 1.0492979141157418e-22, "3": 0.00307072889433342, "4": 0.0005534425746387988, "5": 8.255924234031709e-05, "6": 1.0476269441080798e-05, "7": 1.154753531907854e-06, "8": 1.1239244204053309e-07, "9": 9.787069022956398e-09} |
| Unadjusted home-win probability | 6.5% |
| Unadjusted draw probability | 10.5% |
| Unadjusted away-win probability | 83.0% |
| Raw p over 1 5 | 90.1% |
| Raw p under 3 5 | 44.5% |
| Raw p btts yes | 52.6% |
| P home draw | 19.5% |
| P draw away | 92.3% |
| P home away | 88.2% |
| Raw p home draw | 17.0% |
| Raw p draw away | 93.5% |
| Raw p home away | 89.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0083 |
| Totals anchor target over 2 5 | 0.7500 |
| Totals anchor reference over odds | 1.30 |
| Totals anchor reference under odds | 3.54 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7456 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 7.0, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 8.84, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.09, "price": 8.84, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.28, "draw": 7.01, "home": 10.9}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.06, "home_away": 1.13, "home_draw": 4.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.32, "under": 3.38}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.24, "draw": 7.12, "home": 10.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.3, "under": 3.54}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.07, "home_away": 1.12, "home_draw": 4.31}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.42 |
| Reference draw odds | 7.12 |
| Reference away odds | 1.24 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.51 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.5% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | -0.0165 |
| Raw ev home | -0.2861 |
| Raw edge prob draw | -0.0183 |
| Raw ev draw | -0.2538 |
| Raw edge prob away | 0.0348 |
| Raw ev away | 0.0620 |
| Market p home draw | 22.5% |
| Market home draw odds | 4.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:22:35Z |
| Market reference home draw last update utc | 2026-11-03T13:22:35Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.8% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:22:35Z |
| Market reference draw away last update utc | 2026-11-03T13:22:35Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.7% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:35Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.31 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 90.5% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:22:05Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.20 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 46.9% |
| Market under 3 5 odds | 2.08 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:22:05Z |
| Market reference under 3 5 odds | 2.06 |
| Market reference under 3 5 opposite odds | 1.83 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,433.0433 |
| Elo away rating | 1,551.6935 |
| Elo rating diff | -58.6502 |
| Elo home expectancy | 0.4164 |

</details>


---

## 2026-11-04 — Borussia Dortmund vs Real Betis

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **54.0%**. Expected goals are 1.91 for Borussia Dortmund and 1.44 for Real Betis (3.35 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.2%; Double Chance 1X: 76.1%; Double Chance X2: 46.0%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 63.4%; BTTS No (at least one team does not score): 36.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 54.0% | 1.85 |
| Draw | 22.1% | 4.53 |
| Real Betis win | 23.9% | 4.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 1.91 |
| Real Betis expected goals | 1.44 |
| Expected total goals | 3.35 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 83.6% |
| Under 1.5 | 16.4% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 41.8% |
| Under 3.5 | 58.2% |
| Over 4.5 | 23.4% |
| Under 4.5 | 76.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.26% |
| 2 | 1-1 | 9.69% |
| 3 | 1-0 | 8.34% |
| 4 | 2-0 | 7.28% |
| 5 | 2-2 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 54.0% | 56.1% | 1.80 | -2.8% |
| Draw | 22.1% | 22.5% | 4.25 | -6.1% |
| Real Betis win | 23.9% | 21.4% | 4.57 | +9.2% |

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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:22:17Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Borussia Dortmund |
| Matched away-team name | Real Betis Balompié |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9108 |
| Dc lambda away | 1.4421 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.4% |
| P btts no | 36.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.72 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.10 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.39 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.27 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.13428089712714678, "-10": 3.2901278845827935e-07, "-11": 4.135068196282694e-08, "-12": 4.777873195200874e-09, "-13": 5.107609787602877e-10, "-14": 5.076540220000009e-11, "-15": 4.668770609468398e-12, "-16": 3.532033996298602e-13, "-2": 0.06716905974016842, "-3": 0.026397090545187796, "-4": 0.00829408598412524, "-5": 0.0021594972637546334, "-6": 0.0004786422821876829, "-7": 9.219999995128379e-05, "-8": 1.5688092760794363e-05, "-9": 2.3888510689737275e-06, "0": 0.22093180892826003, "1": 0.24229011201773482, "10": 7.527966450763126e-06, "11": 1.2536170544421728e-06, "12": 1.9192615110264685e-07, "13": 2.7185327199427747e-08, "14": 3.5801564436467478e-09, "15": 4.3626867302354925e-10, "16": 4.3731430822774046e-11, "2": 0.16176911527307777, "3": 0.08423638538353742, "4": 0.03506949510510068, "5": 0.012098484083516855, "6": 0.0035530938528567186, "7": 0.0009068675433529497, "8": 0.00020445625702491765, "9": 4.125120615428861e-05} |
| Raw goal margin distribution | {"-1": 0.1651360087409028, "-10": 4.806486703559813e-07, "-11": 6.17478883793243e-08, "-12": 7.29381743754491e-09, "-13": 7.971894597888554e-10, "-14": 8.100971386441128e-11, "-15": 7.611231025469734e-12, "-16": 5.852341866135109e-13, "-2": 0.0836749602012191, "-3": 0.033414077683311005, "-4": 0.010691095999214258, "-5": 0.0028382713419295843, "-6": 0.0006419848694753102, "-7": 0.00012627096896822873, "-8": 2.1946982461678604e-05, "-9": 3.4146938875774186e-06, "0": 0.2123956312891662, "1": 0.21723951621047546, "10": 8.01679795749635e-06, "11": 1.3646227994359582e-06, "12": 2.135810517061792e-07, "13": 3.093048280800677e-08, "14": 4.164660163436363e-09, "15": 5.184593299444705e-10, "16": 5.2821021630971284e-11, "2": 0.14690282688896655, "3": 0.07772870566675319, "4": 0.03295273808761746, "5": 0.011591523199722896, "6": 0.003473991156242461, "7": 0.0009053671827983169, "8": 0.0002085035103778727, "9": 4.2984081506187664e-05} |
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
| Totals anchor scale | 0.9774 |
| Totals anchor target over 2 5 | 0.6362 |
| Totals anchor reference over odds | 1.52 |
| Totals anchor reference under odds | 2.55 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6505 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.2, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.27, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.99, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.85, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:32Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.5, "under": 2.57}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.57, "draw": 4.16, "home": 1.8}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.13, "home_away": 1.27, "home_draw": 1.24}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.45, "draw": 4.25, "home": 1.75}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.52, "under": 2.55}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.18, "home_away": 1.25, "home_draw": 1.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.75 |
| Reference draw odds | 4.25 |
| Reference away odds | 4.45 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.57 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | -2.1% |
| Draw probability edge | -0.4% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0702 |
| Raw ev home | -0.1161 |
| Raw edge prob draw | -0.0122 |
| Raw ev draw | -0.0973 |
| Raw edge prob away | 0.0824 |
| Raw ev away | 0.3552 |
| Market p home draw | 78.1% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:21:54Z |
| Market reference home draw last update utc | 2026-11-03T13:22:35Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.4% |
| Market draw away odds | 2.18 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:22:35Z |
| Market reference draw away last update utc | 2026-11-03T13:22:35Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.5% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:35Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.24 |
| Market reference dc draw away odds | 2.18 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:16:32Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.0% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:16:32Z |
| Market reference under 3 5 odds | 1.63 |
| Market reference under 3 5 opposite odds | 2.28 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,519.5879 |
| Elo away rating | 1,456.8479 |
| Elo rating diff | 122.7400 |
| Elo home expectancy | 0.6696 |

</details>


---

## 2026-11-04 — Fenerbahce vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **71.8%**. Expected goals are 0.59 for Fenerbahce and 3.45 for Liverpool (4.04 combined). The most likely exact score is 0-3 at 10.0%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 68.7%; Under 3.5 goals: 50.6%; Double Chance 1X: 28.2%; Double Chance X2: 87.4%; Double Chance 12 (either team wins): 84.4%; Under 4.5 goals: 69.2%; BTTS Yes (both teams score): 46.1%; BTTS No (at least one team does not score): 53.9%.

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
| Expected total goals | 4.04 |
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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Fenerbahçe SK |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.5907 |
| Dc lambda away | 3.4538 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Goal margin distribution | {"-1": 0.1257083708043672, "-10": 0.0009399903350848472, "-11": 0.00028252700592678307, "-12": 7.800968151617609e-05, "-13": 1.9916704991684615e-05, "-14": 4.7282251674670525e-06, "-15": 1.0488217123786805e-06, "-16": 2.183121076525986e-07, "-17": 4.280162059795555e-08, "-18": 7.930500164274238e-09, "-19": 1.39268026419629e-09, "-2": 0.1627376265367107, "-20": 2.3163210930083859e-10, "-21": 3.388818156329935e-11, "-3": 0.158613583109431, "-4": 0.12193857814970362, "-5": 0.07705960334790123, "-6": 0.04124570159026136, "-7": 0.01912128465342365, "-8": 0.007811700014966886, "-9": 0.002851079820546312, "0": 0.15589231121785896, "1": 0.10063036986003325, "10": 8.903169092509289e-11, "11": 4.577093747904067e-12, "12": 2.161657841414394e-13, "13": 9.43983809206185e-15, "14": 3.833132328992826e-16, "15": 1.454339965017455e-17, "16": 5.177864710782826e-19, "17": 1.73636769219438e-20, "18": 5.502887941387719e-22, "19": 1.6529134705348187e-23, "2": 0.02103973929161004, "20": 4.702253809026495e-25, "21": 1.1766957295797825e-26, "3": 0.0035075297197035143, "4": 0.00046122274621062753, "5": 4.985456910931796e-05, "6": 4.5642087613764504e-06, "7": 3.6191991300229906e-07, "8": 2.5290043501606175e-08, "9": 1.5787814050554965e-09} |
| Raw goal margin distribution | {"-1": 0.14896065065050804, "-10": 0.0014015646866280171, "-11": 0.0004334494670608362, "-12": 0.00012316026406804332, "-13": 3.236135707069886e-05, "-14": 7.90732547450033e-06, "-15": 1.8054442046511258e-06, "-16": 3.8684316797299304e-07, "-17": 7.80749864314302e-08, "-18": 1.4892355045597232e-08, "-19": 2.692344509680349e-09, "-2": 0.196351403341422, "-20": 4.608168851870346e-10, "-21": 6.907723499087667e-11, "-3": 0.19568813171978378, "-4": 0.15419526623792687, "-5": 0.10001419664202753, "-6": 0.054991268180681445, "-7": 0.026203603094382542, "-8": 0.011007559903031249, "-9": 0.004132195002321483, "0": 0.07262284340828609, "1": 0.02696030175732324, "10": 3.0039950869153396e-11, "11": 1.5890338613924435e-12, "12": 7.722784159359925e-14, "13": 3.4708721627236373e-15, "14": 1.4506081568877655e-16, "15": 5.665173026513799e-18, "16": 2.0762165351134308e-19, "17": 7.167343830072377e-21, "18": 2.338397349817522e-22, "19": 7.230930156146908e-24, "2": 0.005744486641459356, "20": 2.1169008968057116e-25, "21": 5.4276982510733745e-27, "3": 0.0009792426226550054, "4": 0.0001319791933771868, "5": 1.4642144435064928e-05, "6": 1.3770362660716024e-06, "7": 1.1223317850523574e-07, "8": 8.06417445977938e-09, "9": 5.177955007063206e-10} |
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
| Totals anchor scale | 0.9711 |
| Totals anchor target over 2 5 | 0.6870 |
| Totals anchor reference over odds | 1.42 |
| Totals anchor reference under odds | 2.96 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7028 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.35, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.7, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.53, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.53, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.55, "draw": 4.93, "home": 5.89}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.17, "home_away": 1.22, "home_draw": 2.61}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.53, "draw": 4.92, "home": 5.68}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:18Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.17, "home_away": 1.21, "home_draw": 2.66}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.42, "under": 2.96}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.68 |
| Reference draw odds | 4.92 |
| Reference away odds | 1.53 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.97 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | -3.9% |
| Draw probability edge | -3.6% |
| Away probability edge | +7.5% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.1312 |
| Raw ev home | -0.8007 |
| Raw edge prob draw | -0.1190 |
| Raw ev draw | -0.6420 |
| Raw edge prob away | 0.2502 |
| Raw ev away | 0.3850 |
| Market p home draw | 36.6% |
| Market home draw odds | 2.66 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:22:18Z |
| Market reference home draw last update utc | 2026-11-03T13:22:18Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.1% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:21:54Z |
| Market reference draw away last update utc | 2026-11-03T13:22:18Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.4% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:18Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.66 |
| Market reference dc draw away odds | 1.17 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 87.8% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.9% |
| Market under 3 5 odds | 1.83 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market reference under 3 5 odds | 1.83 |
| Market reference under 3 5 opposite odds | 2.04 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,423.6387 |
| Elo away rating | 1,539.8399 |
| Elo rating diff | -56.2012 |
| Elo home expectancy | 0.4198 |

</details>


---

## 2026-11-04 — PSV Eindhoven vs Club Brugge

The model's most likely 1X2 outcome is **PSV Eindhoven win** at **48.1%**. Expected goals are 2.41 for PSV Eindhoven and 1.90 for Club Brugge (4.30 combined). The most likely exact score is 2-1 at 8.5%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 72.0%; Under 3.5 goals: 48.7%; Double Chance 1X: 68.5%; Double Chance X2: 51.9%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 68.1%; BTTS Yes (both teams score): 70.4%; BTTS No (at least one team does not score): 29.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PSV Eindhoven win | 48.1% | 2.08 |
| Draw | 20.5% | 4.88 |
| Club Brugge win | 31.5% | 3.18 |

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
| Over 3.5 | 51.3% |
| Under 3.5 | 48.7% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.47% |
| 2 | 1-1 | 7.90% |
| 3 | 2-2 | 7.16% |
| 4 | 1-2 | 6.82% |
| 5 | 3-1 | 5.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 48.1% | 47.2% | 2.13 | +2.4% |
| Draw | 20.5% | 21.2% | 4.50 | -7.9% |
| Club Brugge win | 31.5% | 31.6% | 3.16 | -0.6% |

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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:22:17Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
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
| Dc lambda away | 1.8983 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 70.4% |
| P btts no | 29.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 50.03 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.55 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.57 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.13 |
| Fair Under 4.5 odds | 1.47 |
| Goal margin distribution | {"-1": 0.1644592037630807, "-10": 1.3375838071496321e-06, "-11": 1.9548107663318885e-07, "-12": 2.628688337551816e-08, "-13": 3.272720993155074e-09, "-14": 3.792402706587387e-10, "-15": 4.1054115390699014e-11, "-16": 4.1123868374067905e-12, "-17": 3.3163754173280005e-13, "-2": 0.09053409645491414, "-3": 0.03985564780045134, "-4": 0.014215048125609349, "-5": 0.004235838684706107, "-6": 0.0010802455754109071, "-7": 0.00024029495049258408, "-8": 4.7337109928943475e-05, "-9": 8.360904171197253e-06, "0": 0.20474096831469246, "1": 0.20318633825806362, "10": 1.397249914956969e-05, "11": 2.5871071878201923e-06, "12": 4.407632833979337e-07, "13": 6.95235443421914e-08, "14": 1.0206902848024418e-08, "15": 1.3998865562620713e-09, "16": 1.776587964190394e-10, "17": 1.8151522293764273e-11, "2": 0.14246637472496446, "3": 0.07945965679617856, "4": 0.035905564402797054, "5": 0.013555309773742441, "6": 0.004379748187598724, "7": 0.0012343203839520088, "8": 0.00030806446580619677, "9": 6.893657844778456e-05} |
| Raw goal margin distribution | {"-1": 0.1534471984336081, "-10": 3.4056117344698746e-06, "-11": 5.685892245290034e-07, "-12": 8.744714841489698e-08, "-13": 1.2463041048754244e-08, "-14": 1.6545547408575233e-09, "-15": 2.0551087552251243e-10, "-16": 2.393610755459766e-11, "-17": 2.572292704324142e-12, "-18": 2.1639014087080553e-13, "-2": 0.09045063496650227, "-3": 0.0434609046479486, "-4": 0.01717983281216588, "-5": 0.005730331356934931, "-6": 0.0016467381739885384, "-7": 0.00041468666555976414, "-8": 9.278878757883913e-05, "-9": 1.8660916666523494e-05, "0": 0.18763016646770653, "1": 0.193584563856964, "10": 3.62878504713485e-05, "11": 7.675759268936626e-06, "12": 1.4956328096958598e-06, "13": 2.700598164064963e-07, "14": 4.542277824691719e-08, "15": 7.147990621767784e-09, "16": 1.0547737261485397e-09, "17": 1.4360936851170027e-10, "18": 1.530581526073471e-11, "2": 0.14518603399600394, "3": 0.08838297071836598, "4": 0.04426346183728144, "5": 0.018705218716061858, "6": 0.006810268256087528, "7": 0.002172782963948949, "8": 0.0006159541531422799, "9": 0.0001569431887210132} |
| Unadjusted home-win probability | 50.0% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 31.2% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 37.7% |
| Raw p btts yes | 77.0% |
| P home draw | 68.5% |
| P draw away | 51.9% |
| P home away | 79.5% |
| Raw p home draw | 68.8% |
| Raw p draw away | 50.0% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8685 |
| Totals anchor target over 2 5 | 0.7200 |
| Totals anchor reference over odds | 1.35 |
| Totals anchor reference under odds | 3.20 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7993 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.55, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.13, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.86, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.64, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:10:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.35, "under": 3.17}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.16, "draw": 4.37, "home": 2.13}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.8, "home_away": 1.25, "home_draw": 1.41}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:16Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.81, "home_away": 1.24, "home_draw": 1.41}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.06, "draw": 4.5, "home": 2.07}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.35, "under": 3.2}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.07 |
| Reference draw odds | 4.50 |
| Reference away odds | 3.06 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.26 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | +0.8% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.0276 |
| Raw ev home | 0.0648 |
| Raw edge prob draw | -0.0244 |
| Raw ev draw | -0.1557 |
| Raw edge prob away | -0.0032 |
| Raw ev away | -0.0127 |
| Market p home draw | 68.6% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:21:54Z |
| Market reference home draw last update utc | 2026-11-03T13:22:16Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.4% |
| Market draw away odds | 1.81 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:22:16Z |
| Market reference draw away last update utc | 2026-11-03T13:22:16Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.0% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:16Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.41 |
| Market reference dc draw away odds | 1.81 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 89.7% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:10:01Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.1% |
| Market under 3 5 odds | 1.99 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:10:01Z |
| Market reference under 3 5 odds | 1.98 |
| Market reference under 3 5 opposite odds | 1.91 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,466.2523 |
| Elo away rating | 1,460.9610 |
| Elo rating diff | 65.2913 |
| Elo home expectancy | 0.5929 |

</details>


---

## 2026-11-04 — Porto vs Napoli

The model's most likely 1X2 outcome is **Porto win** at **51.6%**. Expected goals are 1.64 for Porto and 0.98 for Napoli (2.62 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 55.3%; Under 3.5 goals: 66.4%; Double Chance 1X: 75.8%; Double Chance X2: 48.4%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 51.6% | 1.94 |
| Draw | 24.3% | 4.12 |
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
| Draw | 24.3% | 24.6% | 3.89 | -5.7% |
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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:22:17Z |
| Market best away last update utc | 2026-11-03T13:22:17Z |
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
| Dc lambda home | 1.6421 |
| Dc lambda away | 0.9755 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Goal margin distribution | {"-1": 0.15321673496455174, "-10": 4.5643775650621034e-08, "-11": 4.474357201256392e-09, "-12": 4.0297244720293726e-10, "-13": 3.356068995974762e-11, "-14": 2.5983897246707062e-12, "-15": 1.8680852109971888e-13, "-16": 1.1349157859264768e-14, "-2": 0.06254197524065859, "-3": 0.01978197905535693, "-4": 0.0049446822615913395, "-5": 0.0010171169665449847, "-6": 0.0001773247990568089, "-7": 2.6788795774773982e-05, "-8": 3.5675075596662775e-06, "-9": 4.245328025285414e-07, "0": 0.24250000272643124, "1": 0.22421795962197144, "10": 7.3594218269237635e-06, "11": 1.2144118581224441e-06, "12": 1.841127701570491e-07, "13": 2.5811464894002722e-08, "14": 3.364025468153533e-09, "15": 4.0712228917098863e-10, "16": 4.1635621034548856e-11, "2": 0.15640406157050535, "3": 0.08327590936752094, "4": 0.035039770131146446, "5": 0.012132965710634923, "6": 0.003560727677802366, "7": 0.0009055150816045745, "8": 0.00020299278934642732, "9": 4.066307097314181e-05} |
| Raw goal margin distribution | {"-1": 0.151480901668212, "-10": 1.8133053435519627e-08, "-11": 1.5889395266308612e-09, "-12": 1.2786169350420355e-10, "-13": 9.509477975095966e-12, "-14": 6.544655586646025e-13, "-15": 3.845449642690095e-14, "-2": 0.057399244166973624, "-3": 0.0166042916303627, "-4": 0.0037626637831386835, "-5": 0.0006981331853070954, "-6": 0.00010944142946966016, "-7": 1.483574364295166e-05, "-8": 1.7702782206312335e-06, "-9": 1.885646876728088e-07, "0": 0.23423014175482856, "1": 0.2510004185259718, "10": 3.3128598805064505e-06, "11": 4.886666575704013e-07, "12": 6.619405762193765e-08, "13": 8.287211846885222e-09, "14": 9.600896176908413e-10, "15": 9.496100839131817e-11, "2": 0.1626494499353849, "3": 0.07920270064625465, "4": 0.030212611324593387, "5": 0.009436356620960618, "6": 0.002490124335835034, "7": 0.0005682269249590186, "8": 0.00011413720341560541, "9": 2.04653548661436e-05} |
| Unadjusted home-win probability | 53.6% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 73.0% |
| Raw p under 3 5 | 73.2% |
| Raw p btts yes | 49.7% |
| P home draw | 75.8% |
| P draw away | 48.4% |
| P home away | 75.7% |
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
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4823 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.43, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.58, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.1, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.75, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.53, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 7.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:39Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.88, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:39Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.44, "price": 2.88, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:13Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.17}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.73, "draw": 3.84, "home": 2.05}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.17}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.86, "home_away": 1.31, "home_draw": 1.32}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.88, "draw": 3.89, "home": 1.93}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.75, "under": 2.14}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.94, "home_away": 1.29, "home_draw": 1.29}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.93 |
| Reference draw odds | 3.89 |
| Reference away odds | 3.88 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:54Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:54Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:54Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:54Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0284 |
| Raw ev home | 0.0982 |
| Raw edge prob draw | -0.0118 |
| Raw ev draw | -0.0888 |
| Raw edge prob away | -0.0166 |
| Raw ev away | -0.1073 |
| Market p home draw | 75.0% |
| Market home draw odds | 1.32 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-03T13:21:54Z |
| Market reference home draw last update utc | 2026-11-03T13:22:39Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.9% |
| Market draw away odds | 1.94 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:22:39Z |
| Market reference draw away last update utc | 2026-11-03T13:22:39Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:39Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.94 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 79.5% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:16:13Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.6% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market under 3 5 bookmakers | 2 |
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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:22:17Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
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
| Dc lambda away | 1.7513 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Goal margin distribution | {"-1": 0.2372352956982229, "-10": 2.4898068199194824e-05, "-11": 4.8302253522920015e-06, "-12": 8.622140766203171e-07, "-13": 1.424933541643021e-07, "-14": 2.191830413796724e-08, "-15": 3.1496139514483025e-09, "-16": 4.188265418982574e-10, "-17": 4.485511199646267e-11, "-2": 0.17456598592501113, "-3": 0.10205950920690092, "-4": 0.04833475127271028, "-5": 0.01912294532797392, "-6": 0.006474608154772725, "-7": 0.0019120163956960758, "-8": 0.0005000238171512196, "-9": 0.00011723948828992287, "0": 0.20147936859557514, "1": 0.11281929597995861, "10": 5.878819001606157e-07, "11": 8.176288083001267e-08, "12": 1.0463289839342783e-08, "13": 1.2396871830872611e-09, "14": 1.367063869633461e-10, "15": 1.4083271017673573e-11, "16": 1.3425941862567526e-12, "17": 1.0308295662571751e-13, "2": 0.05907030641888598, "3": 0.02475867668122568, "4": 0.008406162786523709, "5": 0.002384281044700575, "6": 0.0005787360122632886, "7": 0.00012252451286342577, "8": 2.2971344685805564e-05, "9": 3.861304013131542e-06} |
| Raw goal margin distribution | {"-1": 0.22928232122494835, "-10": 4.509450705329437e-06, "-11": 7.063466254407591e-07, "-12": 1.0167005095416675e-07, "-13": 1.3534591071335413e-08, "-14": 1.6750827969304232e-09, "-15": 1.9232080194736195e-10, "-16": 1.8507454232852347e-11, "-2": 0.1491432084706571, "-3": 0.07466002853035716, "-4": 0.029641957715708926, "-5": 0.009705281732874044, "-6": 0.0026968301344727484, "-7": 0.0006499332096583517, "-8": 0.00013815906585345, "-9": 2.6255345656488084e-05, "0": 0.22386558973347329, "1": 0.1659136522664426, "10": 1.6172128836171e-07, "11": 1.816041539535307e-08, "12": 1.8739815017865056e-09, "13": 1.7884703802616325e-10, "14": 1.5868550072808624e-11, "15": 1.3061455774927761e-12, "16": 9.011069970176212e-14, "2": 0.07665353563442277, "3": 0.02750940620359558, "4": 0.007830045809354008, "5": 0.001837934039926921, "6": 0.00036613371444028817, "7": 6.325854706965345e-05, "8": 9.640381643019222e-06, "9": 1.3133997643557265e-06} |
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
| Totals anchor scale | 1.2495 |
| Totals anchor target over 2 5 | 0.7254 |
| Totals anchor reference over odds | 1.34 |
| Totals anchor reference under odds | 3.25 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5885 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 6.73, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.21, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 3.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.18, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.36, "under": 3.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.58, "draw": 4.88, "home": 5.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.18, "home_away": 1.22, "home_draw": 2.54}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.56, "draw": 4.92, "home": 5.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.19, "home_away": 1.21, "home_draw": 2.56}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.34, "under": 3.25}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.31 |
| Reference draw odds | 4.92 |
| Reference away odds | 1.56 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.32 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | +3.1% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.1029 |
| Raw ev home | 0.5634 |
| Raw edge prob draw | 0.0320 |
| Raw ev draw | 0.1014 |
| Raw edge prob away | -0.1349 |
| Raw ev away | -0.2164 |
| Market p home draw | 38.0% |
| Market home draw odds | 2.56 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:22:17Z |
| Market reference home draw last update utc | 2026-11-03T13:22:17Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.7% |
| Market draw away odds | 1.19 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:22:17Z |
| Market reference draw away last update utc | 2026-11-03T13:22:17Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.3% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:17Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.56 |
| Market reference dc draw away odds | 1.19 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:21:01Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.8% |
| Market under 3 5 odds | 1.99 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market reference under 3 5 odds | 1.99 |
| Market reference under 3 5 opposite odds | 1.90 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
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
| Market best home last update utc | 2026-11-03T13:22:17Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
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
| Dc lambda away | 3.3041 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Goal margin distribution | {"-1": 0.17712210894097682, "-10": 5.9975745169311985e-05, "-11": 1.2915239585790254e-05, "-12": 2.556011446802837e-06, "-13": 4.6789427448220843e-07, "-14": 7.966370821297064e-08, "-15": 1.2676130763599703e-08, "-16": 1.8924998862227124e-09, "-17": 2.6443297216805086e-10, "-18": 3.137130571752446e-11, "-2": 0.15786973010808386, "-3": 0.1080210089675845, "-4": 0.0587469671810794, "-5": 0.0263814575748213, "-6": 0.01006251774117378, "-7": 0.0033305669536293357, "-8": 0.0009727212245243184, "-9": 0.0002540412849343138, "0": 0.20533613701577325, "1": 0.1719639832310426, "10": 1.4224045949328979e-08, "11": 1.2191636651079616e-09, "12": 9.603607190178127e-11, "13": 6.997314182435595e-12, "14": 4.741941714610384e-13, "15": 3.0032705246871784e-14, "16": 1.7846606790657607e-15, "17": 9.92538699829484e-17, "18": 4.686800716886267e-18, "2": 0.05943605307518449, "3": 0.016187186656694424, "4": 0.003503972152767958, "5": 0.0006263052201247551, "6": 9.508367386502227e-05, "7": 1.2526493376655174e-05, "8": 1.4561690176909596e-06, "9": 1.513699769842305e-07} |
| Raw goal margin distribution | {"-1": 0.18001618719355988, "-10": 0.0006215939093869188, "-11": 0.00018091204429743034, "-12": 4.849271921354188e-05, "-13": 1.2043166858330485e-05, "-14": 2.785639747620945e-06, "-15": 6.028558551282844e-07, "-16": 1.2256245519241118e-07, "-17": 2.349154532817303e-08, "-18": 4.2583429033754884e-09, "-19": 7.313723375766719e-10, "-2": 0.18891893131456317, "-20": 1.1762719874350295e-10, "-21": 1.533428086538478e-11, "-3": 0.15958602249937806, "-4": 0.11059712277143834, "-5": 0.06455625365578621, "-6": 0.032424675116979926, "-7": 0.014258817344155612, "-8": 0.005567962262460431, "-9": 0.001953290460942699, "0": 0.12474441578600387, "1": 0.07294085418384459, "10": 6.203363762637464e-08, "11": 7.186212069009225e-09, "12": 7.666923602255047e-10, "13": 7.578745988679661e-11, "14": 6.977400440429042e-12, "15": 6.010273438544719e-13, "16": 4.863514886886071e-14, "17": 3.7103632842025334e-15, "18": 2.6770564377771915e-16, "19": 1.8300690527301828e-17, "2": 0.02992950814784233, "20": 1.1715174211689603e-18, "21": 6.078780478399476e-20, "3": 0.01006308173280623, "4": 0.0027758246500936383, "5": 0.0006449091941840439, "6": 0.00012892820382893149, "7": 2.2566689560375865e-05, "8": 3.5074596355179633e-06, "9": 4.897509393501706e-07} |
| Unadjusted home-win probability | 11.7% |
| Unadjusted draw probability | 12.5% |
| Unadjusted away-win probability | 75.9% |
| Raw p over 1 5 | 94.2% |
| Raw p under 3 5 | 32.3% |
| Raw p btts yes | 70.3% |
| P home draw | 45.7% |
| P draw away | 74.8% |
| P home away | 79.5% |
| Raw p home draw | 24.1% |
| Raw p draw away | 88.3% |
| Raw p home away | 87.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7293 |
| Totals anchor target over 2 5 | 0.6256 |
| Totals anchor reference over odds | 1.54 |
| Totals anchor reference under odds | 2.47 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8059 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.6, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.93, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.76, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.99, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 3.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.35, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.63, "price": 2.35, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.27, "draw": 4.0, "home": 3.07}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.43, "home_away": 1.29, "home_draw": 1.71}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.17, "draw": 4.0, "home": 3.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:22:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.54, "under": 2.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.54, "under": 2.47}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.4, "home_away": 1.28, "home_draw": 1.75}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.12 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.17 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | -5.8% |
| Draw probability edge | -3.5% |
| Away probability edge | +9.3% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.1933 |
| Raw ev home | -0.6365 |
| Raw edge prob draw | -0.1151 |
| Raw ev draw | -0.5010 |
| Raw edge prob away | 0.3084 |
| Raw ev away | 0.7224 |
| Market p home draw | 55.3% |
| Market home draw odds | 1.75 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:22:36Z |
| Market reference home draw last update utc | 2026-11-03T13:22:36Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.1% |
| Market draw away odds | 1.43 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:21:54Z |
| Market reference draw away last update utc | 2026-11-03T13:22:36Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.6% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:36Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.75 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 85.5% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:22:23Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.04 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.5% |
| Market under 3 5 odds | 1.67 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:22:23Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
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
| Dc lambda away | 3.0127 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Goal margin distribution | {"-1": 0.1369152422459069, "-10": 0.0009375880872506375, "-11": 0.0002725834648935589, "-12": 7.273467296171862e-05, "-13": 1.793284902858327e-05, "-14": 4.108804891674013e-06, "-15": 8.792205056268771e-07, "-16": 1.7647440249453492e-07, "-17": 3.3352525544612776e-08, "-18": 5.955293106235756e-09, "-19": 1.006375570797772e-09, "-2": 0.18708299365223566, "-20": 1.5382615746457643e-10, "-3": 0.18504159255705657, "-4": 0.1416721218964817, "-5": 0.08822133102753478, "-6": 0.046227345208899005, "-7": 0.020890984542987663, "-8": 0.008295361721718068, "-9": 0.0029365373922913924, "0": 0.1194708158265803, "1": 0.053980887539214074, "10": 5.41178247823318e-13, "11": 1.6565712975150987e-14, "12": 4.654086901154243e-16, "13": 1.2081605847767614e-17, "14": 2.914561763442384e-19, "15": 6.566560129337157e-21, "16": 1.387727550104331e-22, "17": 2.7614271388635087e-24, "18": 5.191470346721185e-26, "19": 9.236973452215353e-28, "2": 0.007149959428268668, "20": 1.4865590807570473e-29, "3": 0.0007445965117419559, "4": 6.002309860724118e-05, "5": 3.935410063527693e-06, "6": 2.171189410544179e-07, "7": 1.0330944774026425e-08, "8": 4.3191554368505435e-10, "9": 1.6098351793843026e-11} |
| Raw goal margin distribution | {"-1": 0.16998063743796563, "-10": 0.0006625237240687265, "-11": 0.00018015502100105217, "-12": 4.495500849910901e-05, "-13": 1.0363873021364997e-05, "-14": 2.220145823318772e-06, "-15": 4.4414207519624315e-07, "-16": 8.333645078518186e-08, "-17": 1.4722686271656413e-08, "-18": 2.4572522220220384e-09, "-19": 3.8824863879727507e-10, "-2": 0.22079267421991586, "-20": 5.5816282165302404e-11, "-3": 0.206043482147623, "-4": 0.1483128123430616, "-5": 0.0866633396050739, "-6": 0.0425622931110475, "-7": 0.018014589822609058, "-8": 0.006696053002421751, "-9": 0.002218093494243515, "0": 0.0756802806808737, "1": 0.01942742703891414, "10": 1.10923908882724e-13, "11": 3.1757951033367915e-15, "12": 8.343851408500572e-17, "13": 2.0253166531190376e-18, "14": 4.568090761193738e-20, "15": 9.621826333887364e-22, "16": 1.9008724222660882e-23, "17": 3.535797630924176e-25, "18": 6.21344491292266e-27, "19": 1.0336536219064431e-28, "2": 0.0024476505048264176, "20": 1.5646181631289183e-30, "3": 0.00024049497151497774, "4": 1.8226704917359024e-05, "5": 1.121365747377092e-06, "6": 5.7985480035969526e-08, "7": 2.5840504581283016e-09, "8": 1.0112950173437221e-10, "9": 3.5271278813760004e-12} |
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
| Totals anchor scale | 1.0703 |
| Totals anchor target over 2 5 | 0.6434 |
| Totals anchor reference over odds | 1.50 |
| Totals anchor reference under odds | 2.58 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6065 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 7.14, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.17, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:21:58Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 9.26, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:21:58Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.08, "price": 9.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.69, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:43Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.5, "under": 2.59}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.27, "draw": 6.9, "home": 11.6}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.06, "home_away": 1.14, "home_draw": 4.14}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:21:58Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.07, "home_away": 1.14, "home_draw": 4.17}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.26, "draw": 6.47, "home": 10.97}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.5, "under": 2.58}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.97 |
| Reference draw odds | 6.47 |
| Reference away odds | 1.26 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.66 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | -1.7% |
| Draw probability edge | -1.9% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0569 |
| Raw ev home | -0.7432 |
| Raw edge prob draw | -0.0626 |
| Raw ev draw | -0.4778 |
| Raw edge prob away | 0.1194 |
| Raw ev away | 0.1458 |
| Market p home draw | 25.3% |
| Market home draw odds | 4.17 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:21:58Z |
| Market reference home draw last update utc | 2026-11-03T13:22:15Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.5% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:21:58Z |
| Market reference draw away last update utc | 2026-11-03T13:22:15Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.1% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:15Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.75 |
| Market reference dc draw away odds | 1.05 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:21:43Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.8% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:21:43Z |
| Market reference under 3 5 odds | 1.63 |
| Market reference under 3 5 opposite odds | 2.26 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
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
| 1 | 3-0 | 9.31% |
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
| Market best home last update utc | 2026-11-03T13:21:54Z |
| Market best draw last update utc | 2026-11-03T13:21:54Z |
| Market best away last update utc | 2026-11-03T13:21:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Viking FK |
| Matched away-team name | Sabah FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.8506 |
| Dc lambda away | 0.9068 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:22:17.761945+00:00 |
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
| Fair Under 0.5 odds | 39.47 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.65 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.58 |
| Fair Over 3.5 odds | 1.90 |
| Fair Under 3.5 odds | 2.11 |
| Fair Over 4.5 odds | 3.01 |
| Fair Under 4.5 odds | 1.50 |
| Goal margin distribution | {"-1": 0.08315179659022925, "-10": 7.156424353844827e-10, "-11": 4.784654904313759e-11, "-12": 2.9401556200965413e-12, "-13": 1.6712437229904136e-13, "-14": 8.836037917710991e-15, "-15": 4.366264240065722e-16, "-16": 2.025012063105047e-17, "-17": 8.847602854365173e-19, "-18": 3.652958696210261e-20, "-19": 1.421653972774973e-21, "-2": 0.022020252607596793, "-20": 4.754910015916988e-23, "-3": 0.0046618588958851, "-4": 0.0007854511003847365, "-5": 0.0001093569232466056, "-6": 1.2938327732219527e-05, "-7": 1.3287838239431432e-06, "-8": 1.20444653314132e-07, "-9": 9.764220063310372e-09, "0": 0.1435389528076786, "1": 0.15513095296567067, "10": 0.0006254816407338322, "11": 0.00017758211149116948, "12": 4.633925295634005e-05, "13": 1.1185325160393704e-05, "14": 2.5112879323500066e-06, "15": 5.26961720233565e-07, "16": 1.0378313420591255e-07, "17": 1.9255504498741368e-08, "18": 3.376013368038385e-09, "19": 5.579347521663281e-10, "2": 0.18201193395335502, "20": 7.924318579510012e-11, "3": 0.163631460252095, "4": 0.11707305424776712, "5": 0.06921722648202552, "6": 0.03477572336070799, "7": 0.015166398796681354, "8": 0.005837753852066564, "9": 0.00200967544575038} |
| Raw goal margin distribution | {"-1": 0.03354933868696439, "-10": 1.2166944195121974e-09, "-11": 9.776540093196255e-11, "-12": 7.2287137830937914e-12, "-13": 4.948696191552395e-13, "-14": 3.153522749852204e-14, "-15": 1.8793346691656132e-15, "-16": 1.0517202934526155e-16, "-17": 5.5471132158437615e-18, "-18": 2.7664094453109918e-19, "-19": 1.3082973596355035e-20, "-2": 0.009918443140295986, "-20": 5.879734167315475e-22, "-21": 2.494155424938592e-23, "-22": 8.871995088534698e-25, "-3": 0.0023957169002280184, "-4": 0.00046916033634315525, "-5": 7.67958447132905e-05, "-6": 1.0761602739106538e-05, "-7": 1.315664609284159e-06, "-8": 1.424663955247503e-07, "-9": 1.3833151336112226e-08, "0": 0.07446529718896179, "1": 0.13759925393784714, "10": 0.0023199715486315, "11": 0.0007916194252775756, "12": 0.00024855494093463084, "13": 7.225739128991019e-05, "14": 1.955318765318863e-05, "15": 4.948297925978066e-06, "16": 1.1759316577031117e-06, "17": 2.633776828766882e-07, "18": 5.577743203595051e-08, "19": 1.1201563267272784e-08, "2": 0.17885609172350675, "20": 2.1377650710118664e-09, "21": 3.850843890670936e-10, "22": 5.8167956490057196e-11, "3": 0.1834534313825459, "4": 0.15256037447616894, "5": 0.10604453525836913, "6": 0.06310410939850192, "7": 0.03276091270183602, "8": 0.015064452444368557, "9": 0.006211438029170971} |
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
| Totals anchor scale | 0.8255 |
| Totals anchor target over 2 5 | 0.7208 |
| Totals anchor reference over odds | 1.35 |
| Totals anchor reference under odds | 3.22 |
| Totals anchor reference last update utc | 2026-11-03T13:22:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8175 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.42, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.34, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.44, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.17, "price": 5.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.72, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:16:17Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.35, "under": 3.17}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.98, "draw": 5.49, "home": 1.45}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.98, "home_away": 1.19, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.66, "draw": 5.37, "home": 1.43}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:17Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.01, "home_away": 1.18, "home_draw": 1.14}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.35, "under": 3.22}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.43 |
| Reference draw odds | 5.37 |
| Reference away odds | 6.66 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:17Z |
| Market reference home last update utc | 2026-11-03T13:22:17Z |
| Market reference draw last update utc | 2026-11-03T13:22:17Z |
| Market reference away last update utc | 2026-11-03T13:22:17Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.21 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:16Z |
| Home probability edge | +5.7% |
| Draw probability edge | -3.0% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.1906 |
| Raw ev home | 0.2747 |
| Raw edge prob draw | -0.0987 |
| Raw ev draw | -0.5912 |
| Raw edge prob away | -0.0919 |
| Raw ev away | -0.6760 |
| Market p home draw | 85.3% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:22:17Z |
| Market reference home draw last update utc | 2026-11-03T13:22:17Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 32.3% |
| Market draw away odds | 3.01 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-03T13:22:17Z |
| Market reference draw away last update utc | 2026-11-03T13:22:17Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.4% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-03T13:21:54Z |
| Market reference home away last update utc | 2026-11-03T13:22:17Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.14 |
| Market reference dc draw away odds | 3.01 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-03T13:16:17Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.6% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-03T13:16:17Z |
| Market reference under 3 5 odds | 1.96 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:35Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,427.8588 |
| Elo away rating | 1,421.2723 |
| Elo rating diff | 66.5865 |
| Elo home expectancy | 0.5947 |

</details>


---
