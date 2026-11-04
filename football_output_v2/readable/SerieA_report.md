# Serie A — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 2,000 |
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
| Training sha256 | 95d730bf1bf574a5195cfdfdc3114658abb4d4b6114ce5544536dff795fe2d99 |
| Training as of utc | 2026-11-04T09:29:55.583731+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 100, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 100, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 183, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-04T09:29:55.583731+00:00', 'observations': 670, 'observations_sha256': '50787672292b34ded76318a77db6d7ebf08549a911580814c77134ddaaa6b8ba', 'eligible_training_matches': 244, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 229, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 36, 'retrospective_eligible_training_matches': 244, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '5d36838f30e963448de275d062494eeefd74e5c870e5ff4c7ebeaadbe152540b', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 183, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-10-05T00:00:00+00:00', 'audit_origin_utc': '2026-10-11T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 24, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1620, 'tuning_matches': 250, 'audit_matches': 129, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8311508011954305, 'audit_candidate_poisson_score': 0.8301708166060806, 'audit_gain': 0.0009799845893498915, 'audit_gain_lower95': -0.003523201039368521, 'audit_baseline_briers': [0.5470550783646152, 0.15449888366492173, 0.20909917551654086, 0.23872129172946965], 'audit_candidate_briers': [0.5497559485164174, 0.15368253383849234, 0.20921488521617435, 0.23948125844306573], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1828.641 |
| Base scoring parameter | 0.153 |
| Home-advantage parameter | 0.106 |
| Dixon-Coles low-score adjustment | -0.022 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 2000, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261104T092955583731Z_29bbe0231867e652a574717a69d2e7fb1f884340a400c6f9284d052e286c95f2.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
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

## 2026-11-06 — Venezia vs Udinese

The model's most likely 1X2 outcome is **Venezia win** at **38.8%**. Expected goals are 0.95 for Venezia and 1.32 for Udinese (2.27 combined). The most likely exact score is 1-0 at 13.9%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 39.6%; Under 3.5 goals: 81.1%; Double Chance 1X: 65.6%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 44.9%; BTTS No (at least one team does not score): 55.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 38.8% | 2.58 |
| Draw | 26.9% | 3.72 |
| Udinese win | 34.4% | 2.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.95 |
| Udinese expected goals | 1.32 |
| Expected total goals | 2.27 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 65.8% |
| Under 1.5 | 34.2% |
| Over 2.5 | 39.6% |
| Under 2.5 | 60.4% |
| Over 3.5 | 18.9% |
| Under 3.5 | 81.1% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.94% |
| 2 | 1-1 | 12.47% |
| 3 | 0-1 | 10.25% |
| 4 | 0-0 | 10.04% |
| 5 | 2-1 | 8.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 38.8% | 44.0% | 2.22 | -13.9% |
| Draw | 26.9% | 26.2% | 3.79 | +1.9% |
| Udinese win | 34.4% | 29.8% | 3.31 | +13.7% |
| Over 2.5 | 39.6% | 56.1% | 1.76 | -30.3% |
| Under 2.5 | 60.4% | 43.9% | 2.24 | +35.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:45:00+00:00 |
| Fixture id | fa069801a5c9b49143447a1a1d173fd1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T09:30:06Z |
| Market best draw last update utc | 2026-11-04T09:29:43Z |
| Market best away last update utc | 2026-11-04T09:29:43Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9463 |
| Dc lambda away | 1.3188 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:29:55.583731+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.9% |
| P btts no | 55.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.96 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.28 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.63 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.1829426881783466, "-10": 3.8984345013483004e-07, "-11": 4.6304276186686866e-08, "-12": 5.048188437804334e-09, "-13": 5.069367326721009e-10, "-14": 4.384508458737368e-11, "-2": 0.10264408223305979, "-3": 0.04109081029739453, "-4": 0.012781113511924591, "-5": 0.0032401697620013112, "-6": 0.0006920670345123551, "-7": 0.00012758997828139044, "-8": 2.067963697905166e-05, "-9": 2.9892694271967527e-06, "0": 0.26882990611976415, "1": 0.24972942579603719, "10": 2.6961203050295682e-08, "11": 2.29782972289032e-09, "12": 1.7975460228380536e-10, "13": 1.2952271513739109e-11, "14": 8.03823702955861e-13, "2": 0.10101856604674588, "3": 0.029017480864149705, "4": 0.006476366398717762, "5": 0.0011780892726024044, "6": 0.00018055366863771693, "7": 2.3884845457720354e-05, "8": 2.7777713897174316e-06, "9": 2.8811533077244414e-07} |
| Raw goal margin distribution | {"-1": 0.23920905527121436, "-10": 5.097447967940222e-07, "-11": 6.054574944715264e-08, "-12": 6.6008234549445745e-09, "-13": 6.628516182431518e-10, "-14": 5.73302019712725e-11, "-2": 0.13421358450912524, "-3": 0.05372881534344831, "-4": 0.016712108687946495, "-5": 0.004236725476183465, "-6": 0.0009049211157795042, "-7": 0.00016683191042329206, "-8": 2.7039924220902104e-05, "-9": 3.90865752958524e-06, "0": 0.28563811721549665, "1": 0.17082854034189796, "10": 1.8442932578979346e-08, "11": 1.5718407883425733e-09, "12": 1.2296194663483722e-10, "13": 8.860059761684312e-12, "14": 5.498592303668689e-13, "2": 0.06910220583813577, "3": 0.019849538694211456, "4": 0.004430187652438936, "5": 0.0008058772817404631, "6": 0.0001235085515791281, "7": 1.633853628913812e-05, "8": 1.9001470507383203e-06, "9": 1.9708659181468703e-07} |
| Unadjusted home-win probability | 26.5% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 45.1% |
| P home draw | 65.6% |
| P draw away | 61.2% |
| P home away | 73.1% |
| Raw p home draw | 55.1% |
| Raw p draw away | 73.5% |
| Raw p home away | 71.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3960 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:29:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:29:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:30:06Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.24, "draw": 3.68, "home": 2.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:29:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.31, "draw": 3.79, "home": 2.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:29:43Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.76, "under": 2.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.22 |
| Reference draw odds | 3.68 |
| Reference away odds | 3.24 |
| Market reference 1x2 last update utc | 2026-11-04T09:30:06Z |
| Market reference home last update utc | 2026-11-04T09:30:06Z |
| Market reference draw last update utc | 2026-11-04T09:30:06Z |
| Market reference away last update utc | 2026-11-04T09:30:06Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-11-04T09:29:43Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:29:43Z |
| Market best over 2 5 last update utc | 2026-11-04T09:29:43Z |
| Market best under 2 5 last update utc | 2026-11-04T09:29:43Z |
| Home probability edge | -5.2% |
| Draw probability edge | +0.7% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -16.5% |
| Under 2.5 probability edge | +16.5% |
| Raw edge prob home | -0.1750 |
| Raw ev home | -0.4113 |
| Raw edge prob draw | 0.0240 |
| Raw ev draw | 0.0826 |
| Raw edge prob away | 0.1509 |
| Raw ev away | 0.4869 |
| Count model | {"corners": {"alpha": 0.02176883148999032, "mu": 9.549493705641533, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,353.0341 |
| Elo away rating | 1,444.2839 |
| Elo rating diff | -31.2498 |
| Elo home expectancy | 0.4551 |

</details>


---
