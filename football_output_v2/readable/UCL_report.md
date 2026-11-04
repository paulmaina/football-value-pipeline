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
| Training as of utc | 2026-11-04T09:30:54.245100+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 9, 'bbs_rows_with_statistics': 42, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 52, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-04T09:30:54.245100+00:00', 'observations': 383, 'observations_sha256': '2bd8823c03640db52bc36f82207c824a76b8bb870871ba41cbb7c737225f9963', 'eligible_training_matches': 16, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 94, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 2, 'retrospective_eligible_training_matches': 16, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': '1e3081e2153ab9f63d20d21a823216ae0eba79f5107f3b5f54e1f527881fa21e', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 835.967 |
| Base scoring parameter | 0.206 |
| Home-advantage parameter | 0.294 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 71, 'matches': 566, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-03'} |
| Training data health | {'completed_matches': 63, 'latest_completed_utc': '2026-11-03T20:00:00+00:00', 'latest_completed_date': '2026-11-03', 'next_fixture_utc': '2026-11-04T17:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-11-04T09:30:54.245100+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '936f6e47aadb3f3787783bc63a150534d5c0b8033d4d07c0cc14b54e0fe12b75', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0, 'training_end': '2026-11-03', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261104T093054245100Z_e9cfcde010454c88298529258ed59fba619358bed2d36b20bf302f93e54a4b43.json |
| Over 1 5 in window quote fixtures | 1 |
| Odds provider health | — |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 8, 'ANCHORED_ALTERNATE': 1} |
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

The model's most likely 1X2 outcome is **Real Madrid win** at **81.5%**. Expected goals are 0.86 for AEK Athens and 3.38 for Real Madrid (4.24 combined). The most likely exact score is 0-3 at 8.9%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 78.6%; Under 3.5 goals: 39.4%; Double Chance 1X: 18.5%; Double Chance X2: 92.9%; Double Chance 12 (either team wins): 88.6%; Under 4.5 goals: 59.0%; BTTS Yes (both teams score): 56.5%; BTTS No (at least one team does not score): 43.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AEK Athens win | 7.1% | 14.08 |
| Draw | 11.4% | 8.77 |
| Real Madrid win | 81.5% | 1.23 |

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
| 1 | 0-3 | 8.91% |
| 2 | 0-2 | 7.91% |
| 3 | 1-3 | 7.69% |
| 4 | 0-4 | 7.53% |
| 5 | 1-2 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AEK Athens win | 7.1% | 7.6% | 11.28 | -19.9% |
| Draw | 11.4% | 12.2% | 7.31 | -16.6% |
| Real Madrid win | 81.5% | 80.2% | 1.27 | +3.5% |

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
| Market best home last update utc | 2026-11-04T09:30:50Z |
| Market best draw last update utc | 2026-11-04T09:30:04Z |
| Market best away last update utc | 2026-11-04T09:30:04Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | PAE AEK |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8632 |
| Dc lambda away | 3.3814 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:30:54.245100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 67.63 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.41 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.67 |
| Fair Over 3.5 odds | 1.65 |
| Fair Under 3.5 odds | 2.54 |
| Fair Over 4.5 odds | 2.44 |
| Fair Under 4.5 odds | 1.69 |
| Goal margin distribution | {"-1": 0.15960327851192707, "-10": 0.0009682202850743997, "-11": 0.000291303005581369, "-12": 8.05989328537756e-05, "-13": 2.0637691318239077e-05, "-14": 4.917010101988323e-06, "-15": 1.095233616275505e-06, "-16": 2.2902682013933137e-07, "-17": 4.512743493951922e-08, "-18": 8.406025400402934e-09, "-19": 1.4840933794343567e-09, "-2": 0.1902331410923848, "-20": 2.472035502575663e-10, "-21": 3.494692033522406e-11, "-3": 0.17654146464718096, "-4": 0.13163403343633956, "-5": 0.08157650515976607, "-6": 0.043119865793845295, "-7": 0.019834450978219353, "-8": 0.008066459151981757, "-9": 0.002937764682917523, "0": 0.11407982194780635, "1": 0.05150607172232794, "10": 1.387100991691004e-09, "11": 1.0653309058524491e-10, "12": 7.524445626734322e-12, "13": 4.918265673897582e-13, "14": 2.9912838668217916e-14, "15": 1.7008614936872815e-15, "16": 9.079337977437207e-17, "17": 4.5668226276546835e-18, "18": 2.1715500788605137e-19, "19": 9.786919918812438e-21, "2": 0.015113840602542587, "20": 4.161454652576491e-22, "21": 1.501775547101327e-23, "3": 0.003580478249086823, "4": 0.0006815036075168636, "5": 0.00010781289842465344, "6": 1.4547510599975546e-05, "7": 1.7081937213114544e-06, "8": 1.7733952149870725e-07, "9": 1.6487137303780983e-08} |
| Raw goal margin distribution | {"-1": 0.16551505938382424, "-10": 0.0010040836220587834, "-11": 0.00030209300659123794, "-12": 8.358435542142464e-05, "-13": 2.140212115898428e-05, "-14": 5.0991384801700265e-06, "-15": 1.1358015870798923e-06, "-16": 2.3751008180585133e-07, "-17": 4.679897645897052e-08, "-18": 8.717388554306258e-09, "-19": 1.539064899659072e-09, "-2": 0.19727946655133732, "-20": 2.563600865988204e-10, "-21": 3.624137078195504e-11, "-3": 0.18308064393929005, "-4": 0.13650982025109146, "-5": 0.0845981374676744, "-6": 0.04471704600327175, "-7": 0.020569128417122072, "-8": 0.008365244611549008, "-9": 0.0030465808752948567, "0": 0.09450431771265025, "1": 0.04381035649109349, "10": 1.1798490333866522e-09, "11": 9.061558221327668e-11, "12": 6.400190002495898e-12, "13": 4.183409164903451e-13, "14": 2.5443449323414292e-14, "15": 1.4467294027416782e-15, "16": 7.722760059028429e-17, "17": 3.884476541479509e-18, "18": 1.8470906421679124e-19, "19": 8.324619530382181e-21, "2": 0.01285562502837727, "20": 3.5396761149591216e-22, "21": 1.2773896336496307e-23, "3": 0.0030455055735322182, "4": 0.0005796775991040498, "5": 9.17041691664199e-05, "6": 1.2373912514213463e-05, "7": 1.452966094753847e-06, "8": 1.508425588870972e-07, "9": 1.402373232208912e-08} |
| Unadjusted home-win probability | 6.0% |
| Unadjusted draw probability | 9.5% |
| Unadjusted away-win probability | 84.5% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 38.7% |
| Raw p btts yes | 55.6% |
| P home draw | 18.5% |
| P draw away | 92.9% |
| P home away | 88.6% |
| Raw p home draw | 15.5% |
| Raw p draw away | 94.0% |
| Raw p home away | 90.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7861 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 6.52, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:57Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 9.62, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:57Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.08, "price": 9.62, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.27, "draw": 7.31, "home": 10.9}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.07, "home_away": 1.12, "home_draw": 4.18}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:43Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.28, "under": 3.69}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.23, "draw": 7.17, "home": 11.28}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:57Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.06, "home_away": 1.12, "home_draw": 4.53}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 11.28 |
| Reference draw odds | 7.17 |
| Reference away odds | 1.23 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:50Z |
| Market reference home last update utc | 2026-11-04T09:30:50Z |
| Market reference draw last update utc | 2026-11-04T09:30:50Z |
| Market reference away last update utc | 2026-11-04T09:30:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-11-04T09:30:06Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:30:06Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.8% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | -0.0152 |
| Raw ev home | -0.3187 |
| Raw edge prob draw | -0.0280 |
| Raw ev draw | -0.3092 |
| Raw edge prob away | 0.0431 |
| Raw ev away | 0.0733 |
| Market p home draw | 21.5% |
| Market home draw odds | 4.53 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T09:30:57Z |
| Market reference home draw last update utc | 2026-11-04T09:30:57Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 91.7% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T09:30:04Z |
| Market reference draw away last update utc | 2026-11-04T09:30:57Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.8% |
| Market home away odds | 1.12 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T09:30:04Z |
| Market reference home away last update utc | 2026-11-04T09:30:57Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.53 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 92.2% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-04T09:30:43Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 8.50 |
| Market reference over 1 5 last update utc | 2026-11-04T09:30:51Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 43.7% |
| Market under 3 5 odds | 2.22 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-04T09:30:43Z |
| Market reference under 3 5 odds | 2.06 |
| Market reference under 3 5 opposite odds | 1.65 |
| Market reference under 3 5 last update utc | 2026-11-04T09:30:51Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,433.7048 |
| Elo away rating | 1,551.6587 |
| Elo rating diff | -57.9539 |
| Elo home expectancy | 0.4174 |

</details>


---

## 2026-11-04 — Borussia Dortmund vs Real Betis

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **56.2%**. Expected goals are 2.15 for Borussia Dortmund and 1.51 for Real Betis (3.66 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.4%; Under 3.5 goals: 50.0%; Double Chance 1X: 77.8%; Double Chance X2: 43.8%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 68.7%; BTTS No (at least one team does not score): 31.3%.

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
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.8% |
| Under 1.5 | 12.2% |
| Over 2.5 | 70.4% |
| Under 2.5 | 29.6% |
| Over 3.5 | 50.0% |
| Under 3.5 | 50.0% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.58% |
| 2 | 1-1 | 8.62% |
| 3 | 2-2 | 7.35% |
| 4 | 3-1 | 6.86% |
| 5 | 1-0 | 6.36% |

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
| Market best home last update utc | 2026-11-04T09:30:04Z |
| Market best draw last update utc | 2026-11-04T09:30:04Z |
| Market best away last update utc | 2026-11-04T09:30:04Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Borussia Dortmund |
| Matched away-team name | Real Betis Balompié |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1474 |
| Dc lambda away | 1.5095 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:30:54.245100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 68.7% |
| P btts no | 31.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.62 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.20 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.38 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.12271885855299523, "-10": 4.7417196789625954e-07, "-11": 6.354044237175077e-08, "-12": 7.832934173957325e-09, "-13": 8.938446260063995e-10, "-14": 9.492522115570208e-11, "-15": 9.418003326620994e-12, "-16": 8.658218629957586e-13, "-17": 6.456839334789142e-14, "-2": 0.06266043675100591, "-3": 0.02551992943386214, "-4": 0.008394525448103849, "-5": 0.0023024837352847304, "-6": 0.0005397971787328266, "-7": 0.00011028611963293571, "-8": 1.9942238436274048e-05, "-9": 3.2316316475304805e-06, "0": 0.2158489883668632, "1": 0.2276090446194899, "10": 2.116036600400613e-05, "11": 4.033836814760972e-06, "12": 7.074135263939588e-07, "13": 1.148396097178178e-07, "14": 1.73497045581556e-08, "15": 2.4487818477676017e-09, "16": 3.2025845005459564e-10, "17": 3.397604483589069e-11, "2": 0.16669953328455925, "3": 0.09658311921059226, "4": 0.04519586467354809, "5": 0.01763518062743486, "6": 0.005881589949729146, "7": 0.0017094869156846436, "8": 0.00043974369441065526, "9": 0.00010137441484809622} |
| Raw goal margin distribution | {"-1": 0.15129869269879212, "-10": 5.846012560990097e-07, "-11": 7.833829272619315e-08, "-12": 9.657135948698988e-09, "-13": 1.102010929576954e-09, "-14": 1.1703223151150237e-10, "-15": 1.1611349779099236e-11, "-16": 1.0674619820124922e-12, "-17": 7.960564185804123e-14, "-2": 0.07725334374967709, "-3": 0.031463232355941166, "-4": 0.01034951547871821, "-5": 0.0028387061549987745, "-6": 0.0006655098362857085, "-7": 0.00013597050950469835, "-8": 2.4586560211468216e-05, "-9": 3.984242106882535e-06, "0": 0.19899224129139384, "1": 0.2134685997199961, "10": 1.9845756604221546e-05, "11": 3.783230573220636e-06, "12": 6.634647368902143e-07, "13": 1.077050814032294e-07, "14": 1.6271836401654023e-08, "15": 2.296648768666433e-09, "16": 3.003620659976042e-10, "17": 3.18652482693139e-11, "2": 0.1563431541295817, "3": 0.09058279405786472, "4": 0.04238802531387022, "5": 0.016539576977888548, "6": 0.005516190153141099, "7": 0.0016032832910525213, "8": 0.00041242416723145616, "9": 9.50764255490577e-05} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7045 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.82, "draw": 4.25, "home": 1.75}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.72, "draw": 4.25, "home": 1.7}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.70 |
| Reference draw odds | 4.25 |
| Reference away odds | 4.72 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:50Z |
| Market reference home last update utc | 2026-11-04T09:30:50Z |
| Market reference draw last update utc | 2026-11-04T09:30:50Z |
| Market reference away last update utc | 2026-11-04T09:30:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-11-04T09:30:06Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:30:06Z |
| Home probability edge | -1.5% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +6.1% |
| Under 2.5 probability edge | -6.1% |
| Raw edge prob home | -0.0499 |
| Raw ev home | -0.0778 |
| Raw edge prob draw | -0.0241 |
| Raw ev draw | -0.1543 |
| Raw edge prob away | 0.0739 |
| Raw ev away | 0.3208 |
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
| Market best home last update utc | 2026-11-04T09:30:50Z |
| Market best draw last update utc | 2026-11-04T09:30:50Z |
| Market best away last update utc | 2026-11-04T09:30:04Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Fenerbahçe SK |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.5667 |
| Dc lambda away | 3.6879 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:30:54.245100+00:00 |
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
| Goal margin distribution | {"-1": 0.11386026066012524, "-10": 0.001534023434040217, "-11": 0.0004928796231892027, "-12": 0.00014548778101501294, "-13": 3.971113711827126e-05, "-14": 1.0079191200797495e-05, "-15": 2.39042373540137e-06, "-16": 5.319949241842192e-07, "-17": 1.1152065720796518e-07, "-18": 2.209370741191285e-08, "-19": 4.148536128874397e-09, "-2": 0.15691692293198908, "-20": 7.376386304553182e-10, "-21": 1.1514260100894027e-10, "-3": 0.1630282801194093, "-4": 0.13374340685477618, "-5": 0.09024828578851665, "-6": 0.05159909589594573, "-7": 0.02555903531534218, "-8": 0.011158740578813142, "-9": 0.004352888790700665, "0": 0.14093380915686196, "1": 0.08610283447787478, "10": 5.209815740656717e-11, "11": 2.5720730317336627e-12, "12": 1.1665974281548345e-13, "13": 4.892815959223824e-15, "14": 1.9082018100588414e-16, "15": 6.953854103475437e-18, "16": 2.37799114688154e-19, "17": 7.659671199541482e-21, "18": 2.3317150087192457e-22, "19": 6.727501589091887e-24, "2": 0.01714919159616037, "20": 1.838038685241345e-25, "21": 4.40858372618305e-27, "3": 0.0027377190547770115, "4": 0.0003451043043552516, "5": 3.578236309584671e-05, "6": 3.1435777882298485e-06, "7": 2.392647057357235e-07, "8": 1.6050975268021892e-08, "9": 9.620903946969344e-10} |
| Raw goal margin distribution | {"-1": 0.1313124656781184, "-10": 0.0021988459584107757, "-11": 0.0007258608654684043, "-12": 0.00022016184388536165, "-13": 6.175515064539341e-05, "-14": 1.6108904379589506e-05, "-15": 3.926653558362987e-06, "-16": 8.982261078288399e-07, "-17": 1.9354563515341628e-07, "-18": 3.9415246567835845e-08, "-19": 7.608933710436221e-09, "-2": 0.1840655234976028, "-20": 1.3959715881368742e-09, "-21": 2.4310207326704675e-10, "-22": 3.7216783314591966e-11, "-3": 0.19529751025867795, "-4": 0.16399350915779012, "-5": 0.11342073026608673, "-6": 0.0665208623523599, "-7": 0.03381922063408856, "-8": 0.015160207533098604, "-9": 0.006073780523813713, "0": 0.06051917691212816, "1": 0.021432740783891503, "10": 1.6133011041236747e-11, "11": 8.183254728796099e-13, "12": 3.813878068341188e-14, "13": 1.6438038696461193e-15, "14": 6.588626355101016e-17, "15": 2.467763429564167e-18, "16": 8.673985158697864e-20, "17": 2.8718942539624966e-21, "18": 8.986723369765837e-23, "19": 2.665710537557793e-24, "2": 0.004345868443789426, "20": 7.514806979656913e-26, "21": 2.0108606518570434e-27, "22": 4.730251256494678e-29, "3": 0.0007085212731643285, "4": 9.141867221771899e-05, "5": 9.715222511941494e-06, "6": 8.755284156332128e-07, "7": 6.839557937834855e-08, "8": 4.711092666691259e-09, "9": 2.900198058488156e-10} |
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
| Totals anchor reference last update utc | 2026-11-04T09:30:50Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7335 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.34, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.18, "price": 5.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.72, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.5, "draw": 5.18, "home": 6.35}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.15, "home_away": 1.2, "home_draw": 2.77}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.14, "home_away": 1.18, "home_draw": 2.98}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.44, "draw": 5.32, "home": 6.58}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.36, "under": 3.27}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.58 |
| Reference draw odds | 5.32 |
| Reference away odds | 1.44 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:50Z |
| Market reference home last update utc | 2026-11-04T09:30:50Z |
| Market reference draw last update utc | 2026-11-04T09:30:50Z |
| Market reference away last update utc | 2026-11-04T09:30:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-11-04T09:30:06Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:30:06Z |
| Home probability edge | -3.4% |
| Draw probability edge | -3.4% |
| Away probability edge | +6.9% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | -0.1140 |
| Raw ev home | -0.8250 |
| Raw edge prob draw | -0.1149 |
| Raw ev draw | -0.6780 |
| Raw edge prob away | 0.2289 |
| Raw ev away | 0.3693 |
| Market p home draw | 36.0% |
| Market home draw odds | 2.98 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T09:30:11Z |
| Market reference home draw last update utc | 2026-11-04T09:30:51Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.2% |
| Market draw away odds | 1.15 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T09:30:04Z |
| Market reference draw away last update utc | 2026-11-04T09:30:51Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.9% |
| Market home away odds | 1.20 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T09:30:04Z |
| Market reference home away last update utc | 2026-11-04T09:30:51Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.62 |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 89.5% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market reference over 1 5 last update utc | 2026-11-04T09:30:51Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 50.5% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T09:30:50Z |
| Market reference under 3 5 odds | 1.82 |
| Market reference under 3 5 opposite odds | 1.85 |
| Market reference under 3 5 last update utc | 2026-11-04T09:30:51Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,424.2185 |
| Elo away rating | 1,539.7264 |
| Elo rating diff | -55.5079 |
| Elo home expectancy | 0.4208 |

</details>


---

## 2026-11-04 — PSV Eindhoven vs Club Brugge

The model's most likely 1X2 outcome is **PSV Eindhoven win** at **51.2%**. Expected goals are 2.45 for PSV Eindhoven and 1.90 for Club Brugge (4.35 combined). The most likely exact score is 2-2 at 7.8%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 80.5%; Under 3.5 goals: 36.7%; Double Chance 1X: 71.9%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 56.4%; BTTS Yes (both teams score): 77.8%; BTTS No (at least one team does not score): 22.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PSV Eindhoven win | 51.2% | 1.95 |
| Draw | 20.7% | 4.82 |
| Club Brugge win | 28.1% | 3.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| PSV Eindhoven expected goals | 2.45 |
| Club Brugge expected goals | 1.90 |
| Expected total goals | 4.35 |
| Over 0.5 | 98.9% |
| Under 0.5 | 1.1% |
| Over 1.5 | 92.9% |
| Under 1.5 | 7.1% |
| Over 2.5 | 80.5% |
| Under 2.5 | 19.5% |
| Over 3.5 | 63.3% |
| Under 3.5 | 36.7% |
| Over 4.5 | 43.6% |
| Under 4.5 | 56.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.80% |
| 2 | 2-1 | 7.39% |
| 3 | 1-1 | 6.37% |
| 4 | 3-1 | 6.05% |
| 5 | 3-2 | 5.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 51.2% | 51.3% | 2.02 | +3.4% |
| Draw | 20.7% | 21.7% | 4.42 | -8.3% |
| Club Brugge win | 28.1% | 27.0% | 3.55 | -0.3% |

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
| Market best home last update utc | 2026-11-04T09:30:04Z |
| Market best draw last update utc | 2026-11-04T09:30:04Z |
| Market best away last update utc | 2026-11-04T09:30:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | PSV |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.4550 |
| Dc lambda away | 1.8976 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:30:54.245100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 77.8% |
| P btts no | 22.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 90.63 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 14.07 |
| Fair Over 2.5 odds | 1.24 |
| Fair Under 2.5 odds | 5.13 |
| Fair Over 3.5 odds | 1.58 |
| Fair Under 3.5 odds | 2.73 |
| Fair Over 4.5 odds | 2.30 |
| Fair Under 4.5 odds | 1.77 |
| Goal margin distribution | {"-1": 0.13850214088667023, "-10": 2.9997502726083197e-06, "-11": 5.003176106678681e-07, "-12": 7.687587595101581e-08, "-13": 1.0947069317682039e-08, "-14": 1.4521459236544651e-09, "-15": 1.8023383189825766e-10, "-16": 2.0974889908230552e-11, "-17": 2.2506309062064805e-12, "-18": 1.8848230663348918e-13, "-2": 0.0811449272493114, "-3": 0.03881322468132892, "-4": 0.015290678764283671, "-5": 0.0050867921612942745, "-6": 0.0014587153318881374, "-7": 0.0003666963359454017, "-8": 8.192899633452208e-05, "-9": 1.645570194601597e-05, "0": 0.2073919523578802, "1": 0.19448686513914426, "10": 4.296654824254381e-05, "11": 9.271288389704508e-06, "12": 1.8430338596939128e-06, "13": 3.395392938166713e-07, "14": 5.827085216127992e-08, "15": 9.356778781208671e-09, "16": 1.4087653844778175e-09, "17": 1.9556547920171002e-10, "18": 2.118885272380571e-11, "2": 0.14808642513207626, "3": 0.09163946320299755, "4": 0.04670662763656785, "5": 0.020102250296981948, "6": 0.0074579620088854465, "7": 0.00242552148452551, "8": 0.0007011083286081062, "9": 0.00018218509377136913} |
| Raw goal margin distribution | {"-1": 0.15035041855818534, "-10": 3.2563663360679356e-06, "-11": 5.431176853612435e-07, "-12": 8.345228494135692e-08, "-13": 1.1883545217150988e-08, "-14": 1.5763709212817238e-09, "-15": 1.9565208083261222e-10, "-16": 2.2769203831258824e-11, "-17": 2.4431629475317306e-12, "-18": 2.0460617801096157e-13, "-2": 0.08808653568604612, "-3": 0.042133533381304746, "-4": 0.01659873224725051, "-5": 0.005521945911254117, "-6": 0.0015835023148565016, "-7": 0.0003980656706112347, "-8": 8.893767859535624e-05, "-9": 1.786341827940914e-05, "0": 0.18561725396524345, "1": 0.1936343623287153, "10": 4.277821108617599e-05, "11": 9.230649144463626e-06, "12": 1.8349552085007813e-06, "13": 3.380509763304356e-07, "14": 5.801543097796227e-08, "15": 9.315764802183222e-09, "16": 1.402590281348652e-09, "17": 1.9470824845492893e-10, "18": 2.1095974695853094e-11, "2": 0.14743731140647245, "3": 0.09123777592262072, "4": 0.04650189642607019, "5": 0.020014135221129072, "6": 0.00742527119674192, "7": 0.0024148895897657557, "8": 0.000698035129705312, "9": 0.0001813865138552024} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8050 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 4.42, "home": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.55, "draw": 4.4, "home": 1.91}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.91 |
| Reference draw odds | 4.40 |
| Reference away odds | 3.55 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:50Z |
| Market reference home last update utc | 2026-11-04T09:30:50Z |
| Market reference draw last update utc | 2026-11-04T09:30:50Z |
| Market reference away last update utc | 2026-11-04T09:30:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-11-04T09:30:06Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:30:06Z |
| Home probability edge | -0.1% |
| Draw probability edge | -0.9% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +9.6% |
| Under 2.5 probability edge | -9.6% |
| Raw edge prob home | -0.0032 |
| Raw ev home | 0.0294 |
| Raw edge prob draw | -0.0311 |
| Raw ev draw | -0.1796 |
| Raw edge prob away | 0.0343 |
| Raw ev away | 0.0820 |
| Elo home rating | 1,466.3756 |
| Elo away rating | 1,460.8471 |
| Elo rating diff | 65.5285 |
| Elo home expectancy | 0.5932 |

</details>


---

## 2026-11-04 — Porto vs Napoli

The model's most likely 1X2 outcome is **Porto win** at **52.8%**. Expected goals are 1.64 for Porto and 0.98 for Napoli (2.62 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 48.4%; Under 3.5 goals: 73.1%; Double Chance 1X: 77.1%; Double Chance X2: 47.2%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 52.8% | 1.90 |
| Draw | 24.4% | 4.11 |
| Napoli win | 22.9% | 4.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 1.64 |
| Napoli expected goals | 0.98 |
| Expected total goals | 2.62 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 48.4% |
| Under 2.5 | 51.6% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.33% |
| 2 | 1-1 | 11.55% |
| 3 | 2-0 | 9.66% |
| 4 | 2-1 | 9.47% |
| 5 | 0-1 | 7.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 52.8% | 52.4% | 1.92 | +1.3% |
| Draw | 24.4% | 24.8% | 3.92 | -4.5% |
| Napoli win | 22.9% | 22.8% | 4.19 | -4.1% |
| Over 2.5 | 48.4% | 55.8% | 1.77 | -14.3% |
| Under 2.5 | 51.6% | 44.2% | 2.22 | +14.5% |

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
| Market best home last update utc | 2026-11-04T09:30:04Z |
| Market best draw last update utc | 2026-11-04T09:30:04Z |
| Market best away last update utc | 2026-11-04T09:30:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Dc lambda away | 0.9796 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:30:54.245100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.41 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.72 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.01 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.15048738780814172, "-10": 1.8664502197313892e-08, "-11": 1.6423310291565174e-09, "-12": 1.327106012530918e-10, "-13": 9.911416310627401e-12, "-14": 6.849561069676021e-13, "-15": 4.0395915494942755e-14, "-2": 0.0572176573408416, "-3": 0.016612846272267775, "-4": 0.0037791997750078556, "-5": 0.0007039948984203993, "-6": 0.00011080724980722452, "-7": 1.5082369089926064e-05, "-8": 1.807126018362401e-06, "-9": 1.9328722519919997e-07, "0": 0.243534313407767, "1": 0.2471171872469211, "10": 3.2829554511521792e-06, "11": 4.847202843449943e-07, "12": 6.572309859630373e-08, "13": 8.236260038510634e-09, "14": 9.550783304499641e-10, "15": 9.451388652996328e-11, "2": 0.16014865966167618, "3": 0.0780223810647127, "4": 0.029782209987652235, "5": 0.009309117266756848, "6": 0.0024586068254321414, "7": 0.0005615292573658636, "8": 0.00011289460316971173, "9": 2.0261416859289273e-05} |
| Raw goal margin distribution | {"-1": 0.15174288014555384, "-10": 1.8820217170054423e-08, "-11": 1.6560327356757968e-09, "-12": 1.3381778468815174e-10, "-13": 9.994105680229316e-12, "-14": 6.906705868073202e-13, "-15": 4.073293219185896e-14, "-2": 0.05769501515402713, "-3": 0.016751444605996767, "-4": 0.003810729037547259, "-5": 0.0007098682158685756, "-6": 0.0001117316970654894, "-7": 1.5208198895986389e-05, "-8": 1.822202583261545e-06, "-9": 1.9489978977149903e-07, "0": 0.2340653505157721, "1": 0.25065811605365235, "10": 3.3299967421999956e-06, "11": 4.916658150754375e-07, "12": 6.666484132039339e-08, "13": 8.354276963011117e-09, "14": 9.687635961761229e-10, "15": 9.586817089673893e-11, "2": 0.16244342114173788, "3": 0.07914035954188656, "4": 0.030208957663312785, "5": 0.009442507104438034, "6": 0.002493836069620243, "7": 0.0005695753797152673, "8": 0.0001145122638308, "9": 2.0551741605299597e-05} |
| Unadjusted home-win probability | 53.5% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 73.1% |
| Raw p under 3 5 | 73.1% |
| Raw p btts yes | 49.8% |
| P home draw | 77.1% |
| P draw away | 47.2% |
| P home away | 75.6% |
| Raw p home draw | 76.9% |
| Raw p draw away | 46.5% |
| Raw p home away | 76.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4843 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.12, "price": 1.44, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.17, "draw": 3.92, "home": 1.92}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.77, "under": 2.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.19, "draw": 3.87, "home": 1.87}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.87 |
| Reference draw odds | 3.87 |
| Reference away odds | 4.19 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:50Z |
| Market reference home last update utc | 2026-11-04T09:30:50Z |
| Market reference draw last update utc | 2026-11-04T09:30:50Z |
| Market reference away last update utc | 2026-11-04T09:30:50Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-04T09:30:04Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:30:04Z |
| Market best over 2 5 last update utc | 2026-11-04T09:30:04Z |
| Market best under 2 5 last update utc | 2026-11-04T09:30:04Z |
| Home probability edge | +0.3% |
| Draw probability edge | -0.4% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.0108 |
| Raw ev home | 0.0274 |
| Raw edge prob draw | -0.0135 |
| Raw ev draw | -0.0825 |
| Raw edge prob away | 0.0027 |
| Raw ev away | -0.0328 |
| Elo home rating | 1,455.3386 |
| Elo away rating | 1,429.7462 |
| Elo rating diff | 85.5924 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-04 — RB Leipzig vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **58.9%**. Expected goals are 1.24 for RB Leipzig and 1.76 for Manchester City (3.01 combined). The most likely exact score is 1-2 at 11.2%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 58.8%; Under 3.5 goals: 64.1%; Double Chance 1X: 41.1%; Double Chance X2: 79.2%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

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
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.22% |
| 2 | 0-1 | 10.87% |
| 3 | 1-1 | 9.37% |
| 4 | 0-2 | 9.03% |
| 5 | 1-3 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 20.8% | 18.0% | 5.63 | +17.2% |
| Draw | 20.3% | 19.4% | 5.03 | +2.0% |
| Manchester City win | 58.9% | 62.6% | 1.57 | -7.5% |

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
| Market best home last update utc | 2026-11-04T09:30:04Z |
| Market best draw last update utc | 2026-11-04T09:30:04Z |
| Market best away last update utc | 2026-11-04T09:30:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Manchester City FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2420 |
| Dc lambda away | 1.7647 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:30:54.245100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.97 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.01 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.2702486781029735, "-10": 5.706284945630237e-06, "-11": 9.007155269415943e-07, "-12": 1.306470107771532e-07, "-13": 1.7526116106585413e-08, "-14": 2.185798946560542e-09, "-15": 2.529009388067486e-10, "-16": 2.4533373916102176e-11, "-2": 0.17729177860807552, "-3": 0.08946900141171148, "-4": 0.03580396115174467, "-5": 0.01181508656680722, "-6": 0.003308755690628381, "-7": 0.0008036137731537941, "-8": 0.00017215325657059176, "-9": 3.296881584326906e-05, "0": 0.20286913510361249, "1": 0.12403407556437335, "10": 1.0983172602600554e-07, "11": 1.2200921374077645e-08, "12": 1.2454751918771919e-09, "13": 1.1758499725036904e-10, "14": 1.0320650376861245e-11, "15": 8.403842803863745e-13, "16": 5.737403336506791e-14, "2": 0.056704555677305514, "3": 0.020138752744683377, "4": 0.005671810103449809, "5": 0.0013172194581697176, "6": 0.00025960709397132234, "7": 4.4374129955811966e-05, "8": 6.690034337563468e-06, "9": 9.016688739794759e-07} |
| Raw goal margin distribution | {"-1": 0.23040544856436063, "-10": 4.864997496983233e-06, "-11": 7.679214805808854e-07, "-12": 1.1138549625109766e-07, "-13": 1.494221052800202e-08, "-14": 1.86354283132476e-09, "-15": 2.1561531644537476e-10, "-16": 2.091637621177513e-11, "-2": 0.15115334536956435, "-3": 0.07627843195227824, "-4": 0.03052532129835386, "-5": 0.010073167940583596, "-6": 0.0028209401224106308, "-7": 0.000685135606122919, "-8": 0.0001467724045142193, "-9": 2.810816636116833e-05, "0": 0.22302732584128868, "1": 0.16375783039075134, "10": 1.4500696748254076e-07, "11": 1.6108447649534382e-08, "12": 1.6443571196002578e-09, "13": 1.5524333896639043e-10, "14": 1.3625991940086958e-11, "15": 1.1095298273831323e-12, "16": 7.574891965679132e-14, "2": 0.07486503179658725, "3": 0.02658848740750721, "4": 0.00748829152555934, "5": 0.0017390785527030726, "6": 0.0003427501214432616, "7": 5.8585604109006846e-05, "8": 8.83261719309091e-06, "9": 1.1904417222597674e-06} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5877 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.0, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.56, "draw": 5.03, "home": 5.63}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.57, "draw": 4.85, "home": 5.23}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.23 |
| Reference draw odds | 4.85 |
| Reference away odds | 1.57 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:50Z |
| Market reference home last update utc | 2026-11-04T09:30:50Z |
| Market reference draw last update utc | 2026-11-04T09:30:50Z |
| Market reference away last update utc | 2026-11-04T09:30:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.55 |
| Market reference over 2 5 last update utc | 2026-11-04T09:30:06Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:30:06Z |
| Home probability edge | +2.9% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -16.3% |
| Under 2.5 probability edge | +16.3% |
| Raw edge prob home | 0.0952 |
| Raw ev home | 0.5474 |
| Raw edge prob draw | 0.0288 |
| Raw ev draw | 0.1218 |
| Raw edge prob away | -0.1240 |
| Raw ev away | -0.2117 |
| Elo home rating | 1,451.6590 |
| Elo away rating | 1,506.5247 |
| Elo rating diff | 5.1343 |
| Elo home expectancy | 0.5074 |

</details>


---

## 2026-11-04 — RC Lens vs Como

The model's most likely 1X2 outcome is **Como win** at **57.0%**. Expected goals are 1.35 for RC Lens and 3.13 for Como (4.48 combined). The most likely exact score is 2-2 at 7.8%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 79.8%; Under 3.5 goals: 36.7%; Double Chance 1X: 43.0%; Double Chance X2: 78.0%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 56.7%; BTTS Yes (both teams score): 73.4%; BTTS No (at least one team does not score): 26.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 22.0% | 4.54 |
| Draw | 21.0% | 4.77 |
| Como win | 57.0% | 1.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.35 |
| Como expected goals | 3.13 |
| Expected total goals | 4.48 |
| Over 0.5 | 98.6% |
| Under 0.5 | 1.4% |
| Over 1.5 | 92.8% |
| Under 1.5 | 7.2% |
| Over 2.5 | 79.8% |
| Under 2.5 | 20.2% |
| Over 3.5 | 63.3% |
| Under 3.5 | 36.7% |
| Over 4.5 | 43.3% |
| Under 4.5 | 56.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.79% |
| 2 | 1-1 | 7.00% |
| 3 | 1-3 | 6.11% |
| 4 | 1-2 | 5.86% |
| 5 | 2-1 | 5.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 22.0% | 25.7% | 3.74 | -17.7% |
| Draw | 21.0% | 24.1% | 4.03 | -15.5% |
| Como win | 57.0% | 50.2% | 2.07 | +18.0% |

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
| Market best home last update utc | 2026-11-04T09:30:50Z |
| Market best draw last update utc | 2026-11-04T09:30:04Z |
| Market best away last update utc | 2026-11-04T09:30:04Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3525 |
| Dc lambda away | 3.1295 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:30:54.245100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 73.4% |
| P btts no | 26.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 72.91 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.86 |
| Fair Over 2.5 odds | 1.25 |
| Fair Under 2.5 odds | 4.94 |
| Fair Over 3.5 odds | 1.58 |
| Fair Under 3.5 odds | 2.73 |
| Fair Over 4.5 odds | 2.31 |
| Fair Under 4.5 odds | 1.76 |
| Goal margin distribution | {"-1": 0.14769481439478988, "-10": 0.00032098285826023104, "-11": 8.855319220897766e-05, "-12": 2.2497066501973567e-05, "-13": 5.294968028507351e-06, "-14": 1.1606168683868573e-06, "-15": 2.3800840016204216e-07, "-16": 4.584877616664991e-08, "-17": 8.325803032313296e-09, "-18": 1.4282271226829183e-09, "-19": 2.2869166049599165e-10, "-2": 0.14779255042581185, "-20": 2.953412764295797e-11, "-3": 0.1188648110821174, "-4": 0.07831582546061924, "-5": 0.04341853086900063, "-6": 0.02069958554327805, "-7": 0.008636174458077763, "-8": 0.0031984802670855348, "-9": 0.0010639424671916422, "0": 0.2097850623922149, "1": 0.1351969399878026, "10": 1.51992916572395e-07, "11": 1.8121876271334083e-08, "12": 1.9896755458118364e-09, "13": 2.0238445099834444e-10, "14": 1.9171677283630098e-11, "15": 1.6991078542870224e-12, "16": 1.4145354656181373e-13, "17": 1.1101193076400542e-14, "18": 8.229969595749956e-16, "19": 5.695196500837011e-17, "2": 0.05750883986704411, "20": 3.1786298941137978e-18, "3": 0.019989079629071288, "4": 0.005691758360627072, "5": 0.0013637334070067703, "6": 0.0002809787238480508, "7": 5.066296739516402e-05, "8": 8.109056435722794e-06, "9": 1.1657414048754799e-06} |
| Raw goal margin distribution | {"-1": 0.18875047262043473, "-10": 0.0004102084859779197, "-11": 0.0001131688810469324, "-12": 2.875071783813864e-05, "-13": 6.76684365653741e-06, "-14": 1.4832408526794972e-06, "-15": 3.041690949157912e-07, "-16": 5.859364938427369e-08, "-17": 1.0640178964531202e-08, "-18": 1.8252404156529018e-09, "-19": 2.922625224172607e-10, "-2": 0.18887537695186327, "-20": 3.774391520706778e-11, "-3": 0.15190641162063576, "-4": 0.10008576895488361, "-5": 0.05548785348754872, "-6": 0.02645357977090005, "-7": 0.011036826291256761, "-8": 0.004087581981489161, "-9": 0.0013596932590103042, "0": 0.1363879153310819, "1": 0.08293206147663332, "10": 9.323499409329743e-08, "11": 1.1116261633893564e-08, "12": 1.2205002176728858e-09, "13": 1.2414600310941685e-10, "14": 1.176022711194225e-11, "15": 1.042261141708346e-12, "16": 8.676996846681971e-14, "17": 6.8096572804021005e-15, "18": 5.048400833089385e-16, "19": 3.493528672849651e-17, "2": 0.03527688306949735, "20": 1.9498246766080114e-18, "3": 0.012261635365482521, "4": 0.0034914196602101517, "5": 0.0008365368532588657, "6": 0.00017235704300626065, "7": 3.1077510533770045e-05, "8": 4.9742306808536085e-06, "9": 7.150852516611129e-07} |
| Unadjusted home-win probability | 13.5% |
| Unadjusted draw probability | 13.6% |
| Unadjusted away-win probability | 72.9% |
| Raw p over 1 5 | 93.6% |
| Raw p under 3 5 | 34.5% |
| Raw p btts yes | 70.7% |
| P home draw | 43.0% |
| P draw away | 78.0% |
| P home away | 79.0% |
| Raw p home draw | 27.1% |
| Raw p draw away | 86.5% |
| Raw p home away | 86.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7977 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.65, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.07, "draw": 4.03, "home": 3.54}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.95, "draw": 3.97, "home": 3.74}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.74 |
| Reference draw odds | 3.97 |
| Reference away odds | 1.95 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:50Z |
| Market reference home last update utc | 2026-11-04T09:30:50Z |
| Market reference draw last update utc | 2026-11-04T09:30:50Z |
| Market reference away last update utc | 2026-11-04T09:30:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-11-04T09:30:06Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:30:06Z |
| Home probability edge | -3.6% |
| Draw probability edge | -3.1% |
| Away probability edge | +6.8% |
| Over 2.5 probability edge | +16.5% |
| Under 2.5 probability edge | -16.5% |
| Raw edge prob home | -0.1215 |
| Raw ev home | -0.4951 |
| Raw edge prob draw | -0.1049 |
| Raw ev draw | -0.4504 |
| Raw edge prob away | 0.2264 |
| Raw ev away | 0.5082 |
| Elo home rating | 1,454.3021 |
| Elo away rating | 1,441.7871 |
| Elo rating diff | 72.5150 |
| Elo home expectancy | 0.6029 |

</details>


---

## 2026-11-04 — Slavia Praha vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **81.7%**. Expected goals are 0.32 for Slavia Praha and 3.11 for Arsenal (3.43 combined). The most likely exact score is 0-3 at 14.6%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 62.0%; Under 3.5 goals: 58.6%; Double Chance 1X: 18.3%; Double Chance X2: 94.2%; Double Chance 12 (either team wins): 87.6%; Under 4.5 goals: 76.2%; BTTS Yes (both teams score): 28.1%; BTTS No (at least one team does not score): 71.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Slavia Praha win | 5.8% | 17.15 |
| Draw | 12.4% | 8.05 |
| Arsenal win | 81.7% | 1.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Slavia Praha expected goals | 0.32 |
| Arsenal expected goals | 3.11 |
| Expected total goals | 3.43 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 41.4% |
| Under 3.5 | 58.6% |
| Over 4.5 | 23.8% |
| Under 4.5 | 76.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 14.61% |
| 2 | 0-2 | 14.08% |
| 3 | 0-4 | 11.36% |
| 4 | 0-1 | 9.19% |
| 5 | 0-5 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Slavia Praha win | 5.8% | 7.5% | 12.50 | -27.1% |
| Draw | 12.4% | 14.7% | 6.60 | -18.0% |
| Arsenal win | 81.7% | 77.8% | 1.27 | +3.8% |
| Over 2.5 | 62.0% | 57.5% | 1.72 | +6.7% |
| Under 2.5 | 38.0% | 42.5% | 2.31 | -12.3% |

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
| Market best home last update utc | 2026-11-04T09:30:04Z |
| Market best draw last update utc | 2026-11-04T09:30:04Z |
| Market best away last update utc | 2026-11-04T09:30:04Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-11-04T09:30:54.245100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 28.1% |
| P btts no | 71.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.39 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.55 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.20 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.14497585806499239, "-10": 0.0007472943577665053, "-11": 0.00020986180613537087, "-12": 5.408547122456077e-05, "-13": 1.2878192312584712e-05, "-14": 2.8494201602183e-06, "-15": 5.887741887789001e-07, "-16": 1.1410947189084446e-07, "-17": 2.082285452581572e-08, "-18": 3.589832497497909e-09, "-19": 5.858352733933285e-10, "-2": 0.19362429105097037, "-20": 8.684662899737652e-11, "-3": 0.18615663518952474, "-4": 0.13818832277525117, "-5": 0.08331708732445857, "-6": 0.04223469638522431, "-7": 0.018454593412709306, "-8": 0.007082653857950307, "-9": 0.002422688335614719, "0": 0.12419802969574266, "1": 0.05117740516241692, "10": 3.062243105528247e-13, "11": 8.824891699063024e-15, "12": 2.3339127249103913e-16, "13": 5.702783915672151e-18, "14": 1.294841226206696e-19, "15": 2.7455970799043198e-21, "16": 5.460567158657451e-23, "17": 1.0225494942566678e-24, "18": 1.8090321027324797e-26, "19": 3.0295325436946038e-28, "2": 0.00645184129785126, "20": 4.608728095492099e-30, "3": 0.000636546847638752, "4": 4.8489891561627974e-05, "5": 3.000143044913947e-06, "6": 1.5606491327684562e-07, "7": 6.997910698633329e-09, "8": 2.756055431586229e-10, "9": 9.674254201580777e-12} |
| Raw goal margin distribution | {"-1": 0.1612610876090232, "-10": 0.0008312384041451161, "-11": 0.00023343571513687698, "-12": 6.0160926308221554e-05, "-13": 1.432480777478529e-05, "-14": 3.1694973233811585e-06, "-15": 6.549115646278257e-07, "-16": 1.269274608146103e-07, "-17": 2.3161898903555145e-08, "-18": 3.993080645338955e-09, "-19": 6.516425190240003e-10, "-2": 0.2153742297452576, "-20": 9.660216558963809e-11, "-3": 0.20706772739252272, "-4": 0.15371110420062975, "-5": 0.09267614827521767, "-6": 0.04697894645924342, "-7": 0.02052760952641976, "-8": 0.007878252831442346, "-9": 0.0026948304438645238, "0": 0.07018641779399278, "1": 0.017990546454654904, "10": 1.0764794868089571e-13, "11": 3.1022405994488276e-15, "12": 8.204473275922468e-17, "13": 2.0047167032044453e-18, "14": 4.551794128198772e-20, "15": 9.65167961427976e-22, "16": 1.9195695214483668e-23, "17": 3.5945988508456203e-25, "18": 6.359344710597226e-27, "19": 1.064980645076782e-28, "2": 0.0022680350873336935, "20": 1.6201199852882132e-30, "3": 0.00022376721908165382, "4": 1.704579675253407e-05, "5": 1.0546492665824167e-06, "6": 5.486196620047984e-08, "7": 2.459996498645142e-09, "8": 9.688444171055429e-11, "9": 3.400819542830058e-12} |
| Unadjusted home-win probability | 2.1% |
| Unadjusted draw probability | 7.0% |
| Unadjusted away-win probability | 90.9% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 55.1% |
| Raw p btts yes | 26.0% |
| P home draw | 18.3% |
| P draw away | 94.2% |
| P home away | 87.6% |
| Raw p home draw | 9.1% |
| Raw p draw away | 97.9% |
| Raw p home away | 93.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6203 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.27, "draw": 6.6, "home": 12.5}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.27, "draw": 6.2, "home": 11.87}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 11.87 |
| Reference draw odds | 6.20 |
| Reference away odds | 1.27 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:50Z |
| Market reference home last update utc | 2026-11-04T09:30:50Z |
| Market reference draw last update utc | 2026-11-04T09:30:50Z |
| Market reference away last update utc | 2026-11-04T09:30:50Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-04T09:30:04Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:30:04Z |
| Market best over 2 5 last update utc | 2026-11-04T09:30:04Z |
| Market best under 2 5 last update utc | 2026-11-04T09:30:04Z |
| Home probability edge | -1.6% |
| Draw probability edge | -2.3% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | +4.6% |
| Under 2.5 probability edge | -4.6% |
| Raw edge prob home | -0.0540 |
| Raw ev home | -0.7437 |
| Raw edge prob draw | -0.0772 |
| Raw ev draw | -0.5368 |
| Raw edge prob away | 0.1312 |
| Raw ev away | 0.1548 |
| Elo home rating | 1,396.4207 |
| Elo away rating | 1,607.4002 |
| Elo rating diff | -150.9796 |
| Elo home expectancy | 0.2954 |

</details>


---

## 2026-11-04 — Viking FK vs Sabah FK

The model's most likely 1X2 outcome is **Viking FK win** at **74.6%**. Expected goals are 3.67 for Viking FK and 0.95 for Sabah FK (4.62 combined). The most likely exact score is 3-0 at 7.0%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 81.1%; Under 3.5 goals: 34.9%; Double Chance 1X: 89.1%; Double Chance X2: 25.4%; Double Chance 12 (either team wins): 85.6%; Under 4.5 goals: 54.2%; BTTS Yes (both teams score): 62.4%; BTTS No (at least one team does not score): 37.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 74.6% | 1.34 |
| Draw | 14.4% | 6.93 |
| Sabah FK win | 10.9% | 9.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 3.67 |
| Sabah FK expected goals | 0.95 |
| Expected total goals | 4.62 |
| Over 0.5 | 98.6% |
| Under 0.5 | 1.4% |
| Over 1.5 | 93.2% |
| Under 1.5 | 6.8% |
| Over 2.5 | 81.1% |
| Under 2.5 | 18.9% |
| Over 3.5 | 65.1% |
| Under 3.5 | 34.9% |
| Over 4.5 | 45.8% |
| Under 4.5 | 54.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 7.05% |
| 2 | 3-1 | 6.71% |
| 3 | 4-0 | 6.47% |
| 4 | 4-1 | 6.16% |
| 5 | 2-0 | 5.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 74.6% | 69.9% | 1.45 | +8.2% |
| Draw | 14.4% | 17.0% | 5.49 | -20.8% |
| Sabah FK win | 10.9% | 13.2% | 6.98 | -23.8% |

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
| Market best home last update utc | 2026-11-04T09:30:04Z |
| Market best draw last update utc | 2026-11-04T09:30:04Z |
| Market best away last update utc | 2026-11-04T09:30:04Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Viking FK |
| Matched away-team name | Sabah FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.6722 |
| Dc lambda away | 0.9514 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:30:54.245100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 62.4% |
| P btts no | 37.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 72.86 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.73 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.28 |
| Fair Over 3.5 odds | 1.54 |
| Fair Under 3.5 odds | 2.87 |
| Fair Over 4.5 odds | 2.18 |
| Fair Under 4.5 odds | 1.85 |
| Goal margin distribution | {"-1": 0.07750590347755643, "-10": 4.337180378322039e-09, "-11": 3.6564448957469985e-10, "-12": 2.836505793132125e-11, "-13": 2.037337462385191e-12, "-14": 1.3621291144173926e-13, "-15": 8.516811817104798e-15, "-16": 5.000624052024308e-16, "-17": 2.7672114677644628e-17, "-18": 1.4479162220980922e-18, "-19": 7.184314261723145e-20, "-2": 0.024087662582381122, "-20": 3.3875698539282218e-21, "-21": 1.5076534685773156e-22, "-22": 5.626242822992361e-24, "-3": 0.006103737216119154, "-4": 0.0012540191173002907, "-5": 0.00021535332761036955, "-6": 3.1661202833206896e-05, "-7": 4.061028922886035e-06, "-8": 4.613669751961312e-07, "-9": 4.700027373397642e-08, "0": 0.14432624986932352, "1": 0.13064053931239694, "10": 0.0014358312249690439, "11": 0.0004672317925995489, "12": 0.00013990539852959055, "13": 3.878744863165074e-05, "14": 1.0009766863343292e-05, "15": 2.41579558100222e-06, "16": 5.475008287147673e-07, "17": 1.1694465273579337e-07, "18": 2.3618858157161106e-08, "19": 4.523537863043955e-09, "2": 0.16183446392334372, "20": 8.233009418882667e-10, "21": 1.4143253590351157e-10, "22": 2.0372471245370393e-11, "3": 0.1582885958646672, "4": 0.12552649444945224, "5": 0.08320707864184836, "6": 0.047218647358937015, "7": 0.0233775857606319, "8": 0.010251502572408346, "9": 0.004031056193488435} |
| Raw goal margin distribution | {"-1": 0.04018119603038926, "-10": 2.248513818705182e-09, "-11": 1.8956017869383388e-10, "-12": 1.4705227628006485e-11, "-13": 1.0562118791358949e-12, "-14": 7.061652662491013e-14, "-15": 4.415349925907513e-15, "-16": 2.5924613002782715e-16, "-17": 1.4345986751316637e-17, "-18": 7.506396667261755e-19, "-19": 3.724546476357263e-20, "-2": 0.01248770801590355, "-20": 1.756209556433886e-21, "-21": 7.816091013550152e-23, "-22": 2.9167993100124312e-24, "-3": 0.0031643455607208728, "-4": 0.0006501180647831509, "-5": 0.00011164509907319013, "-6": 1.6414039970095853e-05, "-7": 2.105349294880691e-06, "-8": 2.3918535286375516e-07, "-9": 2.4366236991659955e-08, "0": 0.08520409064555803, "1": 0.15019123047396438, "10": 0.0016507070436640218, "11": 0.0005371542265244101, "12": 0.00016084259959202123, "13": 4.4592089619309325e-05, "14": 1.1507754100494458e-05, "15": 2.7773255743889807e-06, "16": 6.294357293914125e-07, "17": 1.3444571940826752e-07, "18": 2.7153480747131568e-08, "19": 5.20049688497932e-09, "2": 0.1860534057626543, "20": 9.465100355785102e-10, "21": 1.6259827698358113e-10, "22": 2.342126372290078e-11, "3": 0.18197688947120316, "4": 0.1443118557047893, "5": 0.09565923097943946, "6": 0.05428503882088603, "7": 0.02687610131877916, "8": 0.01178566617728984, "9": 0.004634314072770146} |
| Unadjusted home-win probability | 85.8% |
| Unadjusted draw probability | 8.5% |
| Unadjusted away-win probability | 5.7% |
| Raw p over 1 5 | 94.3% |
| Raw p under 3 5 | 32.2% |
| Raw p btts yes | 59.6% |
| P home draw | 89.1% |
| P draw away | 25.4% |
| P home away | 85.6% |
| Raw p home draw | 94.3% |
| Raw p draw away | 14.2% |
| Raw p home away | 91.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8108 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "line": -1.25, "market_key": "spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:30:04Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.98, "draw": 5.49, "home": 1.45}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:50Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.97, "draw": 5.47, "home": 1.41}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.41 |
| Reference draw odds | 5.47 |
| Reference away odds | 6.97 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:50Z |
| Market reference home last update utc | 2026-11-04T09:30:50Z |
| Market reference draw last update utc | 2026-11-04T09:30:50Z |
| Market reference away last update utc | 2026-11-04T09:30:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.35 |
| Market reference over 2 5 last update utc | 2026-11-04T09:30:07Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:30:07Z |
| Home probability edge | +4.8% |
| Draw probability edge | -2.5% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | +7.8% |
| Under 2.5 probability edge | -7.8% |
| Raw edge prob home | 0.1596 |
| Raw ev home | 0.2444 |
| Raw edge prob draw | -0.0845 |
| Raw ev draw | -0.5322 |
| Raw edge prob away | -0.0751 |
| Raw ev away | -0.6048 |
| Elo home rating | 1,428.8826 |
| Elo away rating | 1,421.0274 |
| Elo rating diff | 67.8552 |
| Elo home expectancy | 0.5964 |

</details>


---
