# UEFA Champions League — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 566 |
| Training data through | 2026-11-03 |
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
| Training sha256 | 9876abe764b24a62196f1fe0dbaa5b950f9ada7b55c2ad2a4bdf889e1ab12f65 |
| Training as of utc | 2026-11-04T10:20:15.005079+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 9, 'bbs_rows_with_statistics': 42, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 52, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-04T10:20:15.005079+00:00', 'observations': 383, 'observations_sha256': '2bd8823c03640db52bc36f82207c824a76b8bb870871ba41cbb7c737225f9963', 'eligible_training_matches': 16, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 94, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 2, 'retrospective_eligible_training_matches': 16, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': '1e3081e2153ab9f63d20d21a823216ae0eba79f5107f3b5f54e1f527881fa21e', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 835.926 |
| Base scoring parameter | 0.206 |
| Home-advantage parameter | 0.294 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 71, 'matches': 566, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-03'} |
| Training data health | {'completed_matches': 63, 'latest_completed_utc': '2026-11-03T20:00:00+00:00', 'latest_completed_date': '2026-11-03', 'next_fixture_utc': '2026-11-04T17:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-11-04T10:20:15.005079+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '936f6e47aadb3f3787783bc63a150534d5c0b8033d4d07c0cc14b54e0fe12b75', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0, 'training_end': '2026-11-03', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261104T102015005079Z_c396d01d66d9aac4f93a45d16fed27f6e92af79267fd7c4679d92ef8cb7be1b1.json |
| Over 1 5 in window quote fixtures | 9 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1, 'ANCHORED_ALTERNATE': 8} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 9} |
| Legacy comparison status | {'None': 9} |
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

## 2026-11-04 — AEK Athens vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **81.6%**. Expected goals are 0.86 for AEK Athens and 3.38 for Real Madrid (4.24 combined). The most likely exact score is 0-3 at 8.9%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 78.6%; Under 3.5 goals: 39.4%; Double Chance 1X: 18.4%; Double Chance X2: 92.9%; Double Chance 12 (either team wins): 88.6%; Under 4.5 goals: 59.0%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AEK Athens win | 7.1% | 14.15 |
| Draw | 11.4% | 8.79 |
| Real Madrid win | 81.6% | 1.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AEK Athens expected goals | 0.86 |
| Real Madrid expected goals | 3.38 |
| Expected total goals | 4.24 |
| Over 0.5 | 98.5% |
| Under 0.5 | 1.5% |
| Over 1.5 | 91.9% |
| Under 1.5 | 8.1% |
| Over 2.5 | 78.6% |
| Under 2.5 | 21.4% |
| Over 3.5 | 60.6% |
| Under 3.5 | 39.4% |
| Over 4.5 | 41.0% |
| Under 4.5 | 59.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 8.92% |
| 2 | 0-2 | 7.91% |
| 3 | 1-3 | 7.70% |
| 4 | 0-4 | 7.54% |
| 5 | 1-2 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AEK Athens win | 7.1% | 7.5% | 11.50 | -18.8% |
| Draw | 11.4% | 12.2% | 7.31 | -16.8% |
| Real Madrid win | 81.6% | 80.3% | 1.27 | +3.6% |

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
| Market best home last update utc | 2026-11-04T10:20:05Z |
| Market best draw last update utc | 2026-11-04T10:19:25Z |
| Market best away last update utc | 2026-11-04T10:19:25Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | PAE AEK |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8631 |
| Dc lambda away | 3.3811 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:20:15.005079+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 67.78 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.42 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.68 |
| Fair Over 3.5 odds | 1.65 |
| Fair Under 3.5 odds | 2.54 |
| Fair Over 4.5 odds | 2.44 |
| Fair Under 4.5 odds | 1.70 |
| Goal margin distribution | {"-1": 0.15974926954255023, "-10": 0.0009685035363046887, "-11": 0.00029136428175598753, "-12": 8.060921316711039e-05, "-13": 2.0638604823210708e-05, "-14": 4.916816323073469e-06, "-15": 1.0950984630810476e-06, "-16": 2.2897926160730695e-07, "-17": 4.5114252004128535e-08, "-18": 8.402858243880092e-09, "-19": 1.4834086701020185e-09, "-2": 0.19039966301363945, "-20": 2.4706923864181176e-10, "-21": 3.492576986638384e-11, "-3": 0.17668631194473156, "-4": 0.1317335251825863, "-5": 0.08163239838910351, "-6": 0.043146195371912284, "-7": 0.01984503115216839, "-8": 0.008070124337999507, "-9": 0.0029388633128956923, "0": 0.11378048983217567, "1": 0.051249572667229466, "10": 1.378987947228003e-09, "11": 1.0589837481555798e-10, "12": 7.478790909495968e-12, "13": 4.887882642027575e-13, "14": 2.9724745447061835e-14, "15": 1.6899780110403599e-15, "16": 9.020233085121811e-17, "17": 4.5365854497703214e-18, "18": 2.1569302259137283e-19, "19": 9.719940296972482e-21, "2": 0.015037499817688878, "20": 4.132522114030955e-22, "21": 1.4912011238619227e-23, "3": 0.0035620998596123258, "4": 0.0006779430663054847, "5": 0.00010723910753482633, "6": 1.4468611827674527e-05, "7": 1.6987515639533312e-06, "8": 1.7634048689878202e-07, "9": 1.639248979482713e-08} |
| Raw goal margin distribution | {"-1": 0.1655310321331954, "-10": 0.0010035563257862863, "-11": 0.0003019095512857381, "-12": 8.352668086186439e-05, "-13": 2.1385572328174263e-05, "-14": 5.094769341345316e-06, "-15": 1.1347330688920532e-06, "-16": 2.372666467865052e-07, "-17": 4.674706006196401e-08, "-18": 8.706980645115984e-09, "-19": 1.537097283389543e-09, "-2": 0.1972907470983181, "-20": 2.5601134952199905e-10, "-21": 3.618982891492399e-11, "-3": 0.18308107238154853, "-4": 0.13650132142989005, "-5": 0.08458689795296566, "-6": 0.04470777408237733, "-7": 0.020563277057482118, "-8": 0.008362204189963226, "-9": 0.0030452288068361453, "0": 0.09451379833165315, "1": 0.04381358403489458, "10": 1.178905523784284e-09, "11": 9.053319086711204e-11, "12": 6.393665682253211e-12, "13": 4.1786818063775834e-13, "14": 2.5411873012425225e-14, "15": 1.4447728976126035e-15, "16": 7.711454354077557e-17, "17": 3.878355613335441e-18, "18": 1.8439733014769756e-19, "19": 8.309638477978437e-21, "2": 0.01285565376739834, "20": 3.53291931027029e-22, "21": 1.2748372786926804e-23, "3": 0.003045261714730466, "4": 0.0005795778181276921, "5": 9.167939175439393e-05, "6": 1.2369307824208185e-05, "7": 1.4522734635262557e-06, "8": 1.5075459831949622e-07, "9": 1.4014043274668273e-08} |
| Unadjusted home-win probability | 6.0% |
| Unadjusted draw probability | 9.5% |
| Unadjusted away-win probability | 84.5% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 38.7% |
| Raw p btts yes | 55.6% |
| P home draw | 18.4% |
| P draw away | 92.9% |
| P home away | 88.6% |
| Raw p home draw | 15.5% |
| Raw p draw away | 94.0% |
| Raw p home away | 90.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7862 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 6.52, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.67, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:10Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 9.12, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:10Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.09, "price": 9.12, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.27, "draw": 7.31, "home": 10.9}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.07, "home_away": 1.12, "home_draw": 4.18}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:44Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.28, "under": 3.69}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.23, "draw": 7.27, "home": 11.5}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:10Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.07, "home_away": 1.13, "home_draw": 4.39}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 11.50 |
| Reference draw odds | 7.27 |
| Reference away odds | 1.23 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.91 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:44Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:44Z |
| Home probability edge | -0.4% |
| Draw probability edge | -0.8% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | -0.0146 |
| Raw ev home | -0.3054 |
| Raw edge prob draw | -0.0275 |
| Raw ev draw | -0.3091 |
| Raw edge prob away | 0.0422 |
| Raw ev away | 0.0733 |
| Market p home draw | 22.6% |
| Market home draw odds | 4.39 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:10Z |
| Market reference home draw last update utc | 2026-11-04T10:20:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.7% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:25Z |
| Market reference draw away last update utc | 2026-11-04T10:20:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.6% |
| Market home away odds | 1.13 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T10:20:10Z |
| Market reference home away last update utc | 2026-11-04T10:20:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.25 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 92.2% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T10:19:44Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 8.50 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:06Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 42.6% |
| Market under 3 5 odds | 2.24 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market reference under 3 5 odds | 2.24 |
| Market reference under 3 5 opposite odds | 1.69 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,433.7048 |
| Elo away rating | 1,551.6587 |
| Elo rating diff | -57.9539 |
| Elo home expectancy | 0.4174 |

</details>


---

## 2026-11-04 — Borussia Dortmund vs Real Betis

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **56.2%**. Expected goals are 2.15 for Borussia Dortmund and 1.51 for Real Betis (3.66 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 63.9%; Under 3.5 goals: 57.9%; Double Chance 1X: 77.8%; Double Chance X2: 43.8%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 76.3%; BTTS Yes (both teams score): 63.0%; BTTS No (at least one team does not score): 37.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 56.2% | 1.78 |
| Draw | 21.6% | 4.63 |
| Real Betis win | 22.2% | 4.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.15 |
| Real Betis expected goals | 1.51 |
| Expected total goals | 3.66 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 83.8% |
| Under 1.5 | 16.2% |
| Over 2.5 | 63.9% |
| Under 2.5 | 36.1% |
| Over 3.5 | 42.1% |
| Under 3.5 | 57.9% |
| Over 4.5 | 23.7% |
| Under 4.5 | 76.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.32% |
| 2 | 1-1 | 9.48% |
| 3 | 1-0 | 8.40% |
| 4 | 2-0 | 7.60% |
| 5 | 3-1 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 56.2% | 57.7% | 1.75 | -1.7% |
| Draw | 21.6% | 22.3% | 4.25 | -8.3% |
| Real Betis win | 22.2% | 20.0% | 4.82 | +7.1% |

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
| Market best home last update utc | 2026-11-04T10:19:25Z |
| Market best draw last update utc | 2026-11-04T10:19:25Z |
| Market best away last update utc | 2026-11-04T10:19:25Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Borussia Dortmund |
| Matched away-team name | Real Betis Balompié |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1475 |
| Dc lambda away | 1.5093 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:20:15.005079+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.0% |
| P btts no | 37.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.27 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.18 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.77 |
| Fair Over 3.5 odds | 2.38 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.22 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.12795459538507126, "-10": 2.2449719212868078e-07, "-11": 2.7185167800853457e-08, "-12": 3.026434286932802e-09, "-13": 3.117156785182376e-10, "-14": 2.985058478364378e-11, "-15": 2.645178298663496e-12, "-16": 1.9288596631029694e-13, "-2": 0.06164081467375241, "-3": 0.023349996125175607, "-4": 0.007070747628624258, "-5": 0.001774090532945146, "-6": 0.0003789090666034229, "-7": 7.032965459952852e-05, "-8": 1.153052995535002e-05, "-9": 1.6917297258288855e-06, "0": 0.21584667589781548, "1": 0.24366260130767678, "10": 1.0313049133997243e-05, "11": 1.7769194002173685e-06, "12": 2.8146636017532504e-07, "13": 4.124900080052469e-08, "14": 5.6203992504959435e-09, "15": 7.086451388121248e-10, "16": 7.35248301474391e-11, "2": 0.16856532516959746, "3": 0.0908544540778451, "4": 0.03914571991634873, "5": 0.013975078750889717, "6": 0.004246909635786034, "7": 0.0011215949498629065, "8": 0.0002616413411328001, "9": 5.461948692941773e-05} |
| Raw goal margin distribution | {"-1": 0.15127883396593955, "-10": 5.839012754783021e-07, "-11": 7.823487968654704e-08, "-12": 9.64320057186905e-09, "-13": 1.1002850600107455e-09, "-14": 1.1683452606031546e-10, "-15": 1.1590304417919855e-11, "-16": 1.0653973340041758e-12, "-17": 7.944264510150995e-14, "-2": 0.07723462905109213, "-3": 0.03145205392196061, "-4": 0.010344633199731093, "-5": 0.0028370303881877215, "-6": 0.0006650371187021586, "-7": 0.0001358574855833906, "-8": 2.4563133239536674e-05, "-9": 3.979959366156855e-06, "0": 0.19898453306123445, "1": 0.21347829788823836, "10": 1.9857967687652492e-05, "11": 3.7857796495953053e-06, "12": 6.639504212632914e-07, "13": 1.077901818248616e-07, "14": 1.6285636134584182e-08, "15": 2.298729696929554e-09, "16": 3.006520759429791e-10, "17": 3.1898174877280287e-11, "2": 0.15636197241788713, "3": 0.09059988038238193, "4": 0.042398768885183194, "5": 0.016544805864392297, "6": 0.005518272101229135, "7": 0.0016039851217853796, "8": 0.00041262930140960547, "9": 9.512933838912005e-05} |
| Unadjusted home-win probability | 52.7% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 68.4% |
| P home draw | 77.8% |
| P draw away | 43.8% |
| P home away | 78.4% |
| Raw p home draw | 72.6% |
| Raw p draw away | 47.3% |
| Raw p home away | 80.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8998 |
| Totals anchor target over 2 5 | 0.6395 |
| Totals anchor reference over odds | 1.52 |
| Totals anchor reference under odds | 2.60 |
| Totals anchor reference last update utc | 2026-11-04T10:20:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7044 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.25, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 9.15, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.01, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.32, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 5.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.13, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.63, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.31, "price": 3.63, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.82, "draw": 4.25, "home": 1.75}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.21, "home_away": 1.26, "home_draw": 1.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.5, "under": 2.57}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.72, "draw": 4.25, "home": 1.7}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.52, "under": 2.6}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.24, "home_away": 1.25, "home_draw": 1.22}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.70 |
| Reference draw odds | 4.25 |
| Reference away odds | 4.72 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.66 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:44Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:44Z |
| Home probability edge | -1.5% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | -0.0498 |
| Raw ev home | -0.0777 |
| Raw edge prob draw | -0.0241 |
| Raw ev draw | -0.1543 |
| Raw edge prob away | 0.0739 |
| Raw ev away | 0.3206 |
| Market p home draw | 79.3% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:25Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.2% |
| Market draw away odds | 2.24 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:20:11Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.4% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:25Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.24 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 86.0% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:06Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.2% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference under 3 5 odds | 1.67 |
| Market reference under 3 5 opposite odds | 2.28 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,519.4389 |
| Elo away rating | 1,458.2663 |
| Elo rating diff | 121.1726 |
| Elo home expectancy | 0.6676 |

</details>


---

## 2026-11-04 — Fenerbahce vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **75.3%**. Expected goals are 0.57 for Fenerbahce and 3.69 for Liverpool (4.25 combined). The most likely exact score is 0-3 at 10.2%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 71.9%; Under 3.5 goals: 46.4%; Double Chance 1X: 24.7%; Double Chance X2: 89.4%; Double Chance 12 (either team wins): 85.9%; Under 4.5 goals: 65.2%; BTTS Yes (both teams score): 45.2%; BTTS No (at least one team does not score): 54.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 10.6% | 9.40 |
| Draw | 14.1% | 7.10 |
| Liverpool win | 75.3% | 1.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 0.57 |
| Liverpool expected goals | 3.69 |
| Expected total goals | 4.25 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 88.0% |
| Under 1.5 | 12.0% |
| Over 2.5 | 71.9% |
| Under 2.5 | 28.1% |
| Over 3.5 | 53.6% |
| Under 3.5 | 46.4% |
| Over 4.5 | 34.8% |
| Under 4.5 | 65.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 10.17% |
| 2 | 0-4 | 9.12% |
| 3 | 0-2 | 8.51% |
| 4 | 1-1 | 6.62% |
| 5 | 0-5 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 10.6% | 14.1% | 6.58 | -30.0% |
| Draw | 14.1% | 17.5% | 5.32 | -25.0% |
| Liverpool win | 75.3% | 68.4% | 1.50 | +12.9% |

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
| Market best home last update utc | 2026-11-04T10:20:05Z |
| Market best draw last update utc | 2026-11-04T10:20:05Z |
| Market best away last update utc | 2026-11-04T10:19:25Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Fenerbahçe SK |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.5666 |
| Dc lambda away | 3.6881 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:20:15.005079+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 45.2% |
| P btts no | 54.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.48 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.31 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.56 |
| Fair Over 3.5 odds | 1.87 |
| Fair Under 3.5 odds | 2.15 |
| Fair Over 4.5 odds | 2.88 |
| Fair Under 4.5 odds | 1.53 |
| Goal margin distribution | {"-1": 0.11385056845578152, "-10": 0.0015343707095558006, "-11": 0.0004930066474663774, "-12": 0.00014552981554342328, "-13": 3.972384539996725e-05, "-14": 1.0082729294163194e-05, "-15": 2.391336808714991e-06, "-16": 5.322145613183659e-07, "-17": 1.1157013804730872e-07, "-18": 2.2104190632512144e-08, "-19": 4.15063227461926e-09, "-2": 0.1569103501786127, "-20": 7.380343485777416e-10, "-21": 1.152084988640635e-10, "-3": 0.16302764509625148, "-4": 0.13374762920094302, "-5": 0.09025420286109545, "-6": 0.05160418548441438, "-7": 0.02556238609657263, "-8": 0.011160561003877495, "-9": 0.0043537370536586685, "0": 0.14093085220803278, "1": 0.08610294207740805, "10": 5.2056161982657596e-11, "11": 2.5697624037703538e-12, "12": 1.1654416238776777e-13, "13": 4.8875158543224515e-15, "14": 1.9059581199237086e-16, "15": 6.94503350576896e-18, "16": 2.374754390532276e-19, "17": 7.648535156622583e-21, "18": 2.328108756920999e-22, "19": 6.716472731950976e-24, "2": 0.0171477299734851, "20": 1.8348557277935023e-25, "21": 4.400562721520544e-27, "3": 0.0027372511686237565, "4": 0.0003450148889300442, "5": 3.576988383043788e-05, "6": 3.1421967321774917e-06, "7": 2.391377756916607e-07, "8": 1.604099010961344e-08, "9": 9.614034839055056e-10} |
| Raw goal margin distribution | {"-1": 0.13129855743140456, "-10": 0.002199570301538354, "-11": 0.0007261338353372054, "-12": 0.00022025489283343264, "-13": 6.178412368843135e-05, "-14": 1.6117210739375788e-05, "-15": 3.928860654260213e-06, "-16": 8.987726737878251e-07, "-17": 1.9367238537374033e-07, "-18": 3.9442886762609916e-08, "-19": 7.614622235669652e-09, "-2": 0.1840557980858504, "-20": 1.3970799390219845e-09, "-21": 2.4330640716554165e-10, "-22": 3.7249885498129236e-11, "-3": 0.19529697275064956, "-4": 0.1640010582500627, "-5": 0.11343139819585234, "-6": 0.06653028180010001, "-7": 0.03382560669360441, "-8": 0.015163782873747571, "-9": 0.006075497502323187, "0": 0.06050932041603123, "1": 0.021427938905077496, "10": 1.6118378461845644e-11, "11": 8.175202625873485e-13, "12": 3.8098314865728866e-14, "13": 1.6419330448288287e-15, "14": 6.580619602280035e-17, "15": 2.4645740891912216e-18, "16": 8.662105367884435e-20, "17": 2.8677392097533106e-21, "18": 8.97302743644332e-23, "19": 2.661442058866502e-24, "2": 0.004344564041536356, "20": 7.502193471107698e-26, "21": 2.0073305722185523e-27, "22": 4.721594058780958e-29, "3": 0.0007082564885888033, "4": 9.137766392053463e-05, "5": 9.710129818398929e-06, "6": 8.750028426858581e-07, "7": 6.83492960422512e-08, "8": 4.707543681514391e-09, "9": 2.897790592097581e-10} |
| Unadjusted home-win probability | 2.7% |
| Unadjusted draw probability | 6.1% |
| Unadjusted away-win probability | 91.3% |
| Raw p over 1 5 | 92.4% |
| Raw p under 3 5 | 38.5% |
| Raw p btts yes | 42.0% |
| P home draw | 24.7% |
| P draw away | 89.4% |
| P home away | 85.9% |
| Raw p home draw | 8.7% |
| Raw p draw away | 97.3% |
| Raw p home away | 93.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9725 |
| Totals anchor target over 2 5 | 0.7192 |
| Totals anchor reference over odds | 1.36 |
| Totals anchor reference under odds | 3.27 |
| Totals anchor reference last update utc | 2026-11-04T10:20:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7335 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.67, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:32Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.34, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:32Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.18, "price": 5.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.72, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:15:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.38, "under": 3.04}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.5, "draw": 5.18, "home": 6.35}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.15, "home_away": 1.2, "home_draw": 2.77}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:32Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.14, "home_away": 1.18, "home_draw": 2.98}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.44, "draw": 5.32, "home": 6.58}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.36, "under": 3.27}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.58 |
| Reference draw odds | 5.32 |
| Reference away odds | 1.44 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.26 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:44Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:44Z |
| Home probability edge | -3.4% |
| Draw probability edge | -3.4% |
| Away probability edge | +6.9% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.1140 |
| Raw ev home | -0.8251 |
| Raw edge prob draw | -0.1149 |
| Raw ev draw | -0.6781 |
| Raw edge prob away | 0.2289 |
| Raw ev away | 0.3694 |
| Market p home draw | 34.6% |
| Market home draw odds | 2.98 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:19:32Z |
| Market reference home draw last update utc | 2026-11-04T10:20:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.5% |
| Market draw away odds | 1.15 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:25Z |
| Market reference draw away last update utc | 2026-11-04T10:20:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.9% |
| Market home away odds | 1.20 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:25Z |
| Market reference home away last update utc | 2026-11-04T10:20:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.78 |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T10:15:05Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:06Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.3% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market reference under 3 5 odds | 1.97 |
| Market reference under 3 5 opposite odds | 1.92 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,424.2185 |
| Elo away rating | 1,539.7264 |
| Elo rating diff | -55.5079 |
| Elo home expectancy | 0.4208 |

</details>


---

## 2026-11-04 — PSV Eindhoven vs Club Brugge

The model's most likely 1X2 outcome is **PSV Eindhoven win** at **51.2%**. Expected goals are 2.45 for PSV Eindhoven and 1.90 for Club Brugge (4.35 combined). The most likely exact score is 2-1 at 9.2%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.1%; Under 3.5 goals: 50.9%; Double Chance 1X: 71.9%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 70.2%; BTTS Yes (both teams score): 68.7%; BTTS No (at least one team does not score): 31.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PSV Eindhoven win | 51.2% | 1.95 |
| Draw | 20.7% | 4.83 |
| Club Brugge win | 28.1% | 3.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| PSV Eindhoven expected goals | 2.45 |
| Club Brugge expected goals | 1.90 |
| Expected total goals | 4.35 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.3% |
| Under 1.5 | 12.7% |
| Over 2.5 | 70.1% |
| Under 2.5 | 29.9% |
| Over 3.5 | 49.1% |
| Under 3.5 | 50.9% |
| Over 4.5 | 29.8% |
| Under 4.5 | 70.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.19% |
| 2 | 1-1 | 8.29% |
| 3 | 2-2 | 7.05% |
| 4 | 1-2 | 6.27% |
| 5 | 3-1 | 6.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 51.2% | 51.3% | 2.02 | +3.4% |
| Draw | 20.7% | 21.6% | 4.42 | -8.4% |
| Club Brugge win | 28.1% | 27.1% | 3.55 | -0.3% |

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
| Market best home last update utc | 2026-11-04T10:19:25Z |
| Market best draw last update utc | 2026-11-04T10:19:25Z |
| Market best away last update utc | 2026-11-04T10:20:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | PSV |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.4550 |
| Dc lambda away | 1.8977 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:20:15.005079+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 68.7% |
| P btts no | 31.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.11 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.88 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.35 |
| Fair Over 3.5 odds | 2.04 |
| Fair Under 3.5 odds | 1.96 |
| Fair Over 4.5 odds | 3.35 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.15002924047603425, "-10": 8.770327377148775e-07, "-11": 1.2300687352375062e-07, "-12": 1.5870734452507862e-08, "-13": 1.89549812585759e-09, "-14": 2.1068240390770206e-10, "-15": 2.1877208292732776e-11, "-16": 2.1051611887978708e-12, "-17": 1.6440421417285103e-13, "-2": 0.08034961141670877, "-3": 0.03427047059911361, "-4": 0.011803180186542191, "-5": 0.0033892744753952404, "-6": 0.0008317867711743785, "-7": 0.00017788888968153435, "-8": 3.3669056331826294e-05, "-9": 5.71077636607201e-06, "0": 0.20715113398258747, "1": 0.21839060156686532, "10": 1.3036758561740562e-05, "11": 2.3654520292395346e-06, "12": 3.9483235790849543e-07, "13": 6.100564440972556e-08, "14": 8.772146418833024e-09, "15": 1.1784209533475293e-09, "16": 1.4669822407186442e-10, "17": 1.482120091536402e-11, "2": 0.15222641501655715, "3": 0.08399573881277962, "4": 0.037425462040846326, "5": 0.01390291353791176, "6": 0.004414098674174396, "7": 0.0012212646881706068, "8": 0.0002990355816272744, "9": 6.561724977919997e-05} |
| Raw goal margin distribution | {"-1": 0.150353114780193, "-10": 3.257720883363229e-06, "-11": 5.433703632796262e-07, "-12": 8.3495245080802e-08, "-13": 1.189025426249446e-08, "-14": 1.5773396471682536e-09, "-15": 1.9578211398196275e-10, "-16": 2.2785472463860508e-11, "-17": 2.4450251781460096e-12, "-18": 2.0477005146281103e-13, "-2": 0.08809119046459683, "-3": 0.04213738537544397, "-4": 0.016600947554262967, "-5": 0.00552292774728307, "-6": 0.0015838565894964937, "-7": 0.000398173452905846, "-8": 8.896601511262204e-05, "-9": 1.786997522452254e-05, "0": 0.18561645590629403, "1": 0.19363000727112167, "10": 4.2778282606172516e-05, "11": 9.23073680100258e-06, "12": 1.8349875071130796e-06, "13": 3.380597430904939e-07, "14": 5.8017429388076804e-08, "15": 9.316166111208455e-09, "16": 1.4026625299784212e-09, "17": 1.9471949763464439e-10, "18": 2.1097135464395643e-11, "2": 0.1474328883142407, "3": 0.09123477936957029, "4": 0.046500397660773254, "5": 0.020013548516712394, "6": 0.007425086882656741, "7": 0.002414843178568537, "8": 0.0006980261891371581, "9": 0.0001813854623709744} |
| Unadjusted home-win probability | 51.0% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 30.5% |
| Raw p over 1 5 | 92.8% |
| Raw p under 3 5 | 36.8% |
| Raw p btts yes | 77.4% |
| P home draw | 71.9% |
| P draw away | 48.8% |
| P home away | 79.3% |
| Raw p home draw | 69.5% |
| Raw p draw away | 49.0% |
| Raw p home away | 81.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8325 |
| Totals anchor target over 2 5 | 0.7013 |
| Totals anchor reference over odds | 1.39 |
| Totals anchor reference under odds | 3.07 |
| Totals anchor reference last update utc | 2026-11-04T10:20:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8050 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.89, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.71, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.08, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.3, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:13Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.76, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:13Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.48, "price": 2.76, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:16Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.36, "under": 3.13}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 4.42, "home": 2.02}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.88, "home_away": 1.25, "home_draw": 1.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.55, "draw": 4.41, "home": 1.91}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.39, "under": 3.07}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:13Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.96, "home_away": 1.24, "home_draw": 1.33}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.91 |
| Reference draw odds | 4.41 |
| Reference away odds | 3.55 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.13 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:44Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:44Z |
| Home probability edge | -0.1% |
| Draw probability edge | -0.9% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0034 |
| Raw ev home | 0.0294 |
| Raw edge prob draw | -0.0308 |
| Raw ev draw | -0.1796 |
| Raw edge prob away | 0.0342 |
| Raw ev away | 0.0820 |
| Market p home draw | 72.7% |
| Market home draw odds | 1.37 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:25Z |
| Market reference home draw last update utc | 2026-11-04T10:20:13Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.3% |
| Market draw away odds | 1.96 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:20:13Z |
| Market reference draw away last update utc | 2026-11-04T10:20:13Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.0% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:25Z |
| Market reference home away last update utc | 2026-11-04T10:20:13Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.96 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T10:19:16Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:06Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 50.8% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-04T10:19:16Z |
| Market reference under 3 5 odds | 1.81 |
| Market reference under 3 5 opposite odds | 1.86 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,466.3756 |
| Elo away rating | 1,460.8471 |
| Elo rating diff | 65.5285 |
| Elo home expectancy | 0.5932 |

</details>


---

## 2026-11-04 — Porto vs Napoli

The model's most likely 1X2 outcome is **Porto win** at **52.8%**. Expected goals are 1.64 for Porto and 0.98 for Napoli (2.62 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 56.6%; Under 3.5 goals: 65.0%; Double Chance 1X: 77.0%; Double Chance X2: 47.2%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 52.8% | 1.90 |
| Draw | 24.3% | 4.12 |
| Napoli win | 23.0% | 4.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 1.64 |
| Napoli expected goals | 0.98 |
| Expected total goals | 2.62 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 79.4% |
| Under 1.5 | 20.6% |
| Over 2.5 | 56.6% |
| Under 2.5 | 43.4% |
| Over 3.5 | 35.0% |
| Under 3.5 | 65.0% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.30% |
| 2 | 1-0 | 9.40% |
| 3 | 2-1 | 9.35% |
| 4 | 2-0 | 8.36% |
| 5 | 2-2 | 6.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 52.8% | 52.5% | 1.92 | +1.3% |
| Draw | 24.3% | 24.7% | 3.92 | -4.8% |
| Napoli win | 23.0% | 22.9% | 4.18 | -4.1% |
| Over 2.5 | 56.6% | 55.8% | 1.77 | +0.2% |
| Under 2.5 | 43.4% | 44.2% | 2.22 | -3.7% |

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
| Market best home last update utc | 2026-11-04T10:19:25Z |
| Market best draw last update utc | 2026-11-04T10:19:25Z |
| Market best away last update utc | 2026-11-04T10:20:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6437 |
| Dc lambda away | 0.9798 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:20:15.005079+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.73 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.86 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.86 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.57 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.14435681661864777, "-10": 5.1185240756825555e-08, "-11": 5.126325116426933e-09, "-12": 4.717397930641583e-10, "-13": 4.0145811477076965e-11, "-14": 3.1761884090477128e-12, "-15": 2.332391524310956e-13, "-16": 1.4418815817769154e-14, "-2": 0.059779524014043975, "-3": 0.01923241460066551, "-4": 0.004897938497704323, "-5": 0.0010275026614094583, "-6": 0.00018280428855846977, "-7": 2.819374732853796e-05, "-8": 3.834165421241813e-06, "-9": 4.660287178881131e-07, "0": 0.24279224190615595, "1": 0.22665276704326795, "10": 8.586679140375134e-06, "11": 1.4427485142070718e-06, "12": 2.2273630304370423e-07, "13": 3.180041157232856e-08, "14": 4.220877632259349e-09, "15": 5.199983491584021e-10, "16": 5.393045815738134e-11, "2": 0.15980887558746684, "3": 0.08625539353731082, "4": 0.03685273981041132, "5": 0.01297010267428235, "6": 0.0038712466610619275, "7": 0.0010016621706139116, "8": 0.00022853005296138745, "9": 4.660034791953888e-05} |
| Raw goal margin distribution | {"-1": 0.15176006330089067, "-10": 1.8852283117177515e-08, "-11": 1.659160688969415e-09, "-12": 1.3409535204037175e-10, "-13": 1.001669059134558e-11, "-14": 6.923585865520881e-13, "-15": 4.0839348987969035e-14, "-2": 0.05771066312131965, "-3": 0.016758784410739507, "-4": 0.0038130614248572487, "-5": 0.0007104289627039104, "-6": 0.00011184010680313159, "-7": 1.5225722324933408e-05, "-8": 1.824635837752888e-06, "-9": 1.9519589344101046e-07, "0": 0.23406394609440875, "1": 0.25064303163460494, "10": 3.3296915571802836e-06, "11": 4.916233548855453e-07, "12": 6.665945932826279e-08, "13": 8.353650977444755e-09, "14": 9.68695216163709e-10, "15": 9.586032299840479e-11, "2": 0.1624291886285112, "3": 0.07913243498815624, "4": 0.030205763804452317, "5": 0.009441493190666684, "6": 0.0024935702286456277, "7": 0.0005695160153590236, "8": 0.00011450072642179154, "9": 2.0549758536340974e-05} |
| Unadjusted home-win probability | 53.5% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 73.1% |
| Raw p under 3 5 | 73.1% |
| Raw p btts yes | 49.8% |
| P home draw | 77.0% |
| P draw away | 47.2% |
| P home away | 75.7% |
| Raw p home draw | 76.9% |
| Raw p draw away | 46.5% |
| Raw p home away | 76.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1421 |
| Totals anchor target over 2 5 | 0.5664 |
| Totals anchor reference over odds | 1.71 |
| Totals anchor reference under odds | 2.20 |
| Totals anchor reference last update utc | 2026-11-04T10:20:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4846 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.46, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.2, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.62, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.12, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 8.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:12Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.13, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:12Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.39, "price": 3.13, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:13Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.77, "under": 2.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.17, "draw": 3.92, "home": 1.92}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.77, "under": 2.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.98, "home_away": 1.3, "home_draw": 1.27}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.18, "draw": 3.89, "home": 1.87}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.2}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:12Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.01, "home_away": 1.29, "home_draw": 1.26}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.87 |
| Reference draw odds | 3.89 |
| Reference away odds | 4.18 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:25Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:25Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:25Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:25Z |
| Home probability edge | +0.3% |
| Draw probability edge | -0.4% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0105 |
| Raw ev home | 0.0273 |
| Raw edge prob draw | -0.0125 |
| Raw ev draw | -0.0825 |
| Raw edge prob away | 0.0020 |
| Raw ev away | -0.0349 |
| Market p home draw | 76.8% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:25Z |
| Market reference home draw last update utc | 2026-11-04T10:20:12Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.2% |
| Market draw away odds | 2.01 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:20:12Z |
| Market reference draw away last update utc | 2026-11-04T10:20:12Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:25Z |
| Market reference home away last update utc | 2026-11-04T10:20:12Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.26 |
| Market reference dc draw away odds | 2.01 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T10:17:13Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:06Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.2% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,455.3386 |
| Elo away rating | 1,429.7462 |
| Elo rating diff | 85.5924 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-04 — RB Leipzig vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **58.9%**. Expected goals are 1.24 for RB Leipzig and 1.76 for Manchester City (3.01 combined). The most likely exact score is 1-2 at 9.4%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 74.6%; Under 3.5 goals: 45.0%; Double Chance 1X: 41.1%; Double Chance X2: 79.2%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 64.9%; BTTS Yes (both teams score): 71.5%; BTTS No (at least one team does not score): 28.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 20.8% | 4.80 |
| Draw | 20.3% | 4.93 |
| Manchester City win | 58.9% | 1.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.24 |
| Manchester City expected goals | 1.76 |
| Expected total goals | 3.01 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 89.9% |
| Under 1.5 | 10.1% |
| Over 2.5 | 74.6% |
| Under 2.5 | 25.4% |
| Over 3.5 | 55.0% |
| Under 3.5 | 45.0% |
| Over 4.5 | 35.1% |
| Under 4.5 | 64.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.43% |
| 2 | 1-1 | 7.50% |
| 3 | 2-2 | 7.26% |
| 4 | 1-3 | 7.19% |
| 5 | 0-2 | 5.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 20.8% | 18.0% | 5.38 | +12.1% |
| Draw | 20.3% | 19.4% | 5.03 | +1.9% |
| Manchester City win | 58.9% | 62.6% | 1.58 | -6.9% |

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
| Market best home last update utc | 2026-11-04T10:19:25Z |
| Market best draw last update utc | 2026-11-04T10:19:25Z |
| Market best away last update utc | 2026-11-04T10:19:25Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Manchester City FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2419 |
| Dc lambda away | 1.7646 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:20:15.005079+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 71.5% |
| P btts no | 28.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 57.04 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.92 |
| Fair Over 2.5 odds | 1.34 |
| Fair Under 2.5 odds | 3.93 |
| Fair Over 3.5 odds | 1.82 |
| Fair Under 3.5 odds | 2.22 |
| Fair Over 4.5 odds | 2.85 |
| Fair Under 4.5 odds | 1.54 |
| Goal margin distribution | {"-1": 0.22898633580434236, "-10": 3.345496378684649e-05, "-11": 6.766653101745343e-06, "-12": 1.2596263905277134e-06, "-13": 2.1713471728481244e-07, "-14": 3.4845307786244616e-08, "-15": 5.22973422377783e-09, "-16": 7.363320756541761e-10, "-17": 9.626513795752839e-11, "-18": 1.0149733832836445e-11, "-2": 0.17301357785330115, "-3": 0.10436300465474797, "-4": 0.05117835639668191, "-5": 0.021013916984011012, "-6": 0.007395165587655807, "-7": 0.0022722741005486175, "-8": 0.0006187529247014825, "-9": 0.0001511454906683718, "0": 0.20268316319622437, "1": 0.1120669882721086, "10": 6.887306893934172e-07, "11": 9.804596795325496e-08, "12": 1.2845899840989199e-08, "13": 1.5585437674685789e-09, "14": 1.7603579859839524e-10, "15": 1.8595303157210508e-11, "16": 1.8427410839300586e-12, "17": 1.6956124293094453e-13, "18": 1.2582854129949719e-14, "2": 0.05914709526140702, "3": 0.025111159271469854, "4": 0.008667093415528423, "5": 0.0025047311106794505, "6": 0.000620395951927775, "7": 0.0001341679319256912, "8": 2.5714153175294292e-05, "9": 4.420965352507548e-06} |
| Raw goal margin distribution | {"-1": 0.2304061134773183, "-10": 4.860849076581296e-06, "-11": 7.671886451660404e-07, "-12": 1.1126785155106714e-07, "-13": 1.492490307745718e-08, "-14": 1.8611939389875552e-09, "-15": 2.1532184208987628e-10, "-16": 2.088605294188239e-11, "-2": 0.15114169909848751, "-3": 0.07626587229233897, "-4": 0.03051746053721362, "-5": 0.010069607321503913, "-6": 0.0028196667848520225, "-7": 0.0006847583719651448, "-8": 0.00014667689837028993, "-9": 2.808704395879491e-05, "0": 0.22304045100950312, "1": 0.16377167930360667, "10": 1.4500456795154457e-07, "11": 1.6107890466457877e-08, "12": 1.6442700959819793e-09, "13": 1.5523224206563407e-10, "14": 1.3624764203854535e-11, "15": 1.1094108439673355e-12, "16": 7.57404095595309e-14, "2": 0.0748717888475518, "3": 0.026590781775239505, "4": 0.007488868596829994, "5": 0.0017391911159176042, "6": 0.00034276740490332523, "7": 5.858764392214366e-05, "8": 8.83277881291299e-06, "9": 1.1904430557551842e-06} |
| Unadjusted home-win probability | 27.5% |
| Unadjusted draw probability | 22.3% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 58.4% |
| P home draw | 41.1% |
| P draw away | 79.2% |
| P home away | 79.7% |
| Raw p home draw | 49.8% |
| Raw p draw away | 72.5% |
| Raw p home away | 77.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2952 |
| Totals anchor target over 2 5 | 0.7455 |
| Totals anchor reference over odds | 1.31 |
| Totals anchor reference under odds | 3.52 |
| Totals anchor reference last update utc | 2026-11-04T10:20:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5877 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 6.42, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.04, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:16Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.16, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:16Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.25, "price": 4.16, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.58, "draw": 5.03, "home": 5.38}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.19, "home_away": 1.21, "home_draw": 2.53}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:40Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.3, "under": 3.44}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.57, "draw": 4.86, "home": 5.23}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.31, "under": 3.52}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:16Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.19, "home_away": 1.21, "home_draw": 2.53}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.23 |
| Reference draw odds | 4.86 |
| Reference away odds | 1.57 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.57 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:44Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:44Z |
| Home probability edge | +2.9% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0951 |
| Raw ev home | 0.4788 |
| Raw edge prob draw | 0.0291 |
| Raw ev draw | 0.1219 |
| Raw edge prob away | -0.1242 |
| Raw ev away | -0.2067 |
| Market p home draw | 38.3% |
| Market home draw odds | 2.53 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:25Z |
| Market reference home draw last update utc | 2026-11-04T10:20:16Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.5% |
| Market draw away odds | 1.19 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:25Z |
| Market reference draw away last update utc | 2026-11-04T10:20:16Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.2% |
| Market home away odds | 1.21 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:25Z |
| Market reference home away last update utc | 2026-11-04T10:20:16Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.53 |
| Market reference dc draw away odds | 1.19 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 91.3% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T10:19:40Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 8.00 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:06Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 46.0% |
| Market under 3 5 odds | 2.12 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-04T10:19:40Z |
| Market reference under 3 5 odds | 2.11 |
| Market reference under 3 5 opposite odds | 1.81 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,451.6590 |
| Elo away rating | 1,506.5247 |
| Elo rating diff | 5.1343 |
| Elo home expectancy | 0.5074 |

</details>


---

## 2026-11-04 — RC Lens vs Como

The model's most likely 1X2 outcome is **Como win** at **56.8%**. Expected goals are 1.35 for RC Lens and 3.13 for Como (4.48 combined). The most likely exact score is 1-1 at 9.8%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 60.8%; Under 3.5 goals: 60.9%; Double Chance 1X: 43.2%; Double Chance X2: 78.1%; Double Chance 12 (either team wins): 78.8%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 21.9% | 4.56 |
| Draw | 21.2% | 4.71 |
| Como win | 56.8% | 1.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.35 |
| Como expected goals | 3.13 |
| Expected total goals | 4.48 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.80% |
| 2 | 0-2 | 8.55% |
| 3 | 1-2 | 8.35% |
| 4 | 0-1 | 7.94% |
| 5 | 0-3 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 21.9% | 25.5% | 3.76 | -17.6% |
| Draw | 21.2% | 24.5% | 3.98 | -15.4% |
| Como win | 56.8% | 50.0% | 2.00 | +13.7% |

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
| Market best home last update utc | 2026-11-04T10:19:25Z |
| Market best draw last update utc | 2026-11-04T10:19:25Z |
| Market best away last update utc | 2026-11-04T10:19:25Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3528 |
| Dc lambda away | 3.1309 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:20:15.005079+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.02 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.50 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.69 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.19988806175298982, "-10": 3.899773774939635e-05, "-11": 7.878863667231726e-06, "-12": 1.4627553356264656e-06, "-13": 2.511683230685831e-07, "-14": 4.0109698662065743e-08, "-15": 5.984030706794968e-09, "-16": 8.323077747350466e-10, "-17": 9.790085002649525e-11, "-2": 0.16851535654511865, "-3": 0.10877253289625706, "-4": 0.05569079853932142, "-5": 0.023515810651157924, "-6": 0.008427513392704582, "-7": 0.002619516745492879, "-8": 0.0007182029238338244, "-9": 0.0001760382997643768, "0": 0.21249077436899694, "1": 0.14792163418502483, "10": 1.4783762807685473e-08, "11": 1.2904964329622304e-09, "12": 1.0351721154694833e-10, "13": 7.679861554926056e-12, "14": 5.298898190929546e-13, "15": 3.4156836489256366e-14, "16": 2.0526524877467986e-15, "17": 1.04319522901343e-16, "2": 0.0526021924875795, "3": 0.014670038560674883, "4": 0.00324521227500131, "5": 0.0005920621127146, "6": 9.16757387792564e-05, "7": 1.231186365330507e-05, "8": 1.4584697913321876e-06, "9": 1.5445610750578329e-07} |
| Raw goal margin distribution | {"-1": 0.1886831318871596, "-10": 0.00041150240473643285, "-11": 0.00011357619444672543, "-12": 2.8867075018570078e-05, "-13": 6.797277889115776e-06, "-14": 1.4905830100427004e-06, "-15": 3.058129318846931e-07, "-16": 5.8937014598106274e-08, "-17": 1.0707392798802804e-08, "-18": 1.8376024167658615e-09, "-19": 2.943699909909925e-10, "-2": 0.188861169667537, "-20": 3.802922079097846e-11, "-3": 0.15194523224437909, "-4": 0.10014820007792842, "-5": 0.055544261618171414, "-6": 0.026491305042533234, "-7": 0.011057215084214603, "-8": 0.004096889879344309, "-9": 0.001363382463022316, "0": 0.13631794533661365, "1": 0.08288116856423577, "10": 9.329296348839475e-08, "11": 1.1125293455694376e-08, "12": 1.2217281889179523e-09, "13": 1.2429523793631573e-10, "14": 1.1776691069677793e-11, "15": 1.0439281614608446e-12, "16": 8.692617131351698e-14, "17": 6.8232895984419056e-15, "18": 5.059519496695105e-16, "19": 3.5018610207210603e-17, "2": 0.03525640101720587, "20": 1.9546565070863896e-18, "3": 0.012255471678846698, "4": 0.0034900669076399432, "5": 0.000836329572194499, "6": 0.00017234125862066753, "7": 3.107987872425904e-05, "8": 4.9754858990607406e-06, "9": 7.153960924186671e-07} |
| Unadjusted home-win probability | 13.5% |
| Unadjusted draw probability | 13.6% |
| Unadjusted away-win probability | 72.9% |
| Raw p over 1 5 | 93.6% |
| Raw p under 3 5 | 34.5% |
| Raw p btts yes | 70.7% |
| P home draw | 43.2% |
| P draw away | 78.1% |
| P home away | 78.8% |
| Raw p home draw | 27.1% |
| Raw p draw away | 86.5% |
| Raw p home away | 86.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7215 |
| Totals anchor target over 2 5 | 0.6078 |
| Totals anchor reference over odds | 1.60 |
| Totals anchor reference under odds | 2.42 |
| Totals anchor reference last update utc | 2026-11-04T10:20:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7972 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:14Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.81, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:14Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.46, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.24, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.21, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.58, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.49, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.24, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.0, "draw": 3.98, "home": 3.76}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.32, "home_away": 1.29, "home_draw": 1.9}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.96, "draw": 3.91, "home": 3.76}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.6, "under": 2.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.3, "home_away": 1.28, "home_draw": 1.92}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:18Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.56, "under": 2.42}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.76 |
| Reference draw odds | 3.91 |
| Reference away odds | 1.96 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.41 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:44Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:44Z |
| Home probability edge | -3.6% |
| Draw probability edge | -3.3% |
| Away probability edge | +6.9% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.1203 |
| Raw ev home | -0.4927 |
| Raw edge prob draw | -0.1088 |
| Raw ev draw | -0.4575 |
| Raw edge prob away | 0.2291 |
| Raw ev away | 0.4575 |
| Market p home draw | 50.3% |
| Market home draw odds | 1.92 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:14Z |
| Market reference home draw last update utc | 2026-11-04T10:20:14Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.3% |
| Market draw away odds | 1.32 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:25Z |
| Market reference draw away last update utc | 2026-11-04T10:20:14Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:25Z |
| Market reference home away last update utc | 2026-11-04T10:20:14Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.92 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 84.7% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T10:20:18Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.84 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:18Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.0% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-04T10:20:18Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.45 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:18Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,454.3021 |
| Elo away rating | 1,441.7871 |
| Elo rating diff | 72.5150 |
| Elo home expectancy | 0.6029 |

</details>


---

## 2026-11-04 — Slavia Praha vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **82.6%**. Expected goals are 0.32 for Slavia Praha and 3.11 for Arsenal (3.43 combined). The most likely exact score is 0-2 at 16.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.6%; Under 3.5 goals: 64.9%; Double Chance 1X: 17.4%; Double Chance X2: 94.6%; Double Chance 12 (either team wins): 87.9%; Under 4.5 goals: 81.3%; BTTS Yes (both teams score): 24.5%; BTTS No (at least one team does not score): 75.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Slavia Praha win | 5.4% | 18.61 |
| Draw | 12.1% | 8.29 |
| Arsenal win | 82.6% | 1.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Slavia Praha expected goals | 0.32 |
| Arsenal expected goals | 3.11 |
| Expected total goals | 3.43 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 56.6% |
| Under 2.5 | 43.4% |
| Over 3.5 | 35.1% |
| Under 3.5 | 64.9% |
| Over 4.5 | 18.7% |
| Under 4.5 | 81.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 16.59% |
| 2 | 0-3 | 15.49% |
| 3 | 0-1 | 12.02% |
| 4 | 0-4 | 10.85% |
| 5 | 0-0 | 6.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Slavia Praha win | 5.4% | 6.8% | 12.72 | -31.6% |
| Draw | 12.1% | 14.2% | 6.60 | -20.4% |
| Arsenal win | 82.6% | 79.0% | 1.27 | +4.9% |
| Over 2.5 | 56.6% | 57.5% | 1.72 | -2.6% |
| Under 2.5 | 43.4% | 42.5% | 2.31 | +0.2% |

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
| Market best home last update utc | 2026-11-04T10:20:05Z |
| Market best draw last update utc | 2026-11-04T10:19:25Z |
| Market best away last update utc | 2026-11-04T10:19:25Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | SK Slavia Praha |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.3194 |
| Dc lambda away | 3.1122 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:20:15.005079+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 24.5% |
| P btts no | 75.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.44 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.65 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.35 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.17472309255460342, "-10": 0.0003725914544840635, "-11": 9.429974391172284e-05, "-12": 2.1897836073278278e-05, "-13": 4.697275082715321e-06, "-14": 9.361802921313774e-07, "-15": 1.7422718836755442e-07, "-16": 3.0409798546359386e-08, "-17": 4.9971085185587085e-09, "-18": 7.751230133328576e-10, "-19": 1.0961975916206947e-10, "-2": 0.21517967337932728, "-3": 0.1887139713033761, "-4": 0.12715436624041, "-5": 0.0694011767196041, "-6": 0.031796601680441, "-7": 0.012544344322170109, "-8": 0.004343784611422423, "-9": 0.0013399337702324663, "0": 0.12057143756659615, "1": 0.0476503461591121, "10": 1.18398223349649e-13, "11": 3.0757163040766897e-15, "12": 7.330952873963251e-17, "13": 1.614093495778599e-18, "14": 3.301913208958669e-20, "15": 6.307329990849152e-22, "16": 1.129969273483217e-23, "17": 1.9058790569118588e-25, "18": 3.034384799357021e-27, "19": 4.40465941113851e-29, "2": 0.005550419550113317, "3": 0.0004996341194466368, "4": 3.4554353962119206e-05, "5": 1.935805859566133e-06, "6": 9.103305935675455e-08, "7": 3.6862931056200308e-09, "8": 1.3101880866873483e-10, "9": 4.148319159888574e-12} |
| Raw goal margin distribution | {"-1": 0.16126918541617266, "-10": 0.0008311089443689065, "-11": 0.0002333953930779061, "-12": 6.0149525099276834e-05, "-13": 1.432185508746257e-05, "-14": 3.1687917858967845e-06, "-15": 6.547550594887458e-07, "-16": 1.268950625460416e-07, "-17": 2.315561151511792e-08, "-18": 3.991932217302878e-09, "-19": 6.514443540765467e-10, "-2": 0.21537639302924164, "-20": 9.657041991800957e-11, "-3": 0.20706384410366283, "-4": 0.15370453305549794, "-5": 0.09267020473529401, "-6": 0.04697500278699889, "-7": 0.020525500382388828, "-8": 0.007877300675738726, "-9": 0.002694457260863002, "0": 0.0701942587893319, "1": 0.017995226763416253, "10": 1.0786799723519186e-13, "11": 3.1092124957589195e-15, "12": 8.224581220451077e-17, "13": 2.0100382966809106e-18, "14": 4.56480496231534e-20, "15": 9.681236995961544e-22, "16": 1.925839893309845e-23, "17": 3.607075023383413e-25, "18": 6.3827163526631686e-27, "19": 1.0691119327035192e-28, "2": 0.0022690550434243274, "20": 1.6267223670026508e-30, "3": 0.00022391060844871173, "4": 1.706005942338187e-05, "5": 1.0557411561757933e-06, "6": 5.4929748430396686e-08, "7": 2.4635309046061254e-09, "8": 9.70432091879323e-11, "9": 3.407081265776627e-12} |
| Unadjusted home-win probability | 2.1% |
| Unadjusted draw probability | 7.0% |
| Unadjusted away-win probability | 90.9% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 55.1% |
| Raw p btts yes | 26.0% |
| P home draw | 17.4% |
| P draw away | 94.6% |
| P home away | 87.9% |
| Raw p home draw | 9.1% |
| Raw p draw away | 97.9% |
| Raw p home away | 93.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9000 |
| Totals anchor target over 2 5 | 0.5664 |
| Totals anchor reference over odds | 1.71 |
| Totals anchor reference under odds | 2.20 |
| Totals anchor reference last update utc | 2026-11-04T10:20:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6241 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 4.27, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 7.5, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.59, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 10.23, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.07, "price": 10.23, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.27, "draw": 6.6, "home": 12.5}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.31}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.05, "home_away": 1.14, "home_draw": 4.14}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.25, "draw": 6.33, "home": 12.72}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.2}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:10Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.06, "home_away": 1.15, "home_draw": 4.26}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 12.72 |
| Reference draw odds | 6.33 |
| Reference away odds | 1.25 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:25Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:25Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:25Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:25Z |
| Home probability edge | -1.4% |
| Draw probability edge | -2.2% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0475 |
| Raw ev home | -0.7392 |
| Raw edge prob draw | -0.0720 |
| Raw ev draw | -0.5367 |
| Raw edge prob away | 0.1194 |
| Raw ev away | 0.1548 |
| Market p home draw | 22.9% |
| Market home draw odds | 4.26 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:11Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 92.1% |
| Market draw away odds | 1.06 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:20:11Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.9% |
| Market home away odds | 1.15 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T10:20:11Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.26 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T10:20:10Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.31 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:10Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.0% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-04T10:20:10Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:10Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,396.4207 |
| Elo away rating | 1,607.4002 |
| Elo rating diff | -150.9796 |
| Elo home expectancy | 0.2954 |

</details>


---

## 2026-11-04 — Viking FK vs Sabah FK

The model's most likely 1X2 outcome is **Viking FK win** at **74.7%**. Expected goals are 3.67 for Viking FK and 0.95 for Sabah FK (4.62 combined). The most likely exact score is 3-0 at 8.9%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 73.4%; Under 3.5 goals: 45.9%; Double Chance 1X: 89.1%; Double Chance X2: 25.3%; Double Chance 12 (either team wins): 85.6%; Under 4.5 goals: 65.5%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 74.7% | 1.34 |
| Draw | 14.4% | 6.93 |
| Sabah FK win | 10.9% | 9.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 3.67 |
| Sabah FK expected goals | 0.95 |
| Expected total goals | 4.62 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 89.2% |
| Under 1.5 | 10.8% |
| Over 2.5 | 73.4% |
| Under 2.5 | 26.6% |
| Over 3.5 | 54.1% |
| Under 3.5 | 45.9% |
| Over 4.5 | 34.5% |
| Under 4.5 | 65.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 8.86% |
| 2 | 2-0 | 8.42% |
| 3 | 3-1 | 7.25% |
| 4 | 4-0 | 6.99% |
| 5 | 2-1 | 6.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 74.7% | 69.9% | 1.45 | +8.3% |
| Draw | 14.4% | 17.0% | 5.49 | -20.8% |
| Sabah FK win | 10.9% | 13.2% | 6.99 | -23.7% |

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
| Market best home last update utc | 2026-11-04T10:19:25Z |
| Market best draw last update utc | 2026-11-04T10:19:25Z |
| Market best away last update utc | 2026-11-04T10:20:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Viking FK |
| Matched away-team name | Sabah FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.6721 |
| Dc lambda away | 0.9514 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:20:15.005079+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.18 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.29 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.76 |
| Fair Over 3.5 odds | 1.85 |
| Fair Under 3.5 odds | 2.18 |
| Fair Over 4.5 odds | 2.89 |
| Fair Under 4.5 odds | 1.53 |
| Goal margin distribution | {"-1": 0.07994504041450387, "-10": 1.4478912233278238e-09, "-11": 1.0560855202314843e-10, "-12": 7.081430825349919e-12, "-13": 4.393060473947519e-13, "-14": 2.5352560098396063e-14, "-15": 1.3676041275612202e-15, "-16": 6.924763624447022e-17, "-17": 3.3034131942251603e-18, "-18": 1.4891691881219284e-19, "-19": 6.32235629843866e-21, "-2": 0.02281299939723411, "-20": 2.289618874463393e-22, "-3": 0.005216224056914252, "-4": 0.0009527031140925857, "-5": 0.00014410852689374944, "-6": 1.854989974440598e-05, "-7": 2.0746786327790694e-06, "-8": 2.0493041048461984e-07, "-9": 1.8112926165526495e-08, "0": 0.14428559649018605, "1": 0.16135390074828834, "10": 0.0005772087706254343, "11": 0.000162504620443568, "12": 4.2058839193703985e-05, "13": 1.0071011370554914e-05, "14": 2.243351699289038e-06, "15": 4.670953959175535e-07, "16": 9.128927891385724e-08, "17": 1.6809212279717957e-08, "18": 2.924813267476017e-09, "19": 4.792947907219903e-10, "2": 0.1845959883371872, "20": 6.69971884617182e-11, "3": 0.1629167534146239, "4": 0.11485151637476483, "5": 0.0670561271553956, "6": 0.03331654782267485, "7": 0.0143826496494847, "8": 0.005483579154994231, "9": 0.0018707509016758733} |
| Raw goal margin distribution | {"-1": 0.040183233099499185, "-10": 2.2485876097331953e-09, "-11": 1.8956565391692032e-10, "-12": 1.4705593085705397e-11, "-13": 1.0562337876458627e-12, "-14": 7.061769670504142e-14, "-15": 4.415404430797532e-15, "-16": 2.59248223716646e-16, "-17": 1.4346040855700772e-17, "-18": 7.506392433958164e-19, "-19": 3.7245281395824465e-20, "-2": 0.012488367163043137, "-20": 1.7561932861753638e-21, "-21": 7.81598821348394e-23, "-22": 2.9167583790752153e-24, "-3": 0.0031645131573455865, "-4": 0.0006501516917914903, "-5": 0.00011165063504859164, "-6": 1.641480899987105e-05, "-7": 2.1054413183795787e-06, "-8": 2.391949861295573e-07, "-9": 2.4367129458275603e-08, "0": 0.0852077815286143, "1": 0.1501961301697209, "10": 0.0016504645805060763, "11": 0.0005370635624386623, "12": 0.00016081191328223853, "13": 4.458259769806566e-05, "14": 1.150504977438117e-05, "15": 2.7766112708688972e-06, "16": 6.292598494975294e-07, "17": 1.3440515792582592e-07, "18": 2.7144683189850204e-08, "19": 5.198695865799618e-09, "2": 0.1860565388930743, "20": 9.461611318798817e-10, "21": 1.625347868824212e-10, "22": 2.341167701701599e-11, "3": 0.18197671640382726, "4": 0.14430894614441625, "5": 0.09565537867455733, "6": 0.05428172880646652, "7": 0.026873895143779258, "8": 0.011784446478319843, "9": 0.004633734288607488} |
| Unadjusted home-win probability | 85.8% |
| Unadjusted draw probability | 8.5% |
| Unadjusted away-win probability | 5.7% |
| Raw p over 1 5 | 94.3% |
| Raw p under 3 5 | 32.2% |
| Raw p btts yes | 59.6% |
| P home draw | 89.1% |
| P draw away | 25.3% |
| P home away | 85.6% |
| Raw p home draw | 94.3% |
| Raw p draw away | 14.2% |
| Raw p home away | 91.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8596 |
| Totals anchor target over 2 5 | 0.7340 |
| Totals anchor reference over odds | 1.33 |
| Totals anchor reference under odds | 3.39 |
| Totals anchor reference last update utc | 2026-11-04T10:20:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8108 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.34, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.44, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.64, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.17, "price": 5.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.89, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:12:18Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.35, "under": 3.17}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.98, "draw": 5.49, "home": 1.45}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:25Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.98, "home_away": 1.19, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.1, "home_away": 1.18, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.99, "draw": 5.48, "home": 1.41}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.33, "under": 3.39}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.41 |
| Reference draw odds | 5.48 |
| Reference away odds | 6.99 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:44Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:44Z |
| Home probability edge | +4.8% |
| Draw probability edge | -2.5% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.1594 |
| Raw ev home | 0.2444 |
| Raw edge prob draw | -0.0844 |
| Raw ev draw | -0.5322 |
| Raw edge prob away | -0.0750 |
| Raw ev away | -0.6042 |
| Market p home draw | 85.9% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:25Z |
| Market reference home draw last update utc | 2026-11-04T10:20:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 31.9% |
| Market draw away odds | 3.10 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:19:54Z |
| Market reference draw away last update utc | 2026-11-04T10:20:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.2% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:25Z |
| Market reference home away last update utc | 2026-11-04T10:20:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 3.02 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 91.2% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T10:12:18Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:06Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 47.7% |
| Market under 3 5 odds | 2.03 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market reference under 3 5 odds | 2.03 |
| Market reference under 3 5 opposite odds | 1.86 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:05Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,428.8826 |
| Elo away rating | 1,421.0274 |
| Elo rating diff | 67.8552 |
| Elo home expectancy | 0.5964 |

</details>


---
