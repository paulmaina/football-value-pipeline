# Ligue 1 — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,743 |
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
| Training sha256 | 76cb9f16a8086c55e6bdded4a1a1c7cf4b2473c7b2e963a52096785ba938b944 |
| Training as of utc | 2026-10-23T16:23:20.185456+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 50, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-23T16:23:20.185456+00:00', 'observations': 168, 'observations_sha256': 'f347bae8059efc361920118b049fc7be40b741bf6bf2a2254495b5eb43cf1c39', 'eligible_training_matches': 75, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 87, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 75, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '690002b3b1752dfb6846f7110eff19a71928ab9a0848197ade56b0ca5acc9575', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5079.453 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.187 |
| Dixon-Coles low-score adjustment | -0.057 |
| Xi per day | 0 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1743, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-18'} |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 32.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261023T162320185456Z_142fa0226b5a0cd750ec875c1fc61c9953573f3a569e6b3c6dce5c2d7a11a9b2.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **38.0%**. Expected goals are 1.22 for Brest and 1.24 for Nice (2.46 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.6%; Double Chance 1X: 66.5%; Double Chance X2: 62.0%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 38.0% | 2.63 |
| Draw | 28.5% | 3.51 |
| Nice win | 33.5% | 2.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.22 |
| Nice expected goals | 1.24 |
| Expected total goals | 2.46 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.54% |
| 2 | 1-0 | 10.50% |
| 3 | 0-0 | 9.21% |
| 4 | 0-1 | 9.15% |
| 5 | 2-1 | 8.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 38.0% | 41.0% | 2.40 | -8.7% |
| Draw | 28.5% | 28.2% | 3.49 | -0.6% |
| Nice win | 33.5% | 30.8% | 3.08 | +3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 8aa36b30d655d6c81ed98bf9ec1b4039 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Brest |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2187 |
| Dc lambda away | 1.2397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.86 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.66 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.18692099243386423, "-10": 2.1475846599778468e-07, "-11": 2.3932680170269905e-08, "-12": 2.4485532478997276e-09, "-13": 2.3047473934536575e-10, "-14": 1.8421311649600115e-11, "-2": 0.09800543898490044, "-3": 0.036243993985704215, "-4": 0.010478488974745336, "-5": 0.002477580736977282, "-6": 0.0004945943108915562, "-7": 8.53399443401343e-05, "-8": 1.2957495177627263e-05, "-9": 1.7558067108957183e-06, "0": 0.2847906620269768, "1": 0.21474950825823694, "10": 2.1156360930739849e-07, "11": 2.317561079475757e-08, "12": 2.3307655056486043e-09, "13": 2.1565599673606028e-10, "14": 1.6943687538324797e-11, "2": 0.11075094317963671, "3": 0.040260807598323574, "4": 0.011441797855585314, "5": 0.00265933226701252, "6": 0.0005218468680392408, "7": 8.851064334080086e-05, "8": 1.3210321143051603e-05, "9": 1.7596172125283476e-06} |
| Raw goal margin distribution | {"-1": 0.20179382078186506, "-10": 2.31846251374246e-07, "-11": 2.583694271159986e-08, "-12": 2.643378407357606e-09, "-13": 2.4881302865252676e-10, "-14": 1.988704860371172e-11, "-2": 0.10580348270494232, "-3": 0.039127836480741654, "-4": 0.011312235713613882, "-5": 0.0026747155399738697, "-6": 0.0005339479233029097, "-7": 9.213022683795403e-05, "-8": 1.3988490140191909e-05, "-9": 1.8955117888722293e-06, "0": 0.28741553004348547, "1": 0.1982362450862622, "10": 1.9529532731485093e-07, "11": 2.1393511439424536e-08, "12": 2.1515402096323092e-09, "13": 1.9907302871158986e-10, "14": 1.5640794816039207e-11, "2": 0.10223469796863227, "3": 0.03716493410003417, "4": 0.010561975495654163, "5": 0.0024548416772874216, "6": 0.0004817192107640479, "7": 8.170457631479465e-05, "8": 1.2194507363589102e-05, "9": 1.6243106297655316e-06} |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 50.8% |
| P home draw | 66.5% |
| P draw away | 62.0% |
| P home away | 71.5% |
| Raw p home draw | 63.9% |
| Raw p draw away | 64.9% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.75, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.0, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.28, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.25, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:42Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.21, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.22, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.71, "price": 2.22, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.38 |
| Reference draw odds | 3.42 |
| Reference away odds | 3.14 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | -2.9% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -11.6% |
| Under 2.5 probability edge | +11.6% |
| Raw edge prob home | -0.0585 |
| Raw ev home | -0.1570 |
| Raw edge prob draw | 0.0052 |
| Raw ev draw | 0.0031 |
| Raw edge prob away | 0.0533 |
| Raw ev away | 0.1130 |
| Market p home draw | 68.2% |
| Market home draw odds | 1.42 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:23:26Z |
| Market reference home draw last update utc | 2026-10-23T16:23:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.4% |
| Market draw away odds | 1.63 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:23:26Z |
| Market reference draw away last update utc | 2026-10-23T16:23:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.3% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:23:26Z |
| Market reference home away last update utc | 2026-10-23T16:23:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.42 |
| Market reference dc draw away odds | 1.63 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 81.1% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-23T16:23:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.2% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:23:13Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market reference under 3 5 last update utc | 2026-10-23T16:23:14Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.1% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:23:26Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.51 |
| Market reference btts yes last update utc | 2026-10-23T16:23:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,500.5834 |
| Elo away rating | 1,443.8626 |
| Elo rating diff | 116.7207 |
| Elo home expectancy | 0.6619 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **45.9%**. Expected goals are 1.68 for RC Lens and 1.03 for Paris FC (2.70 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.8%; Double Chance 1X: 71.6%; Double Chance X2: 54.1%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 45.9% | 2.18 |
| Draw | 25.7% | 3.89 |
| Paris FC win | 28.4% | 3.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.68 |
| Paris FC expected goals | 1.03 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.26% |
| 2 | 1-0 | 9.34% |
| 3 | 2-1 | 8.53% |
| 4 | 2-0 | 8.32% |
| 5 | 0-1 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 45.9% | 39.8% | 2.41 | +10.5% |
| Draw | 25.7% | 25.9% | 3.69 | -5.1% |
| Paris FC win | 28.4% | 34.4% | 2.88 | -18.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | fc6c50376190b578cfeb38c029db8487 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6772 |
| Dc lambda away | 1.0253 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.51 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.40 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1782347273703797, "-10": 3.504473554998976e-08, "-11": 3.224838268412969e-09, "-12": 2.725493574071849e-10, "-13": 2.1290850551960547e-11, "-14": 1.5381908244447714e-12, "-15": 9.432426334035437e-14, "-2": 0.07631148312253808, "-3": 0.023028652134908782, "-4": 0.0054579042070870476, "-5": 0.0010606922047433891, "-6": 0.00017432028986956533, "-7": 2.4788478374045878e-05, "-8": 3.104097198234367e-06, "-9": 3.470848715878044e-07, "0": 0.2570696326766063, "1": 0.20700149369436044, "10": 3.353741782084575e-06, "11": 5.048482414779181e-07, "12": 6.979818764175097e-08, "13": 8.91944988459819e-09, "14": 1.0541474176106443e-09, "15": 1.0574519185823507e-10, "2": 0.1424059488200881, "3": 0.07029959639480839, "4": 0.027255634442537337, "5": 0.008664945560532204, "6": 0.0023295416272024077, "7": 0.000541899161796816, "8": 0.00011100690571431579, "9": 2.030469378301992e-05} |
| Raw goal margin distribution | {"-1": 0.14085795135543636, "-10": 2.769566699034288e-08, "-11": 2.5485724282974562e-09, "-12": 2.1539429882168263e-10, "-13": 1.682604526968473e-11, "-14": 1.2156239781194702e-12, "-15": 7.454396061449595e-14, "-2": 0.06030855678982586, "-3": 0.018199420562186805, "-4": 0.004313352491105287, "-5": 0.0008382593739342425, "-6": 0.0001377643923436294, "-7": 1.959020182262701e-05, "-8": 2.4531514065878157e-06, "-9": 2.742993168594353e-07, "0": 0.25555440017109565, "1": 0.2345937472551493, "10": 3.800778622143912e-06, "11": 5.721419621171747e-07, "12": 7.910193350910355e-08, "13": 1.0108367502757807e-08, "14": 1.1946599439603814e-09, "15": 1.198404918220835e-10, "2": 0.16138794251627972, "3": 0.07967017751636636, "4": 0.030888672847608274, "5": 0.009819939037775647, "6": 0.0026400577597723855, "7": 0.0006141315829732248, "8": 0.00012580356555866662, "9": 2.3011206906845376e-05} |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 52.8% |
| P home draw | 71.6% |
| P draw away | 54.1% |
| P home away | 74.3% |
| Raw p home draw | 77.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.55, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.27, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.43, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.55, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.14, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.71, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.55, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.12, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.76, "price": 2.12, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.45 |
| Reference draw odds | 3.72 |
| Reference away odds | 2.82 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | +6.1% |
| Draw probability edge | -0.2% |
| Away probability edge | -6.0% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.1223 |
| Raw ev home | 0.2526 |
| Raw edge prob draw | -0.0030 |
| Raw ev draw | -0.0570 |
| Raw edge prob away | -0.1192 |
| Raw ev away | -0.3529 |
| Market p home draw | 66.5% |
| Market home draw odds | 1.45 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:23:26Z |
| Market reference home draw last update utc | 2026-10-23T16:23:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.9% |
| Market draw away odds | 1.61 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:23:26Z |
| Market reference draw away last update utc | 2026-10-23T16:23:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:23:26Z |
| Market reference home away last update utc | 2026-10-23T16:23:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.45 |
| Market reference dc draw away odds | 1.61 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 82.6% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-23T16:23:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:23:13Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.40 |
| Market reference under 3 5 last update utc | 2026-10-23T16:23:14Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.9% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:23:26Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.48 |
| Market reference btts yes last update utc | 2026-10-23T16:23:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,574.7541 |
| Elo away rating | 1,494.3238 |
| Elo rating diff | 140.4303 |
| Elo home expectancy | 0.6918 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **45.0%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 53.2%; Under 3.5 goals: 68.7%; Double Chance 1X: 72.2%; Double Chance X2: 55.0%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 45.0% | 2.22 |
| Draw | 27.3% | 3.66 |
| Lille win | 27.8% | 3.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.56 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.90% |
| 2 | 2-1 | 9.43% |
| 3 | 1-0 | 8.89% |
| 4 | 2-0 | 7.46% |
| 5 | 0-0 | 6.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 45.0% | 46.4% | 2.07 | -6.9% |
| Draw | 27.3% | 28.4% | 3.36 | -8.3% |
| Lille win | 27.8% | 25.2% | 3.95 | +9.6% |
| Over 2.5 | 53.2% | 52.4% | 1.83 | -2.6% |
| Under 2.5 | 46.8% | 47.6% | 2.06 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | c177a3c900d7febf9870ca8de90a9e35 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5579 |
| Dc lambda away | 1.2641 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.51 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.47 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.15699144025558417, "-10": 1.8695035622859877e-07, "-11": 2.117159786219797e-08, "-12": 2.202668922295429e-09, "-13": 2.1183892382543502e-10, "-14": 1.881758292466282e-11, "-15": 1.4017549356566926e-12, "-2": 0.08019925494754768, "-3": 0.0293799047179335, "-4": 0.008497337675696588, "-5": 0.0020213211758637463, "-6": 0.0004073812586952412, "-7": 7.112963339530181e-05, "-8": 1.0946057973733419e-05, "-9": 1.505042874102387e-06, "0": 0.2728575331674026, "1": 0.21966874975367853, "10": 1.7036973370917469e-06, "11": 2.3778908749890948e-07, "12": 3.0490155884129023e-08, "13": 3.6140014154980805e-09, "14": 3.956567067416062e-10, "15": 3.632443966315405e-11, "2": 0.13729647585957652, "3": 0.06198856397028281, "4": 0.022096129474713712, "5": 0.006477997726236481, "6": 0.0016090837448216682, "7": 0.0003462583926070851, "8": 6.567190564617695e-05, "9": 1.1128660225976728e-05} |
| Raw goal margin distribution | {"-1": 0.1712855768930864, "-10": 2.039722647607504e-07, "-11": 2.309928074849943e-08, "-12": 2.4032228537149525e-09, "-13": 2.3112694690091277e-10, "-14": 2.0530931761228394e-11, "-15": 1.529385311873062e-12, "-2": 0.08750143082783646, "-3": 0.032054957394380294, "-4": 0.009271023843513512, "-5": 0.0022053633187285727, "-6": 0.00044447349357038614, "-7": 7.760601642021468e-05, "-8": 1.194270115417587e-05, "-9": 1.6420776605384802e-06, "0": 0.26194497216560436, "1": 0.21265143411010703, "10": 1.6492727455697806e-06, "11": 2.3019291787784239e-07, "12": 2.951614821075468e-08, "13": 3.498552182517505e-09, "14": 3.8301745786885957e-10, "15": 3.5164055862645115e-11, "2": 0.132910541542852, "3": 0.06000834001872406, "4": 0.021390268876885585, "5": 0.006271058164581427, "6": 0.001557681583399003, "7": 0.0003351971723020384, "8": 6.357401738782967e-05, "9": 1.0773155305120635e-05} |
| Unadjusted home-win probability | 43.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 72.2% |
| P draw away | 55.0% |
| P home away | 72.7% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.34, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.82, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.73, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.91, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.81, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.46, "price": 2.81, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.09 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market best over 2 5 last update utc | 2026-10-23T16:23:13Z |
| Market best under 2 5 last update utc | 2026-10-23T16:23:13Z |
| Home probability edge | -1.4% |
| Draw probability edge | -1.1% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | -0.0287 |
| Raw ev home | -0.0991 |
| Raw edge prob draw | -0.0218 |
| Raw ev draw | -0.1199 |
| Raw edge prob away | 0.0505 |
| Raw ev away | 0.1963 |
| Market p home draw | 75.4% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:23:26Z |
| Market reference home draw last update utc | 2026-10-23T16:23:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.1% |
| Market draw away odds | 1.82 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:23:26Z |
| Market reference draw away last update utc | 2026-10-23T16:23:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:23:26Z |
| Market reference home away last update utc | 2026-10-23T16:23:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.28 |
| Market reference dc draw away odds | 1.82 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 78.2% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:23:13Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market reference over 1 5 last update utc | 2026-10-23T16:23:14Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.5% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:23:13Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 2.80 |
| Market reference under 3 5 last update utc | 2026-10-23T16:23:14Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.8% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:23:26Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.31 |
| Market reference btts yes last update utc | 2026-10-23T16:23:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,571.2203 |
| Elo away rating | 1,580.6829 |
| Elo rating diff | 50.5374 |
| Elo home expectancy | 0.5722 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **38.9%**. Expected goals are 1.19 for Angers and 1.30 for Lorient (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.0%; Double Chance 1X: 61.1%; Double Chance X2: 67.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 32.4% | 3.08 |
| Draw | 28.7% | 3.49 |
| Lorient win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.19 |
| Lorient expected goals | 1.30 |
| Expected total goals | 2.49 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.66% |
| 2 | 0-1 | 10.18% |
| 3 | 0-0 | 9.09% |
| 4 | 1-0 | 8.94% |
| 5 | 1-2 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 32.4% | 31.7% | 2.97 | -3.7% |
| Draw | 28.7% | 28.9% | 3.34 | -4.2% |
| Lorient win | 38.9% | 39.4% | 2.52 | -2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 1a83b5ebabe7cb572ae6e029b3149c42 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1904 |
| Dc lambda away | 1.2991 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.00 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.16 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.33 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21109318138471375, "-10": 3.6476677072976424e-07, "-11": 4.2584040182331656e-08, "-12": 4.564227653617736e-09, "-13": 4.499948795277656e-10, "-14": 3.7602337425735285e-11, "-2": 0.11537023132897073, "-3": 0.04460478519506433, "-4": 0.013492537175717807, "-5": 0.0033394052012172193, "-6": 0.0006980036784338901, "-7": 0.00012612681992180472, "-8": 2.0057515916247943e-05, "-9": 2.8469039450675086e-06, "0": 0.2869439507452968, "1": 0.18601382609958123, "10": 1.4683976653539683e-07, "11": 1.570781794956511e-08, "12": 1.5426836387844901e-09, "13": 1.3936628611253655e-10, "14": 1.0671011220383261e-11, "2": 0.09345392488585019, "3": 0.033107456248500394, "4": 0.009176531594857084, "5": 0.0020811080996011337, "6": 0.0003985876249276534, "7": 6.599546979330782e-05, "8": 9.61666314544102e-06, "9": 1.2507216047274702e-06} |
| Raw goal margin distribution | {"-1": 0.20826178273993898, "-10": 3.5987414400668283e-07, "-11": 4.2012859280748917e-08, "-12": 4.503007542631089e-09, "-13": 4.439590858384922e-10, "-14": 3.7097976240171666e-11, "-2": 0.11382276724467674, "-3": 0.044006499985076386, "-4": 0.013311561403675806, "-5": 0.003294613667454467, "-6": 0.0006886413359072325, "-7": 0.000124435077419021, "-8": 1.9788483903890744e-05, "-9": 2.8087183441921417e-06, "0": 0.28482354323172676, "1": 0.19022078902446546, "10": 1.501607532957163e-07, "11": 1.606307222893935e-08, "12": 1.577573587608603e-09, "13": 1.425182496571194e-10, "14": 1.0912351068697243e-11, "2": 0.09556751614636873, "3": 0.033856227691436605, "4": 0.009384071695547912, "5": 0.0021281752709038267, "6": 0.00040760224172012045, "7": 6.748804967541901e-05, "8": 9.834157436926173e-06, "9": 1.2790084236740545e-06} |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 51.3% |
| P home draw | 61.1% |
| P draw away | 67.6% |
| P home away | 71.3% |
| Raw p home draw | 61.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.8, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.94, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.25, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.68, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:41Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.72, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.02 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | 0.0147 |
| Raw ev home | -0.0150 |
| Raw edge prob draw | -0.0042 |
| Raw ev draw | -0.0487 |
| Raw edge prob away | -0.0104 |
| Raw ev away | -0.0335 |
| Market p home draw | 61.5% |
| Market home draw odds | 1.57 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:23:26Z |
| Market reference home draw last update utc | 2026-10-23T16:23:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.5% |
| Market draw away odds | 1.43 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:23:26Z |
| Market reference draw away last update utc | 2026-10-23T16:23:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.0% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:23:26Z |
| Market reference home away last update utc | 2026-10-23T16:23:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.57 |
| Market reference dc draw away odds | 1.43 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 73.7% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:23:13Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.15 |
| Market reference over 1 5 last update utc | 2026-10-23T16:23:14Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 74.9% |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.25 |
| Market reference under 3 5 last update utc | 2026-10-23T16:23:14Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.1% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:23:26Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.09 |
| Market reference btts yes last update utc | 2026-10-23T16:23:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,396.7330 |
| Elo away rating | 1,477.6040 |
| Elo rating diff | -20.8710 |
| Elo home expectancy | 0.4700 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **44.4%**. Expected goals are 1.73 for Auxerre and 1.52 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.3%; Double Chance 1X: 69.4%; Double Chance X2: 55.6%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 77.4%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 44.4% | 2.25 |
| Draw | 25.0% | 4.00 |
| Le Mans FC win | 30.6% | 3.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.73 |
| Le Mans FC expected goals | 1.52 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.7% |
| Under 3.5 | 59.3% |
| Over 4.5 | 22.6% |
| Under 4.5 | 77.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.13% |
| 2 | 2-1 | 9.25% |
| 3 | 1-2 | 7.10% |
| 4 | 2-2 | 6.90% |
| 5 | 1-0 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 44.4% | 46.4% | 2.11 | -6.3% |
| Draw | 25.0% | 25.8% | 3.70 | -7.4% |
| Le Mans FC win | 30.6% | 27.8% | 3.45 | +5.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 8eab078a37a63df32ffa443302a2a7ba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7277 |
| Dc lambda away | 1.5164 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.65 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.26 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.45 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.42 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.15862877505121492, "-10": 8.015746509636355e-07, "-11": 1.0838160401847602e-07, "-12": 1.3472346502839317e-08, "-13": 1.549378476362334e-09, "-14": 1.6566793732766927e-10, "-15": 1.6392286277530197e-11, "-16": 1.3349530359023233e-12, "-2": 0.09103758373151553, "-3": 0.03851450774974936, "-4": 0.0130242769898504, "-5": 0.0036491688697035474, "-6": 0.000870301428494766, "-7": 0.0001803768018268914, "-8": 3.3021183417849425e-05, "-9": 5.409671741894667e-06, "0": 0.2502152264484331, "1": 0.2075695485969257, "10": 3.380182472836086e-06, "11": 5.20736315080627e-07, "12": 7.375163557365076e-08, "13": 9.6638916233616e-09, "14": 1.17733245945622e-09, "15": 1.3272914698884024e-10, "16": 1.2315693754867919e-11, "2": 0.13517237033642, "3": 0.06515648976556744, "4": 0.025104586468293753, "5": 0.008014188069851038, "6": 0.002177716719067773, "7": 0.0005142549631964359, "8": 0.00010726463603170354, "9": 2.0021700630225146e-05} |
| Raw goal margin distribution | {"-1": 0.17308020966349447, "-10": 8.745998864640785e-07, "-11": 1.1825540946859874e-07, "-12": 1.469970726696862e-08, "-13": 1.6905303054273597e-09, "-14": 1.8076065529683384e-10, "-15": 1.7885660056713775e-11, "-16": 1.4565702298986699e-12, "-2": 0.09933131031505092, "-3": 0.042023265162708864, "-4": 0.014210817623668392, "-5": 0.0039816162790254715, "-6": 0.0009495878264563271, "-7": 0.0001968095301029045, "-8": 3.602948675265782e-05, "-9": 5.90250488283424e-06, "0": 0.24277712531696563, "1": 0.1980131883703954, "10": 3.2245611807912086e-06, "11": 4.967619708495765e-07, "12": 7.035616065162246e-08, "13": 9.218972654431686e-09, "14": 1.1231288772593027e-09, "15": 1.2661838772882693e-10, "16": 1.174868762725094e-11, "2": 0.12894912674245132, "3": 0.06215672948519451, "4": 0.023948788456250262, "5": 0.007645220325611351, "6": 0.002077456128921375, "7": 0.0004905790159787187, "8": 0.00010232624546133542, "9": 1.909991521004423e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.8% |
| P home draw | 69.4% |
| P draw away | 55.6% |
| P home away | 75.0% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.7% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.33, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.8, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.57, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.12, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 6.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:51Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.37, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.54, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.55, "price": 2.54, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.09 |
| Reference draw odds | 3.68 |
| Reference away odds | 3.42 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | -2.0% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | +5.7% |
| Under 2.5 probability edge | -5.7% |
| Raw edge prob home | -0.0409 |
| Raw ev home | -0.1066 |
| Raw edge prob draw | -0.0149 |
| Raw ev draw | -0.1017 |
| Raw edge prob away | 0.0557 |
| Raw ev away | 0.1517 |
| Market p home draw | 72.1% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:23:26Z |
| Market reference home draw last update utc | 2026-10-23T16:23:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.2% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:23:26Z |
| Market reference draw away last update utc | 2026-10-23T16:23:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.7% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:23:26Z |
| Market reference home away last update utc | 2026-10-23T16:23:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 80.5% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.95 |
| Market reference over 1 5 last update utc | 2026-10-23T16:23:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.1% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:23:13Z |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-23T16:23:14Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.0% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:23:26Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.37 |
| Market reference btts yes last update utc | 2026-10-23T16:23:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,465.3899 |
| Elo away rating | 1,405.6473 |
| Elo rating diff | 119.7426 |
| Elo home expectancy | 0.6658 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **64.8%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.6%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.8%; Under 3.5 goals: 66.8%; Double Chance 1X: 84.9%; Double Chance X2: 35.2%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 64.8% | 1.54 |
| Draw | 20.1% | 4.98 |
| Le Havre win | 15.1% | 6.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.63% |
| 2 | 1-0 | 10.51% |
| 3 | 1-1 | 9.58% |
| 4 | 2-1 | 9.42% |
| 5 | 3-0 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 64.8% | 62.8% | 1.60 | +3.8% |
| Draw | 20.1% | 19.8% | 4.74 | -4.8% |
| Le Havre win | 15.1% | 17.4% | 5.01 | -24.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | fcc34b753fc61a0cc0e11d7cb0a0c36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1127 |
| Dc lambda away | 0.8100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.20 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.79 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.10441109257389147, "-10": 2.4983310893427406e-09, "-11": 1.8163703888339678e-10, "-12": 1.21285810818727e-11, "-13": 7.487141816550207e-13, "-14": 4.297021814728367e-14, "-15": 2.303694791947093e-15, "-16": 1.1539955790867044e-16, "-17": 4.995545339578526e-18, "-2": 0.03578773695685418, "-3": 0.008536592836941496, "-4": 0.001598952154288542, "-5": 0.00024555435309130645, "-6": 3.188798977619125e-05, "-7": 3.5828757021244408e-06, "-8": 3.544926513844041e-07, "-9": 3.131760942968398e-08, "0": 0.20092793374725773, "1": 0.23032861921543643, "10": 2.969745473798947e-05, "11": 5.6314719575694865e-06, "12": 9.807894471041594e-07, "13": 1.5791745041914773e-07, "14": 2.3639043439560867e-08, "15": 3.3054877849007134e-09, "16": 4.31879944673671e-10, "17": 4.876296142204101e-11, "2": 0.1986173880021417, "3": 0.12357080424898112, "4": 0.06036914845372209, "5": 0.024181068918526297, "6": 0.008190365357589973, "7": 0.0024002481899305815, "8": 0.0006194124376774803, "9": 0.00014272812627243026} |
| Raw goal margin distribution | {"-1": 0.08789936185194408, "-10": 2.103241169444593e-09, "-11": 1.529126782695851e-10, "-12": 1.0210548620700425e-11, "-13": 6.303113697464875e-13, "-14": 3.6174841778540426e-14, "-15": 1.9393849553915214e-15, "-16": 9.715009438283616e-17, "-17": 4.2055421184358554e-18, "-2": 0.030128209207335898, "-3": 0.007186602919857446, "-4": 0.0013460914020633336, "-5": 0.00020672201012950602, "-6": 2.68451740420674e-05, "-7": 3.016274229567108e-06, "-8": 2.984326384271976e-07, "-9": 2.6364994520572612e-08, "0": 0.20403769222213158, "1": 0.23768430668106186, "10": 3.064586139418918e-05, "11": 5.81131651111396e-06, "12": 1.012111567069346e-06, "13": 1.6296064224918761e-07, "14": 2.439397096927924e-08, "15": 3.4110505896880334e-09, "16": 4.4567229886097135e-10, "17": 5.03202368719641e-11, "2": 0.20496035760947526, "3": 0.12751711460775295, "4": 0.06229707469278046, "5": 0.024953306368458918, "6": 0.008451929760680352, "7": 0.002476901606189499, "8": 0.000639193758467734, "9": 0.00014728623760479722} |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 84.9% |
| P draw away | 35.2% |
| P home away | 79.9% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.02, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.97, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.27, "price": 3.97, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.70 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:14Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:14Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | 0.0414 |
| Raw ev home | 0.0707 |
| Raw edge prob draw | 0.0062 |
| Raw ev draw | -0.0329 |
| Raw edge prob away | -0.0476 |
| Raw ev away | -0.3647 |
| Market p home draw | 80.8% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:23:26Z |
| Market reference home draw last update utc | 2026-10-23T16:23:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.7% |
| Market draw away odds | 2.44 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:23:26Z |
| Market reference draw away last update utc | 2026-10-23T16:23:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:23:26Z |
| Market reference home away last update utc | 2026-10-23T16:23:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.44 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 84.2% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-23T16:23:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.5% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:23:13Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.25 |
| Market reference under 3 5 last update utc | 2026-10-23T16:23:14Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.3% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:23:26Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.23 |
| Market reference btts yes last update utc | 2026-10-23T16:23:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,561.8610 |
| Elo away rating | 1,427.2190 |
| Elo rating diff | 194.6420 |
| Elo home expectancy | 0.7541 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **54.1%**. Expected goals are 1.90 for Rennes and 1.25 for Strasbourg (3.16 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 61.4%; Under 3.5 goals: 61.1%; Double Chance 1X: 76.7%; Double Chance X2: 45.9%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 54.1% | 1.85 |
| Draw | 22.7% | 4.41 |
| Strasbourg win | 23.3% | 4.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.90 |
| Strasbourg expected goals | 1.25 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.4% |
| Under 2.5 | 38.6% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.35% |
| 2 | 2-1 | 10.04% |
| 3 | 2-0 | 8.02% |
| 4 | 1-0 | 7.83% |
| 5 | 3-1 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 54.1% | 56.1% | 1.81 | -2.1% |
| Draw | 22.7% | 21.8% | 4.39 | -0.5% |
| Strasbourg win | 23.3% | 22.1% | 3.92 | -8.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 31dcb6d13ed240fc4a5c7a696149967e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9036 |
| Dc lambda away | 1.2515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.42 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.69 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.1351428582556461, "-10": 1.3063919618046437e-07, "-11": 1.4604021396912197e-08, "-12": 1.5005063236642279e-09, "-13": 1.4260868531162773e-10, "-14": 1.2601115033251135e-11, "-15": 1.031853658260313e-12, "-16": 7.025242018402167e-14, "-2": 0.06583243581999881, "-3": 0.023299593284547594, "-4": 0.0065630673371647325, "-5": 0.0015277368380402397, "-6": 0.0003022074693568862, "-7": 5.189350471754149e-05, "-8": 7.864708042508526e-06, "-9": 1.0660375768086528e-06, "0": 0.2265388785791344, "1": 0.22755178261585984, "10": 9.451196056221654e-06, "11": 1.6069854585136814e-06, "12": 2.511328526521581e-07, "13": 3.630261330644543e-08, "14": 4.878958264823997e-09, "15": 6.076625177334662e-10, "16": 6.29262489691221e-11, "2": 0.16628132971328738, "3": 0.08951135223889192, "4": 0.038349777769146595, "5": 0.013577842162175481, "6": 0.004085202723086823, "7": 0.0010669587629394046, "8": 0.00024594808807329297, "9": 5.070602575017634e-05} |
| Raw goal margin distribution | {"-1": 0.14203350466712517, "-10": 1.3730021045808573e-07, "-11": 1.5348649333087965e-08, "-12": 1.577013944177919e-09, "-13": 1.4987999833824306e-10, "-14": 1.3243619041270948e-11, "-15": 1.0844656778611778e-12, "-16": 7.383444141168444e-14, "-2": 0.06918909146201493, "-3": 0.024487589904771373, "-4": 0.006897704157629051, "-5": 0.0016056328844655154, "-6": 0.00031761638434599313, "-7": 5.453944396047635e-05, "-8": 8.26571274930499e-06, "-9": 1.1203925615851527e-06, "0": 0.23489506605764549, "1": 0.21904170342306356, "10": 9.097736171264969e-06, "11": 1.5468867268913072e-06, "12": 2.417408784851592e-07, "13": 3.494495259910286e-08, "14": 4.6964928904169235e-09, "15": 5.849368941898546e-10, "16": 6.057290611292986e-11, "2": 0.16006266920500042, "3": 0.0861637682848115, "4": 0.036915556326933066, "5": 0.013070052195693594, "6": 0.0039324225589745295, "7": 0.0010270561813657394, "8": 0.00023675001595643367, "9": 4.880970004476791e-05} |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 61.3% |
| Raw p btts yes | 61.3% |
| P home draw | 76.7% |
| P draw away | 45.9% |
| P home away | 77.3% |
| Raw p home draw | 75.5% |
| Raw p draw away | 47.9% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.06, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.4, "price": 3.06, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.74 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.82 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:14Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:14Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | -0.0404 |
| Raw ev home | -0.0579 |
| Raw edge prob draw | 0.0167 |
| Raw ev draw | 0.0312 |
| Raw edge prob away | 0.0237 |
| Raw ev away | -0.0412 |
| Market p home draw | 75.5% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:23:26Z |
| Market reference home draw last update utc | 2026-10-23T16:23:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.5% |
| Market draw away odds | 2.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:23:26Z |
| Market reference draw away last update utc | 2026-10-23T16:23:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.0% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:23:26Z |
| Market reference home away last update utc | 2026-10-23T16:23:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.28 |
| Market reference dc draw away odds | 2.08 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 86.9% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-10-23T16:23:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.9% |
| Market under 3 5 odds | 1.79 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:23:13Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.01 |
| Market reference under 3 5 last update utc | 2026-10-23T16:23:14Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.5% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:23:26Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.81 |
| Market reference btts yes last update utc | 2026-10-23T16:23:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,575.6733 |
| Elo away rating | 1,512.5539 |
| Elo rating diff | 123.1194 |
| Elo home expectancy | 0.6701 |

</details>


---

## 2026-10-25 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **60.5%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.8%; Double Chance 1X: 82.9%; Double Chance X2: 39.5%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 60.5% | 1.65 |
| Draw | 22.5% | 4.45 |
| Troyes win | 17.1% | 5.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.7% |
| Under 2.5 | 46.3% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.92% |
| 2 | 1-0 | 10.85% |
| 3 | 1-1 | 10.72% |
| 4 | 2-1 | 9.94% |
| 5 | 3-0 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 60.5% | 60.7% | 1.63 | -1.5% |
| Draw | 22.5% | 22.0% | 4.35 | -2.2% |
| Troyes win | 17.1% | 17.3% | 5.00 | -14.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 18e4425261f7dd6b245f82056d424411 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9077 |
| Dc lambda away | 0.9104 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.58 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.51 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.42 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.11297025577681472, "-10": 7.63064325078668e-09, "-11": 6.234427749572693e-10, "-12": 4.678377711149382e-11, "-13": 3.2456497648562053e-12, "-14": 2.0930678765569078e-13, "-15": 1.2550777524774954e-14, "-16": 6.44227913303119e-16, "-2": 0.04313359033377655, "-3": 0.011545907609856926, "-4": 0.0024281746776194475, "-5": 0.000418822468400297, "-6": 6.10987335084117e-05, "-7": 7.71285926211059e-06, "-8": 8.574485879613673e-07, "-9": 8.512053532034374e-08, "0": 0.2249127091783772, "1": 0.24126596345918547, "10": 1.2346618542595095e-05, "11": 2.1136812761744647e-06, "12": 3.3234887201082256e-07, "13": 4.831217661069672e-08, "14": 6.528212552449556e-09, "15": 8.202337372614374e-10, "16": 8.8219086924288e-11, "2": 0.18782539194458234, "3": 0.10534715116468062, "4": 0.046422728952397276, "5": 0.016777866575849804, "6": 0.005128554743314781, "7": 0.001356545039673396, "8": 0.00031599697388011395, "9": 6.573023782656847e-05} |
| Raw goal margin distribution | {"-1": 0.11151307165468248, "-10": 7.532216880852022e-09, "-11": 6.154010926004498e-10, "-12": 4.6180321124681464e-11, "-13": 3.2037846803626872e-12, "-14": 2.0660697498793036e-13, "-15": 1.2388887179358301e-14, "-16": 6.359181269806528e-16, "-2": 0.042577217485607464, "-3": 0.011396978910625442, "-4": 0.002396854065289589, "-5": 0.0004134201485883382, "-6": 6.031063133285553e-05, "-7": 7.613372401824178e-06, "-8": 8.463885044081314e-07, "-9": 8.40225800073873e-08, "0": 0.22998036738746766, "1": 0.24012151618831948, "10": 1.2288052246326424e-05, "11": 2.1036550100019977e-06, "12": 3.3077237214281475e-07, "13": 4.808300736577311e-08, "14": 6.4972459174042945e-09, "15": 8.163429511405022e-10, "16": 8.780061889083135e-11, "2": 0.18693444050606056, "3": 0.10484743600421903, "4": 0.04620252231945997, "5": 0.016698280614621034, "6": 0.005104227397694533, "7": 0.0013501102560586585, "8": 0.0003144980393881784, "9": 6.541844585137461e-05} |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.9% |
| P draw away | 39.5% |
| P home away | 77.5% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 9.5, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 3.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.43, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.88, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.27, "price": 3.88, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.61 |
| Reference draw odds | 4.25 |
| Reference away odds | 5.35 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0057 |
| Raw ev home | -0.0193 |
| Raw edge prob draw | 0.0101 |
| Raw ev draw | 0.0004 |
| Raw edge prob away | -0.0044 |
| Raw ev away | -0.1582 |
| Market p home draw | 82.0% |
| Market home draw odds | 1.18 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:23:26Z |
| Market reference home draw last update utc | 2026-10-23T16:23:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.6% |
| Market draw away odds | 2.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:23:26Z |
| Market reference draw away last update utc | 2026-10-23T16:23:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.4% |
| Market home away odds | 1.25 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:23:26Z |
| Market reference home away last update utc | 2026-10-23T16:23:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.38 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.6% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-23T16:23:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.2% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:23:13Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.39 |
| Market reference under 3 5 last update utc | 2026-10-23T16:23:14Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.4% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:23:26Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.22 |
| Market reference btts yes last update utc | 2026-10-23T16:23:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,462.4520 |
| Elo away rating | 1,403.0456 |
| Elo rating diff | 119.4065 |
| Elo home expectancy | 0.6654 |

</details>


---

## 2026-10-26 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **67.4%**. Expected goals are 2.42 for Paris Saint Germain and 1.10 for Lyon (3.52 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 68.5%; Under 3.5 goals: 53.1%; Double Chance 1X: 85.7%; Double Chance X2: 32.6%; Double Chance 12 (either team wins): 81.7%; Under 4.5 goals: 72.0%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 67.4% | 1.48 |
| Draw | 18.3% | 5.46 |
| Lyon win | 14.3% | 7.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.42 |
| Lyon expected goals | 1.10 |
| Expected total goals | 3.52 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 87.2% |
| Under 1.5 | 12.8% |
| Over 2.5 | 68.5% |
| Under 2.5 | 31.5% |
| Over 3.5 | 46.9% |
| Under 3.5 | 53.1% |
| Over 4.5 | 28.0% |
| Under 4.5 | 72.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.71% |
| 2 | 2-0 | 8.86% |
| 3 | 1-1 | 8.11% |
| 4 | 3-1 | 7.84% |
| 5 | 3-0 | 7.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 67.4% | 68.6% | 1.44 | -2.9% |
| Draw | 18.3% | 17.8% | 5.48 | +0.3% |
| Lyon win | 14.3% | 13.5% | 6.23 | -11.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T19:30:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4237 |
| Dc lambda away | 1.0958 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.09 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.79 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.18 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.88 |
| Fair Over 4.5 odds | 3.57 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.0901358927558811, "-10": 2.4552532492555033e-08, "-11": 2.398391141434379e-09, "-12": 2.1539562448790525e-10, "-13": 1.789803397407098e-11, "-14": 1.3835794255219773e-12, "-15": 9.997630563562573e-14, "-16": 6.778308011974731e-15, "-17": 4.2935708991351616e-16, "-18": 2.2777253025715885e-17, "-2": 0.03775241537356552, "-3": 0.011518556176388188, "-4": 0.002810955672921847, "-5": 0.000568576489463935, "-6": 9.79190008171016e-05, "-7": 1.4657265902686324e-05, "-8": 1.9381659617532584e-06, "-9": 2.2936775951180144e-07, "0": 0.1830186095168913, "1": 0.2195265088645449, "10": 7.386146128979926e-05, "11": 1.5958683711624485e-05, "12": 3.1700739094316332e-06, "13": 5.826306050332594e-07, "14": 9.962022447131439e-08, "15": 1.5921939162521064e-08, "16": 2.387677298285766e-09, "17": 3.3452488049233694e-10, "18": 3.925243351452595e-11, "2": 0.19825434058477384, "3": 0.13379240529071332, "4": 0.07221756961642772, "5": 0.03230972222465595, "6": 0.012307412439185343, "7": 0.00407481787861791, "8": 0.0011917952590527407, "9": 0.00031195971763297957} |
| Raw goal margin distribution | {"-1": 0.09497930359065282, "-10": 2.587185155912928e-08, "-11": 2.5272675888214917e-09, "-12": 2.2696980952685106e-10, "-13": 1.8859776616437737e-11, "-14": 1.4579254310415499e-12, "-15": 1.0534848654082282e-13, "-16": 7.1425372825e-15, "-17": 4.524283961123167e-16, "-18": 2.4001178264797642e-17, "-2": 0.03978102408945578, "-3": 0.012137500506775433, "-4": 0.002962001086086675, "-5": 0.0005991286862111781, "-6": 0.00010318063339195204, "-7": 1.5444867359893493e-05, "-8": 2.0423124203029677e-06, "-9": 2.416927308145823e-07, "0": 0.18769783556705721, "1": 0.21550191570643035, "10": 7.250735452022142e-05, "11": 1.5666112169305882e-05, "12": 3.111956747032407e-06, "13": 5.719492018676314e-07, "14": 9.779388069219257e-08, "15": 1.5630041260309455e-08, "16": 2.3439038616827372e-09, "17": 3.283920150256006e-10, "18": 3.853281620644319e-11, "2": 0.1946197314124651, "3": 0.1313395807925433, "4": 0.07089360041527182, "5": 0.03171738607501051, "6": 0.01208177988048874, "7": 0.004000113988688301, "8": 0.0011699460023490017, "9": 0.00030624054070219845} |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.2% |
| Raw p btts yes | 61.1% |
| P home draw | 85.7% |
| P draw away | 32.6% |
| P home away | 81.7% |
| Raw p home draw | 84.9% |
| Raw p draw away | 33.8% |
| Raw p home away | 81.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.43 |
| Reference draw odds | 5.15 |
| Reference away odds | 6.70 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:14Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:14Z |
| Home probability edge | -1.2% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | -0.0247 |
| Raw ev home | -0.0471 |
| Raw edge prob draw | 0.0094 |
| Raw ev draw | 0.0286 |
| Raw edge prob away | 0.0154 |
| Raw ev away | -0.0619 |
| Elo home rating | 1,650.2164 |
| Elo away rating | 1,562.6863 |
| Elo rating diff | 147.5301 |
| Elo home expectancy | 0.7004 |

</details>


---

## 2026-10-30 — Le Havre vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **74.6%**. Expected goals are 0.82 for Le Havre and 2.31 for Paris Saint Germain (3.13 combined). The most likely exact score is 0-2 at 12.4%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 61.8%; Under 3.5 goals: 61.1%; Double Chance 1X: 25.4%; Double Chance X2: 90.3%; Double Chance 12 (either team wins): 84.2%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 9.7% | 10.33 |
| Draw | 15.8% | 6.34 |
| Paris Saint Germain win | 74.6% | 1.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 0.82 |
| Paris Saint Germain expected goals | 2.31 |
| Expected total goals | 3.13 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.8% |
| Under 2.5 | 38.2% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.36% |
| 2 | 0-1 | 10.22% |
| 3 | 1-2 | 10.15% |
| 4 | 0-3 | 9.51% |
| 5 | 1-3 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 9.7% | 8.1% | 9.87 | -4.4% |
| Draw | 15.8% | 13.0% | 6.94 | +9.4% |
| Paris Saint Germain win | 74.6% | 78.8% | 1.22 | -9.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T18:00:00+00:00 |
| Fixture id | 9a9f6c78276f74f15f42b013b033aa5d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Le Havre |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8210 |
| Dc lambda away | 2.3072 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.17 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.62 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.24129092169914235, "-10": 6.491346259661671e-05, "-11": 1.3424856291816657e-05, "-12": 2.5504829874777962e-06, "-13": 4.480273469088634e-07, "-14": 7.317946918444143e-08, "-15": 1.1168307075318121e-08, "-16": 1.599112160208341e-09, "-17": 2.1468511910322564e-10, "-18": 2.4897638351872056e-11, "-2": 0.22271428480495392, "-3": 0.14960246543737676, "-4": 0.07921566607848772, "-5": 0.03446779691026391, "-6": 0.01269947070097125, "-7": 0.004052100581916122, "-8": 0.0011392541285120267, "-9": 0.0002861306860235948, "0": 0.15761417362965008, "1": 0.06720386023627598, "10": 1.7184252650535224e-09, "11": 1.2646293465451555e-10, "12": 8.549363407263394e-12, "13": 5.344088077320603e-13, "14": 3.106104590753478e-14, "15": 1.6868322818538541e-15, "16": 8.594511951703738e-17, "17": 4.10583954403509e-18, "18": 1.6943999186397786e-19, "2": 0.02293411853432791, "3": 0.005481891895842361, "4": 0.0010329053603124064, "5": 0.00015992660393718866, "6": 2.0967688059492728e-05, "7": 2.3806901778800043e-06, "8": 2.3817765280423675e-07, "9": 2.1286417349996654e-08} |
| Raw goal margin distribution | {"-1": 0.22749593571303292, "-10": 6.12022566360928e-05, "-11": 1.2657335893174978e-05, "-12": 2.4046678162218457e-06, "-13": 4.2241291049128504e-07, "-14": 6.899568247269344e-08, "-15": 1.052979718647663e-08, "-16": 1.5076883731675804e-09, "-17": 2.0241122919224125e-10, "-18": 2.3474200744967195e-11, "-2": 0.2099813547131143, "-3": 0.1410494544095965, "-4": 0.07468678038424843, "-5": 0.032497218108538325, "-6": 0.011973421750943434, "-7": 0.003820435543098222, "-8": 0.0010741211569656023, "-9": 0.00026977213935264725, "0": 0.18480766605167193, "1": 0.07791272138568446, "10": 1.992254439365748e-09, "11": 1.466146640789944e-10, "12": 9.911695054914756e-12, "13": 6.195662629571455e-13, "14": 3.601058938033135e-14, "15": 1.955627149071348e-15, "16": 9.964037970211321e-17, "17": 4.7601005555935975e-18, "18": 1.9644006804485163e-19, "2": 0.026588645076474696, "3": 0.006355425334877687, "4": 0.0011974976924370212, "5": 0.0001854107322244405, "6": 2.4308866070157266e-05, "7": 2.760050537017766e-06, "8": 2.7613099958826263e-07, "9": 2.4678384522239938e-08} |
| Unadjusted home-win probability | 11.2% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 70.3% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 61.9% |
| Raw p btts yes | 50.9% |
| P home draw | 25.4% |
| P draw away | 90.3% |
| P home away | 84.2% |
| Raw p home draw | 29.7% |
| Raw p draw away | 88.8% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.26, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.75, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 2.0, "market_key": "spreads", "opposite_price": 2.03, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 10.50 |
| Reference draw odds | 6.75 |
| Reference away odds | 1.25 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.35 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:14Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:14Z |
| Home probability edge | +1.5% |
| Draw probability edge | +2.7% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -12.2% |
| Under 2.5 probability edge | +12.2% |
| Raw edge prob home | 0.0309 |
| Raw ev home | 0.1081 |
| Raw edge prob draw | 0.0544 |
| Raw ev draw | 0.2826 |
| Raw edge prob away | -0.0852 |
| Raw ev away | -0.1424 |
| Elo home rating | 1,381.9724 |
| Elo away rating | 1,700.4644 |
| Elo rating diff | -258.4920 |
| Elo home expectancy | 0.1842 |

</details>


---

## 2026-10-30 — Lille vs RC Lens

The model's most likely 1X2 outcome is **Lille win** at **39.4%**. Expected goals are 1.25 for Lille and 1.12 for RC Lens (2.37 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 42.7%; Under 3.5 goals: 78.4%; Double Chance 1X: 67.4%; Double Chance X2: 60.6%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 39.4% | 2.54 |
| Draw | 28.0% | 3.57 |
| RC Lens win | 32.6% | 3.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.25 |
| RC Lens expected goals | 1.12 |
| Expected total goals | 2.37 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 69.3% |
| Under 1.5 | 30.7% |
| Over 2.5 | 42.7% |
| Under 2.5 | 57.3% |
| Over 3.5 | 21.6% |
| Under 3.5 | 78.4% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.22% |
| 2 | 1-0 | 11.22% |
| 3 | 0-1 | 9.82% |
| 4 | 0-0 | 9.64% |
| 5 | 2-1 | 8.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 39.4% | 40.6% | 2.31 | -8.9% |
| Draw | 28.0% | 26.7% | 3.51 | -1.8% |
| RC Lens win | 32.6% | 32.8% | 3.01 | -1.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:05:00+00:00 |
| Fixture id | 7932d9a82dcdb164a3e4ef5e03694ee3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lille |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2460 |
| Dc lambda away | 1.1238 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.37 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.26 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.64 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.71 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.1916962347004805, "-10": 9.455311741988573e-08, "-11": 9.559487880813722e-09, "-12": 8.872229586849337e-10, "-13": 7.579689026117398e-11, "-14": 5.531174741363006e-12, "-2": 0.09247251566232209, "-3": 0.03122567774325527, "-4": 0.00822220495838647, "-5": 0.0017681219761926778, "-6": 0.00032073694261329635, "-7": 5.0259690009451656e-05, "-8": 6.927647086332383e-06, "-9": 8.519553407522444e-07, "0": 0.2798105608342694, "1": 0.2181810016137258, "10": 2.7149722333448966e-07, "11": 3.0434269708339583e-08, "12": 3.131841303965541e-09, "13": 2.966586949623278e-10, "14": 2.400279359833662e-11, "2": 0.11624986836273807, "3": 0.04352415903246509, "4": 0.012707073191229611, "5": 0.003029759618828681, "6": 0.000609373625923042, "7": 0.0001058749436579746, "8": 1.618072064000622e-05, "9": 2.206315683188263e-06} |
| Raw goal margin distribution | {"-1": 0.19050783839443292, "-10": 9.396694745341432e-08, "-11": 9.50022505750884e-09, "-12": 8.817227333498391e-10, "-13": 7.532699712771197e-11, "-14": 5.496884930501514e-12, "-2": 0.09189924412052192, "-3": 0.031032098145085805, "-4": 0.008171232449639075, "-5": 0.0017571607299875442, "-6": 0.00031874857493142613, "-7": 4.994811148500304e-05, "-8": 6.8847000236534394e-06, "-9": 8.466737525069174e-07, "0": 0.2929352370586979, "1": 0.21203806699051073, "10": 2.638531586313635e-07, "11": 2.957738607621373e-08, "12": 3.0436636155405616e-09, "13": 2.883062034296863e-10, "14": 2.3326989606428317e-11, "2": 0.11297682746537362, "3": 0.04229872665526754, "4": 0.012349302719516725, "5": 0.0029444560629513818, "6": 0.0005922165759623671, "7": 0.00010289401107302399, "8": 1.5725148851844563e-05, "9": 2.1441963744503064e-06} |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 69.2% |
| Raw p under 3 5 | 78.5% |
| Raw p btts yes | 48.8% |
| P home draw | 67.4% |
| P draw away | 60.6% |
| P home away | 72.0% |
| Raw p home draw | 67.6% |
| Raw p draw away | 61.7% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.38 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.92 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | -1.1% |
| Draw probability edge | +1.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -13.9% |
| Under 2.5 probability edge | +13.9% |
| Raw edge prob home | -0.0222 |
| Raw ev home | -0.1145 |
| Raw edge prob draw | 0.0262 |
| Raw ev draw | 0.0282 |
| Raw edge prob away | -0.0040 |
| Raw ev away | -0.0255 |
| Elo home rating | 1,568.8970 |
| Elo away rating | 1,577.5173 |
| Elo rating diff | 51.3797 |
| Elo home expectancy | 0.5734 |

</details>


---

## 2026-10-31 — Lorient vs Brest

The model's most likely 1X2 outcome is **Brest win** at **36.8%**. Expected goals are 1.38 for Lorient and 1.40 for Brest (2.78 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 52.4%; Under 3.5 goals: 69.7%; Double Chance 1X: 63.2%; Double Chance X2: 63.8%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 36.2% | 2.76 |
| Draw | 27.0% | 3.71 |
| Brest win | 36.8% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.38 |
| Brest expected goals | 1.40 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 52.4% |
| Under 2.5 | 47.6% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 1-2 | 8.34% |
| 3 | 2-1 | 8.27% |
| 4 | 0-1 | 7.98% |
| 5 | 1-0 | 7.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 36.2% | 36.1% | 2.60 | -5.8% |
| Draw | 27.0% | 27.2% | 3.51 | -5.4% |
| Brest win | 36.8% | 36.7% | 2.63 | -3.2% |
| Over 2.5 | 52.4% | 50.0% | 1.91 | +0.1% |
| Under 2.5 | 47.6% | 50.0% | 1.93 | -8.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | c1a1e850def721bbfc43ff80c133a5e6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lorient |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3813 |
| Dc lambda away | 1.3951 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.37 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.74 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.1947856658406231, "-10": 5.683776683643579e-07, "-11": 7.105771641513208e-08, "-12": 8.157990402649403e-09, "-13": 8.597402819711261e-10, "-14": 7.530533510879747e-11, "-2": 0.10985999087884957, "-3": 0.04453114355017887, "-4": 0.014238491011504645, "-5": 0.003742526950141918, "-6": 0.0008331863829098195, "-7": 0.00016066172941780248, "-8": 2.7300927874612766e-05, "-9": 4.14458446280881e-06, "0": 0.2696360729786714, "1": 0.19292639066743303, "10": 5.150756389079922e-07, "11": 6.375870535682732e-08, "12": 7.247791199478882e-09, "13": 7.562824082836678e-10, "14": 6.558986064603572e-11, "2": 0.10777540030945043, "3": 0.043255184977812, "4": 0.013694069601045506, "5": 0.0035639183160829776, "6": 0.0007855959003217056, "7": 0.00014999048940071173, "8": 2.5236140229556398e-05, "9": 3.7933311613108954e-06} |
| Raw goal margin distribution | {"-1": 0.19536969203180912, "-10": 5.700818360882891e-07, "-11": 7.127076888638661e-08, "-12": 8.182450519065208e-09, "-13": 8.623180427119991e-10, "-14": 7.553112322236206e-11, "-2": 0.11018938427522607, "-3": 0.04466466135316776, "-4": 0.014281182303175408, "-5": 0.0037537481750234804, "-6": 0.0008356845270502464, "-7": 0.00016114344175272352, "-8": 2.7382784292812962e-05, "-9": 4.157011177410301e-06, "0": 0.26769005432378956, "1": 0.19337495719088726, "10": 5.162732235819271e-07, "11": 6.390694853238726e-08, "12": 7.2646427898176915e-09, "13": 7.580408145310443e-10, "14": 6.5742361377854e-11, "2": 0.10802598519036513, "3": 0.043355756122484046, "4": 0.013725909211850596, "5": 0.003572204660130517, "6": 0.0007874224623624304, "7": 0.0001503392271350824, "8": 2.529481591228189e-05, "9": 3.80215090528399e-06} |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 36.9% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 57.0% |
| P home draw | 63.2% |
| P draw away | 63.8% |
| P home away | 73.0% |
| Raw p home draw | 63.1% |
| Raw p draw away | 63.7% |
| Raw p home away | 73.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.66 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.62 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market best over 2 5 last update utc | 2026-10-23T16:23:13Z |
| Market best under 2 5 last update utc | 2026-10-23T16:23:13Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +2.4% |
| Under 2.5 probability edge | -2.4% |
| Raw edge prob home | 0.0017 |
| Raw ev home | -0.0561 |
| Raw edge prob draw | -0.0039 |
| Raw ev draw | -0.0604 |
| Raw edge prob away | 0.0022 |
| Raw ev away | -0.0288 |
| Elo home rating | 1,499.1891 |
| Elo away rating | 1,456.9508 |
| Elo rating diff | 102.2383 |
| Elo home expectancy | 0.6430 |

</details>


---

## 2026-10-31 — Lyon vs Angers

The model's most likely 1X2 outcome is **Lyon win** at **68.5%**. Expected goals are 2.14 for Lyon and 0.83 for Angers (2.98 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 57.7%; Under 3.5 goals: 65.0%; Double Chance 1X: 87.6%; Double Chance X2: 31.5%; Double Chance 12 (either team wins): 80.9%; Under 4.5 goals: 81.6%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 68.5% | 1.46 |
| Draw | 19.1% | 5.25 |
| Angers win | 12.4% | 8.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 2.14 |
| Angers expected goals | 0.83 |
| Expected total goals | 2.98 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.0% |
| Under 3.5 | 65.0% |
| Over 4.5 | 18.4% |
| Under 4.5 | 81.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.98% |
| 2 | 1-0 | 10.64% |
| 3 | 2-1 | 9.99% |
| 4 | 1-1 | 9.08% |
| 5 | 3-0 | 8.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 68.5% | 70.1% | 1.40 | -4.0% |
| Draw | 19.1% | 17.9% | 5.03 | -4.1% |
| Angers win | 12.4% | 11.9% | 7.06 | -12.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | 961df571fad52d969150e9ced52b16f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lyon |
| Matched away-team name | Angers |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1444 |
| Dc lambda away | 0.8338 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.89 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.12 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.45 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.08520958589281075, "-10": 2.5813140920909425e-09, "-11": 1.9307207202789653e-10, "-12": 1.3264340594481868e-11, "-13": 8.425219568267737e-13, "-14": 4.97559659668111e-14, "-15": 2.744892976014196e-15, "-16": 1.4144567941939226e-16, "-17": 6.27710889031837e-18, "-2": 0.029797459902966828, "-3": 0.00728118488163323, "-4": 0.0013993897806829356, "-5": 0.0002207223261421113, "-6": 2.9456103261527933e-05, "-7": 3.402489950570571e-06, "-8": 3.461824193557093e-07, "-9": 3.1455901017528585e-08, "0": 0.1906403446193873, "1": 0.2408676334592143, "10": 3.468528397230042e-05, "11": 6.672351671393191e-06, "12": 1.1789630772887415e-06, "13": 1.9259758424388783e-07, "14": 2.9252961413598924e-08, "15": 4.150545322892318e-09, "16": 5.500782829123622e-10, "17": 6.278408137871415e-11, "2": 0.20914288666037614, "3": 0.13143801181164722, "4": 0.0649699734173818, "5": 0.02635574663786303, "6": 0.009046059118930328, "7": 0.0026874231115635644, "8": 0.0007032330510517139, "9": 0.00016434309559630952} |
| Raw goal margin distribution | {"-1": 0.08832721999550189, "-10": 2.6757587811354756e-09, "-11": 2.001361607653844e-10, "-12": 1.3749654073637694e-11, "-13": 8.733480095219887e-13, "-14": 5.157642894272092e-14, "-15": 2.845322661953806e-15, "-16": 1.4662087032327645e-16, "-17": 6.506774702418196e-18, "-2": 0.030887684391135577, "-3": 0.007547587658470267, "-4": 0.001450590420346914, "-5": 0.0002287980777608505, "-6": 3.0533838249890074e-05, "-7": 3.526979684827779e-06, "-8": 3.5884848391906893e-07, "-9": 3.2606804272316e-08, "0": 0.20193523222705081, "1": 0.23530482670506203, "10": 3.3884231837649585e-05, "11": 6.518254574947935e-06, "12": 1.1517350779305443e-06, "13": 1.8814956801572688e-07, "14": 2.8577368063867783e-08, "15": 4.054689016986818e-09, "16": 5.37374296313783e-10, "17": 6.133409116238275e-11, "2": 0.20431275881883598, "3": 0.12840246797639804, "4": 0.0634695003079281, "5": 0.025747064087608077, "6": 0.008837141556854613, "7": 0.002625357423361409, "8": 0.0006869919749471655, "9": 0.00016054761311885062} |
| Unadjusted home-win probability | 67.0% |
| Unadjusted draw probability | 20.2% |
| Unadjusted away-win probability | 12.8% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 50.5% |
| P home draw | 87.6% |
| P draw away | 31.5% |
| P home away | 80.9% |
| Raw p home draw | 87.2% |
| Raw p draw away | 33.0% |
| Raw p home away | 79.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.17, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.40 |
| Reference draw odds | 5.10 |
| Reference away odds | 7.50 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | -1.6% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | -0.0317 |
| Raw ev home | -0.0626 |
| Raw edge prob draw | 0.0226 |
| Raw ev draw | 0.0157 |
| Raw edge prob away | 0.0091 |
| Raw ev away | -0.0930 |
| Elo home rating | 1,586.0725 |
| Elo away rating | 1,418.3146 |
| Elo rating diff | 227.7578 |
| Elo home expectancy | 0.7877 |

</details>


---

## 2026-10-31 — Nice vs Rennes

The model's most likely 1X2 outcome is **Rennes win** at **37.2%**. Expected goals are 1.34 for Nice and 1.30 for Rennes (2.64 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.7%; Double Chance 1X: 62.8%; Double Chance X2: 63.6%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 54.2%; BTTS No (at least one team does not score): 45.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 36.4% | 2.75 |
| Draw | 26.5% | 3.78 |
| Rennes win | 37.2% | 2.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nice expected goals | 1.34 |
| Rennes expected goals | 1.30 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.61% |
| 2 | 0-1 | 9.03% |
| 3 | 1-0 | 8.65% |
| 4 | 1-2 | 8.53% |
| 5 | 2-1 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 36.4% | 35.4% | 2.78 | +1.1% |
| Draw | 26.5% | 25.4% | 3.79 | +0.3% |
| Rennes win | 37.2% | 39.2% | 2.35 | -12.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T16:15:00+00:00 |
| Fixture id | a547720e6b4661d6319c4f11dbdf8e1f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Nice |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3431 |
| Dc lambda away | 1.2984 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.2% |
| P btts no | 45.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.30 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.97 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.66 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.71 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.20432309068157453, "-10": 3.307583304890513e-07, "-11": 3.853612374358999e-08, "-12": 4.122630011242331e-09, "-13": 4.0527618981398937e-10, "-14": 3.342196847750416e-11, "-2": 0.10944717388919131, "-3": 0.04176108785965379, "-4": 0.01252115785801586, "-5": 0.0030793091607387063, "-6": 0.0006405275282029357, "-7": 0.00011529719851838916, "-8": 1.8277630576935816e-05, "-9": 2.587392347202808e-06, "0": 0.2645381577849149, "1": 0.19530565161942473, "10": 4.2847729652748153e-07, "11": 5.1643148424537845e-08, "12": 5.715400954461116e-09, "13": 5.812341075329836e-10, "14": 4.9586069683364057e-11, "2": 0.1080936797965216, "3": 0.04266730500838947, "4": 0.013234134960259252, "5": 0.0033669139855465, "6": 0.0007245096697963384, "7": 0.0001349126898330181, "8": 2.212491448005953e-05, "9": 3.240049565782156e-06} |
| Raw goal margin distribution | {"-1": 0.19327904475808286, "-10": 3.128802229324691e-07, "-11": 3.6453174044082815e-08, "-12": 3.89979413391762e-09, "-13": 3.833702523251189e-10, "-14": 3.161544845332203e-11, "-2": 0.10353134905218182, "-3": 0.039503822806553394, "-4": 0.011844365812937008, "-5": 0.0029128667304172792, "-6": 0.000605905815046892, "-7": 0.00010906516888806483, "-8": 1.7289690394595487e-05, "-9": 2.4475389424345163e-06, "0": 0.2755491106082428, "1": 0.2001896871035173, "10": 4.3919228763509253e-07, "11": 5.2934595790880305e-08, "12": 5.858326777835643e-09, "13": 5.957691093735225e-10, "14": 5.082607539667621e-11, "2": 0.11079679342049956, "3": 0.04373429221507638, "4": 0.013565082806423618, "5": 0.0034511108699732756, "6": 0.0007426275834691529, "7": 0.0001382864701559901, "8": 2.2678195281240287e-05, "9": 3.3210739340904266e-06} |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 54.4% |
| P home draw | 62.8% |
| P draw away | 63.6% |
| P home away | 73.5% |
| Raw p home draw | 64.8% |
| Raw p draw away | 62.7% |
| Raw p home away | 72.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.71 |
| Reference draw odds | 3.74 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | +0.9% |
| Draw probability edge | +1.1% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.0182 |
| Raw ev home | 0.0360 |
| Raw edge prob draw | 0.0220 |
| Raw ev draw | 0.0443 |
| Raw edge prob away | -0.0402 |
| Raw ev away | -0.1733 |
| Elo home rating | 1,473.7323 |
| Elo away rating | 1,526.8081 |
| Elo rating diff | 6.9242 |
| Elo home expectancy | 0.5100 |

</details>


---

## 2026-10-31 — Troyes vs Le Mans FC

The model's most likely 1X2 outcome is **Troyes win** at **38.7%**. Expected goals are 1.54 for Troyes and 1.80 for Le Mans FC (3.34 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.3%; Double Chance 1X: 64.0%; Double Chance X2: 61.3%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 66.6%; BTTS No (at least one team does not score): 33.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 38.7% | 2.58 |
| Draw | 25.3% | 3.96 |
| Le Mans FC win | 36.0% | 2.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 1.54 |
| Le Mans FC expected goals | 1.80 |
| Expected total goals | 3.34 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 64.4% |
| Under 2.5 | 35.6% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.01% |
| 2 | 2-1 | 8.97% |
| 3 | 1-2 | 7.30% |
| 4 | 2-2 | 7.24% |
| 5 | 1-0 | 5.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 38.7% | 44.9% | 2.16 | -16.3% |
| Draw | 25.3% | 26.7% | 3.51 | -11.4% |
| Le Mans FC win | 36.0% | 28.4% | 3.32 | +19.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | 75cf0c0e471877a0bfa95d689d0f0325 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Troyes |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5404 |
| Dc lambda away | 1.8043 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 66.6% |
| P btts no | 33.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.04 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.70 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.14 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.16379010598093796, "-10": 3.7669429792985393e-06, "-11": 6.053402563741381e-07, "-12": 8.944566142333675e-08, "-13": 1.2229284357980664e-08, "-14": 1.5545752098750785e-09, "-15": 1.8268279299572455e-10, "-16": 1.7551556960644608e-11, "-2": 0.10973969335406002, "-3": 0.05475499621936248, "-4": 0.021898742809547796, "-5": 0.007268777223689913, "-6": 0.0020559486788504396, "-7": 0.0005057292289173427, "-8": 0.00010993843028396692, "-9": 2.1394924819260366e-05, "0": 0.2525520443098195, "1": 0.20024164478033457, "10": 1.1154387439044694e-06, "11": 1.5303826635100988e-07, "12": 1.9306500593135944e-08, "13": 2.253663796620872e-09, "14": 2.445927751282254e-10, "15": 2.4539930664547028e-11, "16": 2.012959968679337e-12, "2": 0.11509859072683513, "3": 0.049031346389550215, "4": 0.016742220239469963, "5": 0.004744593703398388, "6": 0.0011457602229883374, "7": 0.00024062643010505703, "8": 4.4659988507724494e-05, "9": 7.4203372106156845e-06} |
| Raw goal margin distribution | {"-1": 0.19840071378854804, "-10": 4.562938471879179e-06, "-11": 7.332551513432014e-07, "-12": 1.0834648995064518e-07, "-13": 1.4813463433675681e-08, "-14": 1.8830736412924274e-09, "-15": 2.2128562839720895e-10, "-16": 2.1260389376007334e-11, "-2": 0.13292886870050488, "-3": 0.06632531475787105, "-4": 0.02652618226519592, "-5": 0.008804747887017399, "-6": 0.0024903927068953813, "-7": 0.0006125952443831383, "-8": 0.00013316960087729623, "-9": 2.591590212468382e-05, "0": 0.23769808323021727, "1": 0.16857427875999476, "10": 9.390368420161767e-07, "11": 1.2883591423303706e-07, "12": 1.625325948774333e-08, "13": 1.897256434842196e-09, "14": 2.0591146613072323e-10, "15": 2.0659044811254785e-11, "16": 1.694618895410643e-12, "2": 0.0968962372405241, "3": 0.04127724711469028, "4": 0.014094509185667703, "5": 0.003994256351804319, "6": 0.0009645631079091015, "7": 0.00020257238173433117, "8": 3.759720092380443e-05, "9": 6.2468423829004475e-06} |
| Unadjusted home-win probability | 32.6% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 43.6% |
| Raw p over 1 5 | 85.2% |
| Raw p under 3 5 | 57.0% |
| Raw p btts yes | 66.2% |
| P home draw | 64.0% |
| P draw away | 61.3% |
| P home away | 74.7% |
| Raw p home draw | 56.4% |
| Raw p draw away | 67.4% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.16 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.35 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | -6.1% |
| Draw probability edge | -1.5% |
| Away probability edge | +7.6% |
| Over 2.5 probability edge | +11.7% |
| Under 2.5 probability edge | -11.7% |
| Raw edge prob home | -0.1225 |
| Raw ev home | -0.2957 |
| Raw edge prob draw | -0.0297 |
| Raw ev draw | -0.1657 |
| Raw edge prob away | 0.1522 |
| Raw ev away | 0.4484 |
| Elo home rating | 1,388.6712 |
| Elo away rating | 1,405.6473 |
| Elo rating diff | 43.0239 |
| Elo home expectancy | 0.5616 |

</details>


---

## 2026-11-01 — Marseille vs Toulouse

The model's most likely 1X2 outcome is **Marseille win** at **54.6%**. Expected goals are 1.90 for Marseille and 1.05 for Toulouse (2.94 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 56.3%; Under 3.5 goals: 66.2%; Double Chance 1X: 78.0%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 82.6%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 54.6% | 1.83 |
| Draw | 23.3% | 4.28 |
| Toulouse win | 22.0% | 4.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 1.90 |
| Toulouse expected goals | 1.05 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 56.3% |
| Under 2.5 | 43.7% |
| Over 3.5 | 33.8% |
| Under 3.5 | 66.2% |
| Over 4.5 | 17.4% |
| Under 4.5 | 82.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.03% |
| 2 | 2-1 | 9.58% |
| 3 | 2-0 | 9.14% |
| 4 | 1-0 | 9.07% |
| 5 | 3-1 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 54.6% | 52.7% | 1.83 | -0.1% |
| Draw | 23.3% | 23.3% | 3.98 | -7.1% |
| Toulouse win | 22.0% | 24.1% | 3.91 | -13.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T19:45:00+00:00 |
| Fixture id | df1e1589c51bbcac432125567d1f7c58 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Marseille |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8952 |
| Dc lambda away | 1.0472 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.10 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 2.96 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.74 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.13829993467898738, "-10": 3.038636426267807e-08, "-11": 2.8505605514140854e-09, "-12": 2.4567576042966424e-10, "-13": 1.9579132254711666e-11, "-14": 1.4505682751303698e-12, "-15": 9.980972966099276e-14, "-16": 5.811860142363523e-15, "-2": 0.058922017119482625, "-3": 0.017865837989963235, "-4": 0.0042781647693283095, "-5": 0.0008427345021601581, "-6": 0.00014066527398778978, "-7": 2.0342282995886114e-05, "-8": 2.592942865136326e-06, "-9": 2.953157361425786e-07, "0": 0.23345885292073656, "1": 0.22396447440631462, "10": 1.003123706679937e-05, "11": 1.7029832184760505e-06, "12": 2.6561142381965894e-07, "13": 3.8307360097107234e-08, "14": 5.136074354300667e-09, "15": 6.395438837495167e-10, "16": 6.739333817782684e-11, "2": 0.1690902687514091, "3": 0.09278307102710888, "4": 0.04020751215800987, "5": 0.014333254519207618, "6": 0.004329575106693929, "7": 0.0011330848073912538, "8": 0.00026137257424910205, "9": 5.38713675557127e-05} |
| Raw goal margin distribution | {"-1": 0.12552806076607725, "-10": 2.7580210999225756e-08, "-11": 2.587313862048094e-09, "-12": 2.2298782610092363e-10, "-13": 1.7771017094991618e-11, "-14": 1.316609606566751e-12, "-15": 9.059239137756748e-14, "-16": 5.275140113463808e-15, "-2": 0.05348062211744505, "-3": 0.0162159440063838, "-4": 0.003883080121317862, "-5": 0.0007649087329099288, "-6": 0.00012767496312851814, "-7": 1.8463691555280993e-05, "-8": 2.3534869361529213e-06, "-9": 2.680435949426138e-07, "0": 0.23424340284935813, "1": 0.23198807328729668, "10": 1.0390609340984332e-05, "11": 1.7639931365995228e-06, "12": 2.751270379749162e-07, "13": 3.967973351670104e-08, "14": 5.32007585967801e-09, "15": 6.624557478011435e-10, "16": 6.980772605886307e-11, "2": 0.17514798167545714, "3": 0.09610705420274684, "4": 0.04164795913252783, "5": 0.014846747943671471, "6": 0.004484683518745808, "7": 0.0011736779327819731, "8": 0.00027073633026363793, "9": 5.5801326517207725e-05} |
| Unadjusted home-win probability | 56.6% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 20.0% |
| Raw p over 1 5 | 79.8% |
| Raw p under 3 5 | 66.0% |
| Raw p btts yes | 55.7% |
| P home draw | 78.0% |
| P draw away | 45.4% |
| P home away | 76.7% |
| Raw p home draw | 80.0% |
| Raw p draw away | 43.4% |
| Raw p home away | 76.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.85 |
| Reference draw odds | 4.05 |
| Reference away odds | 3.92 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | +2.0% |
| Draw probability edge | +0.1% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | 0.0391 |
| Raw ev home | 0.0353 |
| Raw edge prob draw | 0.0016 |
| Raw ev draw | -0.0677 |
| Raw edge prob away | -0.0407 |
| Raw ev away | -0.2179 |
| Elo home rating | 1,561.8610 |
| Elo away rating | 1,533.1052 |
| Elo rating diff | 88.7558 |
| Elo home expectancy | 0.6250 |

</details>


---

## 2026-11-01 — Paris FC vs AS Monaco

The model's most likely 1X2 outcome is **Paris FC win** at **38.6%**. Expected goals are 1.51 for Paris FC and 1.60 for AS Monaco (3.11 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.0%; Under 3.5 goals: 62.3%; Double Chance 1X: 63.9%; Double Chance X2: 61.4%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 79.7%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 38.6% | 2.59 |
| Draw | 25.3% | 3.95 |
| AS Monaco win | 36.1% | 2.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.51 |
| AS Monaco expected goals | 1.60 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 37.7% |
| Under 3.5 | 62.3% |
| Over 4.5 | 20.3% |
| Under 4.5 | 79.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 2-1 | 8.83% |
| 3 | 1-2 | 7.89% |
| 4 | 1-0 | 6.64% |
| 5 | 2-2 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 38.6% | 41.6% | 2.33 | -10.0% |
| Draw | 25.3% | 25.6% | 3.60 | -8.9% |
| AS Monaco win | 36.1% | 32.8% | 2.92 | +5.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:15:00+00:00 |
| Fixture id | cf3a2e2b4a4e9815d1d0be8dcef916da |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paris FC |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5115 |
| Dc lambda away | 1.5999 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.50 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.64 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.65 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.92 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.1775772973518738, "-10": 1.5359406171999345e-06, "-11": 2.1944248134215812e-07, "-12": 2.8816363461753845e-08, "-13": 3.4984817182204366e-09, "-14": 3.9124240850413363e-10, "-15": 3.5937366442391804e-11, "-2": 0.10926194261535083, "-3": 0.04933330437504606, "-4": 0.01773989743013642, "-5": 0.005273734723912744, "-6": 0.0013326330238724383, "-7": 0.0002923666701244026, "-8": 5.661852938956731e-05, "-9": 9.807244924133828e-06, "0": 0.25303847983291555, "1": 0.19840608645308752, "10": 1.0304567001388403e-06, "11": 1.3908306467014737e-07, "12": 1.725404569003929e-08, "13": 1.9789262229018902e-09, "14": 2.090711665883698e-10, "15": 1.8142314487953933e-11, "2": 0.11554161846797531, "3": 0.04928422808982016, "4": 0.016742375638900877, "5": 0.00470199845187794, "6": 0.001122465488086735, "7": 0.00023264220802987805, "8": 4.256155225575003e-05, "9": 6.964727346374518e-06} |
| Raw goal margin distribution | {"-1": 0.19393411390842424, "-10": 1.6774175925337363e-06, "-11": 2.39655540475024e-07, "-12": 3.1470666562430126e-08, "-13": 3.820730251927909e-09, "-14": 4.272801250392849e-10, "-15": 3.924759201283144e-11, "-2": 0.11932616579378055, "-3": 0.05387744274084253, "-4": 0.019373936534931375, "-5": 0.005759503528446477, "-6": 0.0014553831402090449, "-7": 0.00031929684679556986, "-8": 6.183371687545254e-05, "-9": 1.0710599736609385e-05, "0": 0.2500244014730247, "1": 0.18287261636573363, "10": 9.497809073037005e-07, "11": 1.2819407097376658e-07, "12": 1.5903204053054354e-08, "13": 1.8239935197874872e-09, "14": 1.9270271353137894e-10, "15": 1.6721929133593172e-11, "2": 0.10649571515723628, "3": 0.0454257018898562, "4": 0.015431593314490668, "5": 0.0043338728887526365, "6": 0.0010345862077935618, "7": 0.00021442834753753606, "8": 3.92293530744897e-05, "9": 6.4194498005313625e-06} |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 39.4% |
| Raw p over 1 5 | 82.3% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 62.8% |
| P home draw | 63.9% |
| P draw away | 61.4% |
| P home away | 74.7% |
| Raw p home draw | 60.6% |
| Raw p draw away | 64.4% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.32 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.92 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | -3.0% |
| Draw probability edge | -0.3% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | -0.0605 |
| Raw ev home | -0.1709 |
| Raw edge prob draw | -0.0060 |
| Raw ev draw | -0.0999 |
| Raw edge prob away | 0.0665 |
| Raw ev away | 0.1508 |
| Elo home rating | 1,505.3409 |
| Elo away rating | 1,559.0617 |
| Elo rating diff | 6.2792 |
| Elo home expectancy | 0.5090 |

</details>


---

## 2026-11-01 — Strasbourg vs Auxerre

The model's most likely 1X2 outcome is **Strasbourg win** at **53.8%**. Expected goals are 1.77 for Strasbourg and 1.04 for Auxerre (2.81 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.4%; Under 3.5 goals: 69.1%; Double Chance 1X: 77.7%; Double Chance X2: 46.2%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 54.0%; BTTS No (at least one team does not score): 46.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 53.8% | 1.86 |
| Draw | 23.9% | 4.18 |
| Auxerre win | 22.3% | 4.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.77 |
| Auxerre expected goals | 1.04 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 30.9% |
| Under 3.5 | 69.1% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.38% |
| 2 | 1-0 | 10.03% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 9.44% |
| 5 | 0-0 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 53.8% | 53.5% | 1.81 | -2.7% |
| Draw | 23.9% | 23.2% | 3.99 | -4.5% |
| Auxerre win | 22.3% | 23.2% | 4.01 | -10.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | 448a1083448ea9dff55bfebf15ff20b4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:23:13Z |
| Market best draw last update utc | 2026-10-23T16:23:13Z |
| Market best away last update utc | 2026-10-23T16:23:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Strasbourg |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7709 |
| Dc lambda away | 1.0354 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:23:20.185456+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 54.0% |
| P btts no | 46.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.42 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.23 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.49 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.13988825823640968, "-10": 2.9018701507382196e-08, "-11": 2.6943434968036367e-09, "-12": 2.297931359497616e-10, "-13": 1.812026873384411e-11, "-14": 1.3282613541149986e-12, "-15": 9.049278937814379e-14, "-16": 5.253734689300155e-15, "-2": 0.0598002120726088, "-3": 0.018093945961103804, "-4": 0.004310178421354325, "-5": 0.0008430802745434247, "-6": 0.00013957698699748443, "-7": 2.0005530146898012e-05, "-8": 2.5260461652118532e-06, "-9": 2.848856717763602e-07, "0": 0.23929640648318193, "1": 0.23284185016567752, "10": 5.93480209831048e-06, "11": 9.424865848636725e-07, "12": 1.3748433443177304e-07, "13": 1.854277576715905e-08, "14": 2.324810711611729e-09, "15": 2.7090185876467e-10, "16": 2.6900484105426435e-11, "2": 0.1669857459852584, "3": 0.08641794098937854, "4": 0.0352094971413621, "5": 0.011779516130288199, "6": 0.0033355410569404745, "7": 0.0008177046829778498, "8": 0.00017659632120835814, "9": 3.406472793638264e-05} |
| Raw goal margin distribution | {"-1": 0.13409424210369322, "-10": 2.7816779153040556e-08, "-11": 2.5827467846537323e-09, "-12": 2.2027535973561837e-10, "-13": 1.7369747348442194e-11, "-14": 1.2732462455474157e-12, "-15": 8.674467864918332e-14, "-16": 5.036130839408954e-15, "-2": 0.05732335377258616, "-3": 0.01734451483568395, "-4": 0.004131655623064789, "-5": 0.0008081608268823899, "-6": 0.0001337958633734225, "-7": 1.9176923329742702e-05, "-8": 2.421420141428717e-06, "-9": 2.730860239784553e-07, "0": 0.24625423730491136, "1": 0.23383048433453194, "10": 5.960000953823799e-06, "11": 9.464883330065435e-07, "12": 1.3806808563717165e-07, "13": 1.8621507411387853e-08, "14": 2.334681734814743e-09, "15": 2.720520937150896e-10, "16": 2.7014702136791616e-11, "2": 0.16769475862227023, "3": 0.08678486699174175, "4": 0.03535899480218796, "5": 0.011829531332154562, "6": 0.0033497035876803817, "7": 0.000821176613771429, "8": 0.00017734613983897093, "9": 3.4209364967769714e-05} |
| Unadjusted home-win probability | 54.0% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 21.4% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 54.1% |
| P home draw | 77.7% |
| P draw away | 46.2% |
| P home away | 76.1% |
| Raw p home draw | 78.6% |
| Raw p draw away | 46.0% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:23:13Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.82 |
| Reference draw odds | 4.05 |
| Reference away odds | 4.05 |
| Market reference 1x2 last update utc | 2026-10-23T16:23:17Z |
| Market reference home last update utc | 2026-10-23T16:23:17Z |
| Market reference draw last update utc | 2026-10-23T16:23:17Z |
| Market reference away last update utc | 2026-10-23T16:23:17Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-23T16:23:17Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:23:17Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.0046 |
| Raw ev home | -0.0228 |
| Raw edge prob draw | 0.0139 |
| Raw ev draw | -0.0174 |
| Raw edge prob away | -0.0185 |
| Raw ev away | -0.1424 |
| Elo home rating | 1,530.5602 |
| Elo away rating | 1,447.8570 |
| Elo rating diff | 142.7032 |
| Elo home expectancy | 0.6945 |

</details>


---
