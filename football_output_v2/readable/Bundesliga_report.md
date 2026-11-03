# Bundesliga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,604 |
| Training data through | 2026-11-01 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 480 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 70.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 8ae0ce9397a329b411bc9d1695ea06115451107817f04415560cba4e2507101a |
| Training as of utc | 2026-11-03T13:20:10.980291+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 68, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-03T13:20:10.980291+00:00', 'observations': 394, 'observations_sha256': 'af136d54960a56407d900f6dc336e08cd4129b531bb81434d27c4669e55a861b', 'eligible_training_matches': 80, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 114, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 22, 'retrospective_eligible_training_matches': 80, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '19da5aa489681546100a0eb15e2f9f5c656f72167be568725d32ede7cc24da6e', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1601, 'tune_start_date': '2025-11-04', 'audit_start_date': '2026-05-05', 'training_shot_matches': 1304, 'tuning_matches': 207, 'audit_matches': 82, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.6694684707799522, 'audit_candidate_poisson_score': 0.6673755260503863, 'audit_gain': 0.002092944729565893, 'audit_gain_lower95': -0.006070484700337189, 'audit_baseline_briers': [0.58388492118506, 0.13631400624425608, 0.2743748376176622, 0.23546132347341558], 'audit_candidate_briers': [0.5818374794393253, 0.13598617139864622, 0.2735010156442962, 0.2362612110519443], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1591.066 |
| Base scoring parameter | 0.218 |
| Home-advantage parameter | 0.226 |
| Dixon-Coles low-score adjustment | -0.079 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1604, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261103T132010980291Z_8a5a9d0e52e636de6b211f7dbc32727b5445eb66af7685888ec6fd392ed717ed.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
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

## 2026-11-06 — Hamburger SV vs Borussia Mönchengladbach

The model's most likely 1X2 outcome is **Hamburger SV win** at **37.6%**. Expected goals are 1.44 for Hamburger SV and 1.40 for Borussia Mönchengladbach (2.84 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 53.9%; Under 3.5 goals: 68.4%; Double Chance 1X: 64.5%; Double Chance X2: 62.4%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 37.6% | 2.66 |
| Draw | 26.9% | 3.71 |
| Borussia Mönchengladbach win | 35.5% | 2.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.44 |
| Borussia Mönchengladbach expected goals | 1.40 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.71% |
| 2 | 2-1 | 8.50% |
| 3 | 1-2 | 8.22% |
| 4 | 1-0 | 7.52% |
| 5 | 0-1 | 7.25% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:30:00+00:00 |
| Fixture id | fdorg:565852 |
| Matched home-team name | Hamburg |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4419 |
| Dc lambda away | 1.3955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:20:10.980291+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.74 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.64 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.16 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.32 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.18742496639721853, "-10": 5.421564953201939e-07, "-11": 6.775882996010985e-08, "-12": 7.77722993361254e-09, "-13": 8.189740724897483e-10, "-14": 7.13757289594982e-11, "-2": 0.10632391488844961, "-3": 0.04288811515255869, "-4": 0.013670127304006597, "-5": 0.003585486696686603, "-6": 0.0007970301594994717, "-7": 0.000153524110300414, "-8": 2.606750784540733e-05, "-9": 3.955051024983112e-06, "0": 0.2693453965971026, "1": 0.19396115967414104, "10": 7.517881606228318e-07, "11": 9.708090061700993e-08, "12": 1.1513037499887157e-08, "13": 1.252657130036946e-09, "14": 1.1280015600038684e-10, "2": 0.11350764741606344, "3": 0.04730730472072337, "4": 0.015579764393003258, "5": 0.004222148692265962, "6": 0.0009697443220359192, "7": 0.0001929994898366876, "8": 3.38591589653153e-05, "9": 5.307937811075881e-06} |
| Raw goal margin distribution | {"-1": 0.18742496639721853, "-10": 5.421564953201939e-07, "-11": 6.775882996010985e-08, "-12": 7.77722993361254e-09, "-13": 8.189740724897483e-10, "-14": 7.13757289594982e-11, "-2": 0.10632391488844961, "-3": 0.04288811515255869, "-4": 0.013670127304006597, "-5": 0.003585486696686603, "-6": 0.0007970301594994717, "-7": 0.000153524110300414, "-8": 2.606750784540733e-05, "-9": 3.955051024983112e-06, "0": 0.2693453965971026, "1": 0.19396115967414104, "10": 7.517881606228318e-07, "11": 9.708090061700993e-08, "12": 1.1513037499887157e-08, "13": 1.252657130036946e-09, "14": 1.1280015600038684e-10, "2": 0.11350764741606344, "3": 0.04730730472072337, "4": 0.015579764393003258, "5": 0.004222148692265962, "6": 0.0009697443220359192, "7": 0.0001929994898366876, "8": 3.38591589653153e-05, "9": 5.307937811075881e-06} |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 58.4% |
| P home draw | 64.5% |
| P draw away | 62.4% |
| P home away | 73.1% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5394 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.011797638629238775, "mu": 9.857167505714557, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,426.8279 |
| Elo away rating | 1,410.3288 |
| Elo rating diff | 76.4991 |
| Elo home expectancy | 0.6083 |

</details>


---
