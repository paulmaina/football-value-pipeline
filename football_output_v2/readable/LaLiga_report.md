# La Liga — football model report

Fixtures in this report: **16**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,989 |
| Training data through | 2026-10-21 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | c6aac313a3165c68f1473a43e05aefb673aea2a96b6b48c13e7e354a2eae1c0a |
| Training as of utc | 2026-10-22T15:05:32.065784+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 89, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 89, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 33, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T15:05:32.065784+00:00', 'observations': 180, 'observations_sha256': '93cd4c73c31c572efca3ee566366023f58ff20b78b20d684d35028e8813a4068', 'eligible_training_matches': 84, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 105, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 10, 'retrospective_eligible_training_matches': 84, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'd2cbd702cc71c67522fca78aa83d4a5405d45ac3496787ac326cf6035d2d5106', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2505.488 |
| Base scoring parameter | 0.095 |
| Home-advantage parameter | 0.284 |
| Dixon-Coles low-score adjustment | -0.022 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-21', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 4.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261022T150532065784Z_7471a2e2ce5f1db6668722d357a8d49e7a3ddcd497c1ee1e29ed8c677ce338ec.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **59.7%**. Expected goals are 1.75 for Alavés and 0.59 for Málaga (2.34 combined). The most likely exact score is 1-0 at 15.2%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 40.3%; Under 3.5 goals: 79.9%; Double Chance 1X: 84.3%; Double Chance X2: 40.3%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 37.8%; BTTS No (at least one team does not score): 62.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 59.7% | 1.67 |
| Draw | 24.6% | 4.07 |
| Málaga win | 15.7% | 6.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.75 |
| Málaga expected goals | 0.59 |
| Expected total goals | 2.34 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 20.1% |
| Under 3.5 | 79.9% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.23% |
| 2 | 2-0 | 13.48% |
| 3 | 1-1 | 10.91% |
| 4 | 0-0 | 10.57% |
| 5 | 2-1 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 59.7% | 54.2% | 1.74 | +3.9% |
| Draw | 24.6% | 26.2% | 3.76 | -7.6% |
| Málaga win | 15.7% | 19.6% | 5.14 | -19.2% |
| Over 2.5 | 40.3% | 46.1% | 2.12 | -14.6% |
| Under 2.5 | 59.7% | 53.9% | 1.84 | +9.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | 903eb4941471ffe20d525b02dd3b77aa |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7471 |
| Dc lambda away | 0.5915 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 37.8% |
| P btts no | 62.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.46 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 4.97 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.84 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.11935583656473535, "-10": 2.0322029913508642e-10, "-11": 1.084330590749165e-11, "-12": 5.309835461754974e-13, "-13": 2.4023835720229324e-14, "-14": 1.0100090444481709e-15, "-15": 3.9584938724000857e-17, "-16": 1.3746148447108307e-18, "-2": 0.031198357558333858, "-3": 0.005684980468256258, "-4": 0.0008006388361707171, "-5": 9.163303672443588e-05, "-6": 8.820292334617309e-06, "-7": 7.319912596240128e-07, "-8": 5.3363960156327065e-08, "-9": 3.467726535041582e-09, "0": 0.24574929152218916, "1": 0.24698067659023856, "10": 7.079703255616081e-06, "11": 1.1157492347158545e-06, "12": 1.613774580129285e-07, "13": 2.1565576639027424e-08, "14": 2.6779404034240323e-09, "15": 3.100006047216434e-10, "16": 3.179585536408368e-11, "2": 0.18763953436489483, "3": 0.10099003238813366, "4": 0.0420090737576973, "5": 0.01420088636216859, "6": 0.0040374138759356176, "7": 0.0009896533666719626, "8": 0.00021309937766064824, "9": 4.090118502664161e-05} |
| Raw goal margin distribution | {"-1": 0.08987732026609206, "-10": 1.5302892959096146e-10, "-11": 8.16522514391038e-12, "-12": 3.9984117751758716e-13, "-13": 1.809042640219729e-14, "-14": 7.60556910933157e-16, "-15": 2.980824664976486e-17, "-16": 1.0351123346497712e-18, "-2": 0.023492984128393252, "-3": 0.004280903430933768, "-4": 0.0006028969773669844, "-5": 6.900150026739466e-05, "-6": 6.641855662994695e-06, "-7": 5.512039860532933e-07, "-8": 4.0184124008345846e-08, "-9": 2.611267093051765e-09, "0": 0.22946819437170557, "1": 0.2697681371539125, "10": 7.732906012071082e-06, "11": 1.218692882113903e-06, "12": 1.7626681094168673e-07, "13": 2.3555306094704798e-08, "14": 2.925018280840884e-09, "15": 3.3860254497193067e-10, "16": 3.4729472723142984e-11, "2": 0.2049519352723559, "3": 0.11030779121906767, "4": 0.045885004963271754, "5": 0.015511118977993893, "6": 0.004409922408778261, "7": 0.0010809628868177822, "8": 0.0002327608092010678, "9": 4.4674897827454966e-05} |
| Unadjusted home-win probability | 65.2% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 11.8% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 37.1% |
| P home draw | 84.3% |
| P draw away | 40.3% |
| P home away | 75.4% |
| Raw p home draw | 88.2% |
| Raw p draw away | 34.8% |
| Raw p home away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.48, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 3.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.46, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:31Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.86, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:31Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.28, "price": 3.86, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.81 |
| Reference draw odds | 3.66 |
| Reference away odds | 4.85 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:00Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:00Z |
| Home probability edge | +5.5% |
| Draw probability edge | -1.6% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.1102 |
| Raw ev home | 0.1348 |
| Raw edge prob draw | -0.0326 |
| Raw ev draw | -0.1372 |
| Raw edge prob away | -0.0776 |
| Raw ev away | -0.3918 |
| Market p home draw | 79.7% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:05:31Z |
| Market reference home draw last update utc | 2026-10-22T15:05:36Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.6% |
| Market draw away odds | 2.21 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:05:31Z |
| Market reference draw away last update utc | 2026-10-22T15:05:36Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.7% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:05:31Z |
| Market reference home away last update utc | 2026-10-22T15:05:36Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 2.07 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 74.1% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:05:30Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.25 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:31Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.2% |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market reference under 3 5 last update utc | 2026-10-22T15:05:15Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 48.8% |
| Market btts yes odds | 2.01 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:05:31Z |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 1.83 |
| Market reference btts yes last update utc | 2026-10-22T15:05:31Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **71.6%**. Expected goals are 2.24 for Atlético Madrid and 0.87 for Deportivo La Coruña (3.11 combined). The most likely exact score is 2-0 at 11.7%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 61.1%; Under 3.5 goals: 61.7%; Double Chance 1X: 88.6%; Double Chance X2: 28.4%; Double Chance 12 (either team wins): 82.9%; Under 4.5 goals: 79.1%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 71.6% | 1.40 |
| Draw | 17.1% | 5.86 |
| Deportivo La Coruña win | 11.4% | 8.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.24 |
| Deportivo La Coruña expected goals | 0.87 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 61.1% |
| Under 2.5 | 38.9% |
| Over 3.5 | 38.3% |
| Under 3.5 | 61.7% |
| Over 4.5 | 20.9% |
| Under 4.5 | 79.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.72% |
| 2 | 1-0 | 10.27% |
| 3 | 2-1 | 10.25% |
| 4 | 3-0 | 8.74% |
| 5 | 1-1 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 71.6% | 75.1% | 1.29 | -7.7% |
| Draw | 17.1% | 15.2% | 5.81 | -0.9% |
| Deportivo La Coruña win | 11.4% | 9.6% | 10.05 | +14.2% |
| Over 2.5 | 61.1% | 61.2% | 1.65 | +0.8% |
| Under 2.5 | 38.9% | 38.8% | 2.44 | -5.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 70df1835c3b5ddff1c99e0189532136b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2371 |
| Dc lambda away | 0.8749 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.82 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.65 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.57 |
| Fair Over 3.5 odds | 2.61 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.79 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.07795275787528075, "-10": 3.339171335622635e-09, "-11": 2.617577470384379e-10, "-12": 1.885072676996792e-11, "-13": 1.2553057491127157e-12, "-14": 7.773017145638823e-14, "-15": 4.496416212892011e-15, "-16": 2.427753681214309e-16, "-17": 1.1204596667025788e-17, "-2": 0.027131535807692134, "-3": 0.006884438634504496, "-4": 0.0013788230856270822, "-5": 0.00022709441114200505, "-6": 3.168682897596835e-05, "-7": 3.8300917886527925e-06, "-8": 4.080180506839976e-07, "-9": 3.883476352793814e-08, "0": 0.1705451452244116, "1": 0.24469125186663507, "10": 4.833817778010915e-05, "11": 9.688866462674124e-06, "12": 1.7841172000334291e-06, "13": 3.0378522990120637e-07, "14": 4.8098177157035215e-08, "15": 7.114221001246833e-09, "16": 9.821714906000965e-10, "17": 1.1590463015244462e-10, "2": 0.2149567598984016, "3": 0.139465605753694, "4": 0.07142150307994319, "5": 0.030077985183331327, "6": 0.010731067579876316, "7": 0.0033166159678139173, "8": 0.0009034148752579064, "9": 0.0002198621045451406} |
| Raw goal margin distribution | {"-1": 0.0898012436434104, "-10": 3.846711095931964e-09, "-11": 3.0154380496655747e-10, "-12": 2.1715956608406923e-11, "-13": 1.4461068536330952e-12, "-14": 8.954482504091961e-14, "-15": 5.17985224463929e-15, "-16": 2.7967618564788006e-16, "-17": 1.2907647434765024e-17, "-2": 0.031255413200192685, "-3": 0.007930843860000113, "-4": 0.0015883982969744361, "-5": 0.0002616117902800569, "-6": 3.6503091445599e-05, "-7": 4.412249357998692e-06, "-8": 4.7003504916407767e-07, "-9": 4.473748147546267e-08, "0": 0.188608125124568, "1": 0.23261423640170648, "10": 4.595239195350745e-05, "11": 9.210661421771726e-06, "12": 1.696060063328793e-06, "13": 2.887915638361302e-07, "14": 4.5724236834571255e-08, "15": 6.76309051988493e-09, "16": 9.336952978849833e-10, "17": 1.101840251037164e-10, "2": 0.20434732415527632, "3": 0.13258212191573884, "4": 0.06789641343883479, "5": 0.028593451962621946, "6": 0.010201423515657804, "7": 0.0031529206087483265, "8": 0.0008588258050050684, "9": 0.00020901055992927247} |
| Unadjusted home-win probability | 68.1% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 13.1% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 52.3% |
| P home draw | 88.6% |
| P draw away | 28.4% |
| P home away | 82.9% |
| Raw p home draw | 86.9% |
| Raw p draw away | 31.9% |
| Raw p home away | 81.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.86, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.31 |
| Reference draw odds | 5.90 |
| Reference away odds | 9.10 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:32Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:32Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:00Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:00Z |
| Home probability edge | -3.5% |
| Draw probability edge | +1.8% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0707 |
| Raw ev home | -0.1221 |
| Raw edge prob draw | 0.0361 |
| Raw ev draw | 0.0958 |
| Raw edge prob away | 0.0345 |
| Raw ev away | 0.3153 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **51.1%**. Expected goals are 1.40 for Rayo Vallecano and 0.97 for Elche CF (2.37 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 43.0%; Under 3.5 goals: 78.2%; Double Chance 1X: 77.1%; Double Chance X2: 48.9%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 90.5%; BTTS Yes (both teams score): 46.6%; BTTS No (at least one team does not score): 53.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 51.1% | 1.96 |
| Draw | 26.1% | 3.84 |
| Elche CF win | 22.9% | 4.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.40 |
| Elche CF expected goals | 0.97 |
| Expected total goals | 2.37 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 69.2% |
| Under 1.5 | 30.8% |
| Over 2.5 | 43.0% |
| Under 2.5 | 57.0% |
| Over 3.5 | 21.8% |
| Under 3.5 | 78.2% |
| Over 4.5 | 9.5% |
| Under 4.5 | 90.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.99% |
| 2 | 1-1 | 12.24% |
| 3 | 2-0 | 10.04% |
| 4 | 2-1 | 9.73% |
| 5 | 0-0 | 9.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 51.1% | 55.4% | 1.81 | -7.6% |
| Draw | 26.1% | 24.5% | 3.83 | -0.2% |
| Elche CF win | 22.9% | 20.1% | 4.49 | +2.7% |
| Over 2.5 | 43.0% | 52.7% | 1.90 | -18.3% |
| Under 2.5 | 57.0% | 47.3% | 1.99 | +13.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T12:00:00+00:00 |
| Fixture id | 734ad601156f5f4e6bc42317e5141516 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Vallecano |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4044 |
| Dc lambda away | 0.9690 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.6% |
| P btts no | 53.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.03 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.24 |
| Fair Over 2.5 odds | 2.33 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.58 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.56 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.14655944958838868, "-10": 1.8883996685945165e-08, "-11": 1.6467288639151305e-09, "-12": 1.3181826770415014e-10, "-13": 9.714623822659645e-12, "-14": 6.128430262051561e-13, "-2": 0.059933946899070716, "-3": 0.01749654880321067, "-4": 0.003979325107356248, "-5": 0.0007387373999870541, "-6": 0.00011565032678740606, "-7": 1.5636823597245264e-05, "-8": 1.8594485199045489e-06, "-9": 1.9726098432412727e-07, "0": 0.2605060376122469, "1": 0.26194266063628846, "10": 9.467569977156157e-07, "11": 1.1964768525379866e-07, "12": 1.3880189584905823e-08, "13": 1.4824613553893634e-09, "14": 1.3553274557749594e-10, "2": 0.15442468635035425, "3": 0.0653331858944216, "4": 0.021534186054752765, "5": 0.005793576159986218, "6": 0.0013144409874413436, "7": 0.000257561152892637, "8": 4.438677355554299e-05, "9": 6.82414441988127e-06} |
| Raw goal margin distribution | {"-1": 0.164532867038333, "-10": 2.1199848420603606e-08, "-11": 1.8486765744253918e-09, "-12": 1.4798389032097324e-10, "-13": 1.0905983300497563e-11, "-14": 6.879994461576576e-13, "-2": 0.06728398710504278, "-3": 0.019642249926247253, "-4": 0.0044673323394004965, "-5": 0.000829332961809536, "-6": 0.0001298331830099857, "-7": 1.755445605897836e-05, "-8": 2.0874832496254047e-06, "-9": 2.214522188559288e-07, "0": 0.2757945767575719, "1": 0.23970462587248376, "10": 8.663805711460276e-07, "11": 1.0949000655564572e-07, "12": 1.2701809027238947e-08, "13": 1.3566054635805799e-09, "14": 1.2402647966241e-10, "2": 0.14131455936642967, "3": 0.059786622170814915, "4": 0.01970600741087483, "5": 0.005301721386351554, "6": 0.001202849449420443, "7": 0.00023569509313009607, "8": 4.0618488500395526e-05, "9": 6.244797930562152e-06} |
| Unadjusted home-win probability | 46.7% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 68.9% |
| Raw p under 3 5 | 78.4% |
| Raw p btts yes | 47.1% |
| P home draw | 77.1% |
| P draw away | 48.9% |
| P home away | 73.9% |
| Raw p home draw | 74.3% |
| Raw p draw away | 53.3% |
| Raw p home away | 72.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.13, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.44, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.91, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:32Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:32Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.76 |
| Reference draw odds | 3.84 |
| Reference away odds | 4.65 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T15:05:30Z |
| Market best under 2 5 last update utc | 2026-10-22T15:05:30Z |
| Home probability edge | -4.3% |
| Draw probability edge | +1.5% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.0867 |
| Raw ev home | -0.1542 |
| Raw edge prob draw | 0.0306 |
| Raw ev draw | 0.0563 |
| Raw edge prob away | 0.0561 |
| Raw ev away | 0.1535 |
| Market p home draw | 79.4% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:05:32Z |
| Market reference home draw last update utc | 2026-10-22T15:05:36Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.5% |
| Market draw away odds | 2.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:05:32Z |
| Market reference draw away last update utc | 2026-10-22T15:05:36Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.1% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:05:32Z |
| Market reference home away last update utc | 2026-10-22T15:05:36Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 2.11 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 77.7% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:05:30Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:31Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.4% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:05:30Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.23 |
| Market reference under 3 5 last update utc | 2026-10-22T15:05:30Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.3% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:05:32Z |
| Market reference btts yes odds | 1.81 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-10-22T15:05:32Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **38.2%**. Expected goals are 1.84 for Real Racing Club de Santander and 2.02 for Espanyol (3.86 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 73.4%; Under 3.5 goals: 46.3%; Double Chance 1X: 61.8%; Double Chance X2: 61.9%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 66.2%; BTTS Yes (both teams score): 73.6%; BTTS No (at least one team does not score): 26.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 38.1% | 2.62 |
| Draw | 23.6% | 4.23 |
| Espanyol win | 38.2% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.84 |
| Espanyol expected goals | 2.02 |
| Expected total goals | 3.86 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 89.9% |
| Under 1.5 | 10.1% |
| Over 2.5 | 73.4% |
| Under 2.5 | 26.6% |
| Over 3.5 | 53.7% |
| Under 3.5 | 46.3% |
| Over 4.5 | 33.8% |
| Under 4.5 | 66.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.86% |
| 2 | 2-2 | 8.04% |
| 3 | 2-1 | 7.67% |
| 4 | 1-2 | 7.07% |
| 5 | 1-3 | 4.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 38.1% | 40.4% | 2.42 | -7.8% |
| Draw | 23.6% | 25.9% | 3.71 | -12.3% |
| Espanyol win | 38.2% | 33.7% | 2.85 | +9.0% |
| Over 2.5 | 73.4% | 57.3% | 1.73 | +26.9% |
| Under 2.5 | 26.6% | 42.7% | 2.28 | -39.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:15:00+00:00 |
| Fixture id | 5960b1b6c20acfd78e78764fed47d505 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8405 |
| Dc lambda away | 2.0171 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 73.6% |
| P btts no | 26.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.58 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.87 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.75 |
| Fair Over 3.5 odds | 1.86 |
| Fair Under 3.5 odds | 2.16 |
| Fair Over 4.5 odds | 2.96 |
| Fair Under 4.5 odds | 1.51 |
| Goal margin distribution | {"-1": 0.1674178751643147, "-10": 8.094850038312e-06, "-11": 1.4446425992552377e-06, "-12": 2.372916515962803e-07, "-13": 3.6094020464261966e-08, "-14": 5.1108489258009595e-09, "-15": 6.760033297399062e-10, "-16": 8.257906860836599e-11, "-17": 8.041909699745494e-12, "-2": 0.1144419384293144, "-3": 0.06081742968463693, "-4": 0.02628876048904719, "-5": 0.00951781926156674, "-6": 0.002954071927447537, "-7": 0.0008006505167882916, "-8": 0.00019233401698019712, "-9": 4.145009610604612e-05, "0": 0.23645138949390335, "1": 0.18141498369742015, "10": 3.849287327634518e-06, "11": 6.268226054652567e-07, "12": 9.394624003276527e-08, "13": 1.303901891113157e-08, "14": 1.6846722006037422e-09, "15": 2.0332178409100527e-10, "16": 2.2663019260300847e-11, "17": 2.0138155533496278e-12, "2": 0.11325438878388996, "3": 0.05491748092473944, "4": 0.02166034485268848, "5": 0.007155589554717867, "6": 0.0020264773051112094, "7": 0.0005011599739503428, "8": 0.0001098505416549407, "9": 2.1601522076682255e-05} |
| Raw goal margin distribution | {"-1": 0.18719121074692, "-10": 9.05091393615632e-06, "-11": 1.6152659743516248e-06, "-12": 2.6531761628708067e-07, "-13": 4.035700121506176e-08, "-14": 5.714479397294368e-09, "-15": 7.558445096664024e-10, "-16": 9.233229020486283e-11, "-17": 8.99172093741655e-12, "-2": 0.1279584094218278, "-3": 0.0680004347565001, "-4": 0.02939366480521106, "-5": 0.010641946742511251, "-6": 0.00330297048740862, "-7": 0.0008952134858697181, "-8": 0.00021505014008214992, "-9": 4.634567048501655e-05, "0": 0.21388440121875682, "1": 0.17065238735235544, "10": 3.62092512248943e-06, "11": 5.896358276970196e-07, "12": 8.837280040279722e-08, "13": 1.2265468157957645e-08, "14": 1.5847276067266942e-09, "15": 1.9125954840500662e-10, "16": 2.1318516599672414e-11, "17": 1.8943442535022858e-12, "2": 0.10653547700524087, "3": 0.05165945522347448, "4": 0.020375326693806924, "5": 0.006731078191770922, "6": 0.0019062548362013456, "7": 0.00047142823738702293, "8": 0.00010333356596736051, "9": 2.031999362841417e-05} |
| Unadjusted home-win probability | 35.8% |
| Unadjusted draw probability | 21.4% |
| Unadjusted away-win probability | 42.8% |
| Raw p over 1 5 | 89.9% |
| Raw p under 3 5 | 46.2% |
| Raw p btts yes | 73.1% |
| P home draw | 61.8% |
| P draw away | 61.9% |
| P home away | 76.4% |
| Raw p home draw | 57.2% |
| Raw p draw away | 64.2% |
| Raw p home away | 78.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:31Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.09, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:31Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.78, "price": 2.09, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.39 |
| Reference draw odds | 3.66 |
| Reference away odds | 2.84 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:00Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:00Z |
| Home probability edge | -2.3% |
| Draw probability edge | -2.3% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | +16.1% |
| Under 2.5 probability edge | -16.1% |
| Raw edge prob home | -0.0452 |
| Raw ev home | -0.1325 |
| Raw edge prob draw | -0.0451 |
| Raw ev draw | -0.2065 |
| Raw edge prob away | 0.0903 |
| Raw ev away | 0.2188 |
| Market p home draw | 66.3% |
| Market home draw odds | 1.46 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:05:31Z |
| Market reference home draw last update utc | 2026-10-22T15:05:36Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.7% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:05:31Z |
| Market reference draw away last update utc | 2026-10-22T15:05:36Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.0% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:05:31Z |
| Market reference home away last update utc | 2026-10-22T15:05:36Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.45 |
| Market reference dc draw away odds | 1.61 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:31Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.5% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:05:30Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market reference under 3 5 last update utc | 2026-10-22T15:05:30Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:05:31Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-22T15:05:31Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **43.9%**. Expected goals are 1.26 for Valencia and 1.54 for Villarreal (2.80 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 52.9%; Under 3.5 goals: 69.2%; Double Chance 1X: 56.1%; Double Chance X2: 69.8%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 84.8%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.2% | 3.31 |
| Draw | 25.9% | 3.85 |
| Villarreal win | 43.9% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.26 |
| Villarreal expected goals | 1.54 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 52.9% |
| Under 2.5 | 47.1% |
| Over 3.5 | 30.8% |
| Under 3.5 | 69.2% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.26% |
| 2 | 0-1 | 9.17% |
| 3 | 1-2 | 9.15% |
| 4 | 2-1 | 7.26% |
| 5 | 0-2 | 7.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.2% | 29.4% | 3.29 | -0.6% |
| Draw | 25.9% | 26.4% | 3.74 | -3.0% |
| Villarreal win | 43.9% | 44.2% | 2.16 | -5.3% |
| Over 2.5 | 52.9% | 55.3% | 1.79 | -5.3% |
| Under 2.5 | 47.1% | 44.7% | 2.19 | +3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0dae715cc56fe201f9e667917c126691 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2619 |
| Dc lambda away | 1.5380 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.51 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.25 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.58 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.21814910115246824, "-10": 1.491805388692337e-06, "-11": 2.0560133877849432e-07, "-12": 2.6031235670655438e-08, "-13": 3.0466277970720027e-09, "-14": 3.29392460011994e-10, "-15": 2.990531698432365e-11, "-2": 0.13246600498194777, "-3": 0.05914765643127719, "-4": 0.02083866452423833, "-5": 0.0060363555030936355, "-6": 0.0014811560692095133, "-7": 0.0003148107598665561, "-8": 5.896761923651152e-05, "-9": 9.86804368739239e-06, "0": 0.2594563196680701, "1": 0.17249399921668784, "10": 1.992031731526047e-07, "11": 2.252455569502003e-08, "12": 2.339759898247334e-09, "13": 2.2466846792064288e-10, "14": 1.9928866207483778e-11, "15": 1.4844431236630682e-12, "2": 0.08616260180590722, "3": 0.03156444240603773, "4": 0.009123819349788948, "5": 0.0021683421794952778, "6": 0.0004365158781986081, "7": 7.61193384489657e-05, "8": 1.169782838773409e-05, "9": 1.60608649293555e-06} |
| Raw goal margin distribution | {"-1": 0.2162983001935622, "-10": 1.479148747755901e-06, "-11": 2.038569944151515e-07, "-12": 2.5810383805182542e-08, "-13": 3.0207798718756035e-09, "-14": 3.2659785816570664e-10, "-15": 2.9651596987043935e-11, "-2": 0.13134214883150827, "-3": 0.05864584121103684, "-4": 0.02066186700327662, "-5": 0.005985142399329272, "-6": 0.001468589778270425, "-7": 0.00031213987076750933, "-8": 5.846733147162605e-05, "-9": 9.784322119791762e-06, "0": 0.2553019359815915, "1": 0.17699122396839193, "10": 2.0439675347996736e-07, "11": 2.3111810845070386e-08, "12": 2.4007615920756763e-09, "13": 2.3052597368576178e-10, "14": 2.0448447125015347e-11, "15": 1.5231451909149746e-12, "2": 0.08840901378123621, "3": 0.03238738344924383, "4": 0.00936169351582532, "5": 0.002224874709114122, "6": 0.0004478966219975885, "7": 7.810390472089729e-05, "8": 1.2002811538483688e-05, "9": 1.6479600187521434e-06} |
| Unadjusted home-win probability | 31.0% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 43.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 56.5% |
| P home draw | 56.1% |
| P draw away | 69.8% |
| P home away | 74.1% |
| Raw p home draw | 56.5% |
| Raw p draw away | 69.0% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.24 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.19 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:00Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:00Z |
| Home probability edge | +0.8% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.0157 |
| Raw ev home | 0.0196 |
| Raw edge prob draw | -0.0083 |
| Raw ev draw | -0.0452 |
| Raw edge prob away | -0.0074 |
| Raw ev away | -0.0609 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **55.0%**. Expected goals are 1.20 for Athletic Bilbao and 0.62 for Getafe (1.82 combined). The most likely exact score is 1-0 at 21.2%. Goal-market probabilities: at least one goal: 85.5%; Over 2.5 goals: 28.7%; Under 3.5 goals: 88.5%; Double Chance 1X: 82.5%; Double Chance X2: 45.0%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 31.8%; BTTS No (at least one team does not score): 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 55.0% | 1.82 |
| Draw | 27.5% | 3.63 |
| Getafe win | 17.5% | 5.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.20 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.82 |
| Over 0.5 | 85.5% |
| Under 0.5 | 14.5% |
| Over 1.5 | 55.3% |
| Under 1.5 | 44.7% |
| Over 2.5 | 28.7% |
| Under 2.5 | 71.3% |
| Over 3.5 | 11.5% |
| Under 3.5 | 88.5% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.16% |
| 2 | 0-0 | 14.49% |
| 3 | 2-0 | 12.84% |
| 4 | 1-1 | 10.88% |
| 5 | 0-1 | 9.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 55.0% | 60.3% | 1.63 | -10.3% |
| Draw | 27.5% | 23.8% | 4.09 | +12.6% |
| Getafe win | 17.5% | 15.9% | 5.55 | -3.1% |
| Over 2.5 | 28.7% | 41.1% | 2.36 | -32.2% |
| Under 2.5 | 71.3% | 58.9% | 1.69 | +20.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:00:00+00:00 |
| Fixture id | 9c4254cba9944a839b421db27260504d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1966 |
| Dc lambda away | 0.6241 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 31.8% |
| P btts no | 68.2% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.90 |
| Fair Over 1.5 odds | 1.81 |
| Fair Under 1.5 odds | 2.24 |
| Fair Over 2.5 odds | 3.48 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.67 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.92 |
| Fair Under 4.5 odds | 1.04 |
| Goal margin distribution | {"-1": 0.12933242610470502, "-10": 3.9210674115806336e-10, "-11": 2.2120272302066022e-11, "-12": 1.1432670849105537e-12, "-13": 5.1901278926623644e-14, "-2": 0.03679951341216439, "-3": 0.007221519491354009, "-4": 0.0010870567723325578, "-5": 0.0001324391629005346, "-6": 1.3537560277060773e-05, "-7": 1.1911810110901336e-06, "-8": 9.197573633219569e-08, "-9": 6.3255209562187416e-09, "0": 0.27531290487588933, "1": 0.3022939868791814, "10": 3.1812399253132674e-07, "11": 3.441059773796145e-08, "12": 3.410036914571328e-09, "13": 2.968240402400054e-10, "2": 0.16343954057440002, "3": 0.06149690748023602, "4": 0.017749517321274492, "5": 0.0041462967453437275, "6": 0.0008126321298050044, "7": 0.00013710111286867273, "8": 2.029766704070341e-05, "9": 2.6765710852816198e-06} |
| Raw goal margin distribution | {"-1": 0.1411063352704113, "-10": 4.2780257779162807e-10, "-11": 2.41340138257452e-11, "-12": 1.2473455686697705e-12, "-13": 5.6626164727276084e-14, "-2": 0.04014959460453484, "-3": 0.007878937875052651, "-4": 0.001186018093022913, "-5": 0.0001444958970153858, "-6": 1.4769965868048048e-05, "-7": 1.299621387930626e-06, "-8": 1.0034884118795334e-07, "-9": 6.901371200487697e-09, "0": 0.31271522472847935, "1": 0.27300638531706745, "10": 2.8730270879758784e-07, "11": 3.107674420528637e-08, "12": 3.0796571954868683e-09, "13": 2.6806639171926056e-10, "2": 0.14760478251898723, "3": 0.05553881039012361, "4": 0.016029864222673187, "5": 0.003744584861195496, "6": 0.0007339006727885827, "7": 0.00012381814019404616, "8": 1.8331137732377584e-05, "9": 2.4172528358262203e-06} |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 31.3% |
| Unadjusted away-win probability | 19.0% |
| Raw p over 1 5 | 54.6% |
| Raw p under 3 5 | 88.8% |
| Raw p btts yes | 32.7% |
| P home draw | 82.5% |
| P draw away | 45.0% |
| P home away | 72.5% |
| Raw p home draw | 81.0% |
| Raw p draw away | 50.3% |
| Raw p home away | 68.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.08, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:00Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.62 |
| Reference draw odds | 3.94 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.29 |
| Reference Under 2.5 odds | 1.64 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:00Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:00Z |
| Home probability edge | -5.3% |
| Draw probability edge | +3.7% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -12.4% |
| Under 2.5 probability edge | +12.4% |
| Raw edge prob home | -0.1066 |
| Raw ev home | -0.1902 |
| Raw edge prob draw | 0.0748 |
| Raw ev draw | 0.2790 |
| Raw edge prob away | 0.0318 |
| Raw ev away | 0.0572 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **56.2%**. Expected goals are 1.97 for Barcelona and 1.35 for Real Madrid (3.32 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 65.5%; Under 3.5 goals: 57.2%; Double Chance 1X: 75.9%; Double Chance X2: 43.8%; Double Chance 12 (either team wins): 80.4%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 56.2% | 1.78 |
| Draw | 19.6% | 5.10 |
| Real Madrid win | 24.1% | 4.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.97 |
| Real Madrid expected goals | 1.35 |
| Expected total goals | 3.32 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.30% |
| 2 | 1-1 | 8.65% |
| 3 | 2-0 | 7.62% |
| 4 | 1-0 | 7.50% |
| 5 | 3-1 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 56.2% | 60.8% | 1.63 | -8.3% |
| Draw | 19.6% | 17.0% | 5.97 | +17.1% |
| Real Madrid win | 24.1% | 22.3% | 3.90 | -5.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T20:00:00+00:00 |
| Fixture id | 72089d103a5fe6a922c35e17efba6ffc |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9717 |
| Dc lambda away | 1.3512 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.75 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.59 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.1370134659538049, "-10": 2.3771838762264284e-07, "-11": 2.8631758288752126e-08, "-12": 3.170514346541854e-09, "-13": 3.2482805045478587e-10, "-14": 3.094176585948162e-11, "-15": 2.7266847252221927e-12, "-16": 1.9739667218927196e-13, "-2": 0.06850051896785694, "-3": 0.025759283279202363, "-4": 0.007748895569355399, "-5": 0.0019322499408983408, "-6": 0.0004102557880354562, "-7": 7.571305008535447e-05, "-8": 1.2343846085125249e-05, "-9": 1.8011181119317284e-06, "0": 0.19618839359060997, "1": 0.2352877244382535, "10": 1.2194458607426705e-05, "11": 2.1433041586341057e-06, "12": 3.463391205793654e-07, "13": 5.1779922052911646e-08, "14": 7.197621450468847e-09, "15": 9.255819381071856e-10, "16": 9.778130122575507e-11, "2": 0.17088553131451098, "3": 0.09377374185405035, "4": 0.04116454490909269, "5": 0.014979001102141284, "6": 0.004640986515641952, "7": 0.0012498628834384758, "8": 0.00029735700008977757, "9": 6.331489658763543e-05} |
| Raw goal margin distribution | {"-1": 0.14760399261156618, "-10": 2.5609295324385303e-07, "-11": 3.084486484221922e-08, "-12": 3.4155808914403456e-09, "-13": 3.499358024818012e-10, "-14": 3.3333425641911545e-11, "-15": 2.9374452301751305e-12, "-16": 2.1265454997829662e-13, "-2": 0.0737953019816971, "-3": 0.027750360392346813, "-4": 0.008347850456921966, "-5": 0.0020816041986429106, "-6": 0.00044196672118676603, "-7": 8.156532941926831e-05, "-8": 1.3297970047421751e-05, "-9": 1.9403364671890198e-06, "0": 0.2227426303356912, "1": 0.21636886649588685, "10": 1.1213934737646495e-05, "11": 1.9709667916877757e-06, "12": 3.1849091626794694e-07, "13": 4.7616436720539655e-08, "14": 6.618879919989699e-09, "15": 8.511583648295001e-10, "16": 8.991896777114558e-11, "2": 0.15714508183265324, "3": 0.08623364555239858, "4": 0.03785461372055899, "5": 0.013774579602266848, "6": 0.004267817176648616, "7": 0.001149364744848102, "8": 0.00027344731735431824, "9": 5.8223914739615314e-05} |
| Unadjusted home-win probability | 51.7% |
| Unadjusted draw probability | 22.3% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 64.0% |
| P home draw | 75.9% |
| P draw away | 43.8% |
| P home away | 80.4% |
| Raw p home draw | 74.0% |
| Raw p draw away | 48.3% |
| Raw p home away | 77.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.47, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.64, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.61 |
| Reference draw odds | 5.45 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.18 |
| Reference Under 2.5 odds | 5.01 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:32Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:32Z |
| Home probability edge | -4.5% |
| Draw probability edge | +2.7% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -17.7% |
| Under 2.5 probability edge | +17.7% |
| Raw edge prob home | -0.0904 |
| Raw ev home | -0.1571 |
| Raw edge prob draw | 0.0531 |
| Raw ev draw | 0.3298 |
| Raw edge prob away | 0.0373 |
| Raw ev away | 0.0145 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **36.8%**. Expected goals are 1.41 for Celta Vigo and 1.29 for Real Betis (2.70 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.5%; Double Chance 1X: 63.6%; Double Chance X2: 63.2%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 36.8% | 2.72 |
| Draw | 26.8% | 3.73 |
| Real Betis win | 36.4% | 2.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.41 |
| Real Betis expected goals | 1.29 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.5% |
| Under 3.5 | 71.5% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.74% |
| 2 | 0-1 | 8.99% |
| 3 | 1-0 | 8.54% |
| 4 | 1-2 | 8.43% |
| 5 | 2-1 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 36.8% | 33.8% | 2.94 | +8.2% |
| Draw | 26.8% | 27.3% | 3.54 | -5.1% |
| Real Betis win | 36.4% | 38.9% | 2.44 | -11.2% |
| Over 2.5 | 50.4% | 52.1% | 1.88 | -5.2% |
| Under 2.5 | 49.6% | 47.9% | 2.02 | +0.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:15:00+00:00 |
| Fixture id | 2013e3955186ebe5258e85eb741a7553 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4144 |
| Dc lambda away | 1.2851 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.02 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.51 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.34 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.20403786329070192, "-10": 2.881620034774417e-07, "-11": 3.3213850679766804e-08, "-12": 3.515372199479014e-09, "-13": 3.4175398011409223e-10, "-14": 2.7766552803825583e-11, "-2": 0.10504483369093819, "-3": 0.039490552031617686, "-4": 0.011684208693315198, "-5": 0.0028381420137239587, "-6": 0.0005834296549326411, "-7": 0.00010382456758715658, "-8": 1.627582965075133e-05, "-9": 2.278805587517098e-06, "0": 0.26818799788999104, "1": 0.19345094218298406, "10": 6.464975159708104e-07, "11": 8.201161519689804e-08, "12": 9.553300553581788e-09, "13": 1.022166631275388e-09, "14": 9.140207912945059e-11, "2": 0.10947045332364358, "3": 0.04529407702234285, "4": 0.014749371202172843, "5": 0.003943068428919793, "6": 0.0008921023472876053, "7": 0.0001747238955844872, "8": 3.0145417260020088e-05, "9": 4.645275011430602e-06} |
| Raw goal margin distribution | {"-1": 0.18998180042610321, "-10": 2.6831067210814176e-07, "-11": 3.092576568612498e-08, "-12": 3.2732000269644463e-09, "-13": 3.1821072519445786e-10, "-14": 2.5853729343271544e-11, "-2": 0.09780834943185004, "-3": 0.036770068328437176, "-4": 0.010879289600027412, "-5": 0.00264262387841235, "-6": 0.0005432374877802121, "-7": 9.66721468287818e-05, "-8": 1.5154596164697243e-05, "-9": 2.1218198492930942e-06, "0": 0.26297814787846463, "1": 0.2093639215842976, "10": 6.996774154251784e-07, "11": 8.875776555713898e-08, "12": 1.0339140483892948e-08, "13": 1.1062484990845904e-09, "14": 9.892067472795842e-11, "2": 0.11847532582069169, "3": 0.049019898703667526, "4": 0.015962631977612732, "5": 0.004267419222869503, "6": 0.0009654853255044969, "7": 0.00018909641670006416, "8": 3.262513329804772e-05, "9": 5.027388247666025e-06} |
| Unadjusted home-win probability | 39.8% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 33.9% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 55.0% |
| P home draw | 63.6% |
| P draw away | 63.2% |
| P home away | 73.2% |
| Raw p home draw | 66.1% |
| Raw p draw away | 60.2% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.16, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.16, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.84 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T15:05:30Z |
| Market best under 2 5 last update utc | 2026-10-22T15:05:30Z |
| Home probability edge | +3.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | 0.0605 |
| Raw ev home | 0.1709 |
| Raw edge prob draw | -0.0104 |
| Raw ev draw | -0.0691 |
| Raw edge prob away | -0.0501 |
| Raw ev away | -0.1735 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **56.3%**. Expected goals are 1.97 for Real Sociedad and 1.18 for Levante (3.16 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.1%; Under 3.5 goals: 61.1%; Double Chance 1X: 78.7%; Double Chance X2: 43.7%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 56.3% | 1.78 |
| Draw | 22.4% | 4.46 |
| Levante win | 21.3% | 4.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.97 |
| Levante expected goals | 1.18 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 82.6% |
| Under 1.5 | 17.4% |
| Over 2.5 | 61.1% |
| Under 2.5 | 38.9% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.26% |
| 2 | 2-1 | 9.95% |
| 3 | 2-0 | 8.40% |
| 4 | 1-0 | 8.30% |
| 5 | 3-1 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 56.3% | 57.1% | 1.68 | -5.5% |
| Draw | 22.4% | 22.6% | 4.32 | -3.2% |
| Levante win | 21.3% | 20.3% | 4.74 | +1.1% |
| Over 2.5 | 61.1% | 58.1% | 1.71 | +4.4% |
| Under 2.5 | 38.9% | 41.9% | 2.32 | -9.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:30:00+00:00 |
| Fixture id | 3cb8660cd2375b60e81144a7572cfb89 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:31Z |
| Market best draw last update utc | 2026-10-22T15:05:31Z |
| Market best away last update utc | 2026-10-22T15:05:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9724 |
| Dc lambda away | 1.1841 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.13 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.74 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.57 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.72 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.12884102892998694, "-10": 7.489707098263989e-08, "-11": 7.924460212528613e-09, "-12": 7.705825966678104e-10, "-13": 6.93098180342849e-11, "-14": 5.795910645010174e-12, "-15": 4.492757133375067e-13, "-16": 2.90150404024683e-14, "-2": 0.05823939968434715, "-3": 0.01955519431208576, "-4": 0.005221270741990337, "-5": 0.0011514525197755666, "-6": 0.00021571795858120284, "-7": 3.507365156128775e-05, "-8": 5.0323384571134644e-06, "-9": 6.456989074039183e-07, "0": 0.2240115522010773, "1": 0.2297135530097691, "10": 1.3092809938153396e-05, "11": 2.307390541203355e-06, "12": 3.7372659528592236e-07, "13": 5.599032080828332e-08, "14": 7.79871891970547e-09, "15": 1.0069268419305452e-09, "16": 1.0831573338654969e-10, "2": 0.17183744446963672, "3": 0.0961051012406436, "4": 0.04274092408306044, "5": 0.015699908373270115, "6": 0.00489915042416803, "7": 0.0013267797820510669, "8": 0.0003170816383746456, "9": 6.776644320154766e-05} |
| Raw goal margin distribution | {"-1": 0.1350297120654543, "-10": 7.849463803046316e-08, "-11": 8.305099622833291e-09, "-12": 8.075963613054256e-10, "-13": 7.263900987288918e-11, "-14": 6.07430840976989e-12, "-15": 4.708559898487863e-13, "-16": 3.04087337989347e-14, "-2": 0.0610368407917301, "-3": 0.02049449836961355, "-4": 0.005472066551795797, "-5": 0.0012067607926883723, "-6": 0.00022607964308012424, "-7": 3.6758361142694095e-05, "-8": 5.2740591915731795e-06, "-9": 6.767140737063529e-07, "0": 0.22194711887009305, "1": 0.22637457041158734, "10": 1.2902500468067683e-05, "11": 2.273851654344731e-06, "12": 3.682943228675668e-07, "13": 5.5176478070682534e-08, "14": 7.68536127746004e-09, "15": 9.922907390154279e-10, "16": 1.067413188857579e-10, "2": 0.16933971532269457, "3": 0.09470817338665077, "4": 0.0421196668700066, "5": 0.015471703636699054, "6": 0.004827939223096772, "7": 0.001307494482834527, "8": 0.0003124727241035279, "9": 6.678142959818826e-05} |
| Unadjusted home-win probability | 55.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 22.4% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.2% |
| Raw p btts yes | 60.0% |
| P home draw | 78.7% |
| P draw away | 43.7% |
| P home away | 77.6% |
| Raw p home draw | 77.6% |
| Raw p draw away | 44.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:31Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:31Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.71 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:01Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:01Z |
| Home probability edge | -0.8% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0164 |
| Raw ev home | -0.0684 |
| Raw edge prob draw | -0.0041 |
| Raw ev draw | -0.0412 |
| Raw edge prob away | 0.0205 |
| Raw ev away | 0.0594 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **48.4%**. Expected goals are 1.51 for Sevilla and 1.06 for CA Osasuna (2.57 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 47.3%; Under 3.5 goals: 74.2%; Double Chance 1X: 75.1%; Double Chance X2: 51.6%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 48.4% | 2.07 |
| Draw | 26.7% | 3.74 |
| CA Osasuna win | 24.9% | 4.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.51 |
| CA Osasuna expected goals | 1.06 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 47.3% |
| Under 2.5 | 52.7% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.71% |
| 2 | 1-0 | 11.53% |
| 3 | 2-1 | 9.44% |
| 4 | 2-0 | 8.92% |
| 5 | 0-0 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 48.4% | 49.3% | 1.94 | -6.2% |
| Draw | 26.7% | 27.1% | 3.47 | -7.3% |
| CA Osasuna win | 24.9% | 23.6% | 4.31 | +7.4% |
| Over 2.5 | 47.3% | 44.7% | 2.19 | +3.6% |
| Under 2.5 | 52.7% | 55.3% | 1.79 | -5.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T20:00:00+00:00 |
| Fixture id | 85e464708d03287f24590e1478aeca31 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5108 |
| Dc lambda away | 1.0580 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.42 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.70 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.88 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.47 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.15454933887139138, "-10": 4.068802303587608e-08, "-11": 3.867244562223229e-09, "-12": 3.375450892827245e-10, "-13": 2.7229790105998802e-11, "-14": 2.032718664339696e-12, "-15": 1.2957212616818553e-13, "-2": 0.06718958469110792, "-3": 0.021086079520439692, "-4": 0.005183451586874543, "-5": 0.0010432589420994974, "-6": 0.00017740045394792778, "-7": 2.608519976527913e-05, "-8": 3.3762395078042695e-06, "-9": 3.900815205068916e-07, "0": 0.26702848193875106, "1": 0.2385015009478737, "10": 1.5420339854031876e-06, "11": 2.092838308053157e-07, "12": 2.608389930084513e-08, "13": 3.0046348247531735e-09, "14": 3.202811356691434e-10, "15": 2.915226829423055e-11, "2": 0.14732479885867145, "3": 0.06602013715680817, "4": 0.023174283251728656, "5": 0.006660181465033256, "6": 0.0016171688049130236, "7": 0.000339548235118603, "8": 6.275484194635987e-05, "9": 1.0353234512742568e-05} |
| Raw goal margin distribution | {"-1": 0.16291657962913333, "-10": 4.2890856688765586e-08, "-11": 4.076615670229826e-09, "-12": 3.5581964839275934e-10, "-13": 2.8704000291972277e-11, "-14": 2.1427692577714763e-12, "-15": 1.3658711039949247e-13, "-2": 0.07082720252647778, "-3": 0.022227671618295437, "-4": 0.005464081628388796, "-5": 0.0010997405731757563, "-6": 0.00018700484513817562, "-7": 2.749744227788871e-05, "-8": 3.5590277942110247e-06, "-9": 4.11200381454872e-07, "0": 0.2630862051737793, "1": 0.2337914973888378, "10": 1.5115814074087593e-06, "11": 2.0515082709664245e-07, "12": 2.5568786154587136e-08, "13": 2.9452983398172425e-09, "14": 3.1395612185204623e-10, "15": 2.8576560020387005e-11, "2": 0.14441538183529495, "3": 0.06471635047311527, "4": 0.02271663012937953, "5": 0.006528654081434159, "6": 0.0015852324405864658, "7": 0.00033284272848859434, "8": 6.151553935187142e-05, "9": 1.0148775542007584e-05} |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 72.9% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.1% |
| P home draw | 75.1% |
| P draw away | 51.6% |
| P home away | 73.3% |
| Raw p home draw | 73.7% |
| Raw p draw away | 52.6% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.48, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.96, "price": 1.48, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.97 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:01Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:01Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | +2.6% |
| Under 2.5 probability edge | -2.6% |
| Raw edge prob home | -0.0191 |
| Raw ev home | -0.0801 |
| Raw edge prob draw | -0.0079 |
| Raw ev draw | -0.0871 |
| Raw edge prob away | 0.0270 |
| Raw ev away | 0.1325 |

</details>


---

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **63.6%**. Expected goals are 2.18 for Villarreal and 0.98 for Espanyol (3.16 combined). The most likely exact score is 2-0 at 9.9%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.0%; Under 3.5 goals: 61.3%; Double Chance 1X: 83.9%; Double Chance X2: 36.4%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 78.9%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 63.6% | 1.57 |
| Draw | 20.3% | 4.93 |
| Espanyol win | 16.1% | 6.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.18 |
| Espanyol expected goals | 0.98 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 82.5% |
| Under 1.5 | 17.5% |
| Over 2.5 | 61.0% |
| Under 2.5 | 39.0% |
| Over 3.5 | 38.7% |
| Under 3.5 | 61.3% |
| Over 4.5 | 21.1% |
| Under 4.5 | 78.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.95% |
| 2 | 2-1 | 9.74% |
| 3 | 1-1 | 9.45% |
| 4 | 1-0 | 8.93% |
| 5 | 3-0 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 63.6% | 62.7% | 1.56 | -0.7% |
| Draw | 20.3% | 20.7% | 4.31 | -12.7% |
| Espanyol win | 16.1% | 16.6% | 5.40 | -13.0% |
| Over 2.5 | 61.0% | 60.0% | 1.66 | +1.2% |
| Under 2.5 | 39.0% | 40.0% | 2.42 | -5.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:00:00+00:00 |
| Fixture id | 00b03cb40c27ed23e2ecb18f062a5122 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1799 |
| Dc lambda away | 0.9794 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.05 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.70 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.58 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.74 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.10606526157002572, "-10": 1.1871904515062181e-08, "-11": 1.0404083777531394e-09, "-12": 8.377964147541872e-11, "-13": 6.239248091781353e-12, "-14": 4.3211262452183005e-13, "-15": 2.7958627869781878e-14, "-16": 1.687062539017576e-15, "-17": 8.634883948552108e-17, "-2": 0.040535093438330214, "-3": 0.011390751978342644, "-4": 0.0025355118692275535, "-5": 0.0004650951358396874, "-6": 7.237032446545171e-05, "-7": 9.763704271688923e-06, "-8": 1.1616376879245981e-06, "-9": 1.2353411475882126e-07, "0": 0.20265635088908465, "1": 0.22829887400943022, "10": 3.389260874324319e-05, "11": 6.610960177777003e-06, "12": 1.184882527389154e-06, "13": 1.9640165808985642e-07, "14": 3.0275125152136006e-08, "15": 4.359944322850972e-09, "16": 5.855613036780324e-10, "17": 6.670736551339622e-11, "2": 0.19213522944576958, "3": 0.12017228465160822, "4": 0.0595379212584848, "5": 0.02430781454421143, "6": 0.008418616646980572, "7": 0.0025279642510839763, "8": 0.0006694268113071502, "9": 0.00015845115649557422} |
| Raw goal margin distribution | {"-1": 0.10289364005602437, "-10": 1.1516904327302485e-08, "-11": 1.0092975168983764e-09, "-12": 8.127441677314121e-11, "-13": 6.05267867983472e-12, "-14": 4.191913562751083e-13, "-15": 2.7122593674031433e-14, "-16": 1.636615071439502e-15, "-17": 8.37667892179081e-17, "-2": 0.039322990884506005, "-3": 0.011050139477129765, "-4": 0.002459693605317097, "-5": 0.0004511876064841629, "-6": 7.020626740612563e-05, "-7": 9.471744641683294e-06, "-8": 1.1269017618734092e-06, "-9": 1.1984013003392135e-07, "0": 0.19863381028982233, "1": 0.2314704219723781, "10": 3.436344783382137e-05, "11": 6.702800215867127e-06, "12": 1.2013430192876745e-06, "13": 1.9913008713418337e-07, "14": 3.0695709843676284e-08, "15": 4.42051305143407e-09, "16": 5.936959726198706e-10, "17": 6.763407008049317e-11, "2": 0.19480438888951732, "3": 0.12184172856035853, "4": 0.06036502727775364, "5": 0.024645500833887234, "6": 0.008535568807140887, "7": 0.002563082951978661, "8": 0.0006787265472298783, "9": 0.00016065237384625423} |
| Unadjusted home-win probability | 64.5% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 15.6% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.2% |
| Raw p btts yes | 55.6% |
| P home draw | 83.9% |
| P draw away | 36.4% |
| P home away | 79.7% |
| Raw p home draw | 84.4% |
| Raw p draw away | 35.5% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.55 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:01Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:01Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0177 |
| Raw ev home | 0.0064 |
| Raw edge prob draw | -0.0080 |
| Raw ev draw | -0.1439 |
| Raw edge prob away | -0.0096 |
| Raw ev away | -0.1562 |

</details>


---

## 2026-10-31 — Barcelona vs Alavés

The model's most likely 1X2 outcome is **Barcelona win** at **84.3%**. Expected goals are 2.84 for Barcelona and 0.70 for Alavés (3.54 combined). The most likely exact score is 2-0 at 12.1%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 69.7%; Under 3.5 goals: 52.0%; Double Chance 1X: 95.1%; Double Chance X2: 15.7%; Double Chance 12 (either team wins): 89.2%; Under 4.5 goals: 71.1%; BTTS Yes (both teams score): 46.9%; BTTS No (at least one team does not score): 53.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 84.3% | 1.19 |
| Draw | 10.8% | 9.23 |
| Alavés win | 4.9% | 20.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.84 |
| Alavés expected goals | 0.70 |
| Expected total goals | 3.54 |
| Over 0.5 | 97.4% |
| Under 0.5 | 2.6% |
| Over 1.5 | 87.5% |
| Under 1.5 | 12.5% |
| Over 2.5 | 69.7% |
| Under 2.5 | 30.3% |
| Over 3.5 | 48.0% |
| Under 3.5 | 52.0% |
| Over 4.5 | 28.9% |
| Under 4.5 | 71.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.14% |
| 2 | 3-0 | 11.49% |
| 3 | 2-1 | 8.53% |
| 4 | 1-0 | 8.42% |
| 5 | 4-0 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 84.3% | 87.6% | 1.17 | -1.4% |
| Draw | 10.8% | 9.1% | 6.29 | -31.9% |
| Alavés win | 4.9% | 3.3% | 21.66 | +5.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:00:00+00:00 |
| Fixture id | 2db2b55e71574a19ff0557898d3e9933 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8382 |
| Dc lambda away | 0.7025 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.9% |
| P btts no | 53.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 38.24 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.01 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.30 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.92 |
| Fair Over 4.5 odds | 3.46 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.036002957072418205, "-10": 2.127148170904811e-10, "-11": 1.338492605670599e-11, "-12": 7.737829186821739e-13, "-13": 4.1364607551140635e-14, "-14": 2.0562288341943735e-15, "-15": 9.55111420663726e-17, "-16": 4.163143936921907e-18, "-17": 1.708970285929306e-19, "-18": 6.6001108489637665e-21, "-19": 2.208517060891823e-22, "-2": 0.010079153433331003, "-3": 0.002048917111633188, "-4": 0.0003289981439153397, "-5": 4.3461884232746406e-05, "-6": 4.865370078505481e-06, "-7": 4.7191019519611133e-07, "-8": 4.0345659658628616e-08, "-9": 3.0820835603063347e-09, "0": 0.10834509934250117, "1": 0.2031220765292983, "10": 0.00033739324102383133, "11": 8.577469934540144e-05, "12": 2.0033967234750073e-05, "13": 4.326944469603219e-06, "14": 8.690173572700767e-07, "15": 1.6308560788272407e-07, "16": 2.8720210436479624e-08, "17": 4.763271051306668e-09, "18": 7.432357753070091e-10, "19": 1.0048025478796076e-10, "2": 0.22517799664797541, "3": 0.1849400099557936, "4": 0.11997880378883345, "5": 0.06403600399941337, "6": 0.028962506547692765, "7": 0.011349695698722174, "8": 0.003920362902606343, "9": 0.0012099807244626665} |
| Raw goal margin distribution | {"-1": 0.0473819388532106, "-10": 2.799447955422093e-10, "-11": 1.7615323838481335e-11, "-12": 1.0183423229628355e-12, "-13": 5.4438175779086256e-14, "-14": 2.7061140754087062e-15, "-15": 1.2569809430059723e-16, "-16": 5.478934162534862e-18, "-17": 2.249102078670379e-19, "-18": 8.686121199460917e-21, "-19": 2.906534041772257e-22, "-2": 0.013264739079893043, "-3": 0.0026964914327294153, "-4": 0.00043298026621704306, "-5": 5.719831115591725e-05, "-6": 6.4031036976847735e-06, "-7": 6.210606525461987e-07, "-8": 5.309718240900003e-08, "-9": 4.056197231276804e-09, "0": 0.12541369768381258, "1": 0.19531656314174056, "10": 0.0003244279961588639, "11": 8.247857528299455e-05, "12": 1.926410803417135e-05, "13": 4.160669963346707e-06, "14": 8.356230225325959e-07, "15": 1.568186037372491e-07, "16": 2.7616558923626553e-08, "17": 4.580229519855125e-09, "18": 7.146749369510959e-10, "19": 9.661903011295842e-11, "2": 0.2165249250692901, "3": 0.17783319149336618, "4": 0.11536829480232345, "5": 0.061575247911036995, "6": 0.02784954415356011, "7": 0.010913553043847807, "8": 0.0037697123891651564, "9": 0.0011634839531374785} |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 12.5% |
| Unadjusted away-win probability | 6.4% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 52.8% |
| Raw p btts yes | 47.6% |
| P home draw | 95.1% |
| P draw away | 15.7% |
| P home away | 89.2% |
| Raw p home draw | 93.6% |
| Raw p draw away | 18.9% |
| Raw p home away | 87.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.82, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.12 |
| Reference draw odds | 7.70 |
| Reference away odds | 18.25 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.24 |
| Reference Under 2.5 odds | 4.12 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:32Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:32Z |
| Home probability edge | -3.2% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | -0.0648 |
| Raw ev home | -0.0514 |
| Raw edge prob draw | 0.0341 |
| Raw ev draw | -0.2111 |
| Raw edge prob away | 0.0307 |
| Raw ev away | 0.3828 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **58.1%**. Expected goals are 1.23 for Levante and 1.94 for Atlético Madrid (3.16 combined). The most likely exact score is 1-2 at 10.5%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 61.8%; Under 3.5 goals: 60.7%; Double Chance 1X: 41.9%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 78.4%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 20.4% | 4.89 |
| Draw | 21.4% | 4.67 |
| Atlético Madrid win | 58.1% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.23 |
| Atlético Madrid expected goals | 1.94 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.8% |
| Under 2.5 | 38.2% |
| Over 3.5 | 39.3% |
| Under 3.5 | 60.7% |
| Over 4.5 | 21.6% |
| Under 4.5 | 78.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.54% |
| 2 | 1-1 | 9.77% |
| 3 | 0-1 | 8.63% |
| 4 | 0-2 | 8.59% |
| 5 | 1-3 | 6.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 20.4% | 17.1% | 4.56 | -6.8% |
| Draw | 21.4% | 20.3% | 4.63 | -0.8% |
| Atlético Madrid win | 58.1% | 62.6% | 1.61 | -6.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T13:00:00+00:00 |
| Fixture id | 005711684f3e51024ac40c1ee69978e9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Levante |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2268 |
| Dc lambda away | 1.9355 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.61 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.62 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.63 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.24271410008119837, "-10": 1.1544405335743326e-05, "-11": 1.9958767130830354e-06, "-12": 3.1714550689126925e-07, "-13": 4.661474891786458e-08, "-14": 6.3700438419492885e-09, "-15": 8.067293801971143e-10, "-16": 8.497626840860999e-11, "-2": 0.17756709094008838, "-3": 0.0972319650677475, "-4": 0.04236830766665364, "-5": 0.015255194334949944, "-6": 0.004667504891856439, "-7": 0.0012396142043638232, "-8": 0.0002905618600848233, "-9": 6.091197089655174e-05, "0": 0.21414782120942924, "1": 0.12129069380207297, "10": 9.583888271607008e-08, "11": 1.0502620305274624e-08, "12": 1.0578310137327063e-09, "13": 9.855413729680932e-11, "14": 8.536654630768784e-12, "15": 6.852782413525877e-13, "16": 4.575415123037447e-14, "2": 0.05656951109363769, "3": 0.019634632962686468, "4": 0.005423112579629532, "5": 0.0012377103600812926, "6": 0.000240037913020374, "7": 4.040874692211274e-05, "8": 6.003730995019745e-06, "9": 7.977724757698188e-07} |
| Raw goal margin distribution | {"-1": 0.2240601462746124, "-10": 1.0657152375221391e-05, "-11": 1.8424822790677221e-06, "-12": 2.927710777438202e-07, "-13": 4.303214134488656e-08, "-14": 5.880469880099125e-09, "-15": 7.447276564094224e-10, "-16": 7.844536070683263e-11, "-2": 0.16392005390821363, "-3": 0.0897591376370768, "-4": 0.039112063164119276, "-5": 0.014082746214550482, "-6": 0.004308780694887346, "-7": 0.001144342829118402, "-8": 0.0002682305348170918, "-9": 5.623054080661358e-05, "0": 0.22525759111250448, "1": 0.14120975534767793, "10": 1.1157810015676372e-07, "11": 1.2227421555008344e-08, "12": 1.231554161048328e-09, "13": 1.1473926960046835e-10, "14": 9.938593589592275e-12, "15": 7.978186105885071e-13, "16": 5.326816344150068e-14, "2": 0.06585968445943383, "3": 0.022859146321042998, "4": 0.006313727595969218, "5": 0.0014409743374341106, "6": 0.00027945833195650255, "7": 4.7044905820138446e-05, "8": 6.989698536669759e-06, "9": 9.287873009482456e-07} |
| Unadjusted home-win probability | 23.8% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 82.6% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.7% |
| P home draw | 41.9% |
| P draw away | 79.6% |
| P home away | 78.6% |
| Raw p home draw | 46.3% |
| Raw p draw away | 76.2% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.10 |
| Reference draw odds | 4.35 |
| Reference away odds | 1.54 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:32Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:32Z |
| Home probability edge | +3.4% |
| Draw probability edge | +1.1% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | 0.0671 |
| Raw ev home | 0.0854 |
| Raw edge prob draw | 0.0222 |
| Raw ev draw | 0.0429 |
| Raw edge prob away | -0.0894 |
| Raw ev away | -0.1359 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **40.8%**. Expected goals are 1.21 for Rayo Vallecano and 1.09 for Celta Vigo (2.30 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 40.6%; Under 3.5 goals: 79.8%; Double Chance 1X: 69.1%; Double Chance X2: 59.2%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 46.8%; BTTS No (at least one team does not score): 53.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 40.8% | 2.45 |
| Draw | 28.3% | 3.53 |
| Celta Vigo win | 30.9% | 3.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.21 |
| Celta Vigo expected goals | 1.09 |
| Expected total goals | 2.30 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 67.3% |
| Under 1.5 | 32.7% |
| Over 2.5 | 40.6% |
| Under 2.5 | 59.4% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.27% |
| 2 | 1-0 | 12.49% |
| 3 | 0-0 | 10.11% |
| 4 | 0-1 | 10.08% |
| 5 | 2-1 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 40.8% | 42.8% | 2.32 | -5.4% |
| Draw | 28.3% | 27.8% | 3.46 | -1.9% |
| Celta Vigo win | 30.9% | 29.3% | 3.03 | -6.4% |
| Over 2.5 | 40.6% | 46.4% | 2.11 | -14.2% |
| Under 2.5 | 59.4% | 53.6% | 1.84 | +9.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:15:00+00:00 |
| Fixture id | 77383723574e3d39c7aba22eec6c4ce3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Vallecano |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2149 |
| Dc lambda away | 1.0876 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.8% |
| P btts no | 53.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.89 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.46 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.82 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.1861131569077614, "-10": 6.848742518163489e-08, "-11": 6.704728551122659e-09, "-12": 6.025075451323678e-10, "-13": 4.985575268042358e-11, "-14": 3.5389584885391735e-12, "-2": 0.0856301053054746, "-3": 0.028130013145392443, "-4": 0.007192597559920622, "-5": 0.0015003719979184804, "-6": 0.00026384586506056004, "-7": 4.006421735742191e-05, "-8": 5.349773189636796e-06, "-9": 6.372230761640132e-07, "0": 0.2834624387302861, "1": 0.23022359240932824, "10": 2.2906647819871092e-07, "11": 2.5049839678368015e-08, "12": 2.514544306025079e-09, "13": 2.3242622623639617e-10, "14": 1.8429704565238373e-11, "2": 0.11813885778312175, "3": 0.04335201376428504, "4": 0.012382209661131037, "5": 0.0028852562700595907, "6": 0.0005667725222636503, "7": 9.61364783858824e-05, "8": 1.4339696750322019e-05, "9": 1.9079594628041484e-06} |
| Raw goal margin distribution | {"-1": 0.1953978683942205, "-10": 7.190408843009658e-08, "-11": 7.039210385865008e-09, "-12": 6.325651123560608e-10, "-13": 5.234292923080258e-11, "-14": 3.7155081160592e-12, "-2": 0.08990197321382713, "-3": 0.02953334787198951, "-4": 0.007551417937220275, "-5": 0.0015752217364027907, "-6": 0.00027700846342106506, "-7": 4.206291914334029e-05, "-8": 5.6166597516029055e-06, "-9": 6.690125128325289e-07, "0": 0.28861569773592693, "1": 0.2186111884795653, "10": 2.1751243873744544e-07, "11": 2.378633382444222e-08, "12": 2.3877115002501935e-09, "13": 2.2070272216506384e-10, "14": 1.7500116196478847e-11, "2": 0.11217997180613946, "3": 0.041165352137945456, "4": 0.011757654989634036, "5": 0.0027397248720904236, "6": 0.0005381846985921551, "7": 9.128738534672538e-05, "8": 1.361640705984153e-05, "9": 1.8117226013607612e-06} |
| Unadjusted home-win probability | 38.7% |
| Unadjusted draw probability | 28.9% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 67.3% |
| Raw p under 3 5 | 79.9% |
| Raw p btts yes | 46.9% |
| P home draw | 69.1% |
| P draw away | 59.2% |
| P home away | 71.7% |
| Raw p home draw | 67.6% |
| Raw p draw away | 61.3% |
| Raw p home away | 71.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.26 |
| Reference draw odds | 3.42 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:36Z |
| Market best over 2 5 last update utc | 2026-10-22T14:59:01Z |
| Market best under 2 5 last update utc | 2026-10-22T14:59:01Z |
| Home probability edge | -2.1% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | -0.0411 |
| Raw ev home | -0.1019 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | -0.0014 |
| Raw edge prob away | 0.0308 |
| Raw ev away | -0.0174 |

</details>


---

## 2026-10-31 — Real Betis vs Málaga

The model's most likely 1X2 outcome is **Real Betis win** at **73.9%**. Expected goals are 2.42 for Real Betis and 0.55 for Málaga (2.97 combined). The most likely exact score is 2-0 at 14.1%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.6%; Under 3.5 goals: 66.6%; Double Chance 1X: 90.3%; Double Chance X2: 26.1%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 39.6%; BTTS No (at least one team does not score): 60.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 73.9% | 1.35 |
| Draw | 16.5% | 6.07 |
| Málaga win | 9.7% | 10.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 2.42 |
| Málaga expected goals | 0.55 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 78.6% |
| Under 1.5 | 21.4% |
| Over 2.5 | 55.6% |
| Under 2.5 | 44.4% |
| Over 3.5 | 33.4% |
| Under 3.5 | 66.6% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.11% |
| 2 | 1-0 | 11.54% |
| 3 | 3-0 | 11.36% |
| 4 | 2-1 | 7.78% |
| 5 | 1-1 | 7.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 73.9% | 69.1% | 1.39 | +2.7% |
| Draw | 16.5% | 18.0% | 5.21 | -14.2% |
| Málaga win | 9.7% | 12.9% | 6.77 | -34.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:30:00+00:00 |
| Fixture id | 8f0b7ef29a47f675429758e83a426d7e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:31Z |
| Market best draw last update utc | 2026-10-22T15:05:31Z |
| Market best away last update utc | 2026-10-22T15:05:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Betis |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4155 |
| Dc lambda away | 0.5516 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 39.6% |
| P btts no | 60.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.14 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.67 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 2.99 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.80 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.07551148868839433, "-10": 6.241008076709659e-11, "-11": 3.0986153320231876e-12, "-12": 1.4123759052423632e-13, "-13": 5.949627745424409e-15, "-14": 2.3294902479155805e-16, "-15": 8.519364922441084e-18, "-16": 2.9226576656416626e-19, "-17": 9.41967901557783e-21, "-18": 2.6877010715917584e-22, "-2": 0.01786010361604716, "-3": 0.0029735801112365182, "-4": 0.00038544490803543073, "-5": 4.076676976704683e-05, "-6": 3.635192487990502e-06, "-7": 2.799167758317682e-07, "-8": 1.8954842070567472e-08, "-9": 1.1449888283428898e-09, "0": 0.1647084867765222, "1": 0.2125365965746177, "10": 0.00010165407951218751, "11": 2.2101140696718023e-05, "12": 4.411378073633917e-06, "13": 8.137494918026363e-07, "14": 1.395207459691909e-07, "15": 2.2344059064522563e-08, "16": 3.356678559544843e-09, "17": 4.737452472867721e-10, "18": 5.919250000143463e-11, "2": 0.2151485338069047, "3": 0.15685956862855094, "4": 0.0890370253417724, "5": 0.04123742953014808, "6": 0.016102364538497897, "7": 0.005429603618479092, "8": 0.0016100387368274912, "9": 0.00042588697725255443} |
| Raw goal margin distribution | {"-1": 0.05047156437240715, "-10": 4.171463791320764e-11, "-11": 2.0711015755616084e-12, "-12": 9.440261694964148e-14, "-13": 3.976706392112224e-15, "-14": 1.5570215743956875e-16, "-15": 5.694308012776589e-18, "-16": 1.9534922045923584e-19, "-17": 6.29607420089467e-21, "-18": 1.7964481962263323e-22, "-2": 0.011937618831420681, "-3": 0.0019875285550270197, "-4": 0.00025762977032813775, "-5": 2.7248339031472978e-05, "-6": 2.42974751061824e-06, "-7": 1.8709520651366947e-07, "-8": 1.2669337452494079e-08, "-9": 7.653057615360862e-10, "0": 0.14954974469649948, "1": 0.2261345657639075, "10": 0.00010815784904388342, "11": 2.3515158965033615e-05, "12": 4.693615505183842e-06, "13": 8.658127161869022e-07, "14": 1.4844720303838423e-07, "15": 2.3773619110273922e-08, "16": 3.5714369228887092e-09, "17": 5.040551956909584e-10, "18": 6.297960210163204e-11, "2": 0.22891361323782544, "3": 0.16689535359750562, "4": 0.0947335630054795, "5": 0.04387577655006751, "6": 0.017132584558946635, "7": 0.005776986534664136, "8": 0.0017130480890510127, "9": 0.0004531349810699432} |
| Unadjusted home-win probability | 78.6% |
| Unadjusted draw probability | 15.0% |
| Unadjusted away-win probability | 6.5% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.5% |
| Raw p btts yes | 38.8% |
| P home draw | 90.3% |
| P draw away | 26.1% |
| P home away | 83.5% |
| Raw p home draw | 93.5% |
| Raw p draw away | 21.4% |
| Raw p home away | 85.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:31Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:31Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.42 |
| Reference draw odds | 5.10 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:32Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:32Z |
| Home probability edge | +4.7% |
| Draw probability edge | -1.5% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | 0.0945 |
| Raw ev home | 0.0922 |
| Raw edge prob draw | -0.0303 |
| Raw ev draw | -0.2208 |
| Raw edge prob away | -0.0642 |
| Raw ev away | -0.5621 |

</details>


---

## 2026-11-01 — Getafe vs Sevilla

The model's most likely 1X2 outcome is **Getafe win** at **36.2%**. Expected goals are 1.05 for Getafe and 0.90 for Sevilla (1.95 combined). The most likely exact score is 0-0 at 14.4%. Goal-market probabilities: at least one goal: 85.6%; Over 2.5 goals: 31.0%; Under 3.5 goals: 86.6%; Double Chance 1X: 67.8%; Double Chance X2: 63.8%; Double Chance 12 (either team wins): 68.4%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.8%; BTTS No (at least one team does not score): 61.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 36.2% | 2.76 |
| Draw | 31.6% | 3.16 |
| Sevilla win | 32.2% | 3.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 1.05 |
| Sevilla expected goals | 0.90 |
| Expected total goals | 1.95 |
| Over 0.5 | 85.6% |
| Under 0.5 | 14.4% |
| Over 1.5 | 58.3% |
| Under 1.5 | 41.7% |
| Over 2.5 | 31.0% |
| Under 2.5 | 69.0% |
| Over 3.5 | 13.4% |
| Under 3.5 | 86.6% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 14.45% |
| 2 | 1-0 | 13.89% |
| 3 | 1-1 | 13.66% |
| 4 | 0-1 | 13.40% |
| 5 | 2-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 36.2% | 34.1% | 2.97 | +7.4% |
| Draw | 31.6% | 31.4% | 3.00 | -5.2% |
| Sevilla win | 32.2% | 34.5% | 2.63 | -15.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:00:00+00:00 |
| Fixture id | ddcc9a51a2d7368e055d1abefacdb74e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:05:30Z |
| Market best draw last update utc | 2026-10-22T15:05:30Z |
| Market best away last update utc | 2026-10-22T15:05:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Getafe |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0536 |
| Dc lambda away | 0.8963 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:05:32.065784+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 38.8% |
| P btts no | 61.2% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.92 |
| Fair Over 1.5 odds | 1.72 |
| Fair Under 1.5 odds | 2.40 |
| Fair Over 2.5 odds | 3.23 |
| Fair Under 2.5 odds | 1.45 |
| Fair Over 3.5 odds | 7.48 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.74 |
| Fair Under 4.5 odds | 1.05 |
| Goal margin distribution | {"-1": 0.20975148910715477, "-10": 1.5369170616525336e-08, "-11": 1.243385099066695e-09, "-12": 9.210477672711617e-11, "-13": 5.920188899036246e-12, "-2": 0.08324556773597695, "-3": 0.02313036715021264, "-4": 0.004955899676076308, "-5": 0.0008618477514767732, "-6": 0.00012595928079398697, "-7": 1.5864009927187042e-05, "-8": 1.754578631602869e-06, "-9": 1.7293635846684272e-07, "0": 0.31613873300815526, "1": 0.21725567516415564, "10": 6.80638453608672e-08, "11": 6.472802538038331e-09, "12": 5.636240346947725e-10, "13": 4.2585677903685414e-11, "2": 0.1011257990988258, "3": 0.03302965395207636, "4": 0.008318876057602722, "5": 0.001700565447987065, "6": 0.00029215519993416856, "7": 4.32530832985153e-05, "8": 5.623381980750879e-06, "9": 6.515259364340115e-07} |
| Raw goal margin distribution | {"-1": 0.19504178035654074, "-10": 1.4291342637949748e-08, "-11": 1.1561874693860738e-09, "-12": 8.564554039004264e-11, "-13": 5.5050106572791475e-12, "-2": 0.07740762083324877, "-3": 0.0215082524967115, "-4": 0.004608346287336823, "-5": 0.0008014070391578325, "-6": 0.00011712585442450924, "-7": 1.4751479252725141e-05, "-8": 1.6315313971789739e-06, "-9": 1.6080846618694818e-07, "0": 0.3178518324300931, "1": 0.22979161825511668, "10": 7.199122029066412e-08, "11": 6.8462919034809896e-09, "12": 5.961458954852576e-10, "13": 4.504292848775981e-11, "2": 0.10696089298796345, "3": 0.03493550917056264, "4": 0.00879888633471088, "5": 0.0017986903492689889, "6": 0.000309012945801271, "7": 4.574884406669359e-05, "8": 5.947858643724881e-06, "9": 6.891198545457046e-07} |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 31.8% |
| Unadjusted away-win probability | 30.0% |
| Raw p over 1 5 | 58.3% |
| Raw p under 3 5 | 86.6% |
| Raw p btts yes | 38.8% |
| P home draw | 67.8% |
| P draw away | 63.8% |
| P home away | 68.4% |
| Raw p home draw | 70.0% |
| Raw p draw away | 61.7% |
| Raw p home away | 68.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:01Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:05:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.83 |
| Reference draw odds | 3.06 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-10-22T15:05:36Z |
| Market reference home last update utc | 2026-10-22T15:05:36Z |
| Market reference draw last update utc | 2026-10-22T15:05:36Z |
| Market reference away last update utc | 2026-10-22T15:05:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.72 |
| Reference Under 2.5 odds | 1.47 |
| Market reference over 2 5 last update utc | 2026-10-22T15:05:32Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:05:32Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.2% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | 0.0417 |
| Raw ev home | 0.1365 |
| Raw edge prob draw | 0.0034 |
| Raw ev draw | -0.0464 |
| Raw edge prob away | -0.0452 |
| Raw ev away | -0.2123 |
| Market p over 1 5 | 61.2% |
| Market over 1 5 odds | 1.63 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T14:59:01Z |
| Market reference over 1 5 odds | 1.58 |
| Market reference over 1 5 opposite odds | 2.41 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:36Z |
| Market over 1 5 bookmakers | 1 |

</details>


---
