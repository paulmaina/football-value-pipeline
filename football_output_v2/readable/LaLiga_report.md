# La Liga — football model report

Fixtures in this report: **4**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 2,009 |
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
| Training sha256 | 879e096359a83b7f7de6107d7551b944395a93eb240cf59fc6db085f4e26a660 |
| Training as of utc | 2026-11-04T19:38:39.147257+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 109, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 109, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 106, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-04T19:38:39.147257+00:00', 'observations': 578, 'observations_sha256': '1a64d4e6fc100f7c1baf83a358cdd5d95b6e9b4e5aa88d9d16ef8399e6e29328', 'eligible_training_matches': 175, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 182, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 30, 'retrospective_eligible_training_matches': 175, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'bc39a99e1675b61581d7db236a5ef4df6636a1a3e3a9db659eda846816f0d1e7', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 113, 'tuning_matches': 22, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-13T00:00:00+00:00', 'audit_origin_utc': '2026-10-09T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 17, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8357146014428597, 'audit_candidate_poisson_score': 0.8431377996603822, 'audit_gain': -0.007423198217522464, 'audit_gain_lower95': -0.03863242190580627, 'audit_baseline_briers': [0.5199253099261665, 0.2034007044543571, 0.2297020942314571, 0.28429820925673943], 'audit_candidate_briers': [0.5205799373077185, 0.21289054512942154, 0.2329402725030952, 0.2885161094608111], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2009, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1630, 'tuning_matches': 230, 'audit_matches': 129, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8431809848602122, 'audit_candidate_poisson_score': 0.8399549178032156, 'audit_gain': 0.0032260670569965733, 'audit_gain_lower95': -0.005435961271080973, 'audit_baseline_briers': [0.5718814609185049, 0.1849565358388256, 0.20364650089472794, 0.2524583009932362], 'audit_candidate_briers': [0.5742713139409952, 0.18172216617011255, 0.20421601198958697, 0.24866875431667887], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1848.998 |
| Base scoring parameter | 0.089 |
| Home-advantage parameter | 0.289 |
| Dixon-Coles low-score adjustment | -0.021 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2009, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 4.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261104T193839147257Z_bd717103e18bd5bb1118f3356fa9f385cdbccbcef696864a56e2409beb245aed.json |
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

## 2026-11-06 — Sevilla vs Alavés

The model's most likely 1X2 outcome is **Sevilla win** at **49.5%**. Expected goals are 1.52 for Sevilla and 1.05 for Alavés (2.57 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 47.3%; Under 3.5 goals: 74.1%; Double Chance 1X: 76.5%; Double Chance X2: 50.5%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 88.1%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 49.5% | 2.02 |
| Draw | 27.1% | 3.70 |
| Alavés win | 23.5% | 4.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.52 |
| Alavés expected goals | 1.05 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 47.3% |
| Under 2.5 | 52.7% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 11.9% |
| Under 4.5 | 88.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.87% |
| 2 | 1-0 | 11.73% |
| 3 | 2-1 | 9.61% |
| 4 | 2-0 | 9.12% |
| 5 | 0-0 | 8.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 49.5% | 50.2% | 2.05 | +1.4% |
| Draw | 27.1% | 27.4% | 3.50 | -5.3% |
| Alavés win | 23.5% | 22.4% | 4.26 | +0.0% |
| Over 2.5 | 47.3% | 43.0% | 2.28 | +7.8% |
| Under 2.5 | 52.7% | 57.0% | 1.73 | -8.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:00:00+00:00 |
| Fixture id | 9dd0014685fd62d9b2890d7c33a8c9ab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:38:48Z |
| Market best draw last update utc | 2026-11-04T19:39:09Z |
| Market best away last update utc | 2026-11-04T19:39:09Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5209 |
| Dc lambda away | 1.0533 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:38:39.147257+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.29 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.72 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.44 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.14598863634196255, "-10": 3.682459755372858e-08, "-11": 3.4842032574385604e-09, "-12": 3.027371411188611e-10, "-13": 2.4311464299055124e-11, "-14": 1.8066333646791747e-12, "-15": 1.1461853437603636e-13, "-2": 0.06308899606844096, "-3": 0.019705703449524173, "-4": 0.004821620857853478, "-5": 0.0009659687219858639, "-6": 0.0001635062450592948, "-7": 2.3932614931742534e-05, "-8": 3.0835493717273047e-06, "-9": 3.546488124608164e-07, "0": 0.2705583176809922, "1": 0.24277602947035382, "10": 1.6636785396362058e-06, "11": 2.2730159378639448e-07, "12": 2.8518868916394936e-08, "13": 3.3070845803839407e-09, "14": 3.548720574748129e-10, "15": 3.25105429076784e-11, "2": 0.15078018658451575, "3": 0.06800646424647731, "4": 0.024028070823832813, "5": 0.0069511474914536395, "6": 0.0016990078191920226, "7": 0.0003591027896826387, "8": 6.681086973407712e-05, "9": 1.1095894583113639e-05} |
| Raw goal margin distribution | {"-1": 0.16172022634925104, "-10": 4.079277949866904e-08, "-11": 3.859657529233325e-09, "-12": 3.3535979383619197e-10, "-13": 2.693124347100176e-11, "-14": 2.0013143761521994e-12, "-15": 1.2696971344874486e-13, "-2": 0.06988740343074651, "-3": 0.021829170420932676, "-4": 0.005341193917832386, "-5": 0.0010700605490959587, "-6": 0.0001811255151295962, "-7": 2.6511569673305962e-05, "-8": 3.4158295799595293e-06, "-9": 3.9286541516362304e-07, "0": 0.2618456479937648, "1": 0.2346365257865071, "10": 1.607900719924564e-06, "11": 2.1968089843189481e-07, "12": 2.7562722466885246e-08, "13": 3.196208613001358e-09, "14": 3.429743325412101e-10, "15": 3.1420568397681644e-11, "2": 0.1457250092392349, "3": 0.06572642503722255, "4": 0.02322248646934364, "5": 0.00671809775117622, "6": 0.0016420455217470576, "7": 0.00034706322183124, "8": 6.457091498439317e-05, "9": 1.0723884730938932e-05} |
| Unadjusted home-win probability | 47.8% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 73.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 51.1% |
| P home draw | 76.5% |
| P draw away | 50.5% |
| P home away | 72.9% |
| Raw p home draw | 74.0% |
| Raw p draw away | 52.2% |
| Raw p home away | 73.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4730 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.02, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.15, "draw": 3.48, "home": 2.05}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.28, "under": 1.73}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.26, "draw": 3.5, "home": 1.95}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.26 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:09Z |
| Market reference home last update utc | 2026-11-04T19:39:09Z |
| Market reference draw last update utc | 2026-11-04T19:39:09Z |
| Market reference away last update utc | 2026-11-04T19:39:09Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.28 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:48Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:48Z |
| Market best over 2 5 last update utc | 2026-11-04T19:38:48Z |
| Market best under 2 5 last update utc | 2026-11-04T19:38:48Z |
| Home probability edge | -0.7% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +4.3% |
| Under 2.5 probability edge | -4.3% |
| Raw edge prob home | -0.0237 |
| Raw ev home | -0.0199 |
| Raw edge prob draw | -0.0124 |
| Raw ev draw | -0.0835 |
| Raw edge prob away | 0.0361 |
| Raw ev away | 0.1079 |
| Count model | {"corners": {"alpha": 0.01449526018290438, "mu": 8.663498258176089, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,445.5951 |
| Elo away rating | 1,433.5816 |
| Elo rating diff | 72.0135 |
| Elo home expectancy | 0.6022 |

</details>


---

## 2026-11-07 — CA Osasuna vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **43.5%**. Expected goals are 1.12 for CA Osasuna and 1.19 for Athletic Bilbao (2.32 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.5%; Double Chance 1X: 56.5%; Double Chance X2: 71.0%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 46.9%; BTTS No (at least one team does not score): 53.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 29.0% | 3.45 |
| Draw | 27.5% | 3.64 |
| Athletic Bilbao win | 43.5% | 2.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 1.12 |
| Athletic Bilbao expected goals | 1.19 |
| Expected total goals | 2.32 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 67.6% |
| Under 1.5 | 32.4% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.5% |
| Under 3.5 | 79.5% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.41% |
| 2 | 1-1 | 12.88% |
| 3 | 0-0 | 9.69% |
| 4 | 1-0 | 9.26% |
| 5 | 1-2 | 9.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 29.0% | 26.9% | 3.65 | +5.8% |
| Draw | 27.5% | 26.9% | 3.58 | -1.6% |
| Athletic Bilbao win | 43.5% | 46.2% | 2.18 | -5.1% |
| Over 2.5 | 41.3% | 45.4% | 2.17 | -10.5% |
| Under 2.5 | 58.7% | 54.6% | 1.81 | +6.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:30:00+00:00 |
| Fixture id | 71ca5141a1c532e390c6fa14e080d8bd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:38:48Z |
| Market best draw last update utc | 2026-11-04T19:39:09Z |
| Market best away last update utc | 2026-11-04T19:38:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Osasuna |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1205 |
| Dc lambda away | 1.1946 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:38:39.147257+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.9% |
| P btts no | 53.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.32 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.89 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.52 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.24881724071473327, "-10": 2.1145399769596605e-07, "-11": 2.273168976559054e-08, "-12": 2.233937579366627e-09, "-13": 1.8611844095756496e-10, "-2": 0.12521829896863504, "-3": 0.04513132722525212, "-4": 0.012665968544218946, "-5": 0.0029006490798349632, "-6": 0.0005600806099207915, "-7": 9.338997282670192e-05, "-8": 1.3694597069265372e-05, "-9": 1.7914095433679256e-06, "0": 0.2747829843279816, "1": 0.1719805978343185, "10": 8.220612136236346e-08, "11": 8.289181455803319e-09, "12": 7.640866804297059e-10, "13": 5.971076976684915e-11, "2": 0.08124987605668184, "3": 0.0274678509189686, "4": 0.007230638512995385, "5": 0.0015531918563441516, "6": 0.00028130154669930483, "7": 4.399603109507291e-05, "8": 6.051376561203527e-06, "9": 7.424914762669167e-07} |
| Raw goal margin distribution | {"-1": 0.21393537537934995, "-10": 1.8181011188213875e-07, "-11": 1.9544918065320303e-08, "-12": 1.920760286718897e-09, "-13": 1.600263648005254e-10, "-2": 0.10766385688253619, "-3": 0.03880433447283573, "-4": 0.010890317436472036, "-5": 0.0024940050293770265, "-6": 0.00048156251223553117, "-7": 8.02975663420928e-05, "-8": 1.1774741799508884e-05, "-9": 1.540270569747034e-06, "0": 0.2877661101092344, "1": 0.20049798778933997, "10": 9.583733354037194e-08, "11": 9.663672665624579e-09, "12": 8.90785611004674e-10, "13": 6.961185935136246e-11, "2": 0.09472252604443064, "3": 0.03202250083731139, "4": 0.008429604795793941, "5": 0.0018107382214579684, "6": 0.0003279462612961394, "7": 5.129134225813877e-05, "8": 7.054800594691112e-06, "9": 8.656095444305222e-07} |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 28.8% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 47.3% |
| P home draw | 56.5% |
| P draw away | 71.0% |
| P home away | 72.5% |
| Raw p home draw | 62.6% |
| Raw p draw away | 66.2% |
| Raw p home away | 71.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4125 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.12, "draw": 3.58, "home": 3.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.18, "draw": 3.54, "home": 3.65}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.17, "under": 1.81}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.58 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.12 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:09Z |
| Market reference home last update utc | 2026-11-04T19:39:09Z |
| Market reference draw last update utc | 2026-11-04T19:39:09Z |
| Market reference away last update utc | 2026-11-04T19:39:09Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:48Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:48Z |
| Market best over 2 5 last update utc | 2026-11-04T19:38:48Z |
| Market best under 2 5 last update utc | 2026-11-04T19:38:48Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | 0.0687 |
| Raw ev home | 0.2332 |
| Raw edge prob draw | 0.0185 |
| Raw ev draw | 0.0302 |
| Raw edge prob away | -0.0872 |
| Raw ev away | -0.1839 |
| Count model | {"corners": {"alpha": 0.01449526018290438, "mu": 9.23857707938921, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,457.7140 |
| Elo away rating | 1,478.3170 |
| Elo rating diff | 39.3971 |
| Elo home expectancy | 0.5565 |

</details>


---

## 2026-11-07 — Espanyol vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Espanyol win** at **41.0%**. Expected goals are 1.29 for Espanyol and 1.14 for Deportivo La Coruña (2.43 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 46.1%; Under 3.5 goals: 75.0%; Double Chance 1X: 69.5%; Double Chance X2: 59.0%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 88.8%; BTTS Yes (both teams score): 52.0%; BTTS No (at least one team does not score): 48.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 41.0% | 2.44 |
| Draw | 28.5% | 3.51 |
| Deportivo La Coruña win | 30.5% | 3.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.29 |
| Deportivo La Coruña expected goals | 1.14 |
| Expected total goals | 2.43 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 72.3% |
| Under 1.5 | 27.7% |
| Over 2.5 | 46.1% |
| Under 2.5 | 53.9% |
| Over 3.5 | 25.0% |
| Under 3.5 | 75.0% |
| Over 4.5 | 11.2% |
| Under 4.5 | 88.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.57% |
| 2 | 1-0 | 10.62% |
| 3 | 2-1 | 8.72% |
| 4 | 0-0 | 8.57% |
| 5 | 0-1 | 8.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 41.0% | 41.5% | 2.35 | -3.7% |
| Draw | 28.5% | 28.8% | 3.43 | -2.2% |
| Deportivo La Coruña win | 30.5% | 29.7% | 3.41 | +4.0% |
| Over 2.5 | 46.1% | 46.1% | 2.10 | -3.1% |
| Under 2.5 | 53.9% | 53.9% | 1.86 | +0.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:15:00+00:00 |
| Fixture id | 262c2c99c38456b8a70cb9daa32f2f6d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:09Z |
| Market best draw last update utc | 2026-11-04T19:38:48Z |
| Market best away last update utc | 2026-11-04T19:38:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.2896 |
| Dc lambda away | 1.1382 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:38:39.147257+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 52.0% |
| P btts no | 48.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.67 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.61 |
| Fair Over 2.5 odds | 2.17 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 4.00 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.89 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.17735491387616437, "-10": 1.330651800021402e-07, "-11": 1.4213935056646486e-08, "-12": 1.3940260175897943e-09, "-13": 1.2572603676730843e-10, "-14": 9.582386995490698e-12, "-2": 0.08637547908352644, "-3": 0.030458763669955417, "-4": 0.008413921121562229, "-5": 0.0019030683641409986, "-6": 0.0003636739296449372, "-7": 6.0097283084101066e-05, "-8": 8.741836964112537e-06, "-9": 1.1351090691546508e-06, "0": 0.28512208957000884, "1": 0.220130504703638, "10": 5.073722240221152e-07, "11": 6.140623717541037e-08, "12": 6.823464472872947e-09, "13": 6.972606836950769e-10, "14": 6.021151498220145e-11, "2": 0.12127340175620166, "3": 0.04845328856470407, "4": 0.01516510144666495, "5": 0.0038863075813943197, "6": 0.0008414549039511961, "7": 0.0001575467365552543, "8": 2.596528967536742e-05, "9": 3.820005247383624e-06} |
| Raw goal margin distribution | {"-1": 0.1918739956644663, "-10": 1.0134175696922974e-07, "-11": 1.037211998042877e-08, "-12": 9.74561834867791e-10, "-13": 8.426283432700697e-11, "-14": 6.200647477116043e-12, "-2": 0.09078019420118455, "-3": 0.030909686340476403, "-4": 0.008219610774665145, "-5": 0.0017866332253783721, "-6": 0.0003277668463686345, "-7": 5.196137404523884e-05, "-8": 7.247625041177021e-06, "-9": 9.020914068831034e-07, "0": 0.27907572294173194, "1": 0.21774969612901557, "10": 3.533030560980991e-07, "11": 4.0969663133925124e-08, "12": 4.361542989900366e-09, "13": 4.2727031161969817e-10, "14": 3.5623746517065864e-11, "2": 0.11653674951207883, "3": 0.04495751392281659, "4": 0.013545493700943828, "5": 0.003335914326643537, "6": 0.0006933945141558407, "7": 0.00012454660743865898, "8": 1.9682619126010207e-05, "9": 2.7757069581382074e-06} |
| Unadjusted home-win probability | 39.7% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 77.3% |
| Raw p btts yes | 49.5% |
| P home draw | 69.5% |
| P draw away | 59.0% |
| P home away | 71.5% |
| Raw p home draw | 67.6% |
| Raw p draw away | 60.3% |
| Raw p home away | 72.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0447 |
| Totals anchor target over 2 5 | 0.4613 |
| Totals anchor reference over odds | 2.10 |
| Totals anchor reference under odds | 1.81 |
| Totals anchor reference last update utc | 2026-11-04T19:39:09Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4358 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.26, "draw": 3.36, "home": 2.35}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.1, "under": 1.81}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.41, "draw": 3.43, "home": 2.32}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.1, "under": 1.86}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.35 |
| Reference draw odds | 3.36 |
| Reference away odds | 3.26 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:09Z |
| Market reference home last update utc | 2026-11-04T19:39:09Z |
| Market reference draw last update utc | 2026-11-04T19:39:09Z |
| Market reference away last update utc | 2026-11-04T19:39:09Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:09Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:09Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:09Z |
| Market best under 2 5 last update utc | 2026-11-04T19:38:48Z |
| Home probability edge | -0.6% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0185 |
| Raw ev home | -0.0671 |
| Raw edge prob draw | -0.0086 |
| Raw ev draw | -0.0428 |
| Raw edge prob away | 0.0272 |
| Raw ev away | 0.1047 |
| Count model | {"corners": {"alpha": 0.01449526018290438, "mu": 9.555121569245042, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,436.9009 |
| Elo away rating | 1,445.5717 |
| Elo rating diff | 51.3291 |
| Elo home expectancy | 0.5733 |

</details>


---

## 2026-11-07 — Málaga vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **Málaga win** at **39.9%**. Expected goals are 1.69 for Málaga and 1.59 for Real Racing Club de Santander (3.28 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 62.9%; Under 3.5 goals: 58.5%; Double Chance 1X: 65.8%; Double Chance X2: 60.1%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 77.0%; BTTS Yes (both teams score): 65.7%; BTTS No (at least one team does not score): 34.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 39.9% | 2.51 |
| Draw | 25.9% | 3.86 |
| Real Racing Club de Santander win | 34.2% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 1.69 |
| Real Racing Club de Santander expected goals | 1.59 |
| Expected total goals | 3.28 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.9% |
| Under 2.5 | 37.1% |
| Over 3.5 | 41.5% |
| Under 3.5 | 58.5% |
| Over 4.5 | 23.0% |
| Under 4.5 | 77.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.37% |
| 2 | 2-1 | 8.43% |
| 3 | 1-2 | 7.62% |
| 4 | 2-2 | 7.50% |
| 5 | 1-0 | 6.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 39.9% | 39.6% | 2.48 | -1.1% |
| Draw | 25.9% | 26.9% | 3.72 | -3.7% |
| Real Racing Club de Santander win | 34.2% | 33.4% | 2.92 | -0.0% |
| Over 2.5 | 62.9% | 57.0% | 1.73 | +8.9% |
| Under 2.5 | 37.1% | 43.0% | 2.28 | -15.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T13:00:00+00:00 |
| Fixture id | de935794b7d93f3607ac9ad54d18f4c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:38:48Z |
| Market best draw last update utc | 2026-11-04T19:38:48Z |
| Market best away last update utc | 2026-11-04T19:38:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Santander |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6932 |
| Dc lambda away | 1.5894 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:38:39.147257+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.89 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.29 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.70 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.35 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.17379289946158893, "-10": 1.2869354718871558e-06, "-11": 1.8230015926970326e-07, "-12": 2.3741603115761234e-08, "-13": 2.85872331164828e-09, "-14": 3.164884219858451e-10, "-15": 2.8434356967962468e-11, "-2": 0.10166404564578226, "-3": 0.044903912399320046, "-4": 0.01587352116801325, "-5": 0.0046527001501349, "-6": 0.001161409266995034, "-7": 0.0002520254844955825, "-8": 4.831762191726616e-05, "-9": 8.29098917821082e-06, "0": 0.25895965635891105, "1": 0.19238224537341797, "10": 2.515242799469348e-06, "11": 3.795560260808187e-07, "12": 5.265802708744732e-08, "13": 6.7544869364418614e-09, "14": 7.966063608111084e-10, "15": 7.624213586511046e-11, "2": 0.11980223794533501, "3": 0.05636992081334991, "4": 0.021227664656619696, "5": 0.0066282626219923224, "6": 0.0017625669800993631, "7": 0.0004074464151873633, "8": 8.32141715756101e-05, "9": 1.5211211017755225e-05} |
| Raw goal margin distribution | {"-1": 0.18311133251442258, "-10": 1.3559384177799354e-06, "-11": 1.9207473484176847e-07, "-12": 2.5014581125142244e-08, "-13": 3.012002426495299e-09, "-14": 3.334579079741025e-10, "-15": 2.9958951198378036e-11, "-2": 0.10711507158622825, "-3": 0.04731157176169723, "-4": 0.016724628116427803, "-5": 0.004902168770534569, "-6": 0.0012236817449556522, "-7": 0.0002655385947098412, "-8": 5.090831766204646e-05, "-9": 8.735535692126371e-06, "0": 0.2347616365827764, "1": 0.19520100115720637, "10": 2.552095759444291e-06, "11": 3.8511722400586834e-07, "12": 5.3429564596678075e-08, "13": 6.8534526652265684e-09, "14": 8.082781176438685e-10, "15": 7.735922419631804e-11, "2": 0.1215575623541116, "3": 0.05719584443231958, "4": 0.021538689213023144, "5": 0.006725378931067228, "6": 0.0017883918469410306, "7": 0.00041341625890742165, "8": 8.443341312758712e-05, "9": 1.543408339847569e-05} |
| Unadjusted home-win probability | 40.5% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 58.4% |
| Raw p btts yes | 65.2% |
| P home draw | 65.8% |
| P draw away | 60.1% |
| P home away | 74.1% |
| Raw p home draw | 63.9% |
| Raw p draw away | 59.5% |
| Raw p home away | 76.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6294 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.14, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:09Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.9, "draw": 3.58, "home": 2.46}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.92, "draw": 3.72, "home": 2.48}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:48Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.73, "under": 2.28}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.46 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:09Z |
| Market reference home last update utc | 2026-11-04T19:39:09Z |
| Market reference draw last update utc | 2026-11-04T19:39:09Z |
| Market reference away last update utc | 2026-11-04T19:39:09Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:48Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:48Z |
| Market best over 2 5 last update utc | 2026-11-04T19:38:48Z |
| Market best under 2 5 last update utc | 2026-11-04T19:38:48Z |
| Home probability edge | +0.3% |
| Draw probability edge | -1.0% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +5.9% |
| Under 2.5 probability edge | -5.9% |
| Raw edge prob home | 0.0083 |
| Raw ev home | 0.0032 |
| Raw edge prob draw | -0.0346 |
| Raw ev draw | -0.1267 |
| Raw edge prob away | 0.0262 |
| Raw ev away | 0.0533 |
| Count model | {"corners": {"alpha": 0.01449526018290438, "mu": 10.728190046086944, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,392.6833 |
| Elo away rating | 1,397.9822 |
| Elo rating diff | 54.7011 |
| Elo home expectancy | 0.5781 |

</details>


---
