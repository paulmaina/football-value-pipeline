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
| Training as of utc | 2026-10-23T14:35:16.325053+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 50, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-23T14:35:16.325053+00:00', 'observations': 168, 'observations_sha256': 'f347bae8059efc361920118b049fc7be40b741bf6bf2a2254495b5eb43cf1c39', 'eligible_training_matches': 75, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 87, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 75, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '690002b3b1752dfb6846f7110eff19a71928ab9a0848197ade56b0ca5acc9575', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
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
| Additional event odds calls used before this league | 31.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261023T143516325053Z_efa07bed50e2b5233642daea69e112659a870d7f236b34fc0967bc64e3007613.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
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

The model's most likely 1X2 outcome is **Brest win** at **39.0%**. Expected goals are 1.22 for Brest and 1.24 for Nice (2.46 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.6%; Double Chance 1X: 67.4%; Double Chance X2: 61.0%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 39.0% | 2.56 |
| Draw | 28.4% | 3.53 |
| Nice win | 32.6% | 3.07 |

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
| Over 2.5 | 44.7% |
| Under 2.5 | 55.3% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.49% |
| 2 | 1-0 | 10.77% |
| 3 | 0-0 | 9.17% |
| 4 | 0-1 | 8.90% |
| 5 | 2-1 | 8.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 39.0% | 43.0% | 2.34 | -8.6% |
| Draw | 28.4% | 28.0% | 3.51 | -0.4% |
| Nice win | 32.6% | 29.0% | 3.18 | +3.6% |
| Over 2.5 | 44.7% | 56.2% | 1.76 | -21.4% |
| Under 2.5 | 55.3% | 43.8% | 2.23 | +23.4% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.90 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.65 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.18197859095024446, "-10": 2.0908157387370888e-07, "-11": 2.330006926900568e-08, "-12": 2.3838330486355744e-09, "-13": 2.243830358655638e-10, "-14": 1.7934430472797825e-11, "-2": 0.09541409352382951, "-3": 0.03528570118715121, "-4": 0.010201446044844685, "-5": 0.0024120776137008344, "-6": 0.00048151849456108805, "-7": 8.308384940752532e-05, "-8": 1.2614955200494229e-05, "-9": 1.70939238828956e-06, "0": 0.283684932450701, "1": 0.22036875006899653, "10": 2.171002508736305e-07, "11": 2.378213076205484e-08, "12": 2.3917642643773236e-09, "13": 2.2130006519013153e-10, "14": 1.73871378674876e-11, "2": 0.11364889217520341, "3": 0.04131430162639837, "4": 0.011741197315883902, "5": 0.0027289206868765315, "6": 0.0005355026124467253, "7": 9.082684258728114e-05, "8": 1.3556023266973997e-05, "9": 1.8056656844554949e-06} |
| Raw goal margin distribution | {"-1": 0.20179391383641224, "-10": 2.3184809203511414e-07, "-11": 2.583717208656545e-08, "-12": 2.6434043603968947e-09, "-13": 2.4881570282181235e-10, "-14": 1.988727849048129e-11, "-2": 0.10580356330262687, "-3": 0.039127898000728044, "-4": 0.011312263236190485, "-5": 0.0026747244255724972, "-6": 0.000533950181143375, "-7": 9.213070098517042e-05, "-8": 1.3988575081750917e-05, "-9": 1.8955250643161385e-06, "0": 0.2874152457285612, "1": 0.1982362472764548, "10": 1.952960163475568e-07, "11": 2.139359756331877e-08, "12": 2.151549945224274e-09, "13": 1.9907402674649225e-10, "14": 1.5640879029580722e-11, "2": 0.10223468565704047, "3": 0.03716494335381261, "4": 0.01056198255743824, "5": 0.002454844418331153, "6": 0.0004817199728407026, "7": 8.170474452858928e-05, "8": 1.2194538379855814e-05, "9": 1.6243155574928678e-06} |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 50.8% |
| P home draw | 67.4% |
| P draw away | 61.0% |
| P home away | 71.6% |
| Raw p home draw | 63.9% |
| Raw p draw away | 64.9% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.24, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.4, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.68, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.4, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:24:03Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.04, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 4.04, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.27 |
| Reference draw odds | 3.44 |
| Reference away odds | 3.32 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
| Home probability edge | -3.9% |
| Draw probability edge | +0.4% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -11.6% |
| Under 2.5 probability edge | +11.6% |
| Raw edge prob home | -0.0784 |
| Raw ev home | -0.1781 |
| Raw edge prob draw | 0.0075 |
| Raw ev draw | 0.0088 |
| Raw edge prob away | 0.0710 |
| Raw ev away | 0.1491 |
| Market p home draw | 71.0% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:35:12Z |
| Market reference home draw last update utc | 2026-10-23T14:35:24Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.5% |
| Market draw away odds | 1.68 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:35:12Z |
| Market reference draw away last update utc | 2026-10-23T14:35:24Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:35:12Z |
| Market reference home away last update utc | 2026-10-23T14:35:24Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.68 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 80.0% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:24:03Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-23T14:35:18Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.6% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:35:15Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.74 |
| Market reference under 3 5 last update utc | 2026-10-23T14:35:15Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 59.4% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:35:12Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-23T14:35:18Z |
| Market btts yes bookmakers | 2 |
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
| RC Lens win | 45.9% | 39.8% | 2.42 | +11.0% |
| Draw | 25.7% | 25.9% | 3.68 | -5.4% |
| Paris FC win | 28.4% | 34.4% | 2.88 | -18.1% |
| Over 2.5 | 50.4% | 57.7% | 1.72 | -13.4% |
| Under 2.5 | 49.6% | 42.3% | 2.30 | +14.2% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.17823492127158622, "-10": 3.5045026898133494e-08, "-11": 3.2248676652375225e-09, "-12": 2.725520598354567e-10, "-13": 2.1291078657655213e-11, "-14": 1.5382085501564673e-12, "-15": 9.432543755340971e-14, "-2": 0.076311601776651, "-3": 0.023028709422425582, "-4": 0.005457922600376838, "-5": 0.0010606966845612654, "-6": 0.00017432117176149236, "-7": 2.478862419941353e-05, "-8": 3.1041179907230014e-06, "-9": 3.47087477559729e-07, "0": 0.2570697411711988, "1": 0.2070016609912276, "10": 3.353681302713708e-06, "11": 5.048380628798431e-07, "12": 6.97966316644912e-08, "13": 8.919232031195272e-09, "14": 1.054119435252767e-09, "15": 1.0574217278001763e-10, "2": 0.14240575679116982, "3": 0.07029936116266963, "4": 0.027255487419043226, "5": 0.008664880822549584, "6": 0.0023295193424197605, "7": 0.0005418928362792156, "8": 0.00011100537518333298, "9": 2.0304370767989004e-05} |
| Raw goal margin distribution | {"-1": 0.14085840322951926, "-10": 2.7695955959633736e-08, "-11": 2.5486010637595556e-09, "-12": 2.153968912009112e-10, "-13": 1.6826261213882038e-11, "-14": 1.215640563943598e-12, "-15": 7.454504663232419e-14, "-2": 0.06030877842264687, "-3": 0.01819950442111575, "-4": 0.004313376172046181, "-5": 0.0008382646915218358, "-6": 0.00013776538137555771, "-7": 1.9590358601306524e-05, "-8": 2.4531730397715816e-06, "-9": 2.7430195789481907e-07, "0": 0.25555461716028044, "1": 0.23459374037589553, "10": 3.8007068980265627e-06, "11": 5.721299475955554e-07, "12": 7.910010388035274e-08, "13": 1.0108112144893697e-08, "14": 1.1946272311764352e-09, "15": 1.1983696995064114e-10, "2": 0.16138758972623116, "3": 0.07966984420422371, "4": 0.030888480357036757, "5": 0.009819857446261826, "6": 0.0026400302934738665, "7": 0.0006141238999576498, "8": 0.00012580172565471, "9": 2.301082156361729e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.17, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.55, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.27, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.43, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.55, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:35:26Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.45 |
| Reference draw odds | 3.72 |
| Reference away odds | 2.82 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
| Home probability edge | +6.1% |
| Draw probability edge | -0.2% |
| Away probability edge | -6.0% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.1223 |
| Raw ev home | 0.2578 |
| Raw edge prob draw | -0.0030 |
| Raw ev draw | -0.0596 |
| Raw edge prob away | -0.1192 |
| Raw ev away | -0.3529 |
| Market p home draw | 65.8% |
| Market home draw odds | 1.47 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:35:13Z |
| Market reference home draw last update utc | 2026-10-23T14:35:24Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.4% |
| Market draw away odds | 1.58 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:35:13Z |
| Market reference draw away last update utc | 2026-10-23T14:35:24Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:35:13Z |
| Market reference home away last update utc | 2026-10-23T14:35:24Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.47 |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:35:26Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.34 |
| Market reference over 1 5 last update utc | 2026-10-23T14:35:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:35:15Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-10-23T14:35:26Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 62.7% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:35:13Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.45 |
| Market reference btts yes last update utc | 2026-10-23T14:35:18Z |
| Market btts yes bookmakers | 2 |
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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.15699143697539628, "-10": 1.869485569653581e-07, "-11": 2.117137204667647e-08, "-12": 2.2026431326526705e-09, "-13": 2.1183622266024465e-10, "-14": 1.8817323430595636e-11, "-15": 1.4017341940641371e-12, "-2": 0.08019914376053248, "-3": 0.029379834444239073, "-4": 0.0084973086901228, "-5": 0.0020213122044893555, "-6": 0.00040737903007065157, "-7": 7.112917061397628e-05, "-8": 1.0945975396399803e-05, "-9": 1.5050299555081896e-06, "0": 0.2728574404791225, "1": 0.21966881103574967, "10": 1.703708337307589e-06, "11": 2.3779079154398282e-07, "12": 3.0490395994716874e-08, "13": 3.6140324364927764e-09, "14": 3.9566038469704444e-10, "15": 3.632480436560492e-11, "2": 0.13729656988688405, "3": 0.06198865264827264, "4": 0.02209617725829007, "5": 0.006478016425055527, "6": 0.0016090895463535886, "7": 0.00034625988884039416, "8": 6.567223627165149e-05, "9": 1.1128724173526664e-05} |
| Raw goal margin distribution | {"-1": 0.17128545739690038, "-10": 2.0397016363714332e-07, "-11": 2.3099018740132e-08, "-12": 2.403193089554825e-09, "-13": 2.3112384338056696e-10, "-14": 2.0530634746021935e-11, "-15": 1.529361646755162e-12, "-2": 0.0875012503007755, "-3": 0.032054859029128864, "-4": 0.009270985944656591, "-5": 0.002205352038036038, "-6": 0.00044447076123325637, "-7": 7.760545898300475e-05, "-8": 1.1942602975991554e-05, "-9": 1.6420624544360192e-06, "0": 0.2619447867890443, "1": 0.2126516538702821, "10": 1.6492846386922258e-06, "11": 2.301947411584162e-07, "12": 2.951640291976254e-08, "13": 3.498584852066053e-09, "14": 3.830213073037741e-10, "15": 3.5164435444607614e-11, "2": 0.13291073284140983, "3": 0.060008471137490395, "4": 0.02139033127202387, "5": 0.006271080997305168, "6": 0.0015576883748043126, "7": 0.0003351988736301149, "8": 6.357438541538723e-05, "9": 1.07732253377631e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.34, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.82, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.73, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.91, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.91, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.09 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:35:15Z |
| Market best under 2 5 last update utc | 2026-10-23T14:35:15Z |
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
| Market p home draw | 74.6% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:35:13Z |
| Market reference home draw last update utc | 2026-10-23T14:35:24Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.1% |
| Market draw away odds | 1.82 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:35:13Z |
| Market reference draw away last update utc | 2026-10-23T14:35:24Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.3% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:35:13Z |
| Market reference home away last update utc | 2026-10-23T14:35:24Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 77.7% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T14:35:15Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market reference over 1 5 last update utc | 2026-10-23T14:35:18Z |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 68.8% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:35:15Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.97 |
| Market reference under 3 5 last update utc | 2026-10-23T14:35:15Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:35:13Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-23T14:35:18Z |
| Market btts yes bookmakers | 2 |
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
| Over 2.5 | 45.3% | 47.1% | 2.08 | -5.8% |
| Under 2.5 | 54.7% | 52.9% | 1.87 | +2.3% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.21109322644349082, "-10": 3.647641768075422e-07, "-11": 4.258370413197964e-08, "-12": 4.564188073073456e-09, "-13": 4.499906264981531e-10, "-14": 3.7601953153254273e-11, "-2": 0.11537012740919894, "-3": 0.04460471076056305, "-4": 0.013492504232871967, "-5": 0.0033393944580711946, "-6": 0.0006980008904125109, "-7": 0.00012612621797280217, "-8": 2.0057404564668673e-05, "-9": 2.846885920756357e-06, "0": 0.2869438881503298, "1": 0.18601392540320472, "10": 1.4684064010057402e-07, "11": 1.5707921529873658e-08, "12": 1.5426948064440888e-09, "13": 1.3936738502918869e-10, "14": 1.0671102376098175e-11, "2": 0.09345399559338784, "3": 0.03310750306127301, "4": 0.009176550558407702, "5": 0.0020811137526619496, "6": 0.0003985889659924202, "7": 6.599573454190725e-05, "8": 9.616707939277903e-06, "9": 1.2507282382069106e-06} |
| Raw goal margin distribution | {"-1": 0.20826172786452224, "-10": 3.5987141323719765e-07, "-11": 4.201250770010741e-08, "-12": 4.50296634530517e-09, "-13": 4.4395467811200354e-10, "-14": 3.7097579428366497e-11, "-2": 0.1138226104314241, "-3": 0.04400640556024129, "-4": 0.013311522553801693, "-5": 0.0032946014970560507, "-6": 0.0006886382568376678, "-7": 0.00012443442419534398, "-8": 1.978836460787091e-05, "-9": 2.808699222040729e-06, "0": 0.284823418041793, "1": 0.19022102685477835, "10": 1.5016175419876877e-07, "11": 1.6063189660075687e-08, "12": 1.5775861380766947e-09, "13": 1.425194755330979e-10, "14": 1.0912452104077197e-11, "2": 0.09556765692096889, "3": 0.033856299818747715, "4": 0.009384097811071888, "5": 0.002128182576518742, "6": 0.00040760390513621325, "7": 6.74883687626361e-05, "8": 9.834210289400335e-06, "9": 1.2790161235094686e-06} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.78, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.17, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.02 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
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
| Auxerre win | 44.4% | 46.4% | 2.12 | -5.9% |
| Draw | 25.0% | 25.8% | 3.68 | -7.9% |
| Le Mans FC win | 30.6% | 27.8% | 3.45 | +5.5% |
| Over 2.5 | 62.7% | 57.0% | 1.74 | +9.1% |
| Under 2.5 | 37.3% | 43.0% | 2.27 | -15.3% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7277 |
| Dc lambda away | 1.5163 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.15862841001145925, "-10": 8.014509917539414e-07, "-11": 1.0836298345581555e-07, "-12": 1.3469795263193628e-08, "-13": 1.5490578281768146e-09, "-14": 1.6563073851542151e-10, "-15": 1.638832005576122e-11, "-16": 1.33460827950319e-12, "-2": 0.09103599095635544, "-3": 0.038513208432421016, "-4": 0.0130236199476777, "-5": 0.003648922752672637, "-6": 0.0008702277793211029, "-7": 0.00018035841631240616, "-8": 3.301724338659987e-05, "-9": 5.4089318560876395e-06, "0": 0.25021520953900256, "1": 0.20756988608917817, "10": 3.3804415447237966e-06, "11": 5.207802726829367e-07, "12": 7.375843224319969e-08, "13": 9.664856820867915e-09, "14": 1.1774591351247938e-09, "15": 1.3274447475212528e-10, "16": 1.2317226922607959e-11, "2": 0.13517385297543283, "3": 0.0651577952181111, "4": 0.025105305234110344, "5": 0.008014484116781986, "6": 0.002177814861284525, "7": 0.0005142822543379811, "8": 0.00010727117759786618, "9": 2.0023078891145147e-05} |
| Raw goal margin distribution | {"-1": 0.17307780514713167, "-10": 8.744548254360206e-07, "-11": 1.1823372203234359e-07, "-12": 1.4696753247204393e-08, "-13": 1.6901608540831853e-09, "-14": 1.8071797280875947e-10, "-15": 1.7881125235353277e-11, "-16": 1.4561771862361544e-12, "-2": 0.09932842107527835, "-3": 0.04202136038667916, "-4": 0.014209936009896482, "-5": 0.003981301591173909, "-6": 0.0009494964616494512, "-7": 0.00019678718858058824, "-8": 3.602477019689308e-05, "-9": 5.901629183413119e-06, "0": 0.24277709149810464, "1": 0.19801560117050981, "10": 3.224842376281229e-06, "11": 4.968091504793195e-07, "12": 7.036338737381502e-08, "13": 9.219990768742054e-09, "14": 1.1232615813802306e-09, "15": 1.266343469438174e-10, "16": 1.1750274280084806e-11, "2": 0.12895190272429366, "3": 0.062158631168280555, "4": 0.02394972701563132, "5": 0.007645583472422719, "6": 0.002077571689806929, "7": 0.0004906102310058054, "8": 0.00010233356639789297, "9": 1.9101431708697957e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.09 |
| Reference draw odds | 3.68 |
| Reference away odds | 3.42 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
| Home probability edge | -2.0% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | +5.7% |
| Under 2.5 probability edge | -5.7% |
| Raw edge prob home | -0.0409 |
| Raw ev home | -0.1024 |
| Raw edge prob draw | -0.0149 |
| Raw ev draw | -0.1066 |
| Raw edge prob away | 0.0557 |
| Raw ev away | 0.1516 |
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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.10441104751256926, "-10": 2.4983169901275957e-09, "-11": 1.8163592753905397e-10, "-12": 1.2128501129810492e-11, "-13": 7.487088924338025e-13, "-14": 4.296989433069075e-14, "-15": 2.3036763466570878e-15, "-16": 1.153985789360684e-16, "-17": 4.995500274661125e-18, "-2": 0.035787678100425734, "-3": 0.008536574093945348, "-4": 0.0015989478094973499, "-5": 0.00024555356188266173, "-6": 3.1887871261939644e-05, "-7": 3.5828606390904306e-06, "-8": 3.544909898642045e-07, "-9": 3.1317447627149397e-08, "0": 0.2009277261274042, "1": 0.23032845681907937, "10": 2.9697750015717756e-05, "11": 5.631534984215561e-06, "12": 9.808016504264377e-07, "13": 1.5791961294288166e-07, "14": 2.3639396763349313e-08, "15": 3.305541332702123e-09, "16": 4.318874797716338e-10, "17": 4.876387004934151e-11, "2": 0.19861741769587793, "3": 0.1235709676733714, "4": 0.06036930087810164, "5": 0.024181159453386256, "6": 0.008190406093338683, "7": 0.0024002630955942406, "8": 0.0006194170530541541, "9": 0.00014272936740501995} |
| Raw goal margin distribution | {"-1": 0.08789922120551259, "-10": 2.103226842258047e-09, "-11": 1.5291156399615456e-10, "-12": 1.021046938133806e-11, "-13": 6.303061804513613e-13, "-14": 3.6174526900481497e-14, "-15": 1.9393671608968586e-15, "-16": 9.714915670664247e-17, "-17": 4.205499265983105e-18, "-2": 0.030128124453519273, "-3": 0.0071865787433137325, "-4": 0.0013460861714480747, "-5": 0.0002067211024880032, "-6": 2.6845042901123254e-05, "-7": 3.016258024094834e-06, "-8": 2.9843089094268293e-07, "-9": 2.636482749815794e-08, "0": 0.2040372769824245, "1": 0.23768425447853797, "10": 3.0646180978498854e-05, "11": 5.811384371599729e-06, "12": 1.0121246514322009e-06, "13": 1.6296295294224743e-07, "14": 2.4394347418532335e-08, "15": 3.41110750343991e-09, "16": 4.456802909454136e-10, "17": 5.032119894447166e-11, "2": 0.20496048774632608, "3": 0.12751734515248073, "4": 0.06229726222614774, "5": 0.024953411907844933, "6": 0.0084519759002285, "7": 0.0024769181902555377, "8": 0.0006391988315282897, "9": 0.0001472875898721575} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.98, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.70 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:19Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | 0.0414 |
| Raw ev home | 0.0707 |
| Raw edge prob draw | 0.0062 |
| Raw ev draw | -0.0329 |
| Raw edge prob away | -0.0476 |
| Raw ev away | -0.3647 |
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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.13514276636101674, "-10": 1.3063806374426228e-07, "-11": 1.4603883447337841e-08, "-12": 1.5004909873882462e-09, "-13": 1.4260711757314783e-10, "-14": 1.2600966775944057e-11, "-15": 1.031840705315367e-12, "-16": 7.025147487055046e-14, "-2": 0.06583229839693971, "-3": 0.023299523405044223, "-4": 0.00656304199487842, "-5": 0.001527729666938427, "-6": 0.000302205804884967, "-7": 5.189317732751327e-05, "-8": 7.864652193334335e-06, "-9": 1.0660291687431464e-06, "0": 0.226538671670234, "1": 0.2275516700956566, "10": 9.451340432218597e-06, "11": 1.6070129863164415e-06, "12": 2.511376209287175e-07, "13": 3.630337007909308e-08, "14": 4.879069045611532e-09, "15": 6.076774357748412e-10, "16": 6.292790259086231e-11, "2": 0.166281463290143, "3": 0.08951157810308995, "4": 0.03834994239779139, "5": 0.013577924877346997, "6": 0.0040852350364095034, "7": 0.001066969155518671, "8": 0.0002459509360837619, "9": 5.0706706501594185e-05} |
| Raw goal margin distribution | {"-1": 0.14203322415400368, "-10": 1.3729884247941652e-07, "-11": 1.5348484473476146e-08, "-12": 1.5769957837288544e-09, "-13": 1.498781565719525e-10, "-14": 1.3243446074381147e-11, "-15": 1.0844506601099017e-12, "-16": 7.383335228452534e-14, "-2": 0.06918885743249814, "-3": 0.02448748475097595, "-4": 0.006897668590714891, "-5": 0.0016056232684428708, "-6": 0.00031761422369587706, "-7": 5.453902924950236e-05, "-8": 8.265643348494857e-06, "-9": 1.120382273915607e-06, "0": 0.2348946522398448, "1": 0.21904183114827844, "10": 9.097884951618463e-06, "11": 1.5469148921378779e-06, "12": 2.41745728938504e-07, "13": 3.494571872680777e-08, "14": 4.6966045891923e-09, "15": 5.849518846583595e-10, "16": 6.05745631663728e-11, "2": 0.16006297026858596, "3": 0.08616407855161337, "4": 0.03691575457878199, "5": 0.013070145901709287, "6": 0.003932457901407957, "7": 0.0010270672920365568, "8": 0.00023675301257852083, "9": 4.881040793477134e-05} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.74 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:19Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0404 |
| Raw ev home | -0.0579 |
| Raw edge prob draw | 0.0167 |
| Raw ev draw | 0.0312 |
| Raw edge prob away | 0.0237 |
| Raw ev away | -0.0412 |
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
| Toulouse win | 60.5% | 60.7% | 1.64 | -0.9% |
| Draw | 22.5% | 22.0% | 4.33 | -2.6% |
| Troyes win | 17.1% | 17.3% | 4.97 | -15.2% |
| Over 2.5 | 53.7% | 59.6% | 1.67 | -10.4% |
| Under 2.5 | 46.3% | 40.4% | 2.40 | +11.2% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.11296936042683073, "-10": 7.630455960906615e-09, "-11": 6.234267233141544e-10, "-12": 4.678251748773924e-11, "-13": 3.2455586184882607e-12, "-14": 2.0930066922471585e-13, "-15": 1.2550394936813531e-14, "-16": 6.442067857387667e-16, "-2": 0.043133088709068304, "-3": 0.011545744908815207, "-4": 0.002428135661481266, "-5": 0.00041881502767962466, "-6": 6.109755486980105e-05, "-7": 7.712699591921337e-06, "-8": 8.574296947019908e-07, "-9": 8.511855113698776e-08, "0": 0.22491120470157358, "1": 0.2412641560608716, "10": 1.234799587994522e-05, "11": 2.113946440288965e-06, "12": 3.3239519205558793e-07, "13": 4.831958343329583e-08, "14": 6.529304466964774e-09, "15": 8.203822882563961e-10, "16": 8.823619213731156e-11, "2": 0.18782608597180514, "3": 0.10534887140644247, "4": 0.04642409607000056, "5": 0.016778585478290697, "6": 0.0051288440974346945, "7": 0.0013566401418349686, "8": 0.0003160234768424721, "9": 6.573665916928543e-05} |
| Raw goal margin distribution | {"-1": 0.11151110943877361, "-10": 7.531959165826275e-09, "-11": 6.153792967214997e-10, "-12": 4.6178631158804235e-11, "-13": 3.203663727304264e-12, "-14": 2.0659893747599413e-13, "-15": 1.2388389719222086e-14, "-16": 6.358911222857094e-16, "-2": 0.0425763105792258, "-3": 0.011396708091597499, "-4": 0.002396792373229359, "-5": 0.0004134088058012371, "-6": 6.030888465497351e-05, "-7": 7.613141165123022e-06, "-8": 8.463616697546555e-07, "-9": 8.401980886892036e-08, "0": 0.2299773584338605, "1": 0.24012096523466428, "10": 1.2289486916813383e-05, "11": 2.1039298501037966e-06, "12": 3.3082019168902917e-07, "13": 4.809062897354936e-08, "14": 6.498366423411112e-09, "15": 8.164950406800048e-10, "16": 8.781809934210416e-11, "2": 0.18693610271896247, "3": 0.1048496929735187, "4": 0.04620412306775813, "5": 0.016699082889473988, "6": 0.00510454190676964, "7": 0.0013502119239432934, "8": 0.0003145260511763847, "9": 6.542517673884564e-05} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.81, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.1, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.61 |
| Reference draw odds | 4.25 |
| Reference away odds | 5.35 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0057 |
| Raw ev home | -0.0133 |
| Raw edge prob draw | 0.0101 |
| Raw ev draw | -0.0042 |
| Raw edge prob away | -0.0044 |
| Raw ev away | -0.1632 |
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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.09013585684753048, "-10": 2.4552364827397864e-08, "-11": 2.3983731975255984e-09, "-12": 2.153938724414489e-10, "-13": 1.789787671776531e-11, "-14": 1.3835663670999068e-12, "-15": 9.99752968878003e-14, "-16": 6.778235202154187e-15, "-17": 4.29352197317625e-16, "-18": 2.2776978279405494e-17, "-2": 0.03775235646084814, "-3": 0.011518530487730813, "-4": 0.0028109475386728024, "-5": 0.000568574468960383, "-6": 9.79185884722411e-05, "-7": 1.4657194566747712e-05, "-8": 1.9381552598716197e-06, "-9": 2.29366343039404e-07, "0": 0.18301846637639566, "1": 0.21952640945420235, "10": 7.386192222272797e-05, "11": 1.5958795729879783e-05, "12": 3.170098630922572e-06, "13": 5.826356027330575e-07, "14": 9.962115666550935e-08, "15": 1.5922100568407078e-08, "16": 2.387703364974726e-09, "17": 3.3452879281791966e-10, "18": 3.9252922584089324e-11, "2": 0.19825435174250508, "3": 0.13379251475341125, "4": 0.07221768416460951, "5": 0.03230979840684475, "6": 0.0123074509857343, "7": 0.00407483380176677, "8": 0.0011918008420718472, "9": 0.00031196142162501857} |
| Raw goal margin distribution | {"-1": 0.09497918746785698, "-10": 2.5871653560305952e-08, "-11": 2.5272465976664032e-09, "-12": 2.2696777626078063e-10, "-13": 1.885959536534653e-11, "-14": 1.4579104692740735e-12, "-15": 1.0534733675770457e-13, "-16": 7.14245467323439e-15, "-17": 4.524228677134309e-16, "-18": 2.4000868972825786e-17, "-2": 0.0397809292223586, "-3": 0.012137463433658862, "-4": 0.0029619900733792157, "-5": 0.0005991260633176639, "-6": 0.00010318011384553375, "-7": 1.5444779460662854e-05, "-8": 2.0422994600311836e-06, "-9": 2.4169103901909826e-07, "0": 0.18769754928606577, "1": 0.21550190908732483, "10": 7.250783761020818e-05, "11": 1.5666228747030166e-05, "12": 3.111982328948219e-06, "13": 5.719543493805113e-07, "14": 9.779483707805785e-08, "15": 1.5630206305031974e-08, "16": 2.3439304399210763e-09, "17": 3.283959942504303e-10, "18": 3.853331257573796e-11, "2": 0.19461982451953225, "3": 0.13133974369024268, "4": 0.07089374278945504, "5": 0.03171747424928498, "6": 0.012081822820400738, "7": 0.004000131308472467, "8": 0.0011699519768802367, "9": 0.00030624234272739077} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.43 |
| Reference draw odds | 5.15 |
| Reference away odds | 6.70 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:19Z |
| Home probability edge | -1.2% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.24129119445927508, "-10": 6.49129236762937e-05, "-11": 1.342473163002391e-05, "-12": 2.550456799334448e-06, "-13": 4.480223072472693e-07, "-14": 7.317857433933526e-08, "-15": 1.1168159578520645e-08, "-16": 1.5990894767720766e-09, "-17": 2.146818623781627e-10, "-18": 2.4897234459797228e-11, "-2": 0.2227142394656334, "-3": 0.14960227483299077, "-4": 0.07921548297228717, "-5": 0.03446768214186194, "-6": 0.012699415636076171, "-7": 0.0040520789665780994, "-8": 0.0011392469201976113, "-9": 0.00028612859265035324, "0": 0.1576142761579312, "1": 0.06720400222831226, "10": 1.7184548331996637e-09, "11": 1.2646533865983842e-10, "12": 8.549541356563143e-12, "13": 5.344208963174433e-13, "14": 3.106180465888083e-14, "15": 1.686876537424599e-15, "16": 8.594752979749611e-17, "17": 4.105962088803486e-18, "18": 1.694453429365621e-19, "2": 0.022934187586110936, "3": 0.005481917809562566, "4": 0.0010329120499275675, "5": 0.00015992792253822997, "6": 2.0967898271972427e-05, "7": 2.3807183032773537e-06, "8": 2.3818089389712197e-07, "9": 2.128674528304378e-08} |
| Raw goal margin distribution | {"-1": 0.22749607390278032, "-10": 6.120171651933236e-05, "-11": 1.2657211739006812e-05, "-12": 2.404641867712943e-06, "-13": 4.2240793804359675e-07, "-14": 6.899480270429561e-08, "-15": 1.052965261549151e-08, "-16": 1.5076661980978269e-09, "-17": 2.024080528036512e-10, "-18": 2.3473807667676194e-11, "-2": 0.2099812021496156, "-3": 0.14104920093623363, "-4": 0.0746865686868216, "-5": 0.0324970929062478, "-6": 0.01197336357234753, "-7": 0.0038204131655377874, "-8": 0.0010741137990202699, "-9": 0.0002697700245761337, "0": 0.18480787110823407, "1": 0.07791302905986308, "10": 1.992292377205197e-09, "11": 1.4661772036425447e-10, "12": 9.911919559483861e-12, "13": 6.195814154567907e-13, "14": 3.6011535158535626e-14, "15": 1.9556820475402318e-15, "16": 9.964335701296424e-17, "17": 4.760251368018506e-18, "18": 1.964466325000058e-19, "2": 0.026588773951147577, "3": 0.006355467047173741, "4": 0.0011975076467750185, "5": 0.00018541260137860062, "6": 2.4309154413726174e-05, "7": 2.7600882119555092e-06, "8": 2.7613526415682154e-07, "9": 2.467881002374262e-08} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.26, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.75, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 2.0, "market_key": "spreads", "opposite_price": 2.03, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 10.50 |
| Reference draw odds | 6.75 |
| Reference away odds | 1.25 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:19Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:19Z |
| Home probability edge | +1.5% |
| Draw probability edge | +2.7% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -11.3% |
| Under 2.5 probability edge | +11.3% |
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
| Over 2.5 | 42.7% | 56.6% | 1.75 | -25.3% |
| Under 2.5 | 57.3% | 43.4% | 2.25 | +29.0% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.19169629888391124, "-10": 9.455130382751809e-08, "-11": 9.559283320617434e-09, "-12": 8.872020031587755e-10, "-13": 7.579493278095242e-11, "-14": 5.5310206481541565e-12, "-2": 0.0924723379643356, "-3": 0.03122555435712769, "-4": 0.008222155168448859, "-5": 0.0017681074752302, "-6": 0.00032073361573721064, "-7": 5.025905872341034e-05, "-8": 6.927544835822448e-06, "-9": 8.519408854424115e-07, "0": 0.2798105579387919, "1": 0.21818117517389074, "10": 2.7149749847807613e-07, "11": 3.043429991023375e-08, "12": 3.1318443377825365e-09, "13": 2.966589796080994e-10, "14": 2.400282054658896e-11, "2": 0.11624994938302614, "3": 0.04352419664193258, "4": 0.012707085351188283, "5": 0.0030297626731342195, "6": 0.0006093742558815493, "7": 0.00010587505406801783, "8": 1.6180737475675374e-05, "9": 2.206317955614839e-06} |
| Raw goal margin distribution | {"-1": 0.1905077214302794, "-10": 9.396505595212774e-08, "-11": 9.500012752046646e-09, "-12": 8.81701071195503e-10, "-13": 7.532498031589444e-11, "-14": 5.4967265773961736e-12, "-2": 0.09189898033234711, "-3": 0.0310319460814222, "-4": 0.008171175215730006, "-5": 0.0017571446517803363, "-6": 0.0003187449662614169, "-7": 4.994743672346979e-05, "-8": 6.884591875077658e-06, "-9": 8.466585835192156e-07, "0": 0.2929352312677429, "1": 0.2120384109278271, "10": 2.6385364412071623e-07, "11": 2.957743987547795e-08, "12": 3.043669079733649e-09, "13": 2.8830671836577186e-10, "14": 2.332703507728458e-11, "2": 0.11297699958748292, "3": 0.042298798168587566, "4": 0.01234932474464307, "5": 0.0029444614650544943, "6": 0.0005922176776913482, "7": 0.00010289420342331516, "8": 1.572517821140198e-05, "9": 2.1442003552196745e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.38 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.92 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.19478568492950848, "-10": 5.683794909860863e-07, "-11": 7.105797536136596e-08, "-12": 8.158023709171135e-09, "-13": 8.597441593574574e-10, "-14": 7.530569984249943e-11, "-2": 0.10985998802823954, "-3": 0.04453115736244784, "-4": 0.014238500763088791, "-5": 0.0037425309995415146, "-6": 0.0008331876269607043, "-7": 0.0001606620368481288, "-8": 2.730099176851221e-05, "-9": 4.144595950832354e-06, "0": 0.26963596051190186, "1": 0.19292641264970262, "10": 5.150776234675588e-07, "11": 6.375898341884064e-08, "12": 7.24782649938121e-09, "13": 7.562864683514654e-10, "14": 6.559023927379065e-11, "2": 0.1077754061567353, "3": 0.04325520492396284, "4": 0.01369408201589297, "5": 0.003563923214551391, "6": 0.0007855973586581773, "7": 0.00014999084150340788, "8": 2.523621202853643e-05, "9": 3.7933438587267897e-06} |
| Raw goal margin distribution | {"-1": 0.1953697351670082, "-10": 5.700837341742883e-07, "-11": 7.127103736025499e-08, "-12": 8.182484930161754e-09, "-13": 8.623220376067928e-10, "-14": 7.55314983240152e-11, "-2": 0.110189394946016, "-3": 0.04466468069114157, "-4": 0.014281193837558465, "-5": 0.0037537526974805763, "-6": 0.0008356858774434555, "-7": 0.00016114376989135673, "-8": 2.7382851740574056e-05, "-9": 4.157023210311406e-06, "0": 0.2676898293902507, "1": 0.19337501482358938, "10": 5.162753077992915e-07, "11": 6.390723900589929e-08, "12": 7.264679509183865e-09, "13": 7.580450235908645e-10, "14": 6.574275298883805e-11, "2": 0.10802601093826526, "3": 0.043355784096582604, "4": 0.013725924182433784, "5": 0.0035722102276132895, "6": 0.0007874240690502564, "7": 0.00015033960773317087, "8": 2.5294892534855823e-05, "9": 3.8021643321806484e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.66 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.62 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:35:15Z |
| Market best under 2 5 last update utc | 2026-10-23T14:35:15Z |
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
| Over 2.5 | 57.7% | 60.8% | 1.64 | -5.4% |
| Under 2.5 | 42.3% | 39.2% | 2.46 | +4.0% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.08520955766855773, "-10": 2.5813059382200647e-09, "-11": 1.9307142164362905e-10, "-12": 1.326429314887287e-11, "-13": 8.425187686600886e-13, "-14": 4.975576742610583e-14, "-15": 2.7448814581881686e-15, "-16": 1.4144505598113477e-16, "-17": 6.277079515309056e-18, "-2": 0.029797421647690794, "-3": 0.00728117346038295, "-4": 0.0013993872274153415, "-5": 0.00022072187058487576, "-6": 2.9456035718175874e-05, "-7": 3.4024813922804893e-06, "-8": 3.461814732777883e-07, "-9": 3.145580831388141e-08, "0": 0.19064017757877014, "1": 0.24086750908891916, "10": 3.468554201959411e-05, "11": 6.672407641441303e-06, "12": 1.1789740870523835e-06, "13": 1.925995660441461e-07, "14": 2.9253290278865544e-08, "15": 4.150595937957549e-09, "16": 5.500855119091132e-10, "17": 6.278496212363236e-11, "2": 0.2091428964544925, "3": 0.13143813280675223, "4": 0.06497009186172131, "5": 0.02635581890946599, "6": 0.009046092332024611, "7": 0.002687435494525806, "8": 0.0007032369530365051, "9": 0.00016434416266037724} |
| Raw goal margin distribution | {"-1": 0.08832713709748437, "-10": 2.6757487039490384e-09, "-11": 2.0013536504269105e-10, "-12": 1.374959654196205e-11, "-13": 8.733441743249808e-13, "-14": 5.1576191815602745e-14, "-15": 2.8453089947583682e-15, "-16": 1.4662013503230652e-16, "-17": 6.506740301095361e-18, "-2": 0.030887625978116198, "-3": 0.007547571235698626, "-4": 0.001450586892718881, "-5": 0.00022879746658698404, "-6": 3.053374969211662e-05, "-7": 3.5269686714791422e-06, "-8": 3.5884728529812935e-07, "-9": 3.2606688374790396e-08, "0": 0.20193489814581636, "1": 0.23530479438103785, "10": 3.388449676665381e-05, "11": 6.518311722633412e-06, "12": 1.1517462699048403e-06, "13": 1.8815157535076526e-07, "14": 2.8577700164185134e-08, "15": 4.054739999737066e-09, "16": 5.373815620104175e-10, "17": 6.13349748108563e-11, "2": 0.20431284581562933, "3": 0.12840263483815464, "4": 0.06346964007003453, "5": 0.025747144447557466, "6": 0.008837177351940565, "7": 0.002625370515282954, "8": 0.0006869960471684675, "9": 0.00016054871638269836} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.17, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.40 |
| Reference draw odds | 5.10 |
| Reference away odds | 7.50 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
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
| Over 2.5 | 49.6% | 60.5% | 1.65 | -18.2% |
| Under 2.5 | 50.4% | 39.5% | 2.45 | +23.5% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nice |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3431 |
| Dc lambda away | 1.2983 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.20432307265402733, "-10": 3.307530730828959e-07, "-11": 3.8535445517458794e-08, "-12": 4.122550427448207e-09, "-13": 4.052676743484235e-10, "-14": 3.3421208234598e-11, "-2": 0.10944693552910723, "-3": 0.04176092445388872, "-4": 0.012521087285975112, "-5": 0.0030792865189576855, "-6": 0.0006405217215806047, "-7": 0.0001152959561754963, "-8": 1.827740241723513e-05, "-9": 2.5873556333759737e-06, "0": 0.2645380568369145, "1": 0.19530576107274514, "10": 4.284850327986218e-07, "11": 5.1644184592843616e-08, "12": 5.715527111093339e-09, "13": 5.812481031883956e-10, "14": 4.958736176729845e-11, "2": 0.10809390296826787, "3": 0.04266747751526757, "4": 0.013234214804312628, "5": 0.003366941021900388, "6": 0.0007245169373432578, "7": 0.00013491431346713626, "8": 2.2125225120780635e-05, "9": 3.240101559778467e-06} |
| Raw goal margin distribution | {"-1": 0.19327872639056223, "-10": 3.1287476193876935e-07, "-11": 3.6452475649281655e-08, "-12": 3.8997127722685115e-09, "-13": 3.8336159948984846e-10, "-14": 3.1614680016850995e-11, "-2": 0.10353096217496056, "-3": 0.039503606648512324, "-4": 0.011844280590651303, "-5": 0.0029128407714557655, "-6": 0.0006058993777086263, "-7": 0.00010906382366966021, "-8": 1.7289447613743878e-05, "-9": 2.4475003974960915e-06, "0": 0.275548908712242, "1": 0.2001901247047796, "10": 4.3920093129325525e-07, "11": 5.293574391831278e-08, "12": 5.85846561227218e-09, "13": 5.957844234731052e-10, "14": 5.0827482412457063e-11, "2": 0.11079720227496993, "3": 0.043734540126741675, "4": 0.013565186697479872, "5": 0.003451144192294577, "6": 0.0007426362399184353, "7": 0.00013828835918150886, "8": 2.2678550554382474e-05, "9": 3.3211326268384163e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.71 |
| Reference draw odds | 3.74 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
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
| Over 2.5 | 64.4% | 52.7% | 1.88 | +21.0% |
| Under 2.5 | 35.6% | 47.3% | 2.07 | -26.2% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.16378988663866537, "-10": 3.766836716434249e-06, "-11": 6.053215884991324e-07, "-12": 8.944266920502111e-08, "-13": 1.2228843421247024e-08, "-14": 1.5545151120040757e-09, "-15": 1.8267523807181493e-10, "-16": 1.7550773388073077e-11, "-2": 0.10973911035361647, "-3": 0.0547545239790118, "-4": 0.02189848679599231, "-5": 0.007268671050088253, "-6": 0.0020559128520450916, "-7": 0.0005057190235620853, "-8": 0.00010993591413580344, "-9": 2.1394377950458255e-05, "0": 0.2525519578584428, "1": 0.20024162436935228, "10": 1.1155106543127174e-06, "11": 1.5304929143445385e-07, "12": 1.9308037961087474e-08, "13": 2.253860381864358e-09, "14": 2.446159695798226e-10, "15": 2.45424419521378e-11, "16": 2.013179881911222e-12, "2": 0.11509925225742253, "3": 0.04903196602309914, "4": 0.0167425512897423, "5": 0.0047447220896029265, "6": 0.0011457996858479638, "7": 0.00024063651022540266, "8": 4.466219408686476e-05, "9": 7.420759535689883e-06} |
| Raw goal margin distribution | {"-1": 0.19839984335808214, "-10": 4.562795846758986e-06, "-11": 7.332303038003488e-07, "-12": 1.0834253520763988e-07, "-13": 1.4812884171403884e-08, "-14": 1.882995104574261e-09, "-15": 2.2127580257017366e-10, "-16": 2.125937542583837e-11, "-2": 0.13292775733122153, "-3": 0.06632454056548465, "-4": 0.026525791300464056, "-5": 0.008804592440681882, "-6": 0.002490341718737865, "-7": 0.0006125810153301266, "-8": 0.0001331661471387944, "-9": 2.5915160705120755e-05, "0": 0.237697910327464, "1": 0.16857532288870314, "10": 9.391032924787653e-07, "11": 1.2884600693140961e-07, "12": 1.6254656063086887e-08, "13": 1.8974338767748836e-09, "14": 2.059322889809875e-10, "15": 2.0661289028137276e-11, "16": 1.6948147004652835e-12, "2": 0.09689740419681185, "3": 0.041278028632876676, "4": 0.014094876619873034, "5": 0.00399438958204134, "6": 0.0009646024028017127, "7": 0.00020258214313740187, "8": 3.7599294416548335e-05, "9": 6.2472372502378124e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.16 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.35 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
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
| Raw ev away | 0.4483 |
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
| Over 2.5 | 56.3% | 60.8% | 1.64 | -7.7% |
| Under 2.5 | 43.7% | 39.2% | 2.46 | +7.5% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.13829984044422727, "-10": 3.038556709120745e-08, "-11": 2.850477583009855e-09, "-12": 2.4566790355754447e-10, "-13": 1.9578449769529373e-11, "-14": 1.4505135367415587e-12, "-15": 9.980567748681598e-14, "-16": 5.811608323495831e-15, "-2": 0.0589218003603946, "-3": 0.0178657237770701, "-4": 0.004278125553262761, "-5": 0.0008427244103149967, "-6": 0.00014066319137294434, "-7": 2.034192394932724e-05, "-8": 2.5928896966439827e-06, "-9": 2.953088354660213e-07, "0": 0.23345863618825366, "1": 0.22396442195557997, "10": 1.0031367786768223e-05, "11": 1.7030078522932197e-06, "12": 2.656156459041877e-07, "13": 3.830802372870643e-08, "14": 5.136170661333151e-09, "15": 6.395567981848553e-10, "16": 6.739480526390426e-11, "2": 0.1690904622790904, "3": 0.09278332486275222, "4": 0.04020768373857688, "5": 0.014333337138192787, "6": 0.0043296064490074065, "7": 0.0011330946648219185, "8": 0.00026137522721485755, "9": 5.387199210773036e-05} |
| Raw goal margin distribution | {"-1": 0.12552764822418017, "-10": 2.7579415599221122e-08, "-11": 2.587231815753753e-09, "-12": 2.2298011392268714e-10, "-13": 1.777035134350257e-11, "-14": 1.316556493482968e-12, "-15": 9.058847742773341e-14, "-16": 5.2748978083072885e-15, "-2": 0.053480286055411067, "-3": 0.016215798097488236, "-4": 0.003883034411203181, "-5": 0.0007648975804177518, "-6": 0.0001276727402435012, "-7": 1.846331756791813e-05, "-8": 2.3534325468414733e-06, "-9": 2.6803663328028323e-07, "0": 0.2342429693843921, "1": 0.23198829324775083, "10": 1.0390757029499914e-05, "11": 1.7640207386125802e-06, "12": 2.7513173661767056e-07, "13": 3.968046783912648e-08, "14": 5.320181907232444e-09, "15": 6.624699081683953e-10, "16": 6.980932824249476e-11, "2": 0.17514838922219292, "3": 0.09610743076429608, "4": 0.04164818610255789, "5": 0.014846851076611817, "6": 0.004484721286396528, "7": 0.0011736895310644673, "8": 0.0002707393983801772, "9": 5.5802039421276456e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.85 |
| Reference draw odds | 4.05 |
| Reference away odds | 3.92 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
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
| Over 2.5 | 60.0% | 56.6% | 1.75 | +5.0% |
| Under 2.5 | 40.0% | 43.4% | 2.25 | -10.0% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.177577262614067, "-10": 1.5359121794589955e-06, "-11": 2.1943798607777513e-07, "-12": 2.8815716432422155e-08, "-13": 3.498396278843979e-09, "-14": 3.9123207996744327e-10, "-15": 3.5936344374979865e-11, "-2": 0.10926166253089056, "-3": 0.049333077222612945, "-4": 0.017739780003913592, "-5": 0.005273689271867128, "-6": 0.0013326188875099406, "-7": 0.0002923629891008412, "-8": 5.661770455102336e-05, "-9": 9.807082684107756e-06, "0": 0.25303841637634694, "1": 0.1984061705116712, "10": 1.030479854601812e-06, "11": 1.3908654227122142e-07, "12": 1.7254520847517173e-08, "13": 1.9789857377956477e-09, "14": 2.090779824329253e-10, "15": 1.814295061958461e-11, "2": 0.1155418948154493, "3": 0.04928446733764465, "4": 0.01674249858288663, "5": 0.004702044756040733, "6": 0.0011224793642406407, "7": 0.00023264567052367404, "8": 4.256229321643662e-05, "9": 6.964866211619202e-06} |
| Raw goal margin distribution | {"-1": 0.19393375266608226, "-10": 1.6773837390172066e-06, "-11": 2.3965023162925643e-07, "-12": 3.146990747146833e-08, "-13": 3.8206305733171375e-09, "-14": 4.2726813283714105e-10, "-15": 3.9246410374547707e-11, "-2": 0.11932566098398749, "-3": 0.053877104847256864, "-4": 0.019373775994659125, "-5": 0.005759444288263474, "-6": 0.001455365275509264, "-7": 0.000319292294420736, "-8": 6.183271297960465e-05, "-9": 1.0710404697301086e-05, "0": 0.2500242745598874, "1": 0.18287313002442654, "10": 9.49804514406793e-07, "11": 1.2819758208032526e-07, "12": 1.5903679942613334e-08, "13": 1.8240527258354615e-09, "14": 1.927094553969629e-10, "15": 1.672255534757612e-11, "2": 0.10649622387934418, "3": 0.04542603075488278, "4": 0.015431743440166325, "5": 0.004333925904797037, "6": 0.0010346014652525101, "7": 0.00021443205040234907, "8": 3.923012959442871e-05, "9": 6.419593105574552e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.32 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.92 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
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
| Over 2.5 | 53.4% | 60.0% | 1.66 | -11.3% |
| Under 2.5 | 46.6% | 40.0% | 2.42 | +12.7% |

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
| Market best home last update utc | 2026-10-23T14:35:15Z |
| Market best draw last update utc | 2026-10-23T14:35:15Z |
| Market best away last update utc | 2026-10-23T14:35:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-23T14:35:16.325053+00:00 |
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
| Goal margin distribution | {"-1": 0.13988827861700068, "-10": 2.9018546381255496e-08, "-11": 2.694327554822326e-09, "-12": 2.297916449228105e-10, "-13": 1.812014079066274e-11, "-14": 1.3282512152278383e-12, "-15": 9.049204707352118e-14, "-16": 5.253688739817633e-15, "-2": 0.059800160673801755, "-3": 0.018093920644632906, "-4": 0.004310170012754565, "-5": 0.0008430781588100634, "-6": 0.0001395765581452145, "-7": 2.0005457359593376e-05, "-8": 2.52603554020011e-06, "-9": 2.8488431132517353e-07, "0": 0.23929631313993385, "1": 0.23284189053769863, "10": 5.934816396633874e-06, "11": 9.424891070283147e-07, "12": 1.374847389507561e-07, "13": 1.854283525276826e-08, "14": 2.3248187869360862e-09, "15": 2.7090287241772887e-10, "16": 2.6900592691128402e-11, "2": 0.16698577802685519, "3": 0.08641798334888758, "4": 0.035209524478544016, "5": 0.011779528565977117, "6": 0.0033355454954274786, "7": 0.0008177059935671999, "8": 0.0001765966519536089, "9": 3.4064800889016975e-05} |
| Raw goal margin distribution | {"-1": 0.1340942176459102, "-10": 2.7816621325863632e-08, "-11": 2.5827306556177025e-09, "-12": 2.2027385819691013e-10, "-13": 1.7369619005822615e-11, "-14": 1.273236108872674e-12, "-15": 8.674393863065232e-14, "-16": 5.0360851408415034e-15, "-2": 0.05732328569577977, "-3": 0.0173444848773367, "-4": 0.004131646207210855, "-5": 0.0008081585336360742, "-6": 0.00013379540838753888, "-7": 1.9176847265581188e-05, "-8": 2.4214091620663657e-06, "-9": 2.730846302808135e-07, "0": 0.24625405061841535, "1": 0.23383059419000804, "10": 5.960017079524685e-06, "11": 9.464911464389584e-07, "12": 1.380685327999793e-07, "13": 1.8621572669374208e-08, "14": 2.3346905364751963e-09, "15": 2.720531923140413e-10, "16": 2.7014819191272284e-11, "2": 0.167694840507999, "3": 0.08678493525588743, "4": 0.035359032736562455, "5": 0.0118295473271578, "6": 0.0033497090379333294, "7": 0.0008211781733390105, "8": 0.00017734652455758467, "9": 3.420944837051777e-05} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:34:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:35:15Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.82 |
| Reference draw odds | 4.05 |
| Reference away odds | 4.05 |
| Market reference 1x2 last update utc | 2026-10-23T14:35:24Z |
| Market reference home last update utc | 2026-10-23T14:35:24Z |
| Market reference draw last update utc | 2026-10-23T14:35:24Z |
| Market reference away last update utc | 2026-10-23T14:35:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:35:24Z |
| Market best over 2 5 last update utc | 2026-10-23T14:34:52Z |
| Market best under 2 5 last update utc | 2026-10-23T14:34:52Z |
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
