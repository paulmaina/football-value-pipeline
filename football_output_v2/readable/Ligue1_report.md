# Ligue 1 — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,761 |
| Training data through | 2026-11-02 |
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
| Training sha256 | 0289f2ce25122532fc732e568cf66b1052a794d39ed246f5dd00e21f6fea90df |
| Training as of utc | 2026-11-03T13:21:37.802513+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 81, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 81, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 139, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_CHRONOLOGICAL_PARTITIONS', 'cutoff_utc': '2026-11-03T13:21:37.802513+00:00', 'observations': 491, 'observations_sha256': 'b862ec2dad5ade42c0ad1b70fdad82779605ab803c2fd0323165bc9913e20045', 'eligible_training_matches': 183, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 180, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 23, 'retrospective_eligible_training_matches': 183, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '4257569b28b533a7e39a605448fedde66feaf29561140fd4db3e54e616eb044d', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 123, 'tuning_matches': 17, 'audit_matches': 43, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1759, 'tune_start_date': '2025-11-04', 'audit_start_date': '2026-05-05', 'training_shot_matches': 1471, 'tuning_matches': 187, 'audit_matches': 96, 'audit_matchdays': 34, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8547663953061937, 'audit_candidate_poisson_score': 0.853030002969473, 'audit_gain': 0.001736392336720738, 'audit_gain_lower95': -0.004922191592297361, 'audit_baseline_briers': [0.5824577082919972, 0.17370317503684327, 0.21287476509120928, 0.2466053914205321], 'audit_candidate_briers': [0.581621616233085, 0.1732611984790755, 0.21186763973915182, 0.24573253012018595], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1601.922 |
| Base scoring parameter | 0.200 |
| Home-advantage parameter | 0.202 |
| Dixon-Coles low-score adjustment | -0.054 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1761, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261103T132137802513Z_856cf98deb7c1c986aa974878f535ddaa2b8a2e35e6327776f0dac5018f37a3d.json |
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

## 2026-11-06 — Toulouse FC vs RC Strasbourg Alsace

The model's most likely 1X2 outcome is **Toulouse FC win** at **39.6%**. Expected goals are 1.50 for Toulouse FC and 1.39 for RC Strasbourg Alsace (2.89 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.2%; Under 3.5 goals: 67.1%; Double Chance 1X: 65.6%; Double Chance X2: 60.4%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse FC win | 39.6% | 2.53 |
| Draw | 26.0% | 3.84 |
| RC Strasbourg Alsace win | 34.4% | 2.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse FC expected goals | 1.50 |
| RC Strasbourg Alsace expected goals | 1.39 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 32.9% |
| Under 3.5 | 67.1% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.20% |
| 2 | 2-1 | 8.71% |
| 3 | 1-2 | 8.04% |
| 4 | 1-0 | 7.71% |
| 5 | 0-1 | 7.07% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:45:00+00:00 |
| Fixture id | fdorg:559638 |
| Matched home-team name | Toulouse |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.5045 |
| Dc lambda away | 1.3887 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:21:37.802513+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.22 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.04 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.98 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.18444673515649582, "-10": 4.917311387004162e-07, "-11": 6.112488794330425e-08, "-12": 6.981228364474246e-09, "-13": 7.371004899902046e-10, "-14": 7.183359201024837e-11, "-15": 5.837376179979485e-12, "-2": 0.10181590073448475, "-3": 0.04068033687067777, "-4": 0.012863359413233941, "-5": 0.0033500963611573166, "-6": 0.0007398745459097185, "-7": 0.00014164393956703455, "-8": 2.3909633668647543e-05, "-9": 3.607112243303374e-06, "0": 0.26014338626756744, "1": 0.20034569318646492, "10": 1.0952021629823978e-06, "11": 1.4748957232964086e-07, "12": 1.824953248029883e-08, "13": 2.087484486704065e-09, "14": 2.203945234977363e-10, "15": 1.940294062973527e-11, "2": 0.11950028034032455, "3": 0.051726669340889, "4": 0.01771989063799846, "5": 0.004999661368708178, "6": 0.0011962392161246995, "7": 0.0002481044791413926, "8": 4.53718186797827e-05, "9": 7.415656086846285e-06} |
| Raw goal margin distribution | {"-1": 0.18444673515649582, "-10": 4.917311387004162e-07, "-11": 6.112488794330425e-08, "-12": 6.981228364474246e-09, "-13": 7.371004899902046e-10, "-14": 7.183359201024837e-11, "-15": 5.837376179979485e-12, "-2": 0.10181590073448475, "-3": 0.04068033687067777, "-4": 0.012863359413233941, "-5": 0.0033500963611573166, "-6": 0.0007398745459097185, "-7": 0.00014164393956703455, "-8": 2.3909633668647543e-05, "-9": 3.607112243303374e-06, "0": 0.26014338626756744, "1": 0.20034569318646492, "10": 1.0952021629823978e-06, "11": 1.4748957232964086e-07, "12": 1.824953248029883e-08, "13": 2.087484486704065e-09, "14": 2.203945234977363e-10, "15": 1.940294062973527e-11, "2": 0.11950028034032455, "3": 0.051726669340889, "4": 0.01771989063799846, "5": 0.004999661368708178, "6": 0.0011962392161246995, "7": 0.0002481044791413926, "8": 4.53718186797827e-05, "9": 7.415656086846285e-06} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 34.4% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.1% |
| Raw p btts yes | 59.0% |
| P home draw | 65.6% |
| P draw away | 60.4% |
| P home away | 74.0% |
| Raw p home draw | 65.6% |
| Raw p draw away | 60.4% |
| Raw p home away | 74.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5525 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.015425808281886944, "mu": 9.118380611678907, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,453.8748 |
| Elo away rating | 1,507.0944 |
| Elo rating diff | 6.7804 |
| Elo home expectancy | 0.5098 |

</details>


---
