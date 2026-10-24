# Ligue 1 — football model report

Fixtures in this report: **8**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,744 |
| Training data through | 2026-10-23 |
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
| Training sha256 | 6dc495c5225ffd8905fdcef4ff7b125391bfa0b806e25c3045748aff44845797 |
| Training as of utc | 2026-10-24T14:49:18.960151+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 64, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 64, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 64, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-24T14:49:18.960151+00:00', 'observations': 243, 'observations_sha256': '74fc35e22a1c1e9a6b223007148aa46d5d227cc2eee1d44dbd1c39f80c8d1412', 'eligible_training_matches': 91, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 101, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 91, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '5dbbff99011df08cab1e5b41a1ba38de1cccf4e94aa85b48d771e5fe4812caf7', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5081.975 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.186 |
| Dixon-Coles low-score adjustment | -0.057 |
| Xi per day | 0 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1744, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-23'} |
| Training data health | {'training_end': '2026-10-23', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 8.00 |
| Additional event odds calls used before this league | 22.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261024T144918960151Z_a8a0704ac53f35485f91ad20c9d99baa264a4fa2af1a1f31b3013a91c70880e1.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
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

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **44.3%**. Expected goals are 1.68 for RC Lens and 1.03 for Paris FC (2.70 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 50.1%; Under 3.5 goals: 72.0%; Double Chance 1X: 70.5%; Double Chance X2: 55.7%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 44.3% | 2.26 |
| Draw | 26.2% | 3.82 |
| Paris FC win | 29.5% | 3.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.68 |
| Paris FC expected goals | 1.03 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.1% |
| Under 2.5 | 49.9% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.49% |
| 2 | 1-0 | 9.02% |
| 3 | 2-1 | 8.24% |
| 4 | 0-1 | 8.17% |
| 5 | 2-0 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 44.3% | 36.6% | 2.68 | +18.6% |
| Draw | 26.2% | 26.8% | 3.55 | -7.0% |
| Paris FC win | 29.5% | 36.6% | 2.68 | -20.9% |

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
| Market best home last update utc | 2026-10-24T14:49:25Z |
| Market best draw last update utc | 2026-10-24T14:49:25Z |
| Market best away last update utc | 2026-10-24T14:49:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6765 |
| Dc lambda away | 1.0255 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:49:18.960151+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.3% |
| P btts no | 46.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.25 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.46 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.18511394844667364, "-10": 3.6469865099309996e-08, "-11": 3.356703157275502e-09, "-12": 2.8375506499203027e-10, "-13": 2.2170978137966823e-11, "-14": 1.6021242801101533e-12, "-15": 9.826777966112868e-14, "-2": 0.07927380122194962, "-3": 0.02392822937998697, "-4": 0.0056724003839499215, "-5": 0.0011026237995448976, "-6": 0.00018125156218307172, "-7": 2.5779752469108336e-05, "-8": 3.2289305492577406e-06, "-9": 3.6112138582282717e-07, "0": 0.26204158040314873, "1": 0.19986105308318466, "10": 3.2261861495423626e-06, "11": 4.854443554959311e-07, "12": 6.708746691800827e-08, "13": 8.569468340003233e-09, "14": 1.0123635037280084e-09, "15": 1.0151323652957152e-10, "2": 0.13744056246207417, "3": 0.06782144784964908, "4": 0.02628419160704336, "5": 0.008352689975235444, "6": 0.0022446674627681225, "7": 0.0005219396009117698, "8": 0.00010687385210625766, "9": 1.9540569674384186e-05} |
| Raw goal margin distribution | {"-1": 0.14094147636812815, "-10": 2.776731128677725e-08, "-11": 2.5557161018163546e-09, "-12": 2.160445397145844e-10, "-13": 1.6880469664827615e-11, "-14": 1.2198203498911271e-12, "-15": 7.481881328271278e-14, "-2": 0.060357237665176464, "-3": 0.018218400093508377, "-4": 0.004318834379438168, "-5": 0.0008395122436236131, "-6": 0.00013800074485187044, "-7": 1.9628106924896162e-05, "-8": 2.458432995035143e-06, "-9": 2.7494946595359205e-07, "0": 0.25561811265512646, "1": 0.23457682798283058, "10": 3.786573230587374e-06, "11": 5.69765821392972e-07, "12": 7.87405297043014e-08, "13": 1.0057981130823827e-08, "14": 1.188210588339389e-09, "15": 1.1914603999142628e-10, "2": 0.16131392625611057, "3": 0.07960200279317042, "4": 0.030849743850328577, "5": 0.00980354846173663, "6": 0.0026345651900135806, "7": 0.0006126002744994469, "8": 0.00012543779207926806, "9": 2.2934757825411413e-05} |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 52.8% |
| P home draw | 70.5% |
| P draw away | 55.7% |
| P home away | 73.8% |
| Raw p home draw | 77.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.85, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.86, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.71, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.39, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.37, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.39, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.72 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.72 |
| Market reference 1x2 last update utc | 2026-10-24T14:49:26Z |
| Market reference home last update utc | 2026-10-24T14:49:26Z |
| Market reference draw last update utc | 2026-10-24T14:49:26Z |
| Market reference away last update utc | 2026-10-24T14:49:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | +7.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -7.0% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | 0.1538 |
| Raw ev home | 0.3924 |
| Raw edge prob draw | -0.0128 |
| Raw ev draw | -0.0926 |
| Raw edge prob away | -0.1409 |
| Raw ev away | -0.3974 |
| Market p home draw | 63.5% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:49:20Z |
| Market reference home draw last update utc | 2026-10-24T14:49:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.9% |
| Market draw away odds | 1.52 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:49:20Z |
| Market reference draw away last update utc | 2026-10-24T14:49:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:49:20Z |
| Market reference home away last update utc | 2026-10-24T14:49:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.52 |
| Market reference dc home draw odds | 1.53 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 81.7% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-24T14:49:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market reference under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.4% |
| Market btts yes odds | 1.52 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:49:20Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.67 |
| Market reference btts yes last update utc | 2026-10-24T14:49:20Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,574.7541 |
| Elo away rating | 1,494.3238 |
| Elo rating diff | 140.4303 |
| Elo home expectancy | 0.6918 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **45.5%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 53.4%; Under 3.5 goals: 68.7%; Double Chance 1X: 72.1%; Double Chance X2: 54.5%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 45.5% | 2.20 |
| Draw | 26.7% | 3.75 |
| Lille win | 27.9% | 3.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.56 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.61% |
| 2 | 2-1 | 9.53% |
| 3 | 1-0 | 8.99% |
| 4 | 2-0 | 7.54% |
| 5 | 1-2 | 6.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 45.5% | 47.4% | 2.07 | -5.9% |
| Draw | 26.7% | 27.2% | 3.37 | -10.1% |
| Lille win | 27.9% | 25.4% | 3.93 | +9.5% |
| Over 2.5 | 53.4% | 51.7% | 1.83 | -2.2% |
| Under 2.5 | 46.6% | 48.3% | 2.07 | -3.6% |

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
| Market best home last update utc | 2026-10-24T14:49:25Z |
| Market best draw last update utc | 2026-10-24T14:49:25Z |
| Market best away last update utc | 2026-10-24T14:49:25Z |
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
| Dc lambda home | 1.5575 |
| Dc lambda away | 1.2642 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:49:18.960151+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.84 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.44 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.15755944172032924, "-10": 1.8777979670646855e-07, "-11": 2.126728323825223e-08, "-12": 2.212805394817275e-09, "-13": 2.128312042908417e-10, "-14": 1.8907317911568507e-11, "-15": 1.408585973745165e-12, "-2": 0.08049718053544899, "-3": 0.029492139016180585, "-4": 0.00853062052299963, "-5": 0.0020294239207769285, "-6": 0.0004090504268484303, "-7": 7.142723468438945e-05, "-8": 1.0992787993368435e-05, "-9": 1.5115947523908734e-06, "0": 0.26686855187404823, "1": 0.22214313259657337, "10": 1.7185752423094846e-06, "11": 2.397964545322443e-07, "12": 3.07386662953074e-08, "13": 3.642404359649199e-09, "14": 3.986518990436419e-10, "15": 3.658965598122682e-11, "2": 0.13880717239827176, "3": 0.06265396593507083, "4": 0.022327185133050827, "5": 0.006543907945973603, "6": 0.0016249960609342263, "7": 0.0003495830403142647, "8": 6.628349909899926e-05, "9": 1.1229075608163497e-05} |
| Raw goal margin distribution | {"-1": 0.1713361205253951, "-10": 2.0419888220879927e-07, "-11": 2.3126851456003527e-08, "-12": 2.4062886215262533e-09, "-13": 2.3144073418759534e-10, "-14": 2.0560535535906786e-11, "-15": 1.5317498813963067e-12, "-2": 0.08753569113717317, "-3": 0.032070871982380525, "-4": 0.009276520722124955, "-5": 0.0022068726424186846, "-6": 0.00044481696856903867, "-7": 7.767268757148184e-05, "-8": 1.1953975134572181e-05, "-9": 1.6437655392363642e-06, "0": 0.26196935047260433, "1": 0.21263182248980544, "10": 1.6449924946442456e-06, "11": 2.2952929742997323e-07, "12": 2.9422555443777825e-08, "13": 3.4864506869251232e-09, "14": 3.815831659608956e-10, "15": 3.502302837194834e-11, "2": 0.13286398592074425, "3": 0.059971365341202516, "4": 0.021371221385131027, "5": 0.0062637231072312245, "6": 0.0015554200120275483, "7": 0.0003346152460564331, "8": 6.344549592724611e-05, "9": 1.0748290003525657e-05} |
| Unadjusted home-win probability | 43.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 72.1% |
| P draw away | 54.5% |
| P home away | 73.3% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.34, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.82, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.73, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.89, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.10 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-24T14:49:26Z |
| Market reference home last update utc | 2026-10-24T14:49:26Z |
| Market reference draw last update utc | 2026-10-24T14:49:26Z |
| Market reference away last update utc | 2026-10-24T14:49:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market best over 2 5 last update utc | 2026-10-24T14:49:25Z |
| Market best under 2 5 last update utc | 2026-10-24T14:49:25Z |
| Home probability edge | -1.9% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | -0.0389 |
| Raw ev home | -0.0994 |
| Raw edge prob draw | -0.0098 |
| Raw ev draw | -0.1172 |
| Raw edge prob away | 0.0487 |
| Raw ev away | 0.1906 |
| Market p home draw | 75.4% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:49:20Z |
| Market reference home draw last update utc | 2026-10-24T14:49:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.1% |
| Market draw away odds | 1.82 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:49:20Z |
| Market reference draw away last update utc | 2026-10-24T14:49:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:49:20Z |
| Market reference home away last update utc | 2026-10-24T14:49:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.82 |
| Market reference dc home draw odds | 1.28 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 78.6% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:49:25Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.16 |
| Market reference over 1 5 last update utc | 2026-10-24T14:49:25Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 68.8% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.97 |
| Market reference under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.8% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:49:20Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.31 |
| Market reference btts yes last update utc | 2026-10-24T14:49:20Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,571.2203 |
| Elo away rating | 1,580.6829 |
| Elo rating diff | 50.5374 |
| Elo home expectancy | 0.5722 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **38.7%**. Expected goals are 1.19 for Angers and 1.30 for Lorient (2.49 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.0%; Double Chance 1X: 61.3%; Double Chance X2: 67.7%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 32.3% | 3.10 |
| Draw | 29.0% | 3.45 |
| Lorient win | 38.7% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.19 |
| Lorient expected goals | 1.30 |
| Expected total goals | 2.49 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.81% |
| 2 | 0-1 | 10.14% |
| 3 | 0-0 | 9.19% |
| 4 | 1-0 | 8.91% |
| 5 | 1-2 | 8.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 32.3% | 31.4% | 2.98 | -3.8% |
| Draw | 29.0% | 29.5% | 3.34 | -3.1% |
| Lorient win | 38.7% | 39.0% | 2.51 | -2.9% |

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
| Market best home last update utc | 2026-10-24T14:49:25Z |
| Market best draw last update utc | 2026-10-24T14:49:25Z |
| Market best away last update utc | 2026-10-24T14:49:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1900 |
| Dc lambda away | 1.2992 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:49:18.960151+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.88 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.17 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.36 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21015520256495251, "-10": 3.635053110735803e-07, "-11": 4.244117458720834e-08, "-12": 4.549385785706337e-09, "-13": 4.4857871209661433e-10, "-14": 3.748856487409084e-11, "-2": 0.11487047985998056, "-3": 0.04441698442744451, "-4": 0.013437271653895263, "-5": 0.003326095377239773, "-6": 0.0006952969423863105, "-7": 0.0001256511238712391, "-8": 1.9983976707421428e-05, "-9": 2.83676312923546e-06, "0": 0.2900706132702222, "1": 0.18522613104736602, "10": 1.4582834241210604e-07, "11": 1.5594879588196258e-08, "12": 1.5311257123153592e-09, "13": 1.3828026251838036e-10, "14": 1.0584827948702733e-11, "2": 0.09303192246722997, "3": 0.03294853297675119, "4": 0.00912980626827967, "5": 0.0020698964316207655, "6": 0.00039632155118515333, "7": 6.560050750956154e-05, "8": 9.556221090921073e-06, "9": 1.242483986091601e-06} |
| Raw goal margin distribution | {"-1": 0.2083095252862545, "-10": 3.603128443387765e-07, "-11": 4.20684371500152e-08, "-12": 4.5094310385755126e-09, "-13": 4.4463909258437104e-10, "-14": 3.715932347747245e-11, "-2": 0.11386163576721928, "-3": 0.04402689454175311, "-4": 0.013319259505366027, "-5": 0.0032968841153265373, "-6": 0.0006891905326812547, "-7": 0.00012454759932584823, "-8": 1.9808468457819476e-05, "-9": 2.8118494026715893e-06, "0": 0.28482703016803096, "1": 0.19018426528837515, "10": 1.497318763991015e-07, "11": 1.6012323423110012e-08, "12": 1.5721108950139004e-09, "13": 1.4198174945530066e-10, "14": 1.0868162689815652e-11, "2": 0.09552220155303415, "3": 0.03383049951472996, "4": 0.009374192979898463, "5": 0.002125303432322719, "6": 0.0004069302889602703, "7": 6.735650230722625e-05, "8": 9.812022077194617e-06, "9": 1.2757428052469333e-06} |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 51.3% |
| P home draw | 61.3% |
| P draw away | 67.7% |
| P home away | 71.0% |
| Raw p home draw | 61.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.8, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.94, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.25, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.68, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.71, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.71, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.15 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.54 |
| Market reference 1x2 last update utc | 2026-10-24T14:49:26Z |
| Market reference home last update utc | 2026-10-24T14:49:26Z |
| Market reference draw last update utc | 2026-10-24T14:49:26Z |
| Market reference away last update utc | 2026-10-24T14:49:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | 0.0173 |
| Raw ev home | -0.0121 |
| Raw edge prob draw | -0.0105 |
| Raw ev draw | -0.0487 |
| Raw edge prob away | -0.0068 |
| Raw ev away | -0.0370 |
| Market p home draw | 61.5% |
| Market home draw odds | 1.57 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:49:21Z |
| Market reference home draw last update utc | 2026-10-24T14:49:21Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.5% |
| Market draw away odds | 1.43 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:49:21Z |
| Market reference draw away last update utc | 2026-10-24T14:49:21Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.0% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:49:21Z |
| Market reference home away last update utc | 2026-10-24T14:49:21Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.43 |
| Market reference dc home draw odds | 1.57 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 74.1% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:49:25Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.51 |
| Market reference over 1 5 last update utc | 2026-10-24T14:49:25Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.7% |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.64 |
| Market reference under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.1% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:49:21Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.09 |
| Market reference btts yes last update utc | 2026-10-24T14:49:21Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,396.7330 |
| Elo away rating | 1,477.6040 |
| Elo rating diff | -20.8710 |
| Elo home expectancy | 0.4700 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **44.3%**. Expected goals are 1.73 for Auxerre and 1.52 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 62.5%; Under 3.5 goals: 59.3%; Double Chance 1X: 69.7%; Double Chance X2: 55.7%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 44.3% | 2.26 |
| Draw | 25.4% | 3.94 |
| Le Mans FC win | 30.3% | 3.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.73 |
| Le Mans FC expected goals | 1.52 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 62.5% |
| Under 2.5 | 37.5% |
| Over 3.5 | 40.7% |
| Under 3.5 | 59.3% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.30% |
| 2 | 2-1 | 9.23% |
| 3 | 1-2 | 7.04% |
| 4 | 2-2 | 7.00% |
| 5 | 1-0 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 44.3% | 46.2% | 2.07 | -8.4% |
| Draw | 25.4% | 26.5% | 3.71 | -5.8% |
| Le Mans FC win | 30.3% | 27.3% | 3.56 | +8.0% |

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
| Market best home last update utc | 2026-10-24T14:49:25Z |
| Market best draw last update utc | 2026-10-24T14:49:25Z |
| Market best away last update utc | 2026-10-24T14:49:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7263 |
| Dc lambda away | 1.5160 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:49:18.960151+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.30 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.25 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.46 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.44 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.15727391234714383, "-10": 7.93847518336218e-07, "-11": 1.0731692431114754e-07, "-12": 1.3337492212812575e-08, "-13": 1.5335777729518699e-09, "-14": 1.639472085045646e-10, "-15": 1.6219209790086996e-11, "-16": 1.3207782683475962e-12, "-2": 0.09026166790828719, "-3": 0.03818417531714796, "-4": 0.012911253829207192, "-5": 0.0036170287116659592, "-6": 0.00086250744199196, "-7": 0.00017873252006501644, "-8": 3.2714588936929646e-05, "-9": 5.3584961306083185e-06, "0": 0.25402330510921267, "1": 0.207124535168521, "10": 3.3506317747184872e-06, "11": 5.157703463704277e-07, "12": 7.298958114671767e-08, "13": 9.556327805195865e-09, "14": 1.1632894792392436e-09, "15": 1.3104245052814854e-10, "16": 1.2150964998881727e-11, "2": 0.1348045776813781, "3": 0.06493565742790983, "4": 0.025001541495698897, "5": 0.007975333706182024, "6": 0.0021655005555842543, "7": 0.0005109725476360638, "8": 0.00010649617204840031, "9": 1.9862503739451957e-05} |
| Raw goal margin distribution | {"-1": 0.17317561572638268, "-10": 8.74112118971726e-07, "-11": 1.1816755982024179e-07, "-12": 1.4686023840377856e-08, "-13": 1.6886352678061155e-09, "-14": 1.8052363774566725e-10, "-15": 1.7859107083150643e-11, "-16": 1.4543199596526997e-12, "-2": 0.09938787484351519, "-3": 0.04204491369780137, "-4": 0.01421668920359364, "-5": 0.003982740461496075, "-6": 0.0009497141331733235, "-7": 0.00019680386753696323, "-8": 3.602230654683134e-05, "-9": 5.900284751213458e-06, "0": 0.24286204470573994, "1": 0.1979964448845442, "10": 3.2029676202854674e-06, "11": 4.930400682619616e-07, "12": 6.977289083064859e-08, "13": 9.13517527047499e-09, "14": 1.1120226827476709e-09, "15": 1.252673388617239e-10, "16": 1.1615465399778261e-11, "2": 0.12886366703664054, "3": 0.06207390788592977, "4": 0.023899710040407276, "5": 0.007623856436453251, "6": 0.0020700657749326418, "7": 0.000488453711112613, "8": 0.00010180282814993459, "9": 1.898715245742238e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.7% |
| P home draw | 69.7% |
| P draw away | 55.7% |
| P home away | 74.6% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.7% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.33, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.8, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.57, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.12, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 6.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:17Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.54, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.14 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-24T14:49:26Z |
| Market reference home last update utc | 2026-10-24T14:49:26Z |
| Market reference draw last update utc | 2026-10-24T14:49:26Z |
| Market reference away last update utc | 2026-10-24T14:49:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | -2.0% |
| Draw probability edge | -1.1% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +8.2% |
| Under 2.5 probability edge | -8.2% |
| Raw edge prob home | -0.0390 |
| Raw ev home | -0.1241 |
| Raw edge prob draw | -0.0223 |
| Raw ev draw | -0.0990 |
| Raw edge prob away | 0.0613 |
| Raw ev away | 0.1890 |
| Market p home draw | 72.8% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:49:21Z |
| Market reference home draw last update utc | 2026-10-24T14:49:21Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.2% |
| Market draw away odds | 1.82 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:49:21Z |
| Market reference draw away last update utc | 2026-10-24T14:49:21Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.9% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:49:21Z |
| Market reference home away last update utc | 2026-10-24T14:49:21Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.82 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 79.5% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-24T14:49:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.8% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.81 |
| Market reference under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.0% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:49:21Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.37 |
| Market reference btts yes last update utc | 2026-10-24T14:49:21Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,465.3899 |
| Elo away rating | 1,405.6473 |
| Elo rating diff | 119.7426 |
| Elo home expectancy | 0.6658 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **65.4%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.7%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.7%; Double Chance 1X: 85.4%; Double Chance X2: 34.6%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 65.4% | 1.53 |
| Draw | 20.1% | 4.98 |
| Le Havre win | 14.6% | 6.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.73% |
| 2 | 1-0 | 10.60% |
| 3 | 1-1 | 9.57% |
| 4 | 2-1 | 9.50% |
| 5 | 3-0 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 65.4% | 63.9% | 1.55 | +1.3% |
| Draw | 20.1% | 19.7% | 4.91 | -1.5% |
| Le Havre win | 14.6% | 16.4% | 5.36 | -22.0% |

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
| Market best home last update utc | 2026-10-24T14:49:25Z |
| Market best draw last update utc | 2026-10-24T14:49:25Z |
| Market best away last update utc | 2026-10-24T14:49:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1120 |
| Dc lambda away | 0.8101 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:49:18.960151+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.22 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 3.00 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.85 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.10086243847587409, "-10": 2.4151496135230172e-09, "-11": 1.7560237341858005e-10, "-12": 1.172648097157936e-11, "-13": 7.239446474839066e-13, "-14": 4.1551656388511215e-14, "-15": 2.2278048718699454e-15, "-16": 1.116062341385962e-16, "-17": 4.831776061304876e-18, "-2": 0.034573920746734134, "-3": 0.008247839012057348, "-4": 0.001545000769346376, "-5": 0.0002372883613053851, "-6": 3.0816991354713765e-05, "-7": 3.462807049800831e-06, "-8": 3.426388991373163e-07, "-9": 3.0272653898593485e-08, "0": 0.20068531037583542, "1": 0.23230646178880593, "10": 2.987660450543942e-05, "11": 5.6637927480093405e-06, "12": 9.861306283781302e-07, "13": 1.5873104637950205e-07, "14": 2.375388402002444e-08, "15": 3.320574383075158e-09, "16": 4.337248356447039e-10, "17": 4.895785793175135e-11, "2": 0.20027080626535315, "3": 0.12456584046294761, "4": 0.060838326636276696, "5": 0.024362102742329365, "6": 0.008249323650289334, "7": 0.0024168303851741756, "8": 0.0006235112853647067, "9": 0.0001436309130331196} |
| Raw goal margin distribution | {"-1": 0.08794511426481338, "-10": 2.105844474290665e-09, "-11": 1.5311320079935848e-10, "-12": 1.0224685468182352e-11, "-13": 6.312299772486783e-13, "-14": 3.623018860340133e-14, "-15": 1.942492735421766e-15, "-16": 9.731296568178968e-17, "-17": 4.2129766465549924e-18, "-2": 0.030146082690450098, "-3": 0.00719154876001408, "-4": 0.0013471344858660389, "-5": 0.00020689914267444607, "-6": 2.687029846731634e-05, "-7": 3.019329755195036e-06, "-8": 2.9875757111909345e-07, "-9": 2.6395673616871472e-08, "0": 0.2041012961084015, "1": 0.23771362572569577, "10": 3.05720121888701e-05, "11": 5.795623157104444e-06, "12": 1.0090837995029023e-06, "13": 1.6242566934882918e-07, "14": 2.4306779294848555e-08, "15": 3.397864054295097e-09, "16": 4.4382021255231477e-10, "17": 5.0097400765805645e-11, "2": 0.20493230845909907, "3": 0.127465234285802, "4": 0.06225439919506529, "5": 0.02492915491281477, "6": 0.008441334862556552, "7": 0.0024730845160307415, "8": 0.0006380241306403275, "9": 0.0001469740653810784} |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 85.4% |
| P draw away | 34.6% |
| P home away | 79.9% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.31, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.31, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.56 |
| Reference draw odds | 5.00 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-24T14:49:26Z |
| Market reference home last update utc | 2026-10-24T14:49:26Z |
| Market reference draw last update utc | 2026-10-24T14:49:26Z |
| Market reference away last update utc | 2026-10-24T14:49:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | +1.5% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | 0.0304 |
| Raw ev home | 0.0370 |
| Raw edge prob draw | 0.0068 |
| Raw ev draw | 0.0021 |
| Raw edge prob away | -0.0373 |
| Raw ev away | -0.3200 |
| Market p home draw | 82.2% |
| Market home draw odds | 1.18 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:49:21Z |
| Market reference home draw last update utc | 2026-10-24T14:49:21Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 37.6% |
| Market draw away odds | 2.58 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:49:21Z |
| Market reference draw away last update utc | 2026-10-24T14:49:21Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.2% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:49:21Z |
| Market reference home away last update utc | 2026-10-24T14:49:21Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.58 |
| Market reference dc home draw odds | 1.18 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 83.1% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-24T14:49:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.0% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market reference under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:49:21Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-24T14:49:21Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,561.8610 |
| Elo away rating | 1,427.2190 |
| Elo rating diff | 194.6420 |
| Elo home expectancy | 0.7541 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **52.7%**. Expected goals are 1.90 for Rennes and 1.25 for Strasbourg (3.15 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.2%; Double Chance 1X: 75.5%; Double Chance X2: 47.3%; Double Chance 12 (either team wins): 77.1%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 52.7% | 1.90 |
| Draw | 22.9% | 4.37 |
| Strasbourg win | 24.5% | 4.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.90 |
| Strasbourg expected goals | 1.25 |
| Expected total goals | 3.15 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 38.8% |
| Under 3.5 | 61.2% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.45% |
| 2 | 2-1 | 9.78% |
| 3 | 2-0 | 7.81% |
| 4 | 1-0 | 7.63% |
| 5 | 1-2 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 52.7% | 53.3% | 1.81 | -4.7% |
| Draw | 22.9% | 22.2% | 4.39 | +0.4% |
| Strasbourg win | 24.5% | 24.5% | 3.91 | -4.3% |

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
| Market best home last update utc | 2026-10-24T14:49:25Z |
| Market best draw last update utc | 2026-10-24T14:49:25Z |
| Market best away last update utc | 2026-10-24T14:49:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9030 |
| Dc lambda away | 1.2517 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:49:18.960151+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.22 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.58 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.71 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.14215279414529494, "-10": 1.3754190206612486e-07, "-11": 1.5377090646145705e-08, "-12": 1.580081529721145e-09, "-13": 1.501852959258222e-10, "-14": 1.3271809852297565e-11, "-15": 1.0868767706481546e-12, "-16": 7.400721381193055e-14, "-2": 0.06925483594033893, "-3": 0.02451375363226177, "-4": 0.006905824405727047, "-5": 0.0016076887248121722, "-6": 0.0003180546833208829, "-7": 5.462000618037321e-05, "-8": 8.278711710158421e-06, "-9": 1.1222601729937314e-06, "0": 0.22864193903038957, "1": 0.22163939765349946, "10": 9.181953291518333e-06, "11": 1.5607412067733147e-06, "12": 2.4383322779884946e-07, "13": 3.523688223312327e-08, "14": 4.734312053023352e-09, "15": 5.894727117562034e-10, "16": 6.102588999344907e-11, "2": 0.16191862451914724, "3": 0.08713912348952, "4": 0.037322916268892566, "5": 0.013210482318071823, "6": 0.003973517884537823, "7": 0.001037484915850272, "8": 0.00023908342826461647, "9": 4.927616889615439e-05} |
| Raw goal margin distribution | {"-1": 0.14208846712039608, "-10": 1.3747966156348798e-07, "-11": 1.537013220049e-08, "-12": 1.5793665107549986e-09, "-13": 1.5011733403081653e-10, "-14": 1.3265804088936003e-11, "-15": 1.0863849368470125e-12, "-16": 7.397372404541419e-14, "-2": 0.06922349672127762, "-3": 0.02450266066114046, "-4": 0.006902699380002683, "-5": 0.001606961213029851, "-6": 0.00031791075712051377, "-7": 5.4595289518849495e-05, "-8": 8.274965425060671e-06, "-9": 1.1217523274847832e-06, "0": 0.23493569481005674, "1": 0.2190367700256922, "10": 9.074133086416074e-06, "11": 1.5424140130180068e-06, "12": 2.40969986416833e-07, "13": 3.4823108850824645e-08, "14": 4.678718816990819e-09, "15": 5.825507566268468e-10, "16": 6.030928604582067e-11, "2": 0.16001727534525664, "3": 0.08611588171636157, "4": 0.03688464737780119, "5": 0.013055356620106227, "6": 0.003926858366711252, "7": 0.0010253021228359782, "8": 0.00023627596198226737, "9": 4.8697537479901736e-05} |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 61.3% |
| Raw p btts yes | 61.3% |
| P home draw | 75.5% |
| P draw away | 47.3% |
| P home away | 77.1% |
| Raw p home draw | 75.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.86 |
| Reference draw odds | 4.40 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-24T14:49:26Z |
| Market reference home last update utc | 2026-10-24T14:49:26Z |
| Market reference draw last update utc | 2026-10-24T14:49:26Z |
| Market reference away last update utc | 2026-10-24T14:49:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:05Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:05Z |
| Home probability edge | -0.6% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | -0.0124 |
| Raw ev home | -0.0582 |
| Raw edge prob draw | 0.0126 |
| Raw ev draw | 0.0314 |
| Raw edge prob away | -0.0002 |
| Raw ev away | -0.0432 |
| Market p home draw | 76.6% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:49:21Z |
| Market reference home draw last update utc | 2026-10-24T14:49:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.2% |
| Market draw away odds | 2.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:49:21Z |
| Market reference draw away last update utc | 2026-10-24T14:49:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.2% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:49:21Z |
| Market reference home away last update utc | 2026-10-24T14:49:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.09 |
| Market reference dc home draw odds | 1.26 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 86.3% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-24T14:49:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.1% |
| Market under 3 5 odds | 1.79 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.09 |
| Market reference under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.9% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:49:21Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.83 |
| Market reference btts yes last update utc | 2026-10-24T14:49:21Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,575.6733 |
| Elo away rating | 1,512.5539 |
| Elo rating diff | 123.1194 |
| Elo home expectancy | 0.6701 |

</details>


---

## 2026-10-25 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **60.2%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.8%; Double Chance 1X: 82.5%; Double Chance X2: 39.8%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 60.2% | 1.66 |
| Draw | 22.2% | 4.49 |
| Troyes win | 17.5% | 5.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
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
| 1 | 2-0 | 10.88% |
| 2 | 1-0 | 10.82% |
| 3 | 1-1 | 10.61% |
| 4 | 2-1 | 9.91% |
| 5 | 3-0 | 6.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 60.2% | 60.3% | 1.62 | -2.4% |
| Draw | 22.2% | 21.5% | 4.41 | -1.9% |
| Troyes win | 17.5% | 18.2% | 5.23 | -8.4% |

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
| Market best home last update utc | 2026-10-24T14:49:25Z |
| Market best draw last update utc | 2026-10-24T14:49:25Z |
| Market best away last update utc | 2026-10-24T14:49:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9074 |
| Dc lambda away | 0.9105 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:49:18.960151+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.75 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.11599762061395176, "-10": 7.83978031449946e-09, "-11": 6.405724913326888e-10, "-12": 4.8072406881974014e-11, "-13": 3.3352707749183194e-12, "-14": 2.1510058848965274e-13, "-15": 1.2899056868499348e-14, "-16": 6.621524077222653e-16, "-2": 0.04429150085056352, "-3": 0.01185671157126717, "-4": 0.002493713464049843, "-5": 0.00043015651273321017, "-6": 6.275644147500994e-05, "-7": 7.922657074142375e-06, "-8": 8.808312992057037e-07, "-9": 8.744763787892609e-08, "0": 0.22249056704732728, "1": 0.24043774950868677, "10": 1.2290764991501808e-05, "11": 2.1038598676170323e-06, "12": 3.3076374074834005e-07, "13": 4.807581211732729e-08, "14": 6.495470774080835e-09, "15": 8.160194213398603e-10, "16": 8.775543098339516e-11, "2": 0.18715756786765414, "3": 0.10496022533440605, "4": 0.04624667912982169, "5": 0.016712214772750967, "6": 0.0051078639162121815, "7": 0.0013509067454205875, "8": 0.00031464494112215383, "9": 6.544095089976366e-05} |
| Raw goal margin distribution | {"-1": 0.11153907824280886, "-10": 7.538446610173079e-09, "-11": 6.159511277281677e-10, "-12": 4.622467188679322e-11, "-13": 3.2070746447692546e-12, "-14": 2.0683287504205859e-13, "-15": 1.2403262288476131e-14, "-16": 6.367015876937298e-16, "-2": 0.04258909064440107, "-3": 0.011400981094701201, "-4": 0.0023978638502206214, "-5": 0.00041362280257525006, "-6": 6.034430360616791e-05, "-7": 7.618137877368002e-06, "-8": 8.469752282919082e-07, "-9": 8.408645687645422e-08, "0": 0.23000140625631568, "1": 0.24012680094745548, "10": 1.2274869834862099e-05, "11": 2.1011390294782434e-06, "12": 3.303359771816648e-07, "13": 4.801363758508992e-08, "14": 6.487070440539835e-09, "15": 8.149640959364205e-10, "16": 8.764194038110713e-11, "2": 0.18691552444239778, "3": 0.10482448445710647, "4": 0.0461868701423955, "5": 0.01669060153128122, "6": 0.005101258119331462, "7": 0.001349159671553424, "8": 0.00031423802335678395, "9": 6.535631872545048e-05} |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.5% |
| P draw away | 39.8% |
| P home away | 77.8% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.63, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.09, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.63, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.64 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-24T14:49:26Z |
| Market reference home last update utc | 2026-10-24T14:49:26Z |
| Market reference draw last update utc | 2026-10-24T14:49:26Z |
| Market reference away last update utc | 2026-10-24T14:49:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -6.7% |
| Under 2.5 probability edge | +6.7% |
| Raw edge prob home | -0.0016 |
| Raw ev home | -0.0254 |
| Raw edge prob draw | 0.0150 |
| Raw ev draw | 0.0143 |
| Raw edge prob away | -0.0135 |
| Raw ev away | -0.1192 |
| Market p home draw | 82.1% |
| Market home draw odds | 1.17 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:49:20Z |
| Market reference home draw last update utc | 2026-10-24T14:49:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.4% |
| Market draw away odds | 2.44 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:49:20Z |
| Market reference draw away last update utc | 2026-10-24T14:49:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.5% |
| Market home away odds | 1.25 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:49:20Z |
| Market reference home away last update utc | 2026-10-24T14:49:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.38 |
| Market reference dc home draw odds | 1.17 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.85 |
| Market reference over 1 5 last update utc | 2026-10-24T14:49:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-10-24T14:49:25Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.3% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:49:20Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.23 |
| Market reference btts yes last update utc | 2026-10-24T14:49:20Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,462.4520 |
| Elo away rating | 1,403.0456 |
| Elo rating diff | 119.4065 |
| Elo home expectancy | 0.6654 |

</details>


---

## 2026-10-26 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **67.4%**. Expected goals are 2.42 for Paris Saint Germain and 1.10 for Lyon (3.52 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 68.6%; Under 3.5 goals: 53.1%; Double Chance 1X: 85.5%; Double Chance X2: 32.6%; Double Chance 12 (either team wins): 82.0%; Under 4.5 goals: 72.0%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 67.4% | 1.48 |
| Draw | 18.0% | 5.55 |
| Lyon win | 14.5% | 6.88 |

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
| Over 2.5 | 68.6% |
| Under 2.5 | 31.4% |
| Over 3.5 | 46.9% |
| Under 3.5 | 53.1% |
| Over 4.5 | 28.0% |
| Under 4.5 | 72.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.72% |
| 2 | 2-0 | 8.87% |
| 3 | 1-1 | 7.98% |
| 4 | 3-1 | 7.85% |
| 5 | 3-0 | 7.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 67.4% | 68.7% | 1.43 | -3.6% |
| Draw | 18.0% | 17.3% | 5.30 | -4.5% |
| Lyon win | 14.5% | 14.0% | 6.35 | -7.6% |

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
| Market best home last update utc | 2026-10-24T14:49:25Z |
| Market best draw last update utc | 2026-10-24T14:49:25Z |
| Market best away last update utc | 2026-10-24T14:49:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4230 |
| Dc lambda away | 1.0959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:49:18.960151+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.56 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.79 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.18 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.88 |
| Fair Over 4.5 odds | 3.57 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.09174001552994783, "-10": 2.5019136916895177e-08, "-11": 2.444272883506359e-09, "-12": 2.1954319436642568e-10, "-13": 1.8244907863566593e-11, "-14": 1.4105664212501458e-12, "-15": 1.0193879994343414e-13, "-16": 6.912206709473552e-15, "-17": 4.378931730172065e-16, "-18": 2.3233428238136634e-17, "-2": 0.03842939555902786, "-3": 0.011726835362052252, "-4": 0.00286218041809309, "-5": 0.0005790150599419841, "-6": 9.972968057978545e-05, "-7": 1.4930210453320372e-05, "-8": 1.9745072884633953e-06, "-9": 2.3369771420273334e-07, "0": 0.18015642213615035, "1": 0.21970835136497233, "10": 7.373006319021143e-05, "11": 1.5925501306012978e-05, "12": 3.162529178216479e-06, "13": 5.810685586897927e-07, "14": 9.932312681301554e-08, "15": 1.5869655479416272e-08, "16": 2.3791172129261784e-09, "17": 3.332256595163511e-10, "18": 3.908901250867938e-11, "2": 0.19836576275714088, "3": 0.13383050932393825, "4": 0.07221749979652153, "5": 0.032300291548556584, "6": 0.012300199365139977, "7": 0.004071222068701972, "8": 0.0011903885575990317, "9": 0.000311498247015293} |
| Raw goal margin distribution | {"-1": 0.0950341036404683, "-10": 2.5917493440788764e-08, "-11": 2.5320388403564256e-09, "-12": 2.2742628248375913e-10, "-13": 1.8900023667981258e-11, "-14": 1.4612153125817883e-12, "-15": 1.055990935127629e-13, "-16": 7.16040176162834e-15, "-17": 4.536165047234583e-16, "-18": 2.406766572200639e-17, "-2": 0.03980927122477981, "-3": 0.012147908202698947, "-4": 0.002964952086823918, "-5": 0.0005998056235117553, "-6": 0.00010331065179682902, "-7": 1.5466306163112312e-05, "-8": 2.0454054777158273e-06, "-9": 2.420890454812824e-07, "0": 0.18776106179915428, "1": 0.21552931851857632, "10": 7.232765698250697e-05, "11": 1.5622585223671644e-05, "12": 3.102375282238726e-06, "13": 5.700161586436115e-07, "14": 9.743391956722978e-08, "15": 1.5567801630450375e-08, "16": 2.333864454364768e-09, "17": 3.2688743446605465e-10, "18": 3.8345507465780045e-11, "2": 0.19459268343169722, "3": 0.13128494339146451, "4": 0.07084386378378336, "5": 0.03168591354020608, "6": 0.012066239495864226, "7": 0.003993784089470062, "8": 0.0011677463919677555, "9": 0.000305573295151678} |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 61.1% |
| P home draw | 85.5% |
| P draw away | 32.6% |
| P home away | 82.0% |
| Raw p home draw | 84.9% |
| Raw p draw away | 33.8% |
| Raw p home away | 81.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.13, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:49:25Z", "line": -1.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.45 |
| Reference draw odds | 5.70 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-24T14:49:26Z |
| Market reference home last update utc | 2026-10-24T14:49:26Z |
| Market reference draw last update utc | 2026-10-24T14:49:26Z |
| Market reference away last update utc | 2026-10-24T14:49:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:05Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:05Z |
| Home probability edge | -1.3% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0257 |
| Raw ev home | -0.0540 |
| Raw edge prob draw | 0.0152 |
| Raw ev draw | -0.0049 |
| Raw edge prob away | 0.0104 |
| Raw ev away | -0.0432 |
| Elo home rating | 1,650.2164 |
| Elo away rating | 1,562.6863 |
| Elo rating diff | 147.5301 |
| Elo home expectancy | 0.7004 |

</details>


---
