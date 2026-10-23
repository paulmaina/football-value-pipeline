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
| Training as of utc | 2026-10-23T14:32:41.860332+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 21, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-23T14:32:41.860332+00:00', 'observations': 131, 'observations_sha256': '435ee8cc5b0788f1317ee26813f165b239364f52405a96cac107c96bde9cdc63', 'eligible_training_matches': 18, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 61, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 18, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '727de9d4e01f3afdf1db23d4fb253804d2b01e5a2dbfa8fdac4c119389f6098b', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
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
| Additional event odds calls used before this league | 15.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261023T143241860332Z_2dbc8e4205f530bc2da7f061fcdb3ed9964cf7c8acad75b228dc36d353abf63f.json |
| Over 1 5 in window quote fixtures | 5 |
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

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **63.7%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.46 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 68.5%; Under 3.5 goals: 53.9%; Double Chance 1X: 82.9%; Double Chance X2: 36.3%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 72.5%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 63.7% | 1.57 |
| Draw | 19.2% | 5.21 |
| Borussia Monchengladbach win | 17.1% | 5.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.17 |
| Borussia Monchengladbach expected goals | 1.29 |
| Expected total goals | 3.46 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 87.3% |
| Under 1.5 | 12.7% |
| Over 2.5 | 68.5% |
| Under 2.5 | 31.5% |
| Over 3.5 | 46.1% |
| Under 3.5 | 53.9% |
| Over 4.5 | 27.5% |
| Under 4.5 | 72.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.78% |
| 2 | 1-1 | 8.40% |
| 3 | 2-0 | 8.37% |
| 4 | 3-1 | 7.79% |
| 5 | 1-0 | 6.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 63.7% | 71.0% | 1.35 | -13.9% |
| Draw | 19.2% | 16.0% | 6.05 | +16.1% |
| Borussia Monchengladbach win | 17.1% | 13.0% | 7.77 | +32.6% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1678 |
| Dc lambda away | 1.2876 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.16 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.90 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.17 |
| Fair Over 3.5 odds | 2.17 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.63 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.09766970125296143, "-10": 1.1305003779307308e-07, "-11": 1.296404944606549e-08, "-12": 1.366991910718179e-09, "-13": 1.3338034741196126e-10, "-14": 1.2108115440599611e-11, "-15": 1.0269296025272584e-12, "-16": 8.093565864561067e-14, "-17": 5.265753107735759e-15, "-2": 0.049050744345746376, "-3": 0.017454900092390205, "-4": 0.004979820815615162, "-5": 0.0011792646743009874, "-6": 0.00023798673821871043, "-7": 4.177080935218015e-05, "-8": 6.479410100838705e-06, "-9": 8.997875907599422e-07, "0": 0.1919084119970749, "1": 0.2376006793150515, "10": 2.8924387170403132e-05, "11": 5.584059859089342e-06, "12": 9.912684025160481e-07, "13": 1.6282950198082072e-07, "14": 2.4884775966650796e-08, "15": 3.55315200702735e-09, "16": 4.71442739330318e-10, "17": 5.1637531271610065e-11, "2": 0.19449641494394726, "3": 0.11651968389392826, "4": 0.05596436476869278, "5": 0.022311310670515592, "6": 0.007580231742973768, "7": 0.0022398480064631677, "8": 0.000584920791410082, "9": 0.00013674691004314334} |
| Raw goal margin distribution | {"-1": 0.12108248281134266, "-10": 1.401496992649639e-07, "-11": 1.6071711841864842e-08, "-12": 1.6946788247471958e-09, "-13": 1.6535346597458782e-10, "-14": 1.5010598587959767e-11, "-15": 1.2730988663968659e-12, "-16": 1.0033705817734047e-13, "-17": 6.528027136121265e-15, "-2": 0.06080888784276198, "-3": 0.021639081652729618, "-4": 0.006173552909193593, "-5": 0.0014619507669656505, "-6": 0.0002950354590013737, "-7": 5.178385149660599e-05, "-8": 8.032614537547329e-06, "-9": 1.11547915161404e-06, "0": 0.22360988022016684, "1": 0.21054018580477463, "10": 2.5630170194383536e-05, "11": 4.948087706090902e-06, "12": 8.783722094135866e-07, "13": 1.4428474573544366e-07, "14": 2.2050632897314926e-08, "15": 3.148481249753551e-09, "16": 4.1774982386857727e-10, "17": 4.575649976997325e-11, "2": 0.17234509370389306, "3": 0.10324918248408058, "4": 0.04959054742946751, "5": 0.01977026121162622, "6": 0.00671691429590895, "7": 0.001984750282762916, "8": 0.0005183037879334599, "9": 0.00012117271689504114} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 65.1% |
| P home draw | 82.9% |
| P draw away | 36.3% |
| P home away | 80.8% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:30Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.44, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:30Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.14, "price": 6.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.39 |
| Reference draw odds | 5.82 |
| Reference away odds | 7.13 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:49Z |
| Market reference home last update utc | 2026-10-23T14:32:49Z |
| Market reference draw last update utc | 2026-10-23T14:32:49Z |
| Market reference away last update utc | 2026-10-23T14:32:49Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.82 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -7.3% |
| Draw probability edge | +3.2% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -8.5% |
| Under 2.5 probability edge | +8.5% |
| Raw edge prob home | -0.1452 |
| Raw ev home | -0.2374 |
| Raw edge prob draw | 0.0634 |
| Raw ev draw | 0.3528 |
| Raw edge prob away | 0.0818 |
| Raw ev away | 0.6435 |
| Market p home draw | 87.0% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:32:30Z |
| Market reference home draw last update utc | 2026-10-23T14:32:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 29.8% |
| Market draw away odds | 3.44 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:32:30Z |
| Market reference draw away last update utc | 2026-10-23T14:32:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.2% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:32:30Z |
| Market reference home away last update utc | 2026-10-23T14:32:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.24 |
| Market reference dc home draw odds | 1.11 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 92.4% |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 6.80 |
| Market reference over 1 5 last update utc | 2026-10-23T14:32:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 43.1% |
| Market under 3 5 odds | 2.23 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 3 5 odds | 2.23 |
| Market reference under 3 5 opposite odds | 1.71 |
| Market reference under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.3% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:32:30Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.56 |
| Market reference btts yes last update utc | 2026-10-23T14:32:47Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,553.6374 |
| Elo away rating | 1,396.1351 |
| Elo rating diff | 217.5024 |
| Elo home expectancy | 0.7777 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.5%**. Expected goals are 1.76 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 50.4%; Under 3.5 goals: 72.0%; Double Chance 1X: 76.4%; Double Chance X2: 48.5%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.5% | 1.94 |
| Draw | 25.0% | 4.00 |
| FC Schalke 04 win | 23.6% | 4.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.76 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.94% |
| 2 | 1-0 | 9.92% |
| 3 | 2-0 | 9.72% |
| 4 | 2-1 | 9.05% |
| 5 | 0-0 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.5% | 47.3% | 2.08 | +7.0% |
| Draw | 25.0% | 24.1% | 3.88 | -3.0% |
| FC Schalke 04 win | 23.6% | 28.6% | 3.38 | -20.4% |
| Over 2.5 | 50.4% | 61.0% | 1.64 | -17.3% |
| Under 2.5 | 49.6% | 39.0% | 2.46 | +21.9% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Koln |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7565 |
| Dc lambda away | 0.9312 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.88 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.44 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.15121608557792218, "-10": 1.3544619949962264e-08, "-11": 1.1327785589375536e-09, "-12": 8.700383241239556e-11, "-13": 6.177344658731296e-12, "-14": 4.076828069270011e-13, "-15": 2.5028883015093636e-14, "-16": 1.321635770174258e-15, "-2": 0.06258206536881573, "-3": 0.017245180634380824, "-4": 0.0037253941625184097, "-5": 0.0006592194141459249, "-6": 9.85831713420794e-05, "-7": 1.2750722479140455e-05, "-8": 1.4518549498489576e-06, "-9": 1.475826896360722e-07, "0": 0.24989641716264785, "1": 0.2179597769184736, "10": 5.6259415460602e-06, "11": 8.875005747429221e-07, "12": 1.2857520840280293e-07, "13": 1.7219316858853575e-08, "14": 2.1435405918865493e-09, "15": 2.482252832604592e-10, "16": 2.4723591645393616e-11, "2": 0.16222449702153474, "3": 0.08431979132779158, "4": 0.034358107644203176, "5": 0.011467855873565202, "6": 0.003234820994596684, "7": 0.0007891825839368177, "8": 0.00016949666581824629, "9": 3.249889403900213e-05} |
| Raw goal margin distribution | {"-1": 0.11901780213611288, "-10": 1.0660578145853147e-08, "-11": 8.915772014359359e-10, "-12": 6.847819708840465e-11, "-13": 4.862009101145505e-12, "-14": 3.208753319046182e-13, "-15": 1.9699509050201553e-14, "-16": 1.0402212435895433e-15, "-2": 0.04925653143889126, "-3": 0.013573182302001932, "-4": 0.002932149867648614, "-5": 0.0005188525116044867, "-6": 7.759195945259399e-05, "-7": 1.0035724435763281e-05, "-8": 1.1427129891046987e-06, "-9": 1.1615806140392456e-07, "0": 0.25873886073272884, "1": 0.23545840978578575, "10": 6.077613350093515e-06, "11": 9.587524678514556e-07, "12": 1.3889771101997326e-07, "13": 1.8601748554274613e-08, "14": 2.3156321143862893e-09, "15": 2.681537451150703e-10, "16": 2.6708494821019045e-11, "2": 0.1752484914282001, "3": 0.09108930216485438, "4": 0.037116506098182074, "5": 0.0123885385910091, "6": 0.0034945246232946227, "7": 0.0008525411379637494, "8": 0.00018310449736092758, "9": 3.510802781323466e-05} |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 76.4% |
| P draw away | 48.5% |
| P home away | 75.0% |
| Raw p home draw | 81.5% |
| Raw p draw away | 44.4% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.68, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.06, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.54, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:24Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.73, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.04 |
| Reference draw odds | 3.88 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:49Z |
| Market reference home last update utc | 2026-10-23T14:32:49Z |
| Market reference draw last update utc | 2026-10-23T14:32:49Z |
| Market reference away last update utc | 2026-10-23T14:32:49Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market best under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | +4.1% |
| Draw probability edge | +0.9% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | 0.0826 |
| Raw ev home | 0.1562 |
| Raw edge prob draw | 0.0177 |
| Raw ev draw | 0.0039 |
| Raw edge prob away | -0.1003 |
| Raw ev away | -0.3734 |
| Market p home draw | 71.3% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:32:31Z |
| Market reference home draw last update utc | 2026-10-23T14:32:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.6% |
| Market draw away odds | 1.80 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:32:31Z |
| Market reference draw away last update utc | 2026-10-23T14:32:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:32:31Z |
| Market reference home away last update utc | 2026-10-23T14:32:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.81 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:28:24Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-23T14:32:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.4% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.52 |
| Market reference under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 63.4% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:32:31Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.45 |
| Market reference btts yes last update utc | 2026-10-23T14:32:47Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,415.8199 |
| Elo away rating | 1,439.3959 |
| Elo rating diff | 36.4240 |
| Elo home expectancy | 0.5522 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **45.5%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 46.7%; Under 3.5 goals: 75.5%; Double Chance 1X: 72.4%; Double Chance X2: 54.5%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 88.8%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 45.5% | 2.20 |
| Draw | 26.9% | 3.71 |
| Union Berlin win | 27.6% | 3.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.34 |
| Union Berlin expected goals | 1.16 |
| Expected total goals | 2.50 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 46.7% |
| Under 2.5 | 53.3% |
| Over 3.5 | 24.5% |
| Under 3.5 | 75.5% |
| Over 4.5 | 11.2% |
| Under 4.5 | 88.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.86% |
| 2 | 1-0 | 11.04% |
| 3 | 2-1 | 9.84% |
| 4 | 0-0 | 8.74% |
| 5 | 2-0 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 45.5% | 51.4% | 1.86 | -15.4% |
| Draw | 26.9% | 24.2% | 4.12 | +11.0% |
| Union Berlin win | 27.6% | 24.4% | 3.90 | +7.4% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3432 |
| Dc lambda away | 1.1565 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.45 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.70 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.08 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 8.92 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.15817902669714393, "-10": 1.0000401693254311e-07, "-11": 1.0393082534725513e-08, "-12": 9.916591699675302e-10, "-13": 8.703323405353984e-11, "-14": 6.471626008721031e-12, "-2": 0.08027655345523688, "-3": 0.02761824893235837, "-4": 0.007435268409347405, "-5": 0.0016379451999249455, "-6": 0.00030474676203118723, "-7": 4.901800677692119e-05, "-8": 6.93909686204766e-06, "-9": 8.767665008095205e-07, "0": 0.269492048976512, "1": 0.2379479269894133, "10": 5.719286603092333e-07, "11": 6.903169947941529e-08, "12": 7.649735078944457e-09, "13": 7.797382849737226e-10, "14": 6.733748973386483e-11, "2": 0.138699515270826, "3": 0.055419440681443166, "4": 0.017327759972785135, "5": 0.004433277471467225, "6": 0.0009579534811657304, "7": 0.00017895372441387704, "8": 2.94217037028615e-05, "9": 4.317462654078455e-06} |
| Raw goal margin distribution | {"-1": 0.1763104073257917, "-10": 1.1146704672390299e-07, "-11": 1.1584396827630202e-08, "-12": 1.1053287900177012e-09, "-13": 9.70094788624568e-11, "-14": 7.213440627893272e-12, "-2": 0.08947830906497202, "-3": 0.030784009868845247, "-4": 0.008287541206955107, "-5": 0.0018256958043433625, "-6": 0.00033967857096382597, "-7": 5.463672979657701e-05, "-8": 7.734495651962664e-06, "-9": 9.772664689820522e-07, "0": 0.29698579805514147, "1": 0.20705432102003277, "10": 4.976731755158091e-07, "11": 6.006907412647986e-08, "12": 6.6565433991969264e-09, "13": 6.785021546993433e-10, "14": 5.859482951771685e-11, "2": 0.1206916753743615, "3": 0.04822414217593388, "4": 0.015078036700537232, "5": 0.003857689656564623, "6": 0.0008335790528671927, "7": 0.0001557195407050969, "8": 2.5601781702933724e-05, "9": 3.7569114792470382e-06} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 52.1% |
| P home draw | 72.4% |
| P draw away | 54.5% |
| P home away | 73.1% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.5, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.85, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.58, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.9, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:05Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.86, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.90 |
| Reference draw odds | 3.93 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:49Z |
| Market reference home last update utc | 2026-10-23T14:32:49Z |
| Market reference draw last update utc | 2026-10-23T14:32:49Z |
| Market reference away last update utc | 2026-10-23T14:32:49Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -5.9% |
| Draw probability edge | +2.7% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -18.4% |
| Under 2.5 probability edge | +18.4% |
| Raw edge prob home | -0.1181 |
| Raw ev home | -0.2636 |
| Raw edge prob draw | 0.0550 |
| Raw ev draw | 0.2236 |
| Raw edge prob away | 0.0632 |
| Raw ev away | 0.1976 |
| Market p home draw | 75.1% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:32:30Z |
| Market reference home draw last update utc | 2026-10-23T14:32:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.0% |
| Market draw away odds | 2.00 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:32:30Z |
| Market reference draw away last update utc | 2026-10-23T14:32:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.9% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:32:30Z |
| Market reference home away last update utc | 2026-10-23T14:32:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.02 |
| Market reference dc home draw odds | 1.29 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 86.0% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:31:05Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-23T14:32:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.5% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.21 |
| Market reference under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 65.8% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:32:30Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 2.59 |
| Market reference btts yes last update utc | 2026-10-23T14:32:47Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,477.3863 |
| Elo away rating | 1,413.5523 |
| Elo rating diff | 123.8339 |
| Elo home expectancy | 0.6710 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **64.9%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 71.0%; Under 3.5 goals: 50.3%; Double Chance 1X: 83.8%; Double Chance X2: 35.1%; Double Chance 12 (either team wins): 81.1%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 64.9% | 1.54 |
| Draw | 18.9% | 5.29 |
| Eintracht Frankfurt win | 16.2% | 6.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.42 |
| Eintracht Frankfurt expected goals | 1.22 |
| Expected total goals | 3.64 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 88.9% |
| Under 1.5 | 11.1% |
| Over 2.5 | 71.0% |
| Under 2.5 | 29.0% |
| Over 3.5 | 49.7% |
| Under 3.5 | 50.3% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.67% |
| 2 | 1-1 | 8.09% |
| 3 | 2-0 | 7.91% |
| 4 | 3-1 | 7.81% |
| 5 | 3-0 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 64.9% | 67.0% | 1.49 | -3.2% |
| Draw | 18.9% | 17.7% | 5.16 | -2.5% |
| Eintracht Frankfurt win | 16.2% | 15.3% | 5.85 | -5.5% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4204 |
| Dc lambda away | 1.2230 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.59 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.97 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.45 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.27 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.09592746267871144, "-10": 6.701359906823767e-08, "-11": 7.290151441516991e-09, "-12": 7.293610363832757e-10, "-13": 6.75322288714988e-11, "-14": 5.818345204204006e-12, "-15": 4.686533446361758e-13, "-16": 3.5418430516198007e-14, "-17": 2.4965873100945307e-15, "-18": 1.4567214709114645e-16, "-2": 0.04530580104573927, "-3": 0.01517323741948059, "-4": 0.004085665318248032, "-5": 0.0009147597911830417, "-6": 0.000174737587049474, "-7": 2.905208502007428e-05, "-8": 4.271157618059148e-06, "-9": 5.62376330902449e-07, "0": 0.18891871306359262, "1": 0.21465280510495494, "10": 6.700801807965815e-05, "11": 1.4426480092617315e-05, "12": 2.8564484464089785e-06, "13": 5.234255472463759e-07, "14": 8.924899150749328e-08, "15": 1.4227072821271633e-08, "16": 2.127909468137085e-09, "17": 2.968455849062106e-10, "18": 3.427838540208684e-11, "2": 0.1925030599281739, "3": 0.12759159833661, "4": 0.06799337725692756, "5": 0.030128040930260933, "6": 0.011389644294575488, "7": 0.0037476682029354215, "8": 0.001090408998309803, "9": 0.0002841390100458879} |
| Raw goal margin distribution | {"-1": 0.1008199178034008, "-10": 7.043140057189441e-08, "-11": 7.661960908627254e-09, "-12": 7.665596241553048e-10, "-13": 7.097648133057463e-11, "-14": 6.115090182301262e-12, "-15": 4.925554201590898e-13, "-16": 3.722482752752938e-14, "-17": 2.6239172846234727e-15, "-18": 1.5310166125381743e-16, "-2": 0.04761646988149045, "-3": 0.015947096970209025, "-4": 0.004294040831014139, "-5": 0.0009614140141058629, "-6": 0.00018364948547109012, "-7": 3.053378815565524e-05, "-8": 4.488993536922317e-06, "-9": 5.910584297018606e-07, "0": 0.2009315184621497, "1": 0.2079582373752766, "10": 6.491817949009746e-05, "11": 1.3976548641529773e-05, "12": 2.7673618510510974e-06, "13": 5.071010096948098e-07, "14": 8.646550392082855e-08, "15": 1.3783360461908335e-08, "16": 2.0615444651262818e-09, "17": 2.8758759793306595e-10, "18": 3.3209314943743265e-11, "2": 0.18649929597908707, "3": 0.12361228580731552, "4": 0.06587280739531537, "5": 0.029188410952113036, "6": 0.011034425339436757, "7": 0.0036307863452739483, "8": 0.0010564014441636254, "9": 0.0002752773143113929} |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.2% |
| P home draw | 83.8% |
| P draw away | 35.1% |
| P home away | 81.1% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.1% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.84, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.86, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:57Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.79, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:57Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.21, "price": 4.79, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.46 |
| Reference draw odds | 5.13 |
| Reference away odds | 5.87 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:49Z |
| Market reference home last update utc | 2026-10-23T14:32:49Z |
| Market reference draw last update utc | 2026-10-23T14:32:49Z |
| Market reference away last update utc | 2026-10-23T14:32:49Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.15 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -2.0% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0405 |
| Raw ev home | -0.0625 |
| Raw edge prob draw | 0.0240 |
| Raw ev draw | 0.0368 |
| Raw edge prob away | 0.0165 |
| Raw ev away | -0.0063 |
| Market p home draw | 83.6% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:32:57Z |
| Market reference home draw last update utc | 2026-10-23T14:32:57Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.9% |
| Market draw away odds | 2.78 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:32:57Z |
| Market reference draw away last update utc | 2026-10-23T14:32:57Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.5% |
| Market home away odds | 1.19 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:32:57Z |
| Market reference home away last update utc | 2026-10-23T14:32:57Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.78 |
| Market reference dc home draw odds | 1.16 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:31:35Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-23T14:32:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.2% |
| Market under 3 5 odds | 1.90 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 3 5 odds | 1.90 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market reference under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 64.5% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:32:57Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.65 |
| Market reference btts yes last update utc | 2026-10-23T14:32:57Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,632.7906 |
| Elo away rating | 1,482.9718 |
| Elo rating diff | 209.8188 |
| Elo home expectancy | 0.7699 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **53.5%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 56.2%; Under 3.5 goals: 66.8%; Double Chance 1X: 77.3%; Double Chance X2: 46.5%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 53.5% | 1.87 |
| Draw | 23.8% | 4.19 |
| Werder Bremen win | 22.7% | 4.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.73 |
| Werder Bremen expected goals | 1.16 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 56.2% |
| Under 2.5 | 43.8% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.28% |
| 2 | 2-1 | 10.43% |
| 3 | 1-0 | 9.05% |
| 4 | 2-0 | 8.99% |
| 5 | 0-0 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 53.5% | 57.5% | 1.74 | -6.9% |
| Draw | 23.8% | 21.5% | 4.23 | +0.9% |
| Werder Bremen win | 22.7% | 21.0% | 4.43 | +0.4% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.18 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.98 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.85 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.1327274734181861, "-10": 7.592047869089915e-08, "-11": 7.89323153314478e-09, "-12": 7.539495075774019e-10, "-13": 6.659434137184394e-11, "-14": 5.468259689438282e-12, "-15": 4.1696467828006334e-13, "-16": 2.6877906379444828e-14, "-2": 0.06489934409232218, "-3": 0.021781463401785633, "-4": 0.005776010317093309, "-5": 0.0012603411781491611, "-6": 0.0002330700125357884, "-7": 3.734661617992173e-05, "-8": 5.275106460713249e-06, "-9": 6.657889054001461e-07, "0": 0.23843433789804322, "1": 0.23617925658941819, "10": 4.760854816610386e-06, "11": 7.376266084810562e-07, "12": 1.0499768572455979e-07, "13": 1.3820715445279465e-08, "14": 1.6912120367194722e-09, "15": 1.9217811488309537e-10, "16": 1.8461025896584756e-11, "2": 0.16730944100061643, "3": 0.08368024205409517, "4": 0.03306888605867304, "5": 0.010753144051125318, "6": 0.0029633944954365796, "7": 0.000707636231612951, "8": 0.0001489518028295543, "9": 2.801604468778639e-05} |
| Raw goal margin distribution | {"-1": 0.14247784076705286, "-10": 8.149771554679675e-08, "-11": 8.473080640761977e-09, "-12": 8.093358151146142e-10, "-13": 7.14864656247143e-11, "-14": 5.869966580693833e-12, "-15": 4.475955543152249e-13, "-16": 2.885239933119665e-14, "-2": 0.0696669511996081, "-3": 0.023381563698234183, "-4": 0.006200325049771612, "-5": 0.0013529278081465498, "-6": 0.00025019169941570713, "-7": 4.009015689243162e-05, "-8": 5.662624014326884e-06, "-9": 7.146987975066424e-07, "0": 0.26203353230793264, "1": 0.21840348956457412, "10": 4.402534415059234e-06, "11": 6.82109968565133e-07, "12": 9.70951525955297e-08, "13": 1.2780514788288492e-08, "14": 1.5639248583767983e-09, "15": 1.7771404446994173e-10, "16": 1.7071577474584738e-11, "2": 0.1547170834530861, "3": 0.07738214242919016, "4": 0.030579993414845387, "5": 0.009943820716817067, "6": 0.0027403579302687888, "7": 0.0006543767837971854, "8": 0.0001377411123427451, "9": 2.5907448486243322e-05} |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 24.3% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.7% |
| P home draw | 77.3% |
| P draw away | 46.5% |
| P home away | 76.2% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.0, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.45, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.17, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.99, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 9.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.91, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.91, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.68 |
| Reference draw odds | 4.23 |
| Reference away odds | 4.32 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:49Z |
| Market reference home last update utc | 2026-10-23T14:32:49Z |
| Market reference draw last update utc | 2026-10-23T14:32:49Z |
| Market reference away last update utc | 2026-10-23T14:32:49Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -4.0% |
| Draw probability edge | +2.4% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0805 |
| Raw ev home | -0.1394 |
| Raw edge prob draw | 0.0472 |
| Raw ev draw | 0.1084 |
| Raw edge prob away | 0.0333 |
| Raw ev away | 0.0782 |
| Market p home draw | 77.6% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:32:30Z |
| Market reference home draw last update utc | 2026-10-23T14:32:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.5% |
| Market draw away odds | 2.18 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:32:30Z |
| Market reference draw away last update utc | 2026-10-23T14:32:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.9% |
| Market home away odds | 1.25 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:32:30Z |
| Market reference home away last update utc | 2026-10-23T14:32:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.13 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:31:00Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-23T14:32:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.0% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market reference under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:32:30Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.37 |
| Market reference btts yes last update utc | 2026-10-23T14:32:47Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,456.9980 |
| Elo away rating | 1,456.2478 |
| Elo rating diff | 60.7502 |
| Elo home expectancy | 0.5865 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **66.9%**. Expected goals are 2.69 for RB Leipzig and 1.32 for Elversberg (4.01 combined). The most likely exact score is 2-1 at 8.8%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 76.6%; Under 3.5 goals: 43.0%; Double Chance 1X: 84.5%; Double Chance X2: 33.1%; Double Chance 12 (either team wins): 82.4%; Under 4.5 goals: 62.5%; BTTS Yes (both teams score): 68.8%; BTTS No (at least one team does not score): 31.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 66.9% | 1.50 |
| Draw | 17.6% | 5.68 |
| Elversberg win | 15.5% | 6.45 |

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
| Over 2.5 | 76.6% |
| Under 2.5 | 23.4% |
| Over 3.5 | 57.0% |
| Under 3.5 | 43.0% |
| Over 4.5 | 37.5% |
| Under 4.5 | 62.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.83% |
| 2 | 3-1 | 7.90% |
| 3 | 1-1 | 6.91% |
| 4 | 2-0 | 6.68% |
| 5 | 3-0 | 5.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 66.9% | 68.1% | 1.45 | -3.0% |
| Draw | 17.6% | 17.0% | 5.15 | -9.3% |
| Elversberg win | 15.5% | 15.0% | 6.48 | +0.5% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6858 |
| Dc lambda away | 1.3213 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 68.8% |
| P btts no | 31.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.90 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.02 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.27 |
| Fair Over 3.5 odds | 1.76 |
| Fair Under 3.5 odds | 2.32 |
| Fair Over 4.5 odds | 2.67 |
| Fair Under 4.5 odds | 1.60 |
| Goal margin distribution | {"-1": 0.09042792089428696, "-10": 1.078955126794534e-07, "-11": 1.262805757406269e-08, "-12": 1.3600892491920375e-09, "-13": 1.3563524934949976e-10, "-14": 1.2591273335016213e-11, "-15": 1.0931568275175718e-12, "-16": 8.912008329433266e-14, "-17": 6.842008523780088e-15, "-18": 4.903443682680251e-16, "-19": 2.873288134905626e-17, "-2": 0.043714650098707064, "-3": 0.015341841153081922, "-4": 0.004369088522703533, "-5": 0.001040564263893579, "-6": 0.00021223872656811674, "-7": 3.777599987938789e-05, "-8": 5.956378896668034e-06, "-9": 8.422595641711124e-07, "0": 0.1761534328141763, "1": 0.20144042904191684, "10": 0.00013704902581544276, "11": 3.2604437289280105e-05, "12": 7.13797709267992e-06, "13": 1.446931256694716e-06, "14": 2.7303138130168294e-07, "15": 4.818290407050437e-08, "16": 7.984609303653584e-09, "17": 1.2460322523397095e-09, "18": 1.8151580694560344e-10, "19": 2.1620215806139248e-11, "2": 0.19052803446486807, "3": 0.1359179916231227, "4": 0.07867883071558396, "5": 0.0380893486398497, "6": 0.015791626239523994, "7": 0.005713283564707798, "8": 0.0018311322595915914, "9": 0.0005263212864850814} |
| Raw goal margin distribution | {"-1": 0.09366313419856194, "-10": 1.1175565891128154e-07, "-11": 1.3079847900177981e-08, "-12": 1.4087487648645406e-09, "-13": 1.4048783203507467e-10, "-14": 1.3041747642158895e-11, "-15": 1.1322663799331169e-12, "-16": 9.230850647492281e-14, "-17": 7.0867930636123475e-15, "-18": 5.078872754609432e-16, "-19": 2.976084924980331e-17, "-2": 0.0452786163625825, "-3": 0.015890721721380594, "-4": 0.004525400126204069, "-5": 0.0010777922275270356, "-6": 0.0002198319294758586, "-7": 3.912750078954324e-05, "-8": 6.169478524097603e-06, "-9": 8.723928385039892e-07, "0": 0.1827027465562, "1": 0.1977953465646291, "10": 0.00013456911150576232, "11": 3.2014457097070286e-05, "12": 7.008814762419025e-06, "13": 1.42074890693155e-06, "14": 2.680908541767862e-07, "15": 4.731103013652023e-08, "16": 7.840127088245476e-09, "17": 1.2234851879259732e-09, "18": 1.7823126227701323e-10, "19": 2.122899607847605e-11, "2": 0.1870804127378738, "3": 0.1334585434777333, "4": 0.07725513027700326, "5": 0.037400118488986944, "6": 0.015505875358395815, "7": 0.0056099011905312674, "8": 0.001797997758514627, "9": 0.0005167974560012261} |
| Unadjusted home-win probability | 65.7% |
| Unadjusted draw probability | 18.3% |
| Unadjusted away-win probability | 16.1% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 43.2% |
| Raw p btts yes | 69.0% |
| P home draw | 84.5% |
| P draw away | 33.1% |
| P home away | 82.4% |
| Raw p home draw | 83.9% |
| Raw p draw away | 34.3% |
| Raw p home away | 81.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:29Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.25, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:29Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.18, "price": 5.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.66, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.44 |
| Reference draw odds | 5.38 |
| Reference away odds | 6.06 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:49Z |
| Market reference home last update utc | 2026-10-23T14:32:49Z |
| Market reference draw last update utc | 2026-10-23T14:32:49Z |
| Market reference away last update utc | 2026-10-23T14:32:49Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.66 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -1.2% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.0242 |
| Raw ev home | -0.0479 |
| Raw edge prob draw | 0.0131 |
| Raw ev draw | -0.0591 |
| Raw edge prob away | 0.0111 |
| Raw ev away | 0.0413 |
| Market p home draw | 84.2% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:32:29Z |
| Market reference home draw last update utc | 2026-10-23T14:32:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.8% |
| Market draw away odds | 2.91 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:32:29Z |
| Market reference draw away last update utc | 2026-10-23T14:32:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.0% |
| Market home away odds | 1.19 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:32:29Z |
| Market reference home away last update utc | 2026-10-23T14:32:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.86 |
| Market reference dc home draw odds | 1.15 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 91.5% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.60 |
| Market reference over 1 5 last update utc | 2026-10-23T14:32:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 44.0% |
| Market under 3 5 odds | 2.17 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 3 5 odds | 2.17 |
| Market reference under 3 5 opposite odds | 1.73 |
| Market reference under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.4% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:32:29Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.77 |
| Market reference btts yes last update utc | 2026-10-23T14:32:47Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,582.0473 |
| Elo away rating | 1,431.9590 |
| Elo rating diff | 210.0883 |
| Elo home expectancy | 0.7702 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **39.0%**. Expected goals are 1.02 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 14.3%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 33.3%; Under 3.5 goals: 85.9%; Double Chance 1X: 68.3%; Double Chance X2: 61.0%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 94.6%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 39.0% | 2.56 |
| Draw | 29.3% | 3.41 |
| Hamburger SV win | 31.7% | 3.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.02 |
| Hamburger SV expected goals | 0.96 |
| Expected total goals | 1.98 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
| Over 1.5 | 60.7% |
| Under 1.5 | 39.3% |
| Over 2.5 | 33.3% |
| Under 2.5 | 66.7% |
| Over 3.5 | 14.1% |
| Under 3.5 | 85.9% |
| Over 4.5 | 5.4% |
| Under 4.5 | 94.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.25% |
| 2 | 0-0 | 13.19% |
| 3 | 1-1 | 12.93% |
| 4 | 0-1 | 11.84% |
| 5 | 2-0 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 39.0% | 43.7% | 2.18 | -14.9% |
| Draw | 29.3% | 24.5% | 3.77 | +10.4% |
| Hamburger SV win | 31.7% | 31.7% | 3.23 | +2.3% |
| Over 2.5 | 33.3% | 61.0% | 1.64 | -45.4% |
| Under 2.5 | 66.7% | 39.0% | 2.47 | +64.8% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0151 |
| Dc lambda away | 0.9633 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.58 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 7.08 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.65 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.19517358481230815, "-10": 2.8697446587827242e-08, "-11": 2.494577428522039e-09, "-12": 1.9852842251867173e-10, "-13": 1.3681773665916594e-11, "-2": 0.08795759253979812, "-3": 0.026204359858431014, "-4": 0.006025157726480035, "-5": 0.0011249560226472065, "-6": 0.0001765698857608586, "-7": 2.3886898083953106e-05, "-8": 2.838138533280622e-06, "-9": 3.005378221335565e-07, "0": 0.292882096290467, "1": 0.2343536533665483, "10": 5.500414250251638e-08, "11": 5.038550820869577e-09, "12": 4.2255948965878814e-10, "13": 3.0687681774856474e-11, "2": 0.11085961731360304, "3": 0.03480407602760513, "4": 0.008432988086786714, "5": 0.0016592243943982664, "6": 0.0002744370408010014, "7": 3.912391989017363e-05, "8": 4.898608222602262e-06, "9": 5.466316384883348e-07} |
| Raw goal margin distribution | {"-1": 0.1948357946700362, "-10": 2.864777944370491e-08, "-11": 2.490260022222927e-09, "-12": 1.9818482610344934e-10, "-13": 1.3658094394576739e-11, "-2": 0.08780536288368715, "-3": 0.026159007540630233, "-4": 0.006014729886628673, "-5": 0.0011230090427046845, "-6": 0.0001762642933473695, "-7": 2.3845556635467777e-05, "-8": 2.833226520111082e-06, "-9": 3.00017676367959e-07, "0": 0.3404571976245468, "1": 0.20612583145578817, "10": 4.837891129058115e-08, "11": 4.4316590006794925e-09, "12": 3.716623355097394e-10, "13": 2.6991360409471795e-11, "2": 0.09750661218793139, "3": 0.030611936303036078, "4": 0.00741723739346573, "5": 0.0014593713516048296, "6": 0.00024138118781060614, "7": 3.441145636658041e-05, "8": 4.308572443207241e-06, "9": 4.807900340568409e-07} |
| Unadjusted home-win probability | 34.3% |
| Unadjusted draw probability | 34.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 86.1% |
| Raw p btts yes | 40.9% |
| P home draw | 68.3% |
| P draw away | 61.0% |
| P home away | 70.7% |
| Raw p home draw | 68.4% |
| Raw p draw away | 65.7% |
| Raw p home away | 66.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.03, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.19 |
| Reference draw odds | 3.79 |
| Reference away odds | 2.97 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:49Z |
| Market reference home last update utc | 2026-10-23T14:32:49Z |
| Market reference draw last update utc | 2026-10-23T14:32:49Z |
| Market reference away last update utc | 2026-10-23T14:32:49Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market best under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -4.7% |
| Draw probability edge | +4.8% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -27.7% |
| Under 2.5 probability edge | +27.7% |
| Raw edge prob home | -0.0941 |
| Raw ev home | -0.2514 |
| Raw edge prob draw | 0.0952 |
| Raw ev draw | 0.2835 |
| Raw edge prob away | -0.0011 |
| Raw ev away | 0.0211 |
| Market p home draw | 68.8% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:32:29Z |
| Market reference home draw last update utc | 2026-10-23T14:32:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.1% |
| Market draw away odds | 1.74 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:32:29Z |
| Market reference draw away last update utc | 2026-10-23T14:32:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:32:29Z |
| Market reference home away last update utc | 2026-10-23T14:32:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home draw odds | 1.41 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-23T14:32:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.3% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.3% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:32:29Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-23T14:32:47Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,397.1739 |
| Elo away rating | 1,419.8287 |
| Elo rating diff | 37.3451 |
| Elo home expectancy | 0.5535 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **66.8%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 72.1%; Under 3.5 goals: 49.2%; Double Chance 1X: 33.2%; Double Chance X2: 84.6%; Double Chance 12 (either team wins): 82.3%; Under 4.5 goals: 68.4%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 15.4% | 6.48 |
| Draw | 17.7% | 5.64 |
| Bayern Munich win | 66.8% | 1.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.24 |
| Bayern Munich expected goals | 2.45 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 89.3% |
| Under 1.5 | 10.7% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.6% |
| Under 4.5 | 68.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.85% |
| 2 | 1-3 | 8.03% |
| 3 | 0-2 | 7.96% |
| 4 | 1-1 | 7.53% |
| 5 | 0-3 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 15.4% | 13.9% | 6.90 | +6.6% |
| Draw | 17.7% | 15.6% | 6.14 | +8.9% |
| Bayern Munich win | 66.8% | 70.5% | 1.37 | -8.5% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.45 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.39 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.16 |
| Fair Under 4.5 odds | 1.46 |
| Goal margin distribution | {"-1": 0.21897481125125007, "-10": 7.400585998893599e-05, "-11": 1.609998579295891e-05, "-12": 3.221429241847733e-06, "-13": 5.965669460217467e-07, "-14": 1.0280395345471622e-07, "-15": 1.6563030386907578e-08, "-16": 2.503756062694783e-09, "-17": 3.528662900593919e-10, "-18": 4.105959751609608e-11, "-2": 0.19732298065752524, "-3": 0.13173552635043173, "-4": 0.07079140182992716, "-5": 0.03165351757712519, "-6": 0.012080812758040406, "-7": 0.004014361690685113, "-8": 0.0011798021740650876, "-9": 0.00031058780060680874, "0": 0.17740613820647508, "1": 0.09133299383427577, "10": 6.97649865282784e-08, "11": 7.677969325651967e-09, "12": 7.77175231939369e-10, "13": 7.280798578870173e-11, "14": 6.347155249030172e-12, "15": 5.17319177482321e-13, "16": 3.956036306174102e-14, "17": 2.820511670798539e-15, "18": 1.6602821263116832e-16, "2": 0.043366390120715, "3": 0.014646302216745722, "4": 0.00398157652926651, "5": 0.0009006291706206655, "6": 0.00017388801839169566, "7": 2.9230717760108164e-05, "8": 4.3459191958990124e-06, "9": 5.787704152108178e-07} |
| Raw goal margin distribution | {"-1": 0.20680237532880852, "-10": 6.989200057536677e-05, "-11": 1.5205015068713602e-05, "-12": 3.0423554899353333e-06, "-13": 5.634048079548054e-07, "-14": 9.708925718964957e-08, "-15": 1.5642319804196967e-08, "-16": 2.3645765375958533e-09, "-17": 3.3325105541028294e-10, "-18": 3.8777164587349506e-11, "-2": 0.18635413303366327, "-3": 0.1244125733402344, "-4": 0.06685622865767639, "-5": 0.029893952574074033, "-6": 0.011409261001251659, "-7": 0.0037912101776405296, "-8": 0.0011142189853736416, "-9": 0.0002933227550082966, "0": 0.19914652279625214, "1": 0.1004413174280357, "10": 7.672240734782227e-08, "11": 8.44366665172337e-09, "12": 8.546802299076131e-10, "13": 8.006887440006902e-11, "14": 6.9801350899505175e-12, "15": 5.689096298692919e-13, "16": 4.3505581247698906e-14, "17": 3.1017915447970245e-15, "18": 1.8258563205707947e-16, "2": 0.04769117022186252, "3": 0.016106927281595608, "4": 0.004378645385978714, "5": 0.0009904458029198042, "6": 0.00019122926906243478, "7": 3.2145796145910663e-05, "8": 4.77932268665074e-06, "9": 6.364891870031925e-07} |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 33.2% |
| P draw away | 84.6% |
| P home away | 82.3% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 6.43 |
| Reference draw odds | 5.78 |
| Reference away odds | 1.39 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:49Z |
| Market reference home last update utc | 2026-10-23T14:32:49Z |
| Market reference draw last update utc | 2026-10-23T14:32:49Z |
| Market reference away last update utc | 2026-10-23T14:32:49Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.23 |
| Reference Under 2.5 odds | 4.23 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | +1.5% |
| Draw probability edge | +2.2% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0308 |
| Raw ev home | 0.1719 |
| Raw edge prob draw | 0.0435 |
| Raw ev draw | 0.2228 |
| Raw edge prob away | -0.0743 |
| Raw ev away | -0.1355 |
| Elo home rating | 1,530.2552 |
| Elo away rating | 1,716.3142 |
| Elo rating diff | -126.0590 |
| Elo home expectancy | 0.3261 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.4%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 70.5%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.6%; Double Chance X2: 69.3%; Double Chance 12 (either team wins): 77.1%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 70.0%; BTTS No (at least one team does not score): 30.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.7% | 3.26 |
| Draw | 22.9% | 4.37 |
| Bayer Leverkusen win | 46.4% | 2.15 |

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
| 1 | 1-1 | 9.42% |
| 2 | 1-2 | 8.07% |
| 3 | 2-1 | 7.47% |
| 4 | 2-2 | 6.87% |
| 5 | 1-3 | 5.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.7% | 35.6% | 2.81 | -13.8% |
| Draw | 22.9% | 23.3% | 4.06 | -7.1% |
| Bayer Leverkusen win | 46.4% | 41.1% | 2.32 | +7.7% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5009 |
| Dc lambda away | 2.1589 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 70.0% |
| P btts no | 30.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.10 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.92 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.1797556954101892, "-10": 1.87176200957624e-05, "-11": 3.5873065402253725e-06, "-12": 6.32478421559435e-07, "-13": 1.0322522446414308e-07, "-14": 1.5678614299792724e-08, "-15": 2.2247809329972816e-09, "-16": 2.9252478670336563e-10, "-17": 3.120174325641374e-11, "-2": 0.14125952814334136, "-3": 0.08228673121013941, "-4": 0.03871369435943704, "-5": 0.01518721819095658, "-6": 0.0050923967603319015, "-7": 0.0014880592687803614, "-8": 0.00038483933716822736, "-9": 8.919334214521346e-05, "0": 0.228911472136505, "1": 0.1629055442124968, "10": 6.569511293421288e-07, "11": 8.753400870911941e-08, "12": 1.0729511141166947e-08, "13": 1.2174354710785072e-09, "14": 1.2855639489097546e-10, "15": 1.2682333101749469e-11, "16": 1.1593123612763198e-12, "17": 8.596913312379339e-14, "2": 0.09084332878667421, "3": 0.036790102046974506, "4": 0.012033492517044019, "5": 0.00328194426110466, "6": 0.0007650698632366037, "7": 0.00015542647035520738, "8": 2.794538559904662e-05, "9": 4.502865548143128e-06} |
| Raw goal margin distribution | {"-1": 0.20043666936255541, "-10": 2.0871090742505568e-05, "-11": 4.000027778060202e-06, "-12": 7.052453496495637e-07, "-13": 1.1510133316544819e-07, "-14": 1.7482445956994447e-08, "-15": 2.480742984269398e-09, "-16": 3.2617989554667e-10, "-17": 3.4791517911852746e-11, "-2": 0.15751150066298586, "-3": 0.09175385680468003, "-4": 0.04316772238241783, "-5": 0.016934514503873687, "-6": 0.005678279307837367, "-7": 0.001659261159808062, "-8": 0.00042911527674088166, "-9": 9.945507644754193e-05, "0": 0.2251827318177463, "1": 0.13652333261792313, "10": 5.505592702720024e-07, "11": 7.335805938431988e-08, "12": 8.991889290412972e-09, "13": 1.0202743470909983e-09, "14": 1.0773695606681105e-10, "15": 1.0628455825683417e-11, "16": 9.715641531521025e-13, "17": 7.204661212158919e-14, "2": 0.07613144200841185, "3": 0.030832022096526867, "4": 0.010084693614335949, "5": 0.0027504402637630043, "6": 0.0006411684017233541, "7": 0.00013025547910300013, "8": 2.3419688947468547e-05, "9": 3.7736359062221075e-06} |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.7% |
| P home draw | 53.6% |
| P draw away | 69.3% |
| P home away | 77.1% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.45, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.15, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.39, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.99, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:31:00Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.77, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.68 |
| Reference draw odds | 4.03 |
| Reference away odds | 2.34 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:49Z |
| Market reference home last update utc | 2026-10-23T14:32:49Z |
| Market reference draw last update utc | 2026-10-23T14:32:49Z |
| Market reference away last update utc | 2026-10-23T14:32:49Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.05 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -5.0% |
| Draw probability edge | -0.4% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | -0.0994 |
| Raw ev home | -0.2775 |
| Raw edge prob draw | -0.0075 |
| Raw ev draw | -0.0858 |
| Raw edge prob away | 0.1068 |
| Raw ev away | 0.2011 |
| Market p home draw | 58.8% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:32:31Z |
| Market reference home draw last update utc | 2026-10-23T14:32:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.2% |
| Market draw away odds | 1.48 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:32:31Z |
| Market reference draw away last update utc | 2026-10-23T14:32:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:32:31Z |
| Market reference home away last update utc | 2026-10-23T14:32:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.51 |
| Market reference dc home draw odds | 1.65 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:31:00Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market reference over 1 5 last update utc | 2026-10-23T14:32:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.89 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 3 5 odds | 1.89 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market reference under 3 5 last update utc | 2026-10-23T14:32:47Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 72.9% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:32:31Z |
| Market reference btts yes odds | 1.32 |
| Market reference btts yes opposite odds | 3.15 |
| Market reference btts yes last update utc | 2026-10-23T14:32:47Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,478.2065 |
| Elo away rating | 1,602.6691 |
| Elo rating diff | -64.4626 |
| Elo home expectancy | 0.4083 |

</details>


---

## 2026-10-30 — Elversberg vs FSV Mainz 05

The model's most likely 1X2 outcome is **Elversberg win** at **37.8%**. Expected goals are 1.91 for Elversberg and 1.56 for FSV Mainz 05 (3.47 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 67.0%; Under 3.5 goals: 54.6%; Double Chance 1X: 62.6%; Double Chance X2: 62.2%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 73.4%; BTTS Yes (both teams score): 68.6%; BTTS No (at least one team does not score): 31.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 37.8% | 2.64 |
| Draw | 24.8% | 4.03 |
| FSV Mainz 05 win | 37.4% | 2.68 |

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
| 1 | 1-1 | 10.60% |
| 2 | 1-2 | 8.79% |
| 3 | 2-1 | 7.41% |
| 4 | 2-2 | 7.11% |
| 5 | 2-0 | 4.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 37.8% | 30.4% | 3.38 | +27.8% |
| Draw | 24.8% | 25.5% | 3.74 | -7.2% |
| FSV Mainz 05 win | 37.4% | 44.0% | 2.05 | -23.4% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9113 |
| Dc lambda away | 1.5583 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.6% |
| P btts no | 31.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.44 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.67 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.03 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.76 |
| Fair Under 4.5 odds | 1.36 |
| Goal margin distribution | {"-1": 0.1906711433830741, "-10": 1.1520187355395316e-06, "-11": 1.596600113675266e-07, "-12": 2.0350382652007925e-08, "-13": 2.4004855569029915e-09, "-14": 2.6326355357551443e-10, "-15": 2.665490268712394e-11, "-16": 2.1885832063701294e-12, "-2": 0.11250010690441133, "-3": 0.04795940463465858, "-4": 0.016443158342180707, "-5": 0.004688532855414479, "-6": 0.001140711929698091, "-7": 0.00024158071344992642, "-8": 4.524295559732843e-05, "-9": 7.588765735554787e-06, "0": 0.24822432234678396, "1": 0.162758197564676, "10": 6.103501204479685e-06, "11": 1.0375144664420544e-06, "12": 1.6219934552918237e-07, "13": 2.3466813815870308e-08, "14": 3.15663437989652e-09, "15": 3.9200278910588074e-10, "16": 3.947786256652409e-11, "2": 0.11637088210413203, "3": 0.060847632769512154, "4": 0.025587841708904647, "5": 0.008948781267619825, "6": 0.0026704313957940555, "7": 0.0006936593010896933, "8": 0.0001593358258064802, "9": 3.27802397934799e-05} |
| Raw goal margin distribution | {"-1": 0.1566687738100778, "-10": 9.465793276364043e-07, "-11": 1.3118785445786524e-07, "-12": 1.6721300560150645e-08, "-13": 1.9724071617550183e-09, "-14": 2.163157853660876e-10, "-15": 2.1901536047480162e-11, "-16": 1.798293340248435e-12, "-2": 0.0924379719421213, "-3": 0.03940680788638056, "-4": 0.013510851245375634, "-5": 0.003852427170640521, "-6": 0.0009372888635658754, "-7": 0.00019849964436581611, "-8": 3.7174782986099493e-05, "-9": 6.235461755912681e-06, "0": 0.24114600096140937, "1": 0.19449389749674495, "10": 7.293603366205933e-06, "11": 1.2398160910290537e-06, "12": 1.9382607669181158e-07, "13": 2.8042532721372752e-08, "14": 3.7721364128177205e-09, "15": 4.684381580995365e-10, "16": 4.717552461437769e-11, "2": 0.1390616678866384, "3": 0.07271211790171335, "4": 0.030577133053571875, "5": 0.010693675480730346, "6": 0.0031911302652468184, "7": 0.0008289137077116606, "8": 0.00019040420842489478, "9": 3.91719538168166e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.3% |
| Raw p btts yes | 68.3% |
| P home draw | 62.6% |
| P draw away | 62.2% |
| P home away | 75.2% |
| Raw p home draw | 69.3% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.20 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.23 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:48Z |
| Market reference home last update utc | 2026-10-23T14:32:48Z |
| Market reference draw last update utc | 2026-10-23T14:32:48Z |
| Market reference away last update utc | 2026-10-23T14:32:48Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:48Z |
| Home probability edge | +7.4% |
| Draw probability edge | -0.7% |
| Away probability edge | -6.7% |
| Over 2.5 probability edge | +6.8% |
| Under 2.5 probability edge | -6.8% |
| Raw edge prob home | 0.1474 |
| Raw ev home | 0.5271 |
| Raw edge prob draw | -0.0142 |
| Raw ev draw | -0.0981 |
| Raw edge prob away | -0.1333 |
| Raw ev away | -0.3705 |
| Elo home rating | 1,434.5693 |
| Elo away rating | 1,522.8682 |
| Elo rating diff | -28.2988 |
| Elo home expectancy | 0.4594 |

</details>


---

## 2026-10-31 — Augsburg vs SC Freiburg

The model's most likely 1X2 outcome is **SC Freiburg win** at **39.2%**. Expected goals are 1.36 for Augsburg and 1.43 for SC Freiburg (2.80 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 53.6%; Under 3.5 goals: 69.1%; Double Chance 1X: 60.8%; Double Chance X2: 65.6%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 34.4% | 2.91 |
| Draw | 26.4% | 3.79 |
| SC Freiburg win | 39.2% | 2.55 |

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
| 1 | 1-1 | 12.52% |
| 2 | 1-2 | 8.91% |
| 3 | 2-1 | 8.11% |
| 4 | 0-1 | 7.73% |
| 5 | 0-0 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 34.4% | 34.3% | 3.06 | +5.2% |
| Draw | 26.4% | 24.9% | 3.81 | +0.6% |
| SC Freiburg win | 39.2% | 40.9% | 2.17 | -14.9% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.26 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.61 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.24 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.49 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.200707293809469, "-10": 7.676245485907684e-07, "-11": 9.861761072725347e-08, "-12": 1.1634959798547228e-08, "-13": 1.2598265134918372e-09, "-14": 1.132131775337214e-10, "-2": 0.11981340049987607, "-3": 0.04982833659203565, "-4": 0.016356246665326365, "-5": 0.004415127173962957, "-6": 0.0010096566842810542, "-7": 0.00020001381187117855, "-8": 3.4920820201023904e-05, "-9": 5.447268904690961e-06, "0": 0.26396268731145967, "1": 0.18194349694927117, "10": 4.4619251544051305e-07, "11": 5.4539812060131706e-08, "12": 6.122231990628136e-09, "13": 6.307269294098349e-10, "14": 5.392787958950675e-11, "2": 0.10370338755689926, "3": 0.04103454979522343, "4": 0.012815709946328495, "5": 0.0032914553675063556, "6": 0.0007161503561837236, "7": 0.00013498210882069515, "8": 2.2422621829944527e-05, "9": 3.3278711762150515e-06} |
| Raw goal margin distribution | {"-1": 0.19242346361869955, "-10": 7.359422350579656e-07, "-11": 9.454734738216804e-08, "-12": 1.1154747896835826e-08, "-13": 1.2078294549419742e-09, "-14": 1.0854050859256637e-10, "-2": 0.11486831930486073, "-3": 0.04777176220860159, "-4": 0.015681172195623615, "-5": 0.004232900793019966, "-6": 0.0009679849325234956, "-7": 0.0001917586038919298, "-8": 3.3479526568006845e-05, "-9": 5.222442742405324e-06, "0": 0.2792230336653756, "1": 0.18243801168353205, "10": 4.474052478376692e-07, "11": 5.4688048964004526e-08, "12": 6.13887195840216e-09, "13": 6.324412185441987e-10, "14": 5.407445328678977e-11, "2": 0.1039852489809102, "3": 0.04114607996710507, "4": 0.012850542504263996, "5": 0.0033004014040709266, "6": 0.0007180968225813534, "7": 0.00013534898448700188, "8": 2.2483565568311606e-05, "9": 3.336916189408456e-06} |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 58.0% |
| P home draw | 60.8% |
| P draw away | 65.6% |
| P home away | 73.6% |
| Raw p home draw | 62.4% |
| Raw p draw away | 65.5% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:48Z |
| Market reference home last update utc | 2026-10-23T14:32:48Z |
| Market reference draw last update utc | 2026-10-23T14:32:48Z |
| Market reference away last update utc | 2026-10-23T14:32:48Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | +0.1% |
| Draw probability edge | +1.5% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | 0.0019 |
| Raw ev home | 0.0545 |
| Raw edge prob draw | 0.0305 |
| Raw ev draw | 0.0638 |
| Raw edge prob away | -0.0324 |
| Raw ev away | -0.1837 |
| Elo home rating | 1,477.3863 |
| Elo away rating | 1,490.4954 |
| Elo rating diff | 46.8909 |
| Elo home expectancy | 0.5671 |

</details>


---

## 2026-10-31 — Bayer Leverkusen vs VfB Stuttgart

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **58.0%**. Expected goals are 2.29 for Bayer Leverkusen and 1.23 for VfB Stuttgart (3.51 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 68.0%; Under 3.5 goals: 53.6%; Double Chance 1X: 79.3%; Double Chance X2: 42.0%; Double Chance 12 (either team wins): 78.7%; Under 4.5 goals: 72.5%; BTTS Yes (both teams score): 64.6%; BTTS No (at least one team does not score): 35.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 58.0% | 1.72 |
| Draw | 21.3% | 4.69 |
| VfB Stuttgart win | 20.7% | 4.83 |

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
| Over 2.5 | 68.0% |
| Under 2.5 | 32.0% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.5% |
| Under 4.5 | 72.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.32% |
| 2 | 2-1 | 9.19% |
| 3 | 2-0 | 7.50% |
| 4 | 3-1 | 7.01% |
| 5 | 2-2 | 5.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 58.0% | 55.7% | 1.79 | +3.8% |
| Draw | 21.3% | 21.4% | 4.35 | -7.3% |
| VfB Stuttgart win | 20.7% | 22.9% | 3.79 | -21.5% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Leverkusen |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2878 |
| Dc lambda away | 1.2253 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.6% |
| P btts no | 35.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.49 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.91 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.13 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.63 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.1219670867792147, "-10": 9.042394858920729e-08, "-11": 9.866860617180078e-09, "-12": 9.900004178631455e-10, "-13": 9.191730195496534e-11, "-14": 7.9402285386429e-12, "-15": 6.412050396013137e-13, "-16": 4.858372646443111e-14, "-17": 3.436446127714701e-15, "-18": 2.0241058172747583e-16, "-2": 0.05847049855360822, "-3": 0.019787179627808318, "-4": 0.005369645238427657, "-5": 0.0012096606351511595, "-6": 0.0002322527845816518, "-7": 3.8784752853844844e-05, "-8": 5.724275284054141e-06, "-9": 7.563699744500749e-07, "0": 0.21304478144612182, "1": 0.2030570238500208, "10": 3.992955437361447e-05, "11": 8.135029800799916e-06, "12": 1.5239990355230815e-06, "13": 2.64189614750568e-07, "14": 4.261089296157066e-08, "15": 6.424712810769668e-09, "16": 9.089014041134008e-10, "17": 1.2003410279346807e-10, "18": 1.3200715855054136e-11, "2": 0.1748213696105006, "3": 0.11046145946567314, "4": 0.055968237881322325, "5": 0.02354120814783937, "6": 0.008439083581493294, "7": 0.0026312647408815487, "8": 0.0007250921246541527, "9": 0.0001788859026615347} |
| Raw goal margin distribution | {"-1": 0.10878090495718165, "-10": 8.0647978213512e-08, "-11": 8.800128422893005e-09, "-12": 8.829688746939369e-10, "-13": 8.197988122798738e-11, "-14": 7.081789594302353e-12, "-15": 5.718826800971287e-13, "-16": 4.3331212301232424e-14, "-17": 3.064922918804298e-15, "-18": 1.8052744256392876e-16, "-2": 0.05214909951463247, "-3": 0.017647935712031087, "-4": 0.0047891188004887675, "-5": 0.001078881049450852, "-6": 0.00020714332655457824, "-7": 3.45916314424989e-05, "-8": 5.105408861249892e-06, "-9": 6.745968316195055e-07, "0": 0.2122973116005338, "1": 0.21115853023603162, "10": 4.152265139441655e-05, "11": 8.459598705790107e-06, "12": 1.5848030780746156e-06, "13": 2.747301703562699e-07, "14": 4.4310969200729794e-08, "15": 6.6810440170380135e-09, "16": 9.451644714531331e-10, "17": 1.2482318633208342e-10, "18": 1.3727393936766918e-11, "2": 0.1817963385894448, "3": 0.11486861663906993, "4": 0.05820124134021381, "5": 0.024480447995484326, "6": 0.008775783530262588, "7": 0.0027362461283625445, "8": 0.0007540216261653665, "9": 0.00018602303712406953} |
| Unadjusted home-win probability | 60.3% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 64.4% |
| P home draw | 79.3% |
| P draw away | 42.0% |
| P home away | 78.7% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.7% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.77 |
| Reference draw odds | 4.50 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:48Z |
| Market reference home last update utc | 2026-10-23T14:32:48Z |
| Market reference draw last update utc | 2026-10-23T14:32:48Z |
| Market reference away last update utc | 2026-10-23T14:32:48Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.42 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | +2.3% |
| Draw probability edge | -0.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.0463 |
| Raw ev home | 0.0794 |
| Raw edge prob draw | -0.0015 |
| Raw ev draw | -0.0765 |
| Raw edge prob away | -0.0448 |
| Raw ev away | -0.3000 |
| Elo home rating | 1,584.4079 |
| Elo away rating | 1,540.5013 |
| Elo rating diff | 103.9067 |
| Elo home expectancy | 0.6452 |

</details>


---

## 2026-10-31 — Bayern Munich vs Borussia Dortmund

The model's most likely 1X2 outcome is **Bayern Munich win** at **69.0%**. Expected goals are 2.72 for Bayern Munich and 1.39 for Borussia Dortmund (4.11 combined). The most likely exact score is 2-1 at 9.0%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 78.5%; Under 3.5 goals: 40.7%; Double Chance 1X: 85.5%; Double Chance X2: 31.0%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 60.1%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 69.0% | 1.45 |
| Draw | 16.5% | 6.07 |
| Borussia Dortmund win | 14.5% | 6.89 |

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
| Over 2.5 | 78.5% |
| Under 2.5 | 21.5% |
| Over 3.5 | 59.3% |
| Under 3.5 | 40.7% |
| Over 4.5 | 39.9% |
| Under 4.5 | 60.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.97% |
| 2 | 3-1 | 8.14% |
| 3 | 2-0 | 6.46% |
| 4 | 1-1 | 6.23% |
| 5 | 3-0 | 5.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 69.0% | 73.1% | 1.34 | -7.5% |
| Draw | 16.5% | 14.7% | 5.55 | -8.6% |
| Borussia Dortmund win | 14.5% | 12.2% | 7.60 | +10.3% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Bayern Munich |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7222 |
| Dc lambda away | 1.3880 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 70.2% |
| P btts no | 29.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 47.45 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.35 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.64 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.50 |
| Fair Under 4.5 odds | 1.67 |
| Goal margin distribution | {"-1": 0.08299739970204692, "-10": 1.4502895665660254e-07, "-11": 1.780239376423089e-08, "-12": 2.011416054805222e-09, "-13": 2.104657470615489e-10, "-14": 2.0503081923830203e-11, "-15": 1.8682148917166147e-12, "-16": 1.5986564042181868e-13, "-17": 1.2881547851931264e-14, "-18": 9.675565961421885e-16, "-19": 5.895821083741e-17, "-2": 0.041252643812294966, "-3": 0.015037022059700205, "-4": 0.004462528782638006, "-5": 0.0011099112133762076, "-6": 0.00023674825402917322, "-7": 4.411078346113906e-05, "-8": 7.285856576844126e-06, "-9": 1.0797833791329638e-06, "0": 0.16472115068102736, "1": 0.20783935954066154, "10": 0.0001506470077429114, "11": 3.626752691573601e-05, "12": 8.036652749075785e-06, "13": 1.64925750330928e-06, "14": 3.151083723318712e-07, "15": 5.631205508260401e-08, "16": 9.450688118913627e-09, "17": 1.4935167674458093e-09, "18": 2.2001494468639045e-10, "19": 2.629383004667226e-11, "2": 0.19574359386229348, "3": 0.13993661349258513, "4": 0.08144872778966471, "5": 0.03973061301682644, "6": 0.016621015856479404, "7": 0.006073643578060182, "8": 0.0019675188457402492, "9": 0.000571884957529663} |
| Raw goal margin distribution | {"-1": 0.09634612866420637, "-10": 1.6835441312901788e-07, "-11": 2.066560791418569e-08, "-12": 2.3349183312876107e-09, "-13": 2.4431560529118847e-10, "-14": 2.3800656118596334e-11, "-15": 2.1686856814295615e-12, "-16": 1.8557732671577211e-13, "-17": 1.4953327106532137e-14, "-18": 1.123171721481267e-15, "-19": 6.84406425688589e-17, "-2": 0.04788743433825945, "-3": 0.017455472909889917, "-4": 0.005180251113929319, "-5": 0.0012884216728919057, "-6": 0.00027482520929096517, "-7": 5.120525744279476e-05, "-8": 8.457663465380426e-06, "-9": 1.2534482857159962e-06, "0": 0.18207628803138112, "1": 0.19558219295855883, "10": 0.00014176271617715082, "11": 3.4128677373909435e-05, "12": 7.562697326360658e-06, "13": 1.5519938088891202e-06, "14": 2.965250981165204e-07, "15": 5.299109488885887e-08, "16": 8.893341046419591e-09, "17": 1.4054377632946953e-09, "18": 2.0703973232270142e-10, "19": 2.4743171616643238e-11, "2": 0.18419976577000088, "3": 0.1316839592008056, "4": 0.07664535163115153, "5": 0.03738753063227441, "6": 0.015640804213377307, "7": 0.005715455113367395, "8": 0.0018514859331150223, "9": 0.0005381584814390337} |
| Unadjusted home-win probability | 64.9% |
| Unadjusted draw probability | 18.2% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 41.2% |
| Raw p btts yes | 70.8% |
| P home draw | 85.5% |
| P draw away | 31.0% |
| P home away | 83.5% |
| Raw p home draw | 83.2% |
| Raw p draw away | 35.1% |
| Raw p home away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.35 |
| Reference draw odds | 6.25 |
| Reference away odds | 7.50 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:48Z |
| Market reference home last update utc | 2026-10-23T14:32:48Z |
| Market reference draw last update utc | 2026-10-23T14:32:48Z |
| Market reference away last update utc | 2026-10-23T14:32:48Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.63 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -4.1% |
| Draw probability edge | +1.7% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | -0.0814 |
| Raw ev home | -0.1298 |
| Raw edge prob draw | 0.0347 |
| Raw ev draw | 0.0105 |
| Raw edge prob away | 0.0467 |
| Raw ev away | 0.2806 |
| Elo home rating | 1,720.7230 |
| Elo away rating | 1,615.6111 |
| Elo rating diff | 165.1118 |
| Elo home expectancy | 0.7212 |

</details>


---

## 2026-10-31 — Borussia Monchengladbach vs SC Paderborn

The model's most likely 1X2 outcome is **Borussia Monchengladbach win** at **53.4%**. Expected goals are 1.56 for Borussia Monchengladbach and 0.85 for SC Paderborn (2.40 combined). The most likely exact score is 1-0 at 12.9%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.2%; Under 3.5 goals: 77.7%; Double Chance 1X: 78.5%; Double Chance X2: 46.6%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 53.4% | 1.87 |
| Draw | 25.1% | 3.98 |
| SC Paderborn win | 21.5% | 4.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.56 |
| SC Paderborn expected goals | 0.85 |
| Expected total goals | 2.40 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.2% |
| Under 2.5 | 55.8% |
| Over 3.5 | 22.3% |
| Under 3.5 | 77.7% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.90% |
| 2 | 1-1 | 11.82% |
| 3 | 2-0 | 11.08% |
| 4 | 2-1 | 9.40% |
| 5 | 0-0 | 9.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 53.4% | 54.1% | 1.86 | -0.7% |
| Draw | 25.1% | 22.1% | 4.10 | +3.0% |
| SC Paderborn win | 21.5% | 23.8% | 3.69 | -20.8% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | M'gladbach |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5557 |
| Dc lambda away | 0.8482 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.82 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.48 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.10 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.14178751718118926, "-10": 6.066110683125822e-09, "-11": 4.63152481109793e-10, "-12": 3.246385335911232e-11, "-13": 2.102734440628197e-12, "-14": 1.2618378114246628e-13, "-15": 6.558216199166972e-15, "-2": 0.05539612429717456, "-3": 0.014194112287902448, "-4": 0.00283068904085569, "-5": 0.0004605362354071444, "-6": 6.316372395244928e-05, "-7": 7.48036604782693e-06, "-8": 7.790183500759458e-07, "-9": 7.236825031732297e-08, "0": 0.25130393254851013, "1": 0.24614034082018366, "10": 2.361765498065403e-06, "11": 3.3074771055602644e-07, "12": 4.252255267719225e-08, "13": 5.051845917741542e-09, "14": 5.56052263710685e-10, "15": 5.300834117215913e-11, "2": 0.16835831089809028, "3": 0.07912428954337758, "4": 0.02894277434283948, "5": 0.008636906333114177, "6": 0.002172743893991542, "7": 0.00047196530028662616, "8": 9.01532349891213e-05, "9": 1.5361304857399332e-05} |
| Raw goal margin distribution | {"-1": 0.126386010444811, "-10": 5.407186354615374e-09, "-11": 4.128430730631926e-10, "-12": 2.8937504452387128e-11, "-13": 1.8743273192116843e-12, "-14": 1.1247721237023861e-13, "-15": 5.845837472335751e-15, "-2": 0.04937878371251711, "-3": 0.012652293089956565, "-4": 0.0025232086843471617, "-5": 0.0004105110140549332, "-6": 5.6302636747535237e-05, "-7": 6.667819849356177e-06, "-8": 6.943983736140915e-07, "-9": 6.45073319733065e-08, "0": 0.28171508346425833, "1": 0.24287423304096165, "10": 2.3304265446852872e-06, "11": 3.2635892297733327e-07, "12": 4.1958308556831595e-08, "13": 4.9848115047867775e-09, "14": 5.486738444799817e-10, "15": 5.230495807417063e-11, "2": 0.1661243154990076, "3": 0.07807436632988922, "4": 0.028558724251259923, "5": 0.008522300710691627, "6": 0.002143913123258161, "7": 0.0004657026554326681, "8": 8.895696549043271e-05, "9": 1.5157471234976561e-05} |
| Unadjusted home-win probability | 52.7% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 77.8% |
| Raw p btts yes | 46.4% |
| P home draw | 78.5% |
| P draw away | 46.6% |
| P home away | 74.9% |
| Raw p home draw | 80.9% |
| Raw p draw away | 47.3% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.02, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.81 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:48Z |
| Market reference home last update utc | 2026-10-23T14:32:48Z |
| Market reference draw last update utc | 2026-10-23T14:32:48Z |
| Market reference away last update utc | 2026-10-23T14:32:48Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -0.7% |
| Draw probability edge | +3.0% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -20.9% |
| Under 2.5 probability edge | +20.9% |
| Raw edge prob home | -0.0142 |
| Raw ev home | -0.0200 |
| Raw edge prob draw | 0.0608 |
| Raw ev draw | 0.1550 |
| Raw edge prob away | -0.0467 |
| Raw ev away | -0.2937 |
| Elo home rating | 1,413.4046 |
| Elo away rating | 1,399.4332 |
| Elo rating diff | 73.9714 |
| Elo home expectancy | 0.6049 |

</details>


---

## 2026-10-31 — FC Schalke 04 vs RB Leipzig

The model's most likely 1X2 outcome is **RB Leipzig win** at **58.2%**. Expected goals are 0.91 for FC Schalke 04 and 2.08 for RB Leipzig (3.00 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.3%; Under 3.5 goals: 65.5%; Double Chance 1X: 41.8%; Double Chance X2: 80.4%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 19.6% | 5.10 |
| Draw | 22.2% | 4.51 |
| RB Leipzig win | 58.2% | 1.72 |

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
| 1 | 1-1 | 10.54% |
| 2 | 0-2 | 9.97% |
| 3 | 1-2 | 9.10% |
| 4 | 0-1 | 8.60% |
| 5 | 0-3 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 19.6% | 24.8% | 4.04 | -20.7% |
| Draw | 22.2% | 22.1% | 3.68 | -18.5% |
| RB Leipzig win | 58.2% | 53.1% | 1.88 | +9.4% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Schalke 04 |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9121 |
| Dc lambda away | 2.0844 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.55 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.16 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.53 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.21078505425772665, "-10": 2.324908661943769e-05, "-11": 4.343650661382609e-06, "-12": 7.454956445184707e-07, "-13": 1.1830611491798428e-07, "-14": 1.7457069644736427e-08, "-15": 2.4063893469591408e-09, "-16": 3.0969300355000723e-10, "-17": 3.415237054355621e-11, "-2": 0.17999554036313112, "-3": 0.10918455769222797, "-4": 0.05221621445958475, "-5": 0.0205218365383303, "-6": 0.006829981500080413, "-7": 0.001968613341117871, "-8": 0.0004999856922600369, "-9": 0.00011343986104738583, "0": 0.22159668642787753, "1": 0.1283516100027658, "10": 8.852577914085977e-09, "11": 7.237486701204784e-10, "12": 5.4355941939933333e-11, "13": 3.77466257302769e-12, "14": 2.437313048148696e-13, "15": 1.470194832507945e-14, "16": 8.279601153902904e-16, "17": 3.9954702638438407e-17, "2": 0.05097689672829957, "3": 0.013531373897921957, "4": 0.0028317511501385027, "5": 0.00048700671884587953, "6": 7.092629643884128e-05, "7": 8.945759249737647e-06, "8": 9.94222037972245e-07, "9": 9.870985670189632e-08} |
| Raw goal margin distribution | {"-1": 0.22941669855211655, "-10": 2.530411235922847e-05, "-11": 4.727593224800888e-06, "-12": 8.113912542456294e-07, "-13": 1.2876339073749275e-07, "-14": 1.9000129294712524e-08, "-15": 2.6190941352764965e-09, "-16": 3.370672872862246e-10, "-17": 3.717115582706933e-11, "-2": 0.19590564791051876, "-3": 0.11883556377767161, "-4": 0.05683169318807671, "-5": 0.022335796071638953, "-6": 0.007433695014280376, "-7": 0.0021426223744151363, "-8": 0.0005441802657476012, "-9": 0.00012346700052974995, "0": 0.221974582627242, "1": 0.09445238681258222, "10": 6.514504285624101e-09, "11": 5.325978329670999e-10, "12": 3.999987575973697e-11, "13": 2.777728221928074e-12, "14": 1.793588992005116e-13, "15": 1.0818984740971124e-14, "16": 6.092857665170602e-16, "17": 2.940217912736867e-17, "2": 0.03751327753646919, "3": 0.009957573274574917, "4": 0.0020838511880302323, "5": 0.00035838231392474376, "6": 5.2193797851705574e-05, "7": 6.583075295824089e-06, "8": 7.316358907077575e-07, "9": 7.263938151785683e-08} |
| Unadjusted home-win probability | 14.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 63.4% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 64.8% |
| Raw p btts yes | 53.4% |
| P home draw | 41.8% |
| P draw away | 80.4% |
| P home away | 77.8% |
| Raw p home draw | 36.6% |
| Raw p draw away | 85.6% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.60 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.79 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:48Z |
| Market reference home last update utc | 2026-10-23T14:32:48Z |
| Market reference draw last update utc | 2026-10-23T14:32:48Z |
| Market reference away last update utc | 2026-10-23T14:32:48Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -5.2% |
| Draw probability edge | +0.0% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | -0.1037 |
| Raw ev home | -0.4165 |
| Raw edge prob draw | 0.0008 |
| Raw ev draw | -0.1831 |
| Raw edge prob away | 0.1029 |
| Raw ev away | 0.1912 |
| Elo home rating | 1,438.7706 |
| Elo away rating | 1,513.4005 |
| Elo rating diff | -14.6300 |
| Elo home expectancy | 0.4790 |

</details>


---

## 2026-10-31 — Werder Bremen vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **39.8%**. Expected goals are 1.82 for Werder Bremen and 1.59 for TSG Hoffenheim (3.42 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 66.6%; Under 3.5 goals: 55.6%; Double Chance 1X: 60.2%; Double Chance X2: 63.6%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 74.0%; BTTS Yes (both teams score): 67.8%; BTTS No (at least one team does not score): 32.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 36.4% | 2.74 |
| Draw | 23.7% | 4.22 |
| TSG Hoffenheim win | 39.8% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.82 |
| TSG Hoffenheim expected goals | 1.59 |
| Expected total goals | 3.42 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 66.6% |
| Under 2.5 | 33.4% |
| Over 3.5 | 44.4% |
| Under 3.5 | 55.6% |
| Over 4.5 | 26.0% |
| Under 4.5 | 74.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.24% |
| 2 | 1-2 | 9.18% |
| 3 | 2-1 | 7.46% |
| 4 | 2-2 | 6.69% |
| 5 | 0-1 | 5.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 36.4% | 30.4% | 2.92 | +6.4% |
| Draw | 23.7% | 22.9% | 3.91 | -7.2% |
| TSG Hoffenheim win | 39.8% | 46.7% | 2.21 | -12.0% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8230 |
| Dc lambda away | 1.5937 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 67.8% |
| P btts no | 32.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.84 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.43 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 2.99 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.85 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.19908710104733138, "-10": 1.4997287061415112e-06, "-11": 2.126893209816809e-07, "-12": 2.7738651855039264e-08, "-13": 3.34772911264501e-09, "-14": 3.7564936067751607e-10, "-15": 3.8933700797193485e-11, "-16": 3.2821123030188447e-12, "-2": 0.12069323944705798, "-3": 0.052829582519869064, "-4": 0.01857527959840324, "-5": 0.005427618739481404, "-6": 0.0013525708866784917, "-7": 0.0002933019620879541, "-8": 5.623042305215063e-05, "-9": 9.653516392537882e-06, "0": 0.23724508017893542, "1": 0.1630934388607377, "10": 4.085738449458074e-06, "11": 6.627919384846466e-07, "12": 9.887592466923556e-08, "13": 1.364989129131788e-08, "14": 1.7520044829115124e-09, "15": 2.0770737707421687e-10, "16": 2.002872700114972e-11, "2": 0.11218928955286435, "3": 0.05617192508187849, "4": 0.022591817141882412, "5": 0.007550901644554427, "6": 0.00215240102788099, "7": 0.0005338900157713974, "8": 0.00011707976912509633, "9": 2.2991627797903145e-05} |
| Raw goal margin distribution | {"-1": 0.1648191563731347, "-10": 1.241587319492139e-06, "-11": 1.7608008891264833e-07, "-12": 2.296412561951333e-08, "-13": 2.771499937511043e-09, "-14": 3.1099056841586133e-10, "-15": 3.2232222409787755e-11, "-16": 2.717177446754045e-12, "-2": 0.09991886868087724, "-3": 0.04373627008813406, "-4": 0.015378002375332496, "-5": 0.004493387753652928, "-6": 0.001119759096920157, "-7": 0.00024281724782575876, "-8": 4.6551739621526644e-05, "-9": 7.99190113011919e-06, "0": 0.2455615179104579, "1": 0.1900552851648496, "10": 4.761173665507151e-06, "11": 7.723616091093881e-07, "12": 1.1522163117178356e-07, "13": 1.5906427628003986e-08, "14": 2.0416376890192713e-09, "15": 2.4204459147121744e-10, "16": 2.3339782693176178e-11, "2": 0.13073589941664118, "3": 0.06545800563326658, "4": 0.026326590936370537, "5": 0.008799181471260274, "6": 0.002508225922517572, "7": 0.000622150222000905, "8": 0.00013643485025234626, "9": 2.6792496424492896e-05} |
| Unadjusted home-win probability | 42.5% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 33.0% |
| Raw p over 1 5 | 86.6% |
| Raw p under 3 5 | 55.5% |
| Raw p btts yes | 67.9% |
| P home draw | 60.2% |
| P draw away | 63.6% |
| P home away | 76.3% |
| Raw p home draw | 67.0% |
| Raw p draw away | 57.5% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.02 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:48Z |
| Market reference home last update utc | 2026-10-23T14:32:48Z |
| Market reference draw last update utc | 2026-10-23T14:32:48Z |
| Market reference away last update utc | 2026-10-23T14:32:48Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | +6.0% |
| Draw probability edge | +0.8% |
| Away probability edge | -6.9% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.1205 |
| Raw ev home | 0.2400 |
| Raw edge prob draw | 0.0166 |
| Raw ev draw | -0.0399 |
| Raw edge prob away | -0.1371 |
| Raw ev away | -0.2712 |
| Elo home rating | 1,423.4938 |
| Elo away rating | 1,492.4811 |
| Elo rating diff | -8.9873 |
| Elo home expectancy | 0.4871 |

</details>


---

## 2026-11-01 — Eintracht Frankfurt vs Hamburger SV

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **59.5%**. Expected goals are 1.97 for Eintracht Frankfurt and 1.05 for Hamburger SV (3.03 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 59.0%; Under 3.5 goals: 63.9%; Double Chance 1X: 81.3%; Double Chance X2: 40.5%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 59.5% | 1.68 |
| Draw | 21.9% | 4.58 |
| Hamburger SV win | 18.7% | 5.35 |

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
| 1 | 1-1 | 10.29% |
| 2 | 2-1 | 10.27% |
| 3 | 2-0 | 9.75% |
| 4 | 1-0 | 8.73% |
| 5 | 3-1 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 59.5% | 61.4% | 1.69 | +0.5% |
| Draw | 21.9% | 19.9% | 4.33 | -5.4% |
| Hamburger SV win | 18.7% | 18.7% | 4.30 | -19.7% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9713 |
| Dc lambda away | 1.0539 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.22 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.49 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.19 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.1152964530227509, "-10": 2.734179329860747e-08, "-11": 2.579581112115523e-09, "-12": 2.2361222369998144e-10, "-13": 1.7925648449738052e-11, "-14": 1.3359178311907982e-12, "-15": 9.242013971204247e-14, "-16": 5.388106617659736e-15, "-2": 0.051327044639138765, "-3": 0.015574582786200364, "-4": 0.003739262733268775, "-5": 0.0007393141215225941, "-6": 0.00012394598480573051, "-7": 1.8011511092328626e-05, "-8": 2.3077328826468604e-06, "-9": 2.642531952961786e-07, "0": 0.21854499622812779, "1": 0.23240826051878094, "10": 1.4771613370625583e-05, "11": 2.606672713778331e-06, "12": 4.226386779991362e-07, "13": 6.337018208504134e-08, "14": 8.83336564745823e-09, "15": 1.143008508525956e-09, "16": 1.246394157654912e-10, "2": 0.18512119488528408, "3": 0.10506611866277174, "4": 0.04718116169159897, "5": 0.01744809557736509, "6": 0.005471266554171712, "7": 0.0014871060563103843, "8": 0.0003563803188175348, "9": 7.63281616104404e-05} |
| Raw goal margin distribution | {"-1": 0.11505054667827835, "-10": 2.7283478231100076e-08, "-11": 2.5740793352184872e-09, "-12": 2.2313529953563972e-10, "-13": 1.7887416304975492e-11, "-14": 1.3330685616619338e-12, "-15": 9.222302437920783e-14, "-16": 5.3766147671540166e-15, "-2": 0.051217573397059006, "-3": 0.01554136503648447, "-4": 0.003731287566594922, "-5": 0.0007377372990942001, "-6": 0.00012368163058462005, "-7": 1.7973095818180798e-05, "-8": 2.3028109085330615e-06, "-9": 2.6368959133814836e-07, "0": 0.23802440274859538, "1": 0.22495061061671498, "10": 1.4297613346870404e-05, "11": 2.523028300859298e-06, "12": 4.0907680507536874e-07, "13": 6.133672324340857e-08, "14": 8.549915531233313e-09, "15": 1.1063309942558454e-09, "16": 1.2063991452271174e-10, "2": 0.17918091953609952, "3": 0.10169469663238935, "4": 0.04566718544530165, "5": 0.01688821105353915, "6": 0.005295701406913969, "7": 0.0014393869420652663, "8": 0.0003449445822228235, "9": 7.387889967074708e-05} |
| Unadjusted home-win probability | 57.6% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 57.2% |
| P home draw | 81.3% |
| P draw away | 40.5% |
| P home away | 78.1% |
| Raw p home draw | 81.4% |
| Raw p draw away | 42.4% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.56 |
| Reference draw odds | 4.35 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:48Z |
| Market reference home last update utc | 2026-10-23T14:32:48Z |
| Market reference draw last update utc | 2026-10-23T14:32:48Z |
| Market reference away last update utc | 2026-10-23T14:32:48Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.86 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | -1.9% |
| Draw probability edge | +1.9% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0382 |
| Raw ev home | -0.0273 |
| Raw edge prob draw | 0.0390 |
| Raw ev draw | 0.0306 |
| Raw edge prob away | -0.0008 |
| Raw ev away | -0.1984 |
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
| 1 | 1-1 | 13.02% |
| 2 | 1-0 | 9.32% |
| 3 | 0-1 | 9.04% |
| 4 | 0-0 | 8.93% |
| 5 | 1-2 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 39.8% | 35.5% | 2.50 | -0.6% |
| Draw | 27.3% | 25.4% | 3.58 | -2.3% |
| 1. FC Köln win | 32.9% | 39.1% | 2.70 | -11.1% |
| Over 2.5 | 46.3% | 58.1% | 1.70 | -21.2% |
| Under 2.5 | 53.7% | 41.9% | 2.34 | +25.5% |

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
| Market best home last update utc | 2026-10-23T14:32:47Z |
| Market best draw last update utc | 2026-10-23T14:32:47Z |
| Market best away last update utc | 2026-10-23T14:32:47Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Union Berlin |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4350 |
| Dc lambda away | 1.0708 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:32:41.860332+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.20 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.66 |
| Fair Over 2.5 odds | 2.16 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 4.12 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.02 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.1970485154669088, "-10": 6.298407210930685e-08, "-11": 6.0610339102235674e-09, "-12": 5.354862608768485e-10, "-13": 4.3520199407017924e-11, "-14": 2.999339428884043e-12, "-2": 0.09332516037892867, "-3": 0.02975883242100747, "-4": 0.007422696587423809, "-5": 0.0015146650075049614, "-6": 0.00026100642738294684, "-7": 3.887989596943535e-05, "-8": 5.096874086991696e-06, "-9": 5.963454505629568e-07, "0": 0.2728752801017676, "1": 0.19824647399241066, "10": 8.647219918372232e-07, "11": 1.1152176212520424e-07, "12": 1.3204695239945925e-08, "13": 1.4382622013726614e-09, "14": 1.32843389394241e-10, "2": 0.12311398489091437, "3": 0.05261283112370088, "4": 0.017587521178577224, "5": 0.004809796009900245, "6": 0.00111078091235218, "7": 0.00022175296783313812, "8": 3.895968100101411e-05, "9": 6.109090212447584e-06} |
| Raw goal margin distribution | {"-1": 0.1601574764116858, "-10": 5.119231687311161e-08, "-11": 4.9262989533665175e-09, "-12": 4.3523356667748213e-10, "-13": 3.537243248671849e-11, "-14": 2.4378089461567415e-12, "-2": 0.0758530057259687, "-3": 0.024187441809513186, "-4": 0.006033033797765758, "-5": 0.0012310923765970724, "-6": 0.000212141312700743, "-7": 3.1600877615641566e-05, "-8": 4.142647253273981e-06, "-9": 4.846988174736702e-07, "0": 0.29213111489122723, "1": 0.21938410527125754, "10": 9.569212337912816e-07, "11": 1.234125455520009e-07, "12": 1.461261929282066e-08, "13": 1.5916140138043e-09, "14": 1.4700754841456857e-10, "2": 0.13624076573844307, "3": 0.05822256834844265, "4": 0.019462755225846617, "5": 0.005322630828781475, "6": 0.001229215691463461, "7": 0.0002453969317062423, "8": 4.311367857361385e-05, "9": 6.760459660586533e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.03, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:32:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-23T14:32:48Z |
| Market reference home last update utc | 2026-10-23T14:32:48Z |
| Market reference draw last update utc | 2026-10-23T14:32:48Z |
| Market reference away last update utc | 2026-10-23T14:32:48Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.34 |
| Market reference over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market best over 2 5 last update utc | 2026-10-23T14:32:47Z |
| Market best under 2 5 last update utc | 2026-10-23T14:32:47Z |
| Home probability edge | +4.2% |
| Draw probability edge | +1.9% |
| Away probability edge | -6.2% |
| Over 2.5 probability edge | -11.8% |
| Under 2.5 probability edge | +11.8% |
| Raw edge prob home | 0.0848 |
| Raw ev home | 0.1004 |
| Raw edge prob draw | 0.0385 |
| Raw ev draw | 0.0458 |
| Raw edge prob away | -0.1233 |
| Raw ev away | -0.2772 |
| Elo home rating | 1,422.1325 |
| Elo away rating | 1,400.3928 |
| Elo rating diff | 81.7397 |
| Elo home expectancy | 0.6155 |

</details>


---
