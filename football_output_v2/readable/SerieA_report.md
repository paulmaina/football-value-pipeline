# Serie A — football model report

Fixtures in this report: **4**.

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
| Training sha256 | 8eef22bc415971580cb49dc11e8f7168c040418fb1bb157734ca5a1fe982d7ea |
| Training as of utc | 2026-11-04T19:39:34.288843+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 100, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 100, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 188, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-04T19:39:34.288843+00:00', 'observations': 688, 'observations_sha256': '9afa13aebbeae9aefca6d327ccbca7c57a0ec87ccf31027b5bf891852c6e7f57', 'eligible_training_matches': 248, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 233, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 36, 'retrospective_eligible_training_matches': 248, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '25b382a9664890c12125e0ca51b6ccb856f332e795372110918768cc20746769', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 187, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-10-05T00:00:00+00:00', 'audit_origin_utc': '2026-10-11T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 24, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1620, 'tuning_matches': 250, 'audit_matches': 129, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8311508011954305, 'audit_candidate_poisson_score': 0.8301708166060806, 'audit_gain': 0.0009799845893498915, 'audit_gain_lower95': -0.003523201039368521, 'audit_baseline_briers': [0.5470550783646152, 0.15449888366492173, 0.20909917551654086, 0.23872129172946965], 'audit_candidate_briers': [0.5497559485164174, 0.15368253383849234, 0.20921488521617435, 0.23948125844306573], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1827.523 |
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
| Live odds matched | 4.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261104T193934288843Z_f53fe6566593b7567bbbeb82d24726c2f4336f21d443a4b0858197d8047deeed.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 4} |
| Legacy comparison status | {'None': 4} |
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

The model's most likely 1X2 outcome is **Venezia win** at **38.8%**. Expected goals are 0.95 for Venezia and 1.32 for Udinese (2.27 combined). The most likely exact score is 1-0 at 13.9%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.6%; Under 3.5 goals: 81.1%; Double Chance 1X: 65.7%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 45.0%; BTTS No (at least one team does not score): 55.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 38.8% | 2.58 |
| Draw | 27.0% | 3.71 |
| Udinese win | 34.3% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.95 |
| Udinese expected goals | 1.32 |
| Expected total goals | 2.27 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
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
| 2 | 1-1 | 12.51% |
| 3 | 0-1 | 10.23% |
| 4 | 0-0 | 10.08% |
| 5 | 2-1 | 8.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 38.8% | 44.0% | 2.22 | -14.0% |
| Draw | 27.0% | 26.3% | 3.79 | +2.2% |
| Udinese win | 34.3% | 29.7% | 3.31 | +13.5% |
| Over 2.5 | 39.6% | 56.1% | 1.76 | -30.4% |
| Under 2.5 | 60.4% | 43.9% | 2.24 | +35.4% |

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
| Market best home last update utc | 2026-11-04T19:39:57Z |
| Market best draw last update utc | 2026-11-04T19:39:10Z |
| Market best away last update utc | 2026-11-04T19:39:10Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Bbs statistics cutoff utc | 2026-11-04T19:39:34.288843+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 45.0% |
| P btts no | 55.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.92 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.29 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.65 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.18252461684803467, "-10": 3.88951708803821e-07, "-11": 4.619834945711219e-08, "-12": 5.036639141287083e-09, "-13": 5.057768591984064e-10, "-14": 4.374475399807953e-11, "-2": 0.10240947390235541, "-3": 0.04099687894134062, "-4": 0.01275189334125484, "-5": 0.0032327613446728166, "-6": 0.000690484523685664, "-7": 0.00012729819920414073, "-8": 2.0632341642640788e-05, "-9": 2.9824322408662857e-06, "0": 0.26973911001036754, "1": 0.2496493498668101, "10": 2.6952932745881872e-08, "11": 2.2971285476067835e-09, "12": 1.7970003892584702e-10, "13": 1.2948360605350815e-11, "14": 8.035821936486144e-13, "2": 0.10098631245314613, "3": 0.02900825938297268, "4": 0.006474318221647774, "5": 0.00117771853550103, "6": 0.00018049713394390293, "7": 2.387740451674218e-05, "8": 2.7769104389640095e-06, "9": 2.8802649116861583e-07} |
| Raw goal margin distribution | {"-1": 0.23920888502412063, "-10": 5.097433222865043e-07, "-11": 6.054556286394685e-08, "-12": 6.6008018757229906e-09, "-13": 6.628493221853058e-10, "-14": 5.7329986553250604e-11, "-2": 0.13421343647298276, "-3": 0.053728740102995776, "-4": 0.01671208103752786, "-5": 0.004236717491384164, "-6": 0.0009049192152244044, "-7": 0.0001668315256486938, "-8": 2.7039856458824708e-05, "-9": 3.908646972214124e-06, "0": 0.28563807724, "1": 0.17082873028607937, "10": 1.8443209569428247e-08, "11": 1.5718669137369247e-09, "12": 1.2296418756323248e-10, "13": 8.86023537685343e-12, "14": 5.498709525770143e-13, "2": 0.06910237716159877, "3": 0.01984961755697037, "4": 0.004430212062888112, "5": 0.0008058829801133364, "6": 0.00012350961950577312, "7": 1.633870345866438e-05, "8": 1.9001695164015624e-06, "9": 1.9708923656856942e-07} |
| Unadjusted home-win probability | 26.5% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 45.1% |
| P home draw | 65.7% |
| P draw away | 61.2% |
| P home away | 73.0% |
| Raw p home draw | 55.1% |
| Raw p draw away | 73.5% |
| Raw p home away | 71.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3957 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.25, "draw": 3.66, "home": 2.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.31, "draw": 3.79, "home": 2.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.76, "under": 2.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.22 |
| Reference draw odds | 3.66 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:57Z |
| Market reference home last update utc | 2026-11-04T19:39:57Z |
| Market reference draw last update utc | 2026-11-04T19:39:57Z |
| Market reference away last update utc | 2026-11-04T19:39:57Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:10Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:10Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:10Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:10Z |
| Home probability edge | -5.2% |
| Draw probability edge | +0.7% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -16.6% |
| Under 2.5 probability edge | +16.6% |
| Raw edge prob home | -0.1748 |
| Raw ev home | -0.4113 |
| Raw edge prob draw | 0.0227 |
| Raw ev draw | 0.0826 |
| Raw edge prob away | 0.1521 |
| Raw ev away | 0.4869 |
| Count model | {"corners": {"alpha": 0.02176883148999032, "mu": 9.549493705641533, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,353.0341 |
| Elo away rating | 1,444.2839 |
| Elo rating diff | -31.2498 |
| Elo home expectancy | 0.4551 |

</details>


---

## 2026-11-07 — Cagliari vs Frosinone

The model's most likely 1X2 outcome is **Frosinone win** at **42.8%**. Expected goals are 1.38 for Cagliari and 1.93 for Frosinone (3.31 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 63.4%; Under 3.5 goals: 58.3%; Double Chance 1X: 57.2%; Double Chance X2: 67.4%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 76.7%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 32.6% | 3.07 |
| Draw | 24.7% | 4.06 |
| Frosinone win | 42.8% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.38 |
| Frosinone expected goals | 1.93 |
| Expected total goals | 3.31 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 84.2% |
| Under 1.5 | 15.8% |
| Over 2.5 | 63.4% |
| Under 2.5 | 36.6% |
| Over 3.5 | 41.7% |
| Under 3.5 | 58.3% |
| Over 4.5 | 23.3% |
| Under 4.5 | 76.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.87% |
| 2 | 2-1 | 8.01% |
| 3 | 1-2 | 8.01% |
| 4 | 2-2 | 7.08% |
| 5 | 0-1 | 5.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 32.6% | 34.8% | 2.82 | -8.2% |
| Draw | 24.7% | 25.6% | 3.83 | -5.6% |
| Frosinone win | 42.8% | 39.6% | 2.50 | +6.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:00:00+00:00 |
| Fixture id | 52b256088d29b4abb82e0c63ea9852fe |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:10Z |
| Market best draw last update utc | 2026-11-04T19:39:10Z |
| Market best away last update utc | 2026-11-04T19:39:10Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3808 |
| Dc lambda away | 1.9288 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:39:34.288843+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.65 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.32 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.73 |
| Fair Over 3.5 odds | 2.40 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.28 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.18295765175789416, "-10": 7.781683651751521e-06, "-11": 1.337933812991295e-06, "-12": 2.1149093679484497e-07, "-13": 3.093076756590098e-08, "-14": 4.2058848997476084e-09, "-15": 5.290840383744246e-10, "-16": 5.4679227795561496e-11, "-2": 0.1300318959066027, "-3": 0.06980449469913795, "-4": 0.029976198522409663, "-5": 0.010670463282819728, "-6": 0.0032341145754928666, "-7": 0.0008520212821158134, "-8": 0.0001982932923238634, "-9": 4.1302532151229914e-05, "0": 0.24654784382643843, "1": 0.1822468294751279, "10": 3.844111311940508e-07, "11": 4.731612346232307e-08, "12": 5.3544939356084865e-09, "13": 5.606211925979181e-10, "14": 5.4574320908784124e-11, "15": 4.914821620095686e-12, "16": 3.6362825038455415e-13, "2": 0.09310116832046596, "3": 0.03578003551116591, "4": 0.01099983268442717, "5": 0.0028031409901652523, "6": 0.0006082319245644675, "7": 0.00011471399272420025, "8": 1.9112879428321045e-05, "9": 2.850013504582145e-06} |
| Raw goal margin distribution | {"-1": 0.21436243020314066, "-10": 9.117413798406665e-06, "-11": 1.5675908651434336e-06, "-12": 2.4779346882563854e-07, "-13": 3.624005030546054e-08, "-14": 4.927827284631122e-09, "-15": 6.199015955764188e-10, "-16": 6.406494639206551e-11, "-2": 0.15235194014922354, "-3": 0.0817864734217864, "-4": 0.03512162897684477, "-5": 0.01250205399293952, "-6": 0.0037892520662401665, "-7": 0.000998271189339644, "-8": 0.00023233044164653848, "-9": 4.839213381027111e-05, "0": 0.2256574686967346, "1": 0.15284707308635798, "10": 3.223985648147879e-07, "11": 3.9683164869520214e-08, "12": 4.4907158509888075e-09, "13": 4.701827112469444e-10, "14": 4.577048193709012e-11, "15": 4.121970744493528e-12, "16": 3.049683438820956e-13, "2": 0.0780822421969522, "3": 0.030008059501271195, "4": 0.009225357912104604, "5": 0.0023509429328844767, "6": 0.0005101129588652128, "7": 9.620852159920119e-05, "8": 1.6029621405677323e-05, "9": 2.390254050984328e-06} |
| Unadjusted home-win probability | 27.3% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 50.1% |
| Raw p over 1 5 | 84.5% |
| Raw p under 3 5 | 57.8% |
| Raw p btts yes | 64.2% |
| P home draw | 57.2% |
| P draw away | 67.4% |
| P home away | 75.3% |
| Raw p home draw | 49.9% |
| Raw p draw away | 72.7% |
| Raw p home away | 77.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6337 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.09, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.46, "draw": 3.77, "home": 2.79}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.5, "draw": 3.83, "home": 2.82}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.79 |
| Reference draw odds | 3.77 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:57Z |
| Market reference home last update utc | 2026-11-04T19:39:57Z |
| Market reference draw last update utc | 2026-11-04T19:39:57Z |
| Market reference away last update utc | 2026-11-04T19:39:57Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:10Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:10Z |
| Home probability edge | -2.3% |
| Draw probability edge | -0.9% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | -0.0751 |
| Raw ev home | -0.2297 |
| Raw edge prob draw | -0.0298 |
| Raw ev draw | -0.1357 |
| Raw edge prob away | 0.1049 |
| Raw ev away | 0.2530 |
| Count model | {"corners": {"alpha": 0.02176883148999032, "mu": 10.414982603531172, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,408.9297 |
| Elo away rating | 1,456.3373 |
| Elo rating diff | 12.5924 |
| Elo home expectancy | 0.5181 |

</details>


---

## 2026-11-07 — Parma vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **50.7%**. Expected goals are 0.87 for Parma and 1.31 for Bologna (2.17 combined). The most likely exact score is 0-1 at 15.9%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 37.6%; Under 3.5 goals: 82.3%; Double Chance 1X: 49.3%; Double Chance X2: 78.1%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 92.9%; BTTS Yes (both teams score): 42.1%; BTTS No (at least one team does not score): 57.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 21.9% | 4.57 |
| Draw | 27.5% | 3.64 |
| Bologna win | 50.7% | 1.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 0.87 |
| Bologna expected goals | 1.31 |
| Expected total goals | 2.17 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 64.5% |
| Under 1.5 | 35.5% |
| Over 2.5 | 37.6% |
| Under 2.5 | 62.4% |
| Over 3.5 | 17.7% |
| Under 3.5 | 82.3% |
| Over 4.5 | 7.1% |
| Under 4.5 | 92.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.90% |
| 2 | 1-1 | 12.48% |
| 3 | 0-0 | 11.08% |
| 4 | 0-2 | 10.58% |
| 5 | 1-2 | 9.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 21.9% | 20.8% | 4.63 | +1.3% |
| Draw | 27.5% | 26.8% | 3.69 | +1.4% |
| Bologna win | 50.7% | 52.4% | 1.89 | -4.3% |
| Over 2.5 | 37.6% | 44.9% | 2.19 | -17.7% |
| Under 2.5 | 62.4% | 55.1% | 1.79 | +11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:00:00+00:00 |
| Fixture id | 813cc4970b2dcab8457490a332fb5a6c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:11Z |
| Market best draw last update utc | 2026-11-04T19:39:11Z |
| Market best away last update utc | 2026-11-04T19:39:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8658 |
| Dc lambda away | 1.3051 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:39:34.288843+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.1% |
| P btts no | 57.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.03 |
| Fair Over 1.5 odds | 1.55 |
| Fair Under 1.5 odds | 2.81 |
| Fair Over 2.5 odds | 2.66 |
| Fair Under 2.5 odds | 1.60 |
| Fair Over 3.5 odds | 5.64 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 14.06 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.2695372043830539, "-10": 5.436432859617686e-07, "-11": 6.39582016361988e-08, "-12": 6.905834184255836e-09, "-13": 6.871267233588487e-10, "-14": 5.927193882482902e-11, "-2": 0.1516991454952802, "-3": 0.060585076207144886, "-4": 0.01874607660220299, "-5": 0.00471996965537418, "-6": 0.0010003013756357223, "-7": 0.00018286859202316073, "-8": 2.9377835856205566e-05, "-9": 4.2078872317296815e-06, "0": 0.27476617854520385, "1": 0.14587069220332674, "10": 7.365871666459141e-09, "11": 5.748892843698892e-10, "12": 4.117958512356259e-11, "13": 2.7181943816429258e-12, "14": 1.5555022924490368e-13, "2": 0.054786107840990764, "3": 0.014515460649897845, "4": 0.0029795686924949335, "5": 0.0004976913265921645, "6": 6.997285310968858e-05, "7": 8.486247391056174e-06, "8": 9.044284552447426e-07, "9": 8.594020018903452e-08} |
| Raw goal margin distribution | {"-1": 0.2475430453416901, "-10": 4.992821488023134e-07, "-11": 5.873923061508876e-08, "-12": 6.3423200834493535e-09, "-13": 6.310573786102546e-10, "-14": 5.443536551322558e-11, "-2": 0.13932053846735942, "-3": 0.05564135125947726, "-4": 0.01721640209536016, "-5": 0.004334821477005533, "-6": 0.0009186770685372461, "-7": 0.0001679465670439607, "-8": 2.6980612825005015e-05, "-9": 3.864524833152375e-06, "0": 0.2900284521149888, "1": 0.16325573311825659, "10": 8.243744927778967e-09, "11": 6.434052664315508e-10, "12": 4.608741658318905e-11, "13": 3.0421519897533033e-12, "14": 1.740888887857796e-13, "2": 0.061315580704928166, "3": 0.01624543034762013, "4": 0.003334677198840167, "5": 0.0005570067651159644, "6": 7.831230016290941e-05, "7": 9.497648350901377e-06, "8": 1.012219303848792e-06, "9": 9.618265447478694e-08} |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 46.5% |
| Raw p over 1 5 | 64.1% |
| Raw p under 3 5 | 82.5% |
| Raw p btts yes | 42.5% |
| P home draw | 49.3% |
| P draw away | 78.1% |
| P home away | 72.5% |
| Raw p home draw | 53.5% |
| Raw p draw away | 75.5% |
| Raw p home away | 71.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3757 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:11Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.3, "price": 3.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:11Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.4, "price": 1.3, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.87, "draw": 3.58, "home": 4.59}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:11Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.89, "draw": 3.69, "home": 4.63}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:11Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.19, "under": 1.79}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.59 |
| Reference draw odds | 3.58 |
| Reference away odds | 1.87 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:57Z |
| Market reference home last update utc | 2026-11-04T19:39:57Z |
| Market reference draw last update utc | 2026-11-04T19:39:57Z |
| Market reference away last update utc | 2026-11-04T19:39:57Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.19 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:11Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:11Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:11Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:11Z |
| Home probability edge | +1.1% |
| Draw probability edge | +0.7% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.0372 |
| Raw ev home | 0.1334 |
| Raw edge prob draw | 0.0218 |
| Raw ev draw | 0.0702 |
| Raw edge prob away | -0.0590 |
| Raw ev away | -0.1208 |
| Count model | {"corners": {"alpha": 0.02176883148999032, "mu": 8.403398697248056, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,382.0338 |
| Elo away rating | 1,530.3171 |
| Elo rating diff | -88.2833 |
| Elo home expectancy | 0.3756 |

</details>


---

## 2026-11-07 — Torino vs Lecce

The model's most likely 1X2 outcome is **Torino win** at **52.4%**. Expected goals are 1.34 for Torino and 0.81 for Lecce (2.14 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.1%; Double Chance 1X: 78.8%; Double Chance X2: 47.6%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 86.3%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 52.4% | 1.91 |
| Draw | 26.4% | 3.79 |
| Lecce win | 21.2% | 4.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.34 |
| Lecce expected goals | 0.81 |
| Expected total goals | 2.14 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.56% |
| 2 | 1-0 | 10.87% |
| 3 | 2-1 | 9.62% |
| 4 | 2-0 | 9.41% |
| 5 | 0-0 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 52.4% | 53.9% | 1.87 | -2.0% |
| Draw | 26.4% | 25.4% | 3.85 | +1.6% |
| Lecce win | 21.2% | 20.7% | 4.59 | -2.6% |
| Over 2.5 | 50.4% | 50.4% | 2.01 | +1.3% |
| Under 2.5 | 49.6% | 49.6% | 1.96 | -2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:00:00+00:00 |
| Fixture id | 0d53a5dbd9d4f4716e923b97e92dfb0d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:10Z |
| Market best draw last update utc | 2026-11-04T19:39:10Z |
| Market best away last update utc | 2026-11-04T19:39:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Torino |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3361 |
| Dc lambda away | 0.8068 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:39:34.288843+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.56 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.10 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.29 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.13468400301984598, "-10": 2.490495284665388e-08, "-11": 2.283835060980459e-09, "-12": 1.923535809131096e-10, "-13": 1.497436991385984e-11, "-14": 1.0780670942134538e-12, "-15": 6.584702839548636e-14, "-2": 0.05583474964957796, "-3": 0.016782111921395605, "-4": 0.003962381958987955, "-5": 0.0007672256744958808, "-6": 0.0001256367253804109, "-7": 1.780222391403546e-05, "-8": 2.221415476190011e-06, "-9": 2.4752015714003913e-07, "0": 0.26381337986672937, "1": 0.23696903143320885, "10": 4.077960713623084e-06, "11": 6.193193262486267e-07, "12": 8.638587876646479e-08, "13": 1.1137394937345923e-08, "14": 1.3279246607062224e-09, "15": 1.343248639760992e-10, "2": 0.16155530465092624, "3": 0.08041847729037004, "4": 0.03144547454634654, "5": 0.010083644500472225, "6": 0.0027346615847236933, "7": 0.0006417321889855832, "8": 0.00013261783717224488, "9": 2.447232901136175e-05} |
| Raw goal margin distribution | {"-1": 0.15287916154284306, "-10": 4.164208865124008e-09, "-11": 3.0296136487378267e-10, "-12": 2.0228268675061965e-11, "-13": 1.2448341140485748e-12, "-14": 6.660779219804078e-14, "-2": 0.05388543465308833, "-3": 0.013351280752971739, "-4": 0.00255960714409375, "-5": 0.00039902358492736114, "-6": 5.233594818063996e-05, "-7": 5.919670418628965e-06, "-8": 5.882812686486046e-07, "-9": 5.2116772522495294e-08, "0": 0.287847086371311, "1": 0.25503257227430437, "10": 6.463359830716012e-07, "11": 7.787636323770807e-08, "12": 8.611319638942081e-09, "13": 8.776372763531112e-10, "14": 7.777162998018722e-11, "2": 0.1477939159690972, "3": 0.060645792764613946, "4": 0.019255005447327563, "5": 0.00497120280918012, "6": 0.0010798305124201965, "7": 0.00020227658321536222, "8": 3.3290911379098154e-05, "9": 4.884394801507538e-06} |
| Unadjusted home-win probability | 48.9% |
| Unadjusted draw probability | 28.8% |
| Unadjusted away-win probability | 22.3% |
| Raw p over 1 5 | 63.4% |
| Raw p under 3 5 | 83.0% |
| Raw p btts yes | 41.1% |
| P home draw | 78.8% |
| P draw away | 47.6% |
| P home away | 73.6% |
| Raw p home draw | 77.7% |
| Raw p draw away | 51.1% |
| Raw p home away | 71.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.2665 |
| Totals anchor target over 2 5 | 0.5040 |
| Totals anchor reference over odds | 1.93 |
| Totals anchor reference under odds | 1.96 |
| Totals anchor reference last update utc | 2026-11-04T19:39:57Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3706 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.15, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.34, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.59, "draw": 3.78, "home": 1.82}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:57Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.93, "under": 1.96}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.53, "draw": 3.85, "home": 1.87}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:10Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.01, "under": 1.93}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.82 |
| Reference draw odds | 3.78 |
| Reference away odds | 4.59 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:57Z |
| Market reference home last update utc | 2026-11-04T19:39:57Z |
| Market reference draw last update utc | 2026-11-04T19:39:57Z |
| Market reference away last update utc | 2026-11-04T19:39:57Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:57Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:57Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:10Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:57Z |
| Home probability edge | -1.5% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0500 |
| Raw ev home | -0.0855 |
| Raw edge prob draw | 0.0343 |
| Raw ev draw | 0.1082 |
| Raw edge prob away | 0.0157 |
| Raw ev away | 0.0242 |
| Count model | {"corners": {"alpha": 0.02176883148999032, "mu": 9.026678602780107, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,432.4444 |
| Elo away rating | 1,399.8995 |
| Elo rating diff | 92.5448 |
| Elo home expectancy | 0.6301 |

</details>


---
