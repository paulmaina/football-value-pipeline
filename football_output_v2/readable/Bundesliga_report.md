# Bundesliga — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,586 |
| Training data through | 2026-10-18 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 2eead5c4dfb5262d1a281063c18395ef90333836aa35d233ca6464c57bc3af47 |
| Training as of utc | 2026-10-23T16:21:43.479598+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 21, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-23T16:21:43.479598+00:00', 'observations': 131, 'observations_sha256': '435ee8cc5b0788f1317ee26813f165b239364f52405a96cac107c96bde9cdc63', 'eligible_training_matches': 18, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 61, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 18, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '727de9d4e01f3afdf1db23d4fb253804d2b01e5a2dbfa8fdac4c119389f6098b', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 4828.985 |
| Base scoring parameter | 0.233 |
| Home-advantage parameter | 0.236 |
| Dixon-Coles low-score adjustment | -0.111 |
| Xi per day | 0 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1586, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-18'} |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 16.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261023T162143479598Z_1095c4efa46b5ade95de6b80f458af70fad79a8d72c36261753021ff25ab45d2.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **65.6%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.46 combined). The most likely exact score is 2-1 at 11.1%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.7%; Under 3.5 goals: 53.7%; Double Chance 1X: 84.1%; Double Chance X2: 34.4%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 72.3%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 65.6% | 1.53 |
| Draw | 18.5% | 5.40 |
| Borussia Monchengladbach win | 15.9% | 6.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.17 |
| Borussia Monchengladbach expected goals | 1.29 |
| Expected total goals | 3.46 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.7% |
| Under 2.5 | 31.3% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.7% |
| Under 4.5 | 72.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.09% |
| 2 | 2-0 | 8.61% |
| 3 | 1-1 | 8.12% |
| 4 | 3-1 | 8.01% |
| 5 | 1-0 | 6.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 65.6% | 74.6% | 1.34 | -12.2% |
| Draw | 18.5% | 14.7% | 6.15 | +14.0% |
| Borussia Monchengladbach win | 15.9% | 10.7% | 7.93 | +26.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:30:00+00:00 |
| Fixture id | d4d56a31d8ccd432e3a6183180e093f3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1677 |
| Dc lambda away | 1.2877 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.17 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.96 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.60 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.09110587415920543, "-10": 1.0550283046891577e-07, "-11": 1.209927529262281e-08, "-12": 1.2758803719666845e-09, "-13": 1.2449767175943782e-10, "-14": 1.1302417454115736e-11, "-15": 9.586517474962234e-13, "-16": 7.555882695746718e-14, "-17": 4.916193071762927e-15, "-2": 0.04575548747384173, "-3": 0.016283129498774262, "-4": 0.004645773134237623, "-5": 0.0011002208265981203, "-6": 0.00022204753388552255, "-7": 3.897543211885077e-05, "-8": 6.046144575322597e-06, "-9": 8.3966912681938e-07, "0": 0.18531145616614358, "1": 0.24434103976731797, "10": 2.9738822998436228e-05, "11": 5.741183143762922e-06, "12": 1.0191412429925253e-06, "13": 1.6740484708419943e-07, "14": 2.558353310426819e-08, "15": 3.652854913946929e-09, "16": 4.846621891854611e-10, "17": 5.3084195646975404e-11, "2": 0.2000063699545035, "3": 0.11981767712471134, "4": 0.0575470936731935, "5": 0.022941807775872482, "6": 0.007794281863480752, "7": 0.0023030505464077446, "8": 0.0006014138657996599, "9": 0.0001406000490137598} |
| Raw goal margin distribution | {"-1": 0.12109308582221284, "-10": 1.402287549772434e-07, "-11": 1.6081713664651933e-08, "-12": 1.6958323797151963e-09, "-13": 1.6547568847961064e-10, "-14": 1.5022572577241704e-11, "-15": 1.2741889521889302e-12, "-16": 1.0042877697872144e-13, "-17": 6.53434254433752e-15, "-2": 0.060815762129946764, "-3": 0.02164267031128692, "-4": 0.006174914735702853, "-5": 0.0014623550479941313, "-6": 0.0002951337806212517, "-7": 5.1804072899606206e-05, "-8": 8.03621402801796e-06, "-9": 1.1160435764934487e-06, "0": 0.22360946233984072, "1": 0.2105394575128359, "10": 2.5624822040224787e-05, "11": 4.946960959651937e-06, "12": 8.78155567451684e-07, "13": 1.442464422828443e-07, "14": 2.2044365474435366e-08, "15": 3.1475272949966018e-09, "16": 4.176151271405817e-10, "17": 4.5740649072552336e-11, "2": 0.17233794482266537, "3": 0.10324237289940115, "4": 0.049586159962863044, "5": 0.019768090403870064, "6": 0.006716038684299923, "7": 0.0019844517856151917, "8": 0.0005182156430484921, "9": 0.0001211497588527269} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 65.1% |
| P home draw | 84.1% |
| P draw away | 34.4% |
| P home away | 81.5% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:12Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.67, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:12Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.14, "price": 6.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.55, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.55, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.29 |
| Reference draw odds | 5.30 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -9.1% |
| Draw probability edge | +3.8% |
| Away probability edge | +5.2% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.1814 |
| Raw ev home | -0.2431 |
| Raw edge prob draw | 0.0766 |
| Raw ev draw | 0.3752 |
| Raw edge prob away | 0.1048 |
| Raw ev away | 0.6776 |
| Market p home draw | 86.5% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:21:12Z |
| Market reference home draw last update utc | 2026-10-23T16:21:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 30.7% |
| Market draw away odds | 3.50 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:21:12Z |
| Market reference draw away last update utc | 2026-10-23T16:21:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.8% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:21:12Z |
| Market reference home away last update utc | 2026-10-23T16:21:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.10 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 92.4% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 9.00 |
| Market reference over 1 5 last update utc | 2026-10-23T16:21:26Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 43.1% |
| Market under 3 5 odds | 2.23 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 3 5 odds | 2.23 |
| Market reference under 3 5 opposite odds | 1.71 |
| Market reference under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.7% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:21:12Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.70 |
| Market reference btts yes last update utc | 2026-10-23T16:21:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,553.6374 |
| Elo away rating | 1,396.1351 |
| Elo rating diff | 217.5024 |
| Elo home expectancy | 0.7777 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.7%**. Expected goals are 1.76 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 50.4%; Under 3.5 goals: 72.0%; Double Chance 1X: 76.8%; Double Chance X2: 48.3%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.7% | 1.93 |
| Draw | 25.1% | 3.98 |
| FC Schalke 04 win | 23.2% | 4.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.76 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.01% |
| 2 | 1-0 | 9.96% |
| 3 | 2-0 | 9.76% |
| 4 | 2-1 | 9.09% |
| 5 | 0-0 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.7% | 47.8% | 2.08 | +7.5% |
| Draw | 25.1% | 24.4% | 3.85 | -3.3% |
| FC Schalke 04 win | 23.2% | 27.8% | 3.39 | -21.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 983440c6e348b558c6a3e10e2061ba55 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FC Koln |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7567 |
| Dc lambda away | 0.9314 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.81 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.44 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.148884816472071, "-10": 1.33477484256879e-08, "-11": 1.1164378883301118e-09, "-12": 8.57583539626523e-11, "-13": 6.089596408576425e-12, "-14": 4.019367869984875e-13, "-15": 2.467885057371439e-14, "-16": 1.303277448215753e-15, "-2": 0.06162036895196049, "-3": 0.016981764044215204, "-4": 0.0036688582083915476, "-5": 0.0006492830056718032, "-6": 9.710760285847952e-05, "-7": 1.2561234842757829e-05, "-8": 1.4304357032903052e-06, "-9": 1.4542144133716472e-07, "0": 0.25121387250895283, "1": 0.21892772970685112, "10": 5.65426490556508e-06, "11": 8.920361306885337e-07, "12": 1.2924211451675456e-07, "13": 1.7309952188995496e-08, "14": 2.1549879894212637e-09, "15": 2.495696474549639e-10, "16": 2.4858988708610507e-11, "2": 0.16295005682658478, "3": 0.08470182421159497, "4": 0.03451601340165374, "5": 0.011521352828757016, "6": 0.0032501425842565825, "7": 0.0007929782129625291, "8": 0.00017032445233284953, "9": 3.266004991591233e-05} |
| Raw goal margin distribution | {"-1": 0.11902097031633918, "-10": 1.0670409560949264e-08, "-11": 8.924988048858646e-10, "-12": 6.85566382337024e-11, "-13": 4.868123496794733e-12, "-14": 3.2131487634513584e-13, "-15": 1.9728678928965423e-14, "-16": 1.0418614211553237e-15, "-2": 0.04926033612896283, "-3": 0.013575501398457005, "-4": 0.002932945576742153, "-5": 0.0005190475105261231, "-6": 7.762941441028713e-05, "-7": 1.0041657670558357e-05, "-8": 1.1435138210529641e-06, "-9": 1.1625229128718276e-07, "0": 0.25871915407885654, "1": 0.23545239226633283, "10": 6.081048756617179e-06, "11": 9.593670077328975e-07, "12": 1.3899730785714584e-07, "13": 1.861650718423035e-08, "14": 2.3176464584631043e-09, "15": 2.6840716161913256e-10, "16": 2.673534489487255e-11, "2": 0.17524952527086668, "3": 0.09109511694405666, "4": 0.03712128170240581, "5": 0.012390984409822016, "6": 0.0034954633097167933, "7": 0.0008528321994985095, "8": 0.00018318054006644826, "9": 3.5125230113774634e-05} |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 76.8% |
| P draw away | 48.3% |
| P home away | 74.9% |
| Raw p home draw | 81.5% |
| Raw p draw away | 44.4% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.54, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.55, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.88, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.31, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.26, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.7, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.94 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.15 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:27Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:27Z |
| Home probability edge | +3.9% |
| Draw probability edge | +0.8% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | 0.0780 |
| Raw ev home | 0.1562 |
| Raw edge prob draw | 0.0150 |
| Raw ev draw | -0.0039 |
| Raw edge prob away | -0.0930 |
| Raw ev away | -0.3715 |
| Market p home draw | 71.8% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:21:42Z |
| Market reference home draw last update utc | 2026-10-23T16:21:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.6% |
| Market draw away odds | 1.80 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:21:42Z |
| Market reference draw away last update utc | 2026-10-23T16:21:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:21:42Z |
| Market reference home away last update utc | 2026-10-23T16:21:49Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.81 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.39 |
| Market reference over 1 5 last update utc | 2026-10-23T16:21:50Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.1% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.58 |
| Market reference under 3 5 last update utc | 2026-10-23T16:21:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.3% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:21:42Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.52 |
| Market reference btts yes last update utc | 2026-10-23T16:21:51Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,415.8199 |
| Elo away rating | 1,439.3959 |
| Elo rating diff | 36.4240 |
| Elo home expectancy | 0.5522 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **46.9%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 46.9%; Under 3.5 goals: 75.4%; Double Chance 1X: 73.2%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 46.9% | 2.13 |
| Draw | 26.3% | 3.80 |
| Union Berlin win | 26.8% | 3.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.34 |
| Union Berlin expected goals | 1.16 |
| Expected total goals | 2.50 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 46.9% |
| Under 2.5 | 53.1% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.55% |
| 2 | 1-0 | 11.39% |
| 3 | 2-1 | 10.15% |
| 4 | 2-0 | 8.78% |
| 5 | 0-0 | 8.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 46.9% | 54.2% | 1.86 | -12.7% |
| Draw | 26.3% | 22.9% | 4.12 | +8.3% |
| Union Berlin win | 26.8% | 22.9% | 3.90 | +4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04bb232a2940fcf03abf05b308e27577 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3432 |
| Dc lambda away | 1.1566 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.73 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.13 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.85 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.1538327874101125, "-10": 9.728427821849812e-08, "-11": 1.0110791321010756e-08, "-12": 9.647588577784172e-10, "-13": 8.467533477867303e-11, "-14": 6.296503796126417e-12, "-2": 0.078071565304602, "-3": 0.026860528663563914, "-4": 0.0072315238971294585, "-5": 0.0015931166996888775, "-6": 0.00029641661814220336, "-7": 4.7679801429511203e-05, "-8": 6.7498972677479105e-06, "-9": 8.528912157637284e-07, "0": 0.26287774057589963, "1": 0.24536748874167316, "10": 5.897306358140426e-07, "11": 7.118019527057583e-08, "12": 7.887798406068201e-09, "13": 8.040016683942299e-10, "14": 6.943245108147159e-11, "2": 0.14302103525762733, "3": 0.0571458354506608, "4": 0.017867461527487687, "5": 0.004571341010593383, "6": 0.0009877830679859043, "7": 0.00018452553246633312, "8": 3.0337667829731065e-05, "9": 4.451861760250999e-06} |
| Raw goal margin distribution | {"-1": 0.17631742886167256, "-10": 1.1150362736664307e-07, "-11": 1.1588613581608547e-08, "-12": 1.1057707796812139e-09, "-13": 9.705172458700151e-11, "-14": 7.216818851439408e-12, "-2": 0.08948272922478871, "-3": 0.030786540577977705, "-4": 0.008288504172354293, "-5": 0.0018259712061049933, "-6": 0.0003397417212715075, "-7": 5.464881796800803e-05, "-8": 7.736481613356665e-06, "-9": 9.775522422359816e-07, "0": 0.29697722480216837, "1": 0.20705337873893667, "10": 4.976442531867526e-07, "11": 6.006541455696486e-08, "12": 6.6561194360491426e-09, "13": 6.784568844327663e-10, "14": 5.859058045656631e-11, "2": 0.12068831422083529, "3": 0.04822251868655589, "4": 0.015077459111338093, "5": 0.0038575265470794625, "6": 0.000833540835978153, "7": 0.0001557118881425248, "8": 2.5600443886918706e-05, "9": 3.7567039703010403e-06} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 52.1% |
| P home draw | 73.2% |
| P draw away | 53.1% |
| P home away | 73.7% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.5, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.85, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.58, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.9, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:50Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.97, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.42, "price": 2.97, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.73 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -7.3% |
| Draw probability edge | +3.4% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -16.9% |
| Under 2.5 probability edge | +16.9% |
| Raw edge prob home | -0.1465 |
| Raw ev home | -0.2636 |
| Raw edge prob draw | 0.0682 |
| Raw ev draw | 0.2235 |
| Raw edge prob away | 0.0783 |
| Raw ev away | 0.1977 |
| Market p home draw | 75.1% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:21:42Z |
| Market reference home draw last update utc | 2026-10-23T16:21:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.0% |
| Market draw away odds | 2.00 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:21:42Z |
| Market reference draw away last update utc | 2026-10-23T16:21:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.9% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:21:42Z |
| Market reference home away last update utc | 2026-10-23T16:21:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.02 |
| Market reference dc home draw odds | 1.29 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-23T16:21:26Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.5% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.21 |
| Market reference under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.7% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:21:42Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.76 |
| Market reference btts yes last update utc | 2026-10-23T16:21:51Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,477.3863 |
| Elo away rating | 1,413.5523 |
| Elo rating diff | 123.8339 |
| Elo home expectancy | 0.6710 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **64.9%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.9%; Under 3.5 goals: 50.3%; Double Chance 1X: 84.1%; Double Chance X2: 35.1%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 64.9% | 1.54 |
| Draw | 19.2% | 5.21 |
| Eintracht Frankfurt win | 15.9% | 6.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.42 |
| Eintracht Frankfurt expected goals | 1.22 |
| Expected total goals | 3.64 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 70.9% |
| Under 2.5 | 29.1% |
| Over 3.5 | 49.7% |
| Under 3.5 | 50.3% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.66% |
| 2 | 1-1 | 8.22% |
| 3 | 2-0 | 7.90% |
| 4 | 3-1 | 7.79% |
| 5 | 3-0 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 64.9% | 66.8% | 1.51 | -2.1% |
| Draw | 19.2% | 18.3% | 4.90 | -5.9% |
| Eintracht Frankfurt win | 15.9% | 14.9% | 5.80 | -7.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 3ed4d1e775910625c50518a384e9c547 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4206 |
| Dc lambda away | 1.2230 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.10 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.96 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.43 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.28 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.09464004087257895, "-10": 6.611008704376499e-08, "-11": 7.191882692567449e-09, "-12": 7.195318359799437e-10, "-13": 6.66223688448964e-11, "-14": 5.739976318317795e-12, "-15": 4.623427389591346e-13, "-16": 3.4941643168162074e-14, "-17": 2.4629842044630753e-15, "-18": 1.4370992950782747e-16, "-2": 0.044695831186203884, "-3": 0.014968765406111995, "-4": 0.0040305790161044375, "-5": 0.0009024229265344458, "-6": 0.00017238074387137208, "-7": 2.8660234406100294e-05, "-8": 4.213553441060695e-06, "-9": 5.547927215471571e-07, "0": 0.19200792267295347, "1": 0.2143272364636466, "10": 6.696411109028494e-05, "11": 1.4418540041009168e-05, "12": 2.8551768964303015e-06, "13": 5.232477754753437e-07, "14": 8.922811829507505e-08, "15": 1.4225252662253923e-08, "16": 2.1278626195327172e-09, "17": 2.9686992401156503e-10, "18": 3.4284329838361136e-11, "2": 0.19222368040595528, "3": 0.12741781865960963, "4": 0.06790721771411384, "5": 0.030092823042558038, "6": 0.011377474614375873, "7": 0.0037440460042187343, "8": 0.0010894674477403216, "9": 0.0002839231602997437} |
| Raw goal margin distribution | {"-1": 0.10080770032947975, "-10": 7.041845905832263e-08, "-11": 7.660575255385084e-09, "-12": 7.664234823888657e-10, "-13": 7.096412609118278e-11, "-14": 6.114048633752696e-12, "-15": 4.924734588952132e-13, "-16": 3.7218778236350834e-14, "-17": 2.623496052099601e-15, "-18": 1.5307545701190858e-16, "-2": 0.047608643388713234, "-3": 0.015944274785270406, "-4": 0.004293250487463291, "-5": 0.0009612335234619974, "-6": 0.00018361473865120646, "-7": 3.052801218960497e-05, "-8": 4.488149293812958e-06, "-9": 5.909483755823983e-07, "0": 0.20090571954349726, "1": 0.20795286575766644, "10": 6.497251135182465e-05, "11": 1.3989713911503223e-05, "12": 2.770260222892714e-06, "13": 5.076857062442357e-07, "14": 8.657435803205623e-08, "15": 1.3802175150727208e-08, "16": 2.0645772183298693e-09, "17": 2.880406264461721e-10, "18": 3.3264669288439014e-11, "2": 0.1865066981987814, "3": 0.12362824704899696, "4": 0.06588756875832241, "5": 0.0291978233550346, "6": 0.011039093725009946, "7": 0.0036326932076030704, "8": 0.0010570652691904534, "9": 0.0002754789163220495} |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.2% |
| P home draw | 84.1% |
| P draw away | 35.1% |
| P home away | 80.8% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.1% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 6.5, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.65, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.22, "price": 4.65, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.43 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.40 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -1.9% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0386 |
| Raw ev home | -0.0498 |
| Raw edge prob draw | 0.0178 |
| Raw ev draw | -0.0156 |
| Raw edge prob away | 0.0208 |
| Raw ev away | -0.0150 |
| Market p home draw | 82.9% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:21:42Z |
| Market reference home draw last update utc | 2026-10-23T16:21:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.3% |
| Market draw away odds | 2.69 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:21:42Z |
| Market reference draw away last update utc | 2026-10-23T16:21:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.8% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:21:42Z |
| Market reference home away last update utc | 2026-10-23T16:21:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.67 |
| Market reference dc home draw odds | 1.17 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 89.6% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.10 |
| Market reference over 1 5 last update utc | 2026-10-23T16:21:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 49.0% |
| Market under 3 5 odds | 1.92 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 1.87 |
| Market reference under 3 5 last update utc | 2026-10-23T16:21:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.4% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:21:42Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.72 |
| Market reference btts yes last update utc | 2026-10-23T16:21:51Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,632.7906 |
| Elo away rating | 1,482.9718 |
| Elo rating diff | 209.8188 |
| Elo home expectancy | 0.7699 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **53.5%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.8%; Double Chance 1X: 77.8%; Double Chance X2: 46.5%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 53.5% | 1.87 |
| Draw | 24.3% | 4.11 |
| Werder Bremen win | 22.2% | 4.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.73 |
| Werder Bremen expected goals | 1.16 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.50% |
| 2 | 2-1 | 10.43% |
| 3 | 1-0 | 9.05% |
| 4 | 2-0 | 8.98% |
| 5 | 0-0 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 53.5% | 57.5% | 1.77 | -5.4% |
| Draw | 24.3% | 22.4% | 4.04 | -1.7% |
| Werder Bremen win | 22.2% | 20.1% | 4.48 | -0.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 4e5820453145833132980b8d190998c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7299 |
| Dc lambda away | 1.1608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.86 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.97 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.87 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.12998140534007058, "-10": 7.43396376115471e-08, "-11": 7.728770649518615e-09, "-12": 7.382303594897682e-10, "-13": 6.520501795097247e-11, "-14": 5.3541048194691925e-12, "-15": 4.082546285193016e-13, "-16": 2.631612716288876e-14, "-2": 0.06355466115661579, "-3": 0.02132990441367022, "-4": 0.005656194202881185, "-5": 0.0012341809125153804, "-6": 0.00022822927603470414, "-7": 3.657045826815719e-05, "-8": 5.165406692432509e-06, "-9": 6.519344972836587e-07, "0": 0.2432454491772947, "1": 0.2361289872914117, "10": 4.759787555366798e-06, "11": 7.374608770364576e-07, "12": 1.0497403799141012e-07, "13": 1.3817594927686645e-08, "14": 1.6908292165052042e-09, "15": 1.9213453234834038e-10, "16": 1.8456855960764198e-11, "2": 0.1672719221933876, "3": 0.08366156520102914, "4": 0.03306152063799577, "5": 0.010750750277439738, "6": 0.002962734518170779, "7": 0.0007074784627725053, "8": 0.0001489185428391879, "9": 2.8009777295170756e-05} |
| Raw goal margin distribution | {"-1": 0.14247951988054522, "-10": 8.148762392032469e-08, "-11": 8.471915875422432e-09, "-12": 8.092134940852101e-10, "-13": 7.14746822989831e-11, "-14": 5.868918573947074e-12, "-15": 4.4750957499078877e-13, "-16": 2.8846504263236096e-14, "-2": 0.06966563858941299, "-3": 0.023380840759541863, "-4": 0.006200054786830303, "-5": 0.001352851228226527, "-6": 0.0002501742275137907, "-7": 4.008682105125885e-05, "-8": 5.66207653779426e-06, "-9": 7.146200175595814e-07, "0": 0.26202794363322474, "1": 0.21840760258666184, "10": 4.402567430260184e-06, "11": 6.821147373838244e-07, "12": 9.709577902542813e-08, "13": 1.2780590033807435e-08, "14": 1.5639331697325114e-09, "15": 1.7771491363964666e-10, "16": 1.7071676408381667e-11, "2": 0.15471823229070014, "3": 0.07738279867204197, "4": 0.03058026692632469, "5": 0.009943910830421385, "6": 0.002740382494487426, "7": 0.0006543824911472857, "8": 0.0001377422666115381, "9": 2.590765487201605e-05} |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 24.3% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.7% |
| P home draw | 77.8% |
| P draw away | 46.5% |
| P home away | 75.7% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.93, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:43Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:43Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.0, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.45, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.17, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 9.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.64 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -4.0% |
| Draw probability edge | +1.9% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.0803 |
| Raw ev home | -0.1246 |
| Raw edge prob draw | 0.0376 |
| Raw ev draw | 0.0586 |
| Raw edge prob away | 0.0427 |
| Raw ev away | 0.0903 |
| Market p home draw | 77.6% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:21:43Z |
| Market reference home draw last update utc | 2026-10-23T16:21:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.5% |
| Market draw away odds | 2.14 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:21:43Z |
| Market reference draw away last update utc | 2026-10-23T16:21:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.9% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:21:43Z |
| Market reference home away last update utc | 2026-10-23T16:21:49Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.13 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 84.0% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.74 |
| Market reference over 1 5 last update utc | 2026-10-23T16:21:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.0% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.45 |
| Market reference under 3 5 last update utc | 2026-10-23T16:21:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:21:43Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.37 |
| Market reference btts yes last update utc | 2026-10-23T16:21:49Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,456.9980 |
| Elo away rating | 1,456.2478 |
| Elo rating diff | 60.7502 |
| Elo home expectancy | 0.5865 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **67.9%**. Expected goals are 2.69 for RB Leipzig and 1.32 for Elversberg (4.01 combined). The most likely exact score is 2-1 at 9.0%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 76.7%; Under 3.5 goals: 42.9%; Double Chance 1X: 85.3%; Double Chance X2: 32.1%; Double Chance 12 (either team wins): 82.6%; Under 4.5 goals: 62.4%; BTTS Yes (both teams score): 68.7%; BTTS No (at least one team does not score): 31.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 67.9% | 1.47 |
| Draw | 17.4% | 5.75 |
| Elversberg win | 14.7% | 6.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.69 |
| Elversberg expected goals | 1.32 |
| Expected total goals | 4.01 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 91.7% |
| Under 1.5 | 8.3% |
| Over 2.5 | 76.7% |
| Under 2.5 | 23.3% |
| Over 3.5 | 57.1% |
| Under 3.5 | 42.9% |
| Over 4.5 | 37.6% |
| Under 4.5 | 62.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.97% |
| 2 | 3-1 | 8.03% |
| 3 | 1-1 | 6.82% |
| 4 | 2-0 | 6.79% |
| 5 | 3-0 | 6.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 67.9% | 70.2% | 1.45 | -1.5% |
| Draw | 17.4% | 16.5% | 5.15 | -10.5% |
| Elversberg win | 14.7% | 13.3% | 6.48 | -4.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04dac5e98ab5fc5564980542ca3fc746 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6856 |
| Dc lambda away | 1.3212 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 68.7% |
| P btts no | 31.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.44 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.10 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.29 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.33 |
| Fair Over 4.5 odds | 2.66 |
| Fair Under 4.5 odds | 1.60 |
| Goal margin distribution | {"-1": 0.08550488275074494, "-10": 1.0199602688652237e-07, "-11": 1.1937201445512453e-08, "-12": 1.2856399232341955e-09, "-13": 1.282066007720918e-10, "-14": 1.1901268666515087e-11, "-15": 1.0332176225314903e-12, "-16": 8.423073551832528e-14, "-17": 6.466426249848148e-15, "-18": 4.63413147346212e-16, "-19": 2.7154197309977882e-17, "-2": 0.041333620159716075, "-3": 0.01450591897097512, "-4": 0.004130932873492919, "-5": 0.0009838175971784726, "-6": 0.00020065867482594514, "-7": 3.5713826519591194e-05, "-8": 5.631051102199952e-06, "-9": 7.962318877463715e-07, "0": 0.17381643578150766, "1": 0.20469925677640066, "10": 0.0001392187899606787, "11": 3.311920998917417e-05, "12": 7.2503611870225954e-06, "13": 1.4696486615991819e-06, "14": 2.773059851803237e-07, "15": 4.8935117415876225e-08, "16": 8.108906052872536e-09, "17": 1.265373836575709e-09, "18": 1.8432562646766108e-10, "19": 2.195417810401576e-11, "2": 0.19360442368125313, "3": 0.13810834637735672, "4": 0.07994396089731234, "5": 0.03870035567728288, "6": 0.016044314109469705, "7": 0.005804468340274233, "8": 0.0018602802555475442, "9": 0.0005346767755908021} |
| Raw goal margin distribution | {"-1": 0.09366787776734993, "-10": 1.1173340131945716e-07, "-11": 1.307682426911172e-08, "-12": 1.4083776190111982e-09, "-13": 1.404462508310159e-10, "-14": 1.3037461053319963e-11, "-15": 1.1318570222062367e-12, "-16": 9.227209002535867e-14, "-17": 7.083764155645046e-15, "-18": 5.076543542892553e-16, "-19": 2.9746558941154174e-17, "-2": 0.04527966539745505, "-3": 0.015890772566021002, "-4": 0.004525305491470209, "-5": 0.0010777408666416569, "-6": 0.000219815192090785, "-7": 3.912336032075624e-05, "-8": 6.168637268121056e-06, "-9": 8.722466920784549e-07, "0": 0.18270709418023948, "1": 0.1978016410411469, "10": 0.00013452762629258242, "11": 3.200321383189434e-05, "12": 7.00605055200887e-06, "13": 1.4201268807525901e-06, "14": 2.679617884451631e-07, "15": 4.728618306599268e-08, "16": 7.835665598232857e-09, "17": 1.2227353696677566e-09, "18": 1.7811452750445067e-10, "19": 2.121440265622195e-11, "2": 0.18708066321319608, "3": 0.1334546005936927, "4": 0.07725014201732419, "5": 0.037396295337820434, "6": 0.0155036794476462, "7": 0.005608879002095095, "8": 0.0017975956197324625, "9": 0.000516660125219578} |
| Unadjusted home-win probability | 65.7% |
| Unadjusted draw probability | 18.3% |
| Unadjusted away-win probability | 16.1% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 43.2% |
| Raw p btts yes | 69.0% |
| P home draw | 85.3% |
| P draw away | 32.1% |
| P home away | 82.6% |
| Raw p home draw | 83.9% |
| Raw p draw away | 34.3% |
| Raw p home away | 81.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.25, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.18, "price": 5.25, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.36 |
| Reference draw odds | 4.80 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.0458 |
| Raw ev home | -0.0480 |
| Raw edge prob draw | 0.0178 |
| Raw ev draw | -0.0591 |
| Raw edge prob away | 0.0280 |
| Raw ev away | 0.0414 |
| Market p home draw | 84.2% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:21:42Z |
| Market reference home draw last update utc | 2026-10-23T16:21:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.8% |
| Market draw away odds | 2.91 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:21:42Z |
| Market reference draw away last update utc | 2026-10-23T16:21:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.0% |
| Market home away odds | 1.19 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:21:42Z |
| Market reference home away last update utc | 2026-10-23T16:21:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.86 |
| Market reference dc home draw odds | 1.15 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 92.2% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 8.50 |
| Market reference over 1 5 last update utc | 2026-10-23T16:21:26Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 44.0% |
| Market under 3 5 odds | 2.17 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 3 5 odds | 2.17 |
| Market reference under 3 5 opposite odds | 1.73 |
| Market reference under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.7% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:21:42Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.90 |
| Market reference btts yes last update utc | 2026-10-23T16:21:51Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,582.0473 |
| Elo away rating | 1,431.9590 |
| Elo rating diff | 210.0883 |
| Elo home expectancy | 0.7702 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **38.3%**. Expected goals are 1.02 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 86.7%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.9%; Double Chance 1X: 68.0%; Double Chance X2: 61.7%; Double Chance 12 (either team wins): 70.4%; Under 4.5 goals: 94.7%; BTTS Yes (both teams score): 40.0%; BTTS No (at least one team does not score): 60.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 38.3% | 2.61 |
| Draw | 29.6% | 3.37 |
| Hamburger SV win | 32.0% | 3.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.02 |
| Hamburger SV expected goals | 0.96 |
| Expected total goals | 1.98 |
| Over 0.5 | 86.7% |
| Under 0.5 | 13.3% |
| Over 1.5 | 60.7% |
| Under 1.5 | 39.3% |
| Over 2.5 | 33.2% |
| Under 2.5 | 66.8% |
| Over 3.5 | 14.1% |
| Under 3.5 | 85.9% |
| Over 4.5 | 5.3% |
| Under 4.5 | 94.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.98% |
| 2 | 0-0 | 13.34% |
| 3 | 1-1 | 13.09% |
| 4 | 0-1 | 11.97% |
| 5 | 2-0 | 7.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 38.3% | 42.3% | 2.23 | -14.6% |
| Draw | 29.6% | 25.2% | 3.64 | +7.9% |
| Hamburger SV win | 32.0% | 32.5% | 3.22 | +3.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 7630f897583f3acc0f483fa2d17d1ac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0157 |
| Dc lambda away | 0.9634 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 40.0% |
| P btts no | 60.0% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.49 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.54 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 7.08 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.71 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.1974844279502257, "-10": 2.905060512405589e-08, "-11": 2.525456341143646e-09, "-12": 2.0099974119803193e-10, "-13": 1.385247203952151e-11, "-2": 0.08899883792891158, "-3": 0.026515322592819905, "-4": 0.006096937348132996, "-5": 0.001138421100825329, "-6": 0.0001786942524891611, "-7": 2.4175855833882127e-05, "-8": 2.8726646473873188e-06, "-9": 3.04214902808042e-07, "0": 0.29642397798485687, "1": 0.2299106180410778, "10": 5.424814797018334e-08, "11": 4.972349001181254e-09, "12": 4.1726239096462604e-10, "13": 3.032026773614814e-11, "2": 0.10881230841979211, "3": 0.034180830340803235, "4": 0.008286849113301084, "5": 0.0016314457674540912, "6": 0.00027000530328842435, "7": 3.851550292445062e-05, "8": 4.825370349868295e-06, "9": 5.38788369785692e-07} |
| Raw goal margin distribution | {"-1": 0.19477018188466563, "-10": 2.8651330652248012e-08, "-11": 2.4907462123054344e-09, "-12": 1.9823718030962177e-10, "-13": 1.3662082254758185e-11, "-2": 0.08777562884759176, "-3": 0.02615089330200637, "-4": 0.006013140421049169, "-5": 0.001122774525417143, "-6": 0.00017623826050644563, "-7": 2.384358041217039e-05, "-8": 2.8331824522705996e-06, "-9": 3.000337422395764e-07, "0": 0.3403801645156232, "1": 0.20617640647878635, "10": 4.8647984603405825e-08, "11": 4.4590417683047845e-09, "12": 3.741874170964223e-10, "13": 2.7190235486195754e-11, "2": 0.0975793589778693, "3": 0.030652263171545888, "4": 0.007431378271129132, "5": 0.0014630277999540336, "6": 0.0002421320234643357, "7": 3.453945735236817e-05, "8": 4.3272360673980525e-06, "9": 4.831679845040041e-07} |
| Unadjusted home-win probability | 34.4% |
| Unadjusted draw probability | 34.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 86.1% |
| Raw p btts yes | 40.9% |
| P home draw | 68.0% |
| P draw away | 61.7% |
| P home away | 70.4% |
| Raw p home draw | 68.4% |
| Raw p draw away | 65.6% |
| Raw p home away | 66.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.71, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.34, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.64, "price": 2.34, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.17 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.75 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:27Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:27Z |
| Home probability edge | -4.0% |
| Draw probability edge | +4.4% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -29.0% |
| Under 2.5 probability edge | +29.0% |
| Raw edge prob home | -0.0791 |
| Raw ev home | -0.2338 |
| Raw edge prob draw | 0.0879 |
| Raw ev draw | 0.2390 |
| Raw edge prob away | -0.0088 |
| Raw ev away | 0.0176 |
| Market p home draw | 68.8% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:21:42Z |
| Market reference home draw last update utc | 2026-10-23T16:21:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.1% |
| Market draw away odds | 1.70 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:21:42Z |
| Market reference draw away last update utc | 2026-10-23T16:21:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:21:42Z |
| Market reference home away last update utc | 2026-10-23T16:21:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home draw odds | 1.41 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 82.2% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-23T16:21:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.4% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-23T16:21:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.1% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:21:42Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.66 |
| Market reference btts yes last update utc | 2026-10-23T16:21:51Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,397.1739 |
| Elo away rating | 1,419.8287 |
| Elo rating diff | 37.3451 |
| Elo home expectancy | 0.5535 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **67.6%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 10.0%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 72.2%; Under 3.5 goals: 49.1%; Double Chance 1X: 32.4%; Double Chance X2: 85.4%; Double Chance 12 (either team wins): 82.3%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 14.6% | 6.83 |
| Draw | 17.7% | 5.64 |
| Bayern Munich win | 67.6% | 1.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.24 |
| Bayern Munich expected goals | 2.45 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 72.2% |
| Under 2.5 | 27.8% |
| Over 3.5 | 50.9% |
| Under 3.5 | 49.1% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.97% |
| 2 | 1-3 | 8.13% |
| 3 | 0-2 | 8.06% |
| 4 | 1-1 | 7.52% |
| 5 | 0-3 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 14.6% | 12.3% | 6.90 | +1.0% |
| Draw | 17.7% | 15.5% | 6.14 | +8.8% |
| Bayern Munich win | 67.6% | 72.2% | 1.37 | -7.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | f2bd909f25eea6b4ce42d2f52275e5c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Freiburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2379 |
| Dc lambda away | 2.4469 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.50 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.42 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.46 |
| Goal margin distribution | {"-1": 0.2216740276467751, "-10": 7.491134445206658e-05, "-11": 1.6296811135660068e-05, "-12": 3.2607790636638038e-06, "-13": 6.038479348935209e-07, "-14": 1.0405760435306664e-07, "-15": 1.6764839642084557e-08, "-16": 2.534236953759825e-09, "-17": 3.571585831218135e-10, "-18": 4.155870940722439e-11, "-2": 0.19975212933937958, "-3": 0.133356201360749, "-4": 0.0716616913599091, "-5": 0.03204236480529324, "-6": 0.012229104222739538, "-7": 0.004063598739918253, "-8": 0.0011942610610586322, "-9": 0.0003143910623610221, "0": 0.17718477849802364, "1": 0.08660034657191852, "10": 6.614677601691094e-08, "11": 7.279737776184698e-09, "12": 7.36862559824361e-10, "13": 6.903108750343264e-11, "14": 6.0178722806312915e-12, "15": 4.904791608232303e-13, "16": 3.750769614386881e-14, "17": 2.6741531402671258e-15, "18": 1.5741251159844173e-16, "2": 0.0411184184142549, "3": 0.013887056850185786, "4": 0.003775166101524061, "5": 0.0008539365142747514, "6": 0.00016487229500729278, "7": 2.7715062816801356e-05, "8": 4.120560887579402e-06, "9": 5.48755982654696e-07} |
| Raw goal margin distribution | {"-1": 0.20680523235280385, "-10": 6.988666268091749e-05, "-11": 1.520370180168453e-05, "-12": 3.0420621624951177e-06, "-13": 5.633448077210144e-07, "-14": 9.707793589875318e-08, "-15": 1.5640337275160398e-08, "-16": 2.364252897026238e-09, "-17": 3.332021552249691e-10, "-18": 3.877115711967228e-11, "-2": 0.18635374635238058, "-3": 0.12441132820504425, "-4": 0.06685498021489361, "-5": 0.029893121756469226, "-6": 0.011408836511421131, "-7": 0.0037910326731485314, "-8": 0.0011141559471084458, "-9": 0.000293303267827199, "0": 0.199144464699278, "1": 0.10044432001477645, "10": 7.672103174172265e-08, "11": 8.443480191011825e-09, "12": 8.546577663455393e-10, "13": 8.00664306626598e-11, "14": 6.979892264770541e-12, "15": 5.688873975740271e-13, "16": 4.350369465742304e-14, "17": 3.1016445594296193e-15, "18": 1.8257655211798667e-16, "2": 0.04769162874276702, "3": 0.016107048499685386, "4": 0.004378665987156432, "5": 0.0009904472199875585, "6": 0.0001912288601239055, "7": 3.2145606212886955e-05, "8": 4.7792757513814155e-06, "9": 6.364803804337744e-07} |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 32.4% |
| P draw away | 85.4% |
| P home away | 82.3% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 6.25 |
| Reference draw odds | 5.10 |
| Reference away odds | 1.33 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.90 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | +2.3% |
| Draw probability edge | +2.2% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.0468 |
| Raw ev home | 0.1719 |
| Raw edge prob draw | 0.0439 |
| Raw ev draw | 0.2227 |
| Raw edge prob away | -0.0907 |
| Raw ev away | -0.1355 |
| Elo home rating | 1,530.2552 |
| Elo away rating | 1,716.3142 |
| Elo rating diff | -126.0590 |
| Elo home expectancy | 0.3261 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **47.1%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 70.5%; Under 3.5 goals: 50.6%; Double Chance 1X: 52.9%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 70.0%; BTTS No (at least one team does not score): 30.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 29.8% | 3.36 |
| Draw | 23.1% | 4.33 |
| Bayer Leverkusen win | 47.1% | 2.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.50 |
| Bayer Leverkusen expected goals | 2.16 |
| Expected total goals | 3.66 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 49.4% |
| Under 3.5 | 50.6% |
| Over 4.5 | 30.2% |
| Under 4.5 | 69.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.51% |
| 2 | 1-2 | 8.19% |
| 3 | 2-1 | 7.25% |
| 4 | 2-2 | 6.93% |
| 5 | 1-3 | 5.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 29.8% | 33.8% | 2.81 | -16.3% |
| Draw | 23.1% | 23.7% | 4.06 | -6.2% |
| Bayer Leverkusen win | 47.1% | 42.5% | 2.32 | +9.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:30:00+00:00 |
| Fixture id | 2fd479cbb110c8f057e363bb06195f2b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5009 |
| Dc lambda away | 2.1591 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 70.0% |
| P btts no | 30.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.84 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.93 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.18242798218797857, "-10": 1.901013092483008e-05, "-11": 3.643701554531962e-06, "-12": 6.424805556748931e-07, "-13": 1.0486732443237942e-07, "-14": 1.5929501543601523e-08, "-15": 2.260590487457881e-09, "-16": 2.972600590056123e-10, "-17": 3.170932249188684e-11, "-2": 0.14336729116884764, "-3": 0.08352106503479823, "-4": 0.03929766958943104, "-5": 0.015417632213261739, "-6": 0.0051701102615584835, "-7": 0.0015109027394140878, "-8": 0.00039078227686918887, "-9": 9.05789461980555e-05, "0": 0.2310718170132079, "1": 0.1580786502266773, "10": 6.374267893436668e-07, "11": 8.493238176942424e-08, "12": 1.0410600842562426e-08, "13": 1.1812485703885353e-09, "14": 1.2473507602939128e-10, "15": 1.230533969166803e-11, "16": 1.1248473056252899e-12, "17": 8.34121426140761e-14, "2": 0.08814808294110475, "3": 0.035698019067886985, "4": 0.011676164147154144, "5": 0.0031844642511069336, "6": 0.0007423416078538455, "7": 0.00015080849573711222, "8": 2.711499070199023e-05, "9": 4.3690515217977865e-06} |
| Raw goal margin distribution | {"-1": 0.20043921689691008, "-10": 2.0887013658652238e-05, "-11": 4.003446606364799e-06, "-12": 7.059130836533111e-07, "-13": 1.1522094437048193e-07, "-14": 1.750223171173141e-08, "-15": 2.4837800736279844e-09, "-16": 3.266087402118979e-10, "-17": 3.484000476448949e-11, "-2": 0.15752203815368826, "-3": 0.09176715473792063, "-4": 0.043177554363686504, "-5": 0.016939825185625496, "-6": 0.00568055864932847, "-7": 0.0016600751609667952, "-8": 0.0004293644681775871, "-9": 9.952186515212136e-05, "0": 0.2251639950495221, "1": 0.136512453678146, "10": 5.504645626003816e-07, "11": 7.334531143482954e-08, "12": 8.990313766242758e-09, "13": 1.0200943676853821e-09, "14": 1.0771784339052178e-10, "15": 1.0626559071980202e-11, "16": 9.713877584605393e-13, "17": 7.20324739518641e-14, "2": 0.07612230413189722, "3": 0.030827845299909402, "4": 0.010083220061603334, "5": 0.0027500173359627034, "6": 0.0006410661668112255, "7": 0.00013023414457969046, "8": 2.3415773773883924e-05, "9": 3.772994915072979e-06} |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.7% |
| P home draw | 52.9% |
| P draw away | 70.2% |
| P home away | 76.9% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.13, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:42Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.75, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.45, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.15, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.39, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.99, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.16 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -4.1% |
| Draw probability edge | -0.6% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.0812 |
| Raw ev home | -0.2776 |
| Raw edge prob draw | -0.0118 |
| Raw ev draw | -0.0858 |
| Raw edge prob away | 0.0930 |
| Raw ev away | 0.2012 |
| Market p home draw | 58.8% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:21:42Z |
| Market reference home draw last update utc | 2026-10-23T16:21:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.2% |
| Market draw away odds | 1.48 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:21:42Z |
| Market reference draw away last update utc | 2026-10-23T16:21:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:21:42Z |
| Market reference home away last update utc | 2026-10-23T16:21:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.51 |
| Market reference dc home draw odds | 1.65 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 90.8% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.75 |
| Market reference over 1 5 last update utc | 2026-10-23T16:21:51Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 50.8% |
| Market under 3 5 odds | 1.89 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market reference under 3 5 last update utc | 2026-10-23T16:21:51Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.7% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:21:42Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 3.30 |
| Market reference btts yes last update utc | 2026-10-23T16:21:51Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,478.2065 |
| Elo away rating | 1,602.6691 |
| Elo rating diff | -64.4626 |
| Elo home expectancy | 0.4083 |

</details>


---

## 2026-10-30 — Elversberg vs FSV Mainz 05

The model's most likely 1X2 outcome is **Elversberg win** at **37.7%**. Expected goals are 1.91 for Elversberg and 1.56 for FSV Mainz 05 (3.47 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 67.0%; Under 3.5 goals: 54.6%; Double Chance 1X: 62.4%; Double Chance X2: 62.3%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 73.4%; BTTS Yes (both teams score): 68.6%; BTTS No (at least one team does not score): 31.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 37.7% | 2.65 |
| Draw | 24.7% | 4.04 |
| FSV Mainz 05 win | 37.6% | 2.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 1.91 |
| FSV Mainz 05 expected goals | 1.56 |
| Expected total goals | 3.47 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 67.0% |
| Under 2.5 | 33.0% |
| Over 3.5 | 45.4% |
| Under 3.5 | 54.6% |
| Over 4.5 | 26.6% |
| Under 4.5 | 73.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.57% |
| 2 | 1-2 | 8.84% |
| 3 | 2-1 | 7.39% |
| 4 | 2-2 | 7.08% |
| 5 | 2-0 | 4.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 37.7% | 30.2% | 3.38 | +27.4% |
| Draw | 24.7% | 25.4% | 3.74 | -7.4% |
| FSV Mainz 05 win | 37.6% | 44.4% | 2.05 | -23.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T19:30:00+00:00 |
| Fixture id | b275fe870ec88a9f0054c9220beb2673 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9111 |
| Dc lambda away | 1.5582 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.6% |
| P btts no | 31.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.51 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.67 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.03 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.76 |
| Fair Under 4.5 odds | 1.36 |
| Goal margin distribution | {"-1": 0.1917178808068498, "-10": 1.158026159887985e-06, "-11": 1.6048659014152705e-07, "-12": 2.045496639481584e-08, "-13": 2.4127301890512685e-09, "-14": 2.6459637182538987e-10, "-15": 2.67888977315237e-11, "-16": 2.1995403902302836e-12, "-2": 0.11311521036788207, "-3": 0.04822065784620305, "-4": 0.016532296677705047, "-5": 0.004713807785514164, "-6": 0.0011468239968907533, "-7": 0.00024286682877588915, "-8": 4.548220910140687e-05, "-9": 7.628620178818624e-06, "0": 0.24746172732888494, "1": 0.16221629414072736, "10": 6.079081034621936e-06, "11": 1.0332782129741439e-06, "12": 1.6152369951436883e-07, "13": 2.3367120665689998e-08, "14": 3.1429631411387762e-09, "15": 3.9027362972777515e-10, "16": 3.930115056632216e-11, "2": 0.11597620362719671, "3": 0.06063731630471893, "4": 0.025497581668469892, "5": 0.008916545515240272, "6": 0.0026606055547312287, "7": 0.0006910522476860401, "8": 0.00015872421669059885, "9": 3.265175991609482e-05} |
| Raw goal margin distribution | {"-1": 0.1566789583908605, "-10": 9.463819011405171e-07, "-11": 1.3115559004331015e-07, "-12": 1.6716556719550883e-08, "-13": 1.971772540504894e-09, "-14": 2.162379625579594e-10, "-15": 2.1892880180764322e-11, "-16": 1.7975459348369492e-12, "-2": 0.09244194262953492, "-3": 0.0394077089339245, "-4": 0.013510805629450522, "-5": 0.003852298443842909, "-6": 0.0009372270783209428, "-7": 0.00019847977455287114, "-8": 3.7169747116613946e-05, "-9": 6.234391171791512e-06, "0": 0.24115287327341467, "1": 0.19449684953986807, "10": 7.288799905056361e-06, "11": 1.2388974744257754e-06, "12": 1.9366643066272303e-07, "13": 2.8017107506795072e-08, "14": 3.768403367920009e-09, "15": 4.679369100534978e-10, "16": 4.712196150782679e-11, "2": 0.1390551198729465, "3": 0.07270396015574658, "4": 0.03057152385136255, "5": 0.010690911296423581, "6": 0.003190058070335208, "7": 0.0008285695697485052, "8": 0.00019030985916385822, "9": 3.9149362086296995e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.3% |
| Raw p btts yes | 68.3% |
| P home draw | 62.4% |
| P draw away | 62.3% |
| P home away | 75.3% |
| Raw p home draw | 69.3% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.08 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:27Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:27Z |
| Home probability edge | +7.5% |
| Draw probability edge | -0.6% |
| Away probability edge | -6.9% |
| Over 2.5 probability edge | +5.9% |
| Under 2.5 probability edge | -5.9% |
| Raw edge prob home | 0.1500 |
| Raw ev home | 0.5270 |
| Raw edge prob draw | -0.0126 |
| Raw ev draw | -0.0981 |
| Raw edge prob away | -0.1373 |
| Raw ev away | -0.3705 |
| Elo home rating | 1,434.5693 |
| Elo away rating | 1,522.8682 |
| Elo rating diff | -28.2988 |
| Elo home expectancy | 0.4594 |

</details>


---

## 2026-10-31 — Augsburg vs SC Freiburg

The model's most likely 1X2 outcome is **SC Freiburg win** at **39.4%**. Expected goals are 1.36 for Augsburg and 1.43 for SC Freiburg (2.80 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 53.6%; Under 3.5 goals: 69.1%; Double Chance 1X: 60.6%; Double Chance X2: 65.6%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 34.4% | 2.91 |
| Draw | 26.3% | 3.81 |
| SC Freiburg win | 39.4% | 2.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.36 |
| SC Freiburg expected goals | 1.43 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 78.3% |
| Under 1.5 | 21.7% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 30.9% |
| Under 3.5 | 69.1% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.45% |
| 2 | 1-2 | 8.94% |
| 3 | 2-1 | 8.11% |
| 4 | 0-1 | 7.76% |
| 5 | 0-0 | 6.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 34.4% | 34.3% | 3.06 | +5.2% |
| Draw | 26.3% | 24.6% | 3.81 | +0.0% |
| SC Freiburg win | 39.4% | 41.1% | 2.17 | -14.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 24400b6372faf9f4996cd5704d707374 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Augsburg |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3643 |
| Dc lambda away | 1.4339 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.34 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.61 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.24 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.48 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.20144060848658135, "-10": 7.705335639363055e-07, "-11": 9.89930352741839e-08, "-12": 1.1679453207889575e-08, "-13": 1.2646659012564078e-09, "-14": 1.1364997146171021e-10, "-2": 0.1202510497030479, "-3": 0.05001118697336365, "-4": 0.016416545654567155, "-5": 0.00443147941644159, "-6": 0.0010134134367313496, "-7": 0.00020076146220072614, "-8": 3.505195452337612e-05, "-9": 5.4678182086638176e-06, "0": 0.26253554331023976, "1": 0.18194246776571796, "10": 4.461273557214906e-07, "11": 5.4531104550958093e-08, "12": 6.121171196048176e-09, "13": 6.306090291367266e-10, "14": 5.391704320808274e-11, "2": 0.10369964804037651, "3": 0.04103249539200166, "4": 0.01281489071149156, "5": 0.003291199627929663, "6": 0.0007160848868967872, "7": 0.00013496792176576555, "8": 2.2419958842264207e-05, "9": 3.3274305466176477e-06} |
| Raw goal margin distribution | {"-1": 0.19242947305389974, "-10": 7.360649314583641e-07, "-11": 9.456473427544402e-08, "-12": 1.1156990853220053e-08, "-13": 1.2080930195572596e-09, "-14": 1.085660149920787e-10, "-2": 0.11487180416294882, "-3": 0.047774013533748265, "-4": 0.015682176763698964, "-5": 0.004233244008552839, "-6": 0.0009680799471420657, "-7": 0.0001917807073313601, "-8": 3.348395931246323e-05, "-9": 5.223223780709465e-06, "0": 0.27921616316256104, "1": 0.18243785708852706, "10": 4.4734206238866673e-07, "11": 5.4679580754932185e-08, "12": 6.137837798908119e-09, "13": 6.323260388252157e-10, "14": 5.40638474580785e-11, "2": 0.10398199937401027, "3": 0.04114421785215642, "4": 0.012849782840357336, "5": 0.0033001608406411946, "6": 0.0007180346285461663, "7": 0.0001353354097315251, "8": 2.2481003459085493e-05, "9": 3.336490408152041e-06} |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 58.0% |
| P home draw | 60.6% |
| P draw away | 65.6% |
| P home away | 73.7% |
| Raw p home draw | 62.4% |
| Raw p draw away | 65.5% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.63 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.23 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | +0.1% |
| Draw probability edge | +1.7% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | 0.0019 |
| Raw ev home | 0.0545 |
| Raw edge prob draw | 0.0334 |
| Raw ev draw | 0.0638 |
| Raw edge prob away | -0.0352 |
| Raw ev away | -0.1837 |
| Elo home rating | 1,477.3863 |
| Elo away rating | 1,490.4954 |
| Elo rating diff | 46.8909 |
| Elo home expectancy | 0.5671 |

</details>


---

## 2026-10-31 — Bayer Leverkusen vs VfB Stuttgart

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **58.4%**. Expected goals are 2.29 for Bayer Leverkusen and 1.23 for VfB Stuttgart (3.51 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 68.2%; Under 3.5 goals: 53.6%; Double Chance 1X: 79.4%; Double Chance X2: 41.6%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 64.5%; BTTS No (at least one team does not score): 35.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 58.4% | 1.71 |
| Draw | 21.0% | 4.76 |
| VfB Stuttgart win | 20.6% | 4.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.29 |
| VfB Stuttgart expected goals | 1.23 |
| Expected total goals | 3.51 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.2% |
| Under 2.5 | 31.8% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.26% |
| 2 | 1-1 | 9.19% |
| 3 | 2-0 | 7.56% |
| 4 | 3-1 | 7.06% |
| 5 | 2-2 | 5.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 58.4% | 56.5% | 1.79 | +4.6% |
| Draw | 21.0% | 20.8% | 4.35 | -8.6% |
| VfB Stuttgart win | 20.6% | 22.7% | 3.79 | -22.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | a7ba9b844f121a4a8777d87b1f863137 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Leverkusen |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2880 |
| Dc lambda away | 1.2253 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.5% |
| P btts no | 35.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.84 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.93 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.14 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.12109751562191641, "-10": 8.977251394109555e-08, "-11": 9.795772908251842e-09, "-12": 9.828675593257604e-10, "-13": 9.125504592762365e-11, "-14": 7.883021146532483e-12, "-15": 6.365854982929423e-13, "-16": 4.823371992648491e-14, "-17": 3.4116856261124426e-15, "-18": 2.0095005539507693e-16, "-2": 0.05805132482711808, "-3": 0.0196450880939924, "-4": 0.005331043665538255, "-5": 0.0012009581299350556, "-6": 0.00023058106337316717, "-7": 3.850548620705443e-05, "-8": 5.683047834060795e-06, "-9": 7.509215138815081e-07, "0": 0.21022323752050578, "1": 0.20454743994320612, "10": 4.0250516093702065e-05, "11": 8.201111300453264e-06, "12": 1.5365083672407592e-06, "13": 2.6638069516560946e-07, "14": 4.296793503810468e-08, "15": 6.479096724105909e-09, "16": 9.166729394313388e-10, "17": 1.2107057101245807e-10, "18": 1.3315689098014261e-11, "2": 0.17611354197757845, "3": 0.11128599881792477, "4": 0.05639034068600079, "5": 0.023720633115504604, "6": 0.008504092567421677, "7": 0.002651751871278185, "8": 0.000730798277720084, "9": 0.00018030869990269438} |
| Raw goal margin distribution | {"-1": 0.10877128775520428, "-10": 8.063478343256586e-08, "-11": 8.79868450080127e-09, "-12": 8.82823809981856e-10, "-13": 8.19664120170565e-11, "-14": 7.080627187983888e-12, "-15": 5.717889756863036e-13, "-16": 4.3324124385902034e-14, "-17": 3.0644182670664942e-15, "-18": 1.8049582757787256e-16, "-2": 0.05214241865254683, "-3": 0.01764546133811237, "-4": 0.004788409420307512, "-5": 0.0010787154605298634, "-6": 0.0002071107657845678, "-7": 3.4586104420655544e-05, "-8": 5.104583922391741e-06, "-9": 6.744870004021521e-07, "0": 0.21227602244018684, "1": 0.21115644005018266, "10": 4.155102450017735e-05, "11": 8.466092106260813e-06, "12": 1.586153495853877e-06, "13": 2.7498754961137923e-07, "14": 4.435624421147905e-08, "15": 6.688438630094156e-09, "16": 9.462909662149853e-10, "17": 1.2498240396913167e-10, "18": 1.3745923720836612e-11, "2": 0.18180383278783255, "3": 0.11488168878743439, "4": 0.058212332531656245, "5": 0.024487055158437285, "6": 0.008778862805090912, "7": 0.0027374309118265235, "8": 0.000754410628463615, "9": 0.00018613453774880275} |
| Unadjusted home-win probability | 60.3% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 64.4% |
| P home draw | 79.4% |
| P draw away | 41.6% |
| P home away | 79.0% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.7% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.67 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.80 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | +1.9% |
| Draw probability edge | +0.2% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | 0.0377 |
| Raw ev home | 0.0795 |
| Raw edge prob draw | 0.0041 |
| Raw ev draw | -0.0766 |
| Raw edge prob away | -0.0419 |
| Raw ev away | -0.3001 |
| Elo home rating | 1,584.4079 |
| Elo away rating | 1,540.5013 |
| Elo rating diff | 103.9067 |
| Elo home expectancy | 0.6452 |

</details>


---

## 2026-10-31 — Bayern Munich vs Borussia Dortmund

The model's most likely 1X2 outcome is **Bayern Munich win** at **69.8%**. Expected goals are 2.72 for Bayern Munich and 1.39 for Borussia Dortmund (4.11 combined). The most likely exact score is 2-1 at 9.1%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 78.6%; Under 3.5 goals: 40.6%; Double Chance 1X: 86.0%; Double Chance X2: 30.2%; Double Chance 12 (either team wins): 83.7%; Under 4.5 goals: 60.0%; BTTS Yes (both teams score): 70.1%; BTTS No (at least one team does not score): 29.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 69.8% | 1.43 |
| Draw | 16.3% | 6.15 |
| Borussia Dortmund win | 14.0% | 7.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.72 |
| Borussia Dortmund expected goals | 1.39 |
| Expected total goals | 4.11 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 92.5% |
| Under 1.5 | 7.5% |
| Over 2.5 | 78.6% |
| Under 2.5 | 21.4% |
| Over 3.5 | 59.4% |
| Under 3.5 | 40.6% |
| Over 4.5 | 40.0% |
| Under 4.5 | 60.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.06% |
| 2 | 3-1 | 8.22% |
| 3 | 2-0 | 6.53% |
| 4 | 1-1 | 6.15% |
| 5 | 3-0 | 5.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 69.8% | 74.6% | 1.34 | -6.5% |
| Draw | 16.3% | 14.3% | 5.55 | -9.7% |
| Borussia Dortmund win | 14.0% | 11.1% | 7.60 | +6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:30:00+00:00 |
| Fixture id | bad7337b335a16859b1db6b8e6cf6ca5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Bayern Munich |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7221 |
| Dc lambda away | 1.3881 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 70.1% |
| P btts no | 29.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 48.04 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.41 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.66 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.50 |
| Fair Under 4.5 odds | 1.67 |
| Goal margin distribution | {"-1": 0.0798756336873134, "-10": 1.3968044041930844e-07, "-11": 1.71474054817427e-08, "-12": 1.9375866303216825e-09, "-13": 2.0275888400315937e-10, "-14": 1.9754084315681705e-11, "-15": 1.8001301539296435e-12, "-16": 1.5405349434772428e-13, "-17": 1.2414344636044823e-14, "-18": 9.32547750371903e-16, "-19": 5.682977838673762e-17, "-2": 0.039703288917136356, "-3": 0.014473488168821604, "-4": 0.004295660176291388, "-5": 0.0010685016017806628, "-6": 0.00022793558550236623, "-7": 4.247259312769752e-05, "-8": 7.0159011126335525e-06, "-9": 1.0398685556754166e-06, "0": 0.16271858693165844, "1": 0.21010527677739382, "10": 0.0001522077686140019, "11": 3.664121780552106e-05, "12": 8.119006127150836e-06, "13": 1.666064806311966e-06, "14": 3.1830184777122796e-07, "15": 5.687958534889412e-08, "16": 9.545404279616541e-09, "17": 1.508401060975486e-09, "18": 2.2219504432898216e-10, "19": 2.6552750246566788e-11, "2": 0.19786347914205274, "3": 0.14144338000007636, "4": 0.08232080172100187, "5": 0.04015365743759372, "6": 0.016797023245123683, "7": 0.006137609111576916, "8": 0.001988127195414589, "9": 0.0005778424072138755} |
| Raw goal margin distribution | {"-1": 0.09636387771342311, "-10": 1.685138290384692e-07, "-11": 2.0687040698965786e-08, "-12": 2.3375509211532904e-09, "-13": 2.4461317427386997e-10, "-14": 2.3831800481093965e-11, "-15": 2.1717201355871493e-12, "-16": 1.8585382557043145e-13, "-17": 1.4976962725368903e-14, "-18": 1.1250479430379649e-15, "-19": 6.856080586951667e-17, "-2": 0.047898998748592214, "-3": 0.01746116280525389, "-4": 0.005182387329120017, "-5": 0.0012890659258324275, "-6": 0.0002749869500112169, "-7": 5.1239953680386e-05, "-8": 8.464151151700598e-06, "-9": 1.2545223331737445e-06, "0": 0.1820879315269219, "1": 0.19558622768087813, "10": 0.0001416896507481703, "11": 3.41091745915939e-05, "12": 7.5579528762136455e-06, "13": 1.55093358689738e-06, "14": 2.9630601679455744e-07, "15": 5.294899633686744e-08, "16": 8.885781658483232e-09, "17": 1.4041649875295866e-09, "18": 2.0684054773043659e-10, "19": 2.471785732816626e-11, "2": 0.18419038338675386, "3": 0.13166912106618936, "4": 0.07663213087853611, "5": 0.0373788916978509, "6": 0.01563628702320741, "7": 0.005713477698063576, "8": 0.0018507402777555631, "9": 0.0005379113668846219} |
| Unadjusted home-win probability | 64.9% |
| Unadjusted draw probability | 18.2% |
| Unadjusted away-win probability | 16.9% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 41.2% |
| Raw p btts yes | 70.8% |
| P home draw | 86.0% |
| P draw away | 30.2% |
| P home away | 83.7% |
| Raw p home draw | 83.1% |
| Raw p draw away | 35.1% |
| Raw p home away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.29 |
| Reference draw odds | 5.40 |
| Reference away odds | 6.75 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.33 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -4.8% |
| Draw probability edge | +1.9% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0964 |
| Raw ev home | -0.1298 |
| Raw edge prob draw | 0.0387 |
| Raw ev draw | 0.0106 |
| Raw edge prob away | 0.0577 |
| Raw ev away | 0.2808 |
| Elo home rating | 1,720.7230 |
| Elo away rating | 1,615.6111 |
| Elo rating diff | 165.1118 |
| Elo home expectancy | 0.7212 |

</details>


---

## 2026-10-31 — Borussia Monchengladbach vs SC Paderborn

The model's most likely 1X2 outcome is **Borussia Monchengladbach win** at **53.6%**. Expected goals are 1.56 for Borussia Monchengladbach and 0.85 for SC Paderborn (2.40 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.3%; Under 3.5 goals: 77.6%; Double Chance 1X: 78.6%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 53.6% | 1.86 |
| Draw | 25.0% | 4.00 |
| SC Paderborn win | 21.4% | 4.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.56 |
| SC Paderborn expected goals | 0.85 |
| Expected total goals | 2.40 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.3% |
| Under 2.5 | 55.7% |
| Over 3.5 | 22.4% |
| Under 3.5 | 77.6% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.95% |
| 2 | 1-1 | 11.77% |
| 3 | 2-0 | 11.13% |
| 4 | 2-1 | 9.44% |
| 5 | 0-0 | 9.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 53.6% | 54.6% | 1.86 | -0.3% |
| Draw | 25.0% | 21.9% | 4.10 | +2.6% |
| SC Paderborn win | 21.4% | 23.6% | 3.69 | -21.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | aecb9d8c01176616c87d893bee4bc0de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | M'gladbach |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5558 |
| Dc lambda away | 0.8487 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.87 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.47 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.08 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.14096667312149602, "-10": 6.063620669533358e-09, "-11": 4.632545763880737e-10, "-12": 3.249153497790862e-11, "-13": 2.1058589111084805e-12, "-14": 1.2645081472066397e-13, "-15": 6.575940774688794e-15, "-2": 0.05510176660186214, "-3": 0.014126882720707945, "-4": 0.0028189734786498288, "-5": 0.00045891076191042763, "-6": 6.297972334296695e-05, "-7": 7.463222604749232e-06, "-8": 7.777196717964683e-07, "-9": 7.229300349043476e-08, "0": 0.25022483690575525, "1": 0.24720394336435494, "10": 2.3715026677407347e-06, "11": 3.321121476115576e-07, "12": 4.2698116859955275e-08, "13": 5.072723762736723e-09, "14": 5.58350647533069e-10, "15": 5.32251305440632e-11, "2": 0.1690711539271599, "3": 0.07945546680467741, "4": 0.02906309647965619, "5": 0.008672665295111133, "6": 0.0021817176341096525, "7": 0.0004739119269162015, "8": 9.052484238416163e-05, "9": 1.5424617788498286e-05} |
| Raw goal margin distribution | {"-1": 0.12644916776271495, "-10": 5.4391564354395576e-09, "-11": 4.1554613121963796e-10, "-12": 2.914538214112949e-11, "-13": 1.8889862464574175e-12, "-14": 1.1342823044822903e-13, "-15": 5.898715063663528e-15, "-2": 0.04942709063620758, "-3": 0.012672020439720516, "-4": 0.0025286604445379393, "-5": 0.00041164966609457554, "-6": 5.6493733066825236e-05, "-7": 6.694619843833957e-06, "-8": 6.976259216006076e-07, "-9": 6.484788158796771e-08, "0": 0.281710157940747, "1": 0.24282747566478155, "10": 2.3295178810760575e-06, "11": 3.2623247568207043e-07, "12": 4.1942194738620904e-08, "13": 4.982916895603726e-09, "14": 5.484656774929159e-10, "15": 5.2282839488906604e-11, "2": 0.16607793936099408, "3": 0.07804879715656153, "4": 0.028548567054025916, "5": 0.008519125513274719, "6": 0.0021430927779470736, "7": 0.0004655218494264814, "8": 8.89222018950521e-05, "9": 1.515154228407508e-05} |
| Unadjusted home-win probability | 52.7% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 19.2% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 77.8% |
| Raw p btts yes | 46.5% |
| P home draw | 78.6% |
| P draw away | 46.4% |
| P home away | 75.0% |
| Raw p home draw | 80.8% |
| Raw p draw away | 47.3% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.02, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.72 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.65 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -0.9% |
| Draw probability edge | +3.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -22.0% |
| Under 2.5 probability edge | +22.0% |
| Raw edge prob home | -0.0190 |
| Raw ev home | -0.0203 |
| Raw edge prob draw | 0.0630 |
| Raw ev draw | 0.1550 |
| Raw edge prob away | -0.0440 |
| Raw ev away | -0.2932 |
| Elo home rating | 1,413.4046 |
| Elo away rating | 1,399.4332 |
| Elo rating diff | 73.9714 |
| Elo home expectancy | 0.6049 |

</details>


---

## 2026-10-31 — FC Schalke 04 vs RB Leipzig

The model's most likely 1X2 outcome is **RB Leipzig win** at **58.3%**. Expected goals are 0.91 for FC Schalke 04 and 2.08 for RB Leipzig (3.00 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.3%; Under 3.5 goals: 65.5%; Double Chance 1X: 41.7%; Double Chance X2: 80.4%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 19.6% | 5.10 |
| Draw | 22.1% | 4.53 |
| RB Leipzig win | 58.3% | 1.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.91 |
| RB Leipzig expected goals | 2.08 |
| Expected total goals | 3.00 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 80.6% |
| Under 1.5 | 19.4% |
| Over 2.5 | 57.3% |
| Under 2.5 | 42.7% |
| Over 3.5 | 34.5% |
| Under 3.5 | 65.5% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.50% |
| 2 | 0-2 | 9.99% |
| 3 | 1-2 | 9.11% |
| 4 | 0-1 | 8.61% |
| 5 | 0-3 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 19.6% | 24.8% | 4.04 | -20.8% |
| Draw | 22.1% | 22.0% | 3.68 | -18.8% |
| RB Leipzig win | 58.3% | 53.3% | 1.88 | +9.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 3966f2fe1c2f73bfa12e61db83bd0bf9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Schalke 04 |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9122 |
| Dc lambda away | 2.0845 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.62 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.16 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.53 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.21114890970593622, "-10": 2.3299453052777594e-05, "-11": 4.353306687965684e-06, "-12": 7.471953193013365e-07, "-13": 1.1858260142265805e-07, "-14": 1.749886762343845e-08, "-15": 2.4122890549493743e-09, "-16": 3.104697024720792e-10, "-17": 3.423958038584945e-11, "-2": 0.1803101870656564, "-3": 0.1093801651458632, "-4": 0.05231229232691627, "-5": 0.02056065121689175, "-6": 0.006843262997668211, "-7": 0.001972548591402239, "-8": 0.0005010127831767061, "-9": 0.00011367922912083496, "0": 0.22076471103902195, "1": 0.12822232296376618, "10": 8.848240155267956e-09, "11": 7.234426963968406e-10, "12": 5.4336631584844666e-11, "13": 3.773577209384617e-12, "14": 2.4367776895940983e-13, "15": 1.46997181409186e-14, "16": 8.27889898804705e-16, "17": 3.995356060398218e-17, "2": 0.05092626927341527, "3": 0.013518666988819114, "4": 0.002829259244885869, "5": 0.000486608348355362, "6": 7.087280436274066e-05, "7": 8.939593976678212e-06, "8": 9.936022994940039e-07, "9": 9.865488577686227e-08} |
| Raw goal margin distribution | {"-1": 0.22941227158144642, "-10": 2.5314743319712723e-05, "-11": 4.729846711345975e-06, "-12": 8.118241091307165e-07, "-13": 1.2883942427311723e-07, "-14": 1.9012435239125367e-08, "-15": 2.62094041867287e-09, "-16": 3.373238336893627e-10, "-17": 3.720113887991545e-11, "-2": 0.19590614823262248, "-3": 0.11884102166103089, "-4": 0.05683705320128931, "-5": 0.02233904834000834, "-6": 0.007435172227556077, "-7": 0.0021431645268194708, "-8": 0.0005443479714860183, "-9": 0.00012351193392643532, "0": 0.22195920298673366, "1": 0.09445332238114036, "10": 6.5179421225073725e-09, "11": 5.329147425161045e-10, "12": 4.002637966275885e-11, "13": 2.77975703800695e-12, "14": 1.795020893136075e-13, "15": 1.0828357998696023e-14, "16": 6.098544286238508e-16, "17": 2.943127571529621e-17, "2": 0.03751418020019758, "3": 0.009958351882449057, "4": 0.0020841373746796265, "5": 0.00035845377106099864, "6": 5.2207538311570866e-05, "7": 6.585236738179329e-06, "8": 7.319243337938121e-07, "9": 7.267285068131052e-08} |
| Unadjusted home-win probability | 14.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 63.4% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 64.8% |
| Raw p btts yes | 53.4% |
| P home draw | 41.7% |
| P draw away | 80.4% |
| P home away | 77.9% |
| Raw p home draw | 36.6% |
| Raw p draw away | 85.6% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.76 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -5.2% |
| Draw probability edge | +0.1% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | -0.1033 |
| Raw ev home | -0.4165 |
| Raw edge prob draw | 0.0024 |
| Raw ev draw | -0.1832 |
| Raw edge prob away | 0.1009 |
| Raw ev away | 0.1912 |
| Elo home rating | 1,438.7706 |
| Elo away rating | 1,513.4005 |
| Elo rating diff | -14.6300 |
| Elo home expectancy | 0.4790 |

</details>


---

## 2026-10-31 — Werder Bremen vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **40.0%**. Expected goals are 1.82 for Werder Bremen and 1.59 for TSG Hoffenheim (3.42 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 66.7%; Under 3.5 goals: 55.6%; Double Chance 1X: 60.0%; Double Chance X2: 63.5%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 74.0%; BTTS Yes (both teams score): 67.8%; BTTS No (at least one team does not score): 32.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 36.5% | 2.74 |
| Draw | 23.6% | 4.24 |
| TSG Hoffenheim win | 40.0% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.82 |
| TSG Hoffenheim expected goals | 1.59 |
| Expected total goals | 3.42 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 86.6% |
| Under 1.5 | 13.4% |
| Over 2.5 | 66.7% |
| Under 2.5 | 33.3% |
| Over 3.5 | 44.4% |
| Under 3.5 | 55.6% |
| Over 4.5 | 26.0% |
| Under 4.5 | 74.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.16% |
| 2 | 1-2 | 9.21% |
| 3 | 2-1 | 7.47% |
| 4 | 2-2 | 6.64% |
| 5 | 0-1 | 5.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 36.5% | 30.5% | 2.92 | +6.5% |
| Draw | 23.6% | 22.6% | 3.91 | -7.9% |
| TSG Hoffenheim win | 40.0% | 46.9% | 2.21 | -11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 2fad25b09c01b71e47a5b0fd1d0b4e61 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8229 |
| Dc lambda away | 1.5938 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 67.8% |
| P btts no | 32.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.01 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.44 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.00 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.84 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.1997237946773889, "-10": 1.5049536634308803e-06, "-11": 2.1343753546694546e-07, "-12": 2.7837174755584834e-08, "-13": 3.3597333614797943e-09, "-14": 3.7700911762457715e-10, "-15": 3.9075950687127255e-11, "-16": 3.2942138495576447e-12, "-2": 0.12108111977745017, "-3": 0.053001131852702596, "-4": 0.01863622220565086, "-5": 0.00544560898860819, "-6": 0.0013570998008886166, "-7": 0.0002942939744694795, "-8": 5.6422511989522165e-05, "-9": 9.68682111719163e-06, "0": 0.23557872102481558, "1": 0.1632717219537177, "10": 4.089028257281694e-06, "11": 6.633054134632111e-07, "12": 9.894951298148347e-08, "13": 1.3659634472569664e-08, "14": 1.7532016889500617e-09, "15": 2.078429705365302e-10, "16": 2.004118225763683e-11, "2": 0.11230712884159649, "3": 0.056229186571631, "4": 0.022614151520356562, "5": 0.0075581347953996405, "6": 0.0021543969537479927, "7": 0.0005343687722971347, "8": 0.00011718118321743562, "9": 2.301084156469388e-05} |
| Raw goal margin distribution | {"-1": 0.1648284364143264, "-10": 1.242011046405417e-06, "-11": 1.7614613872108062e-07, "-12": 2.29735169841276e-08, "-13": 2.7727271937541343e-09, "-14": 3.111388078339927e-10, "-15": 3.224867554497595e-11, "-16": 2.718655125264739e-12, "-2": 0.09992605880761551, "-3": 0.04374087577087053, "-4": 0.015380137212940417, "-5": 0.004494162632779717, "-6": 0.001119989927088986, "-7": 0.00024287549581318712, "-8": 4.656447893363803e-05, "-9": 7.994358314446429e-06, "0": 0.24555803782227506, "1": 0.19005264979740502, "10": 4.759738221007694e-06, "11": 7.721052362599656e-07, "12": 1.1517987875220945e-07, "13": 1.590017974767083e-08, "14": 2.040773641798773e-09, "15": 2.419347748621702e-10, "16": 2.3328471994778835e-11, "2": 0.1307285007598217, "3": 0.06545227658541153, "4": 0.02632347701080835, "5": 0.008797870985882387, "6": 0.0025077756568974577, "7": 0.0006220195385263659, "8": 0.00013640203037230077, "9": 2.678523482883349e-05} |
| Unadjusted home-win probability | 42.5% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 33.0% |
| Raw p over 1 5 | 86.6% |
| Raw p under 3 5 | 55.5% |
| Raw p btts yes | 67.9% |
| P home draw | 60.0% |
| P draw away | 63.5% |
| P home away | 76.4% |
| Raw p home draw | 67.0% |
| Raw p draw away | 57.5% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.97 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | +6.0% |
| Draw probability edge | +1.0% |
| Away probability edge | -7.0% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.1197 |
| Raw ev home | 0.2400 |
| Raw edge prob draw | 0.0200 |
| Raw ev draw | -0.0399 |
| Raw edge prob away | -0.1396 |
| Raw ev away | -0.2712 |
| Elo home rating | 1,423.4938 |
| Elo away rating | 1,492.4811 |
| Elo rating diff | -8.9873 |
| Elo home expectancy | 0.4871 |

</details>


---

## 2026-11-01 — Eintracht Frankfurt vs Hamburger SV

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **59.6%**. Expected goals are 1.97 for Eintracht Frankfurt and 1.05 for Hamburger SV (3.03 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 59.0%; Under 3.5 goals: 63.9%; Double Chance 1X: 81.4%; Double Chance X2: 40.4%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 59.6% | 1.68 |
| Draw | 21.9% | 4.57 |
| Hamburger SV win | 18.6% | 5.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 1.97 |
| Hamburger SV expected goals | 1.05 |
| Expected total goals | 3.03 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 59.0% |
| Under 2.5 | 41.0% |
| Over 3.5 | 36.1% |
| Under 3.5 | 63.9% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.30% |
| 2 | 2-1 | 10.29% |
| 3 | 2-0 | 9.76% |
| 4 | 1-0 | 8.74% |
| 5 | 3-1 | 6.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 59.6% | 61.6% | 1.69 | +0.7% |
| Draw | 21.9% | 20.0% | 4.33 | -5.3% |
| Hamburger SV win | 18.6% | 18.5% | 4.30 | -20.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:30:00+00:00 |
| Fixture id | 1eb5e1a69ae9dd9edd92fde344308a4e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9713 |
| Dc lambda away | 1.0540 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.21 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.49 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.19 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.11451742781927553, "-10": 2.7181634041790733e-08, "-11": 2.564754342462883e-09, "-12": 2.2235160364718607e-10, "-13": 1.7826571839066493e-11, "-14": 1.328681748800556e-12, "-15": 9.192963257146983e-14, "-16": 5.3600367786340834e-15, "-2": 0.0509830994729368, "-3": 0.015471718342011297, "-4": 0.0037149457299264295, "-5": 0.0007345834741241413, "-6": 0.00012316607140721209, "-7": 1.7900113818172987e-05, "-8": 2.2937103454816605e-06, "-9": 2.626763340878459e-07, "0": 0.21878996697652123, "1": 0.2328071793360503, "10": 1.4797101046465992e-05, "11": 2.611193274094712e-06, "12": 4.233754554044911e-07, "13": 6.348124134965605e-08, "14": 8.84892904133113e-09, "15": 1.1450314980070142e-09, "16": 1.2485957292673954e-10, "2": 0.18543426345153605, "3": 0.10524330207455894, "4": 0.04726074410378949, "5": 0.01747758413459497, "6": 0.00548054190604664, "7": 0.0014896367307818867, "8": 0.00035698939887194876, "9": 7.645921923937254e-05} |
| Raw goal margin distribution | {"-1": 0.11506239649714166, "-10": 2.7310986747733215e-08, "-11": 2.576959565804689e-09, "-12": 2.2340973655995333e-10, "-13": 1.791140541829561e-11, "-14": 1.3350047159657932e-12, "-15": 9.23671098295013e-14, "-16": 5.3855442687357285e-15, "-2": 0.051225719245685544, "-3": 0.015545345579801419, "-4": 0.0037326245156041635, "-5": 0.0007380792301177835, "-6": 0.0001237521974875034, "-7": 1.798529737099027e-05, "-8": 2.304625717213181e-06, "-9": 2.639263654343453e-07, "0": 0.23801929873403146, "1": 0.224946262986906, "10": 1.4297465365694297e-05, "11": 2.5230242925467787e-06, "12": 4.0907985228474574e-07, "13": 6.133774762488065e-08, "14": 8.550138036810568e-09, "15": 1.1063686146344363e-09, "16": 1.206435918690841e-10, "2": 0.17917293062917675, "3": 0.10168967973234741, "4": 0.04566494814484299, "5": 0.016887439847554482, "6": 0.005295487125544254, "7": 0.0014393379824155993, "8": 0.0003449353728317426, "9": 7.387751394885824e-05} |
| Unadjusted home-win probability | 57.6% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 57.2% |
| P home draw | 81.4% |
| P draw away | 40.4% |
| P home away | 78.1% |
| Raw p home draw | 81.4% |
| Raw p draw away | 42.4% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.54 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | -2.0% |
| Draw probability edge | +1.9% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.0402 |
| Raw ev home | -0.0274 |
| Raw edge prob draw | 0.0385 |
| Raw ev draw | 0.0306 |
| Raw edge prob away | 0.0018 |
| Raw ev away | -0.1983 |
| Elo home rating | 1,477.2860 |
| Elo away rating | 1,419.8287 |
| Elo rating diff | 117.4573 |
| Elo home expectancy | 0.6629 |

</details>


---

## 2026-11-01 — Union Berlin vs 1. FC Köln

The model's most likely 1X2 outcome is **Union Berlin win** at **39.8%**. Expected goals are 1.44 for Union Berlin and 1.07 for 1. FC Köln (2.51 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 46.3%; Under 3.5 goals: 75.7%; Double Chance 1X: 67.1%; Double Chance X2: 60.2%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 88.9%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 39.8% | 2.51 |
| Draw | 27.3% | 3.66 |
| 1. FC Köln win | 32.9% | 3.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 1.44 |
| 1. FC Köln expected goals | 1.07 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 72.7% |
| Under 1.5 | 27.3% |
| Over 2.5 | 46.3% |
| Under 2.5 | 53.7% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 11.1% |
| Under 4.5 | 88.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.04% |
| 2 | 1-0 | 9.33% |
| 3 | 0-1 | 9.01% |
| 4 | 0-0 | 8.94% |
| 5 | 1-2 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 39.8% | 35.6% | 2.50 | -0.5% |
| Draw | 27.3% | 25.5% | 3.58 | -2.1% |
| 1. FC Köln win | 32.9% | 38.9% | 2.70 | -11.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:30:00+00:00 |
| Fixture id | 60eaeb599578cd5c951f917c4fef06ff |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:21:26Z |
| Market best draw last update utc | 2026-10-23T16:21:26Z |
| Market best away last update utc | 2026-10-23T16:21:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Union Berlin |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4351 |
| Dc lambda away | 1.0709 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:21:43.479598+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.18 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.67 |
| Fair Over 2.5 odds | 2.16 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 4.12 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.03 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.19654620037178885, "-10": 6.28744808670294e-08, "-11": 6.051090334022524e-09, "-12": 5.346610912964356e-10, "-13": 4.345741899251752e-11, "-14": 2.9952694224043514e-12, "-2": 0.09309196548256167, "-3": 0.029687013803764237, "-4": 0.007405457302432528, "-5": 0.001511289475644256, "-6": 0.0002604497751564419, "-7": 3.880075171064009e-05, "-8": 5.0869981959453295e-06, "-9": 5.952487463512986e-07, "0": 0.2734774407113285, "1": 0.19835546761990167, "10": 8.655612863367073e-07, "11": 1.1163616131972002e-07, "12": 1.3218972086491474e-08, "13": 1.4398951906282514e-09, "14": 1.3299970927099966e-10, "2": 0.12318358429564152, "3": 0.0526447415701549, "4": 0.017599008975558928, "5": 0.004813177028739298, "6": 0.0011116191273982752, "7": 0.00022193204269327116, "8": 3.8993238077606055e-05, "9": 6.114684505386231e-06} |
| Raw goal margin distribution | {"-1": 0.16016297532532045, "-10": 5.1235607244757396e-08, "-11": 4.9309558262945815e-09, "-12": 4.3568845905306637e-10, "-13": 3.5412892809093106e-11, "-14": 2.440806597562152e-12, "-2": 0.07585944751089266, "-3": 0.02419156641207301, "-4": 0.006034612080816692, "-5": 0.0012315303910182857, "-6": 0.00021223717799153096, "-7": 3.161823442569648e-05, "-8": 4.145329520468745e-06, "-9": 4.85060561302894e-07, "0": 0.29211290810520546, "1": 0.21937983652566487, "10": 9.573050633691685e-07, "11": 1.2346885676780655e-07, "12": 1.4620095781422574e-08, "13": 1.5925145665227083e-09, "14": 1.4709679963924214e-10, "2": 0.13624023027793705, "3": 0.05822473631897851, "4": 0.01946438763901486, "5": 0.005323341990034304, "6": 0.0012294434097211032, "7": 0.0002454553727712405, "8": 4.312626366046924e-05, "9": 6.762800659310167e-06} |
| Unadjusted home-win probability | 44.0% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 26.8% |
| Raw p over 1 5 | 72.8% |
| Raw p under 3 5 | 75.6% |
| Raw p btts yes | 51.5% |
| P home draw | 67.1% |
| P draw away | 60.2% |
| P home away | 72.7% |
| Raw p home draw | 73.2% |
| Raw p draw away | 56.0% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:20:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.03, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:21:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-23T16:21:27Z |
| Market reference home last update utc | 2026-10-23T16:21:27Z |
| Market reference draw last update utc | 2026-10-23T16:21:27Z |
| Market reference away last update utc | 2026-10-23T16:21:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-23T16:21:26Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:21:26Z |
| Home probability edge | +4.2% |
| Draw probability edge | +1.9% |
| Away probability edge | -6.1% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | 0.0844 |
| Raw ev home | 0.1004 |
| Raw edge prob draw | 0.0373 |
| Raw ev draw | 0.0458 |
| Raw edge prob away | -0.1216 |
| Raw ev away | -0.2771 |
| Elo home rating | 1,422.1325 |
| Elo away rating | 1,400.3928 |
| Elo rating diff | 81.7397 |
| Elo home expectancy | 0.6155 |

</details>


---
