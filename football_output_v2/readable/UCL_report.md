# UEFA Champions League — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 548 |
| Training data through | 2026-10-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 4 |
| Training seasons loaded | ['2023', '2024', '2025', '2026'] |
| Training sha256 | 66be1a7d446df6ae24928a837f8907a8fd91f257b46d367c0f54697605dca1b1 |
| Training as of utc | 2026-10-21T17:28:56.715717+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 45, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 34, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 2, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T17:28:56.715717+00:00', 'observations': 119, 'observations_sha256': 'fc113bc506ce659ae4887d05d300490ad49dfc5c970eb2772cbbe5d2109345a8', 'eligible_training_matches': 0, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 36, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 0, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': 'ccc37546f410b84c1ad748739ea7654757e07e07464bd766cea904fcad36a0c5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 465.606 |
| Base scoring parameter | 0.213 |
| Home-advantage parameter | 0.327 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0029 |
| Training data health | {'completed_matches': 45, 'latest_completed_utc': '2026-10-20T19:00:00+00:00', 'latest_completed_date': '2026-10-20', 'next_fixture_utc': '2026-10-21T19:00:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-21T17:28:46.123777+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '6d62c0fdf9f5d06d36ac12d719b95f5fef5b6cfda75cb1b77088f1046e2420b4', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0029422055555555554, 'training_end': '2026-10-20', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261021T172856715717Z_941f768158917ea111c406112295800fed92dfcc835c60c5115e6a1891b415f2.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'UNRELIABLE_AUDIT', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **79.3%**. Expected goals are 3.97 for Aston Villa and 1.34 for Viking FK (5.31 combined). The most likely exact score is 3-1 at 6.6%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 89.3%; Under 3.5 goals: 22.9%; Double Chance 1X: 91.1%; Double Chance X2: 20.7%; Double Chance 12 (either team wins): 88.2%; Under 4.5 goals: 39.8%; BTTS Yes (both teams score): 73.2%; BTTS No (at least one team does not score): 26.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 79.3% | 1.26 |
| Draw | 11.8% | 8.47 |
| Viking FK win | 8.9% | 11.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 3.97 |
| Viking FK expected goals | 1.34 |
| Expected total goals | 5.31 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 96.6% |
| Under 1.5 | 3.4% |
| Over 2.5 | 89.3% |
| Under 2.5 | 10.7% |
| Over 3.5 | 77.1% |
| Under 3.5 | 22.9% |
| Over 4.5 | 60.2% |
| Under 4.5 | 39.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 6.62% |
| 2 | 4-1 | 6.56% |
| 3 | 5-1 | 5.21% |
| 4 | 2-1 | 5.00% |
| 5 | 3-0 | 4.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 79.3% | 75.9% | 1.27 | +0.7% |
| Draw | 11.8% | 14.3% | 6.60 | -22.0% |
| Viking FK win | 8.9% | 9.8% | 9.62 | -14.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | d3b3e714b6af9e5430e3030ed639e6dd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.9681 |
| Dc lambda away | 1.3427 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:28:56.715717+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 23 |
| Score grid omitted mass | 0 |
| P btts yes | 73.2% |
| P btts no | 26.8% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 217.44 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 29.83 |
| Fair Over 2.5 odds | 1.12 |
| Fair Under 2.5 odds | 9.30 |
| Fair Over 3.5 odds | 1.30 |
| Fair Under 3.5 odds | 4.37 |
| Fair Over 4.5 odds | 1.66 |
| Fair Under 4.5 odds | 2.51 |
| Goal margin distribution | {"-1": 0.05646982172269879, "-10": 4.662428145212172e-08, "-11": 5.477304959734783e-09, "-12": 5.931845794199261e-10, "-13": 5.956695837809284e-11, "-14": 5.574631695476429e-12, "-15": 4.883803597814467e-13, "-16": 4.021101198425309e-14, "-17": 3.122502214246281e-15, "-18": 2.2940263869658846e-16, "-19": 1.5990457235310274e-17, "-2": 0.022345040210004677, "-20": 1.0601433720169996e-18, "-21": 6.691222244487278e-20, "-22": 3.959845198747969e-21, "-23": 1.8769458322685345e-22, "-3": 0.007348245879252728, "-4": 0.0020056947551187355, "-5": 0.0004647031904654071, "-6": 9.314433690052388e-05, "-7": 1.6407964386733754e-05, "-8": 2.5736880007586668e-06, "-9": 3.634197368180151e-07, "0": 0.11811667173291979, "1": 0.14052625158301899, "10": 0.0020296524018761845, "11": 0.0007046398507265348, "12": 0.00022551783598254044, "13": 6.692482303939212e-05, "14": 1.8509246978643515e-05, "15": 4.792052033513873e-06, "16": 1.1660014797225529e-06, "17": 2.6757628355016884e-07, "18": 5.809436851611408e-08, "19": 1.1967054596108016e-08, "2": 0.16721088474714998, "20": 2.344670160904221e-09, "21": 4.3733413134098155e-10, "22": 7.648510904924634e-11, "23": 1.0713742026143346e-11, "3": 0.16250167728173961, "4": 0.13107798932298448, "5": 0.08974935788903832, "6": 0.05316219634276136, "7": 0.02767527394128208, "8": 0.012828736511647317, "9": 0.005353370001422102} |
| Raw goal margin distribution | {"-1": 0.050489470768244116, "-10": 4.168660753042629e-08, "-11": 4.8972392725321196e-09, "-12": 5.303642648256655e-10, "-13": 5.325860985629828e-11, "-14": 4.984258767711811e-12, "-15": 4.3665917735770457e-13, "-16": 3.595252565361616e-14, "-17": 2.791818345808487e-15, "-18": 2.051080996413658e-16, "-19": 1.4297012076957394e-17, "-2": 0.019978622564781, "-20": 9.478704936319026e-19, "-21": 5.982598485538823e-20, "-22": 3.540483789567068e-21, "-23": 1.6781707262554956e-22, "-3": 0.006570041027228334, "-4": 0.0017932846894022072, "-5": 0.00041548950280255334, "-6": 8.328002695422225e-05, "-7": 1.467030376576142e-05, "-8": 2.301125470503346e-06, "-9": 3.2493231993506665e-07, "0": 0.09303263587631616, "1": 0.14663579132005564, "10": 0.0021178938646772383, "11": 0.0007352748752847046, "12": 0.00023532248219508008, "13": 6.983445637229118e-05, "14": 1.9313957690306113e-05, "15": 5.000391984170027e-06, "16": 1.2166947295143895e-06, "17": 2.792094689416725e-07, "18": 6.062008772479566e-08, "19": 1.2487336000945859e-08, "2": 0.17448056947380938, "20": 2.446607381579503e-09, "21": 4.5634773359459075e-10, "22": 7.981038676614247e-11, "23": 1.1179534231540733e-11, "3": 0.16956662382022586, "4": 0.13677675503685208, "5": 0.09365131401623686, "6": 0.05547348371722295, "7": 0.02887848817330583, "8": 0.013386480524676647, "9": 0.005586113893629506} |
| Unadjusted home-win probability | 82.8% |
| Unadjusted draw probability | 9.3% |
| Unadjusted away-win probability | 7.9% |
| Raw p over 1 5 | 96.8% |
| Raw p under 3 5 | 22.4% |
| Raw p btts yes | 72.4% |
| P home draw | 91.1% |
| P draw away | 20.7% |
| P home away | 88.2% |
| Raw p home draw | 92.1% |
| Raw p draw away | 17.2% |
| Raw p home away | 90.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:28Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 8.37, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:28Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.1, "price": 8.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.3, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.73, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.29 |
| Reference draw odds | 6.00 |
| Reference away odds | 8.50 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +3.4% |
| Draw probability edge | -2.5% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +11.5% |
| Under 2.5 probability edge | -11.5% |
| Raw edge prob home | 0.0690 |
| Raw ev home | 0.0511 |
| Raw edge prob draw | -0.0502 |
| Raw ev draw | -0.3860 |
| Raw edge prob away | -0.0188 |
| Raw ev away | -0.2367 |
| Market p over 1 5 | 92.4% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 9.00 |
| Market reference over 1 5 last update utc | 2026-10-21T17:28:55Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 43.0% |
| Market under 3 5 odds | 2.22 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market reference under 3 5 odds | 2.22 |
| Market reference under 3 5 opposite odds | 1.70 |
| Market reference under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T17:28:28Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-21T17:28:55Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Bayern Munich win** at **37.1%**. Expected goals are 1.01 for Bayern Munich and 1.21 for Arsenal (2.22 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 38.6%; Under 3.5 goals: 81.6%; Double Chance 1X: 63.4%; Double Chance X2: 62.9%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 92.5%; BTTS Yes (both teams score): 43.8%; BTTS No (at least one team does not score): 56.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 37.1% | 2.70 |
| Draw | 26.3% | 3.80 |
| Arsenal win | 36.6% | 2.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 1.01 |
| Arsenal expected goals | 1.21 |
| Expected total goals | 2.22 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 64.3% |
| Under 1.5 | 35.7% |
| Over 2.5 | 38.6% |
| Under 2.5 | 61.4% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.76% |
| 2 | 0-1 | 12.20% |
| 3 | 1-1 | 12.11% |
| 4 | 0-0 | 9.75% |
| 5 | 2-1 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 37.1% | 42.9% | 2.29 | -15.1% |
| Draw | 26.3% | 25.3% | 3.78 | -0.4% |
| Arsenal win | 36.6% | 31.9% | 3.06 | +12.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 2ebbccdeea2dab59717d5c3d802c3fed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FC Bayern München |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0114 |
| Dc lambda away | 1.2131 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:28:56.715717+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.26 |
| Fair Over 1.5 odds | 1.56 |
| Fair Under 1.5 odds | 2.80 |
| Fair Over 2.5 odds | 2.59 |
| Fair Under 2.5 odds | 1.63 |
| Fair Over 3.5 odds | 5.42 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.25 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.209415052657091, "-10": 2.0342939606242714e-07, "-11": 2.2228931350104444e-08, "-12": 2.229456587642483e-09, "-13": 2.0597755001708703e-10, "-14": 1.6409466850313035e-11, "-2": 0.10405185467463246, "-3": 0.038369663116584574, "-4": 0.010987990711620519, "-5": 0.002563900257699136, "-6": 0.0005039540254387648, "-7": 8.549100256485977e-05, "-8": 1.2748961156181191e-05, "-9": 1.6955141670980211e-06, "0": 0.26340600092909033, "1": 0.23517483363134345, "10": 4.4224661953971765e-08, "11": 4.029040319829377e-09, "12": 3.369102824612149e-10, "13": 2.595179193319411e-11, "14": 1.7237494877350458e-12, "2": 0.09688195717626429, "3": 0.029786075149784746, "4": 0.007111738761866506, "5": 0.0013835372430975458, "6": 0.0002267320233305129, "7": 3.206819914911204e-05, "8": 3.9871371654306954e-06, "9": 4.420994944806584e-07} |
| Raw goal margin distribution | {"-1": 0.23650163468792565, "-10": 2.2974176928495208e-07, "-11": 2.5104110401623342e-08, "-12": 2.517823436057369e-09, "-13": 2.3261951168248814e-10, "-14": 1.8531933044999996e-11, "-2": 0.11751033849107499, "-3": 0.04333254909023365, "-4": 0.012409221458828125, "-5": 0.0028955253905054343, "-6": 0.0005691374584184771, "-7": 9.654875139661718e-05, "-8": 1.4397962876846819e-05, "-9": 1.914818763347577e-06, "0": 0.2742010940788694, "1": 0.19828435666810695, "10": 3.728740235085716e-08, "11": 3.397028735904492e-09, "12": 2.8406117092194143e-10, "13": 2.1880888734567987e-11, "14": 1.4533551611577258e-12, "2": 0.08168466095975319, "3": 0.02511371075529829, "4": 0.0059961626140612664, "5": 0.0011665099872208468, "6": 0.0001911659197880992, "7": 2.703785154050156e-05, "8": 3.361698680030693e-06, "9": 3.727499770821967e-07} |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 41.3% |
| Raw p over 1 5 | 64.5% |
| Raw p under 3 5 | 81.5% |
| Raw p btts yes | 44.0% |
| P home draw | 63.4% |
| P draw away | 62.9% |
| P home away | 73.7% |
| Raw p home draw | 58.7% |
| Raw p draw away | 68.8% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.20 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | -5.8% |
| Draw probability edge | +1.1% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -25.2% |
| Under 2.5 probability edge | +25.2% |
| Raw edge prob home | -0.1163 |
| Raw ev home | -0.2844 |
| Raw edge prob draw | 0.0216 |
| Raw ev draw | 0.0365 |
| Raw edge prob away | 0.0947 |
| Raw ev away | 0.2648 |
| Market p over 1 5 | 83.8% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-21T17:28:55Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 59.8% |
| Market under 3 5 odds | 1.63 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market reference under 3 5 odds | 1.63 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market reference under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.3% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T17:28:27Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.62 |
| Market reference btts yes last update utc | 2026-10-21T17:28:55Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **69.2%**. Expected goals are 4.47 for Club Brugge and 1.35 for RC Lens (5.82 combined). The most likely exact score is 2-2 at 5.6%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.5%; Under 3.5 goals: 19.7%; Double Chance 1X: 84.5%; Double Chance X2: 30.8%; Double Chance 12 (either team wins): 84.8%; Under 4.5 goals: 35.6%; BTTS Yes (both teams score): 76.7%; BTTS No (at least one team does not score): 23.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 69.2% | 1.44 |
| Draw | 15.2% | 6.56 |
| RC Lens win | 15.5% | 6.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Club Brugge expected goals | 4.47 |
| RC Lens expected goals | 1.35 |
| Expected total goals | 5.82 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.1% |
| Under 1.5 | 2.9% |
| Over 2.5 | 90.5% |
| Under 2.5 | 9.5% |
| Over 3.5 | 80.3% |
| Under 3.5 | 19.7% |
| Over 4.5 | 64.4% |
| Under 4.5 | 35.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.64% |
| 2 | 4-1 | 5.31% |
| 3 | 3-1 | 4.75% |
| 4 | 5-1 | 4.74% |
| 5 | 4-0 | 3.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 69.2% | 51.6% | 1.86 | +28.7% |
| Draw | 15.2% | 23.2% | 4.17 | -36.4% |
| RC Lens win | 15.5% | 25.2% | 3.96 | -38.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | d306a78e402e5f505e8644fdf3f75dcd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.4671 |
| Dc lambda away | 1.3550 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:28:56.715717+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 24 |
| Score grid omitted mass | 0 |
| P btts yes | 76.7% |
| P btts no | 23.3% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 233.00 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 35.00 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.56 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.07 |
| Fair Over 4.5 odds | 1.55 |
| Fair Under 4.5 odds | 2.81 |
| Goal margin distribution | {"-1": 0.10021385203596798, "-10": 7.733425946759485e-08, "-11": 9.122826058175792e-09, "-12": 9.927866309329287e-10, "-13": 1.0023465248746333e-10, "-14": 9.435687063446855e-12, "-15": 8.318108738864584e-13, "-16": 6.893784086474039e-14, "-17": 5.389860035082911e-15, "-18": 3.987804276172827e-16, "-19": 2.799906745306048e-17, "-2": 0.03853946937509739, "-20": 1.8702771598395713e-18, "-21": 1.1911607341461418e-19, "-22": 7.235735238060403e-21, "-23": 4.11753534361949e-22, "-24": 1.8564532560150108e-23, "-3": 0.012421559544777767, "-4": 0.0033479042354547144, "-5": 0.0007699183773623928, "-6": 0.00015373225032899005, "-7": 2.7048194034218013e-05, "-8": 4.245713279117844e-06, "-9": 6.008194343993059e-07, "0": 0.15243592796738512, "1": 0.09769942545468958, "10": 0.0035269055179938725, "11": 0.0013716478900580298, "12": 0.000492108103566613, "13": 0.00016379997700633915, "14": 5.083476584545064e-05, "15": 1.477417513514603e-05, "16": 4.036711182151979e-06, "17": 1.0404922243514583e-06, "18": 2.537970310320861e-07, "19": 5.874726063957591e-08, "2": 0.12594960706568287, "20": 1.2937232255042313e-08, "21": 2.7164212826931875e-09, "22": 5.440023477454808e-10, "23": 1.0205793892825908e-10, "24": 1.5169973680673654e-11, "3": 0.13383156689337003, "4": 0.1189177859997838, "5": 0.09015915344401984, "6": 0.05935010267825553, "7": 0.03442596433526633, "8": 0.017815165219435502, "9": 0.008311406343738031} |
| Raw goal margin distribution | {"-1": 0.0377922734589519, "-10": 2.916400699272505e-08, "-11": 3.4403660781873624e-09, "-12": 3.7439598498960526e-10, "-13": 3.7800117647504793e-11, "-14": 3.5583510515780953e-12, "-15": 3.1368940893284905e-13, "-16": 2.599758098007148e-14, "-17": 2.032603878735455e-15, "-18": 1.50386584932201e-16, "-19": 1.0558903707263135e-17, "-2": 0.01453386069885657, "-20": 7.05311934754492e-19, "-21": 4.4920608562436915e-20, "-22": 2.728713438689163e-21, "-23": 1.5527895447738754e-22, "-24": 7.000987157932996e-24, "-3": 0.004684372125865474, "-4": 0.0012625491367727938, "-5": 0.0002903487418875867, "-6": 5.7974931866784215e-05, "-7": 1.0200313876220163e-05, "-8": 1.6011275289082348e-06, "-9": 2.2657878030795384e-07, "0": 0.07335256876080193, "1": 0.12253464254952068, "10": 0.004423445736164945, "11": 0.0017203211086437092, "12": 0.000617202100069904, "13": 0.00020543796996431635, "14": 6.375697536573267e-05, "15": 1.8529773954389606e-05, "16": 5.062844120921115e-06, "17": 1.3049855942662746e-06, "18": 3.18312296443024e-07, "19": 7.368082821093428e-08, "2": 0.15796602701828114, "20": 1.6225879759005763e-08, "21": 3.406936216253288e-09, "22": 6.822878734123907e-10, "23": 1.2800109118057018e-10, "24": 1.9026184583952007e-11, "3": 0.16785158290134258, "4": 0.14914671537164573, "5": 0.11307763160750578, "6": 0.07443691283865495, "7": 0.04317705262453954, "8": 0.022343784438492824, "9": 0.010424167805225037} |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 7.3% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 97.9% |
| Raw p under 3 5 | 16.8% |
| Raw p btts yes | 73.3% |
| P home draw | 84.5% |
| P draw away | 30.8% |
| P home away | 84.8% |
| Raw p home draw | 94.1% |
| Raw p draw away | 13.2% |
| Raw p home away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.91, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.91, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.91, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.85 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +17.6% |
| Draw probability edge | -7.9% |
| Away probability edge | -9.7% |
| Over 2.5 probability edge | +21.5% |
| Under 2.5 probability edge | -21.5% |
| Raw edge prob home | 0.3519 |
| Raw ev home | 0.6145 |
| Raw edge prob draw | -0.1582 |
| Raw ev draw | -0.6941 |
| Raw edge prob away | -0.1937 |
| Raw ev away | -0.7678 |
| Market p over 1 5 | 88.0% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-21T17:28:55Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.0% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 2.03 |
| Market reference under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.42 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T17:28:27Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.90 |
| Market reference btts yes last update utc | 2026-10-21T17:28:55Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **70.6%**. Expected goals are 2.01 for Inter Milan and 1.00 for Shakhtar Donetsk (3.01 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 59.7%; Under 3.5 goals: 63.4%; Double Chance 1X: 87.1%; Double Chance X2: 29.4%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 80.4%; BTTS Yes (both teams score): 52.8%; BTTS No (at least one team does not score): 47.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.6% | 1.42 |
| Draw | 16.5% | 6.05 |
| Shakhtar Donetsk win | 12.9% | 7.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.01 |
| Shakhtar Donetsk expected goals | 1.00 |
| Expected total goals | 3.01 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 80.6% |
| Under 1.5 | 19.4% |
| Over 2.5 | 59.7% |
| Under 2.5 | 40.3% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.6% |
| Under 4.5 | 80.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.96% |
| 2 | 2-0 | 11.47% |
| 3 | 2-1 | 11.44% |
| 4 | 1-1 | 7.74% |
| 5 | 3-0 | 7.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.6% | 79.7% | 1.25 | -11.8% |
| Draw | 16.5% | 13.0% | 6.82 | +12.7% |
| Shakhtar Donetsk win | 12.9% | 7.3% | 10.34 | +33.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | a889456204e8ef1b64294efbee8dc3e5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0145 |
| Dc lambda away | 0.9969 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:28:56.715717+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.8% |
| P btts no | 47.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.40 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.16 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.09 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.08551513387516951, "-10": 1.0972873975199138e-08, "-11": 9.79719370216237e-10, "-12": 8.036643985003164e-11, "-13": 6.096206618406802e-12, "-14": 4.300098139323468e-13, "-15": 2.833604679378653e-14, "-16": 1.7424462525364992e-15, "-17": 9.138322135289055e-17, "-2": 0.03170516611294381, "-3": 0.00913814100748967, "-4": 0.0020810449977412917, "-5": 0.0003899647048478798, "-6": 6.193096377043279e-05, "-7": 8.522310593480699e-06, "-8": 1.033766048460334e-06, "-9": 1.1205022287409041e-07, "0": 0.16519012928992496, "1": 0.27936745397918566, "10": 2.056308023030293e-05, "11": 3.7101675417684914e-06, "12": 6.150219350310264e-07, "13": 9.42756644240312e-08, "14": 1.3438238342155123e-08, "15": 1.7894817825213972e-09, "16": 2.2236757479414032e-10, "17": 2.35669065924421e-11, "2": 0.21365124346613498, "3": 0.12443922435412788, "4": 0.05726706946610769, "5": 0.02168566968556544, "6": 0.006959522188975318, "7": 0.001935320921588824, "8": 0.0004743970139088828, "9": 0.00010390978711051641} |
| Raw goal margin distribution | {"-1": 0.1228313549097863, "-10": 1.5761104690492674e-08, "-11": 1.4072393063278053e-09, "-12": 1.154359263526986e-10, "-13": 8.756407021966204e-12, "-14": 6.176531062550542e-13, "-15": 4.070104159047025e-14, "-16": 2.5027971583247857e-15, "-17": 1.3126009848948753e-16, "-2": 0.04554034280034636, "-3": 0.013125749682449539, "-4": 0.002989150166962647, "-5": 0.0005601335213177791, "-6": 8.895576544258867e-05, "-7": 1.224118947983328e-05, "-8": 1.484870322222447e-06, "-9": 1.609455551301477e-07, "0": 0.20039896551363803, "1": 0.2431726777741784, "10": 1.7898932791435998e-05, "11": 3.2294791797397576e-06, "12": 5.353398497252805e-07, "13": 8.206133334572166e-08, "14": 1.1697183604189505e-08, "15": 1.557636978415744e-09, "16": 1.9355768842303936e-10, "17": 2.0513584174930627e-11, "2": 0.1859706427625383, "3": 0.10831691013152007, "4": 0.04984756252741895, "5": 0.0188760798427084, "6": 0.006057848266205089, "7": 0.0016845812357591534, "8": 0.000412934257577807, "9": 9.0447261549986e-05} |
| Unadjusted home-win probability | 61.4% |
| Unadjusted draw probability | 20.0% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 79.8% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 54.2% |
| P home draw | 87.1% |
| P draw away | 29.4% |
| P home away | 83.5% |
| Raw p home draw | 81.5% |
| Raw p draw away | 38.6% |
| Raw p home away | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:46Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 8.93, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:46Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.09, "price": 8.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.29, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.73, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.04, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.04, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.22 |
| Reference draw odds | 6.00 |
| Reference away odds | 10.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | -9.1% |
| Draw probability edge | +3.5% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -12.3% |
| Under 2.5 probability edge | +12.3% |
| Raw edge prob home | -0.1829 |
| Raw ev home | -0.2319 |
| Raw edge prob draw | 0.0704 |
| Raw ev draw | 0.3667 |
| Raw edge prob away | 0.1125 |
| Raw ev away | 0.9144 |
| Market p over 1 5 | 91.2% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market reference over 1 5 last update utc | 2026-10-21T17:28:55Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 49.1% |
| Market under 3 5 odds | 1.98 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market reference under 3 5 odds | 1.98 |
| Market reference under 3 5 opposite odds | 1.91 |
| Market reference under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.3% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T17:28:46Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.15 |
| Market reference btts yes last update utc | 2026-10-21T17:28:55Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **64.0%**. Expected goals are 4.60 for Real Betis and 2.70 for Feyenoord (7.30 combined). The most likely exact score is 3-3 at 5.0%. Goal-market probabilities: at least one goal: 100.0%; Over 2.5 goals: 97.4%; Under 3.5 goals: 6.8%; Double Chance 1X: 80.5%; Double Chance X2: 36.0%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 15.6%; BTTS Yes (both teams score): 92.8%; BTTS No (at least one team does not score): 7.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 64.0% | 1.56 |
| Draw | 16.5% | 6.05 |
| Feyenoord win | 19.5% | 5.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 4.60 |
| Feyenoord expected goals | 2.70 |
| Expected total goals | 7.30 |
| Over 0.5 | 100.0% |
| Under 0.5 | 0.0% |
| Over 1.5 | 99.4% |
| Under 1.5 | 0.6% |
| Over 2.5 | 97.4% |
| Under 2.5 | 2.6% |
| Over 3.5 | 93.2% |
| Under 3.5 | 6.8% |
| Over 4.5 | 84.4% |
| Under 4.5 | 15.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-3 | 5.02% |
| 2 | 4-2 | 4.21% |
| 3 | 4-4 | 3.90% |
| 4 | 5-2 | 3.88% |
| 5 | 4-3 | 3.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 64.0% | 58.2% | 1.68 | +7.6% |
| Draw | 16.5% | 21.2% | 4.48 | -26.0% |
| Feyenoord win | 19.5% | 20.5% | 4.57 | -11.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | f5905225efa837b0dc89b7dcdbb6c625 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.6007 |
| Dc lambda away | 2.6980 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:28:56.715717+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 24 |
| Score grid omitted mass | 0 |
| P btts yes | 92.8% |
| P btts no | 7.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 2787.45 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 167.35 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 38.02 |
| Fair Over 3.5 odds | 1.07 |
| Fair Under 3.5 odds | 14.62 |
| Fair Over 4.5 odds | 1.18 |
| Fair Under 4.5 odds | 6.41 |
| Goal margin distribution | {"-1": 0.08987235864407947, "-10": 1.189127836795758e-05, "-11": 2.6819240763390336e-06, "-12": 5.610466129809041e-07, "-13": 1.0937585755009181e-07, "-14": 1.9954325339604687e-08, "-15": 3.4196638990821833e-09, "-16": 5.523786849314902e-10, "-17": 8.435928951302971e-11, "-18": 1.2214705054394023e-11, "-19": 1.6810619629586073e-12, "-2": 0.05451338308543755, "-20": 2.2037911816300566e-13, "-21": 2.7538984213428932e-14, "-22": 3.2542598327535267e-15, "-23": 3.448979803973665e-16, "-24": 2.55550120743687e-17, "-3": 0.028744697764605125, "-4": 0.013224339311443453, "-5": 0.0053589575396566155, "-6": 0.0019310313833500502, "-7": 0.0006242811134939794, "-8": 0.00018255980807877555, "-9": 4.864816263423104e-05, "0": 0.16524572963567652, "1": 0.1323838605095663, "10": 0.0021400946154105562, "11": 0.0008230769508899123, "12": 0.0002936178392624196, "13": 9.761004141631311e-05, "14": 3.0366840420707334e-05, "15": 8.874328778919849e-06, "16": 2.444435235142504e-06, "17": 6.365962402043509e-07, "18": 1.5718231218279122e-07, "19": 3.6888750285423964e-08, "2": 0.13721175008268768, "20": 8.246510082835849e-09, "21": 1.7572647727344562e-09, "22": 3.541041724403382e-10, "23": 6.399690955258515e-11, "24": 8.086004409753708e-12, "3": 0.1233773527872094, "4": 0.09679239085278164, "5": 0.06688628608546054, "6": 0.041099414082293284, "7": 0.022657710702404615, "8": 0.01129875350227598, "9": 0.00513430114839682} |
| Raw goal margin distribution | {"-1": 0.08483384600334548, "-10": 1.1224617814308167e-05, "-11": 2.531567408682874e-06, "-12": 5.295926654691848e-07, "-13": 1.0324392055442736e-07, "-14": 1.8835626309360203e-08, "-15": 3.227947335251661e-09, "-16": 5.214106873347934e-10, "-17": 7.96298559809908e-11, "-18": 1.1529912235468088e-11, "-19": 1.5868166123523343e-12, "-2": 0.05145720013987908, "-20": 2.0802400709915179e-13, "-21": 2.5995066571055183e-14, "-22": 3.071816314513432e-15, "-23": 3.255619703024514e-16, "-24": 2.412232183107888e-17, "-3": 0.027133184222219855, "-4": 0.012482943382913959, "-5": 0.0050585183867058285, "-6": 0.0018227720010276726, "-7": 0.0005892820511663979, "-8": 0.00017232496040622618, "-9": 4.592080145133632e-05, "0": 0.11819599161602573, "1": 0.14436734010487956, "10": 0.0023338174760152972, "11": 0.0008975824518505012, "12": 0.0003201963313238965, "13": 0.0001064457705989165, "14": 3.311566804331156e-05, "15": 9.6776392235235e-06, "16": 2.665707221392506e-06, "17": 6.942213768756807e-07, "18": 1.714105649587444e-07, "19": 4.022794574807662e-08, "2": 0.1496322536170615, "20": 8.992989940197823e-09, "21": 1.916333608365704e-09, "22": 3.8615792966361725e-10, "23": 6.978995454186536e-11, "24": 8.817955181387949e-12, "3": 0.13454555700756035, "4": 0.10555410573480142, "5": 0.07294087945829456, "6": 0.044819761775272846, "7": 0.02470870251389629, "8": 0.012321524567614523, "9": 0.005599061677446059} |
| Unadjusted home-win probability | 69.8% |
| Unadjusted draw probability | 11.8% |
| Unadjusted away-win probability | 18.4% |
| Raw p over 1 5 | 99.4% |
| Raw p under 3 5 | 6.7% |
| Raw p btts yes | 92.3% |
| P home draw | 80.5% |
| P draw away | 36.0% |
| P home away | 83.5% |
| Raw p home draw | 81.6% |
| Raw p draw away | 30.2% |
| Raw p home away | 88.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.15, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.15, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.65 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.33 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +5.8% |
| Draw probability edge | -4.7% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +25.4% |
| Under 2.5 probability edge | -25.4% |
| Raw edge prob home | 0.1159 |
| Raw ev home | 0.1730 |
| Raw edge prob draw | -0.0941 |
| Raw ev draw | -0.4705 |
| Raw edge prob away | -0.0218 |
| Raw ev away | -0.1609 |
| Market p over 1 5 | 89.5% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market reference over 1 5 last update utc | 2026-10-21T17:28:55Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 50.5% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market reference under 3 5 odds | 1.93 |
| Market reference under 3 5 opposite odds | 1.97 |
| Market reference under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.9% |
| Market btts yes odds | 1.42 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T17:28:47Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.88 |
| Market reference btts yes last update utc | 2026-10-21T17:28:55Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **80.0%**. Expected goals are 2.82 for Real Madrid and 0.76 for RB Leipzig (3.58 combined). The most likely exact score is 2-0 at 11.0%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.4%; Under 3.5 goals: 51.9%; Double Chance 1X: 92.2%; Double Chance X2: 20.0%; Double Chance 12 (either team wins): 87.8%; Under 4.5 goals: 71.0%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 80.0% | 1.25 |
| Draw | 12.2% | 8.18 |
| RB Leipzig win | 7.8% | 12.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.82 |
| RB Leipzig expected goals | 0.76 |
| Expected total goals | 3.58 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.9% |
| Under 1.5 | 13.1% |
| Over 2.5 | 69.4% |
| Under 2.5 | 30.6% |
| Over 3.5 | 48.1% |
| Under 3.5 | 51.9% |
| Over 4.5 | 29.0% |
| Under 4.5 | 71.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.04% |
| 2 | 3-0 | 10.36% |
| 3 | 2-1 | 8.44% |
| 4 | 1-0 | 8.14% |
| 5 | 3-1 | 7.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 80.0% | 79.9% | 1.22 | -2.4% |
| Draw | 12.2% | 12.1% | 7.28 | -11.0% |
| RB Leipzig win | 7.8% | 7.9% | 11.27 | -11.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 30f27b8e9719e9ae71c25b4c8aa265f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8158 |
| Dc lambda away | 0.7647 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:28:56.715717+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.48 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.65 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.27 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.92 |
| Fair Over 4.5 odds | 3.45 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.05790423731633425, "-10": 6.464086352631416e-10, "-11": 4.422694775693445e-11, "-12": 2.780523863635905e-12, "-13": 1.616710892767473e-13, "-14": 8.742161883887849e-15, "-15": 4.4175818475012627e-16, "-16": 2.0949175463120258e-17, "-17": 9.356305574411965e-19, "-18": 3.928867063891889e-20, "-19": 1.4203486644195425e-21, "-2": 0.016030978443437163, "-3": 0.0035136571206706604, "-4": 0.0006102497753658477, "-5": 8.735970357029929e-05, "-6": 1.0610001935406849e-05, "-7": 1.1173620336680093e-06, "-8": 1.0377705011462909e-07, "-9": 8.615656008261321e-09, "0": 0.12223245817048449, "1": 0.2022301992329268, "10": 0.0002920419190944448, "11": 7.35734507394506e-05, "12": 1.703165680908257e-05, "13": 3.646353322106339e-06, "14": 7.26007891683931e-07, "15": 1.3508378320400016e-07, "16": 2.3587486137955423e-08, "17": 3.878959402137308e-09, "18": 5.997555624666608e-10, "19": 7.983586417717454e-11, "2": 0.2143528036767089, "3": 0.17299144651727966, "4": 0.1106290015801289, "5": 0.05831343567406488, "6": 0.02607768615693452, "7": 0.010112152604834692, "8": 0.00345817637327428, "9": 0.0010571345860456314} |
| Raw goal margin distribution | {"-1": 0.05712596093892169, "-10": 6.377204184020436e-10, "-11": 4.363250440909725e-11, "-12": 2.743151537530001e-12, "-13": 1.5949810858437997e-13, "-14": 8.624660671591816e-15, "-15": 4.358206234307116e-16, "-16": 2.0667602833121763e-17, "-17": 9.230549810310672e-19, "-18": 3.876060143923033e-20, "-19": 1.4012581131155299e-21, "-2": 0.01581551007000575, "-3": 0.003466430933744026, "-4": 0.0006020475607007289, "-5": 8.618552363498482e-05, "-6": 1.0467395551947941e-05, "-7": 1.102343849919716e-06, "-8": 1.023822087288331e-07, "-9": 8.499855129812468e-09, "0": 0.12301362786389627, "1": 0.2022983175463361, "10": 0.0002921402891848121, "11": 7.359823289065791e-05, "12": 1.7037393675983766e-05, "13": 3.6475815434073044e-06, "14": 7.262524369263871e-07, "15": 1.3512928421975205e-07, "16": 2.3595431241008173e-08, "17": 3.88026597342715e-09, "18": 5.999575814407212e-10, "19": 7.986275573164044e-11, "2": 0.21442500531383527, "3": 0.17304971618034526, "4": 0.11066626535690591, "5": 0.058333077710231024, "6": 0.026086470047794366, "7": 0.010115558736970207, "8": 0.003459341209895679, "9": 0.0010574906665188806} |
| Unadjusted home-win probability | 80.0% |
| Unadjusted draw probability | 12.3% |
| Unadjusted away-win probability | 7.7% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 51.9% |
| Raw p btts yes | 50.0% |
| P home draw | 92.2% |
| P draw away | 20.0% |
| P home away | 87.8% |
| Raw p home draw | 92.3% |
| Raw p draw away | 20.0% |
| Raw p home away | 87.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 6.35, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:46Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 9.84, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:46Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.08, "price": 9.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.78, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.22 |
| Reference draw odds | 6.50 |
| Reference away odds | 9.50 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 5.00 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +0.0% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -14.4% |
| Under 2.5 probability edge | +14.4% |
| Raw edge prob home | 0.0005 |
| Raw ev home | -0.0241 |
| Raw edge prob draw | 0.0016 |
| Raw ev draw | -0.1045 |
| Raw edge prob away | -0.0021 |
| Raw ev away | -0.1310 |
| Market p over 1 5 | 95.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T17:28:36Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 13.00 |
| Market reference over 1 5 last update utc | 2026-10-21T17:28:55Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 33.1% |
| Market under 3 5 odds | 2.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market reference under 3 5 odds | 2.78 |
| Market reference under 3 5 opposite odds | 1.45 |
| Market reference under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 68.9% |
| Market btts yes odds | 1.44 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T17:28:46Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.88 |
| Market reference btts yes last update utc | 2026-10-21T17:28:55Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **84.8%**. Expected goals are 5.51 for Sporting Lisbon and 0.76 for LASK (6.27 combined). The most likely exact score is 5-0 at 7.0%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 91.4%; Under 3.5 goals: 16.9%; Double Chance 1X: 94.2%; Double Chance X2: 15.2%; Double Chance 12 (either team wins): 90.6%; Under 4.5 goals: 30.8%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 84.8% | 1.18 |
| Draw | 9.4% | 10.59 |
| LASK win | 5.8% | 17.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 5.51 |
| LASK expected goals | 0.76 |
| Expected total goals | 6.27 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 97.4% |
| Under 1.5 | 2.6% |
| Over 2.5 | 91.4% |
| Under 2.5 | 8.6% |
| Over 3.5 | 83.1% |
| Under 3.5 | 16.9% |
| Over 4.5 | 69.2% |
| Under 4.5 | 30.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-0 | 7.00% |
| 2 | 6-0 | 6.43% |
| 3 | 4-0 | 6.35% |
| 4 | 5-1 | 5.34% |
| 5 | 7-0 | 5.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 84.8% | 72.8% | 1.34 | +13.6% |
| Draw | 9.4% | 16.6% | 5.89 | -44.4% |
| LASK win | 5.8% | 10.6% | 8.45 | -51.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 8fdcaee14b3e8966e09d468a0b17ce18 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 5.5104 |
| Dc lambda away | 0.7627 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:28:56.715717+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 26 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 159.64 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 38.21 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 11.62 |
| Fair Over 3.5 odds | 1.20 |
| Fair Under 3.5 odds | 5.91 |
| Fair Over 4.5 odds | 1.44 |
| Fair Under 4.5 odds | 3.25 |
| Goal margin distribution | {"-1": 0.04499704477970163, "-10": 2.8741086169722086e-10, "-11": 1.9328656398758563e-11, "-12": 1.1969788373419347e-12, "-13": 6.86715195025454e-14, "-14": 3.6689895319447975e-15, "-15": 1.8339490156754574e-16, "-16": 8.611043525190465e-18, "-17": 3.8116450551132653e-19, "-18": 1.595702040374139e-20, "-19": 6.336174576746707e-22, "-2": 0.010577983683544559, "-20": 2.3926026957081474e-23, "-21": 8.612110733469475e-25, "-22": 2.961285381355413e-26, "-23": 9.746059290115654e-28, "-24": 3.074025114381393e-29, "-25": 9.219204396906962e-31, "-26": 2.3281187127921693e-32, "-3": 0.00207630309189102, "-4": 0.00033373721741606136, "-5": 4.512706033142324e-05, "-6": 5.246328016633687e-06, "-7": 5.336969124445249e-07, "-8": 4.8190196401043975e-08, "-9": 3.90793141350861e-09, "0": 0.09441278154567821, "1": 0.047833657926667134, "10": 0.01712599979156072, "11": 0.008321032284733553, "12": 0.003722929369680137, "13": 0.0015431131267196465, "14": 0.0005956489283438439, "15": 0.0002151066980127743, "16": 7.297015079584329e-05, "17": 2.3335907507489467e-05, "18": 7.058084068561925e-06, "19": 2.024813113257123e-06, "2": 0.08491284292081512, "20": 5.523968348886934e-07, "21": 1.4365243193744034e-07, "22": 3.568670277236919e-08, "23": 8.48551086195149e-09, "24": 1.933655663897616e-09, "25": 4.189748513944459e-10, "26": 7.644030602753614e-11, "3": 0.12041595185879457, "4": 0.13983654868560152, "5": 0.13660792137833608, "6": 0.11474058603765577, "7": 0.08432941684665851, "8": 0.055013070671424684, "9": 0.0322312320593308} |
| Raw goal margin distribution | {"-1": 0.007898219506147768, "-10": 5.0448514680229637e-11, "-11": 3.3927110489969173e-12, "-12": 2.1010272225265981e-13, "-13": 1.2053741251391746e-14, "-14": 6.440086194756214e-16, "-15": 3.2190851554372785e-17, "-16": 1.5114750817953112e-18, "-17": 6.690485891284104e-20, "-18": 2.8008961572890185e-21, "-19": 1.1121729856133515e-22, "-2": 0.0018567272022889155, "-20": 4.1996760841121914e-24, "-21": 1.5116624062137845e-25, "-22": 5.1978706772410945e-27, "-23": 1.7107015798510527e-28, "-24": 5.3957599303827516e-30, "-25": 1.618224049052687e-31, "-26": 4.086488950558294e-33, "-3": 0.00036444832458077964, "-4": 5.858006483377091e-05, "-5": 7.921040813007756e-06, "-6": 9.208749258866436e-07, "-7": 9.367849344056712e-08, "-8": 8.458705479065493e-09, "-9": 6.859494944606893e-10, "0": 0.022457315616462636, "1": 0.0545951268403525, "10": 0.019546824796914598, "11": 0.009497241748146389, "12": 0.00424917955191646, "13": 0.001761238018038024, "14": 0.000679846162823409, "15": 0.00024551284537387814, "16": 8.328475828393102e-05, "17": 2.6634526513931005e-05, "18": 8.055771013033588e-06, "19": 2.311028124082753e-06, "2": 0.09691559522259258, "20": 6.304802219640485e-07, "21": 1.6395824786331804e-07, "22": 4.073115351868735e-08, "23": 9.684969995889861e-09, "24": 2.206985223624355e-09, "25": 4.78198535221063e-10, "26": 8.724543311503909e-11, "3": 0.13743720322228614, "4": 0.15960297504555654, "5": 0.15591796902676922, "6": 0.13095960292365344, "7": 0.09624969966073986, "8": 0.06278937679799089, "9": 0.03678723891862326} |
| Unadjusted home-win probability | 96.7% |
| Unadjusted draw probability | 2.2% |
| Unadjusted away-win probability | 1.0% |
| Raw p over 1 5 | 98.6% |
| Raw p under 3 5 | 12.8% |
| Raw p btts yes | 53.1% |
| P home draw | 94.2% |
| P draw away | 15.2% |
| P home away | 90.6% |
| Raw p home draw | 99.0% |
| Raw p draw away | 3.3% |
| Raw p home away | 97.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:27Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 7.07, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:27Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 7.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:53Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:54Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.33 |
| Reference draw odds | 5.00 |
| Reference away odds | 7.50 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +12.0% |
| Draw probability edge | -7.2% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | +16.8% |
| Under 2.5 probability edge | -16.8% |
| Raw edge prob home | 0.2396 |
| Raw ev home | 0.2963 |
| Raw edge prob draw | -0.1439 |
| Raw ev draw | -0.8677 |
| Raw edge prob away | -0.0957 |
| Raw ev away | -0.9139 |
| Market p over 1 5 | 91.3% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 8.00 |
| Market reference over 1 5 last update utc | 2026-10-21T17:28:55Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 46.4% |
| Market under 3 5 odds | 2.09 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market reference under 3 5 odds | 2.09 |
| Market reference under 3 5 opposite odds | 1.82 |
| Market reference under 3 5 last update utc | 2026-10-21T17:28:54Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.7% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T17:28:27Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.45 |
| Market reference btts yes last update utc | 2026-10-21T17:28:55Z |
| Market btts yes bookmakers | 2 |

</details>


---
