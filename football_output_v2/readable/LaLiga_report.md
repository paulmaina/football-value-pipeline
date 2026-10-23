# La Liga — football model report

Fixtures in this report: **19**.

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
| Training sha256 | 4972947ab4b48973d535eea5e43b21c734ac5552b9636820b9db06ffb0d0407d |
| Training as of utc | 2026-10-23T16:20:51.645253+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 89, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 89, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 43, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-23T16:20:51.645253+00:00', 'observations': 199, 'observations_sha256': '87d09381dff61c3e75741469708ebd3588bcddcf650fa5b2071c4e6ea565bddf', 'eligible_training_matches': 92, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 113, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 10, 'retrospective_eligible_training_matches': 92, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '7b4484ef5cfeae70288d3a8f98146b7a8cdb760229ee0be6fb0fa002df12e2a8', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2502.986 |
| Base scoring parameter | 0.095 |
| Home-advantage parameter | 0.284 |
| Dixon-Coles low-score adjustment | -0.022 |
| Xi per day | 0.0009 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1989, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-21'} |
| Training data health | {'training_end': '2026-10-21', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 19.00 |
| Additional event odds calls used before this league | 9.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261023T162051645253Z_7ebda34db65d8e576f64369398e9b384cd6cb814d80b7b78d1ac5ed8f7dec0d6.json |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
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

The model's most likely 1X2 outcome is **Alavés win** at **62.9%**. Expected goals are 1.75 for Alavés and 0.59 for Málaga (2.34 combined). The most likely exact score is 1-0 at 16.0%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 41.1%; Under 3.5 goals: 79.5%; Double Chance 1X: 86.0%; Double Chance X2: 37.1%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 37.3%; BTTS No (at least one team does not score): 62.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 62.9% | 1.59 |
| Draw | 23.1% | 4.32 |
| Málaga win | 14.0% | 7.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.75 |
| Málaga expected goals | 0.59 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 67.5% |
| Under 1.5 | 32.5% |
| Over 2.5 | 41.1% |
| Under 2.5 | 58.9% |
| Over 3.5 | 20.5% |
| Under 3.5 | 79.5% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.02% |
| 2 | 2-0 | 14.18% |
| 3 | 1-1 | 10.28% |
| 4 | 0-0 | 9.95% |
| 5 | 2-1 | 8.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 62.9% | 60.5% | 1.62 | +1.8% |
| Draw | 23.1% | 23.3% | 3.83 | -11.4% |
| Málaga win | 14.0% | 16.2% | 6.36 | -11.0% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7472 |
| Dc lambda away | 0.5919 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 37.3% |
| P btts no | 62.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.05 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.08 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.87 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.50 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.10632185198618987, "-10": 1.8208917348836433e-10, "-11": 9.722325707371303e-12, "-12": 4.764104829790597e-13, "-13": 2.1569231758875948e-14, "-14": 9.0742318134445e-16, "-15": 3.5588194665682573e-17, "-16": 1.2366062810514972e-18, "-2": 0.027808009326808422, "-3": 0.005070349040567477, "-4": 0.0007145368638623209, "-5": 8.183211159866732e-05, "-6": 7.882084861366872e-06, "-7": 6.545642029015102e-07, "-8": 4.775115139483858e-08, "-9": 3.1050667596039446e-09, "0": 0.23142992650008026, "1": 0.2599932943998585, "10": 7.454920559746977e-06, "11": 1.1749475810953853e-06, "12": 1.6994917642522683e-07, "13": 2.2712339012511495e-08, "14": 2.8205024721801437e-09, "15": 3.265216650192287e-10, "16": 3.3490908055079914e-11, "2": 0.19752103668597712, "3": 0.10630917376215722, "4": 0.04422287315772223, "5": 0.01494980416097707, "6": 0.004250522132769155, "7": 0.0010419403487673714, "8": 0.00022436953267434737, "9": 4.306658222567716e-05} |
| Raw goal margin distribution | {"-1": 0.0899208852548148, "-10": 1.5400051230783717e-10, "-11": 8.222581887080243e-12, "-12": 4.0292048693541666e-13, "-13": 1.824201119329934e-14, "-14": 7.674461481147999e-16, "-15": 3.0098440811344386e-17, "-16": 1.0458502126003061e-18, "-2": 0.0235184091428877, "-3": 0.004288208545670829, "-4": 0.0006043140346543685, "-5": 6.920887644224582e-05, "-6": 6.66621240269352e-06, "-7": 5.535926197811265e-07, "-8": 4.0385167537509537e-08, "-9": 2.6260862332905236e-09, "0": 0.22947763445286512, "1": 0.26973393739176277, "10": 7.734218992705107e-06, "11": 1.2189669660878692e-06, "12": 1.7631631853997815e-07, "13": 2.3563256288446025e-08, "14": 2.9261725345665874e-09, "15": 3.387547919366596e-10, "16": 3.474564418045669e-11, "2": 0.20492115793214247, "3": 0.1102920445926214, "4": 0.04587968211696849, "5": 0.015509898241353634, "6": 0.004409767849932983, "7": 0.001080976620759041, "8": 0.00023277553222555115, "9": 4.468007077087264e-05} |
| Unadjusted home-win probability | 65.2% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 11.8% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 37.1% |
| P home draw | 86.0% |
| P draw away | 37.1% |
| P home away | 76.9% |
| Raw p home draw | 88.2% |
| Raw p draw away | 34.8% |
| Raw p home away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 5.55, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.79, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 5.55, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.60 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.50 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:44Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:44Z |
| Home probability edge | +2.4% |
| Draw probability edge | -0.2% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | 0.0471 |
| Raw ev home | 0.0564 |
| Raw edge prob draw | -0.0039 |
| Raw ev draw | -0.1211 |
| Raw edge prob away | -0.0432 |
| Raw ev away | -0.2469 |
| Market p home draw | 83.5% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:20:39Z |
| Market reference home draw last update utc | 2026-10-23T16:20:43Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.9% |
| Market draw away odds | 2.42 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:20:39Z |
| Market reference draw away last update utc | 2026-10-23T16:20:43Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:20:39Z |
| Market reference home away last update utc | 2026-10-23T16:20:43Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.16 |
| Market reference dc draw away odds | 2.31 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 71.9% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference over 1 5 odds | 1.37 |
| Market reference over 1 5 opposite odds | 3.35 |
| Market reference over 1 5 last update utc | 2026-10-23T16:20:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.8% |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.85 |
| Market reference under 3 5 last update utc | 2026-10-23T16:20:44Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 46.5% |
| Market btts yes odds | 2.08 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:20:39Z |
| Market reference btts yes odds | 1.98 |
| Market reference btts yes opposite odds | 1.75 |
| Market reference btts yes last update utc | 2026-10-23T16:20:43Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,466.1423 |
| Elo away rating | 1,401.2778 |
| Elo rating diff | 124.8645 |
| Elo home expectancy | 0.6723 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **73.1%**. Expected goals are 2.24 for Atlético Madrid and 0.88 for Deportivo La Coruña (3.11 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 61.5%; Under 3.5 goals: 61.4%; Double Chance 1X: 89.1%; Double Chance X2: 26.9%; Double Chance 12 (either team wins): 84.0%; Under 4.5 goals: 78.9%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 73.1% | 1.37 |
| Draw | 16.0% | 6.25 |
| Deportivo La Coruña win | 10.9% | 9.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.24 |
| Deportivo La Coruña expected goals | 0.88 |
| Expected total goals | 3.11 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 82.5% |
| Under 1.5 | 17.5% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 38.6% |
| Under 3.5 | 61.4% |
| Over 4.5 | 21.1% |
| Under 4.5 | 78.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.96% |
| 2 | 1-0 | 10.49% |
| 3 | 2-1 | 10.47% |
| 4 | 3-0 | 8.92% |
| 5 | 3-1 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 73.1% | 78.1% | 1.28 | -6.5% |
| Draw | 16.0% | 13.1% | 6.00 | -4.0% |
| Deportivo La Coruña win | 10.9% | 8.8% | 10.34 | +13.0% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2366 |
| Dc lambda away | 0.8751 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.38 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.71 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.59 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.73 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.07500156963656542, "-10": 3.2181028240185493e-09, "-11": 2.5231277316366487e-10, "-12": 1.8173820151498238e-11, "-13": 1.2104477382987653e-12, "-14": 7.496603142035838e-14, "-15": 4.337302962478606e-15, "-16": 2.342267140490825e-16, "-17": 1.0812059479259201e-17, "-2": 0.02610969308762349, "-3": 0.006626385033842099, "-4": 0.0013273839612454896, "-5": 0.00021866226894745757, "-6": 3.0515834787087057e-05, "-7": 3.6892197138740097e-06, "-8": 3.9308225143149794e-07, "-9": 3.741996173153739e-08, "0": 0.1599967270037681, "1": 0.249833265611263, "10": 4.925399348184195e-05, "11": 9.870173130635039e-06, "12": 1.8170871667007338e-06, "13": 3.093282467605586e-07, "14": 4.896458284876753e-08, "15": 7.240712416551995e-09, "16": 9.994060338586022e-10, "17": 1.1791199002312914e-10, "2": 0.21942761697334534, "3": 0.1423345028524188, "4": 0.07287424840022876, "5": 0.030682827231294812, "6": 0.01094437035132127, "7": 0.003381769852267605, "8": 0.0009209519332776805, "9": 0.00022407885135802122} |
| Raw goal margin distribution | {"-1": 0.08984471571507038, "-10": 3.854979765981496e-09, "-11": 3.0224659945141647e-10, "-12": 2.1770500442595127e-11, "-13": 1.4500007594825404e-12, "-14": 8.980214432692988e-14, "-15": 5.195674617508816e-15, "-16": 2.8058122834745753e-16, "-17": 1.2951814407559896e-17, "-2": 0.031276918126279016, "-3": 0.007937776268803475, "-4": 0.001590079183952213, "-5": 0.0002619365099476368, "-6": 3.6555054974706026e-05, "-7": 4.41933279542791e-06, "-8": 4.708749870654041e-07, "-9": 4.4825539520438585e-08, "0": 0.18866819679341224, "1": 0.23263279278099178, "10": 4.586296397024362e-05, "11": 9.19063334097499e-06, "12": 1.6919846974014595e-06, "13": 2.880316748608053e-07, "14": 4.559347862501591e-08, "15": 6.742205234620113e-09, "16": 9.305991186156106e-10, "17": 1.097940079129653e-10, "2": 0.2043205064181246, "3": 0.1325350842556472, "4": 0.06785701610104825, "5": 0.028570381817524425, "6": 0.010190874437109275, "7": 0.003148942409053266, "8": 0.0008575464109283208, "9": 0.0002086515135085484} |
| Unadjusted home-win probability | 68.0% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 13.1% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 52.3% |
| P home draw | 89.1% |
| P draw away | 26.9% |
| P home away | 84.0% |
| Raw p home draw | 86.9% |
| Raw p draw away | 32.0% |
| Raw p home away | 81.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:39Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 8.45, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:39Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.09, "price": 8.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.52, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.25 |
| Reference draw odds | 6.25 |
| Reference away odds | 9.00 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | -5.0% |
| Draw probability edge | +2.9% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | -0.1006 |
| Raw ev home | -0.1291 |
| Raw edge prob draw | 0.0573 |
| Raw ev draw | 0.1320 |
| Raw edge prob away | 0.0433 |
| Raw ev away | 0.3541 |
| Market p home draw | 89.5% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:20:39Z |
| Market reference home draw last update utc | 2026-10-23T16:20:43Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 27.2% |
| Market draw away odds | 3.91 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:20:39Z |
| Market reference draw away last update utc | 2026-10-23T16:20:43Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.3% |
| Market home away odds | 1.15 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:20:39Z |
| Market reference home away last update utc | 2026-10-23T16:20:43Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.08 |
| Market reference dc draw away odds | 3.56 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 83.1% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-23T16:20:44Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.7% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market reference under 3 5 last update utc | 2026-10-23T16:20:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 43.2% |
| Market btts yes odds | 2.05 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:20:39Z |
| Market reference btts yes odds | 2.12 |
| Market reference btts yes opposite odds | 1.66 |
| Market reference btts yes last update utc | 2026-10-23T16:20:43Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,646.3999 |
| Elo away rating | 1,445.4329 |
| Elo rating diff | 260.9670 |
| Elo home expectancy | 0.8179 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **50.7%**. Expected goals are 1.40 for Rayo Vallecano and 0.97 for Elche CF (2.37 combined). The most likely exact score is 1-0 at 13.9%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 43.1%; Under 3.5 goals: 78.2%; Double Chance 1X: 76.4%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 90.5%; BTTS Yes (both teams score): 46.6%; BTTS No (at least one team does not score): 53.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 50.7% | 1.97 |
| Draw | 25.6% | 3.90 |
| Elche CF win | 23.6% | 4.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.40 |
| Elche CF expected goals | 0.97 |
| Expected total goals | 2.37 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 69.1% |
| Under 1.5 | 30.9% |
| Over 2.5 | 43.1% |
| Under 2.5 | 56.9% |
| Over 3.5 | 21.8% |
| Under 3.5 | 78.2% |
| Over 4.5 | 9.5% |
| Under 4.5 | 90.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.89% |
| 2 | 1-1 | 12.05% |
| 3 | 2-0 | 9.97% |
| 4 | 2-1 | 9.66% |
| 5 | 0-0 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 50.7% | 54.7% | 1.78 | -9.7% |
| Draw | 25.6% | 23.7% | 3.88 | -0.5% |
| Elche CF win | 23.6% | 21.6% | 4.63 | +9.5% |
| Over 2.5 | 43.1% | 50.9% | 1.89 | -18.6% |
| Under 2.5 | 56.9% | 49.1% | 2.00 | +13.8% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
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
| Dc lambda away | 0.9691 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.6% |
| P btts no | 53.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.21 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.24 |
| Fair Over 2.5 odds | 2.32 |
| Fair Under 2.5 odds | 1.76 |
| Fair Over 3.5 odds | 4.59 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.53 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.15145096223555338, "-10": 1.952329772450582e-08, "-11": 1.7025667282144297e-09, "-12": 1.362951679791988e-10, "-13": 1.0045082086872472e-11, "-14": 6.337197933996874e-13, "-2": 0.06193780956687051, "-3": 0.018082389538221964, "-4": 0.004112768198266357, "-5": 0.0007635487893658098, "-6": 0.00011954069585113067, "-7": 1.6163665904387073e-05, "-8": 1.922197644148132e-06, "-9": 2.0392840880829566e-07, "0": 0.2564432106502704, "1": 0.2601035100849652, "10": 9.402029251079974e-07, "11": 1.1882088929944283e-07, "12": 1.3784447103454045e-08, "13": 1.472253575041879e-09, "14": 1.3460048817368097e-10, "2": 0.15334244327467142, "3": 0.06487578003771421, "4": 0.021383620592463466, "5": 0.005753127990264161, "6": 0.0013052787211183347, "7": 0.0002557688079157633, "8": 4.40784171164906e-05, "9": 6.7768194600125945e-06} |
| Raw goal margin distribution | {"-1": 0.16453393248354461, "-10": 2.1209802184445288e-08, "-11": 1.8496415933830325e-09, "-12": 1.4806891706138342e-10, "-13": 1.0912818469271839e-11, "-14": 6.884631709274991e-13, "-2": 0.06728825771079709, "-3": 0.019644422296872938, "-4": 0.004468046389837805, "-5": 0.0008295073408778552, "-6": 0.00012986712325812255, "-7": 1.75599512564515e-05, "-8": 2.088245150337203e-06, "-9": 2.2154460130900468e-07, "0": 0.27579601440980545, "1": 0.23969754647394848, "10": 8.664409575341722e-07, "11": 1.094990053214794e-07, "12": 1.2703012539579132e-08, "13": 1.356750509094479e-09, "14": 1.2404064350722489e-10, "2": 0.1413122314698972, "3": 0.0597860647691526, "4": 0.01970600623216875, "5": 0.0053017764480242915, "6": 0.001202875373786826, "7": 0.000235702915742846, "8": 4.062032239329171e-05, "9": 6.245156003205439e-06} |
| Unadjusted home-win probability | 46.7% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 68.9% |
| Raw p under 3 5 | 78.4% |
| Raw p btts yes | 47.1% |
| P home draw | 76.4% |
| P draw away | 49.3% |
| P home away | 74.4% |
| Raw p home draw | 74.3% |
| Raw p draw away | 53.3% |
| Raw p home away | 72.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.04, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.13, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.44, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.04, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.85 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:44Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:44Z |
| Market best over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market best under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | -4.0% |
| Draw probability edge | +1.9% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.0796 |
| Raw ev home | -0.1682 |
| Raw edge prob draw | 0.0387 |
| Raw ev draw | 0.0701 |
| Raw edge prob away | 0.0409 |
| Raw ev away | 0.1895 |
| Market p home draw | 78.9% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:20:39Z |
| Market reference home draw last update utc | 2026-10-23T16:20:43Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.0% |
| Market draw away odds | 2.12 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:20:39Z |
| Market reference draw away last update utc | 2026-10-23T16:20:43Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:20:39Z |
| Market reference home away last update utc | 2026-10-23T16:20:43Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.23 |
| Market reference dc draw away odds | 2.11 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 76.4% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-10-23T16:20:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.2% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.25 |
| Market reference under 3 5 last update utc | 2026-10-23T16:20:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.3% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:20:39Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.02 |
| Market reference btts yes last update utc | 2026-10-23T16:20:43Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,498.4715 |
| Elo away rating | 1,425.5500 |
| Elo rating diff | 132.9215 |
| Elo home expectancy | 0.6825 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **38.4%**. Expected goals are 1.84 for Real Racing Club de Santander and 2.02 for Espanyol (3.86 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 73.5%; Under 3.5 goals: 46.3%; Double Chance 1X: 61.7%; Double Chance X2: 61.6%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 66.1%; BTTS Yes (both teams score): 73.5%; BTTS No (at least one team does not score): 26.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 38.4% | 2.60 |
| Draw | 23.2% | 4.31 |
| Espanyol win | 38.3% | 2.61 |

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
| Over 2.5 | 73.5% |
| Under 2.5 | 26.5% |
| Over 3.5 | 53.7% |
| Under 3.5 | 46.3% |
| Over 4.5 | 33.9% |
| Under 4.5 | 66.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.69% |
| 2 | 2-2 | 7.90% |
| 3 | 2-1 | 7.74% |
| 4 | 1-2 | 7.09% |
| 5 | 3-2 | 4.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 38.4% | 41.0% | 2.42 | -7.0% |
| Draw | 23.2% | 25.1% | 3.72 | -13.6% |
| Espanyol win | 38.3% | 33.9% | 2.85 | +9.3% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santander |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8413 |
| Dc lambda away | 2.0177 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 73.5% |
| P btts no | 26.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.36 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.89 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.77 |
| Fair Over 3.5 odds | 1.86 |
| Fair Under 3.5 odds | 2.16 |
| Fair Over 4.5 odds | 2.95 |
| Fair Under 4.5 odds | 1.51 |
| Goal margin distribution | {"-1": 0.16777137311122567, "-10": 8.130387511037895e-06, "-11": 1.4514365305807746e-06, "-12": 2.384825312806227e-07, "-13": 3.628665019080182e-08, "-14": 5.1397607400016155e-09, "-15": 6.800431136234212e-10, "-16": 8.309716061603698e-11, "-17": 8.093915053099028e-12, "-2": 0.11469791781952704, "-3": 0.060964992828315634, "-4": 0.026358627721081176, "-5": 0.009545571485408175, "-6": 0.0029635007725275714, "-7": 0.0008034369347038734, "-8": 0.0001930605509468082, "-9": 4.161926640217486e-05, "0": 0.23217139194851336, "1": 0.18299580607692456, "10": 3.895778535071327e-06, "11": 6.346654825868003e-07, "12": 9.516280111750463e-08, "13": 1.321360551605533e-08, "14": 1.7079736898637314e-09, "15": 2.062236814625173e-10, "16": 2.2995988750045645e-11, "17": 2.044035150180425e-12, "2": 0.11426889596670593, "3": 0.05542642137698027, "4": 0.02186869779735517, "5": 0.007227130150712488, "6": 0.0020475419151942506, "7": 0.0005065745456915125, "8": 0.00011108333932107755, "9": 2.1853128583537537e-05} |
| Raw goal margin distribution | {"-1": 0.18715492960937008, "-10": 9.06973623751897e-06, "-11": 1.619129036592104e-06, "-12": 2.6603573975221223e-07, "-13": 4.047904798226239e-08, "-14": 5.733585782040923e-09, "-15": 7.58612263232483e-10, "-16": 9.269783609342304e-11, "-17": 9.02904991438979e-12, "-2": 0.12794960390306645, "-3": 0.06800861630818784, "-4": 0.029403986057073405, "-5": 0.010648424259175608, "-6": 0.0033058904400336026, "-7": 0.0008962624562915396, "-8": 0.00021536590630894984, "-9": 4.642777089705703e-05, "0": 0.2138416550128575, "1": 0.17063954341970838, "10": 3.632727354469673e-06, "11": 5.918115310650102e-07, "12": 8.873720814347753e-08, "13": 1.2321395011861653e-08, "14": 1.5926477052086535e-09, "15": 1.9229902368529038e-10, "16": 2.14432511045801e-11, "17": 1.9060175871681077e-12, "2": 0.10655321918490467, "3": 0.051683912543768966, "4": 0.02039207721381121, "5": 0.0067391390851546705, "6": 0.0019092875680144883, "7": 0.0004723695642976051, "8": 0.00010358275804046105, "9": 2.0377559266136885e-05} |
| Unadjusted home-win probability | 35.9% |
| Unadjusted draw probability | 21.4% |
| Unadjusted away-win probability | 42.8% |
| Raw p over 1 5 | 89.9% |
| Raw p under 3 5 | 46.1% |
| Raw p btts yes | 73.1% |
| P home draw | 61.7% |
| P draw away | 61.6% |
| P home away | 76.8% |
| Raw p home draw | 57.2% |
| Raw p draw away | 64.1% |
| Raw p home away | 78.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.24, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.75 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | -2.6% |
| Draw probability edge | -1.8% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | +16.5% |
| Under 2.5 probability edge | -16.5% |
| Raw edge prob home | -0.0519 |
| Raw ev home | -0.1324 |
| Raw edge prob draw | -0.0367 |
| Raw ev draw | -0.2045 |
| Raw edge prob away | 0.0886 |
| Raw ev away | 0.2188 |
| Market p home draw | 66.5% |
| Market home draw odds | 1.46 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:20:39Z |
| Market reference home draw last update utc | 2026-10-23T16:20:43Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.9% |
| Market draw away odds | 1.61 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:20:39Z |
| Market reference draw away last update utc | 2026-10-23T16:20:43Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:20:39Z |
| Market reference home away last update utc | 2026-10-23T16:20:43Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.46 |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-23T16:20:44Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.0% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.73 |
| Market reference under 3 5 last update utc | 2026-10-23T16:20:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:20:39Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.36 |
| Market reference btts yes last update utc | 2026-10-23T16:20:43Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,429.4672 |
| Elo away rating | 1,440.6093 |
| Elo rating diff | 48.8579 |
| Elo home expectancy | 0.5699 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.3%**. Expected goals are 1.26 for Valencia and 1.54 for Villarreal (2.80 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.2%; Under 3.5 goals: 69.2%; Double Chance 1X: 55.7%; Double Chance X2: 69.6%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 84.7%; BTTS Yes (both teams score): 56.5%; BTTS No (at least one team does not score): 43.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.4% | 3.29 |
| Draw | 25.3% | 3.96 |
| Villarreal win | 44.3% | 2.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.26 |
| Villarreal expected goals | 1.54 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 30.8% |
| Under 3.5 | 69.2% |
| Over 4.5 | 15.3% |
| Under 4.5 | 84.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.94% |
| 2 | 0-1 | 9.27% |
| 3 | 1-2 | 9.26% |
| 4 | 0-2 | 7.33% |
| 5 | 2-1 | 7.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.4% | 29.8% | 3.22 | -2.1% |
| Draw | 25.3% | 25.0% | 3.68 | -7.0% |
| Villarreal win | 44.3% | 45.2% | 2.22 | -1.6% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2622 |
| Dc lambda away | 1.5379 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.93 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.24 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.54 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.22056555266382627, "-10": 1.5069464451097754e-06, "-11": 2.0766869171747142e-07, "-12": 2.6290539025028522e-08, "-13": 3.0766903848714694e-09, "-14": 3.326111722258354e-10, "-15": 3.0194127742088064e-11, "-2": 0.13391772455067377, "-3": 0.05978905614581026, "-4": 0.02106240499975499, "-5": 0.006100546967776881, "-6": 0.001496759108146639, "-7": 0.0003180962807754988, "-8": 5.957734146536316e-05, "-9": 9.969135492135878e-06, "0": 0.2527137374496558, "1": 0.17356551249682545, "10": 2.00936953442176e-07, "11": 2.272704715128572e-08, "12": 2.361464751829901e-09, "13": 2.268170838614333e-10, "14": 2.012513452864808e-11, "15": 1.4994584586412332e-12, "2": 0.0867201714375891, "3": 0.0317770629948742, "4": 0.009187767736403733, "5": 0.002184141720535535, "6": 0.0004398189528905022, "7": 7.671682362097042e-05, "8": 1.1792968336544424e-05, "9": 1.6196064680385386e-06} |
| Raw goal margin distribution | {"-1": 0.21626013356437, "-10": 1.477530990482905e-06, "-11": 2.0361501814568644e-07, "-12": 2.5777350145412858e-08, "-13": 3.0166336743554415e-09, "-14": 3.2611863304055164e-10, "-15": 2.960474117332342e-11, "-2": 0.13130366300718802, "-3": 0.0586219793237057, "-4": 0.020651268810666375, "-5": 0.005981464857651422, "-6": 0.0014675425093909778, "-7": 0.0003118870709230237, "-8": 5.841439729415456e-05, "-9": 9.774538893371755e-06, "0": 0.2553047927583373, "1": 0.17702725340359812, "10": 2.0494461407363807e-07, "11": 2.3180335063624854e-08, "12": 2.4085638501110815e-09, "13": 2.3134092022882443e-10, "14": 2.052652764211813e-11, "15": 1.5293649568251952e-12, "2": 0.0884497936453035, "3": 0.032410852261439825, "4": 0.009371016533687798, "5": 0.0022277041347006474, "6": 0.00044859108301527475, "7": 7.824693039590497e-05, "8": 1.2028177510968622e-05, "9": 1.6519093021824199e-06} |
| Unadjusted home-win probability | 31.0% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 43.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 56.6% |
| P home draw | 55.7% |
| P draw away | 69.6% |
| P home away | 74.7% |
| Raw p home draw | 56.5% |
| Raw p draw away | 69.0% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.07, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.07, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.10 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:44Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:44Z |
| Home probability edge | +0.6% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | 0.0121 |
| Raw ev home | -0.0017 |
| Raw edge prob draw | 0.0052 |
| Raw ev draw | -0.0605 |
| Raw edge prob away | -0.0173 |
| Raw ev away | -0.0350 |
| Market p home draw | 56.3% |
| Market home draw odds | 1.71 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:20:40Z |
| Market reference home draw last update utc | 2026-10-23T16:20:43Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.2% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:20:40Z |
| Market reference draw away last update utc | 2026-10-23T16:20:43Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.4% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:20:40Z |
| Market reference home away last update utc | 2026-10-23T16:20:43Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.72 |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 78.2% |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-23T16:20:44Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 68.1% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-10-23T16:20:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.9% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:20:40Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-23T16:20:43Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,465.9892 |
| Elo away rating | 1,546.8125 |
| Elo rating diff | -20.8233 |
| Elo home expectancy | 0.4701 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **55.9%**. Expected goals are 1.20 for Athletic Bilbao and 0.62 for Getafe (1.82 combined). The most likely exact score is 1-0 at 21.5%. Goal-market probabilities: at least one goal: 86.0%; Over 2.5 goals: 29.0%; Under 3.5 goals: 88.4%; Double Chance 1X: 82.6%; Double Chance X2: 44.1%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 95.9%; BTTS Yes (both teams score): 31.6%; BTTS No (at least one team does not score): 68.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 55.9% | 1.79 |
| Draw | 26.7% | 3.75 |
| Getafe win | 17.4% | 5.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.20 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.82 |
| Over 0.5 | 86.0% |
| Under 0.5 | 14.0% |
| Over 1.5 | 55.5% |
| Under 1.5 | 44.5% |
| Over 2.5 | 29.0% |
| Under 2.5 | 71.0% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.1% |
| Under 4.5 | 95.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.50% |
| 2 | 0-0 | 14.04% |
| 3 | 2-0 | 13.04% |
| 4 | 1-1 | 10.54% |
| 5 | 0-1 | 9.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 55.9% | 62.1% | 1.59 | -11.1% |
| Draw | 26.7% | 22.1% | 4.15 | +10.7% |
| Getafe win | 17.4% | 15.8% | 5.92 | +3.2% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1965 |
| Dc lambda away | 0.6241 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 31.6% |
| P btts no | 68.4% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.12 |
| Fair Over 1.5 odds | 1.80 |
| Fair Under 1.5 odds | 2.25 |
| Fair Over 2.5 odds | 3.45 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.62 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.65 |
| Fair Under 4.5 odds | 1.04 |
| Goal margin distribution | {"-1": 0.12911188441538404, "-10": 3.916355281775215e-10, "-11": 2.209488141266272e-11, "-12": 1.1420164300227301e-12, "-13": 5.1847343139639494e-14, "-2": 0.036739351406132964, "-3": 0.0072101084007235505, "-4": 0.0010853981529906243, "-5": 0.00013224426402768663, "-6": 1.3518370247836105e-05, "-7": 1.189556792087271e-06, "-8": 9.18552868685948e-08, "-9": 6.317578304988608e-09, "0": 0.2667346751661872, "1": 0.3071823076025893, "10": 3.2306608301601546e-07, "11": 3.494269152236214e-08, "12": 3.4625210910845833e-09, "13": 3.013713599373778e-10, "2": 0.16607245248599806, "3": 0.0624832059232906, "4": 0.01803291703493238, "5": 0.004212201578257063, "6": 0.0008254904162871324, "7": 0.0001392606044367202, "8": 2.0615916603901766e-05, "9": 2.7183446623245406e-06} |
| Raw goal margin distribution | {"-1": 0.14111826862645785, "-10": 4.2805453517519104e-10, "-11": 2.4149530653820683e-11, "-12": 1.2482149267474677e-12, "-13": 5.666873603369073e-14, "-2": 0.040155820545631715, "-3": 0.00788059146318177, "-4": 0.0011863315976986984, "-5": 0.00014454193477129413, "-6": 1.4775471775228348e-05, "-7": 1.300176166526442e-06, "-8": 1.0039710213956258e-07, "-9": 6.905063126828915e-09, "0": 0.3127328071371567, "1": 0.272997013703238, "10": 2.8711313675746067e-07, "11": 3.1054035991875935e-08, "12": 3.077188673813454e-09, "13": 2.6783274701167804e-10, "2": 0.14759080345767991, "3": 0.05552965845197986, "4": 0.016026093876681618, "5": 0.0037434397213654868, "6": 0.0007336243426446943, "7": 0.00012376275650262104, "8": 1.8321640043479963e-05, "9": 2.415829156381013e-06} |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 31.3% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 54.6% |
| Raw p under 3 5 | 88.8% |
| Raw p btts yes | 32.7% |
| P home draw | 82.6% |
| P draw away | 44.1% |
| P home away | 73.3% |
| Raw p home draw | 80.9% |
| Raw p draw away | 50.3% |
| Raw p home away | 68.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.89, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.56, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.56 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.60 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.38 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | -6.2% |
| Draw probability edge | +4.6% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -12.2% |
| Under 2.5 probability edge | +12.2% |
| Raw edge prob home | -0.1244 |
| Raw ev home | -0.2101 |
| Raw edge prob draw | 0.0920 |
| Raw ev draw | 0.2978 |
| Raw edge prob away | 0.0324 |
| Raw ev away | 0.1278 |
| Market p home draw | 84.4% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:20:05Z |
| Market reference home draw last update utc | 2026-10-23T16:20:43Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.8% |
| Market draw away odds | 2.47 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:20:05Z |
| Market reference draw away last update utc | 2026-10-23T16:20:43Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:20:05Z |
| Market reference home away last update utc | 2026-10-23T16:20:43Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.15 |
| Market reference dc draw away odds | 2.44 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 67.2% |
| Market over 1 5 odds | 1.44 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference over 1 5 odds | 1.46 |
| Market reference over 1 5 opposite odds | 2.90 |
| Market reference over 1 5 last update utc | 2026-10-23T16:20:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 80.9% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 4.70 |
| Market reference under 3 5 last update utc | 2026-10-23T16:20:44Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 40.2% |
| Market btts yes odds | 2.50 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:20:05Z |
| Market reference btts yes odds | 2.25 |
| Market reference btts yes opposite odds | 1.58 |
| Market reference btts yes last update utc | 2026-10-23T16:20:43Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,491.3653 |
| Elo away rating | 1,456.5803 |
| Elo rating diff | 94.7851 |
| Elo home expectancy | 0.6331 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **56.1%**. Expected goals are 1.97 for Barcelona and 1.35 for Real Madrid (3.32 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.7%; Under 3.5 goals: 57.2%; Double Chance 1X: 75.2%; Double Chance X2: 43.9%; Double Chance 12 (either team wins): 80.9%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 56.1% | 1.78 |
| Draw | 19.1% | 5.24 |
| Real Madrid win | 24.8% | 4.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.97 |
| Real Madrid expected goals | 1.35 |
| Expected total goals | 3.32 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.27% |
| 2 | 1-1 | 8.41% |
| 3 | 2-0 | 7.60% |
| 4 | 1-0 | 7.47% |
| 5 | 3-1 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 56.1% | 60.4% | 1.63 | -8.6% |
| Draw | 19.1% | 15.9% | 5.66 | +8.1% |
| Real Madrid win | 24.8% | 23.7% | 4.03 | +0.1% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9720 |
| Dc lambda away | 1.3513 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.57 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.58 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.03 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.14090343107160552, "-10": 2.4459015501126345e-07, "-11": 2.9461380402453458e-08, "-12": 3.2626005631167366e-09, "-13": 3.342850848988687e-10, "-14": 3.184475193299399e-11, "-15": 2.806438858248392e-12, "-16": 2.0317910433841121e-13, "-2": 0.0704479473625795, "-3": 0.026492707585167054, "-4": 0.007969927679562595, "-5": 0.0019874776420864926, "-6": 0.00042200691632916456, "-7": 7.788656057185351e-05, "-8": 1.2699012119937588e-05, "-9": 1.853061422584017e-06, "0": 0.19091915194264208, "1": 0.2345998428033531, "10": 1.2170544856117596e-05, "11": 2.139354382437816e-06, "12": 3.4574199729886564e-07, "13": 5.1696818853470786e-08, "14": 7.186927775869458e-09, "15": 9.243141162681053e-10, "16": 9.765660734403648e-11, "2": 0.17040042361490618, "3": 0.09351628864112232, "4": 0.04105574031111368, "5": 0.014941023514405193, "6": 0.004629736313551775, "7": 0.0012469751652111629, "8": 0.0002967042765698971, "9": 6.318329545123453e-05} |
| Raw goal margin distribution | {"-1": 0.14759072595208675, "-10": 2.561984350863719e-07, "-11": 3.0859621288703525e-08, "-12": 3.4174440035983103e-09, "-13": 3.501502978313302e-10, "-14": 3.335610793725966e-11, "-15": 2.939632805808197e-12, "-16": 2.1282201064615423e-13, "-2": 0.07379141596483647, "-3": 0.0277500548793883, "-4": 0.008348181467735145, "-5": 0.0020818035854642783, "-6": 0.000442035418613552, "-7": 8.158306670949155e-05, "-8": 1.3301708861180683e-05, "-9": 1.9410079549730397e-06, "0": 0.2227290879437945, "1": 0.21636154366828325, "10": 1.1224380378468228e-05, "11": 1.9730363460888765e-06, "12": 3.18863266712593e-07, "13": 4.7677796354076156e-08, "14": 6.628200467819548e-09, "15": 8.524559379086418e-10, "16": 9.006457149280384e-11, "2": 0.15715312616792398, "3": 0.08624613011988248, "4": 0.03786397827044818, "5": 0.013779476034306286, "6": 0.004269810600072796, "7": 0.001150032619106442, "8": 0.0002736378444441424, "9": 5.8271289419989905e-05} |
| Unadjusted home-win probability | 51.7% |
| Unadjusted draw probability | 22.3% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 64.0% |
| P home draw | 75.2% |
| P draw away | 43.9% |
| P home away | 80.9% |
| Raw p home draw | 74.0% |
| Raw p draw away | 48.3% |
| Raw p home away | 77.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.63 |
| Reference draw odds | 5.95 |
| Reference away odds | 4.05 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 4.80 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:19Z |
| Home probability edge | -4.4% |
| Draw probability edge | +3.2% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -17.8% |
| Under 2.5 probability edge | +17.8% |
| Raw edge prob home | -0.0872 |
| Raw ev home | -0.1570 |
| Raw edge prob draw | 0.0636 |
| Raw ev draw | 0.2606 |
| Raw edge prob away | 0.0236 |
| Raw ev away | 0.0482 |
| Elo home rating | 1,739.3786 |
| Elo away rating | 1,656.5478 |
| Elo rating diff | 142.8309 |
| Elo home expectancy | 0.6947 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Real Betis win** at **37.9%**. Expected goals are 1.41 for Celta Vigo and 1.29 for Real Betis (2.70 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.5%; Double Chance 1X: 62.1%; Double Chance X2: 64.4%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 86.3%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 35.6% | 2.81 |
| Draw | 26.4% | 3.78 |
| Real Betis win | 37.9% | 2.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.41 |
| Real Betis expected goals | 1.29 |
| Expected total goals | 2.70 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.5% |
| Under 3.5 | 71.5% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.56% |
| 2 | 0-1 | 9.37% |
| 3 | 1-2 | 8.79% |
| 4 | 1-0 | 8.27% |
| 5 | 2-1 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 35.6% | 31.4% | 3.15 | +12.2% |
| Draw | 26.4% | 26.6% | 3.53 | -6.7% |
| Real Betis win | 37.9% | 42.0% | 2.31 | -12.4% |
| Over 2.5 | 50.5% | 52.0% | 1.90 | -4.0% |
| Under 2.5 | 49.5% | 48.0% | 1.98 | -2.1% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Dc lambda home | 1.4143 |
| Dc lambda away | 1.2852 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.22 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.51 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.32 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.2127520968721149, "-10": 3.00514502368524e-07, "-11": 3.4638025665020205e-08, "-12": 3.666151089215773e-09, "-13": 3.564167483091849e-10, "-14": 2.8958424092186356e-11, "-2": 0.10953516717162962, "-3": 0.04117944266630393, "-4": 0.012184107420349925, "-5": 0.0029596133817130898, "-6": 0.0006084086283102881, "-7": 0.00010827114001856194, "-8": 1.6973102232261314e-05, "-9": 2.3764612385214744e-06, "0": 0.26439401301474014, "1": 0.18728263095516196, "10": 6.254394573753438e-07, "11": 7.93336457436603e-08, "12": 9.240576862665938e-09, "13": 9.886242753533961e-10, "14": 8.839598353750716e-11, "2": 0.10597364734640076, "3": 0.04384390345934504, "4": 0.01427601216724152, "5": 0.003816213067030924, "6": 0.0008633312041368017, "7": 0.00016907493347934248, "8": 2.9168371621295645e-05, "9": 4.494342176623738e-06} |
| Raw goal margin distribution | {"-1": 0.18999169033304913, "-10": 2.68365196461076e-07, "-11": 3.093241919891639e-08, "-12": 3.2739430195846323e-09, "-13": 3.182869709386467e-10, "-14": 2.5860426400229296e-11, "-2": 0.09781699859983219, "-3": 0.03677402965314517, "-4": 0.010880640886859047, "-5": 0.002642991337763317, "-6": 0.0005433205378716717, "-7": 9.668819818390698e-05, "-8": 1.5157304819615347e-05, "-9": 2.1222253240073473e-06, "0": 0.26299006767303806, "1": 0.20935475837393785, "10": 6.991504006994138e-07, "11": 8.868348415910487e-08, "12": 1.0329621740429247e-08, "13": 1.1051382353698987e-09, "14": 9.881386052907396e-11, "2": 0.1184631336128671, "3": 0.04901111100419667, "4": 0.01595850646999824, "5": 0.004265971491734336, "6": 0.0009650787941035131, "7": 0.00018900119923097303, "8": 3.2605999615626754e-05, "9": 5.024021264748934e-06} |
| Unadjusted home-win probability | 39.8% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 33.9% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 55.0% |
| P home draw | 62.1% |
| P draw away | 64.4% |
| P home away | 73.6% |
| Raw p home draw | 66.1% |
| Raw p draw away | 60.2% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.75, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.1, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.74, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.04, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.46, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 5.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:49Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.17, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.17, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:44Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:44Z |
| Market best over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market best under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | +4.2% |
| Draw probability edge | -0.1% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | 0.0840 |
| Raw ev home | 0.2545 |
| Raw edge prob draw | -0.0028 |
| Raw ev draw | -0.0716 |
| Raw edge prob away | -0.0812 |
| Raw ev away | -0.2175 |
| Market p home draw | 60.3% |
| Market home draw odds | 1.66 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:20:40Z |
| Market reference home draw last update utc | 2026-10-23T16:20:43Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.9% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:20:40Z |
| Market reference draw away last update utc | 2026-10-23T16:20:43Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:20:40Z |
| Market reference home away last update utc | 2026-10-23T16:20:43Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.61 |
| Market reference dc draw away odds | 1.43 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 76.5% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.95 |
| Market reference over 1 5 last update utc | 2026-10-23T16:20:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.2% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-23T16:20:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.5% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:20:40Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.15 |
| Market reference btts yes last update utc | 2026-10-23T16:20:43Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,477.2163 |
| Elo away rating | 1,549.1815 |
| Elo rating diff | -11.9651 |
| Elo home expectancy | 0.4828 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **58.2%**. Expected goals are 1.97 for Real Sociedad and 1.18 for Levante (3.16 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 61.4%; Under 3.5 goals: 61.0%; Double Chance 1X: 79.7%; Double Chance X2: 41.8%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 59.7%; BTTS No (at least one team does not score): 40.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 58.2% | 1.72 |
| Draw | 21.5% | 4.65 |
| Levante win | 20.3% | 4.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.97 |
| Levante expected goals | 1.18 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 61.4% |
| Under 2.5 | 38.6% |
| Over 3.5 | 39.0% |
| Under 3.5 | 61.0% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.29% |
| 2 | 1-1 | 9.85% |
| 3 | 2-0 | 8.69% |
| 4 | 1-0 | 8.58% |
| 5 | 3-1 | 6.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 58.2% | 60.9% | 1.60 | -6.9% |
| Draw | 21.5% | 20.8% | 4.54 | -2.3% |
| Levante win | 20.3% | 18.2% | 5.17 | +4.9% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9723 |
| Dc lambda away | 1.1842 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.7% |
| P btts no | 40.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.04 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.78 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.67 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.12262801747643898, "-10": 7.13391849537408e-08, "-11": 7.548655047925258e-09, "-12": 7.341008073640914e-10, "-13": 6.603404546214386e-11, "-14": 5.5224459399840196e-12, "-15": 4.281137733974978e-13, "-16": 2.765059886620748e-14, "-2": 0.055435989725191724, "-3": 0.018615385977046497, "-4": 0.004970747526927138, "-5": 0.0010962950625413796, "-6": 0.00020540162722398824, "-7": 3.339910771761604e-05, "-8": 4.79247803351842e-06, "-9": 6.149740953986281e-07, "0": 0.21519941516475477, "1": 0.2375184402891238, "10": 1.3530926273252414e-05, "11": 2.384471341263076e-06, "12": 3.8619030927897957e-07, "13": 5.7854443072703546e-08, "14": 8.057928860242668e-09, "15": 1.040337608893703e-09, "16": 1.1190327145125971e-10, "2": 0.177666704812689, "3": 0.0993595075124627, "4": 0.04418575016978706, "5": 0.016229723782823925, "6": 0.005064198182326159, "7": 0.0013714021325705757, "8": 0.00032772776011765045, "9": 7.003789163825799e-05} |
| Raw goal margin distribution | {"-1": 0.13504392705861493, "-10": 7.856217435110226e-08, "-11": 8.312945464347292e-09, "-12": 8.084274533949314e-10, "-13": 7.271989715146763e-11, "-14": 6.081585611931094e-12, "-15": 4.714596743651031e-13, "-16": 3.045018204858919e-14, "-2": 0.061048803584460555, "-3": 0.020500166909533827, "-4": 0.005474028531710649, "-5": 0.0012072933535682649, "-6": 0.0002261982451921034, "-7": 3.6780719115084405e-05, "-8": 5.277709509678928e-06, "-9": 6.772393339711824e-07, "0": 0.22196068794425655, "1": 0.2263678406001353, "10": 1.2895700047825051e-05, "11": 2.2725293574578394e-06, "12": 3.680601231035622e-07, "13": 5.513839401921609e-08, "14": 7.679639330665338e-09, "15": 9.914976611235326e-10, "16": 1.0664983267689626e-10, "2": 0.1693259195624303, "3": 0.09469495139539708, "4": 0.04211139496813954, "5": 0.015467799139226423, "6": 0.004826453076691058, "7": 0.001307019947447159, "8": 0.0003123421712951892, "9": 6.674987538247454e-05} |
| Unadjusted home-win probability | 55.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 22.4% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.2% |
| Raw p btts yes | 60.0% |
| P home draw | 79.7% |
| P draw away | 41.8% |
| P home away | 78.5% |
| Raw p home draw | 77.6% |
| Raw p draw away | 44.6% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.55 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | -2.7% |
| Draw probability edge | +0.7% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | -0.0546 |
| Raw ev home | -0.1128 |
| Raw edge prob draw | 0.0135 |
| Raw ev draw | 0.0077 |
| Raw edge prob away | 0.0411 |
| Raw ev away | 0.1557 |
| Elo home rating | 1,485.8012 |
| Elo away rating | 1,453.6938 |
| Elo rating diff | 92.1074 |
| Elo home expectancy | 0.6295 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **49.5%**. Expected goals are 1.51 for Sevilla and 1.06 for CA Osasuna (2.57 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.2%; Double Chance 1X: 76.1%; Double Chance X2: 50.5%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 49.5% | 2.02 |
| Draw | 26.6% | 3.76 |
| CA Osasuna win | 23.9% | 4.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.51 |
| CA Osasuna expected goals | 1.06 |
| Expected total goals | 2.57 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 11.80% |
| 3 | 2-1 | 9.65% |
| 4 | 2-0 | 9.12% |
| 5 | 0-0 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 49.5% | 51.5% | 1.94 | -4.0% |
| Draw | 26.6% | 26.9% | 3.48 | -7.4% |
| CA Osasuna win | 23.9% | 21.5% | 4.31 | +3.0% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5108 |
| Dc lambda away | 1.0581 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.46 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.45 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.14824326259932055, "-10": 3.903989537084362e-08, "-11": 3.710721417018564e-09, "-12": 3.2389420695161367e-10, "-13": 2.6129455588318708e-11, "-14": 1.95064372896358e-12, "-15": 1.2434437625644502e-13, "-2": 0.06445089108559582, "-3": 0.020227240230372315, "-4": 0.0049724907808036956, "-5": 0.0010008324730812954, "-6": 0.00017019172690235614, "-7": 2.5026055644320763e-05, "-8": 3.2392618678417605e-06, "-9": 3.742680865317441e-07, "0": 0.26618537136611403, "1": 0.24393126037353716, "10": 1.5769563842290683e-06, "11": 2.1402066316202849e-07, "12": 2.667392053236919e-08, "13": 3.072559853417289e-09, "14": 3.2751731448843517e-10, "15": 2.981046665109637e-11, "2": 0.1506778515863764, "3": 0.06752171172371789, "4": 0.023701024299780705, "5": 0.0068114697926726095, "6": 0.001653880816665874, "7": 0.0003472517864476844, "8": 6.417774588855297e-05, "9": 1.0587843553451953e-05} |
| Raw goal margin distribution | {"-1": 0.1629194141480112, "-10": 4.29048630655721e-08, "-11": 4.078084553232933e-09, "-12": 3.5595988321653044e-10, "-13": 2.8716283774469977e-11, "-14": 2.1437583601569693e-12, "-15": 1.3665452700575374e-13, "-2": 0.07083155910675885, "-3": 0.022229746366756262, "-4": 0.005464769667506209, "-5": 0.0010999153507260785, "-6": 0.000187040786566561, "-7": 2.7503646725776757e-05, "-8": 3.559950290673047e-06, "-9": 4.113208001692238e-07, "0": 0.26309188263274197, "1": 0.23378544949984742, "10": 1.5113661798167872e-06, "11": 2.0511892105575452e-07, "12": 2.55644745656373e-08, "13": 2.9447631490378387e-09, "14": 3.138949164178888e-10, "15": 2.8570562605033116e-11, "2": 0.1444107213189877, "3": 0.06471328726853495, "4": 0.022715229737451673, "5": 0.006528160944997733, "6": 0.0015850911012853196, "7": 0.0003328085742679333, "8": 6.150840670222694e-05, "9": 1.0147464333137832e-05} |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 72.9% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.1% |
| P home draw | 76.1% |
| P draw away | 50.5% |
| P home away | 73.4% |
| Raw p home draw | 73.7% |
| Raw p draw away | 52.6% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.48, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.96, "price": 1.48, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.80 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.21 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:45Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:45Z |
| Home probability edge | -2.1% |
| Draw probability edge | -0.3% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | +3.7% |
| Under 2.5 probability edge | -3.7% |
| Raw edge prob home | -0.0412 |
| Raw ev home | -0.0802 |
| Raw edge prob draw | -0.0062 |
| Raw ev draw | -0.0844 |
| Raw edge prob away | 0.0473 |
| Raw ev away | 0.1325 |
| Elo home rating | 1,440.7731 |
| Elo away rating | 1,423.7802 |
| Elo rating diff | 76.9929 |
| Elo home expectancy | 0.6090 |

</details>


---

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **63.4%**. Expected goals are 2.18 for Villarreal and 0.98 for Espanyol (3.16 combined). The most likely exact score is 2-0 at 9.9%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.0%; Under 3.5 goals: 61.3%; Double Chance 1X: 83.4%; Double Chance X2: 36.6%; Double Chance 12 (either team wins): 80.0%; Under 4.5 goals: 78.9%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 63.4% | 1.58 |
| Draw | 20.0% | 4.99 |
| Espanyol win | 16.6% | 6.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.18 |
| Espanyol expected goals | 0.98 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 82.4% |
| Under 1.5 | 17.6% |
| Over 2.5 | 61.0% |
| Under 2.5 | 39.0% |
| Over 3.5 | 38.7% |
| Under 3.5 | 61.3% |
| Over 4.5 | 21.1% |
| Under 4.5 | 78.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.91% |
| 2 | 2-1 | 9.71% |
| 3 | 1-1 | 9.34% |
| 4 | 1-0 | 8.90% |
| 5 | 3-0 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 63.4% | 62.3% | 1.56 | -1.1% |
| Draw | 20.0% | 20.2% | 4.31 | -13.6% |
| Espanyol win | 16.6% | 17.5% | 5.40 | -10.5% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1796 |
| Dc lambda away | 0.9797 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.30 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.69 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.59 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.74 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.10910697859655678, "-10": 1.2244866247098672e-08, "-11": 1.0734187629542295e-09, "-12": 8.646407501923435e-11, "-13": 6.441120920692189e-12, "-14": 4.462294747824858e-13, "-15": 2.888080435068637e-14, "-16": 1.7432351537210068e-15, "-17": 8.924952575229935e-17, "-2": 0.041709328969746544, "-3": 0.011724055844289632, "-4": 0.002610463820992189, "-5": 0.00047898531035606276, "-6": 7.455391062854488e-05, "-7": 1.0061316254821351e-05, "-8": 1.1974066961720192e-06, "-9": 1.2737643349915802e-07, "0": 0.20036054505869458, "1": 0.22750126810735394, "10": 3.372949054164702e-05, "11": 6.578228570694814e-06, "12": 1.1788526348293282e-06, "13": 1.9537514458507412e-07, "14": 3.0112731708804784e-08, "15": 4.33595960263781e-09, "16": 5.822586638395987e-10, "17": 6.632082846054191e-11, "2": 0.1914329129138404, "3": 0.11971410546260484, "4": 0.05930197621182361, "5": 0.024207933831944424, "6": 0.008382817264724628, "7": 0.002516856253016696, "8": 0.0006663913262760153, "9": 0.0001577105619369778} |
| Raw goal margin distribution | {"-1": 0.10293797099848168, "-10": 1.1552530395740498e-08, "-11": 1.0127266918350502e-09, "-12": 8.157531774068732e-11, "-13": 6.07693409771362e-12, "-14": 4.209992552692392e-13, "-15": 2.724785745975737e-14, "-16": 1.6446710559257452e-15, "-17": 8.420327656115998e-17, "-2": 0.0393510456533657, "-3": 0.011061167085806843, "-4": 0.0024628658272309607, "-5": 0.0004519030461694695, "-6": 7.033856485461086e-05, "-7": 9.492440301871184e-06, "-8": 1.1297042347741528e-06, "-9": 1.201744543390751e-07, "0": 0.19867620335041, "1": 0.23146832764163616, "10": 3.4317649447981474e-05, "11": 6.692936609850659e-06, "12": 1.1994089096291095e-06, "13": 1.9878200396891829e-07, "14": 3.0637823284876026e-08, "15": 4.411568015834831e-09, "16": 5.924118150858298e-10, "17": 6.747729970597576e-11, "2": 0.1947710295259725, "3": 0.12180162342421635, "4": 0.060336056030762815, "5": 0.02463006033485241, "6": 0.008528992868187545, "7": 0.0025607440022060173, "8": 0.0006780115431058345, "9": 0.00016046064413913005} |
| Unadjusted home-win probability | 64.5% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 15.6% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.2% |
| Raw p btts yes | 55.6% |
| P home draw | 83.4% |
| P draw away | 36.6% |
| P home away | 80.0% |
| Raw p home draw | 84.4% |
| Raw p draw away | 35.5% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.54 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:46Z |
| Market reference home last update utc | 2026-10-23T16:20:46Z |
| Market reference draw last update utc | 2026-10-23T16:20:46Z |
| Market reference away last update utc | 2026-10-23T16:20:46Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +1.5% |
| Under 2.5 probability edge | -1.5% |
| Raw edge prob home | 0.0221 |
| Raw ev home | 0.0062 |
| Raw edge prob draw | -0.0034 |
| Raw ev draw | -0.1437 |
| Raw edge prob away | -0.0187 |
| Raw ev away | -0.1557 |
| Elo home rating | 1,558.8984 |
| Elo away rating | 1,440.6093 |
| Elo rating diff | 178.2890 |
| Elo home expectancy | 0.7362 |

</details>


---

## 2026-10-31 — Barcelona vs Alavés

The model's most likely 1X2 outcome is **Barcelona win** at **85.2%**. Expected goals are 2.84 for Barcelona and 0.70 for Alavés (3.54 combined). The most likely exact score is 2-0 at 12.3%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 70.2%; Under 3.5 goals: 51.8%; Double Chance 1X: 95.0%; Double Chance X2: 14.8%; Double Chance 12 (either team wins): 90.2%; Under 4.5 goals: 70.8%; BTTS Yes (both teams score): 46.6%; BTTS No (at least one team does not score): 53.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 85.2% | 1.17 |
| Draw | 9.8% | 10.18 |
| Alavés win | 5.0% | 20.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.84 |
| Alavés expected goals | 0.70 |
| Expected total goals | 3.54 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 87.6% |
| Under 1.5 | 12.4% |
| Over 2.5 | 70.2% |
| Under 2.5 | 29.8% |
| Over 3.5 | 48.2% |
| Under 3.5 | 51.8% |
| Over 4.5 | 29.2% |
| Under 4.5 | 70.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.27% |
| 2 | 3-0 | 11.61% |
| 3 | 2-1 | 8.62% |
| 4 | 1-0 | 8.51% |
| 5 | 4-0 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 85.2% | 89.4% | 1.16 | -1.1% |
| Draw | 9.8% | 7.1% | 6.48 | -36.4% |
| Alavés win | 5.0% | 3.5% | 23.04 | +14.2% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8386 |
| Dc lambda away | 0.7025 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.6% |
| P btts no | 53.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.19 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.09 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.35 |
| Fair Over 3.5 odds | 2.07 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.43 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.03677361007348083, "-10": 2.1733634517240814e-10, "-11": 1.3676294516233723e-11, "-12": 7.906597246442289e-13, "-13": 4.2268566828887915e-14, "-14": 2.1012527599871146e-15, "-15": 9.760660577307529e-17, "-16": 4.254661239903682e-18, "-17": 1.7466121724006674e-19, "-18": 6.745762435443819e-21, "-19": 2.257316836497071e-22, "-2": 0.010295242164200694, "-3": 0.00209289250726867, "-4": 0.00033606939995746004, "-5": 4.43975282882862e-05, "-6": 4.970292242755239e-06, "-7": 4.821053236183482e-07, "-8": 4.121890107096142e-08, "-9": 3.1489181922894857e-09, "0": 0.09820741313784086, "1": 0.20527695028745305, "10": 0.00034132484077478167, "11": 8.678488562147515e-05, "12": 2.0272410024671637e-05, "13": 4.378984433812833e-06, "14": 8.795778606796766e-07, "15": 1.6508792813784265e-07, "16": 2.9076438333522468e-08, "17": 4.822950636504935e-09, "18": 7.5264033835839e-10, "19": 1.0176280821011973e-10, "2": 0.22758896029570966, "3": 0.18693975208923921, "4": 0.12128967259532553, "5": 0.06474314017295905, "6": 0.02928579420050308, "7": 0.011477759544525788, "8": 0.0039650778431732, "9": 0.0012239306224054746} |
| Raw goal margin distribution | {"-1": 0.047370805072505, "-10": 2.7996700954191336e-10, "-11": 1.7617445781040602e-11, "-12": 1.0185072289601563e-12, "-13": 5.444926500129913e-14, "-14": 2.7067789836928275e-15, "-15": 1.2573428299876275e-16, "-16": 5.480743605055098e-18, "-17": 2.24994023134332e-19, "-18": 8.689715172274582e-21, "-19": 2.9078166553383693e-22, "-2": 0.013262062352868764, "-3": 0.0026960095242600716, "-4": 0.000432915832968467, "-5": 5.719173760865296e-05, "-6": 6.402600792102647e-06, "-7": 6.210354997485291e-07, "-8": 5.309711295773684e-08, "-9": 4.056354259974633e-09, "0": 0.12539118210756825, "1": 0.1952901272784691, "10": 0.00032471922203086505, "11": 8.25627589221895e-05, "12": 1.9286147462808536e-05, "13": 4.16594472117902e-06, "14": 8.367859719414231e-07, "15": 1.5705632051251602e-07, "16": 2.7661855532278105e-08, "17": 4.58831175317978e-09, "18": 7.160240215333322e-10, "19": 9.681199832587058e-11, "2": 0.21651664719826175, "3": 0.1778450426498976, "4": 0.11538887130550256, "5": 0.061593355060467044, "6": 0.02786102613497795, "7": 0.010919360986137511, "8": 0.003772174886552088, "9": 0.0011643858051031777} |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 12.5% |
| Unadjusted away-win probability | 6.4% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 52.8% |
| Raw p btts yes | 47.6% |
| P home draw | 95.0% |
| P draw away | 14.8% |
| P home away | 90.2% |
| Raw p home draw | 93.6% |
| Raw p draw away | 18.9% |
| Raw p home away | 87.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.09 |
| Reference draw odds | 7.60 |
| Reference away odds | 13.00 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.90 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:19Z |
| Home probability edge | -4.1% |
| Draw probability edge | +2.7% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.0829 |
| Raw ev home | -0.0595 |
| Raw edge prob draw | 0.0544 |
| Raw ev draw | -0.1875 |
| Raw edge prob away | 0.0286 |
| Raw ev away | 0.4706 |
| Elo home rating | 1,739.3786 |
| Elo away rating | 1,440.0805 |
| Elo rating diff | 359.2981 |
| Elo home expectancy | 0.8878 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **57.1%**. Expected goals are 1.23 for Levante and 1.94 for Atlético Madrid (3.16 combined). The most likely exact score is 1-2 at 10.4%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.8%; Double Chance 1X: 42.9%; Double Chance X2: 78.5%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 78.4%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 21.5% | 4.65 |
| Draw | 21.4% | 4.68 |
| Atlético Madrid win | 57.1% | 1.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.23 |
| Atlético Madrid expected goals | 1.94 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.2% |
| Under 3.5 | 60.8% |
| Over 4.5 | 21.6% |
| Under 4.5 | 78.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.35% |
| 2 | 1-1 | 9.74% |
| 3 | 0-1 | 8.48% |
| 4 | 0-2 | 8.44% |
| 5 | 1-3 | 6.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 21.5% | 19.2% | 4.52 | -2.8% |
| Draw | 21.4% | 20.2% | 4.59 | -1.9% |
| Atlético Madrid win | 57.1% | 60.6% | 1.62 | -7.5% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Levante |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2269 |
| Dc lambda away | 1.9355 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.66 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.81 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.63 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.2384395080745186, "-10": 1.1344410592706648e-05, "-11": 1.9613704362735792e-06, "-12": 3.116736592775695e-07, "-13": 4.58121390496289e-08, "-14": 6.260591085604107e-09, "-15": 7.928956854253437e-10, "-16": 8.352142306981513e-11, "-2": 0.1744450109491434, "-3": 0.09552497584533635, "-4": 0.041625759815526665, "-5": 0.014988314951031525, "-6": 0.004586003500435045, "-7": 0.001218010493780155, "-8": 0.000285507962465655, "-9": 5.985460640790504e-05, "0": 0.2136731536953958, "1": 0.12763482691914288, "10": 1.0087974752872703e-07, "11": 1.1055400594431333e-08, "12": 1.1135449894615747e-09, "13": 1.0374831392494798e-10, "14": 8.986873422788896e-12, "15": 7.214432095684532e-13, "16": 4.817001592932132e-14, "2": 0.05953030813207837, "3": 0.020662807171010374, "4": 0.005707256210139064, "5": 0.0013025992231965697, "6": 0.00025263015901634756, "7": 4.252992850385538e-05, "8": 6.319091681517106e-06, "9": 8.397051565594096e-07} |
| Raw goal margin distribution | {"-1": 0.22405529137041633, "-10": 1.0660042210706769e-05, "-11": 1.8430478578543962e-06, "-12": 2.9287148386539745e-07, "-13": 4.3048453865534395e-08, "-14": 5.882911649849877e-09, "-15": 7.450630780902313e-10, "-16": 7.848286944012151e-11, "-2": 0.1639213571272366, "-3": 0.08976229010458227, "-4": 0.03911462416315683, "-5": 0.01408412263816367, "-6": 0.004309346042580314, "-7": 0.0011445322055892197, "-8": 0.0002682842714925584, "-9": 5.624378856877e-05, "0": 0.22525588227266258, "1": 0.14120569817957532, "10": 1.11605864369584e-07, "11": 1.2230874576110182e-08, "12": 1.2319435179780585e-09, "13": 1.1477943329689137e-10, "14": 9.942409660023988e-12, "15": 7.981512143904369e-13, "16": 5.329172996748056e-14, "2": 0.06585991398696078, "3": 0.022859796055357474, "4": 0.006314084621691399, "5": 0.0014410990887006668, "6": 0.0002794912552176636, "7": 4.7051955903217584e-05, "8": 6.9909739707222666e-06, "9": 9.289874539656505e-07} |
| Unadjusted home-win probability | 23.8% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 82.6% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.7% |
| P home draw | 42.9% |
| P draw away | 78.5% |
| P home away | 78.6% |
| Raw p home draw | 46.3% |
| Raw p draw away | 76.2% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.50 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.58 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:19Z |
| Home probability edge | +2.3% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | 0.0457 |
| Raw ev home | 0.0758 |
| Raw edge prob draw | 0.0232 |
| Raw ev draw | 0.0339 |
| Raw edge prob away | -0.0689 |
| Raw ev away | -0.1305 |
| Elo home rating | 1,479.7866 |
| Elo away rating | 1,584.7626 |
| Elo rating diff | -44.9761 |
| Elo home expectancy | 0.4356 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **40.5%**. Expected goals are 1.21 for Rayo Vallecano and 1.09 for Celta Vigo (2.30 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 40.8%; Under 3.5 goals: 79.8%; Double Chance 1X: 68.4%; Double Chance X2: 59.5%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 46.7%; BTTS No (at least one team does not score): 53.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 40.5% | 2.47 |
| Draw | 27.8% | 3.59 |
| Celta Vigo win | 31.6% | 3.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.21 |
| Celta Vigo expected goals | 1.09 |
| Expected total goals | 2.30 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 67.3% |
| Under 1.5 | 32.7% |
| Over 2.5 | 40.8% |
| Under 2.5 | 59.2% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.03% |
| 2 | 1-0 | 12.42% |
| 3 | 0-1 | 10.32% |
| 4 | 0-0 | 9.93% |
| 5 | 2-1 | 8.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 40.5% | 42.4% | 2.35 | -4.7% |
| Draw | 27.8% | 26.8% | 3.46 | -3.7% |
| Celta Vigo win | 31.6% | 30.8% | 2.99 | -5.5% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Vallecano |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2149 |
| Dc lambda away | 1.0875 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.7% |
| P btts no | 53.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.07 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.45 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.77 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.19048159542934107, "-10": 7.008713893838727e-08, "-11": 6.861246908401564e-09, "-12": 6.165647686373789e-10, "-13": 5.101827893935777e-11, "-14": 3.621425938072777e-12, "-2": 0.08763974163972824, "-3": 0.028789766113405054, "-4": 0.007361187121372368, "-5": 0.0015355187023718823, "-6": 0.00027002291409873656, "-7": 4.100163971735881e-05, "-8": 5.4748750517901675e-06, "-9": 6.521156909463132e-07, "0": 0.27839173936216915, "1": 0.22898775449214054, "10": 2.2790925679605052e-07, "11": 2.492416092803152e-08, "12": 2.5020159216265452e-09, "13": 2.3127624820335238e-10, "14": 1.833912889543111e-11, "2": 0.11750972171414263, "3": 0.043122577499859545, "4": 0.012317095190271975, "5": 0.0028701818652711137, "6": 0.0005638307934189966, "7": 9.564081357029955e-05, "8": 1.4266259327918962e-05, "9": 1.8982544111958736e-06} |
| Raw goal margin distribution | {"-1": 0.1953895911520629, "-10": 7.189302142982734e-08, "-11": 7.038035486862757e-09, "-12": 6.324513283883746e-10, "-13": 5.233282848547327e-11, "-14": 3.714736491116776e-12, "-2": 0.08989788881735301, "-3": 0.02953157032091532, "-4": 0.007550857282546825, "-5": 0.0015750832556108128, "-6": 0.0002769803910373686, "-7": 4.205809806916858e-05, "-8": 5.615942031390254e-06, "-9": 6.6891826452131e-07, "0": 0.288617890423899, "1": 0.2186128491194642, "10": 2.175832156587845e-07, "11": 2.3794904860626574e-08, "12": 2.388655368852113e-09, "13": 2.2079765647525305e-10, "14": 1.7508225394371e-11, "2": 0.11218562809237821, "3": 0.04116879328122657, "4": 0.011759036103886613, "5": 0.0027401405653745222, "6": 0.0005382849246414421, "7": 9.130754958088523e-05, "8": 1.361988812401993e-05, "9": 1.8122488956035601e-06} |
| Unadjusted home-win probability | 38.7% |
| Unadjusted draw probability | 28.9% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 67.3% |
| Raw p under 3 5 | 79.9% |
| Raw p btts yes | 46.9% |
| P home draw | 68.4% |
| P draw away | 59.5% |
| P home away | 72.2% |
| Raw p home draw | 67.6% |
| Raw p draw away | 61.3% |
| Raw p home away | 71.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.04, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:46Z |
| Market reference home last update utc | 2026-10-23T16:20:46Z |
| Market reference draw last update utc | 2026-10-23T16:20:46Z |
| Market reference away last update utc | 2026-10-23T16:20:46Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.11 |
| Reference Under 2.5 odds | 1.84 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | -1.8% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | -0.0367 |
| Raw ev home | -0.0903 |
| Raw edge prob draw | 0.0205 |
| Raw ev draw | -0.0014 |
| Raw edge prob away | 0.0163 |
| Raw ev away | -0.0304 |
| Elo home rating | 1,498.4715 |
| Elo away rating | 1,513.3163 |
| Elo rating diff | 45.1552 |
| Elo home expectancy | 0.5646 |

</details>


---

## 2026-10-31 — Real Betis vs Málaga

The model's most likely 1X2 outcome is **Real Betis win** at **74.4%**. Expected goals are 2.42 for Real Betis and 0.55 for Málaga (2.97 combined). The most likely exact score is 2-0 at 14.2%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.8%; Under 3.5 goals: 66.4%; Double Chance 1X: 90.4%; Double Chance X2: 25.6%; Double Chance 12 (either team wins): 83.9%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 39.5%; BTTS No (at least one team does not score): 60.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 74.4% | 1.34 |
| Draw | 16.1% | 6.22 |
| Málaga win | 9.6% | 10.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 2.42 |
| Málaga expected goals | 0.55 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 33.6% |
| Under 3.5 | 66.4% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.20% |
| 2 | 1-0 | 11.61% |
| 3 | 3-0 | 11.43% |
| 4 | 2-1 | 7.84% |
| 5 | 1-1 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 74.4% | 70.1% | 1.38 | +2.6% |
| Draw | 16.1% | 17.2% | 5.27 | -15.3% |
| Málaga win | 9.6% | 12.7% | 6.89 | -34.1% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Betis |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4156 |
| Dc lambda away | 0.5520 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 39.5% |
| P btts no | 60.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.57 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.70 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.77 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.07463441658698004, "-10": 6.203416982599405e-11, "-11": 3.081958145432698e-12, "-12": 1.4057000087844314e-13, "-13": 5.9253739290215825e-15, "-14": 2.3215110933213456e-16, "-15": 8.495739956756604e-18, "-16": 2.9164611510006534e-19, "-17": 9.405837156853458e-21, "-18": 2.6853924417890676e-22, "-2": 0.017662712948526563, "-3": 0.0029424737680841086, "-4": 0.0003816489220311251, "-5": 4.0390754179392444e-05, "-6": 3.603961605938386e-06, "-7": 2.7769035893016475e-07, "-8": 1.881622862238908e-08, "-9": 1.1373527961177062e-09, "0": 0.16078917609291596, "1": 0.21400016902251756, "10": 0.00010234280798029411, "11": 2.22511696155189e-05, "12": 4.441385897387325e-06, "13": 8.19297025031099e-07, "14": 1.4047405938872626e-07, "15": 2.249708939940074e-08, "16": 3.3797227336306843e-09, "17": 4.770040722539362e-10, "18": 5.95980633208581e-11, "2": 0.21661360673435667, "3": 0.1579212876516625, "4": 0.08963794067636924, "5": 0.041515430604579906, "6": 0.016210913707183215, "7": 0.005466229908190921, "8": 0.0016209119622186989, "9": 0.0004287674414029958} |
| Raw goal margin distribution | {"-1": 0.050502283262629816, "-10": 4.1976173456964654e-11, "-11": 2.085444361755268e-12, "-12": 9.511839613990757e-14, "-13": 4.0094761409664845e-15, "-14": 1.570878640092496e-16, "-15": 5.748745490918902e-18, "-16": 1.973458813075049e-19, "-17": 6.364573800399325e-21, "-18": 1.817103368236354e-22, "-2": 0.011951688956708726, "-3": 0.001991060565944919, "-4": 0.00025824737230753096, "-5": 2.7330893735622413e-05, "-6": 2.438664334953667e-06, "-7": 1.8790254961863003e-07, "-8": 1.273222932900998e-08, "-9": 7.696035650274068e-10, "0": 0.14957810343243616, "1": 0.22612947402951025, "10": 0.00010814349093739238, "11": 2.3512342558800822e-05, "12": 4.693118989231278e-06, "13": 8.657339206341031e-07, "14": 1.4843598166046508e-07, "15": 2.3772200817963223e-08, "16": 3.5712818714693093e-09, "17": 5.040401624980367e-10, "18": 6.297601900727948e-11, "2": 0.22889103864829746, "3": 0.16687210051210696, "4": 0.09471852508725348, "5": 0.04386848164467794, "6": 0.01712973128426547, "7": 0.0057760500830890855, "8": 0.0017127835512414386, "9": 0.0004530695300303069} |
| Unadjusted home-win probability | 78.6% |
| Unadjusted draw probability | 15.0% |
| Unadjusted away-win probability | 6.5% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.5% |
| Raw p btts yes | 38.8% |
| P home draw | 90.4% |
| P draw away | 25.6% |
| P home away | 83.9% |
| Raw p home draw | 93.5% |
| Raw p draw away | 21.4% |
| Raw p home away | 85.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.36 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:19Z |
| Home probability edge | +4.2% |
| Draw probability edge | -1.1% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.0843 |
| Raw ev home | 0.0843 |
| Raw edge prob draw | -0.0224 |
| Raw ev draw | -0.2117 |
| Raw edge prob away | -0.0619 |
| Raw ev away | -0.5540 |
| Elo home rating | 1,565.6917 |
| Elo away rating | 1,401.2778 |
| Elo rating diff | 224.4139 |
| Elo home expectancy | 0.7845 |

</details>


---

## 2026-11-01 — Athletic Bilbao vs Real Sociedad

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **47.6%**. Expected goals are 1.44 for Athletic Bilbao and 0.99 for Real Sociedad (2.43 combined). The most likely exact score is 1-0 at 12.5%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.0%; Under 3.5 goals: 77.3%; Double Chance 1X: 74.0%; Double Chance X2: 52.4%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 47.6% | 2.10 |
| Draw | 26.4% | 3.79 |
| Real Sociedad win | 26.0% | 3.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.44 |
| Real Sociedad expected goals | 0.99 |
| Expected total goals | 2.43 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.0% |
| Under 2.5 | 56.0% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.51% |
| 2 | 1-1 | 12.46% |
| 3 | 2-0 | 9.23% |
| 4 | 2-1 | 9.09% |
| 5 | 0-0 | 8.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 47.6% | 47.9% | 2.06 | -1.9% |
| Draw | 26.4% | 25.6% | 3.58 | -5.5% |
| Real Sociedad win | 26.0% | 26.5% | 3.50 | -9.0% |
| Over 2.5 | 44.0% | 51.4% | 1.87 | -17.7% |
| Under 2.5 | 56.0% | 48.6% | 1.97 | +10.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T20:00:00+00:00 |
| Fixture id | 3757bcd765c7da1538cdf2785e784038 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4428 |
| Dc lambda away | 0.9856 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.31 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 9.99 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.1656460544101335, "-10": 2.4371572509400225e-08, "-11": 2.160581883910188e-09, "-12": 1.7583481728094736e-10, "-13": 1.3170935828652374e-11, "-14": 8.417238275351233e-13, "-2": 0.0684254039016433, "-3": 0.020234502273276566, "-4": 0.00466834417780092, "-5": 0.0008798386656358345, "-6": 0.00013990423983063394, "-7": 1.9219478461896025e-05, "-8": 2.3226350560685374e-06, "-9": 2.504433146150575e-07, "0": 0.26389899946765727, "1": 0.24031877596400436, "10": 1.085860563332775e-06, "11": 1.4092088399392442e-07, "12": 1.6788953365339452e-08, "13": 1.840981828701044e-09, "14": 1.7223309631699654e-10, "2": 0.14454228647052209, "3": 0.06257259936522308, "4": 0.02113336517772144, "5": 0.005830730301162601, "6": 0.0013572657995800104, "7": 0.00027295417912166683, "8": 4.828844784771215e-05, "9": 7.622296388973688e-06} |
| Raw goal margin distribution | {"-1": 0.16243551380108742, "-10": 2.3899204341463022e-08, "-11": 2.1187056321505887e-09, "-12": 1.7242679875992095e-10, "-13": 1.2915657642355642e-11, "-14": 8.254095933112752e-13, "-2": 0.06709918735698187, "-3": 0.019842318520494007, "-4": 0.004577862647086497, "-5": 0.0008627856922010505, "-6": 0.00013719262532853508, "-7": 1.8846967831888358e-05, "-8": 2.277617900700387e-06, "-9": 2.455892392511799e-07, "0": 0.27139810882916926, "1": 0.23907726714050162, "10": 1.080250908135991e-06, "11": 1.4019287379084118e-07, "12": 1.670222009343078e-08, "13": 1.8314711478352973e-09, "14": 1.713433243550722e-10, "2": 0.1437955677703183, "3": 0.06224934358169221, "4": 0.02102418827619471, "5": 0.005800608214000162, "6": 0.001350254040056612, "7": 0.00027154407281419193, "8": 4.803898530016169e-05, "9": 7.582918907192234e-06} |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 25.5% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 77.3% |
| Raw p btts yes | 48.1% |
| P home draw | 74.0% |
| P draw away | 52.4% |
| P home away | 73.6% |
| Raw p home draw | 74.5% |
| Raw p draw away | 52.6% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.52, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.79, "price": 1.52, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.94 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market best over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market best under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.0049 |
| Raw ev home | -0.0243 |
| Raw edge prob draw | 0.0150 |
| Raw ev draw | -0.0284 |
| Raw edge prob away | -0.0101 |
| Raw ev away | -0.1076 |
| Elo home rating | 1,491.3653 |
| Elo away rating | 1,506.9598 |
| Elo rating diff | 44.4055 |
| Elo home expectancy | 0.5636 |

</details>


---

## 2026-11-01 — Elche CF vs Valencia

The model's most likely 1X2 outcome is **Elche CF win** at **40.9%**. Expected goals are 1.37 for Elche CF and 1.10 for Valencia (2.47 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 44.9%; Under 3.5 goals: 76.4%; Double Chance 1X: 68.2%; Double Chance X2: 59.1%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 40.9% | 2.44 |
| Draw | 27.3% | 3.66 |
| Valencia win | 31.8% | 3.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elche CF expected goals | 1.37 |
| Valencia expected goals | 1.10 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 44.9% |
| Under 2.5 | 55.1% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.96% |
| 2 | 1-0 | 10.84% |
| 3 | 0-1 | 9.59% |
| 4 | 0-0 | 8.68% |
| 5 | 2-1 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 40.9% | 39.3% | 2.48 | +1.4% |
| Draw | 27.3% | 27.1% | 3.37 | -8.0% |
| Valencia win | 31.8% | 33.5% | 2.86 | -9.1% |
| Over 2.5 | 44.9% | 48.6% | 1.97 | -11.6% |
| Under 2.5 | 55.1% | 51.4% | 1.87 | +3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T17:30:00+00:00 |
| Fixture id | 5262991e389930615bec34b642428c93 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Elche |
| Matched away-team name | Valencia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3658 |
| Dc lambda away | 1.1047 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.51 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.54 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.19174673915535104, "-10": 7.651087593423503e-08, "-11": 7.597808864805639e-09, "-12": 6.926758631262621e-10, "-13": 5.8099389585124716e-11, "-14": 4.1385014162561345e-12, "-2": 0.08780081237367922, "-3": 0.02893738506312506, "-4": 0.0074555020831575175, "-5": 0.00157090462778877, "-6": 0.00027945249359242054, "-7": 4.2967845909088385e-05, "-8": 5.8135515849026265e-06, "-9": 7.019791352049249e-07, "0": 0.27310999277505055, "1": 0.21620962023074036, "10": 5.804525680065555e-07, "11": 7.126295943888588e-08, "12": 8.032254704737211e-09, "13": 8.329346204880916e-10, "14": 7.335240867727791e-11, "2": 0.12203563927779797, "3": 0.049725522673439514, "4": 0.01583904148684807, "5": 0.004126042970825945, "6": 0.0009074523796404275, "7": 0.00017250089932515926, "8": 2.8855010665126372e-05, "9": 4.307604675743709e-06} |
| Raw goal margin distribution | {"-1": 0.18115461048815554, "-10": 7.228439966712803e-08, "-11": 7.178104365843712e-09, "-12": 6.544123082975682e-10, "-13": 5.4889967549151674e-11, "-14": 3.909889760676215e-12, "-2": 0.08295067773335645, "-3": 0.027338878057316364, "-4": 0.007043658639606865, "-5": 0.0014841275383074698, "-6": 0.00026401548130455376, "-7": 4.0594293407355566e-05, "-8": 5.492409819092585e-06, "-9": 6.632016657442678e-07, "0": 0.2747326631268447, "1": 0.22463225987323654, "10": 6.030646183152474e-07, "11": 7.403907192902851e-08, "12": 8.345158389700657e-09, "13": 8.653823355649856e-10, "14": 7.620991753621988e-11, "2": 0.12678964704156725, "3": 0.05166262500064487, "4": 0.016456065551660237, "5": 0.004286776674791722, "6": 0.0009428030008490497, "7": 0.00017922082654889593, "8": 2.9979083481374668e-05, "9": 4.47541127874038e-06} |
| Unadjusted home-win probability | 42.5% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 30.0% |
| Raw p over 1 5 | 70.9% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 50.1% |
| P home draw | 68.2% |
| P draw away | 59.1% |
| P home away | 72.7% |
| Raw p home draw | 70.0% |
| Raw p draw away | 57.5% |
| Raw p home away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.65 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market best over 2 5 last update utc | 2026-10-23T16:20:43Z |
| Market best under 2 5 last update utc | 2026-10-23T16:20:43Z |
| Home probability edge | +1.6% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | 0.0319 |
| Raw ev home | 0.0540 |
| Raw edge prob draw | 0.0032 |
| Raw ev draw | -0.0742 |
| Raw edge prob away | -0.0351 |
| Raw ev away | -0.1412 |
| Elo home rating | 1,460.0313 |
| Elo away rating | 1,451.1044 |
| Elo rating diff | 68.9269 |
| Elo home expectancy | 0.5979 |

</details>


---

## 2026-11-01 — Getafe vs Sevilla

The model's most likely 1X2 outcome is **Getafe win** at **35.4%**. Expected goals are 1.05 for Getafe and 0.90 for Sevilla (1.95 combined). The most likely exact score is 0-0 at 14.3%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 31.1%; Under 3.5 goals: 86.6%; Double Chance 1X: 66.6%; Double Chance X2: 64.6%; Double Chance 12 (either team wins): 68.8%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.7%; BTTS No (at least one team does not score): 61.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.4% | 2.83 |
| Draw | 31.2% | 3.21 |
| Sevilla win | 33.4% | 2.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 1.05 |
| Sevilla expected goals | 0.90 |
| Expected total goals | 1.95 |
| Over 0.5 | 85.7% |
| Under 0.5 | 14.3% |
| Over 1.5 | 58.3% |
| Under 1.5 | 41.7% |
| Over 2.5 | 31.1% |
| Under 2.5 | 68.9% |
| Over 3.5 | 13.4% |
| Under 3.5 | 86.6% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 14.26% |
| 2 | 0-1 | 13.91% |
| 3 | 1-0 | 13.58% |
| 4 | 1-1 | 13.48% |
| 5 | 2-0 | 7.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.4% | 32.5% | 3.00 | +6.1% |
| Draw | 31.2% | 30.6% | 3.00 | -6.4% |
| Sevilla win | 33.4% | 36.9% | 2.61 | -12.7% |

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
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 38.7% |
| P btts no | 61.3% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.01 |
| Fair Over 1.5 odds | 1.72 |
| Fair Under 1.5 odds | 2.40 |
| Fair Over 2.5 odds | 3.22 |
| Fair Under 2.5 odds | 1.45 |
| Fair Over 3.5 odds | 7.48 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.67 |
| Fair Under 4.5 odds | 1.05 |
| Goal margin distribution | {"-1": 0.21773655951497678, "-10": 1.595265124470306e-08, "-11": 1.290573198892818e-09, "-12": 9.559907191287433e-11, "-13": 6.144711722294364e-12, "-2": 0.08641467366072711, "-3": 0.024010617489148824, "-4": 0.005144436188887456, "-5": 0.0008946235636225743, "-6": 0.00013074782387824738, "-7": 1.6466898067827303e-05, "-8": 1.8212358644512025e-06, "-9": 1.7950403134898782e-07, "0": 0.3119706242538255, "1": 0.21239264556897372, "10": 6.655112596503179e-08, "11": 6.329051947836352e-09, "12": 5.511161984338473e-10, "13": 4.16413206176743e-11, "2": 0.09886491075949407, "3": 0.032291743573259715, "4": 0.0081331621750341, "5": 0.0016626294239229426, "6": 0.00028564266742106304, "7": 4.2289630382130747e-05, "8": 5.498215625717206e-06, "9": 6.370349527475697e-07} |
| Raw goal margin distribution | {"-1": 0.19503581085752583, "-10": 1.4289461897297824e-08, "-11": 1.1560207935578141e-09, "-12": 8.56321168539079e-11, "-13": 5.504077201885759e-12, "-2": 0.07740526434766741, "-3": 0.021507321791147904, "-4": 0.004608088259222497, "-5": 0.0008013520215991857, "-6": 0.00011711633500940355, "-7": 1.4750094444961664e-05, "-8": 1.6313577029842555e-06, "-9": 1.6078932442182022e-07, "0": 0.31785573576717235, "1": 0.22979192171094479, "10": 7.200301633121045e-08, "11": 6.847529987705783e-09, "12": 5.962638206463585e-10, "13": 4.505259144770866e-11, "2": 0.10696395711982173, "3": 0.03493709394323946, "4": 0.008799433524551694, "5": 0.0017988325791268597, "6": 0.00030904260970754995, "7": 4.5754010963621405e-05, "8": 5.948631277839619e-06, "9": 6.89221067879993e-07} |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 31.8% |
| Unadjusted away-win probability | 29.9% |
| Raw p over 1 5 | 58.3% |
| Raw p under 3 5 | 86.6% |
| Raw p btts yes | 38.9% |
| P home draw | 66.6% |
| P draw away | 64.6% |
| P home away | 68.8% |
| Raw p home draw | 70.1% |
| Raw p draw away | 61.7% |
| Raw p home away | 68.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.75 |
| Reference draw odds | 2.90 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:45Z |
| Market reference home last update utc | 2026-10-23T16:20:45Z |
| Market reference draw last update utc | 2026-10-23T16:20:45Z |
| Market reference away last update utc | 2026-10-23T16:20:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.50 |
| Reference Under 2.5 odds | 1.44 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:19Z |
| Home probability edge | +2.9% |
| Draw probability edge | +0.6% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0579 |
| Raw ev home | 0.1480 |
| Raw edge prob draw | 0.0118 |
| Raw ev draw | -0.0464 |
| Raw edge prob away | -0.0697 |
| Raw ev away | -0.2183 |
| Market p over 1 5 | 60.7% |
| Market reference over 1 5 odds | 1.63 |
| Market reference over 1 5 opposite odds | 2.49 |
| Market reference over 1 5 last update utc | 2026-10-23T16:20:43Z |
| Market over 1 5 bookmakers | 0 |
| Elo home rating | 1,456.2995 |
| Elo away rating | 1,476.0418 |
| Elo rating diff | 40.2576 |
| Elo home expectancy | 0.5577 |

</details>


---

## 2026-11-01 — Real Racing Club de Santander vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **79.8%**. Expected goals are 1.19 for Real Racing Club de Santander and 3.66 for Real Madrid (4.85 combined). The most likely exact score is 1-3 at 7.4%. Goal-market probabilities: at least one goal: 99.1%; Over 2.5 goals: 85.8%; Under 3.5 goals: 29.1%; Double Chance 1X: 20.2%; Double Chance X2: 91.0%; Double Chance 12 (either team wins): 88.8%; Under 4.5 goals: 47.3%; BTTS Yes (both teams score): 68.2%; BTTS No (at least one team does not score): 31.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 9.0% | 11.13 |
| Draw | 11.2% | 8.90 |
| Real Madrid win | 79.8% | 1.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.19 |
| Real Madrid expected goals | 3.66 |
| Expected total goals | 4.85 |
| Over 0.5 | 99.1% |
| Under 0.5 | 0.9% |
| Over 1.5 | 95.3% |
| Under 1.5 | 4.7% |
| Over 2.5 | 85.8% |
| Under 2.5 | 14.2% |
| Over 3.5 | 70.9% |
| Under 3.5 | 29.1% |
| Over 4.5 | 52.7% |
| Under 4.5 | 47.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-3 | 7.42% |
| 2 | 1-4 | 6.79% |
| 3 | 0-3 | 6.25% |
| 4 | 1-2 | 6.08% |
| 5 | 0-4 | 5.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 9.0% | 10.2% | 8.07 | -27.5% |
| Draw | 11.2% | 12.0% | 6.84 | -23.2% |
| Real Madrid win | 79.8% | 77.7% | 1.26 | +0.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:15:00+00:00 |
| Fixture id | 6c520ed959578ca3aebe351ee3765d53 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:20:43Z |
| Market best draw last update utc | 2026-10-23T16:20:43Z |
| Market best away last update utc | 2026-10-23T16:20:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santander |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1865 |
| Dc lambda away | 3.6608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:20:51.645253+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 68.2% |
| P btts no | 31.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 107.78 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.50 |
| Fair Over 2.5 odds | 1.17 |
| Fair Under 2.5 odds | 7.05 |
| Fair Over 3.5 odds | 1.41 |
| Fair Under 3.5 odds | 3.43 |
| Fair Over 4.5 odds | 1.90 |
| Fair Under 4.5 odds | 2.12 |
| Goal margin distribution | {"-1": 0.1520735499616736, "-10": 0.001344068830732945, "-11": 0.00043342272417493284, "-12": 0.0001287210277388878, "-13": 3.541945624621779e-05, "-14": 9.077242195492533e-06, "-15": 2.176556187748963e-06, "-16": 4.902764491309124e-07, "-17": 1.0411741425199831e-07, "-18": 2.0912548050540568e-08, "-19": 3.984007924597173e-09, "-2": 0.17983719030471693, "-20": 7.210902043100498e-10, "-21": 1.226490769615805e-10, "-22": 1.7043724068166673e-11, "-3": 0.1683272816367345, "-4": 0.12925593448864933, "-5": 0.08359615675434302, "-6": 0.04652229220313425, "-7": 0.022667506975769046, "-8": 0.00980729790662517, "-9": 0.003811986027986098, "0": 0.11231795249350274, "1": 0.05828018234532818, "10": 2.0542666957830505e-08, "11": 2.1471123345723925e-09, "12": 2.0668090848873978e-10, "13": 1.8433191154998384e-11, "14": 1.5311591510142097e-12, "15": 1.1899920713821098e-13, "16": 8.688063585986771e-15, "17": 5.980164168926864e-16, "18": 3.8931797729276914e-17, "19": 2.4039502406219423e-18, "2": 0.02256589864968849, "20": 1.4102712425969555e-19, "21": 7.774726354909595e-21, "22": 3.501814175868767e-22, "3": 0.006845976568391627, "4": 0.00170388062343054, "5": 0.0003571764017593664, "6": 6.442661660555174e-05, "7": 1.0174562688600712e-05, "8": 1.4268198262343926e-06, "9": 1.797541152449345e-07} |
| Raw goal margin distribution | {"-1": 0.1560432112753549, "-10": 0.0013791538145557735, "-11": 0.00044473660105267507, "-12": 0.00013208110504490933, "-13": 3.63440302122209e-05, "-14": 9.314190548361545e-06, "-15": 2.2333720567658833e-06, "-16": 5.030744107331404e-07, "-17": 1.0683524961219635e-07, "-18": 2.1458440041538698e-08, "-19": 4.088004721776293e-09, "-2": 0.18453158152063637, "-20": 7.399132270411266e-10, "-21": 1.258506547250759e-10, "-22": 1.7488625973142988e-11, "-3": 0.17272122324011577, "-4": 0.13262997476608498, "-5": 0.08577831420068255, "-6": 0.04773668973399416, "-7": 0.023259209645575783, "-8": 0.010063303313886912, "-9": 0.003911492440951428, "0": 0.1041499047300487, "1": 0.050067340188019276, "10": 1.7647794731536733e-08, "11": 1.8445413063390251e-09, "12": 1.7755543890305147e-10, "13": 1.583558621762056e-11, "14": 1.3153882333721366e-12, "15": 1.0222984119353874e-13, "16": 7.463741835214275e-15, "17": 5.137439551094098e-16, "18": 3.344552955399453e-17, "19": 2.0651856196866854e-18, "2": 0.019385912652912046, "20": 1.211535846646892e-19, "21": 6.679112068893885e-21, "22": 3.0083385906307883e-22, "3": 0.00588124168414426, "4": 0.0014637697992705356, "5": 0.00030684311020266324, "6": 5.5347619052393464e-05, "7": 8.74076351333405e-06, "8": 1.225752404201501e-06, "9": 1.5442316883701372e-07} |
| Unadjusted home-win probability | 7.7% |
| Unadjusted draw probability | 10.4% |
| Unadjusted away-win probability | 81.9% |
| Raw p over 1 5 | 95.5% |
| Raw p under 3 5 | 28.7% |
| Raw p btts yes | 67.8% |
| P home draw | 20.2% |
| P draw away | 91.0% |
| P home away | 88.8% |
| Raw p home draw | 18.1% |
| Raw p draw away | 92.3% |
| Raw p home away | 89.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.26, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.75, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:43Z", "line": 1.75, "market_key": "spreads", "opposite_price": 1.86, "price": 1.98, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 7.50 |
| Reference draw odds | 6.50 |
| Reference away odds | 1.25 |
| Market reference 1x2 last update utc | 2026-10-23T16:20:46Z |
| Market reference home last update utc | 2026-10-23T16:20:46Z |
| Market reference draw last update utc | 2026-10-23T16:20:46Z |
| Market reference away last update utc | 2026-10-23T16:20:46Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.00 |
| Market reference over 2 5 last update utc | 2026-10-23T16:20:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:20:19Z |
| Home probability edge | -1.3% |
| Draw probability edge | -0.8% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +6.2% |
| Under 2.5 probability edge | -6.2% |
| Raw edge prob home | -0.0253 |
| Raw ev home | -0.3772 |
| Raw edge prob draw | -0.0163 |
| Raw ev draw | -0.2876 |
| Raw edge prob away | 0.0417 |
| Raw ev away | 0.0315 |
| Elo home rating | 1,429.4672 |
| Elo away rating | 1,656.5478 |
| Elo rating diff | -167.0806 |
| Elo home expectancy | 0.2765 |

</details>


---
