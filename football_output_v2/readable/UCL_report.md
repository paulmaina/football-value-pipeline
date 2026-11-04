# UEFA Champions League — football model report

Fixtures in this report: **7**.

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
| Training sha256 | 9bed1cd7f17667c912add5c70be4d4d3eed8ab3fb1683647cd560f54d920573d |
| Training as of utc | 2026-11-04T19:40:38.048372+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 50, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 54, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-04T19:40:38.048372+00:00', 'observations': 403, 'observations_sha256': '76871ac374e244312581862c204ae0070fdb5fdaea99a97e4f752a522ddd69f6', 'eligible_training_matches': 17, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 104, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 2, 'retrospective_eligible_training_matches': 17, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': 'bf043dfd636691a132abd41ec1026619ff4a829e22f53dfb0ebdc98faf777280', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 835.457 |
| Base scoring parameter | 0.206 |
| Home-advantage parameter | 0.294 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 71, 'matches': 566, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-03'} |
| Training data health | {'completed_matches': 63, 'latest_completed_utc': '2026-11-03T20:00:00+00:00', 'latest_completed_date': '2026-11-03', 'next_fixture_utc': '2026-11-04T20:00:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-11-04T19:40:38.048372+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'd7f64c6b10f6debdfe0256b7fe552e9244d46c68ebb9f8593ebff10aa5f64c64', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0, 'training_end': '2026-11-03', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261104T194038048372Z_45b7482bd214a4e97efdb2356dc348bb2137bfb5a2337eb74d0a6d7a499ea52f.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 5, 'ANCHORED_MAIN': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 7} |
| Legacy comparison status | {'None': 7} |
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

## 2026-11-04 — Borussia Dortmund vs Real Betis

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **58.9%**. Expected goals are 2.15 for Borussia Dortmund and 1.51 for Real Betis (3.66 combined). The most likely exact score is 2-1 at 10.0%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.7%; Under 3.5 goals: 49.8%; Double Chance 1X: 79.8%; Double Chance X2: 41.1%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 68.4%; BTTS No (at least one team does not score): 31.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 58.9% | 1.70 |
| Draw | 20.9% | 4.78 |
| Real Betis win | 20.2% | 4.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.15 |
| Real Betis expected goals | 1.51 |
| Expected total goals | 3.66 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.9% |
| Under 1.5 | 12.1% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 50.2% |
| Under 3.5 | 49.8% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.04% |
| 2 | 1-1 | 8.36% |
| 3 | 3-1 | 7.19% |
| 4 | 2-2 | 7.13% |
| 5 | 1-0 | 6.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 58.9% | 61.6% | 1.63 | -4.0% |
| Draw | 20.9% | 21.4% | 4.46 | -6.7% |
| Real Betis win | 20.2% | 17.1% | 5.65 | +14.0% |

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
| Market best home last update utc | 2026-11-04T19:40:19Z |
| Market best draw last update utc | 2026-11-04T19:40:18Z |
| Market best away last update utc | 2026-11-04T19:40:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Borussia Dortmund |
| Matched away-team name | Real Betis Balompié |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1476 |
| Dc lambda away | 1.5092 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:40:38.048372+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 68.4% |
| P btts no | 31.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.96 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.25 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 1.99 |
| Fair Under 3.5 odds | 2.01 |
| Fair Over 4.5 odds | 3.27 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.1113937463667586, "-10": 4.2969830870614404e-07, "-11": 5.756989154221351e-08, "-12": 7.095564216682442e-09, "-13": 8.095462597507766e-10, "-14": 8.595642767526868e-11, "-15": 8.526537520460907e-12, "-16": 7.837189816243881e-13, "-17": 5.843518380449761e-14, "-2": 0.056867825984143285, "-3": 0.023156643037310933, "-4": 0.007615760430770911, "-5": 0.0020884951867171037, "-6": 0.0004895381130487307, "-7": 9.999889595998437e-05, "-8": 1.807866336867737e-05, "-9": 2.9290855038038284e-06, "0": 0.2092389549091882, "1": 0.2385737019925863, "10": 2.220231329541049e-05, "11": 4.232916768354764e-06, "12": 7.42405170822386e-07, "13": 1.2053285933198655e-07, "14": 1.8211758475081275e-08, "15": 2.5707270473038476e-09, "16": 3.3624308398146605e-10, "17": 3.567608127789284e-11, "2": 0.17475247079139258, "3": 0.10126095885485291, "4": 0.04739029846043182, "5": 0.018493511597846207, "6": 0.006168536661387145, "7": 0.0017930837771541746, "8": 0.00046129784913021823, "9": 0.00010635475131389542} |
| Raw goal margin distribution | {"-1": 0.1512654108892641, "-10": 5.835021564931689e-07, "-11": 7.817614168672924e-08, "-12": 9.63531142218519e-09, "-13": 1.0993107926533547e-09, "-14": 1.167231983388331e-10, "-15": 1.1578479435001133e-11, "-16": 1.0642390407340274e-12, "-17": 7.935115189926629e-14, "-2": 0.07722278264659926, "-3": 0.03144520440422262, "-4": 0.010341703806260828, "-5": 0.002836039659882443, "-6": 0.0006647606910756423, "-7": 0.00013579195043909333, "-8": 2.454964063950124e-05, "-9": 3.977506248904572e-06, "0": 0.19897831500483154, "1": 0.21348342538964324, "10": 1.9867344364826678e-05, "11": 3.787750131511625e-06, "12": 6.643280360342118e-07, "13": 1.078566810477717e-07, "14": 1.6296467503153524e-08, "15": 2.3003692830204857e-09, "16": 3.008811312077116e-10, "17": 3.1924105515705827e-11, "2": 0.15637413406532702, "3": 0.09061156436783421, "4": 0.04240636399180707, "5": 0.016548589263681673, "6": 0.005519805096353175, "7": 0.0016045090618133934, "8": 0.0004127841590866293, "9": 9.51696537687109e-05} |
| Unadjusted home-win probability | 52.7% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 68.4% |
| P home draw | 79.8% |
| P draw away | 41.1% |
| P home away | 79.1% |
| Raw p home draw | 72.6% |
| Raw p draw away | 47.3% |
| Raw p home away | 80.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7071 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.59, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.59, "price": 2.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.93, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.65, "draw": 4.42, "home": 1.63}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.54, "draw": 4.46, "home": 1.6}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.60 |
| Reference draw odds | 4.46 |
| Reference away odds | 5.54 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:18Z |
| Market reference home last update utc | 2026-11-04T19:40:18Z |
| Market reference draw last update utc | 2026-11-04T19:40:18Z |
| Market reference away last update utc | 2026-11-04T19:40:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.41 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:20Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:20Z |
| Home probability edge | -2.7% |
| Draw probability edge | -0.4% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +9.6% |
| Under 2.5 probability edge | -9.6% |
| Raw edge prob home | -0.0885 |
| Raw ev home | -0.1409 |
| Raw edge prob draw | -0.0147 |
| Raw ev draw | -0.1126 |
| Raw edge prob away | 0.1032 |
| Raw ev away | 0.5478 |
| Elo home rating | 1,519.4389 |
| Elo away rating | 1,458.2663 |
| Elo rating diff | 121.1726 |
| Elo home expectancy | 0.6676 |

</details>


---

## 2026-11-04 — PSV Eindhoven vs Club Brugge

The model's most likely 1X2 outcome is **PSV Eindhoven win** at **51.2%**. Expected goals are 2.45 for PSV Eindhoven and 1.90 for Club Brugge (4.35 combined). The most likely exact score is 2-2 at 7.9%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 80.5%; Under 3.5 goals: 36.7%; Double Chance 1X: 72.1%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 56.5%; BTTS Yes (both teams score): 77.9%; BTTS No (at least one team does not score): 22.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PSV Eindhoven win | 51.2% | 1.95 |
| Draw | 20.9% | 4.78 |
| Club Brugge win | 27.9% | 3.58 |

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
| Over 4.5 | 43.5% |
| Under 4.5 | 56.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.87% |
| 2 | 2-1 | 7.39% |
| 3 | 1-1 | 6.42% |
| 4 | 3-1 | 6.05% |
| 5 | 3-2 | 5.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 51.2% | 51.3% | 1.93 | -1.3% |
| Draw | 20.9% | 21.9% | 4.52 | -5.5% |
| Club Brugge win | 27.9% | 26.8% | 3.62 | +1.1% |

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
| Market best home last update utc | 2026-11-04T19:40:19Z |
| Market best draw last update utc | 2026-11-04T19:40:19Z |
| Market best away last update utc | 2026-11-04T19:40:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | PSV |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.4549 |
| Dc lambda away | 1.8975 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:40:38.048372+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 77.9% |
| P btts no | 22.1% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 89.90 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 14.08 |
| Fair Over 2.5 odds | 1.24 |
| Fair Under 2.5 odds | 5.12 |
| Fair Over 3.5 odds | 1.58 |
| Fair Under 3.5 odds | 2.73 |
| Fair Over 4.5 odds | 2.30 |
| Fair Under 4.5 odds | 1.77 |
| Goal margin distribution | {"-1": 0.13777791712617538, "-10": 2.983427702483965e-06, "-11": 4.975818129454238e-07, "-12": 7.645343431479249e-08, "-13": 1.0886616889060954e-08, "-14": 1.4440872435560067e-09, "-15": 1.7922869978993884e-10, "-16": 2.0857346219881602e-11, "-17": 2.237960235578868e-12, "-18": 1.874174032986997e-13, "-2": 0.08071919723676496, "-3": 0.038608813213389485, "-4": 0.015209810150098932, "-5": 0.00505976891650621, "-6": 0.0014509299919834087, "-7": 0.0003647299203711698, "-8": 8.148752773993328e-05, "-9": 1.6366598867156202e-05, "0": 0.20906471078346686, "1": 0.19441123889257683, "10": 4.29473675006525e-05, "11": 9.267059778387543e-06, "12": 1.8421750717094767e-06, "13": 3.393776812952818e-07, "14": 5.824252647427416e-08, "15": 9.352134934102231e-09, "16": 1.4080520077989112e-09, "17": 1.9546474961854856e-10, "18": 2.1177877611411704e-11, "2": 0.1480288541015123, "3": 0.09160357669846662, "4": 0.046688100831350686, "5": 0.020094145082867748, "6": 0.007454898671909928, "7": 0.002424505169988459, "8": 0.0007008084029105567, "9": 0.00018210548749988002} |
| Raw goal margin distribution | {"-1": 0.1503497655635235, "-10": 3.2556571110985946e-06, "-11": 5.429847575392373e-07, "-12": 8.342959572562366e-08, "-13": 1.18799901405916e-08, "-14": 1.575856153516142e-09, "-15": 1.9558281586587422e-10, "-16": 2.2760520552539812e-11, "-17": 2.4421678290551393e-12, "-18": 2.045187155985136e-13, "-2": 0.08808459754772835, "-3": 0.042131759112042505, "-4": 0.016597662659095503, "-5": 0.0055214586362605554, "-6": 0.0015833232835419783, "-7": 0.00039801050244930657, "-8": 8.892303605395771e-05, "-9": 1.786000510151182e-05, "0": 0.18561824916300904, "1": 0.19363677318409359, "10": 4.277628035780856e-05, "11": 9.230143085413887e-06, "12": 1.834836496891536e-06, "13": 3.3802572048331975e-07, "14": 5.8010508820425066e-08, "15": 9.314879331757286e-09, "16": 1.402442825932611e-09, "17": 1.946860870954396e-10, "18": 2.109351242716659e-11, "2": 0.14743915943148844, "3": 0.09123866040385581, "4": 0.046502111928167625, "5": 0.02001409710623525, "6": 0.007425200988717849, "7": 0.0024148467977416054, "8": 0.0006980166297632696, "9": 0.00018138004355847698} |
| Unadjusted home-win probability | 51.0% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 30.5% |
| Raw p over 1 5 | 92.8% |
| Raw p under 3 5 | 36.8% |
| Raw p btts yes | 77.4% |
| P home draw | 72.1% |
| P draw away | 48.8% |
| P home away | 79.1% |
| Raw p home draw | 69.5% |
| Raw p draw away | 49.0% |
| Raw p home away | 81.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8046 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.51, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.93, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.81, "price": 1.51, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.62, "draw": 4.52, "home": 1.93}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.61, "draw": 4.4, "home": 1.92}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.92 |
| Reference draw odds | 4.40 |
| Reference away odds | 3.61 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:18Z |
| Market reference home last update utc | 2026-11-04T19:40:18Z |
| Market reference draw last update utc | 2026-11-04T19:40:18Z |
| Market reference away last update utc | 2026-11-04T19:40:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.43 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:20Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:20Z |
| Home probability edge | -0.1% |
| Draw probability edge | -1.0% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +6.6% |
| Under 2.5 probability edge | -6.6% |
| Raw edge prob home | -0.0029 |
| Raw ev home | -0.0165 |
| Raw edge prob draw | -0.0335 |
| Raw ev draw | -0.1610 |
| Raw edge prob away | 0.0364 |
| Raw ev away | 0.1033 |
| Elo home rating | 1,466.3756 |
| Elo away rating | 1,460.8471 |
| Elo rating diff | 65.5285 |
| Elo home expectancy | 0.5932 |

</details>


---

## 2026-11-04 — Porto vs Napoli

The model's most likely 1X2 outcome is **Porto win** at **49.3%**. Expected goals are 1.64 for Porto and 0.98 for Napoli (2.62 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 52.8%; Under 3.5 goals: 68.6%; Double Chance 1X: 74.9%; Double Chance X2: 50.7%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 84.7%; BTTS Yes (both teams score): 55.0%; BTTS No (at least one team does not score): 45.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 49.3% | 2.03 |
| Draw | 25.6% | 3.90 |
| Napoli win | 25.1% | 3.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 1.64 |
| Napoli expected goals | 0.98 |
| Expected total goals | 2.62 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.8% |
| Under 2.5 | 47.2% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.3% |
| Under 4.5 | 84.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.08% |
| 2 | 1-0 | 9.82% |
| 3 | 2-1 | 8.83% |
| 4 | 2-0 | 8.31% |
| 5 | 0-1 | 7.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 49.3% | 47.5% | 2.07 | +2.0% |
| Draw | 25.6% | 26.6% | 3.71 | -5.0% |
| Napoli win | 25.1% | 26.0% | 3.98 | -0.1% |
| Over 2.5 | 52.8% | 52.8% | 1.89 | -0.2% |
| Under 2.5 | 47.2% | 47.2% | 2.06 | -2.7% |

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
| Market best home last update utc | 2026-11-04T19:40:18Z |
| Market best draw last update utc | 2026-11-04T19:40:19Z |
| Market best away last update utc | 2026-11-04T19:40:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6436 |
| Dc lambda away | 0.9797 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:40:38.048372+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.0% |
| P btts no | 45.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.44 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.30 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.52 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.16071673519276267, "-10": 3.788393385543167e-08, "-11": 3.6068605920813846e-09, "-12": 3.1545743055790953e-10, "-13": 2.551041337008457e-11, "-14": 1.9177619237248486e-12, "-15": 1.3395534334082805e-13, "-16": 7.951720888860032e-15, "-2": 0.06441410976090138, "-3": 0.019920765974019768, "-4": 0.004856231554999534, "-5": 0.0009727811267727382, "-6": 0.00016500447195253292, "-7": 2.423793447561365e-05, "-8": 3.1371774777445874e-06, "-9": 3.6273078149459e-07, "0": 0.2561171966637424, "1": 0.21914855174535486, "10": 5.524518088769468e-06, "11": 8.824651732790814e-07, "12": 1.2949048795699746e-07, "13": 1.7568856255632122e-08, "14": 2.2158970179426584e-09, "15": 2.596831741726661e-10, "16": 2.5862695378648617e-11, "2": 0.1496198575589281, "3": 0.07763242443297577, "4": 0.03175158357662304, "5": 0.010671120583459792, "6": 0.00303682309618269, "7": 0.0007484249792308365, "8": 0.00016252517530603424, "9": 3.152788618180006e-05} |
| Raw goal margin distribution | {"-1": 0.15175786800198024, "-10": 1.8832680848270407e-08, "-11": 1.6572329311023864e-09, "-12": 1.3392313169562725e-10, "-13": 1.0002598166588587e-11, "-14": 6.91300643652546e-13, "-15": 4.0772626566313304e-14, "-2": 0.05770442724611453, "-3": 0.016755219282384236, "-4": 0.0038118251523240696, "-5": 0.0007101166737712843, "-6": 0.00011177777653913716, "-7": 1.5215420438177477e-05, "-8": 1.8231816506756946e-06, "-9": 1.9501668441363146e-07, "0": 0.23407461480957886, "1": 0.25065321328119633, "10": 3.328135690201812e-06, "11": 4.913617210327648e-07, "12": 6.66196351392464e-08, "13": 8.348113853971743e-09, "14": 9.679911577600663e-10, "15": 9.578599309182862e-11, "2": 0.16243024908509057, "3": 0.07912920078988052, "4": 0.030202891503233003, "5": 0.009440046836901559, "6": 0.002493037396692997, "7": 0.0005693589762549874, "8": 0.00011446192447385156, "9": 2.0541481301438343e-05} |
| Unadjusted home-win probability | 53.5% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 73.1% |
| Raw p under 3 5 | 73.1% |
| Raw p btts yes | 49.8% |
| P home draw | 74.9% |
| P draw away | 50.7% |
| P home away | 74.4% |
| Raw p home draw | 76.9% |
| Raw p draw away | 46.5% |
| Raw p home away | 76.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0842 |
| Totals anchor target over 2 5 | 0.5279 |
| Totals anchor reference over odds | 1.85 |
| Totals anchor reference under odds | 2.06 |
| Totals anchor reference last update utc | 2026-11-04T19:40:18Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4785 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.86, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.98, "draw": 3.71, "home": 2.02}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.89, "under": 2.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.73, "draw": 3.65, "home": 2.07}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.85, "under": 2.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.07 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.73 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:18Z |
| Market reference home last update utc | 2026-11-04T19:40:18Z |
| Market reference draw last update utc | 2026-11-04T19:40:18Z |
| Market reference away last update utc | 2026-11-04T19:40:18Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:18Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:18Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:19Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:19Z |
| Home probability edge | +1.8% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0604 |
| Raw ev home | 0.1076 |
| Raw edge prob draw | -0.0315 |
| Raw ev draw | -0.1316 |
| Raw edge prob away | -0.0289 |
| Raw ev away | -0.0811 |
| Elo home rating | 1,455.3386 |
| Elo away rating | 1,429.7462 |
| Elo rating diff | 85.5924 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-04 — RB Leipzig vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **58.2%**. Expected goals are 1.24 for RB Leipzig and 1.76 for Manchester City (3.01 combined). The most likely exact score is 1-2 at 11.1%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 58.7%; Under 3.5 goals: 64.1%; Double Chance 1X: 41.8%; Double Chance X2: 78.7%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 21.3% | 4.69 |
| Draw | 20.5% | 4.87 |
| Manchester City win | 58.2% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.24 |
| Manchester City expected goals | 1.76 |
| Expected total goals | 3.01 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 80.0% |
| Under 1.5 | 20.0% |
| Over 2.5 | 58.7% |
| Under 2.5 | 41.3% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.08% |
| 2 | 0-1 | 10.74% |
| 3 | 1-1 | 9.47% |
| 4 | 0-2 | 8.92% |
| 5 | 1-3 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 21.3% | 18.7% | 5.23 | +11.5% |
| Draw | 20.5% | 19.7% | 4.97 | +2.0% |
| Manchester City win | 58.2% | 61.6% | 1.60 | -6.9% |

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
| Market best home last update utc | 2026-11-04T19:40:19Z |
| Market best draw last update utc | 2026-11-04T19:40:19Z |
| Market best away last update utc | 2026-11-04T19:40:19Z |
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
| Dc lambda away | 1.7647 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:40:38.048372+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.69 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.01 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.25 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.2669356162645679, "-10": 5.636031761730393e-06, "-11": 8.896163934700995e-07, "-12": 1.2903563330245356e-07, "-13": 1.7309751812080286e-08, "-14": 2.15878963169724e-09, "-15": 2.497732981056782e-10, "-16": 2.422994088477899e-11, "-2": 0.17511958447702336, "-3": 0.08837279821481017, "-4": 0.035365126436680515, "-5": 0.011670195178241779, "-6": 0.00326815258507246, "-7": 0.0007937449337546512, "-8": 0.00017003741785388945, "-9": 3.256327293280903e-05, "0": 0.2051408911929139, "1": 0.1269862205238132, "10": 1.1236822294923101e-07, "11": 1.2481673743550355e-08, "12": 1.274030060093757e-09, "13": 1.2027097361829549e-10, "14": 1.055553566642011e-11, "15": 8.594407282810003e-13, "16": 5.867083175710374e-14, "2": 0.05805037808521859, "3": 0.020615264413845192, "4": 0.005805578293135609, "5": 0.0013481814861460014, "6": 0.000265688362776065, "7": 4.5409962404177265e-05, "8": 6.8456492828998675e-06, "9": 9.22567522483525e-07} |
| Raw goal margin distribution | {"-1": 0.2304130479844989, "-10": 4.864900663801448e-06, "-11": 7.678976212498442e-07, "-12": 1.1138076658290761e-07, "-13": 1.494140321433767e-08, "-14": 1.863420498011377e-09, "-15": 2.1559890630941372e-10, "-16": 2.0914760682264217e-11, "-2": 0.15115943606842616, "-3": 0.07628148720106297, "-4": 0.0305264119065941, "-5": 0.010073459957203976, "-6": 0.0028209985948769727, "-7": 0.0006851434516980918, "-8": 0.00014677261980768126, "-9": 2.8107912588791492e-05, "0": 0.2230296122350063, "1": 0.1637520495664498, "10": 1.4490175971987274e-07, "11": 1.6095444443460925e-08, "12": 1.6428950534085491e-09, "13": 1.5509256320968345e-10, "14": 1.3611639062239177e-11, "15": 1.108271276650088e-12, "16": 7.565757064320563e-14, "2": 0.07485747942060587, "3": 0.026583922146800158, "4": 0.007486444911093099, "5": 0.001738515254909491, "6": 0.000342612086343466, "7": 5.8557333100759685e-05, "8": 8.827643629867194e-06, "9": 1.189674927302754e-06} |
| Unadjusted home-win probability | 27.5% |
| Unadjusted draw probability | 22.3% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 58.4% |
| P home draw | 41.8% |
| P draw away | 78.7% |
| P home away | 79.5% |
| Raw p home draw | 49.8% |
| Raw p draw away | 72.5% |
| Raw p home away | 77.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5867 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.67, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.41, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.6, "draw": 4.97, "home": 5.23}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.6, "draw": 4.82, "home": 5.09}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.09 |
| Reference draw odds | 4.82 |
| Reference away odds | 1.60 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:18Z |
| Market reference home last update utc | 2026-11-04T19:40:18Z |
| Market reference draw last update utc | 2026-11-04T19:40:18Z |
| Market reference away last update utc | 2026-11-04T19:40:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.91 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:20Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:20Z |
| Home probability edge | +2.6% |
| Draw probability edge | +0.8% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -18.9% |
| Under 2.5 probability edge | +18.9% |
| Raw edge prob home | 0.0882 |
| Raw ev home | 0.4374 |
| Raw edge prob draw | 0.0256 |
| Raw ev draw | 0.1085 |
| Raw edge prob away | -0.1137 |
| Raw ev away | -0.1966 |
| Elo home rating | 1,451.6590 |
| Elo away rating | 1,506.5247 |
| Elo rating diff | 5.1343 |
| Elo home expectancy | 0.5074 |

</details>


---

## 2026-11-04 — RC Lens vs Como

The model's most likely 1X2 outcome is **Como win** at **57.0%**. Expected goals are 1.35 for RC Lens and 3.13 for Como (4.48 combined). The most likely exact score is 2-2 at 7.9%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 79.7%; Under 3.5 goals: 36.6%; Double Chance 1X: 43.0%; Double Chance X2: 78.2%; Double Chance 12 (either team wins): 78.7%; Under 4.5 goals: 56.8%; BTTS Yes (both teams score): 73.5%; BTTS No (at least one team does not score): 26.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 21.8% | 4.59 |
| Draw | 21.3% | 4.70 |
| Como win | 57.0% | 1.76 |

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
| Over 2.5 | 79.7% |
| Under 2.5 | 20.3% |
| Over 3.5 | 63.4% |
| Under 3.5 | 36.6% |
| Over 4.5 | 43.2% |
| Under 4.5 | 56.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.90% |
| 2 | 1-1 | 7.09% |
| 3 | 1-3 | 6.11% |
| 4 | 1-2 | 5.86% |
| 5 | 2-1 | 5.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 21.8% | 25.3% | 3.82 | -16.8% |
| Draw | 21.3% | 24.5% | 3.94 | -16.3% |
| Como win | 57.0% | 50.2% | 2.00 | +14.0% |

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
| Market best home last update utc | 2026-11-04T19:40:19Z |
| Market best draw last update utc | 2026-11-04T19:40:18Z |
| Market best away last update utc | 2026-11-04T19:40:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3526 |
| Dc lambda away | 3.1301 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:40:38.048372+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 73.5% |
| P btts no | 26.5% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 72.00 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.90 |
| Fair Over 2.5 odds | 1.25 |
| Fair Under 2.5 odds | 4.93 |
| Fair Over 3.5 odds | 1.58 |
| Fair Under 3.5 odds | 2.73 |
| Fair Over 4.5 odds | 2.31 |
| Fair Under 4.5 odds | 1.76 |
| Goal margin distribution | {"-1": 0.14756470906139038, "-10": 0.00032119335251894773, "-11": 8.862838015302025e-05, "-12": 2.2520544258982268e-05, "-13": 5.3015290632608074e-06, "-14": 1.1622828638354687e-06, "-15": 2.3839693723976083e-07, "-16": 4.593268084302686e-08, "-17": 8.342687983584115e-09, "-18": 1.4314057005793019e-09, "-19": 2.2924410042072724e-10, "-2": 0.14768095284613603, "-20": 2.9609984927939437e-11, "-3": 0.11879243016709586, "-4": 0.07828080057211344, "-5": 0.043406576669058235, "-6": 0.020697587680019575, "-7": 0.008636926943788691, "-8": 0.003199357554188188, "-9": 0.0010644361770886976, "0": 0.21256152269973624, "1": 0.13371204897486966, "10": 1.5038927520762512e-07, "11": 1.793194606876807e-08, "12": 1.9689640583002072e-09, "13": 2.0029234326469664e-10, "14": 1.8974892760353147e-11, "15": 1.6817926929512666e-12, "16": 1.4002251618229532e-13, "17": 1.0989713729241488e-14, "18": 8.147932362604228e-16, "19": 5.638805764449047e-17, "2": 0.05687749339852259, "20": 3.1472514896730126e-18, "3": 0.019770107198825847, "4": 0.005629629452940958, "5": 0.0013489143719087058, "6": 0.00027794116364077696, "7": 5.0118340323461087e-05, "8": 8.022403612310153e-06, "9": 1.1533620304263125e-06} |
| Raw goal margin distribution | {"-1": 0.18872116452287874, "-10": 0.0004107756109840981, "-11": 0.00011334723063965074, "-12": 2.880162448919966e-05, "-13": 6.780149162590292e-06, "-14": 1.48644873807031e-06, "-15": 3.0488690623079925e-07, "-16": 5.8743510379215846e-08, "-17": 1.0669500868652929e-08, "-18": 1.8306311342072294e-09, "-19": 2.931813024034147e-10, "-2": 0.1888698292176101, "-20": 3.7868341777984775e-11, "-3": 0.1519241687272964, "-4": 0.1001136649658318, "-5": 0.05551286448529054, "-6": 0.02647023719040212, "-7": 0.011045804387095855, "-8": 0.004091672644441529, "-9": 0.0013613121740164084, "0": 0.1363567108556723, "1": 0.08290892259907104, "10": 9.324973234284055e-08, "11": 1.1118805971970617e-08, "12": 1.2208674533186269e-09, "13": 1.2419241580869273e-10, "14": 1.1765491047777327e-11, "15": 1.0428052017495136e-12, "16": 8.682176397182391e-14, "17": 6.814235006860712e-15, "18": 5.052172177247712e-16, "19": 3.4963738440936356e-17, "2": 0.035267215886382534, "20": 1.9514713308009508e-18, "3": 0.012258568319679634, "4": 0.003490684019531064, "5": 0.0008364020902437331, "6": 0.00017233901207900758, "7": 3.107616426888118e-05, "8": 4.9743373559142535e-06, "9": 7.151487397167508e-07} |
| Unadjusted home-win probability | 13.5% |
| Unadjusted draw probability | 13.6% |
| Unadjusted away-win probability | 72.9% |
| Raw p over 1 5 | 93.6% |
| Raw p under 3 5 | 34.5% |
| Raw p btts yes | 70.7% |
| P home draw | 43.0% |
| P draw away | 78.2% |
| P home away | 78.7% |
| Raw p home draw | 27.1% |
| Raw p draw away | 86.5% |
| Raw p home away | 86.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7972 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.85, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.51, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.0, "draw": 3.92, "home": 3.82}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.96, "draw": 3.94, "home": 3.82}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.82 |
| Reference draw odds | 3.94 |
| Reference away odds | 1.96 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:18Z |
| Market reference home last update utc | 2026-11-04T19:40:18Z |
| Market reference draw last update utc | 2026-11-04T19:40:18Z |
| Market reference away last update utc | 2026-11-04T19:40:18Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:20Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:20Z |
| Home probability edge | -3.5% |
| Draw probability edge | -3.3% |
| Away probability edge | +6.8% |
| Over 2.5 probability edge | +17.6% |
| Under 2.5 probability edge | -17.6% |
| Raw edge prob home | -0.1181 |
| Raw ev home | -0.4844 |
| Raw edge prob draw | -0.1089 |
| Raw ev draw | -0.4628 |
| Raw edge prob away | 0.2270 |
| Raw ev away | 0.4573 |
| Elo home rating | 1,454.3021 |
| Elo away rating | 1,441.7871 |
| Elo rating diff | 72.5150 |
| Elo home expectancy | 0.6029 |

</details>


---

## 2026-11-04 — Slavia Praha vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **81.0%**. Expected goals are 0.32 for Slavia Praha and 3.11 for Arsenal (3.43 combined). The most likely exact score is 0-2 at 17.1%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 53.5%; Under 3.5 goals: 67.8%; Double Chance 1X: 19.0%; Double Chance X2: 94.3%; Double Chance 12 (either team wins): 86.7%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 23.6%; BTTS No (at least one team does not score): 76.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Slavia Praha win | 5.7% | 17.64 |
| Draw | 13.3% | 7.49 |
| Arsenal win | 81.0% | 1.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Slavia Praha expected goals | 0.32 |
| Arsenal expected goals | 3.11 |
| Expected total goals | 3.43 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 53.5% |
| Under 2.5 | 46.5% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 17.14% |
| 2 | 0-3 | 15.35% |
| 3 | 0-1 | 12.93% |
| 4 | 0-4 | 10.32% |
| 5 | 0-0 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Slavia Praha win | 5.7% | 7.2% | 12.50 | -29.1% |
| Draw | 13.3% | 16.1% | 5.99 | -20.1% |
| Arsenal win | 81.0% | 76.7% | 1.31 | +6.1% |
| Over 2.5 | 53.5% | 53.5% | 1.86 | -0.4% |
| Under 2.5 | 46.5% | 46.5% | 2.10 | -2.5% |

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
| Market best home last update utc | 2026-11-04T19:40:18Z |
| Market best draw last update utc | 2026-11-04T19:40:19Z |
| Market best away last update utc | 2026-11-04T19:40:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
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
| Dc lambda away | 3.1121 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:40:38.048372+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 23.6% |
| P btts no | 76.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.14 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.22 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.10 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.04 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.18279483963839457, "-10": 0.0002749149957610549, "-11": 6.679303633945465e-05, "-12": 1.4888315746017545e-05, "-13": 3.0654148982199676e-06, "-14": 5.863835278329511e-07, "-15": 1.0473720543687913e-07, "-16": 1.7544783795588977e-08, "-17": 2.7668947400598277e-09, "-18": 4.119327228538336e-10, "-19": 5.607843837270162e-11, "-2": 0.21786175623894513, "-3": 0.18418553091359338, "-4": 0.11942718255814756, "-5": 0.06266965279668173, "-6": 0.027589949829021018, "-7": 0.010455503490270966, "-8": 0.0034768692896438697, "-9": 0.0010298004490255236, "0": 0.13344686727009739, "1": 0.050476897342733244, "10": 8.854774426008223e-14, "11": 2.2081888644633382e-15, "12": 5.052153722390963e-17, "13": 1.0676925354038865e-18, "14": 2.0963541930402e-20, "15": 3.84334913650436e-22, "16": 6.608194754746976e-24, "17": 1.069678847072024e-25, "18": 1.6346057388103323e-27, "19": 2.2840657148777313e-29, "2": 0.005695769659511518, "3": 0.0004942570635877531, "4": 3.289474454433573e-05, "5": 1.771766870220184e-06, "6": 8.006194852092736e-08, "7": 3.1141975093974106e-09, "8": 1.06295657473878e-10, "9": 3.23151511936898e-12} |
| Raw goal margin distribution | {"-1": 0.1612731285143755, "-10": 0.0008310228298441071, "-11": 0.00023336771435059417, "-12": 6.014148933978911e-05, "-13": 1.4319726535067442e-05, "-14": 3.1682731619318533e-06, "-15": 6.546380392994607e-07, "-16": 1.2687047122546872e-07, "-17": 2.3150774977615528e-08, "-18": 3.991038199179392e-09, "-19": 6.5128866143467e-10, "-2": 0.2153790467851384, "-20": 9.654598865152815e-11, "-3": 0.20706361248340757, "-4": 0.15370219913552025, "-5": 0.09266746254390604, "-6": 0.04697292641623059, "-7": 0.020524290526367315, "-8": 0.007876719519440594, "-9": 0.0026942183387868505, "0": 0.07019660721932669, "1": 0.017995762419649095, "10": 1.0786300694198778e-13, "11": 3.1090399152023524e-15, "12": 8.224048458296374e-17, "13": 2.009889415080839e-18, "14": 4.564424355270061e-20, "15": 9.680339523208647e-22, "16": 1.9256433852184992e-23, "17": 3.606673257934752e-25, "18": 6.381945739086588e-27, "19": 1.0689729042778978e-28, "2": 0.0022691090304941936, "20": 1.6264973898410715e-30, "3": 0.0002239142107531987, "4": 1.7060191768367522e-05, "5": 1.0557401916168612e-06, "6": 5.492921070460183e-08, "7": 2.4634845979379315e-09, "8": 9.704050225167907e-11, "9": 3.4069550159380274e-12} |
| Unadjusted home-win probability | 2.1% |
| Unadjusted draw probability | 7.0% |
| Unadjusted away-win probability | 90.9% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 55.1% |
| Raw p btts yes | 26.0% |
| P home draw | 19.0% |
| P draw away | 94.3% |
| P home away | 86.7% |
| Raw p home draw | 9.1% |
| Raw p draw away | 97.9% |
| Raw p home away | 93.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.8636 |
| Totals anchor target over 2 5 | 0.5355 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.10 |
| Totals anchor reference last update utc | 2026-11-04T19:40:18Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.6154 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.31, "draw": 5.99, "home": 11.4}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.86, "under": 2.1}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.29, "draw": 5.8, "home": 12.5}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.1}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 12.50 |
| Reference draw odds | 5.80 |
| Reference away odds | 1.29 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:18Z |
| Market reference home last update utc | 2026-11-04T19:40:18Z |
| Market reference draw last update utc | 2026-11-04T19:40:18Z |
| Market reference away last update utc | 2026-11-04T19:40:18Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:18Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:18Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:19Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:19Z |
| Home probability edge | -1.6% |
| Draw probability edge | -2.7% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0517 |
| Raw ev home | -0.7437 |
| Raw edge prob draw | -0.0904 |
| Raw ev draw | -0.5795 |
| Raw edge prob away | 0.1421 |
| Raw ev away | 0.1912 |
| Elo home rating | 1,396.4207 |
| Elo away rating | 1,607.4002 |
| Elo rating diff | -150.9796 |
| Elo home expectancy | 0.2954 |

</details>


---

## 2026-11-04 — Viking FK vs Sabah FK

The model's most likely 1X2 outcome is **Viking FK win** at **71.5%**. Expected goals are 3.67 for Viking FK and 0.95 for Sabah FK (4.62 combined). The most likely exact score is 3-0 at 6.7%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 80.3%; Under 3.5 goals: 35.7%; Double Chance 1X: 87.3%; Double Chance X2: 28.5%; Double Chance 12 (either team wins): 84.2%; Under 4.5 goals: 55.1%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 71.5% | 1.40 |
| Draw | 15.8% | 6.32 |
| Sabah FK win | 12.7% | 7.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 3.67 |
| Sabah FK expected goals | 0.95 |
| Expected total goals | 4.62 |
| Over 0.5 | 98.5% |
| Under 0.5 | 1.5% |
| Over 1.5 | 92.9% |
| Under 1.5 | 7.1% |
| Over 2.5 | 80.3% |
| Under 2.5 | 19.7% |
| Over 3.5 | 64.3% |
| Under 3.5 | 35.7% |
| Over 4.5 | 44.9% |
| Under 4.5 | 55.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 6.75% |
| 2 | 3-1 | 6.42% |
| 3 | 4-0 | 6.19% |
| 4 | 1-1 | 6.06% |
| 5 | 4-1 | 5.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 71.5% | 65.3% | 1.51 | +7.9% |
| Draw | 15.8% | 19.0% | 5.24 | -17.0% |
| Sabah FK win | 12.7% | 15.7% | 6.16 | -21.8% |

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
| Market best home last update utc | 2026-11-04T19:40:20Z |
| Market best draw last update utc | 2026-11-04T19:40:20Z |
| Market best away last update utc | 2026-11-04T19:40:20Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Viking FK |
| Matched away-team name | Sabah FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.6712 |
| Dc lambda away | 0.9515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:40:38.048372+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 66.40 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 14.02 |
| Fair Over 2.5 odds | 1.25 |
| Fair Under 2.5 odds | 5.08 |
| Fair Over 3.5 odds | 1.55 |
| Fair Under 3.5 odds | 2.80 |
| Fair Over 4.5 odds | 2.23 |
| Fair Under 4.5 odds | 1.82 |
| Goal margin distribution | {"-1": 0.09009900156081291, "-10": 5.0479316659110785e-09, "-11": 4.256160621367326e-10, "-12": 3.302139491917407e-11, "-13": 2.3720688563512484e-12, "-14": 1.5861162976349502e-13, "-15": 9.918502617515716e-15, "-16": 5.82432329329403e-16, "-17": 3.223411409323762e-17, "-18": 1.686820512287072e-18, "-19": 8.370718831666939e-20, "-2": 0.028005907738240216, "-20": 3.9474599131994215e-21, "-21": 1.7570499228516572e-22, "-22": 6.557845965824892e-24, "-3": 0.0070976321191608075, "-4": 0.0014584150615363832, "-5": 0.00025048734081634474, "-6": 3.6831331564729306e-05, "-7": 4.724772981352096e-06, "-8": 5.368408263452542e-07, "-9": 5.4695687338021016e-08, "0": 0.1583209179781228, "1": 0.12515275323786867, "10": 0.0013724073466424057, "11": 0.0004464761889653317, "12": 0.0001336553768039393, "13": 3.7044952071809784e-05, "14": 9.557570264199015e-06, "15": 2.306053137672805e-06, "16": 5.224917024081318e-07, "17": 1.1157332850405836e-07, "18": 2.2528083663427003e-08, "19": 4.313490614758181e-09, "2": 0.15500061130279735, "20": 7.848642678910208e-10, "21": 1.3479434002389263e-10, "22": 1.9411517741251434e-11, "3": 0.15156815668299245, "4": 0.12016731305493804, "5": 0.07963458445318504, "6": 0.045179776931004806, "7": 0.022362396032239103, "8": 0.009803782116706903, "9": 0.0038540019058475204} |
| Raw goal margin distribution | {"-1": 0.04021340857036985, "-10": 2.253016515167235e-09, "-11": 1.8996295524167546e-10, "-12": 1.4738263714853774e-11, "-13": 1.0587128872135096e-12, "-14": 7.079228583223064e-14, "-15": 4.426872565232939e-15, "-16": 2.5995392643842943e-16, "-17": 1.438688084751276e-17, "-18": 7.528696352944203e-19, "-19": 3.7360584531928583e-20, "-2": 0.012499727974252764, "-20": 1.7618488058105938e-21, "-21": 7.842147549046938e-23, "-22": 2.9269285407926866e-24, "-3": 0.0031678484261265377, "-4": 0.0006509266442332208, "-5": 0.0001117986837085464, "-6": 1.6438732491430908e-05, "-7": 2.1087828167897633e-06, "-8": 2.3960531318990897e-07, "-9": 2.4412035470520478e-08, "0": 0.0852572945690054, "1": 0.1502550271604425, "10": 0.0016476753232349203, "11": 0.0005360272959554687, "12": 0.00016046304817318678, "13": 4.447517242491516e-05, "14": 1.1474561625549073e-05, "15": 2.7685853316857624e-06, "16": 6.272894755038042e-07, "17": 1.3395193530337518e-07, "18": 2.7046610922633108e-08, "19": 5.178660738249708e-09, "2": 0.18608956222418957, "20": 9.422869160943315e-10, "21": 1.6183045676086335e-10, "22": 2.330494575611636e-11, "3": 0.18196864958916723, "4": 0.14426964185558014, "5": 0.09560713879927137, "6": 0.054241624209165236, "7": 0.02684769081196666, "8": 0.011770156949093282, "9": 0.004627010961068475} |
| Unadjusted home-win probability | 85.8% |
| Unadjusted draw probability | 8.5% |
| Unadjusted away-win probability | 5.7% |
| Raw p over 1 5 | 94.3% |
| Raw p under 3 5 | 32.2% |
| Raw p btts yes | 59.6% |
| P home draw | 87.3% |
| P draw away | 28.5% |
| P home away | 84.2% |
| Raw p home draw | 94.3% |
| Raw p draw away | 14.2% |
| Raw p home away | 91.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8030 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.09, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:20Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:20Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.09, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:20Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.16, "draw": 5.24, "home": 1.51}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.0, "draw": 5.0, "home": 1.51}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.51 |
| Reference draw odds | 5.00 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:18Z |
| Market reference home last update utc | 2026-11-04T19:40:18Z |
| Market reference draw last update utc | 2026-11-04T19:40:18Z |
| Market reference away last update utc | 2026-11-04T19:40:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:20Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:20Z |
| Home probability edge | +6.1% |
| Draw probability edge | -3.1% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +7.0% |
| Under 2.5 probability edge | -7.0% |
| Raw edge prob home | 0.2048 |
| Raw ev home | 0.2957 |
| Raw edge prob draw | -0.1044 |
| Raw ev draw | -0.5533 |
| Raw edge prob away | -0.1004 |
| Raw ev away | -0.6510 |
| Elo home rating | 1,428.8826 |
| Elo away rating | 1,421.0274 |
| Elo rating diff | 67.8552 |
| Elo home expectancy | 0.5964 |

</details>


---
