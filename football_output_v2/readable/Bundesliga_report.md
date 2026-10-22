# Bundesliga — football model report

Fixtures in this report: **17**.

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
| Training sha256 | c1118bb9c22ba061fb20c7769f15b8dca19b9fd25f8153d16c5ac94845c4e21a |
| Training as of utc | 2026-10-22T15:06:06.989068+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 16, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T15:06:06.989068+00:00', 'observations': 123, 'observations_sha256': 'ad7a32598192f59b178f12237714c41c11d76652ee793fdc9d48cd94db15736f', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 57, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '1ea0fe3d45c76e04acb596542465c5afb456570bc7739c2b3d0637a41cf8902d', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 4828.985 |
| Base scoring parameter | 0.233 |
| Home-advantage parameter | 0.236 |
| Dixon-Coles low-score adjustment | -0.111 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 7.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261022T150606989068Z_c196f59bcdfd9a78aae3a36f57849912a290d0f5f8b0f4d1414c99e7b609a602.json |
| Over 1 5 in window quote fixtures | 6 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
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

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **63.9%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.46 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 68.5%; Under 3.5 goals: 53.8%; Double Chance 1X: 83.0%; Double Chance X2: 36.1%; Double Chance 12 (either team wins): 80.9%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 63.9% | 1.56 |
| Draw | 19.1% | 5.24 |
| Borussia Monchengladbach win | 17.0% | 5.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.17 |
| Borussia Monchengladbach expected goals | 1.29 |
| Expected total goals | 3.46 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.5% |
| Under 2.5 | 31.5% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.81% |
| 2 | 2-0 | 8.40% |
| 3 | 1-1 | 8.36% |
| 4 | 3-1 | 7.81% |
| 5 | 1-0 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 63.9% | 71.4% | 1.38 | -11.8% |
| Draw | 19.1% | 15.8% | 5.81 | +11.0% |
| Borussia Monchengladbach win | 17.0% | 12.8% | 7.12 | +20.9% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.30 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.91 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.17 |
| Fair Over 3.5 odds | 2.17 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.63 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.09717315176867526, "-10": 1.1248896961990459e-07, "-11": 1.2899873918957885e-08, "-12": 1.3602423023708615e-09, "-13": 1.3272346480222888e-10, "-14": 1.2048637673670108e-11, "-15": 1.0218980966650194e-12, "-16": 8.054014932355638e-14, "-17": 5.2400951314971114e-15, "-2": 0.04880210671969204, "-3": 0.017366669822211075, "-4": 0.004954717226976834, "-5": 0.0011733356886785614, "-6": 0.0002367933433527214, "-7": 4.156189125534878e-05, "-8": 6.447086759452737e-06, "-9": 8.953104382201266e-07, "0": 0.1909840882801116, "1": 0.23827373035075122, "10": 2.90003849301764e-05, "11": 5.598599392746921e-06, "12": 9.938258925166823e-07, "13": 1.632457353270999e-07, "14": 2.494779586232089e-08, "15": 3.562065744417585e-09, "16": 4.726143178972019e-10, "17": 5.176470208092533e-11, "2": 0.1950435383125269, "3": 0.11684486940686876, "4": 0.05611927827342686, "5": 0.02237255515160063, "6": 0.007600862910974203, "7": 0.00224589172650507, "8": 0.0005864853005168947, "9": 0.0001371094435214067} |
| Raw goal margin distribution | {"-1": 0.12108695520118418, "-10": 1.4017191556591666e-07, "-11": 1.6074465291032227e-08, "-12": 1.694990804888468e-09, "-13": 1.6538601397751625e-10, "-14": 1.5013744266523773e-11, "-15": 1.2733818631880677e-12, "-16": 1.003606580164659e-13, "-17": 6.529655083618207e-15, "-2": 0.060812049445078106, "-3": 0.02164051625866594, "-4": 0.006174047172265126, "-5": 0.0014620874530157106, "-6": 0.00029506694428051367, "-7": 5.1790054895957555e-05, "-8": 8.0336810261994e-06, "-9": 1.1156416453588802e-06, "0": 0.22361460445307493, "1": 0.2105399152820045, "10": 2.5624891914676854e-05, "11": 4.946951726955671e-06, "12": 8.781497603932783e-07, "13": 1.4424478617647905e-07, "14": 2.2044003002738993e-08, "15": 3.147459935909146e-09, "16": 4.1760448499573977e-10, "17": 4.573956169936574e-11, "2": 0.17234149132668894, "3": 0.10324473818345734, "4": 0.04958728801526597, "5": 0.019768506831727282, "6": 0.00671616225167137, "7": 0.001984481684719809, "8": 0.000518221481248483, "9": 0.00012115062193749187} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 65.1% |
| P home draw | 83.0% |
| P draw away | 36.1% |
| P home away | 80.9% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.05, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:05:21Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:07Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.88, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:07Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.16, "price": 5.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.27, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.38 |
| Reference draw odds | 5.81 |
| Reference away odds | 7.12 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.72 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | -7.4% |
| Draw probability edge | +3.3% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.1488 |
| Raw ev home | -0.2205 |
| Raw edge prob draw | 0.0653 |
| Raw ev draw | 0.2992 |
| Raw edge prob away | 0.0836 |
| Raw ev away | 0.5061 |
| Market p home draw | 87.8% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:06:07Z |
| Market reference home draw last update utc | 2026-10-22T15:06:07Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 29.7% |
| Market draw away odds | 3.28 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:06:07Z |
| Market reference draw away last update utc | 2026-10-22T15:06:07Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.5% |
| Market home away odds | 1.18 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:06:07Z |
| Market reference home away last update utc | 2026-10-22T15:06:07Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.28 |
| Market reference dc home draw odds | 1.11 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 92.4% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T15:05:21Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 9.00 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:48Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 43.7% |
| Market under 3 5 odds | 2.18 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 3 5 odds | 2.18 |
| Market reference under 3 5 opposite odds | 1.72 |
| Market reference under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 65.1% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:06:07Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.84 |
| Market reference btts yes last update utc | 2026-10-22T15:06:11Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.2%**. Expected goals are 1.76 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 50.3%; Under 3.5 goals: 72.1%; Double Chance 1X: 76.5%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.2% | 1.95 |
| Draw | 25.3% | 3.95 |
| FC Schalke 04 win | 23.5% | 4.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.76 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.3% |
| Under 2.5 | 49.7% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.11% |
| 2 | 1-0 | 9.86% |
| 3 | 2-0 | 9.66% |
| 4 | 2-1 | 9.00% |
| 5 | 0-0 | 7.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.2% | 46.7% | 2.09 | +6.9% |
| Draw | 25.3% | 24.8% | 3.86 | -2.2% |
| FC Schalke 04 win | 23.5% | 28.5% | 3.38 | -20.6% |
| Over 2.5 | 50.3% | 59.5% | 1.64 | -17.5% |
| Under 2.5 | 49.7% | 40.5% | 2.46 | +22.3% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Koln |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7566 |
| Dc lambda away | 0.9312 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.70 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.46 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.15085011200356732, "-10": 1.3502050802934253e-08, "-11": 1.129122416372415e-09, "-12": 8.671563805322834e-11, "-13": 6.156357840043397e-12, "-14": 4.062630974561866e-13, "-15": 2.493960968660058e-14, "-16": 1.3168185336920592e-15, "-2": 0.0624265712507764, "-3": 0.01720100095465774, "-4": 0.003715551692760269, "-5": 0.0006574238351904856, "-6": 9.830648569247681e-05, "-7": 1.2713871389844692e-05, "-8": 1.447537025901318e-06, "-9": 1.4713132896536943e-07, "0": 0.25342732539680585, "1": 0.2167056452393008, "10": 5.5940097457201426e-06, "11": 8.824678699046276e-07, "12": 1.2784674873670628e-07, "13": 1.7121843019565745e-08, "14": 2.1314169858343363e-09, "15": 2.4682269557727616e-10, "16": 2.458418189910986e-11, "2": 0.1612938582847116, "3": 0.08383714107711839, "4": 0.03416177590496129, "5": 0.011402418289949846, "6": 0.0032163854271917303, "7": 0.0007846900038722748, "8": 0.00016853277779804975, "9": 3.2314262391881276e-05} |
| Raw goal margin distribution | {"-1": 0.11900896685164729, "-10": 1.065206445718556e-08, "-11": 8.9078947596896e-10, "-12": 6.841187160903167e-11, "-13": 4.856885927239335e-12, "-14": 3.205098813388187e-13, "-15": 1.9675405891746913e-14, "-16": 1.0388670657538996e-15, "-2": 0.049249693288063036, "-3": 0.013570247481020148, "-4": 0.002931280344218983, "-5": 0.0005186561041984322, "-6": 7.755614590992974e-05, "-7": 1.003025240547619e-05, "-8": 1.1419937555495367e-06, "-9": 1.160751372280346e-07, "0": 0.2587370214859046, "1": 0.23546410305856694, "10": 6.078237998010382e-06, "11": 9.588559875108114e-07, "12": 1.3891340941764778e-07, "13": 1.8603942711597088e-08, "14": 2.3159165431942286e-09, "15": 2.6818814325036813e-10, "16": 2.6712236009866296e-11, "2": 0.17525576515520108, "3": 0.09109424539872647, "4": 0.0371188849901298, "5": 0.012389433567255888, "6": 0.0034948019414447543, "7": 0.0008526142811682517, "8": 0.000183121299476834, "9": 3.5111447150817475e-05} |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 76.5% |
| P draw away | 48.8% |
| P home away | 74.7% |
| Raw p home draw | 81.5% |
| Raw p draw away | 44.4% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.68, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.06, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.54, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:02Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.09 |
| Reference draw odds | 3.86 |
| Reference away odds | 3.38 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.32 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:48Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:48Z |
| Home probability edge | +4.4% |
| Draw probability edge | +0.5% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | 0.0886 |
| Raw ev home | 0.1618 |
| Raw edge prob draw | 0.0106 |
| Raw ev draw | -0.0013 |
| Raw edge prob away | -0.0992 |
| Raw ev away | -0.3735 |
| Market p home draw | 71.5% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:05:49Z |
| Market reference home draw last update utc | 2026-10-22T15:05:49Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.6% |
| Market draw away odds | 1.80 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:05:49Z |
| Market reference draw away last update utc | 2026-10-22T15:05:49Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.8% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:05:49Z |
| Market reference home away last update utc | 2026-10-22T15:05:49Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.80 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 82.7% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T15:01:02Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:48Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.3% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.58 |
| Market reference under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 62.2% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:05:49Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.62 |
| Market reference btts yes last update utc | 2026-10-22T15:06:11Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **46.3%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 46.9%; Under 3.5 goals: 75.5%; Double Chance 1X: 72.6%; Double Chance X2: 53.7%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 46.3% | 2.16 |
| Draw | 26.3% | 3.80 |
| Union Berlin win | 27.4% | 3.65 |

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
| Over 3.5 | 24.5% |
| Under 3.5 | 75.5% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.56% |
| 2 | 1-0 | 11.23% |
| 3 | 2-1 | 10.01% |
| 4 | 2-0 | 8.65% |
| 5 | 0-0 | 8.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 46.3% | 52.9% | 1.85 | -14.4% |
| Draw | 26.3% | 22.9% | 4.15 | +9.2% |
| Union Berlin win | 27.4% | 24.1% | 3.95 | +8.3% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
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
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.72 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.13 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.86 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.1574620045811318, "-10": 9.953197504727993e-08, "-11": 1.0343787941418407e-08, "-12": 9.869330629263783e-10, "-13": 8.661648680888835e-11, "-14": 6.4405142297647e-12, "-2": 0.07991148186462324, "-3": 0.027492124784562116, "-4": 0.00740116141209875, "-5": 0.0016303966951591942, "-6": 0.00030333567354426844, "-7": 4.878994836182045e-05, "-8": 6.906656900568134e-06, "-9": 8.726478632493225e-07, "0": 0.263195315475361, "1": 0.24189756102554988, "10": 5.813343907073858e-07, "11": 7.016565932891418e-08, "12": 7.77524904682869e-09, "13": 7.925173582465785e-10, "14": 6.844005831761288e-11, "2": 0.14100019457098714, "3": 0.056337872481996204, "4": 0.017614633851348097, "5": 0.004506596124071379, "6": 0.0009737790995047587, "7": 0.00018190679724310892, "8": 2.990667006459969e-05, "9": 4.388547619179725e-06} |
| Raw goal margin distribution | {"-1": 0.17631060366081602, "-10": 1.1144620348775865e-07, "-11": 1.1581965445837335e-08, "-12": 1.105071439679986e-09, "-13": 9.69846987333739e-11, "-14": 7.211460026541266e-12, "-2": 0.08947708778674053, "-3": 0.030783001458533753, "-4": 0.008287099099427006, "-5": 0.0018255592915559892, "-6": 0.00033964571870348645, "-7": 5.4630228232743946e-05, "-8": 7.733401150687646e-06, "-9": 9.771060133654967e-07, "0": 0.296989671029101, "1": 0.20705553033752838, "10": 4.976011335585483e-07, "11": 6.005925707657783e-08, "12": 6.655330909795464e-09, "13": 6.783660869408688e-10, "14": 5.858220525748888e-11, "2": 0.12069104765180658, "3": 0.04822317354252148, "4": 0.015077487091352003, "5": 0.0038574826737839286, "6": 0.0008335195568931857, "7": 0.00015570561445716645, "8": 2.5599023837206535e-05, "9": 3.7564374392546233e-06} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 52.1% |
| P home draw | 72.6% |
| P draw away | 53.7% |
| P home away | 73.7% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.5, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.85, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.58, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.9, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:01:58Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.91, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.91, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 4.15 |
| Reference away odds | 3.95 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | -6.7% |
| Draw probability edge | +3.4% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -18.1% |
| Under 2.5 probability edge | +18.1% |
| Raw edge prob home | -0.1332 |
| Raw ev home | -0.2675 |
| Raw edge prob draw | 0.0676 |
| Raw ev draw | 0.2325 |
| Raw edge prob away | 0.0657 |
| Raw ev away | 0.2130 |
| Market p home draw | 75.6% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:06:07Z |
| Market reference home draw last update utc | 2026-10-22T15:06:07Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.7% |
| Market draw away odds | 2.03 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:06:07Z |
| Market reference draw away last update utc | 2026-10-22T15:06:07Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:06:07Z |
| Market reference home away last update utc | 2026-10-22T15:06:07Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.03 |
| Market reference dc home draw odds | 1.28 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T15:01:58Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:48Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.2% |
| Market under 3 5 odds | 1.70 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market reference under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 64.2% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:06:07Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.72 |
| Market reference btts yes last update utc | 2026-10-22T15:06:11Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **64.7%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 71.0%; Under 3.5 goals: 50.4%; Double Chance 1X: 83.7%; Double Chance X2: 35.3%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 64.7% | 1.55 |
| Draw | 19.0% | 5.27 |
| Eintracht Frankfurt win | 16.3% | 6.12 |

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
| Over 2.5 | 71.0% |
| Under 2.5 | 29.0% |
| Over 3.5 | 49.6% |
| Under 3.5 | 50.4% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.63% |
| 2 | 1-1 | 8.13% |
| 3 | 2-0 | 7.88% |
| 4 | 3-1 | 7.77% |
| 5 | 3-0 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 64.7% | 66.4% | 1.48 | -4.3% |
| Draw | 19.0% | 17.9% | 5.21 | -1.1% |
| Eintracht Frankfurt win | 16.3% | 15.7% | 5.89 | -3.7% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4205 |
| Dc lambda away | 1.2230 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.45 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.96 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.44 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.28 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.09704452941729944, "-10": 6.777428561500591e-08, "-11": 7.372679484883945e-09, "-12": 7.375954111362011e-10, "-13": 6.829259416247455e-11, "-14": 5.883678303821002e-12, "-15": 4.739015029775304e-13, "-16": 3.5813981453595636e-14, "-17": 2.5243916181153215e-15, "-18": 1.4728941901657252e-16, "-2": 0.045831800171450464, "-3": 0.015348861121187976, "-4": 0.0041328172693950675, "-5": 0.0009252869420632493, "-6": 0.00017674288382154448, "-7": 2.938456992002229e-05, "-8": 4.3199050071698614e-06, "-9": 5.687773566734629e-07, "0": 0.18976735482417367, "1": 0.2137355754060503, "10": 6.67576687843355e-05, "11": 1.4373477768863193e-05, "12": 2.8461317969340163e-06, "13": 5.215677199098875e-07, "14": 8.893778466926103e-08, "15": 1.4178352449276657e-08, "16": 2.1207553919758292e-09, "17": 2.9586595797447407e-10, "18": 3.4167256795406456e-11, "2": 0.19169058417619456, "3": 0.12706042841562643, "4": 0.06771434095517419, "5": 0.030006212411867197, "6": 0.011344281023647823, "7": 0.003732971479057671, "8": 0.00108620006318648, "9": 0.0002830598152750368} |
| Raw goal margin distribution | {"-1": 0.10080840866472598, "-10": 7.040291629276987e-08, "-11": 7.65862940372744e-09, "-12": 7.662031036835535e-10, "-13": 7.094132747556782e-11, "-14": 6.1118772017831785e-12, "-15": 4.922818078034859e-13, "-16": 3.720302937180707e-14, "-17": 2.6223003336385274e-15, "-18": 1.5300205002143949e-16, "-2": 0.047609389929196985, "-3": 0.01594416783443144, "-4": 0.004293108892705359, "-5": 0.0009611742645126259, "-6": 0.00018359786963620744, "-7": 3.052425263661249e-05, "-8": 4.487452842220128e-06, "-9": 5.908374284986732e-07, "0": 0.20091772948304235, "1": 0.20795493802079165, "10": 6.495215804895927e-05, "11": 1.3984736386952269e-05, "12": 2.769156048570768e-06, "13": 5.074615335395214e-07, "14": 8.653239622587951e-08, "15": 1.3794888376559906e-08, "16": 2.0633979872454547e-09, "17": 2.8786404339173125e-10, "18": 3.324317795823564e-11, "2": 0.18650616995228336, "3": 0.12362398475719012, "4": 0.0658829563103859, "5": 0.029194672110592946, "6": 0.01103746651759474, "7": 0.003632010492806553, "8": 0.0010568229757212907, "9": 0.00027540425233314134} |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.2% |
| P home draw | 83.7% |
| P draw away | 35.3% |
| P home away | 81.0% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.1% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.48 |
| Reference draw odds | 5.21 |
| Reference away odds | 5.89 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.26 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | -1.7% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | -0.0350 |
| Raw ev home | -0.0687 |
| Raw edge prob draw | 0.0223 |
| Raw ev draw | 0.0468 |
| Raw edge prob away | 0.0127 |
| Raw ev away | 0.0003 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **52.6%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.9%; Double Chance 1X: 76.9%; Double Chance X2: 47.4%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 52.6% | 1.90 |
| Draw | 24.3% | 4.11 |
| Werder Bremen win | 23.1% | 4.33 |

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
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.51% |
| 2 | 2-1 | 10.25% |
| 3 | 1-0 | 8.89% |
| 4 | 2-0 | 8.83% |
| 5 | 0-0 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 52.6% | 55.7% | 1.76 | -7.5% |
| Draw | 24.3% | 22.5% | 4.22 | +2.7% |
| Werder Bremen win | 23.1% | 21.8% | 4.34 | +0.2% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
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
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.84 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.96 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.88 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.13518408800444326, "-10": 7.731101041188876e-08, "-11": 8.037617342729145e-09, "-12": 7.677234223807914e-10, "-13": 6.780939658215535e-11, "-14": 5.567903477526951e-12, "-15": 4.245530647758067e-13, "-16": 2.736651319144046e-14, "-2": 0.06609954887608767, "-3": 0.02218383834114848, "-4": 0.005882589256719049, "-5": 0.0012835692813421627, "-6": 0.0002373602669648416, "-7": 3.803322802731731e-05, "-8": 5.371967499937381e-06, "-9": 6.779986935535671e-07, "0": 0.24346744110261462, "1": 0.2321049228315579, "10": 4.678546654242263e-06, "11": 7.248699014214197e-07, "12": 1.0318121956074582e-07, "13": 1.3581535440176701e-08, "14": 1.6619341611359522e-09, "15": 1.8885010152605484e-10, "16": 1.8141276160444687e-11, "2": 0.16442320430725826, "3": 0.08223646418645222, "4": 0.03249820608151766, "5": 0.010567525469134111, "6": 0.0029122264062551094, "7": 0.0006954139947493472, "8": 0.00014637831415001377, "9": 2.753184696785653e-05} |
| Raw goal margin distribution | {"-1": 0.1424763079622922, "-10": 8.148138949576814e-08, "-11": 8.471189625276745e-09, "-12": 8.091366400563012e-10, "-13": 7.146723118669723e-11, "-14": 5.8682522645888114e-12, "-15": 4.474546826941989e-13, "-16": 2.884274191493341e-14, "-2": 0.06966514935935737, "-3": 0.023380498621814794, "-4": 0.006199913103148848, "-5": 0.0013528087137994608, "-6": 0.0002501641649791144, "-7": 4.008485014184536e-05, "-8": 5.661746934737958e-06, "-9": 7.145719003378174e-07, "0": 0.2620350591442561, "1": 0.21840524690982902, "10": 4.402401830746546e-06, "11": 6.820854459529946e-07, "12": 9.709108906309669e-08, "13": 1.2779903868644184e-08, "14": 1.5638407681434394e-09, "15": 1.7770348232845124e-10, "16": 1.7070512123332733e-11, "2": 0.15471834934105683, "3": 0.07738256925583563, "4": 0.030580043873138098, "5": 0.009943791717796075, "6": 0.00274033622189504, "7": 0.0006543681339236605, "8": 0.00013773853416878732, "9": 2.5906817320122642e-05} |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 24.3% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.7% |
| P home draw | 76.9% |
| P draw away | 47.4% |
| P home away | 75.7% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.0, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.45, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.17, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.99, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:16Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 9.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.83, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.76 |
| Reference draw odds | 4.22 |
| Reference away odds | 4.34 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | -3.1% |
| Draw probability edge | +1.9% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0620 |
| Raw ev home | -0.1295 |
| Raw edge prob draw | 0.0371 |
| Raw ev draw | 0.1058 |
| Raw edge prob away | 0.0249 |
| Raw ev away | 0.0562 |
| Market p home draw | 77.5% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:05:49Z |
| Market reference home draw last update utc | 2026-10-22T15:05:49Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.0% |
| Market draw away odds | 2.15 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:05:49Z |
| Market reference draw away last update utc | 2026-10-22T15:05:49Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.5% |
| Market home away odds | 1.25 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:05:49Z |
| Market reference home away last update utc | 2026-10-22T15:05:49Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.15 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T15:02:16Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:48Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.1% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.39 |
| Market reference under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 62.3% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:05:49Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-22T15:05:49Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **66.3%**. Expected goals are 2.69 for RB Leipzig and 1.32 for Elversberg (4.01 combined). The most likely exact score is 2-1 at 8.7%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 76.3%; Under 3.5 goals: 43.1%; Double Chance 1X: 84.6%; Double Chance X2: 33.7%; Double Chance 12 (either team wins): 81.7%; Under 4.5 goals: 62.7%; BTTS Yes (both teams score): 69.0%; BTTS No (at least one team does not score): 31.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 66.3% | 1.51 |
| Draw | 18.3% | 5.46 |
| Elversberg win | 15.4% | 6.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.69 |
| Elversberg expected goals | 1.32 |
| Expected total goals | 4.01 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 91.6% |
| Under 1.5 | 8.4% |
| Over 2.5 | 76.3% |
| Under 2.5 | 23.7% |
| Over 3.5 | 56.9% |
| Under 3.5 | 43.1% |
| Over 4.5 | 37.3% |
| Under 4.5 | 62.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.74% |
| 2 | 3-1 | 7.83% |
| 3 | 1-1 | 7.19% |
| 4 | 2-0 | 6.62% |
| 5 | 3-0 | 5.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 66.3% | 66.8% | 1.47 | -2.6% |
| Draw | 18.3% | 18.4% | 5.05 | -7.4% |
| Elversberg win | 15.4% | 14.8% | 6.23 | -3.9% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6859 |
| Dc lambda away | 1.3214 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 69.0% |
| P btts no | 31.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.31 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.96 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.22 |
| Fair Over 3.5 odds | 1.76 |
| Fair Under 3.5 odds | 2.32 |
| Fair Over 4.5 odds | 2.68 |
| Fair Under 4.5 odds | 1.59 |
| Goal margin distribution | {"-1": 0.08986103166903463, "-10": 1.072856744013961e-07, "-11": 1.2557701478998918e-08, "-12": 1.3526221665778506e-09, "-13": 1.3490167656459666e-10, "-14": 1.2524207957362316e-11, "-15": 1.087424365265035e-12, "-16": 8.866010433657883e-14, "-17": 6.807258898072588e-15, "-18": 4.87892826050922e-16, "-19": 2.85909697700553e-17, "-2": 0.043442194457012695, "-3": 0.01524710343662123, "-4": 0.00434239485135038, "-5": 0.0010342801501863372, "-6": 0.00021097266860362426, "-7": 3.7553535098852405e-05, "-8": 5.921765232826264e-06, "-9": 8.374316347095612e-07, "0": 0.18330538961882534, "1": 0.19956730561200414, "10": 0.0001358386337574817, "11": 3.231854959978389e-05, "12": 7.075845566357368e-06, "13": 1.4344299039824629e-06, "14": 2.706901118945307e-07, "15": 4.777286850893289e-08, "16": 7.917182125233804e-09, "17": 1.2355911919754767e-09, "18": 1.8000605157586252e-10, "19": 2.1441328854022904e-11, "2": 0.1887609787058556, "3": 0.13466289593605946, "4": 0.07795609070726765, "5": 0.037741492375490564, "6": 0.015648301802093735, "7": 0.00566176684398149, "8": 0.0018147319237732831, "9": 0.0005216398892372013} |
| Raw goal margin distribution | {"-1": 0.09366153589203804, "-10": 1.1182312129085547e-07, "-11": 1.3088805970186247e-08, "-12": 1.4098287906364361e-09, "-13": 1.4060709060170985e-10, "-14": 1.3053895902711491e-11, "-15": 1.1334149444474313e-12, "-16": 9.240981758474312e-14, "-17": 7.09515917819053e-15, "-18": 5.085273403819938e-16, "-19": 2.980017134867796e-17, "-2": 0.04527950080019487, "-3": 0.015891951152290366, "-4": 0.004526048317863966, "-5": 0.0010780230942138344, "-6": 0.00021989536293590698, "-7": 3.914179161094714e-05, "-8": 6.17221521494845e-06, "-9": 8.728492390379014e-07, "0": 0.18269266981947996, "1": 0.1977876086453656, "10": 0.00013462725495117298, "11": 3.203033994283379e-05, "12": 7.012744745046824e-06, "13": 1.4216379762609126e-06, "14": 2.682761575167812e-07, "15": 4.734684066377939e-08, "16": 7.84657845110294e-09, "17": 1.2245724637844001e-09, "18": 1.7840079753395552e-10, "19": 2.125011983907336e-11, "2": 0.18707765016568045, "3": 0.13346200209885892, "4": 0.07726089558130617, "5": 0.03740492211769662, "6": 0.015508753717477234, "7": 0.005611276463068901, "8": 0.0017985485469917144, "9": 0.0005169880204067525} |
| Unadjusted home-win probability | 65.7% |
| Unadjusted draw probability | 18.3% |
| Unadjusted away-win probability | 16.1% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 43.2% |
| Raw p btts yes | 69.0% |
| P home draw | 84.6% |
| P draw away | 33.7% |
| P home away | 81.7% |
| Raw p home draw | 83.9% |
| Raw p draw away | 34.3% |
| Raw p home away | 81.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.05, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:07Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.03, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:07Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.19, "price": 5.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 5.05 |
| Reference away odds | 6.23 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.66 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | -0.6% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | -0.0118 |
| Raw ev home | -0.0348 |
| Raw edge prob draw | -0.0012 |
| Raw ev draw | -0.0774 |
| Raw edge prob away | 0.0130 |
| Raw ev away | 0.0012 |
| Market p home draw | 84.5% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:06:07Z |
| Market reference home draw last update utc | 2026-10-22T15:06:07Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.5% |
| Market draw away odds | 2.82 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:06:07Z |
| Market reference draw away last update utc | 2026-10-22T15:06:07Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.0% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:06:07Z |
| Market reference home away last update utc | 2026-10-22T15:06:07Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.82 |
| Market reference dc home draw odds | 1.15 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 92.2% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T15:02:33Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 8.50 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:48Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 44.3% |
| Market under 3 5 odds | 2.16 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 3 5 odds | 2.16 |
| Market reference under 3 5 opposite odds | 1.74 |
| Market reference under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 67.5% |
| Market btts yes odds | 1.42 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:06:07Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 3.00 |
| Market reference btts yes last update utc | 2026-10-22T15:06:11Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **37.9%**. Expected goals are 1.01 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 33.1%; Under 3.5 goals: 85.9%; Double Chance 1X: 67.7%; Double Chance X2: 62.1%; Double Chance 12 (either team wins): 70.2%; Under 4.5 goals: 94.7%; BTTS Yes (both teams score): 40.0%; BTTS No (at least one team does not score): 60.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 37.9% | 2.64 |
| Draw | 29.8% | 3.36 |
| Hamburger SV win | 32.3% | 3.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.01 |
| Hamburger SV expected goals | 0.96 |
| Expected total goals | 1.98 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 60.7% |
| Under 1.5 | 39.3% |
| Over 2.5 | 33.1% |
| Under 2.5 | 66.9% |
| Over 3.5 | 14.1% |
| Under 3.5 | 85.9% |
| Over 4.5 | 5.3% |
| Under 4.5 | 94.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.84% |
| 2 | 0-0 | 13.41% |
| 3 | 1-1 | 13.14% |
| 4 | 0-1 | 12.09% |
| 5 | 2-0 | 7.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 37.9% | 41.5% | 2.35 | -10.9% |
| Draw | 29.8% | 25.5% | 3.77 | +12.2% |
| Hamburger SV win | 32.3% | 33.0% | 2.93 | -5.3% |
| Over 2.5 | 33.1% | 61.2% | 1.64 | -45.7% |
| Under 2.5 | 66.9% | 38.8% | 2.47 | +65.2% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
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
| Dc lambda home | 1.0149 |
| Dc lambda away | 0.9632 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 40.0% |
| P btts no | 60.0% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.46 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.54 |
| Fair Over 2.5 odds | 3.02 |
| Fair Under 2.5 odds | 1.49 |
| Fair Over 3.5 odds | 7.09 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.76 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.19924717490059776, "-10": 2.9282698281664195e-08, "-11": 2.5453016659326724e-09, "-12": 2.0255350742880203e-10, "-13": 1.395856237198213e-11, "-2": 0.08979019577084352, "-3": 0.026749166334723105, "-4": 0.006150118762675971, "-5": 0.0011482264066288174, "-6": 0.00018021238550554387, "-7": 2.437828765260682e-05, "-8": 2.896356937071967e-06, "-9": 3.0668490498512774e-07, "0": 0.29766994666958374, "1": 0.2275359633096281, "10": 5.331794376945203e-08, "11": 4.883176054669685e-09, "12": 4.094526718240312e-10, "13": 2.9730721860823405e-11, "2": 0.10761793398410091, "3": 0.03378055683671656, "4": 0.008183533718403685, "5": 0.0016098511613129075, "6": 0.00026622182193732536, "7": 3.794574063509597e-05, "8": 4.7502092328705825e-06, "9": 5.299731642421294e-07} |
| Raw goal margin distribution | {"-1": 0.19485316409895465, "-10": 2.8636925047413423e-08, "-11": 2.4891699640948524e-09, "-12": 1.9808658186262085e-10, "-13": 1.3650733295517193e-11, "-2": 0.08781004679108725, "-3": 0.026159265243937958, "-4": 0.006014489796854659, "-5": 0.0011229044956106266, "-6": 0.0001762381501423761, "-7": 2.3840671702345254e-05, "-8": 2.8324833906929167e-06, "-9": 2.9992156299105513e-07, "0": 0.3404820246524458, "1": 0.2061157833453604, "10": 4.8298605576692414e-08, "11": 4.423475054586938e-09, "12": 3.709068973901844e-10, "13": 2.6931878972590288e-11, "2": 0.09748680798629443, "3": 0.03060046347384453, "4": 0.007413137854637202, "5": 0.0014583001665188086, "6": 0.00024115976469869533, "7": 3.4373537887633466e-05, "8": 4.303025696887951e-06, "9": 4.800816201135602e-07} |
| Unadjusted home-win probability | 34.3% |
| Unadjusted draw probability | 34.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 86.1% |
| Raw p btts yes | 40.9% |
| P home draw | 67.7% |
| P draw away | 62.1% |
| P home away | 70.2% |
| Raw p home draw | 68.4% |
| Raw p draw away | 65.7% |
| Raw p home away | 66.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.5, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.88, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.51, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.83, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 3.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:33Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.98, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.98, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.35 |
| Reference draw odds | 3.77 |
| Reference away odds | 2.93 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.41 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:48Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:48Z |
| Home probability edge | -3.6% |
| Draw probability edge | +4.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -28.1% |
| Under 2.5 probability edge | +28.1% |
| Raw edge prob home | -0.0714 |
| Raw ev home | -0.1931 |
| Raw edge prob draw | 0.0856 |
| Raw ev draw | 0.2836 |
| Raw edge prob away | -0.0143 |
| Raw ev away | -0.0736 |
| Market p home draw | 67.0% |
| Market home draw odds | 1.44 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:05:49Z |
| Market reference home draw last update utc | 2026-10-22T15:05:49Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.8% |
| Market draw away odds | 1.64 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:05:49Z |
| Market reference draw away last update utc | 2026-10-22T15:05:49Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:05:49Z |
| Market reference home away last update utc | 2026-10-22T15:05:49Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.64 |
| Market reference dc home draw odds | 1.44 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T15:02:33Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-22T15:05:48Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.6% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market reference under 3 5 last update utc | 2026-10-22T15:06:12Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 63.5% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:05:49Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.68 |
| Market reference btts yes last update utc | 2026-10-22T15:06:11Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **67.2%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 72.2%; Under 3.5 goals: 49.2%; Double Chance 1X: 32.8%; Double Chance X2: 84.7%; Double Chance 12 (either team wins): 82.5%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 15.3% | 6.54 |
| Draw | 17.5% | 5.71 |
| Bayern Munich win | 67.2% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.24 |
| Bayern Munich expected goals | 2.45 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 72.2% |
| Under 2.5 | 27.8% |
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.91% |
| 2 | 1-3 | 8.08% |
| 3 | 0-2 | 8.00% |
| 4 | 1-1 | 7.43% |
| 5 | 0-3 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 15.3% | 13.6% | 6.70 | +2.4% |
| Draw | 17.5% | 15.1% | 6.06 | +6.1% |
| Bayern Munich win | 67.2% | 71.3% | 1.38 | -7.2% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Freiburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2378 |
| Dc lambda away | 2.4470 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.91 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.41 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.60 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.46 |
| Goal margin distribution | {"-1": 0.22026465345291485, "-10": 7.445349401257975e-05, "-11": 1.6197661647754727e-05, "-12": 3.2410318161374237e-06, "-13": 6.002079750069536e-07, "-14": 1.0343327496115545e-07, "-15": 1.6664724886011086e-08, "-16": 2.51917450665173e-09, "-17": 3.550456811370694e-10, "-18": 4.131389658848714e-11, "-2": 0.1984884312856157, "-3": 0.13251583816268342, "-4": 0.07121195606769605, "-5": 0.031842123340435374, "-6": 0.012153011414273572, "-7": 0.004038424921543261, "-8": 0.0011868955522056233, "-9": 0.0003124607894379593, "0": 0.17504769586450886, "1": 0.09039196779714324, "10": 6.9039716982677e-08, "11": 7.598073865641444e-09, "12": 7.690804159478842e-10, "13": 7.204892235166875e-11, "14": 6.280920163441043e-12, "15": 5.119156601468422e-13, "16": 3.9146756936187255e-14, "17": 2.7909948836715365e-15, "18": 1.6428890459193717e-16, "2": 0.04291913508356288, "3": 0.014495086769135258, "4": 0.003940426367135123, "5": 0.0008913116664823056, "6": 0.00017208727050499624, "7": 2.8927714553253518e-05, "8": 4.3008260943961645e-06, "9": 5.727593334146e-07} |
| Raw goal margin distribution | {"-1": 0.20680136828525314, "-10": 6.990265661807953e-05, "-11": 1.5207608389574393e-05, "-12": 3.042929511050827e-06, "-13": 5.635213300970801e-07, "-14": 9.711110000118221e-08, "-15": 1.564612321813632e-08, "-16": 2.3651944456729222e-09, "-17": 3.3334414538105266e-10, "-18": 3.878865814265093e-11, "-2": 0.18635617896556142, "-3": 0.12441604325483953, "-4": 0.0668592519145018, "-5": 0.029895830187377206, "-6": 0.011410180207580715, "-7": 0.0037915833811753164, "-8": 0.0011143486726537958, "-9": 0.00029336217944325477, "0": 0.19914260689606705, "1": 0.10043780568303269, "10": 7.671254258209473e-08, "11": 8.442496441666608e-09, "12": 8.545532446527932e-10, "13": 8.005618020252368e-11, "14": 6.978959018815281e-12, "15": 5.688081236965269e-13, "16": 4.3497386572017395e-14, "17": 3.101176007337673e-15, "18": 1.8254738200095669e-16, "2": 0.04768901324596404, "3": 0.016106018529702993, "4": 0.004378351167869185, "5": 0.0009903688363336975, "6": 0.00019121243022713063, "7": 3.2142636607649305e-05, "8": 4.778804423363049e-06, "9": 6.364137437713464e-07} |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 32.8% |
| P draw away | 84.7% |
| P home away | 82.5% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.70 |
| Reference draw odds | 6.06 |
| Reference away odds | 1.38 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.23 |
| Reference Under 2.5 odds | 4.23 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | +1.7% |
| Draw probability edge | +2.4% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | 0.0340 |
| Raw ev home | 0.1379 |
| Raw edge prob draw | 0.0482 |
| Raw ev draw | 0.2068 |
| Raw edge prob away | -0.0822 |
| Raw ev away | -0.1292 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.7%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 70.5%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.3%; Double Chance X2: 69.8%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 70.0%; BTTS No (at least one team does not score): 30.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.2% | 3.31 |
| Draw | 23.1% | 4.33 |
| Bayer Leverkusen win | 46.7% | 2.14 |

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
| 2 | 1-2 | 8.12% |
| 3 | 2-1 | 7.35% |
| 4 | 2-2 | 6.93% |
| 5 | 1-3 | 5.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.2% | 34.7% | 2.79 | -15.7% |
| Draw | 23.1% | 23.7% | 4.04 | -6.7% |
| Bayer Leverkusen win | 46.7% | 41.6% | 2.34 | +9.3% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
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
| Dc lambda away | 2.1590 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 70.0% |
| P btts no | 30.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.84 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.92 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.18076254149578047, "-10": 1.882633237325017e-05, "-11": 3.6082265194704546e-06, "-12": 6.361818014518554e-07, "-13": 1.038320904257962e-07, "-14": 1.577116148853079e-08, "-15": 2.2379660520148005e-09, "-16": 2.942653127733206e-10, "-17": 3.1388096053714e-11, "-2": 0.1420537211223188, "-3": 0.08275121106693539, "-4": 0.03893310435528157, "-5": 0.015273642940149865, "-6": 0.005121494310606288, "-7": 0.0014965967668900979, "-8": 0.00038705633499723556, "-9": 8.970927259103509e-05, "0": 0.23103375676469456, "1": 0.16039370051409504, "10": 6.467287979111611e-07, "11": 8.61706177086645e-08, "12": 1.0562229201911764e-08, "13": 1.1984360858214227e-09, "14": 1.2654817676226748e-10, "15": 1.2484025354488079e-11, "16": 1.14116686554782e-12, "17": 8.462213697284381e-14, "2": 0.08944120086099697, "3": 0.036221655790713715, "4": 0.011847368816694149, "5": 0.0032311300794066913, "6": 0.0007532123583853277, "7": 0.00015301516646886357, "8": 2.751140627131187e-05, "9": 4.432868818352346e-06} |
| Raw goal margin distribution | {"-1": 0.20043780319095994, "-10": 2.0875501482840127e-05, "-11": 4.000967185974775e-06, "-12": 7.054275828272415e-07, "-13": 1.1513378786034334e-07, "-14": 1.7487787770481043e-08, "-15": 2.481559483341648e-09, "-16": 3.2629488587358634e-10, "-17": 3.480456164918511e-11, "-2": 0.1575156863875112, "-3": 0.09175834119390913, "-4": 0.04317081317734843, "-5": 0.01693611636744007, "-6": 0.0056789479732828755, "-7": 0.0016594951904078347, "-8": 0.000429185830515672, "-9": 9.94737591937752e-05, "0": 0.2251793697115234, "1": 0.13651845466478557, "10": 5.504606215521995e-07, "11": 7.334377553102904e-08, "12": 8.989999007682664e-09, "13": 1.0200440661101737e-09, "14": 1.0771097291762214e-10, "15": 1.062572809236323e-11, "16": 9.712995990484986e-13, "17": 7.202579236551279e-14, "2": 0.07612751925898094, "3": 0.030829916998601003, "4": 0.01008384043459813, "5": 0.00275016340322383, "6": 0.0006410936768189802, "7": 0.0001302382450161654, "8": 2.3416223067217866e-05, "9": 3.7730185092898668e-06} |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.7% |
| P home draw | 53.3% |
| P draw away | 69.8% |
| P home away | 76.9% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.79 |
| Reference draw odds | 4.04 |
| Reference away odds | 2.34 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.05 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | -4.5% |
| Draw probability edge | -0.6% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.0899 |
| Raw ev home | -0.2827 |
| Raw edge prob draw | -0.0117 |
| Raw ev draw | -0.0903 |
| Raw edge prob away | 0.1016 |
| Raw ev away | 0.2114 |

</details>


---

## 2026-10-30 — Elversberg vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **38.9%**. Expected goals are 1.91 for Elversberg and 1.56 for FSV Mainz 05 (3.47 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 67.1%; Under 3.5 goals: 54.7%; Double Chance 1X: 61.1%; Double Chance X2: 63.5%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 73.4%; BTTS Yes (both teams score): 68.6%; BTTS No (at least one team does not score): 31.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 36.5% | 2.74 |
| Draw | 24.6% | 4.07 |
| FSV Mainz 05 win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 1.91 |
| FSV Mainz 05 expected goals | 1.56 |
| Expected total goals | 3.47 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 67.1% |
| Under 2.5 | 32.9% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 26.6% |
| Under 4.5 | 73.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.50% |
| 2 | 1-2 | 9.15% |
| 3 | 2-1 | 7.16% |
| 4 | 2-2 | 7.04% |
| 5 | 0-1 | 4.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 36.5% | 27.9% | 3.38 | +23.4% |
| Draw | 24.6% | 25.1% | 3.74 | -8.1% |
| FSV Mainz 05 win | 38.9% | 47.1% | 2.05 | -20.3% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9114 |
| Dc lambda away | 1.5583 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.6% |
| P btts no | 31.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.68 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.67 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.04 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.76 |
| Fair Under 4.5 odds | 1.36 |
| Goal margin distribution | {"-1": 0.1984472664370343, "-10": 1.1994144745390665e-06, "-11": 1.66236542015326e-07, "-12": 2.1189645698713523e-08, "-13": 2.4996034797739656e-09, "-14": 2.741470995870983e-10, "-15": 2.7758100191695493e-11, "-16": 2.2792320208937382e-12, "-2": 0.11708995019109988, "-3": 0.04991753835355727, "-4": 0.017115126753792023, "-5": 0.004880328824973725, "-6": 0.0011874257776693813, "-7": 0.00025148488283122415, "-8": 4.709993090903446e-05, "-9": 7.900608116761476e-06, "0": 0.24583885468687927, "1": 0.1572134529468537, "10": 5.899254381220728e-06, "11": 1.0028740999697074e-06, "12": 1.5679625852631793e-07, "13": 2.2686902352388713e-08, "14": 3.051966889728629e-09, "15": 3.790338372762375e-10, "16": 3.8174104841352226e-11, "2": 0.11241151766908711, "3": 0.05878092707062159, "4": 0.024720398754310625, "5": 0.008646025613542215, "6": 0.0025802749538793995, "7": 0.0006702911403861038, "8": 0.00015397986912813917, "9": 3.168081006115786e-05} |
| Raw goal margin distribution | {"-1": 0.15666230812099172, "-10": 9.468663557259765e-07, "-11": 1.3123385790973555e-07, "-12": 1.6727964375764238e-08, "-13": 1.9732882067836463e-09, "-14": 2.164228218261571e-10, "-15": 2.191336833790325e-11, "-16": 1.7993180533417965e-12, "-2": 0.09243554816377343, "-3": 0.03940692615520454, "-4": 0.013511374125594961, "-5": 0.003852729200240109, "-6": 0.0009374019929424067, "-7": 0.0001985323502270436, "-8": 3.718259274128024e-05, "-9": 6.2370599774626536e-06, "0": 0.24113453245358674, "1": 0.19449215043453602, "10": 7.298094718089069e-06, "11": 1.2406771600147066e-06, "12": 1.939760302267652e-07, "13": 2.8066455780384405e-08, "14": 3.775654006142754e-09, "15": 4.689109278976927e-10, "16": 4.722600771333426e-11, "2": 0.13906671086514125, "3": 0.07271915154974413, "4": 0.0305821379990326, "5": 0.01069618459978973, "6": 0.0031921137478102884, "7": 0.0008292316138809151, "8": 0.00019049181421188006, "9": 3.91930128166935e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.3% |
| Raw p btts yes | 68.3% |
| P home draw | 61.1% |
| P draw away | 63.5% |
| P home away | 75.4% |
| Raw p home draw | 69.3% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.38 |
| Reference draw odds | 3.74 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | +8.7% |
| Draw probability edge | -0.5% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | 0.1732 |
| Raw ev home | 0.5271 |
| Raw edge prob draw | -0.0094 |
| Raw ev draw | -0.0982 |
| Raw edge prob away | -0.1638 |
| Raw ev away | -0.3705 |

</details>


---

## 2026-10-31 — Augsburg vs SC Freiburg

The model's most likely 1X2 outcome is **SC Freiburg win** at **41.0%**. Expected goals are 1.36 for Augsburg and 1.43 for SC Freiburg (2.80 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 53.6%; Under 3.5 goals: 69.1%; Double Chance 1X: 59.0%; Double Chance X2: 67.3%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 32.7% | 3.06 |
| Draw | 26.3% | 3.81 |
| SC Freiburg win | 41.0% | 2.44 |

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
| 1 | 1-1 | 12.46% |
| 2 | 1-2 | 9.32% |
| 3 | 0-1 | 8.08% |
| 4 | 2-1 | 7.72% |
| 5 | 0-0 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 32.7% | 31.0% | 3.06 | +0.1% |
| Draw | 26.3% | 24.6% | 3.81 | +0.1% |
| SC Freiburg win | 41.0% | 44.4% | 2.17 | -11.0% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Augsburg |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3642 |
| Dc lambda away | 1.4339 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.33 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.61 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.24 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.48 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.20978477302043919, "-10": 8.021947482833278e-07, "-11": 1.0305653945986082e-07, "-12": 1.2158389873403959e-08, "-13": 1.3164738579054845e-09, "-14": 1.1830158822572886e-10, "-2": 0.12523055974126882, "-3": 0.05208028606385306, "-4": 0.017095111419637633, "-5": 0.004614475970616151, "-6": 0.0010552212213159403, "-7": 0.0002090355842944876, "-8": 3.649513658333959e-05, "-9": 5.692717152732692e-06, "0": 0.26270707356324496, "1": 0.17321700622443084, "10": 4.2473130359321707e-07, "11": 5.191558363205686e-08, "12": 5.827549623290159e-09, "13": 6.003574216179627e-10, "14": 5.13305536833372e-11, "2": 0.09872859184036312, "3": 0.03906552916246093, "4": 0.012200567035757804, "5": 0.0031334170190881116, "6": 0.0006817529960585827, "7": 0.00012849655686085, "8": 2.134489342346034e-05, "9": 3.1678625721123402e-06} |
| Raw goal margin distribution | {"-1": 0.1924238517621795, "-10": 7.358084245372313e-07, "-11": 9.452800594929446e-08, "-12": 1.115221175008124e-08, "-13": 1.2075279193772022e-09, "-14": 1.085114374519459e-10, "-2": 0.1148669959063277, "-3": 0.047770336716985565, "-4": 0.015680390613239593, "-5": 0.004232601000280753, "-6": 0.0009678954718368502, "-7": 0.00019173666280051754, "-8": 3.3474949829980434e-05, "-9": 5.221611396050783e-06, "0": 0.27922686856507634, "1": 0.1824392623010505, "10": 4.4734444609504564e-07, "11": 5.4679624051977644e-08, "12": 6.137814510650917e-09, "13": 6.32321083849178e-10, "14": 5.406344649184739e-11, "2": 0.10398500618374576, "3": 0.04114541913145208, "4": 0.012850138090795781, "5": 0.0033002434455154804, "6": 0.0007180502445083612, "7": 0.00013533784905359978, "8": 2.2481318058488726e-05, "9": 3.3365229161071254e-06} |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 58.0% |
| P home draw | 59.0% |
| P draw away | 67.3% |
| P home away | 73.7% |
| Raw p home draw | 62.4% |
| Raw p draw away | 65.5% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.06 |
| Reference draw odds | 3.81 |
| Reference away odds | 2.17 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | +1.7% |
| Draw probability edge | +1.7% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -11.4% |
| Under 2.5 probability edge | +11.4% |
| Raw edge prob home | 0.0348 |
| Raw ev home | 0.0545 |
| Raw edge prob draw | 0.0330 |
| Raw ev draw | 0.0639 |
| Raw edge prob away | -0.0679 |
| Raw ev away | -0.1837 |

</details>


---

## 2026-10-31 — Bayer Leverkusen vs VfB Stuttgart

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **57.2%**. Expected goals are 2.29 for Bayer Leverkusen and 1.23 for VfB Stuttgart (3.51 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 68.0%; Under 3.5 goals: 53.7%; Double Chance 1X: 78.5%; Double Chance X2: 42.8%; Double Chance 12 (either team wins): 78.8%; Under 4.5 goals: 72.5%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 57.2% | 1.75 |
| Draw | 21.2% | 4.71 |
| VfB Stuttgart win | 21.5% | 4.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.29 |
| VfB Stuttgart expected goals | 1.23 |
| Expected total goals | 3.51 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 87.3% |
| Under 1.5 | 12.7% |
| Over 2.5 | 68.0% |
| Under 2.5 | 32.0% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.5% |
| Under 4.5 | 72.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.29% |
| 2 | 2-1 | 9.07% |
| 3 | 2-0 | 7.40% |
| 4 | 3-1 | 6.92% |
| 5 | 1-2 | 5.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 57.2% | 54.2% | 1.79 | +2.4% |
| Draw | 21.2% | 21.3% | 4.35 | -7.6% |
| VfB Stuttgart win | 21.5% | 24.6% | 3.79 | -18.4% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.57 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.89 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.13 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.63 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.12677089805092565, "-10": 9.395357529872544e-08, "-11": 1.0251623228599224e-08, "-12": 1.0285675908905366e-09, "-13": 9.549454269582729e-11, "-14": 8.248939624781043e-12, "-15": 6.661099088044022e-13, "-16": 5.046887617465595e-14, "-17": 3.5696539308378705e-15, "-18": 2.1024854092229062e-16, "-2": 0.060771245432150726, "-3": 0.020564982412681412, "-4": 0.005580503635204136, "-5": 0.001257114563770122, "-6": 0.00024135474747224032, "-7": 4.030320816890066e-05, "-8": 5.9481624438378565e-06, "-9": 7.859236253580835e-07, "0": 0.21243713523205665, "1": 0.20040386417440964, "10": 3.942480112868736e-05, "11": 8.03258608931251e-06, "12": 1.5048809368353596e-06, "13": 2.6088818444796934e-07, "14": 4.20804654141617e-08, "15": 6.345047184998375e-09, "16": 8.976750374307775e-10, "17": 1.1855726749749104e-10, "18": 1.3038919670561095e-11, "2": 0.1725448166955891, "3": 0.1090281581691048, "4": 0.055244656922386615, "5": 0.023237975830696107, "6": 0.008330783269492048, "7": 0.0025976232360139504, "8": 0.0007158564059957009, "9": 0.0001766159784600279} |
| Raw goal margin distribution | {"-1": 0.10877048767188512, "-10": 8.061295108641007e-08, "-11": 8.795978218559453e-09, "-12": 8.825195702227873e-10, "-13": 8.19351139632709e-11, "-14": 7.077658986078469e-12, "-15": 5.715278564534924e-13, "-16": 4.33027166184789e-14, "-17": 3.0627928400501054e-15, "-18": 1.8039500137668125e-16, "-2": 0.05214223535300254, "-3": 0.01764492640174024, "-4": 0.0047881186548985695, "-5": 0.0010786147788096933, "-6": 0.00020708438599160474, "-7": 3.458048869790128e-05, "-8": 5.103572978617954e-06, "-9": 6.743290243847138e-07, "0": 0.21228678151940347, "1": 0.21115770065308168, "10": 4.154036844216538e-05, "11": 8.463621277487052e-06, "12": 1.585634087884953e-06, "13": 2.7488765938987685e-07, "14": 4.433853786138995e-08, "15": 6.685527645083455e-09, "16": 9.45845019597963e-10, "17": 1.249191481592163e-10, "18": 1.3738598843781645e-11, "2": 0.18180371373148638, "3": 0.11487869897255434, "4": 0.058209130732864885, "5": 0.024484944761201145, "6": 0.008777819964061007, "7": 0.0027370138392259816, "8": 0.000754269850586709, "9": 0.00018609333739072622} |
| Unadjusted home-win probability | 60.3% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 64.4% |
| P home draw | 78.5% |
| P draw away | 42.8% |
| P home away | 78.8% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.7% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 4.35 |
| Reference away odds | 3.79 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.42 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | +3.1% |
| Draw probability edge | -0.0% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.0614 |
| Raw ev home | 0.0794 |
| Raw edge prob draw | -0.0003 |
| Raw ev draw | -0.0766 |
| Raw edge prob away | -0.0611 |
| Raw ev away | -0.3001 |

</details>


---

## 2026-10-31 — Bayern Munich vs Borussia Dortmund

The model's most likely 1X2 outcome is **Bayern Munich win** at **68.9%**. Expected goals are 2.72 for Bayern Munich and 1.39 for Borussia Dortmund (4.11 combined). The most likely exact score is 2-1 at 9.0%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 78.3%; Under 3.5 goals: 40.7%; Double Chance 1X: 86.0%; Double Chance X2: 31.1%; Double Chance 12 (either team wins): 83.0%; Under 4.5 goals: 60.2%; BTTS Yes (both teams score): 70.3%; BTTS No (at least one team does not score): 29.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 68.9% | 1.45 |
| Draw | 17.0% | 5.88 |
| Borussia Dortmund win | 14.0% | 7.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.72 |
| Borussia Dortmund expected goals | 1.39 |
| Expected total goals | 4.11 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 92.5% |
| Under 1.5 | 7.5% |
| Over 2.5 | 78.3% |
| Under 2.5 | 21.7% |
| Over 3.5 | 59.3% |
| Under 3.5 | 40.7% |
| Over 4.5 | 39.8% |
| Under 4.5 | 60.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.96% |
| 2 | 3-1 | 8.13% |
| 3 | 2-0 | 6.45% |
| 4 | 1-1 | 6.43% |
| 5 | 3-0 | 5.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 68.9% | 73.0% | 1.34 | -7.6% |
| Draw | 17.0% | 15.8% | 5.54 | -5.8% |
| Borussia Dortmund win | 14.0% | 11.2% | 7.60 | +6.8% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Bayern Munich |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7223 |
| Dc lambda away | 1.3880 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 70.3% |
| P btts no | 29.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.96 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.32 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.61 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.51 |
| Fair Under 4.5 odds | 1.66 |
| Goal margin distribution | {"-1": 0.08031604522222056, "-10": 1.4037098560925746e-07, "-11": 1.7231045635318487e-08, "-12": 1.946909662734388e-09, "-13": 2.0372110175431053e-10, "-14": 1.9846525047657738e-11, "-15": 1.8084350976681798e-12, "-16": 1.5475404835363064e-13, "-17": 1.2469978637244471e-14, "-18": 9.366653768173077e-16, "-19": 5.707698037069112e-17, "-2": 0.03992050086705353, "-3": 0.014551721338267206, "-4": 0.004318596915707715, "-5": 0.0010741365139224155, "-6": 0.00022912261448630744, "-7": 4.2690977734017765e-05, "-8": 7.0515123277935315e-06, "-9": 1.045078063536702e-06, "0": 0.17006690850710035, "1": 0.2076409728206379, "10": 0.0001505090631416561, "11": 3.623456654151738e-05, "12": 8.02940516399412e-06, "13": 1.6477818818488076e-06, "14": 3.1482870158787027e-07, "15": 5.626248412629625e-08, "16": 9.442437738712021e-09, "17": 1.4922237745734075e-09, "18": 2.1982589362866508e-10, "19": 2.627129636610237e-11, "2": 0.19555647832677833, "3": 0.13980307703627395, "4": 0.08137128336525316, "5": 0.03969301699691522, "6": 0.016605376270070735, "7": 0.006067964071272194, "8": 0.001965691245098075, "9": 0.0005713574576582887} |
| Raw goal margin distribution | {"-1": 0.09634733373088952, "-10": 1.6838939416413536e-07, "-11": 2.067040651422549e-08, "-12": 2.3355178221283626e-09, "-13": 2.443843558835576e-10, "-14": 2.3807942321792905e-11, "-15": 2.1694033789089575e-12, "-16": 1.856433531018577e-13, "-17": 1.4959018338807078e-14, "-18": 1.123626187079975e-15, "-19": 6.846969196392868e-17, "-2": 0.04788873517241057, "-3": 0.017456282219297427, "-4": 0.005180599930383093, "-5": 0.0012885369155450548, "-6": 0.00027485607567115047, "-7": 5.12122063238669e-05, "-8": 8.45901226428217e-06, "-9": 1.2536783239738626e-06, "0": 0.18207593623115806, "1": 0.19558091932925978, "10": 0.00014176730409589438, "11": 3.413001653488128e-05, "12": 7.563047034062974e-06, "13": 1.552076600914749e-06, "14": 2.9654304760448916e-07, "15": 5.299468702968437e-08, "16": 8.894008868094846e-09, "17": 1.4055535076314063e-09, "18": 2.0705812433950003e-10, "19": 2.474542584469653e-11, "2": 0.18419830774430998, "3": 0.13168313536766538, "4": 0.07664513506842963, "5": 0.037387595760854625, "6": 0.015640914760662844, "7": 0.005715528950740773, "8": 0.0018515213814079533, "9": 0.0005381722851537805} |
| Unadjusted home-win probability | 64.9% |
| Unadjusted draw probability | 18.2% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 41.2% |
| Raw p btts yes | 70.8% |
| P home draw | 86.0% |
| P draw away | 31.1% |
| P home away | 83.0% |
| Raw p home draw | 83.2% |
| Raw p draw away | 35.1% |
| Raw p home away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.34 |
| Reference draw odds | 5.54 |
| Reference away odds | 7.60 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.48 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | -4.0% |
| Draw probability edge | +1.2% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | -0.0801 |
| Raw ev home | -0.1298 |
| Raw edge prob draw | 0.0240 |
| Raw ev draw | 0.0087 |
| Raw edge prob away | 0.0561 |
| Raw ev away | 0.2806 |

</details>


---

## 2026-10-31 — Borussia Monchengladbach vs SC Paderborn

The model's most likely 1X2 outcome is **Borussia Monchengladbach win** at **52.5%**. Expected goals are 1.56 for Borussia Monchengladbach and 0.85 for SC Paderborn (2.40 combined). The most likely exact score is 1-0 at 12.7%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 44.0%; Under 3.5 goals: 77.7%; Double Chance 1X: 77.9%; Double Chance X2: 47.5%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 90.2%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 52.5% | 1.90 |
| Draw | 25.4% | 3.94 |
| SC Paderborn win | 22.1% | 4.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.56 |
| SC Paderborn expected goals | 0.85 |
| Expected total goals | 2.40 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 70.6% |
| Under 1.5 | 29.4% |
| Over 2.5 | 44.0% |
| Under 2.5 | 56.0% |
| Over 3.5 | 22.3% |
| Under 3.5 | 77.7% |
| Over 4.5 | 9.8% |
| Under 4.5 | 90.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.70% |
| 2 | 1-1 | 11.95% |
| 3 | 2-0 | 10.90% |
| 4 | 0-0 | 9.35% |
| 5 | 2-1 | 9.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 52.5% | 52.4% | 1.85 | -2.8% |
| Draw | 25.4% | 22.6% | 4.11 | +4.4% |
| SC Paderborn win | 22.1% | 25.0% | 3.74 | -17.5% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | M'gladbach |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5556 |
| Dc lambda away | 0.8480 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.70 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.41 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.49 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.15 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.14570039142514485, "-10": 6.222653718905488e-09, "-11": 4.7500647152069e-10, "-12": 3.3287841024085984e-11, "-13": 2.1556581925779393e-12, "-14": 1.2933307809665382e-13, "-15": 6.7206572980793055e-15, "-2": 0.05691611788729282, "-3": 0.014580925673927757, "-4": 0.002907272418180937, "-5": 0.0004729025954026122, "-6": 6.484679187803146e-05, "-7": 7.678131631936257e-06, "-8": 7.994506844506164e-07, "-9": 7.425109968232904e-08, "0": 0.2540255321826448, "1": 0.2421751813872431, "10": 2.321839351825286e-06, "11": 3.251232618758908e-07, "12": 4.179517315205716e-08, "13": 4.9649214540499035e-09, "14": 5.46429428006503e-10, "15": 5.208686272040859e-11, "2": 0.16563645938793492, "3": 0.07783908956921853, "4": 0.02847018982043633, "5": 0.008495096476174302, "6": 0.002136865052467841, "7": 0.0004641262559791467, "8": 8.86470414992252e-05, "9": 1.5103146694294039e-05} |
| Raw goal margin distribution | {"-1": 0.12637968370510247, "-10": 5.397494139236309e-09, "-11": 4.120178885003426e-10, "-12": 2.88736823470448e-11, "-13": 1.8698055502086793e-12, "-14": 1.1218277001582312e-13, "-15": 5.8294595869909965e-15, "-2": 0.049368714153481846, "-3": 0.012647411285407029, "-4": 0.0025217514178267762, "-5": 0.0004101929984245049, "-6": 5.624773527836854e-05, "-7": 6.659967331582492e-06, "-8": 6.934389376064517e-07, "-9": 6.44049779195674e-08, "0": 0.28173473788418, "1": 0.24288991189577047, "10": 2.328691785716914e-06, "11": 3.2608279667612737e-07, "12": 4.191852305599796e-08, "13": 4.9795744040975704e-09, "14": 5.480421026857011e-10, "15": 5.224058644084313e-11, "2": 0.1661253015152367, "3": 0.07806881571932374, "4": 0.02855421376183144, "5": 0.008520168015667429, "6": 0.0021431715725532445, "7": 0.0004654960296820369, "8": 8.890866510857798e-05, "9": 1.5147720542263686e-05} |
| Unadjusted home-win probability | 52.7% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 77.8% |
| Raw p btts yes | 46.4% |
| P home draw | 77.9% |
| P draw away | 47.5% |
| P home away | 74.6% |
| Raw p home draw | 80.9% |
| Raw p draw away | 47.3% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.02, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 4.11 |
| Reference away odds | 3.74 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | +0.2% |
| Draw probability edge | +2.8% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -21.0% |
| Under 2.5 probability edge | +21.0% |
| Raw edge prob home | 0.0031 |
| Raw ev home | -0.0253 |
| Raw edge prob draw | 0.0554 |
| Raw ev draw | 0.1579 |
| Raw edge prob away | -0.0585 |
| Raw ev away | -0.2842 |

</details>


---

## 2026-10-31 — FC Schalke 04 vs RB Leipzig

The model's most likely 1X2 outcome is **RB Leipzig win** at **57.4%**. Expected goals are 0.91 for FC Schalke 04 and 2.08 for RB Leipzig (3.00 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 56.6%; Under 3.5 goals: 65.6%; Double Chance 1X: 42.6%; Double Chance X2: 81.3%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 82.2%; BTTS Yes (both teams score): 54.3%; BTTS No (at least one team does not score): 45.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 18.7% | 5.33 |
| Draw | 23.8% | 4.20 |
| RB Leipzig win | 57.4% | 1.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.91 |
| RB Leipzig expected goals | 2.08 |
| Expected total goals | 3.00 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 56.6% |
| Under 2.5 | 43.4% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 17.8% |
| Under 4.5 | 82.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.32% |
| 2 | 0-2 | 9.84% |
| 3 | 1-2 | 8.97% |
| 4 | 0-1 | 8.48% |
| 5 | 0-3 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 18.7% | 23.1% | 4.04 | -24.3% |
| Draw | 23.8% | 25.4% | 3.68 | -12.4% |
| RB Leipzig win | 57.4% | 51.5% | 1.88 | +8.0% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Schalke 04 |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9120 |
| Dc lambda away | 2.0843 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.3% |
| P btts no | 45.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.40 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.12 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 2.91 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.61 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.20796960327578495, "-10": 2.293457376218732e-05, "-11": 4.28478121265237e-06, "-12": 7.353731114979573e-07, "-13": 1.1669671098910166e-07, "-14": 1.7219141177935717e-08, "-15": 2.373530028056609e-09, "-16": 3.054564969514682e-10, "-17": 3.368467747905867e-11, "-2": 0.17759072526265304, "-3": 0.1077244271917124, "-4": 0.051517018038574953, "-5": 0.020246628319045664, "-6": 0.006738239041215049, "-7": 0.0019421251498792408, "-8": 0.0004932463972116639, "-9": 0.00011190805289390463, "0": 0.23814973425736316, "1": 0.12261898364371579, "10": 8.450650391029804e-09, "11": 6.908245836316526e-10, "12": 5.187839720020732e-11, "13": 3.6022768808336e-12, "14": 2.325785361161019e-13, "15": 1.4027896320082713e-14, "16": 7.899268114926854e-16, "17": 3.8116196080476366e-17, "2": 0.04869701877042652, "3": 0.012925160900580183, "4": 0.0027046567263989906, "5": 0.00046510800799035414, "6": 6.773095379126503e-05, "7": 8.541962510436374e-06, "8": 9.492575095903665e-07, "9": 9.423693017189357e-08} |
| Raw goal margin distribution | {"-1": 0.22942237916952588, "-10": 2.5300353488593917e-05, "-11": 4.726771049921274e-06, "-12": 8.112293631364653e-07, "-13": 1.2873437586393457e-07, "-14": 1.8995354484853877e-08, "-15": 2.6183677686058397e-09, "-16": 3.3696537936106406e-10, "-17": 3.7159367172306394e-11, "-2": 0.19590981598484133, "-3": 0.11883657030505404, "-4": 0.056831174652269084, "-5": 0.022335137279445878, "-6": 0.007433311445031445, "-7": 0.0021424620017157442, "-8": 0.0005441264501285556, "-9": 0.00012345175130763035, "0": 0.22197726995062123, "1": 0.09444758905457712, "10": 6.5091353039997995e-09, "11": 5.321094209459756e-10, "12": 3.995946952074105e-11, "13": 2.7746630773775166e-12, "14": 1.7914421853173223e-13, "15": 1.0805023394983001e-14, "16": 6.084431680809903e-16, "17": 2.935909854050576e-17, "2": 0.037509004563079235, "3": 0.009955638588143268, "4": 0.002083268833567121, "5": 0.0003582506452043755, "6": 5.216994220519132e-05, "7": 6.579468699964597e-06, "8": 7.311680500734362e-07, "9": 7.25862390158217e-08} |
| Unadjusted home-win probability | 14.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 63.4% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 64.8% |
| Raw p btts yes | 53.4% |
| P home draw | 42.6% |
| P draw away | 81.3% |
| P home away | 76.2% |
| Raw p home draw | 36.6% |
| Raw p draw away | 85.6% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.04 |
| Reference draw odds | 3.68 |
| Reference away odds | 1.88 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | -4.3% |
| Draw probability edge | -1.6% |
| Away probability edge | +5.9% |
| Over 2.5 probability edge | -10.8% |
| Under 2.5 probability edge | +10.8% |
| Raw edge prob home | -0.0861 |
| Raw ev home | -0.4166 |
| Raw edge prob draw | -0.0323 |
| Raw ev draw | -0.1831 |
| Raw edge prob away | 0.1185 |
| Raw ev away | 0.1912 |

</details>


---

## 2026-10-31 — Werder Bremen vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **38.3%**. Expected goals are 1.82 for Werder Bremen and 1.59 for TSG Hoffenheim (3.42 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 66.4%; Under 3.5 goals: 55.6%; Double Chance 1X: 61.7%; Double Chance X2: 62.5%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 74.1%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 37.5% | 2.67 |
| Draw | 24.2% | 4.12 |
| TSG Hoffenheim win | 38.3% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.82 |
| TSG Hoffenheim expected goals | 1.59 |
| Expected total goals | 3.42 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 66.4% |
| Under 2.5 | 33.6% |
| Over 3.5 | 44.4% |
| Under 3.5 | 55.6% |
| Over 4.5 | 25.9% |
| Under 4.5 | 74.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.46% |
| 2 | 1-2 | 8.82% |
| 3 | 2-1 | 7.67% |
| 4 | 2-2 | 6.84% |
| 5 | 0-1 | 4.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 37.5% | 32.5% | 2.92 | +9.5% |
| Draw | 24.2% | 23.9% | 3.91 | -5.2% |
| TSG Hoffenheim win | 38.3% | 43.5% | 2.21 | -15.4% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
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
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 67.9% |
| P btts no | 32.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.32 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.42 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.98 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.86 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.19122893934353938, "-10": 1.4404495499070294e-06, "-11": 2.042808350418618e-07, "-12": 2.6641817911821037e-08, "-13": 3.2153285880648383e-09, "-14": 3.607898035594802e-10, "-15": 3.7393317924720266e-11, "-16": 3.1522413585781286e-12, "-2": 0.11592908693546522, "-3": 0.050743963803871264, "-4": 0.0178418505895981, "-5": 0.005213278770693562, "-6": 0.001299147805678588, "-7": 0.00028171521276709586, "-8": 5.4008660575536384e-05, "-9": 9.272017905659322e-06, "0": 0.24248754603025213, "1": 0.16778500295443757, "10": 4.202916699864566e-06, "11": 6.817933746895376e-07, "12": 1.0170947902950243e-07, "13": 1.4040913307043385e-08, "14": 1.8021738060964816e-09, "15": 2.1365292443081654e-10, "16": 2.0601873891787293e-11, "2": 0.1154159340582711, "3": 0.05778700226786333, "4": 0.023241175879767394, "5": 0.007767863217993503, "6": 0.0022142242709918478, "7": 0.0005492192673197834, "8": 0.00012044015157603524, "9": 2.3651275670663283e-05} |
| Raw goal margin distribution | {"-1": 0.1648197882506244, "-10": 1.241520193629651e-06, "-11": 1.7606918749245217e-07, "-12": 2.2962522314415528e-08, "-13": 2.7712844031884757e-09, "-14": 3.109639117896772e-10, "-15": 3.222921574264797e-11, "-16": 2.7169096634602066e-12, "-2": 0.09991901657973165, "-3": 0.04373610708641926, "-4": 0.015377850477400494, "-5": 0.004493313125235499, "-6": 0.001119732541388707, "-7": 0.0002428097016834762, "-8": 4.654994181486316e-05, "-9": 7.99153116213944e-06, "0": 0.2455633381451781, "1": 0.19005546579910343, "10": 4.760778836261686e-06, "11": 7.72289269742124e-07, "12": 1.1520959604706417e-07, "13": 1.590459380651328e-08, "14": 2.0413801957116524e-09, "15": 2.420115347440564e-10, "16": 2.333640474352338e-11, "2": 0.13073533821160369, "3": 0.06545719486106279, "4": 0.026326026937863792, "5": 0.008798908342007049, "6": 0.002508123001441981, "7": 0.0006221183171218765, "8": 0.00013642643088258562, "9": 2.6790560152456272e-05} |
| Unadjusted home-win probability | 42.5% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 33.0% |
| Raw p over 1 5 | 86.6% |
| Raw p under 3 5 | 55.5% |
| Raw p btts yes | 67.9% |
| P home draw | 61.7% |
| P draw away | 62.5% |
| P home away | 75.8% |
| Raw p home draw | 67.0% |
| Raw p draw away | 57.5% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.92 |
| Reference draw odds | 3.91 |
| Reference away odds | 2.21 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Home probability edge | +5.0% |
| Draw probability edge | +0.3% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | 0.0995 |
| Raw ev home | 0.2400 |
| Raw edge prob draw | 0.0062 |
| Raw ev draw | -0.0398 |
| Raw edge prob away | -0.1057 |
| Raw ev away | -0.2712 |

</details>


---

## 2026-11-01 — Union Berlin vs 1. FC Köln

The model's most likely 1X2 outcome is **Union Berlin win** at **41.3%**. Expected goals are 1.44 for Union Berlin and 1.07 for 1. FC Köln (2.51 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 46.2%; Under 3.5 goals: 75.7%; Double Chance 1X: 69.0%; Double Chance X2: 58.7%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 88.9%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 41.3% | 2.42 |
| Draw | 27.7% | 3.61 |
| 1. FC Köln win | 31.0% | 3.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 1.44 |
| 1. FC Köln expected goals | 1.07 |
| Expected total goals | 2.51 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 72.8% |
| Under 1.5 | 27.2% |
| Over 2.5 | 46.2% |
| Under 2.5 | 53.8% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 11.1% |
| Under 4.5 | 88.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.23% |
| 2 | 1-0 | 9.67% |
| 3 | 0-0 | 9.07% |
| 4 | 0-1 | 8.51% |
| 5 | 2-1 | 8.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 41.3% | 38.5% | 2.49 | +2.7% |
| Draw | 27.7% | 26.3% | 3.59 | -0.4% |
| 1. FC Köln win | 31.0% | 35.2% | 2.71 | -16.0% |
| Over 2.5 | 46.2% | 58.4% | 1.70 | -21.4% |
| Under 2.5 | 53.8% | 41.6% | 2.34 | +25.8% |

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
| Market best home last update utc | 2026-10-22T15:06:12Z |
| Market best draw last update utc | 2026-10-22T15:06:12Z |
| Market best away last update utc | 2026-10-22T15:06:12Z |
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
| Bbs statistics cutoff utc | 2026-10-22T15:06:06.989068+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.02 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.67 |
| Fair Over 2.5 odds | 2.16 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.04 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.18548687164856578, "-10": 5.929958829843103e-08, "-11": 5.7065984579617636e-09, "-12": 5.041834780410551e-10, "-13": 4.0977052094062334e-11, "-14": 2.8241238533814397e-12, "-2": 0.08785085771875996, "-3": 0.028013761319199495, "-4": 0.006987568219900996, "-5": 0.0014259032766840444, "-6": 0.0002457163115784811, "-7": 3.660305324728266e-05, "-8": 4.798501591796119e-06, "-9": 5.614475982666162e-07, "0": 0.2773532982123854, "1": 0.2056440293074293, "10": 8.970820891499994e-07, "11": 1.1569669382395907e-07, "12": 1.3699205171727994e-08, "13": 1.492143524168875e-09, "14": 1.3782143005532084e-10, "2": 0.12770899963409993, "3": 0.0545770487341821, "4": 0.018244325442542796, "5": 0.004989476057691464, "6": 0.0011522905224459212, "7": 0.00023004269258035303, "8": 4.0416611349992786e-05, "9": 6.337626042209705e-06} |
| Raw goal margin distribution | {"-1": 0.16015773402330213, "-10": 5.12019400940976e-08, "-11": 4.927334586458821e-09, "-12": 4.353347633574532e-10, "-13": 3.538143563483068e-11, "-14": 2.4384759575636794e-12, "-2": 0.07585439432553452, "-3": 0.02418834548492054, "-4": 0.006033381675404605, "-5": 0.0012311892248784064, "-6": 0.0002121625499702987, "-7": 3.160472767865773e-05, "-8": 4.143242779496285e-06, "-9": 4.84779188478495e-07, "0": 0.29212870858426954, "1": 0.2193823070726124, "10": 9.57012654410851e-07, "11": 1.2342593994707744e-07, "12": 1.4614395787498682e-08, "13": 1.5918278294686185e-09, "14": 1.4702874375400425e-10, "2": 0.1362407411876756, "3": 0.058223129087885024, "4": 0.01946315786579465, "5": 0.005322803547014391, "6": 0.0012292705705264034, "7": 0.00024541095014252547, "8": 4.3116687957729194e-05, "9": 6.761018188497463e-06} |
| Unadjusted home-win probability | 44.0% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 26.8% |
| Raw p over 1 5 | 72.8% |
| Raw p under 3 5 | 75.6% |
| Raw p btts yes | 51.5% |
| P home draw | 69.0% |
| P draw away | 58.7% |
| P home away | 72.3% |
| Raw p home draw | 73.2% |
| Raw p draw away | 56.0% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.03, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:06:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.49 |
| Reference draw odds | 3.59 |
| Reference away odds | 2.71 |
| Market reference 1x2 last update utc | 2026-10-22T15:06:12Z |
| Market reference home last update utc | 2026-10-22T15:06:12Z |
| Market reference draw last update utc | 2026-10-22T15:06:12Z |
| Market reference away last update utc | 2026-10-22T15:06:12Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.26 |
| Market reference over 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:06:12Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:48Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:48Z |
| Home probability edge | +2.8% |
| Draw probability edge | +1.5% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -12.1% |
| Under 2.5 probability edge | +12.1% |
| Raw edge prob home | 0.0551 |
| Raw ev home | 0.0960 |
| Raw edge prob draw | 0.0296 |
| Raw ev draw | 0.0487 |
| Raw edge prob away | -0.0847 |
| Raw ev away | -0.2745 |

</details>


---
