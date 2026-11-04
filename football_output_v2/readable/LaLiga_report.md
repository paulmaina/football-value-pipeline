# La Liga — football model report

Fixtures in this report: **1**.

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
| Training sha256 | 136247952e5a2634175722661c61b35acc8933d6a40fdde4e25de934471c7e0b |
| Training as of utc | 2026-11-04T10:17:48.592362+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 109, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 109, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 104, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-04T10:17:48.592362+00:00', 'observations': 569, 'observations_sha256': '5b6f8ce97645814a67dad074ccb298f96775c919a8571faa8e75eabe0d3efec6', 'eligible_training_matches': 173, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 180, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 30, 'retrospective_eligible_training_matches': 173, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'f217222c6421a59fedbf170b2d1007aac61c6dce82cd8d18940880f28c50a545', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 111, 'tuning_matches': 22, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-13T00:00:00+00:00', 'audit_origin_utc': '2026-10-09T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 17, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8357146014428597, 'audit_candidate_poisson_score': 0.8416171764343858, 'audit_gain': -0.005902574991526133, 'audit_gain_lower95': -0.0343784083572261, 'audit_baseline_briers': [0.5199253099261665, 0.2034007044543571, 0.2297020942314571, 0.28429820925673943], 'audit_candidate_briers': [0.519427815870912, 0.21275508464569426, 0.23114009972363703, 0.2883278648890615], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2009, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1630, 'tuning_matches': 230, 'audit_matches': 129, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8431809848602122, 'audit_candidate_poisson_score': 0.8399549178032156, 'audit_gain': 0.0032260670569965733, 'audit_gain_lower95': -0.005435961271080973, 'audit_baseline_briers': [0.5718814609185049, 0.1849565358388256, 0.20364650089472794, 0.2524583009932362], 'audit_candidate_briers': [0.5742713139409952, 0.18172216617011255, 0.20421601198958697, 0.24866875431667887], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1850.038 |
| Base scoring parameter | 0.089 |
| Home-advantage parameter | 0.289 |
| Dixon-Coles low-score adjustment | -0.020 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2009, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
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
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261104T101748592362Z_d46eb093bc60390be1bad6e3b8d86bc6e6e5de42091141c06d7e4e7ac1c9f257.json |
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
| 2 | 1-0 | 11.74% |
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
| Market best home last update utc | 2026-11-04T10:18:14Z |
| Market best draw last update utc | 2026-11-04T10:18:15Z |
| Market best away last update utc | 2026-11-04T10:18:15Z |
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
| Bbs statistics cutoff utc | 2026-11-04T10:17:48.592362+00:00 |
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
| Goal margin distribution | {"-1": 0.14599242418141486, "-10": 3.682089933607658e-08, "-11": 3.483815540014525e-09, "-12": 3.027001560421838e-10, "-13": 2.430822894019649e-11, "-14": 1.8063735327877755e-12, "-15": 1.1460102755650533e-13, "-2": 0.06308779590321856, "-3": 0.019705155692302596, "-4": 0.004821440630296146, "-5": 0.0009659229147567752, "-6": 0.00016349680314926493, "-7": 2.393098134180206e-05, "-8": 3.0833060876273888e-06, "-9": 3.5461702573849334e-07, "0": 0.2705552202471475, "1": 0.24278153073558653, "10": 1.6635171973105249e-06, "11": 2.2727695734181616e-07, "12": 2.851545140145314e-08, "13": 3.3066503580369345e-09, "14": 3.548214531845808e-10, "15": 3.250559889755393e-11, "2": 0.15077850967227927, "3": 0.06800507339445958, "4": 0.024027335791122862, "5": 0.006950861179022881, "6": 0.0016989193495844208, "7": 0.00035908011615030927, "8": 6.68059033113322e-05, "9": 1.1094944514081267e-05} |
| Raw goal margin distribution | {"-1": 0.161726917092129, "-10": 4.0789311963088556e-08, "-11": 3.859287563470196e-09, "-12": 3.3532399584772995e-10, "-13": 2.6928074853956094e-11, "-14": 2.0010574124830154e-12, "-15": 1.2695227842283584e-13, "-2": 0.06988715198595795, "-3": 0.021828900361134006, "-4": 0.005341076658276299, "-5": 0.0010700263114895466, "-6": 0.00018111784961452411, "-7": 2.6510168983765686e-05, "-8": 3.4156127675757234e-06, "-9": 3.928362628584094e-07, "0": 0.26183532321428227, "1": 0.23464334679687707, "10": 1.607755093430952e-06, "11": 2.196584960928328e-07, "12": 2.755959620152404e-08, "13": 3.1958094355286565e-09, "14": 3.4292762319402354e-10, "15": 3.1415991537122906e-11, "2": 0.1457243227166254, "3": 0.06572550215041671, "4": 0.02322192494445406, "5": 0.006717864102861716, "6": 0.0016419705441210895, "7": 0.00034704353319809527, "8": 6.456652897469298e-05, "9": 1.0723035254872801e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:18:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:18:15Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:18:15Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:18:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.02, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:18:14Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.15, "draw": 3.48, "home": 2.05}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:18:14Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.28, "under": 1.73}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:18:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.26, "draw": 3.5, "home": 1.95}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.26 |
| Market reference 1x2 last update utc | 2026-11-04T10:18:15Z |
| Market reference home last update utc | 2026-11-04T10:18:15Z |
| Market reference draw last update utc | 2026-11-04T10:18:15Z |
| Market reference away last update utc | 2026-11-04T10:18:15Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.28 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-11-04T10:18:14Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:18:14Z |
| Market best over 2 5 last update utc | 2026-11-04T10:18:14Z |
| Market best under 2 5 last update utc | 2026-11-04T10:18:14Z |
| Home probability edge | -0.7% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +4.3% |
| Under 2.5 probability edge | -4.3% |
| Raw edge prob home | -0.0237 |
| Raw ev home | -0.0199 |
| Raw edge prob draw | -0.0125 |
| Raw ev draw | -0.0836 |
| Raw edge prob away | 0.0361 |
| Raw ev away | 0.1079 |
| Count model | {"corners": {"alpha": 0.01449526018290438, "mu": 8.663498258176089, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,445.5951 |
| Elo away rating | 1,433.5816 |
| Elo rating diff | 72.0135 |
| Elo home expectancy | 0.6022 |

</details>


---
