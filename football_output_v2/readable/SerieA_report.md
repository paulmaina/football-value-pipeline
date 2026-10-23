# Serie A — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,970 |
| Training data through | 2026-10-19 |
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
| Training sha256 | b853f76a1c7d175b2be57ae97c26e1d88d1296ed6336164803055513fb1f3834 |
| Training as of utc | 2026-10-23T16:22:31.141591+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 63, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-23T16:22:31.141591+00:00', 'observations': 197, 'observations_sha256': '0ac0924301e6c2ff0d91137e29e8d1d6e1e231a34d06293ffc91e3341806c9fa', 'eligible_training_matches': 91, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 99, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 91, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '61cdfe0f2d468f2f694a0c7982174b928d742c55131fd6b385eb7a1580d75240', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2436.651 |
| Base scoring parameter | 0.132 |
| Home-advantage parameter | 0.126 |
| Dixon-Coles low-score adjustment | -0.034 |
| Xi per day | 0.0009 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1970, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-19'} |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 24.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261023T162231141591Z_674b78702eed8c976099888fba494115d79c96af68c020bc3c5fa08fd6ac44a5.json |
| Over 1 5 in window quote fixtures | 5 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **47.4%**. Expected goals are 1.51 for Torino and 1.00 for Monza (2.51 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 45.6%; Under 3.5 goals: 75.6%; Double Chance 1X: 74.5%; Double Chance X2: 52.6%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 49.8%; BTTS No (at least one team does not score): 50.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 47.4% | 2.11 |
| Draw | 27.2% | 3.68 |
| Monza win | 25.5% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.51 |
| Monza expected goals | 1.00 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.6% |
| Under 2.5 | 54.4% |
| Over 3.5 | 24.4% |
| Under 3.5 | 75.6% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.90% |
| 2 | 1-0 | 11.53% |
| 3 | 2-0 | 9.03% |
| 4 | 2-1 | 9.00% |
| 5 | 0-0 | 8.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 47.4% | 45.9% | 2.14 | +1.4% |
| Draw | 27.2% | 27.7% | 3.48 | -5.4% |
| Monza win | 25.5% | 26.4% | 3.67 | -6.6% |
| Over 2.5 | 45.6% | 54.5% | 1.83 | -16.5% |
| Under 2.5 | 54.4% | 45.5% | 2.10 | +14.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 124c70f8f3248a845bdb983a54e74720 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5140 |
| Dc lambda away | 0.9959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.8% |
| P btts no | 50.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.50 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.15 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.16149095435079713, "-10": 2.5618991129876134e-08, "-11": 2.293445990904626e-09, "-12": 1.8852422040142953e-10, "-13": 1.4322055591545197e-11, "-14": 1.0072596827863675e-12, "-15": 6.076582174258563e-14, "-2": 0.06739018752453765, "-3": 0.020023649568757632, "-4": 0.004650890379278793, "-5": 0.0008834425440994015, "-6": 0.00014167789511430298, "-7": 1.963816499703979e-05, "-8": 2.3953027777032995e-06, "-9": 2.607374876726577e-07, "0": 0.2717364370099831, "1": 0.230966897186452, "10": 1.5748478060442428e-06, "11": 2.1432686286240497e-07, "12": 2.6783465344691394e-08, "13": 3.093260473122127e-09, "14": 3.307227811031547e-10, "15": 3.033147701835309e-11, "2": 0.14520482353043715, "3": 0.06559022762819425, "4": 0.02316026524317179, "5": 0.006688015312673445, "6": 0.0016305441718113846, "7": 0.00034359188695979925, "8": 6.371092896580704e-05, "9": 1.0543104703436561e-05} |
| Raw goal margin distribution | {"-1": 0.15525828137707762, "-10": 2.463023733700246e-08, "-11": 2.204931442819499e-09, "-12": 1.812482103108883e-10, "-13": 1.376930210035195e-11, "-14": 9.683849344906656e-13, "-15": 5.842059134610056e-14, "-2": 0.06478929261889672, "-3": 0.019250845543887427, "-4": 0.004471391292861264, "-5": 0.0008493464642875157, "-6": 0.00013620989852339654, "-7": 1.888023858114521e-05, "-8": 2.302857111340854e-06, "-9": 2.506744380164966e-07, "0": 0.26678189892271537, "1": 0.23817434633315665, "10": 1.623991798599593e-06, "11": 2.2101505057965391e-07, "12": 2.7619258121907232e-08, "13": 3.1897873686605023e-09, "14": 3.410431675113137e-10, "15": 3.1277987452606977e-11, "2": 0.14973601996681216, "3": 0.06763700678100665, "4": 0.023882994067075926, "5": 0.006896718511468044, "6": 0.0016814262001147709, "7": 0.000354313860899138, "8": 6.569906356952768e-05, "9": 1.0872108088441377e-05} |
| Unadjusted home-win probability | 48.8% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 71.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 49.6% |
| P home draw | 74.5% |
| P draw away | 52.6% |
| P home away | 72.8% |
| Raw p home draw | 75.5% |
| Raw p draw away | 51.2% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.5, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.41, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.84, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.64, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.73, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.73, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 2.10 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.55 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market best over 2 5 last update utc | 2026-10-23T16:22:25Z |
| Market best under 2 5 last update utc | 2026-10-23T16:22:25Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | 0.0296 |
| Raw ev home | 0.0453 |
| Raw edge prob draw | -0.0099 |
| Raw ev draw | -0.0716 |
| Raw edge prob away | -0.0197 |
| Raw ev away | -0.1017 |
| Market p home draw | 72.6% |
| Market home draw odds | 1.32 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:22:25Z |
| Market reference home draw last update utc | 2026-10-23T16:22:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.3% |
| Market draw away odds | 1.77 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:22:25Z |
| Market reference draw away last update utc | 2026-10-23T16:22:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.1% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:22:25Z |
| Market reference home away last update utc | 2026-10-23T16:22:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home draw odds | 1.31 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 78.9% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-10-23T16:22:27Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 68.3% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-23T16:22:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:22:25Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.31 |
| Market reference btts yes last update utc | 2026-10-23T16:22:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,443.9623 |
| Elo away rating | 1,369.6129 |
| Elo rating diff | 134.3494 |
| Elo home expectancy | 0.6843 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **41.6%**. Expected goals are 1.04 for Cagliari and 1.43 for Bologna (2.47 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 43.9%; Under 3.5 goals: 76.7%; Double Chance 1X: 58.4%; Double Chance X2: 71.2%; Double Chance 12 (either team wins): 70.4%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 28.8% | 3.47 |
| Draw | 29.6% | 3.38 |
| Bologna win | 41.6% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.04 |
| Bologna expected goals | 1.43 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 43.9% |
| Under 2.5 | 56.1% |
| Over 3.5 | 23.3% |
| Under 3.5 | 76.7% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.03% |
| 2 | 0-1 | 10.69% |
| 3 | 0-0 | 9.60% |
| 4 | 1-0 | 8.95% |
| 5 | 1-2 | 8.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 28.8% | 30.6% | 3.22 | -7.2% |
| Draw | 29.6% | 31.7% | 3.01 | -11.0% |
| Bologna win | 41.6% | 37.7% | 2.57 | +6.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | b7f0880e3da978f9481f7cb5697e2aa5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0400 |
| Dc lambda away | 1.4266 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.41 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.29 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.83 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.21204459712644733, "-10": 8.540483420480753e-07, "-11": 1.0954072275262946e-07, "-12": 1.2898429921824307e-08, "-13": 1.3974954081754666e-09, "-14": 1.2875780549373542e-10, "-2": 0.1260666765298328, "-3": 0.05374281365820426, "-4": 0.017899864698119775, "-5": 0.004874101862860968, "-6": 0.0011203117424508516, "-7": 0.00022253813980005764, "-8": 3.8894998978837393e-05, "-9": 6.0665274940037145e-06, "0": 0.2957764941654436, "1": 0.17870342765128636, "10": 4.215530274168533e-08, "11": 3.94176098650698e-09, "12": 3.3837359007107137e-10, "13": 2.672729002542281e-11, "14": 1.7952421190897456e-12, "2": 0.07798492414951544, "3": 0.024236822158369434, "4": 0.0058850472034618915, "5": 0.0011682605983967553, "6": 0.00019576224753918196, "7": 2.8349110319157105e-05, "8": 3.6122156591100237e-06, "9": 4.107381122805749e-07} |
| Raw goal margin distribution | {"-1": 0.23183255948397197, "-10": 9.33747974450762e-07, "-11": 1.1976304262222035e-07, "-12": 1.4102109002654778e-08, "-13": 1.527909419692578e-09, "-14": 1.4077345994980332e-10, "-2": 0.13783119533161567, "-3": 0.05875808303109869, "-4": 0.019570276741865268, "-5": 0.005328952141981824, "-6": 0.0012248590258465736, "-7": 0.0002433053576077868, "-8": 4.252467304796838e-05, "-9": 6.632654711197789e-06, "0": 0.2744340621202966, "1": 0.16786478679591388, "10": 3.95985180589751e-08, "11": 3.7026870513733118e-09, "12": 3.178507055023435e-10, "13": 2.5106238311808124e-11, "14": 1.6863578921166575e-12, "2": 0.0732550171964186, "3": 0.022766821194746576, "4": 0.005528109936541046, "5": 0.0010974037759064017, "6": 0.00018388896272307823, "7": 2.6629692682030077e-05, "8": 3.3931291606817765e-06, "9": 3.8582620687879426e-07} |
| Unadjusted home-win probability | 27.1% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 49.6% |
| P home draw | 58.4% |
| P draw away | 71.2% |
| P home away | 70.4% |
| Raw p home draw | 54.5% |
| Raw p draw away | 72.9% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.96, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.41, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.1, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.18, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.72, "price": 2.18, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 3.15 |
| Reference draw odds | 3.04 |
| Reference away odds | 2.57 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 2.30 |
| Reference Under 2.5 odds | 1.67 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:31Z |
| Home probability edge | -1.7% |
| Draw probability edge | -2.1% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | -0.0350 |
| Raw ev home | -0.1283 |
| Raw edge prob draw | -0.0427 |
| Raw ev draw | -0.1740 |
| Raw edge prob away | 0.0776 |
| Raw ev away | 0.1689 |
| Market p home draw | 61.7% |
| Market home draw odds | 1.55 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:22:26Z |
| Market reference home draw last update utc | 2026-10-23T16:22:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.9% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:22:26Z |
| Market reference draw away last update utc | 2026-10-23T16:22:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.4% |
| Market home away odds | 1.42 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:22:26Z |
| Market reference home away last update utc | 2026-10-23T16:22:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home draw odds | 1.54 |
| Market reference dc home away odds | 1.37 |
| Market p over 1 5 | 70.5% |
| Market over 1 5 odds | 1.37 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 2.85 |
| Market reference over 1 5 last update utc | 2026-10-23T16:22:27Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.2% |
| Market reference under 3 5 odds | 1.23 |
| Market reference under 3 5 opposite odds | 3.60 |
| Market reference under 3 5 last update utc | 2026-10-23T16:22:27Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 53.0% |
| Market btts yes odds | 1.82 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:22:26Z |
| Market reference btts yes odds | 1.82 |
| Market reference btts yes opposite odds | 2.04 |
| Market reference btts yes last update utc | 2026-10-23T16:22:26Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,429.1686 |
| Elo away rating | 1,493.4486 |
| Elo rating diff | -4.2800 |
| Elo home expectancy | 0.4938 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **65.0%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.5%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 59.8%; Under 3.5 goals: 62.8%; Double Chance 1X: 84.9%; Double Chance X2: 35.0%; Double Chance 12 (either team wins): 80.1%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 65.0% | 1.54 |
| Draw | 19.9% | 5.02 |
| Sassuolo win | 15.1% | 6.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 59.8% |
| Under 2.5 | 40.2% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.54% |
| 2 | 2-1 | 10.14% |
| 3 | 1-0 | 9.64% |
| 4 | 1-1 | 9.37% |
| 5 | 3-0 | 7.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 65.0% | 66.4% | 1.50 | -2.5% |
| Draw | 19.9% | 19.3% | 4.81 | -4.1% |
| Sassuolo win | 15.1% | 14.3% | 6.17 | -7.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | 08ffd99b2249c81d8a7410598f32b9b0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1168 |
| Dc lambda away | 0.9623 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.03 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.46 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.00 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.09931826523534233, "-10": 9.867210168703032e-09, "-11": 8.502240390187184e-10, "-12": 6.730969310822599e-11, "-13": 4.92770226853802e-12, "-14": 3.3546985595848775e-13, "-15": 2.133573728614411e-14, "-16": 1.2660844564751056e-15, "-17": 6.399752453560892e-17, "-2": 0.03804524405120708, "-3": 0.010566278770685137, "-4": 0.0023200136784374166, "-5": 0.0004193010473421526, "-6": 6.423800872055058e-05, "-7": 8.528766910971098e-06, "-8": 9.982474913365627e-07, "-9": 1.044110199737918e-07, "0": 0.19931061757785512, "1": 0.23869281137971549, "10": 2.8144393214378447e-05, "11": 5.334796119432e-06, "12": 9.290711889851288e-07, "13": 1.4962452252426562e-07, "14": 2.2407776046483794e-08, "15": 3.135016592037874e-09, "16": 4.0924351021661006e-10, "17": 4.550605999401377e-11, "2": 0.1978802278201782, "3": 0.12089574819591231, "4": 0.058393760427105694, "5": 0.02321607408554975, "6": 0.00782423415909419, "7": 0.0022851933425377157, "8": 0.0005883853728061899, "9": 0.00013538074947108} |
| Raw goal margin distribution | {"-1": 0.10438329878268549, "-10": 1.0370418218146307e-08, "-11": 8.935837701838069e-10, "-12": 7.074235328253216e-11, "-13": 5.17900526141976e-12, "-14": 3.5257814989138937e-13, "-15": 2.2423817357373195e-14, "-16": 1.3306522399600529e-15, "-17": 6.726127071514274e-17, "-2": 0.03998547565895418, "-3": 0.011105137925315794, "-4": 0.002438329751354475, "-5": 0.00044068456492768113, "-6": 6.751401911413858e-05, "-7": 8.963717022304361e-06, "-8": 1.0491561235019539e-06, "-9": 1.0973577386096886e-07, "0": 0.20601714967610352, "1": 0.23340656951951094, "10": 2.7521089694343962e-05, "11": 5.216648352856259e-06, "12": 9.084953912393381e-07, "13": 1.4631084328227694e-07, "14": 2.1911519275924526e-08, "15": 3.0655865331874524e-09, "16": 4.0018014478796883e-10, "17": 4.449825402850166e-11, "2": 0.193497847229982, "3": 0.11821831454745059, "4": 0.05710053530247693, "5": 0.02270191623575423, "6": 0.007650953724309548, "7": 0.0022345840064787147, "8": 0.0005753546184668304, "9": 0.0001323825218295219} |
| Unadjusted home-win probability | 63.6% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 54.7% |
| P home draw | 84.9% |
| P draw away | 35.0% |
| P home away | 80.1% |
| Raw p home draw | 84.2% |
| Raw p draw away | 36.4% |
| Raw p home away | 79.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.7, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.71, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:50Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:27Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.91, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:27Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.2, "price": 4.91, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 1.48 |
| Reference draw odds | 4.85 |
| Reference away odds | 6.45 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.85 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:27Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:27Z |
| Home probability edge | -1.4% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.0288 |
| Raw ev home | -0.0467 |
| Raw edge prob draw | 0.0134 |
| Raw ev draw | -0.0091 |
| Raw edge prob away | 0.0154 |
| Raw ev away | -0.0225 |
| Market p home draw | 84.3% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:22:27Z |
| Market reference home draw last update utc | 2026-10-23T16:22:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.5% |
| Market draw away odds | 2.73 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:22:27Z |
| Market reference draw away last update utc | 2026-10-23T16:22:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.1% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:22:27Z |
| Market reference home away last update utc | 2026-10-23T16:22:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.73 |
| Market reference dc home draw odds | 1.15 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-10-23T16:22:27Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.2% |
| Market under 3 5 odds | 1.79 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference under 3 5 odds | 1.71 |
| Market reference under 3 5 opposite odds | 1.98 |
| Market reference under 3 5 last update utc | 2026-10-23T16:22:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.9% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:22:27Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.43 |
| Market reference btts yes last update utc | 2026-10-23T16:22:27Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,552.1056 |
| Elo away rating | 1,423.0825 |
| Elo rating diff | 189.0231 |
| Elo home expectancy | 0.7480 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **64.5%**. Expected goals are 1.60 for Lazio and 0.71 for Parma (2.31 combined). The most likely exact score is 1-0 at 17.1%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 42.1%; Under 3.5 goals: 79.1%; Double Chance 1X: 86.8%; Double Chance X2: 35.5%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 64.5% | 1.55 |
| Draw | 22.3% | 4.48 |
| Parma win | 13.2% | 7.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.60 |
| Parma expected goals | 0.71 |
| Expected total goals | 2.31 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 68.4% |
| Under 1.5 | 31.6% |
| Over 2.5 | 42.1% |
| Under 2.5 | 57.9% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.11% |
| 2 | 2-0 | 14.05% |
| 3 | 1-1 | 10.16% |
| 4 | 2-1 | 9.93% |
| 5 | 0-0 | 9.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 64.5% | 70.4% | 1.42 | -8.5% |
| Draw | 22.3% | 19.1% | 4.67 | +4.3% |
| Parma win | 13.2% | 10.5% | 8.22 | +8.6% |
| Over 2.5 | 42.1% | 52.4% | 1.93 | -18.7% |
| Under 2.5 | 57.9% | 47.6% | 1.95 | +12.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | b27cb3ea731fa3f18d05e6a627bdf984 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6029 |
| Dc lambda away | 0.7067 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.10 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.79 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.21 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.09497650049580819, "-10": 7.82499292944348e-10, "-11": 4.984978932729447e-11, "-12": 2.914843201166711e-12, "-13": 1.574778317347443e-13, "-14": 7.887684018538158e-15, "-15": 3.45538596803271e-16, "-2": 0.029550987456257376, "-3": 0.006389639082812259, "-4": 0.0010704659878608466, "-5": 0.00014593854583318252, "-6": 1.6747113640389153e-05, "-7": 1.657803191795872e-06, "-8": 1.4421246733684898e-07, "-9": 1.1185087740599484e-08, "0": 0.223309921113469, "1": 0.29100111341126056, "10": 3.7372308837412947e-06, "11": 5.399676649798018e-07, "12": 7.160742801088769e-08, "13": 8.774063132516182e-09, "14": 9.967110749603978e-10, "15": 9.902726758120132e-11, "2": 0.2016184930576113, "3": 0.09887196050315691, "4": 0.03756714074039597, "5": 0.011615655805263645, "6": 0.0030230973904153842, "7": 0.0006787089772119296, "8": 0.00013390348508513745, "9": 2.355412196302075e-05} |
| Raw goal margin distribution | {"-1": 0.11440024437860626, "-10": 9.425290453070642e-10, "-11": 6.004462210645697e-11, "-12": 3.5109608460832686e-12, "-13": 1.8968378852264512e-13, "-14": 9.50080256264883e-15, "-15": 4.162050582004709e-16, "-2": 0.035594490942253414, "-3": 0.00769639088352258, "-4": 0.0012893881114905035, "-5": 0.00017578459114011433, "-6": 2.0172083442697145e-05, "-7": 1.9968422639603534e-06, "-8": 1.7370551051736675e-07, "-9": 1.3472561783608865e-08, "0": 0.25552226362324676, "1": 0.26425546316648046, "10": 3.393745359136882e-06, "11": 4.903397232109662e-07, "12": 6.502605379531617e-08, "13": 7.967646892327265e-09, "14": 9.051042577441512e-10, "15": 8.992576060627792e-11, "2": 0.18308791894747858, "3": 0.08978472766189997, "4": 0.03411437866962316, "5": 0.010548071341790215, "6": 0.0027452472320014247, "7": 0.0006163294463925801, "8": 0.0001215965363705363, "9": 2.1389283827313917e-05} |
| Unadjusted home-win probability | 58.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 15.9% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 79.7% |
| Raw p btts yes | 40.9% |
| P home draw | 86.8% |
| P draw away | 35.5% |
| P home away | 77.7% |
| Raw p home draw | 84.1% |
| Raw p draw away | 41.5% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.26, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.74, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:27Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.48, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:27Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.14, "price": 6.48, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 1.40 |
| Reference draw odds | 4.88 |
| Reference away odds | 8.65 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market best over 2 5 last update utc | 2026-10-23T16:22:25Z |
| Market best under 2 5 last update utc | 2026-10-23T16:22:25Z |
| Home probability edge | -5.9% |
| Draw probability edge | +3.2% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | -0.1185 |
| Raw ev home | -0.1689 |
| Raw edge prob draw | 0.0644 |
| Raw ev draw | 0.1933 |
| Raw edge prob away | 0.0541 |
| Raw ev away | 0.3084 |
| Market p home draw | 88.4% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:22:27Z |
| Market reference home draw last update utc | 2026-10-23T16:22:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 32.0% |
| Market draw away odds | 3.04 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:22:27Z |
| Market reference draw away last update utc | 2026-10-23T16:22:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.7% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:22:27Z |
| Market reference home away last update utc | 2026-10-23T16:22:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.04 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 76.2% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-23T16:22:27Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.9% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.00 |
| Market reference under 3 5 last update utc | 2026-10-23T16:22:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 43.4% |
| Market btts yes odds | 2.20 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:22:27Z |
| Market reference btts yes odds | 2.20 |
| Market reference btts yes opposite odds | 1.71 |
| Market reference btts yes last update utc | 2026-10-23T16:22:27Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,525.7636 |
| Elo away rating | 1,403.2770 |
| Elo rating diff | 182.4866 |
| Elo home expectancy | 0.7409 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.5%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.26 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.6%; Under 3.5 goals: 80.7%; Double Chance 1X: 65.3%; Double Chance X2: 63.5%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.5% | 2.74 |
| Draw | 28.8% | 3.48 |
| AS Roma win | 34.7% | 2.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.20 |
| AS Roma expected goals | 1.06 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 39.6% |
| Under 2.5 | 60.4% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.40% |
| 2 | 0-1 | 11.56% |
| 3 | 1-0 | 11.36% |
| 4 | 0-0 | 10.60% |
| 5 | 1-2 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 36.5% | 34.3% | 2.80 | +2.3% |
| Draw | 28.8% | 28.1% | 3.44 | -1.0% |
| AS Roma win | 34.7% | 37.6% | 2.60 | -9.8% |
| Over 2.5 | 39.6% | 52.4% | 1.92 | -24.0% |
| Under 2.5 | 60.4% | 47.6% | 1.97 | +19.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:00:00+00:00 |
| Fixture id | 0b4894e9fb123ef3045269f97e339eba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2023 |
| Dc lambda away | 1.0610 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.43 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.51 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.21062793001372493, "-10": 6.350607842078145e-08, "-11": 6.066648002252619e-09, "-12": 5.29948589556004e-10, "-13": 3.9388274222413394e-11, "-2": 0.09581086696356883, "-3": 0.030800905094184643, "-4": 0.0076986476304456, "-5": 0.0015689207709024878, "-6": 0.0002694427107973128, "-7": 3.9946915906822905e-05, "-8": 5.207165829332574e-06, "-9": 6.054053733275224e-07, "0": 0.2877374845033336, "1": 0.20652600594594134, "10": 1.9130708785424533e-07, "11": 2.0708920497912914e-08, "12": 2.0499124005059388e-09, "13": 1.7264794489085638e-10, "2": 0.10616646308000055, "3": 0.03867487832219647, "4": 0.010954002053612237, "5": 0.002529602528340651, "6": 0.0004922782085247686, "7": 8.270282143437329e-05, "8": 1.2216066197781114e-05, "9": 1.60941905303968e-06} |
| Raw goal margin distribution | {"-1": 0.19293261069072073, "-10": 5.8170791991606306e-08, "-11": 5.556975454964468e-09, "-12": 4.8542643375094e-10, "-13": 3.607917798858418e-11, "-2": 0.08776158363526688, "-3": 0.028213252777402012, "-4": 0.007051867176556376, "-5": 0.0014371122589363662, "-6": 0.0002468062313593597, "-7": 3.659088694668279e-05, "-8": 4.769700284701946e-06, "-9": 5.545439258442993e-07, "0": 0.2944155301094043, "1": 0.21921872372654577, "10": 2.0306447823441283e-07, "11": 2.1981653596183286e-08, "12": 2.1758963387291658e-09, "13": 1.8325857782235548e-10, "2": 0.1126912634191507, "3": 0.041051766954184755, "4": 0.011627215366375641, "5": 0.0026850673611701565, "6": 0.0005225327439849758, "7": 8.778558845598019e-05, "8": 1.296684370847487e-05, "9": 1.708331060451993e-06} |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.8% |
| Raw p over 1 5 | 66.5% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 46.2% |
| P home draw | 65.3% |
| P draw away | 63.5% |
| P home away | 71.2% |
| Raw p home draw | 68.2% |
| Raw p draw away | 61.2% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.87, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.36, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.87, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 2.82 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.58 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market best over 2 5 last update utc | 2026-10-23T16:22:25Z |
| Market best under 2 5 last update utc | 2026-10-23T16:22:25Z |
| Home probability edge | +2.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -12.8% |
| Under 2.5 probability edge | +12.8% |
| Raw edge prob home | 0.0449 |
| Raw ev home | 0.0861 |
| Raw edge prob draw | 0.0134 |
| Raw ev draw | 0.0128 |
| Raw edge prob away | -0.0583 |
| Raw ev away | -0.1740 |
| Market p home draw | 62.8% |
| Market home draw odds | 1.54 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:22:25Z |
| Market reference home draw last update utc | 2026-10-23T16:22:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.9% |
| Market draw away odds | 1.47 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:22:25Z |
| Market reference draw away last update utc | 2026-10-23T16:22:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.3% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:22:25Z |
| Market reference home away last update utc | 2026-10-23T16:22:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.44 |
| Market reference dc home draw odds | 1.51 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 76.8% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.45 |
| Market reference over 1 5 last update utc | 2026-10-23T16:22:27Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-10-23T16:22:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.6% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:22:25Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-23T16:22:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,562.3912 |
| Elo away rating | 1,591.2548 |
| Elo rating diff | 31.1364 |
| Elo home expectancy | 0.5447 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **57.6%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.35 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.5%; Double Chance 1X: 79.0%; Double Chance X2: 42.4%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 57.6% | 1.74 |
| Draw | 21.4% | 4.68 |
| Frosinone win | 21.0% | 4.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.35 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.64% |
| 2 | 2-1 | 8.95% |
| 3 | 2-0 | 8.09% |
| 4 | 1-0 | 6.93% |
| 5 | 3-1 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 57.6% | 52.3% | 1.85 | +6.5% |
| Draw | 21.4% | 22.8% | 4.18 | -10.6% |
| Frosinone win | 21.0% | 24.8% | 3.93 | -17.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 63aa6e3f679ee4c68de5b4bd8d3361bb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2476 |
| Dc lambda away | 1.1073 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.63 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.52 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.14 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.13211846239984681, "-10": 4.0613988509822724e-08, "-11": 4.013734399809655e-09, "-12": 3.6461759141596596e-10, "-13": 3.0641960008541936e-11, "-14": 2.395348880939105e-12, "-15": 1.7494309207055113e-13, "-16": 1.1893761940381274e-14, "-17": 6.757542612237204e-16, "-2": 0.05565167425564242, "-3": 0.01731997202267849, "-4": 0.004298507049921486, "-5": 0.000882635493322598, "-6": 0.0001541292766418032, "-7": 2.3375349545726608e-05, "-8": 3.1300082629759757e-06, "-9": 3.749417122285574e-07, "0": 0.2138299684689954, "1": 0.20466624022215305, "10": 3.631660836274807e-05, "11": 7.285339184611575e-06, "12": 1.3434152310710892e-06, "13": 2.2917154669946507e-07, "14": 3.63650706736679e-08, "15": 5.3911816063787695e-09, "16": 7.440085209498177e-10, "17": 8.580625847657512e-11, "2": 0.17263777882941572, "3": 0.10906271277181946, "4": 0.05494374496188096, "5": 0.022900950413147353, "6": 0.008117620859208025, "7": 0.0024990401951670723, "8": 0.0006792538616766536, "9": 0.00016516647300434162} |
| Raw goal margin distribution | {"-1": 0.1084913084788521, "-10": 3.335086312646067e-08, "-11": 3.2959458429364404e-09, "-12": 2.99411897993535e-10, "-13": 2.516216337442955e-11, "-14": 1.966981220005017e-12, "-15": 1.4365747695904457e-13, "-16": 9.76676364687568e-15, "-17": 5.549070332687013e-16, "-2": 0.045699312945080825, "-3": 0.014222587770289395, "-4": 0.0035297917178310515, "-5": 0.0007247910537335835, "-6": 0.0001265658606225771, "-7": 1.9195063371925537e-05, "-8": 2.570259188849569e-06, "-9": 3.0788972429809767e-07, "0": 0.1992315418651158, "1": 0.2232353931788502, "10": 3.961157608592679e-05, "11": 7.946330354985497e-06, "12": 1.4653018836183691e-06, "13": 2.4996404036801595e-07, "14": 3.966443533140273e-08, "15": 5.880317849647403e-09, "16": 8.11511632413668e-10, "17": 9.359137016164797e-11, "2": 0.18830102313247338, "3": 0.11895785812228861, "4": 0.05992873321936542, "5": 0.024978729584806948, "6": 0.008854124071537977, "7": 0.0027257754866280457, "8": 0.0007408818509347264, "9": 0.00018015185357910933} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 60.2% |
| P home draw | 79.0% |
| P draw away | 42.4% |
| P home away | 78.6% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 1.87 |
| Reference draw odds | 4.17 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.92 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:27Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:27Z |
| Home probability edge | +5.2% |
| Draw probability edge | -1.5% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | 0.1045 |
| Raw ev home | 0.1617 |
| Raw edge prob draw | -0.0292 |
| Raw ev draw | -0.1672 |
| Raw edge prob away | -0.0753 |
| Raw ev away | -0.3208 |
| Market p home draw | 75.2% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:22:25Z |
| Market reference home draw last update utc | 2026-10-23T16:22:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.8% |
| Market draw away odds | 2.04 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:22:25Z |
| Market reference draw away last update utc | 2026-10-23T16:22:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:22:25Z |
| Market reference home away last update utc | 2026-10-23T16:22:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.00 |
| Market reference dc home draw odds | 1.27 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 88.5% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-23T16:22:27Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.8% |
| Market under 3 5 odds | 1.83 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market reference under 3 5 last update utc | 2026-10-23T16:22:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.2% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:22:25Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.92 |
| Market reference btts yes last update utc | 2026-10-23T16:22:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,513.0173 |
| Elo away rating | 1,441.1854 |
| Elo rating diff | 131.8319 |
| Elo home expectancy | 0.6811 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **47.1%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.6%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 38.9%; Under 3.5 goals: 80.9%; Double Chance 1X: 76.2%; Double Chance X2: 52.9%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 44.1%; BTTS No (at least one team does not score): 55.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 47.1% | 2.12 |
| Draw | 29.0% | 3.44 |
| Venezia win | 23.8% | 4.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.63% |
| 2 | 1-1 | 13.38% |
| 3 | 0-0 | 11.22% |
| 4 | 2-0 | 9.81% |
| 5 | 0-1 | 9.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 47.1% | 45.1% | 2.21 | +4.2% |
| Draw | 29.0% | 29.9% | 3.20 | -7.1% |
| Venezia win | 23.8% | 25.0% | 3.72 | -11.4% |
| Over 2.5 | 38.9% | 48.2% | 2.03 | -21.0% |
| Under 2.5 | 61.1% | 51.8% | 1.87 | +14.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 95cfaecfe96bb7ced1fb6af974a4110b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3977 |
| Dc lambda away | 0.8591 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.1% |
| P btts no | 55.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.92 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.86 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.15939699344375124, "-10": 7.399402205910573e-09, "-11": 5.726948685726586e-10, "-12": 4.068323058976924e-11, "-13": 2.662518555733473e-12, "-14": 1.5047067338716467e-13, "-2": 0.05949733124856724, "-3": 0.015564910781993476, "-4": 0.0031601821611567894, "-5": 0.0005226097629689135, "-6": 7.278758887430913e-05, "-7": 8.748161445783573e-06, "-8": 9.241874523314774e-07, "-9": 8.706554190962733e-08, "0": 0.29041859475872367, "1": 0.239245568197968, "10": 8.779401110637352e-07, "11": 1.1055684324267118e-07, "12": 1.2778263850098965e-08, "13": 1.3606397158720343e-09, "14": 1.2511127387333954e-10, "2": 0.14375173427406795, "3": 0.061186600385738324, "4": 0.020212307028197152, "5": 0.0054384528695666816, "6": 0.0012323931202410127, "7": 0.00024099209788213982, "8": 4.142286773116696e-05, "9": 6.349221569388902e-06} |
| Raw goal margin distribution | {"-1": 0.1516502193118976, "-10": 7.03978753337814e-09, "-11": 5.448616096293549e-10, "-12": 3.870600510060543e-11, "-13": 2.5331188134452656e-12, "-14": 1.431577229041329e-13, "-2": 0.0566057309951824, "-3": 0.014808448281632032, "-4": 0.0030065957170898015, "-5": 0.000497210665373949, "-6": 6.925007540916038e-05, "-7": 8.322996395142947e-06, "-8": 8.792714768539871e-07, "-9": 8.283411273854114e-08, "0": 0.2820096895625707, "1": 0.24939019472641036, "10": 9.151670265220441e-07, "11": 1.1524473733119361e-07, "12": 1.3320095054821155e-08, "13": 1.418334334256213e-09, "14": 1.3041631319967921e-10, "2": 0.14984717699432598, "3": 0.06378106938315249, "4": 0.021069360755978647, "5": 0.005669057238416004, "6": 0.0012846497536041087, "7": 0.0002512107817546752, "8": 4.317930370628203e-05, "9": 6.618444870171149e-06} |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 66.3% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.8% |
| P home draw | 76.2% |
| P draw away | 52.9% |
| P home away | 71.0% |
| Raw p home draw | 77.3% |
| Raw p draw away | 50.9% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.83, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.69, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.83, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 2.16 |
| Reference draw odds | 3.22 |
| Reference away odds | 3.83 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market best over 2 5 last update utc | 2026-10-23T16:22:25Z |
| Market best under 2 5 last update utc | 2026-10-23T16:22:25Z |
| Home probability edge | +2.0% |
| Draw probability edge | -0.8% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | 0.0400 |
| Raw ev home | 0.0859 |
| Raw edge prob draw | -0.0168 |
| Raw ev draw | -0.0976 |
| Raw edge prob away | -0.0232 |
| Raw ev away | -0.1569 |
| Market p home draw | 72.7% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:22:25Z |
| Market reference home draw last update utc | 2026-10-23T16:22:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.7% |
| Market draw away odds | 1.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:22:25Z |
| Market reference draw away last update utc | 2026-10-23T16:22:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.6% |
| Market home away odds | 1.38 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:22:25Z |
| Market reference home away last update utc | 2026-10-23T16:22:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.71 |
| Market reference dc home draw odds | 1.31 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 74.7% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.20 |
| Market reference over 1 5 last update utc | 2026-10-23T16:22:27Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.7% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-23T16:22:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.9% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:22:25Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-23T16:22:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,396.1582 |
| Elo away rating | 1,364.9563 |
| Elo rating diff | 91.2019 |
| Elo home expectancy | 0.6283 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **71.3%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.34 combined). The most likely exact score is 2-0 at 10.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.4%; Under 3.5 goals: 56.8%; Double Chance 1X: 88.0%; Double Chance X2: 28.7%; Double Chance 12 (either team wins): 83.2%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 71.3% | 1.40 |
| Draw | 16.8% | 5.96 |
| Fiorentina win | 12.0% | 8.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.4% |
| Under 2.5 | 34.6% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.47% |
| 2 | 2-1 | 9.82% |
| 3 | 1-0 | 8.43% |
| 4 | 3-0 | 8.40% |
| 5 | 3-1 | 7.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 71.3% | 73.0% | 1.35 | -3.8% |
| Draw | 16.8% | 15.7% | 5.77 | -3.2% |
| Fiorentina win | 12.0% | 11.3% | 8.07 | -3.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T11:30:00+00:00 |
| Fixture id | c9b6c7048d8dc33dae618f67f462f67a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4051 |
| Dc lambda away | 0.9382 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.98 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.72 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.89 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.03 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.08028443599173513, "-10": 5.964908329241342e-09, "-11": 5.003428853795869e-10, "-12": 3.8569126066876856e-11, "-13": 2.749896153605134e-12, "-14": 1.8234940863392603e-13, "-15": 1.1300375962202082e-14, "-16": 6.570549661301415e-16, "-17": 3.576458233733775e-17, "-18": 1.6565419954759265e-18, "-2": 0.029402598616771653, "-3": 0.007858586144130139, "-4": 0.0016677097924784592, "-5": 0.0002920553191036666, "-6": 4.342449660003924e-05, "-7": 5.601377355999931e-06, "-8": 6.374329806532209e-07, "-9": 6.485787763594135e-08, "0": 0.16772421509184507, "1": 0.22732491408423255, "10": 7.919756741178338e-05, "11": 1.7029263168459402e-05, "12": 3.365022608775226e-06, "13": 6.150133477742575e-07, "14": 1.045424483503922e-07, "15": 1.660738524225226e-08, "16": 2.4753130380698325e-09, "17": 3.4538354654610114e-10, "18": 4.10082273994882e-11, "2": 0.20937908887256024, "3": 0.14345380375446737, "4": 0.0780383698412536, "5": 0.03503264191472209, "6": 0.013352501088021607, "7": 0.0044151221218915815, "8": 0.0012879603073444438, "9": 0.0003359315097882522} |
| Raw goal margin distribution | {"-1": 0.08487203099930742, "-10": 6.305753766265659e-09, "-11": 5.289333649001504e-10, "-12": 4.077303430893071e-11, "-13": 2.907030095069452e-12, "-14": 1.9276917712764596e-13, "-15": 1.1946099478939808e-14, "-16": 6.946002517771566e-16, "-17": 3.78082339785546e-17, "-18": 1.7511997419544782e-18, "-2": 0.03108271522913521, "-3": 0.008307639688768596, "-4": 0.001763005686676946, "-5": 0.00030874387781749805, "-6": 4.5905849322367456e-05, "-7": 5.9214499887149325e-06, "-8": 6.73857031262578e-07, "-9": 6.856397174956267e-08, "0": 0.17835669752045955, "1": 0.22175468255592126, "10": 7.725695835562331e-05, "11": 1.6611988454040224e-05, "12": 3.2825681400057596e-06, "13": 5.99943434500981e-07, "14": 1.0198080373614448e-07, "15": 1.6200447968122567e-08, "16": 2.414659471862006e-09, "17": 3.3692047804311166e-10, "18": 4.000338671978977e-11, "2": 0.20424859093789535, "3": 0.13993869893743346, "4": 0.07612616505781004, "5": 0.034174223349825526, "6": 0.013025319516912558, "7": 0.0043069366528954624, "8": 0.0012564009107860659, "9": 0.0003277000482490987} |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 55.6% |
| P home draw | 88.0% |
| P draw away | 28.7% |
| P home away | 83.2% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.51, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.28, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.9, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:21:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.7, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 6.7, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 1.35 |
| Reference draw odds | 5.85 |
| Reference away odds | 8.03 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:27Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:27Z |
| Home probability edge | -1.7% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.0349 |
| Raw ev home | -0.0614 |
| Raw edge prob draw | 0.0213 |
| Raw ev draw | 0.0291 |
| Raw edge prob away | 0.0137 |
| Raw ev away | 0.0199 |
| Market p home draw | 87.4% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:22:25Z |
| Market reference home draw last update utc | 2026-10-23T16:22:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 29.8% |
| Market draw away odds | 3.41 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:22:25Z |
| Market reference draw away last update utc | 2026-10-23T16:22:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.8% |
| Market home away odds | 1.17 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:22:25Z |
| Market reference home away last update utc | 2026-10-23T16:22:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.19 |
| Market reference dc home draw odds | 1.09 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-10-23T16:22:27Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.9% |
| Market under 3 5 odds | 1.80 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:22:25Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 1.97 |
| Market reference under 3 5 last update utc | 2026-10-23T16:22:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:22:25Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-23T16:22:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,671.4331 |
| Elo away rating | 1,448.7633 |
| Elo rating diff | 282.6699 |
| Elo home expectancy | 0.8358 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **62.3%**. Expected goals are 0.62 for Lecce and 1.48 for Juventus (2.11 combined). The most likely exact score is 0-1 at 19.1%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 36.4%; Under 3.5 goals: 83.3%; Double Chance 1X: 37.7%; Double Chance X2: 86.6%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 35.5%; BTTS No (at least one team does not score): 64.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.4% | 7.49 |
| Draw | 24.3% | 4.11 |
| Juventus win | 62.3% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.11 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 63.3% |
| Under 1.5 | 36.7% |
| Over 2.5 | 36.4% |
| Under 2.5 | 63.6% |
| Over 3.5 | 16.7% |
| Under 3.5 | 83.3% |
| Over 4.5 | 6.6% |
| Under 4.5 | 93.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.06% |
| 2 | 0-2 | 14.44% |
| 3 | 0-0 | 11.27% |
| 4 | 1-1 | 10.45% |
| 5 | 1-2 | 9.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.4% | 11.5% | 7.83 | +4.5% |
| Draw | 24.3% | 21.6% | 4.26 | +3.6% |
| Juventus win | 62.3% | 66.9% | 1.48 | -7.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:00:00+00:00 |
| Fixture id | 63af660d4d0d52f8ac7685172ef939c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6239 |
| Dc lambda away | 1.4832 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.5% |
| P btts no | 64.5% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.88 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.73 |
| Fair Over 2.5 odds | 2.75 |
| Fair Under 2.5 odds | 1.57 |
| Fair Over 3.5 odds | 5.98 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.23 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.29574652672436613, "-10": 2.026964791476143e-06, "-11": 2.71416071814931e-07, "-12": 3.335005892298421e-08, "-13": 3.785668764869937e-09, "-14": 3.9864312473571987e-10, "-15": 3.712733521573362e-11, "-2": 0.1944308226238205, "-3": 0.08951993454720625, "-4": 0.03176717585277618, "-5": 0.00914722517012883, "-6": 0.002213207666575667, "-7": 0.00046141677550710035, "-8": 8.447169603105164e-05, "-9": 1.378037568583394e-05, "0": 0.24311188676720102, "1": 0.09920270743629016, "10": 2.857138266531296e-10, "11": 1.6092536761187697e-11, "12": 8.317435680751544e-13, "13": 3.9713608821587175e-14, "14": 1.7590772690658414e-15, "15": 6.89125489333359e-17, "2": 0.027965268636560275, "3": 0.005415986014972119, "4": 0.0008084260172249949, "5": 9.791628797036757e-05, "6": 9.96532881733444e-06, "7": 8.739100698405142e-07, "8": 6.729587962655465e-08, "9": 4.617875437623164e-09} |
| Raw goal margin distribution | {"-1": 0.27390942340190716, "-10": 1.8772993327716903e-06, "-11": 2.5137546180593355e-07, "-12": 3.0887583063749375e-08, "-13": 3.506145482285061e-09, "-14": 3.692084219851615e-10, "-15": 3.438595575077997e-11, "-2": 0.18007458990747113, "-3": 0.08291003085102855, "-4": 0.029421575689544774, "-5": 0.008471819432092673, "-6": 0.0020497905504919525, "-7": 0.0004273470404773626, "-8": 7.82345402663363e-05, "-9": 1.2762870963101166e-05, "0": 0.2705432293651893, "1": 0.11302246023829916, "10": 3.2551611187803735e-10, "11": 1.833435944671957e-11, "12": 9.476122857998348e-13, "13": 4.524604106031905e-14, "14": 2.0041311959834645e-15, "15": 7.851263360669697e-17, "2": 0.031861060491306166, "3": 0.006170477397721133, "4": 0.0009210464083966482, "5": 0.00011155683196368391, "6": 1.1353581057675197e-05, "7": 9.956529279589636e-07, "8": 7.667074897303908e-08, "9": 5.261183454789997e-09} |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 57.7% |
| Raw p over 1 5 | 62.6% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 37.7% |
| P draw away | 86.6% |
| P home away | 75.7% |
| Raw p home draw | 42.3% |
| Raw p draw away | 84.8% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 7.98 |
| Reference draw odds | 4.36 |
| Reference away odds | 1.47 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:31Z |
| Home probability edge | +1.9% |
| Draw probability edge | +2.7% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -15.4% |
| Under 2.5 probability edge | +15.4% |
| Raw edge prob home | 0.0372 |
| Raw ev home | 0.1909 |
| Raw edge prob draw | 0.0549 |
| Raw ev draw | 0.1525 |
| Raw edge prob away | -0.0921 |
| Raw ev away | -0.1455 |
| Elo home rating | 1,374.5856 |
| Elo away rating | 1,557.5355 |
| Elo rating diff | -122.9499 |
| Elo home expectancy | 0.3301 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **55.3%**. Expected goals are 1.04 for Udinese and 1.69 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.9%; Under 3.5 goals: 70.3%; Double Chance 1X: 44.7%; Double Chance X2: 79.7%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 85.6%; BTTS Yes (both teams score): 53.0%; BTTS No (at least one team does not score): 47.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 20.3% | 4.91 |
| Draw | 24.3% | 4.11 |
| AC Milan win | 55.3% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.69 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.4% |
| Under 4.5 | 85.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.59% |
| 2 | 0-1 | 11.21% |
| 3 | 1-2 | 10.28% |
| 4 | 0-2 | 9.84% |
| 5 | 0-0 | 6.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 20.3% | 17.7% | 5.19 | +5.6% |
| Draw | 24.3% | 23.8% | 4.02 | -2.1% |
| AC Milan win | 55.3% | 58.5% | 1.68 | -7.1% |
| Over 2.5 | 51.9% | 50.6% | 1.90 | -1.4% |
| Under 2.5 | 48.1% | 49.4% | 1.99 | -4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 3564688383b255192409c9deb8e526ed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0448 |
| Dc lambda away | 1.6924 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.0% |
| P btts no | 47.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.89 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.24 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.93 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.25006105143441393, "-10": 4.279440479819788e-06, "-11": 6.497973561203983e-07, "-12": 9.062410085875576e-08, "-13": 1.1682364744591062e-08, "-14": 1.392457155947716e-09, "-15": 1.405383112538254e-10, "-2": 0.17075801739466895, "-3": 0.08479909914095318, "-4": 0.03310797676059754, "-5": 0.010605714287973477, "-6": 0.0028741102643336748, "-7": 0.0006740877546913622, "-8": 0.0001392471471282475, "-9": 2.5687614151906136e-05, "0": 0.2434895584109881, "1": 0.12753350720160067, "10": 2.8717759467019433e-08, "11": 2.691974610752235e-09, "12": 2.3177478484866706e-10, "13": 1.844517134163287e-11, "14": 1.3572605621639435e-12, "15": 8.456790571083768e-14, "2": 0.05431365335565198, "3": 0.016651317712277812, "4": 0.004013464878185592, "5": 0.0007936996792051197, "6": 0.00013278504451919222, "7": 1.9226119268233156e-05, "8": 2.4518333989188497e-06, "9": 2.7922729943834536e-07} |
| Raw goal margin distribution | {"-1": 0.2357742275661996, "-10": 4.03494173825656e-06, "-11": 6.126722607739992e-07, "-12": 8.544644300377424e-08, "-13": 1.101491219045356e-08, "-14": 1.3129014233898314e-09, "-15": 1.3250888768665186e-10, "-2": 0.161002040985672, "-3": 0.07995424310815434, "-4": 0.031216407362251432, "-5": 0.009999774373861655, "-6": 0.0027099027362567497, "-7": 0.0006355748676673651, "-8": 0.00013129149208416572, "-9": 2.4219994877022026e-05, "0": 0.2486887335699181, "1": 0.14408062412779093, "10": 3.244380867703452e-08, "11": 3.0412508097988e-09, "12": 2.618469168678307e-10, "13": 2.0838380887976954e-11, "14": 1.5333613353194364e-12, "15": 9.554035565521356e-14, "2": 0.0613606984223563, "3": 0.018811779752458777, "4": 0.004534200754393516, "5": 0.0008966799993128852, "6": 0.00015001353376817978, "7": 2.1720654630343394e-05, "8": 2.769951945375161e-06, "9": 3.1545626290193814e-07} |
| Unadjusted home-win probability | 23.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 53.3% |
| P home draw | 44.7% |
| P draw away | 79.7% |
| P home away | 75.7% |
| Raw p home draw | 47.9% |
| Raw p draw away | 77.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 5.33 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.68 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:31Z |
| Market reference home last update utc | 2026-10-23T16:22:31Z |
| Market reference draw last update utc | 2026-10-23T16:22:31Z |
| Market reference away last update utc | 2026-10-23T16:22:31Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:31Z |
| Market best over 2 5 last update utc | 2026-10-23T16:22:25Z |
| Market best under 2 5 last update utc | 2026-10-23T16:22:25Z |
| Home probability edge | +2.6% |
| Draw probability edge | +0.5% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0528 |
| Raw ev home | 0.1930 |
| Raw edge prob draw | 0.0104 |
| Raw ev draw | -0.0003 |
| Raw edge prob away | -0.0632 |
| Raw ev away | -0.1240 |
| Elo home rating | 1,386.6713 |
| Elo away rating | 1,580.4486 |
| Elo rating diff | -133.7773 |
| Elo home expectancy | 0.3165 |

</details>


---

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **68.9%**. Expected goals are 1.92 for AS Roma and 0.71 for Cagliari (2.63 combined). The most likely exact score is 1-0 at 14.1%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 49.8%; Under 3.5 goals: 72.5%; Double Chance 1X: 88.9%; Double Chance X2: 31.1%; Double Chance 12 (either team wins): 80.1%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 43.2%; BTTS No (at least one team does not score): 56.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 68.9% | 1.45 |
| Draw | 19.9% | 5.02 |
| Cagliari win | 11.1% | 8.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.92 |
| Cagliari expected goals | 0.71 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.14% |
| 2 | 2-0 | 13.92% |
| 3 | 2-1 | 9.89% |
| 4 | 1-1 | 9.38% |
| 5 | 3-0 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 68.9% | 72.1% | 1.34 | -7.7% |
| Draw | 19.9% | 18.3% | 4.80 | -4.3% |
| Cagliari win | 11.1% | 9.6% | 9.84 | +9.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7eecf109ae6a5f87441a79b0e4111982 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Roma |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9214 |
| Dc lambda away | 0.7103 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 43.2% |
| P btts no | 56.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.38 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.95 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.63 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.67 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.08056360653266145, "-10": 6.452121798204507e-10, "-11": 4.1240945317044674e-11, "-12": 2.4201370658381723e-12, "-13": 1.3125611552257672e-13, "-14": 6.6160793089510305e-15, "-15": 3.105600226414904e-16, "-16": 1.2703510865162316e-17, "-2": 0.02459072424505639, "-3": 0.005260732689050184, "-4": 0.0008768767628038732, "-5": 0.00011930999823501951, "-6": 1.3690044178642052e-05, "-7": 1.3567087683899146e-06, "-8": 1.1825198857401945e-07, "-9": 9.195091139156272e-09, "0": 0.19939665101135912, "1": 0.2655703536939283, "10": 1.612537638324173e-05, "11": 2.788085030740066e-06, "12": 4.425755994487262e-07, "13": 6.492876619680628e-08, "14": 8.852958033450137e-09, "15": 1.1240958708547428e-09, "16": 1.243803189362997e-10, "2": 0.21439656536798904, "3": 0.12406887338712773, "4": 0.05594036106761781, "5": 0.020588923642228484, "6": 0.006390454591214979, "7": 0.0017131036300408584, "8": 0.0004039015838082941, "9": 8.495584062641996e-05} |
| Raw goal margin distribution | {"-1": 0.09158452881037556, "-10": 7.334757716887327e-10, "-11": 4.6882614956230224e-11, "-12": 2.751206436388315e-12, "-13": 1.4921166033874041e-13, "-14": 7.521144250620207e-15, "-15": 3.5304394335213297e-16, "-16": 1.4441322911129882e-17, "-2": 0.027954680655667103, "-3": 0.005980389226103882, "-4": 0.0009968315546251298, "-5": 0.00013563134076291733, "-6": 1.556281178879266e-05, "-7": 1.5423035118905878e-06, "-8": 1.3442859773228808e-07, "-9": 1.0452959165956374e-08, "0": 0.2158126991545609, "1": 0.25337076549105053, "10": 1.538461993676471e-05, "11": 2.660007898723901e-06, "12": 4.22244866041115e-07, "13": 6.194611320446633e-08, "14": 8.446276937901631e-09, "15": 1.0724579280865223e-09, "16": 1.1866662141524934e-10, "2": 0.2045477634470665, "3": 0.11836948283744927, "4": 0.053370611246326534, "5": 0.01964312383256612, "6": 0.006096894284661097, "7": 0.001634408254052317, "8": 0.0003853474307245118, "9": 8.105319766700993e-05} |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 43.7% |
| P home draw | 88.9% |
| P draw away | 31.1% |
| P home away | 80.1% |
| Raw p home draw | 87.3% |
| Raw p draw away | 34.2% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.36 |
| Reference draw odds | 4.93 |
| Reference away odds | 9.02 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:29Z |
| Market reference home last update utc | 2026-10-23T16:22:29Z |
| Market reference draw last update utc | 2026-10-23T16:22:29Z |
| Market reference away last update utc | 2026-10-23T16:22:29Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:29Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:29Z |
| Home probability edge | -3.2% |
| Draw probability edge | +1.6% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0633 |
| Raw ev home | -0.1189 |
| Raw edge prob draw | 0.0328 |
| Raw ev draw | 0.0359 |
| Raw edge prob away | 0.0305 |
| Raw ev away | 0.2464 |
| Elo home rating | 1,629.0662 |
| Elo away rating | 1,426.7784 |
| Elo rating diff | 262.2878 |
| Elo home expectancy | 0.8190 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **43.8%**. Expected goals are 1.17 for Sassuolo and 1.67 for Lazio (2.84 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.4%; Under 3.5 goals: 68.6%; Double Chance 1X: 56.2%; Double Chance X2: 70.1%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 29.9% | 3.34 |
| Draw | 26.2% | 3.81 |
| Lazio win | 43.8% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.17 |
| Lazio expected goals | 1.67 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.40% |
| 2 | 1-2 | 8.58% |
| 3 | 0-1 | 8.45% |
| 4 | 2-1 | 7.58% |
| 5 | 0-2 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 29.9% | 33.5% | 2.98 | -10.9% |
| Draw | 26.2% | 27.5% | 3.37 | -11.6% |
| Lazio win | 43.8% | 39.0% | 2.40 | +5.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T17:30:00+00:00 |
| Fixture id | c7445242bf16a8f37afef7863af45a78 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sassuolo |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1681 |
| Dc lambda away | 1.6708 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.27 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.20320577653114763, "-10": 2.9327910196141233e-06, "-11": 4.390623515873473e-07, "-12": 6.038532486255811e-08, "-13": 7.677050312181676e-09, "-14": 9.015732478707476e-10, "-15": 8.886316340843825e-11, "-2": 0.1345543776360437, "-3": 0.06522386856550413, "-4": 0.024952363817492468, "-5": 0.007849571443414128, "-6": 0.0020918793560272594, "-7": 0.0004829180807512407, "-8": 9.825209473451283e-05, "-9": 1.785974719804211e-05, "0": 0.2624033532291683, "1": 0.17825752670149975, "10": 1.0340598601705638e-07, "11": 1.0822863490574628e-08, "12": 1.0406359088753282e-09, "13": 9.249392449012063e-11, "14": 7.594011592659457e-12, "15": 5.232911958048359e-13, "2": 0.08312870985782085, "3": 0.028171578503420662, "4": 0.0075347308092842055, "5": 0.0016571179163288453, "6": 0.0003087418623512229, "7": 4.9829183472293504e-05, "8": 7.087670873105159e-06, "9": 9.007171881667956e-07} |
| Raw goal margin distribution | {"-1": 0.22583724569364244, "-10": 3.259422332234632e-06, "-11": 4.879616803366873e-07, "-12": 6.711056978828362e-08, "-13": 8.532060097656102e-09, "-14": 1.0019834207763862e-09, "-15": 9.87600471323689e-11, "-2": 0.1495399912348876, "-3": 0.07248799262386997, "-4": 0.02773136282975909, "-5": 0.00872379528238652, "-6": 0.00232485650828028, "-7": 0.0005367017174130539, "-8": 0.00010919464415457721, "-9": 1.984882607592769e-05, "0": 0.24968910063920283, "1": 0.15673176537434075, "10": 9.091903740966294e-08, "11": 9.515931992727407e-09, "12": 9.149723219434167e-10, "13": 8.132467862640672e-11, "14": 6.676985063210306e-12, "15": 4.601003640125773e-13, "2": 0.07309037486605052, "3": 0.024769676287592073, "4": 0.006624862821849155, "5": 0.0014570100980621531, "6": 0.0002714592647316348, "7": 4.3811983916125865e-05, "8": 6.2317882946634685e-06, "9": 7.919497011803116e-07} |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 48.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 56.3% |
| P home draw | 56.2% |
| P draw away | 70.1% |
| P home away | 73.8% |
| Raw p home draw | 51.3% |
| Raw p draw away | 73.7% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.13, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.84 |
| Reference draw odds | 3.43 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:29Z |
| Market reference home last update utc | 2026-10-23T16:22:29Z |
| Market reference draw last update utc | 2026-10-23T16:22:29Z |
| Market reference away last update utc | 2026-10-23T16:22:29Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:29Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:29Z |
| Home probability edge | -3.6% |
| Draw probability edge | -1.3% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | -0.0722 |
| Raw ev home | -0.2163 |
| Raw edge prob draw | -0.0254 |
| Raw ev draw | -0.1585 |
| Raw edge prob away | 0.0977 |
| Raw ev away | 0.1696 |
| Elo home rating | 1,447.3948 |
| Elo away rating | 1,573.0190 |
| Elo rating diff | -65.6242 |
| Elo home expectancy | 0.4067 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **52.0%**. Expected goals are 0.94 for Torino and 1.48 for Como (2.41 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 43.8%; Under 3.5 goals: 77.4%; Double Chance 1X: 48.0%; Double Chance X2: 78.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 21.8% | 4.58 |
| Draw | 26.2% | 3.82 |
| Como win | 52.0% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 0.94 |
| Como expected goals | 1.48 |
| Expected total goals | 2.41 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 43.8% |
| Under 2.5 | 56.2% |
| Over 3.5 | 22.6% |
| Under 3.5 | 77.4% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.48% |
| 2 | 1-1 | 12.34% |
| 3 | 0-2 | 10.29% |
| 4 | 1-2 | 9.63% |
| 5 | 0-0 | 9.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 21.8% | 20.2% | 4.89 | +6.8% |
| Draw | 26.2% | 25.2% | 3.55 | -7.0% |
| Como win | 52.0% | 54.6% | 1.76 | -8.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7d989a0a7bae47eb957731e97c5bd9c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Torino |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9359 |
| Dc lambda away | 1.4781 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.07 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.43 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.09 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.2559984482640501, "-10": 1.4636005762527735e-06, "-11": 1.9464330737656192e-07, "-12": 2.376562811425331e-08, "-13": 2.681546781158355e-09, "-14": 2.802507755601815e-10, "-15": 2.5283822556839983e-11, "-2": 0.15928992375894213, "-3": 0.07082371779313165, "-4": 0.024545651455001732, "-5": 0.006945789359603222, "-6": 0.0016577638002165244, "-7": 0.00034175853428345705, "-8": 6.197048151975531e-05, "-9": 1.0025283768019243e-05, "0": 0.2618694705035865, "1": 0.14187978039278815, "10": 1.3402512310221432e-08, "11": 1.128576862873277e-09, "12": 8.725071366371319e-11, "13": 6.233516205025148e-12, "14": 4.1249867896977214e-13, "15": 2.356386341193326e-14, "2": 0.056458294595047386, "3": 0.015894475300671052, "4": 0.003487948485456001, "5": 0.0006249497975069385, "6": 9.444396225813127e-05, "7": 1.2328179225475331e-05, "8": 1.415443263132431e-06, "9": 1.4498807816865098e-07} |
| Raw goal margin distribution | {"-1": 0.24321424293824626, "-10": 1.3905104055557978e-06, "-11": 1.8492309218123822e-07, "-12": 2.257880580509646e-08, "-13": 2.5476340763214995e-09, "-14": 2.6625544284714235e-10, "-15": 2.402118373547325e-11, "-2": 0.15133520721485783, "-3": 0.06728688014296637, "-4": 0.023319875868531414, "-5": 0.006598926330061099, "-6": 0.001574977389020027, "-7": 0.0003246915899181578, "-8": 5.88757621366506e-05, "-9": 9.524635084369372e-06, "0": 0.2715131633746566, "1": 0.15247153613243675, "10": 1.4403050486235655e-08, "11": 1.2128285471645802e-09, "12": 9.376424395448217e-11, "13": 6.6988670877230456e-12, "14": 4.432929559166347e-13, "15": 2.5322977253600347e-14, "2": 0.060673077449745566, "3": 0.017081046068743253, "4": 0.0037483344142201333, "5": 0.0006716041945352611, "6": 0.00010149449036406262, "7": 1.3248515179684932e-05, "8": 1.5211103938886606e-06, "9": 1.5581187776061515e-07} |
| Unadjusted home-win probability | 23.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.6% |
| Raw p btts yes | 47.3% |
| P home draw | 48.0% |
| P draw away | 78.2% |
| P home away | 73.8% |
| Raw p home draw | 50.6% |
| Raw p draw away | 76.5% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 4.58 |
| Reference draw odds | 3.71 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:29Z |
| Market reference home last update utc | 2026-10-23T16:22:29Z |
| Market reference draw last update utc | 2026-10-23T16:22:29Z |
| Market reference away last update utc | 2026-10-23T16:22:29Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:29Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:29Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.0326 |
| Raw ev home | 0.1480 |
| Raw edge prob draw | 0.0193 |
| Raw ev draw | -0.0361 |
| Raw edge prob away | -0.0519 |
| Raw ev away | -0.1310 |
| Elo home rating | 1,443.9623 |
| Elo away rating | 1,579.5470 |
| Elo rating diff | -75.5848 |
| Elo home expectancy | 0.3929 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **55.4%**. Expected goals are 1.62 for AC Milan and 1.04 for Bologna (2.66 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 50.3%; Under 3.5 goals: 71.9%; Double Chance 1X: 79.7%; Double Chance X2: 44.6%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 55.4% | 1.80 |
| Draw | 24.3% | 4.12 |
| Bologna win | 20.3% | 4.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.62 |
| Bologna expected goals | 1.04 |
| Expected total goals | 2.66 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 50.3% |
| Under 2.5 | 49.7% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.03% |
| 2 | 1-1 | 11.56% |
| 3 | 2-1 | 10.51% |
| 4 | 2-0 | 10.07% |
| 5 | 0-0 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 55.4% | 60.6% | 1.62 | -10.2% |
| Draw | 24.3% | 22.9% | 4.03 | -2.2% |
| Bologna win | 20.3% | 16.5% | 5.26 | +6.7% |
| Over 2.5 | 50.3% | 52.6% | 1.84 | -7.4% |
| Under 2.5 | 49.7% | 47.4% | 2.00 | -0.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 3d0b0fbec194258530882514714c74be |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6166 |
| Dc lambda away | 1.0432 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.27 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.02 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.56 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.46 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.12672405574378745, "-10": 2.8868670425502186e-08, "-11": 2.7037487926129367e-09, "-12": 2.3256397817998494e-10, "-13": 1.848935245499035e-11, "-14": 1.3596919118437313e-12, "-15": 8.500859547071058e-14, "-2": 0.05433221307114365, "-3": 0.016718399246699763, "-4": 0.004037383082016825, "-5": 0.0007991592779849464, "-6": 0.0001337370205884873, "-7": 1.9361580483612007e-05, "-8": 2.468103813275196e-06, "-9": 2.809086055446846e-07, "0": 0.24273834113911974, "1": 0.25941599168052726, "10": 3.0160985369787783e-06, "11": 4.377225277452753e-07, "12": 5.8343009062255996e-08, "13": 7.187566805739505e-09, "14": 8.190577493542195e-10, "15": 7.935068254806632e-11, "2": 0.17075192426361188, "3": 0.08141730453778485, "4": 0.03046742868804007, "5": 0.009345079638919757, "6": 0.0024233442980414826, "7": 0.0005436483819610515, "8": 0.00010738769817450982, "9": 1.8939563729366423e-05} |
| Raw goal margin distribution | {"-1": 0.15050779400607017, "-10": 3.428678064419999e-08, "-11": 3.2111919393228426e-09, "-12": 2.7621189296461843e-10, "-13": 2.1959458559530355e-11, "-14": 1.6148806868464555e-12, "-15": 1.0096312101720507e-13, "-2": 0.06452935462655039, "-3": 0.019856130512591195, "-4": 0.004795124474711828, "-5": 0.0009491465474572666, "-6": 0.00015883696136125588, "-7": 2.2995387497312513e-05, "-8": 2.9313207988312854e-06, "-9": 3.3362990388606224e-07, "0": 0.2560051074223814, "1": 0.23540522205896777, "10": 2.736937461910961e-06, "11": 3.972082375360514e-07, "12": 5.2942954344937126e-08, "13": 6.522307082951437e-09, "14": 7.43248209629636e-10, "15": 7.200622029794615e-11, "2": 0.15494763598758068, "3": 0.07388156192684912, "4": 0.027647454458807792, "5": 0.008480126970228624, "6": 0.0021990467854746754, "7": 0.000493329910960714, "8": 9.744821347137281e-05, "9": 1.71865742606266e-05} |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.3% |
| Raw p btts yes | 52.3% |
| P home draw | 79.7% |
| P draw away | 44.6% |
| P home away | 75.7% |
| Raw p home draw | 75.9% |
| Raw p draw away | 49.7% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.76, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.61 |
| Reference draw odds | 4.05 |
| Reference away odds | 5.55 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:30Z |
| Market reference home last update utc | 2026-10-23T16:22:30Z |
| Market reference draw last update utc | 2026-10-23T16:22:30Z |
| Market reference away last update utc | 2026-10-23T16:22:30Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:30Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:30Z |
| Market best over 2 5 last update utc | 2026-10-23T16:22:25Z |
| Market best under 2 5 last update utc | 2026-10-23T16:22:25Z |
| Home probability edge | -5.1% |
| Draw probability edge | +1.3% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | -0.1026 |
| Raw ev home | -0.1849 |
| Raw edge prob draw | 0.0265 |
| Raw ev draw | 0.0317 |
| Raw edge prob away | 0.0761 |
| Raw ev away | 0.2667 |
| Elo home rating | 1,550.8302 |
| Elo away rating | 1,493.4486 |
| Elo rating diff | 117.3816 |
| Elo home expectancy | 0.6628 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **55.5%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.21 combined). The most likely exact score is 0-1 at 16.2%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 38.9%; Under 3.5 goals: 81.4%; Double Chance 1X: 44.5%; Double Chance X2: 81.6%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.4% | 5.45 |
| Draw | 26.1% | 3.83 |
| Juventus win | 55.5% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.21 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 18.6% |
| Under 3.5 | 81.4% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.23% |
| 2 | 0-2 | 11.94% |
| 3 | 1-1 | 11.86% |
| 4 | 0-0 | 10.62% |
| 5 | 1-2 | 9.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.4% | 16.6% | 5.59 | +2.6% |
| Draw | 26.1% | 24.4% | 3.81 | -0.4% |
| Juventus win | 55.5% | 59.0% | 1.63 | -9.5% |
| Over 2.5 | 38.9% | 45.8% | 2.12 | -17.6% |
| Under 2.5 | 61.1% | 54.2% | 1.75 | +7.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | 34848497b90b1392f6a767fc183d3ac1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7826 |
| Dc lambda away | 1.4324 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.41 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.37 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.13 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.27497803629551115, "-10": 1.2905747181952906e-06, "-11": 1.6664572179015438e-07, "-12": 1.9748734693634918e-08, "-13": 2.1567478985824583e-09, "-14": 2.0430074647361127e-10, "-2": 0.17076916217181012, "-3": 0.07489648492856246, "-4": 0.02544360802084534, "-5": 0.007032775529151232, "-6": 0.0016360835289774545, "-7": 0.00032830685487015746, "-8": 5.789121033133396e-05, "-9": 9.10120290607523e-06, "0": 0.26130634499603594, "1": 0.1270858336188608, "10": 2.6237394116800873e-09, "11": 1.8511286708733758e-10, "12": 1.1986340398898914e-11, "13": 7.152396927850419e-13, "14": 3.701920353911323e-14, "2": 0.04370265787300251, "3": 0.010472846333435648, "4": 0.0019439580319952601, "5": 0.00029358903889148993, "6": 3.731843705835537e-05, "7": 4.091690895528653e-06, "8": 3.9422157565680294e-07, "9": 3.386346932507729e-08} |
| Raw goal margin distribution | {"-1": 0.25785787361922435, "-10": 1.2102233947984582e-06, "-11": 1.5627034088777332e-07, "-12": 1.851917630722433e-08, "-13": 2.0224685380454935e-09, "-14": 1.9158095960759326e-10, "-2": 0.1601370554193541, "-3": 0.07023342156854535, "-4": 0.023859486196946562, "-5": 0.0065949141539413, "-6": 0.0015342207891548968, "-7": 0.00030786643410478094, "-8": 5.4286897231452555e-05, "-9": 8.534561015686377e-06, "0": 0.2786282859886282, "1": 0.13902436367147605, "10": 2.8702152849116828e-09, "11": 2.0250249631600385e-10, "12": 1.3112345406682046e-11, "13": 7.824297982750553e-13, "14": 4.0496812816171116e-14, "2": 0.04780811541723797, "3": 0.011456672674482582, "4": 0.0021265747778994554, "5": 0.00032116899382522615, "6": 4.0824156536688215e-05, "7": 4.476067134258629e-06, "8": 4.312550198602142e-07, "9": 3.7044626773638514e-08} |
| Unadjusted home-win probability | 20.1% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 41.7% |
| P home draw | 44.5% |
| P draw away | 81.6% |
| P home away | 73.9% |
| Raw p home draw | 47.9% |
| Raw p draw away | 79.9% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 5.48 |
| Reference draw odds | 3.81 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:30Z |
| Market reference home last update utc | 2026-10-23T16:22:30Z |
| Market reference draw last update utc | 2026-10-23T16:22:30Z |
| Market reference away last update utc | 2026-10-23T16:22:30Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.75 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:30Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:30Z |
| Market best over 2 5 last update utc | 2026-10-23T16:22:25Z |
| Market best under 2 5 last update utc | 2026-10-23T16:22:25Z |
| Home probability edge | +1.7% |
| Draw probability edge | +1.7% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | 0.0345 |
| Raw ev home | 0.1224 |
| Raw edge prob draw | 0.0346 |
| Raw ev draw | 0.0616 |
| Raw edge prob away | -0.0691 |
| Raw ev away | -0.1514 |
| Elo home rating | 1,396.1582 |
| Elo away rating | 1,557.5355 |
| Elo rating diff | -101.3773 |
| Elo home expectancy | 0.3581 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **56.6%**. Expected goals are 0.81 for Monza and 1.88 for Napoli (2.69 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.3%; Double Chance 1X: 43.4%; Double Chance X2: 80.5%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 19.5% | 5.12 |
| Draw | 23.9% | 4.18 |
| Napoli win | 56.6% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.81 |
| Napoli expected goals | 1.88 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 27.7% |
| Under 3.5 | 72.3% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.37% |
| 2 | 0-1 | 11.25% |
| 3 | 0-2 | 10.86% |
| 4 | 1-2 | 8.85% |
| 5 | 0-0 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 19.5% | 23.7% | 3.79 | -26.0% |
| Draw | 23.9% | 25.3% | 3.85 | -7.9% |
| Napoli win | 56.6% | 51.0% | 1.89 | +6.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | abec89862e33762414fcb8b2232aba08 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8150 |
| Dc lambda away | 1.8783 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.24 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.61 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.60 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.22671227008779463, "-10": 1.0653119431680165e-05, "-11": 1.7984533452747682e-06, "-12": 2.787960245075145e-07, "-13": 3.994889568572707e-08, "-14": 5.3205891019815615e-09, "-15": 6.594814018936184e-10, "-16": 7.066019197127959e-11, "-2": 0.17581035998975308, "-3": 0.09838031361349558, "-4": 0.04305709732117511, "-5": 0.015415539554986243, "-6": 0.004660505162754101, "-7": 0.001217962184126937, "-8": 0.0002801113907789687, "-9": 5.749587093718194e-05, "0": 0.23923353319718638, "1": 0.13510179101854525, "10": 3.5241546884172032e-09, "11": 2.581394322995013e-10, "12": 1.7362759864585075e-11, "13": 1.0794784286745932e-12, "14": 6.238007861752903e-14, "15": 3.3547932243312464e-15, "16": 1.5596064595308284e-16, "2": 0.046302727048575666, "3": 0.01124209671041197, "4": 0.0021348180717078455, "5": 0.00033162850978199433, "6": 4.350138961563624e-05, "7": 4.932657359261691e-06, "8": 4.922150877018419e-07, "9": 4.3836696288686576e-08} |
| Raw goal margin distribution | {"-1": 0.2491017879257823, "-10": 1.1705193972918935e-05, "-11": 1.9760639494084783e-06, "-12": 3.063291993173904e-07, "-13": 4.389414537255313e-08, "-14": 5.846036730207804e-09, "-15": 7.246100806625281e-10, "-16": 7.76384099034804e-11, "-2": 0.19317293674649097, "-3": 0.10809609911422383, "-4": 0.04730930496812383, "-5": 0.016937938398749356, "-6": 0.005120764607181649, "-7": 0.0013382449815112353, "-8": 0.00030777446776214464, "-9": 6.317401454828937e-05, "0": 0.22525667517860276, "1": 0.10610963821113613, "10": 2.7678891313639022e-09, "11": 2.0274403146563925e-10, "12": 1.3636800472356877e-11, "13": 8.478278834043261e-13, "14": 4.8993633050946275e-14, "15": 2.6348717705607257e-15, "16": 1.2249228964688606e-16, "2": 0.0363663988335945, "3": 0.008829600301247454, "4": 0.0016766970410068067, "5": 0.00026046272908873057, "6": 3.4166214074565574e-05, "7": 3.874134338743959e-06, "8": 3.8658824938105897e-07, "9": 3.442956565191266e-08} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 62.1% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.6% |
| Raw p btts yes | 47.6% |
| P home draw | 43.4% |
| P draw away | 80.5% |
| P home away | 76.1% |
| Raw p home draw | 37.9% |
| Raw p draw away | 84.7% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.94 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.90 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:30Z |
| Market reference home last update utc | 2026-10-23T16:22:30Z |
| Market reference draw last update utc | 2026-10-23T16:22:30Z |
| Market reference away last update utc | 2026-10-23T16:22:30Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:30Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:30Z |
| Home probability edge | -4.2% |
| Draw probability edge | -1.4% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | -0.0838 |
| Raw ev home | -0.4191 |
| Raw edge prob draw | -0.0280 |
| Raw ev draw | -0.1328 |
| Raw edge prob away | 0.1117 |
| Raw ev away | 0.1746 |
| Elo home rating | 1,364.4494 |
| Elo away rating | 1,577.6538 |
| Elo rating diff | -153.2044 |
| Elo home expectancy | 0.2928 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **38.9%**. Expected goals are 1.05 for Parma and 1.17 for Udinese (2.22 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 38.3%; Under 3.5 goals: 81.6%; Double Chance 1X: 61.1%; Double Chance X2: 68.3%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 92.5%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.7% | 3.15 |
| Draw | 29.4% | 3.40 |
| Udinese win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.05 |
| Udinese expected goals | 1.17 |
| Expected total goals | 2.22 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 38.3% |
| Under 2.5 | 61.7% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.59% |
| 2 | 0-1 | 12.54% |
| 3 | 0-0 | 11.19% |
| 4 | 1-0 | 10.86% |
| 5 | 1-2 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.7% | 31.4% | 2.96 | -6.1% |
| Draw | 29.4% | 29.0% | 3.21 | -5.6% |
| Udinese win | 38.9% | 39.7% | 2.50 | -2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 482c18a8081afdfa310324fa8f37e95a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Parma |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0479 |
| Dc lambda away | 1.1680 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.94 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.61 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.43 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.41 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.22300398751092187, "-10": 1.6191870384486803e-07, "-11": 1.7033717584165988e-08, "-12": 1.638981919558058e-09, "-13": 1.3458353987807483e-10, "-2": 0.11205928865046962, "-3": 0.03979467146558603, "-4": 0.010973949256485201, "-5": 0.0024656773750685907, "-6": 0.0004666658582699903, "-7": 7.622697859365138e-05, "-8": 1.0945399737148755e-05, "-9": 1.401597887499084e-06, "0": 0.2939785898827427, "1": 0.19338382163819384, "10": 5.300694597301598e-08, "11": 5.002918469758446e-09, "12": 4.318832536369335e-10, "13": 3.181723003124165e-11, "2": 0.08738922233782727, "3": 0.027842815905181176, "4": 0.0068885751203296266, "5": 0.0013886120193899358, "6": 0.00023579191923351033, "7": 3.4554913775425906e-05, "8": 4.451546902239118e-06, "9": 5.114238526948002e-07} |
| Raw goal margin distribution | {"-1": 0.21846410620498016, "-10": 1.5862238746563003e-07, "-11": 1.6686947748818275e-08, "-12": 1.6056157745826741e-09, "-13": 1.3184370861496787e-10, "-2": 0.10977800267267301, "-3": 0.0389845375882541, "-4": 0.01075054326434154, "-5": 0.0024154814895756944, "-6": 0.00045716554560864197, "-7": 7.467516134146529e-05, "-8": 1.0722574951783391e-05, "-9": 1.3730643705923837e-06, "0": 0.29835962636351127, "1": 0.19553928659683267, "10": 5.359776382758843e-08, "11": 5.0586812288204045e-09, "12": 4.36697044219576e-10, "13": 3.2171866338624196e-11, "2": 0.08836326662403599, "3": 0.028153153210158693, "4": 0.006965355495032333, "5": 0.0014040895527408879, "6": 0.00023842006679586906, "7": 3.4940064431570594e-05, "8": 4.50116404848347e-06, "9": 5.171242064480638e-07} |
| Unadjusted home-win probability | 32.1% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 45.2% |
| P home draw | 61.1% |
| P draw away | 68.3% |
| P home away | 70.6% |
| Raw p home draw | 61.9% |
| Raw p draw away | 67.9% |
| Raw p home away | 70.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.03 |
| Reference draw odds | 3.27 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:30Z |
| Market reference home last update utc | 2026-10-23T16:22:30Z |
| Market reference draw last update utc | 2026-10-23T16:22:30Z |
| Market reference away last update utc | 2026-10-23T16:22:30Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:30Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:30Z |
| Home probability edge | +0.4% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | 0.0071 |
| Raw ev home | -0.0507 |
| Raw edge prob draw | 0.0088 |
| Raw ev draw | -0.0423 |
| Raw edge prob away | -0.0158 |
| Raw ev away | -0.0477 |
| Elo home rating | 1,371.5475 |
| Elo away rating | 1,454.9036 |
| Elo rating diff | -23.3561 |
| Elo home expectancy | 0.4664 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **76.7%**. Expected goals are 0.69 for Venezia and 2.67 for Inter Milan (3.36 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 64.7%; Under 3.5 goals: 57.2%; Double Chance 1X: 23.3%; Double Chance X2: 91.4%; Double Chance 12 (either team wins): 85.3%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 8.6% | 11.60 |
| Draw | 14.7% | 6.82 |
| Inter Milan win | 76.7% | 1.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.69 |
| Inter Milan expected goals | 2.67 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.7% |
| Under 2.5 | 35.3% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.00% |
| 2 | 0-3 | 10.70% |
| 3 | 0-1 | 8.76% |
| 4 | 1-2 | 8.26% |
| 5 | 1-3 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 8.6% | 10.3% | 7.76 | -33.1% |
| Draw | 14.7% | 15.5% | 5.92 | -13.2% |
| Inter Milan win | 76.7% | 74.3% | 1.32 | +1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 33320ad169692216a91dec030e7ef6a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6888 |
| Dc lambda away | 2.6746 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.74 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.52 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.09 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.19994504648602643, "-10": 0.00020450464678890387, "-11": 4.9047792686041115e-05, "-12": 1.0805606349047348e-05, "-13": 2.201043730051597e-06, "-14": 4.1686478750632844e-07, "-15": 7.37673892981444e-08, "-16": 1.2248643533646928e-08, "-17": 1.9153406347636023e-09, "-18": 2.819388087276312e-10, "-19": 3.617994125108515e-11, "-2": 0.21288861254487226, "-3": 0.16630799846163422, "-4": 0.1023024606723686, "-5": 0.0516793978369842, "-6": 0.022097802899055923, "-7": 0.008180715765404275, "-8": 0.002668097996202757, "-9": 0.0007772485344597016, "0": 0.1466776197617064, "1": 0.06386291027193572, "10": 3.3567279257371195e-10, "11": 2.0734004004743235e-11, "12": 1.1764232587161607e-12, "13": 6.171544728537392e-14, "14": 3.0103096529786854e-15, "15": 1.3719273767458255e-16, "16": 5.86685634443049e-18, "17": 2.36273073389091e-19, "18": 8.957231897638106e-21, "19": 2.9603125375356613e-22, "2": 0.018053416268860683, "3": 0.003632209172939223, "4": 0.0005754327075626196, "5": 7.48646257492061e-05, "6": 8.244400070848828e-06, "7": 7.860533373819556e-07, "8": 6.602573410545436e-08, "9": 4.95361355789466e-09} |
| Raw goal margin distribution | {"-1": 0.20632815574460786, "-10": 0.00021103331817778177, "-11": 5.0613610019901046e-05, "-12": 1.1150567962967657e-05, "-13": 2.2713105501541737e-06, "-14": 4.3017291157077836e-07, "-15": 7.612236289656897e-08, "-16": 1.2639673125621087e-08, "-17": 1.976486578381421e-09, "-18": 2.9093951293096604e-10, "-19": 3.7334961202984154e-11, "-2": 0.2196849363231495, "-3": 0.1716172679004787, "-4": 0.10556839696521443, "-5": 0.0533292273706917, "-6": 0.022803260187237, "-7": 0.008441879537459136, "-8": 0.0027532752052493166, "-9": 0.0008020616638856176, "0": 0.13881511614702666, "1": 0.05154553924839845, "10": 2.709308897848844e-10, "11": 1.6734993952704327e-11, "12": 9.495240820794595e-13, "13": 4.981226187054385e-14, "14": 2.429705030771726e-15, "15": 1.1073209182432204e-16, "16": 4.7353036790659716e-18, "17": 1.9070259914335672e-19, "18": 7.229632135001619e-21, "19": 2.389350961948345e-22, "2": 0.014571416693848507, "3": 0.0029316575095765162, "4": 0.0004644478162078935, "5": 6.042533120461562e-05, "6": 6.654285650652299e-06, "7": 6.34445611401481e-07, "8": 5.329121479502316e-08, "9": 3.998199909503097e-09} |
| Unadjusted home-win probability | 7.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 79.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 46.6% |
| P home draw | 23.3% |
| P draw away | 91.4% |
| P home away | 85.3% |
| Raw p home draw | 20.8% |
| Raw p draw away | 93.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 8.35 |
| Reference draw odds | 5.71 |
| Reference away odds | 1.32 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:30Z |
| Market reference home last update utc | 2026-10-23T16:22:30Z |
| Market reference draw last update utc | 2026-10-23T16:22:30Z |
| Market reference away last update utc | 2026-10-23T16:22:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:27Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:27Z |
| Home probability edge | -1.7% |
| Draw probability edge | -0.8% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.0333 |
| Raw ev home | -0.4601 |
| Raw edge prob draw | -0.0157 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.0490 |
| Raw ev away | 0.0449 |
| Elo home rating | 1,364.0519 |
| Elo away rating | 1,684.1272 |
| Elo rating diff | -260.0753 |
| Elo home expectancy | 0.1829 |

</details>


---

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Atalanta BC win** at **38.4%**. Expected goals are 1.25 for Fiorentina and 1.59 for Atalanta BC (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.5%; Double Chance 1X: 61.6%; Double Chance X2: 64.4%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 35.6% | 2.81 |
| Draw | 26.1% | 3.83 |
| Atalanta BC win | 38.4% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.25 |
| Atalanta BC expected goals | 1.59 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.7% |
| Under 2.5 | 46.3% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.30% |
| 2 | 2-1 | 8.70% |
| 3 | 1-0 | 8.27% |
| 4 | 1-2 | 7.89% |
| 5 | 0-1 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 35.6% | 41.4% | 2.25 | -20.0% |
| Draw | 26.1% | 26.7% | 3.54 | -7.6% |
| Atalanta BC win | 38.4% | 31.8% | 3.09 | +18.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T19:45:00+00:00 |
| Fixture id | da159a6b84dbb548b4d7b94c722caac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Fiorentina |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2523 |
| Dc lambda away | 1.5903 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.68 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.37 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.185796604324952, "-10": 1.700124238710833e-06, "-11": 2.421805432605507e-07, "-12": 3.169394518827231e-08, "-13": 3.83423056678468e-09, "-14": 4.283790411365543e-10, "-15": 4.0093247642725276e-11, "-2": 0.11674505472797984, "-3": 0.05373210783444994, "-4": 0.019533377088561885, "-5": 0.0058419089772584545, "-6": 0.0014805289909432706, "-7": 0.00032509492571544744, "-8": 6.292076166586272e-05, "-9": 1.0881415032685073e-05, "0": 0.26096063843364353, "1": 0.2038392801349264, "10": 2.1821640054753874e-07, "11": 2.4477848569578223e-08, "12": 2.5225371047061715e-09, "13": 2.4030718254765685e-10, "14": 2.1141899638449825e-11, "15": 1.558168049869001e-12, "2": 0.10135077973707755, "3": 0.03673243719999877, "4": 0.010515270936161322, "5": 0.0024764250302099053, "6": 0.0004942134731490312, "7": 8.545453625612921e-05, "8": 1.3024053394347142e-05, "9": 1.773637399978711e-06} |
| Raw goal margin distribution | {"-1": 0.21730552968150355, "-10": 1.9884453731526286e-06, "-11": 2.8325152347641995e-07, "-12": 3.7068866634335526e-08, "-13": 4.484471108949432e-09, "-14": 5.010271031424437e-10, "-15": 4.689259229095633e-11, "-2": 0.13654364700330926, "-3": 0.06284444323561145, "-4": 0.022846008785363102, "-5": 0.006832628234873456, "-6": 0.0017316093464391817, "-7": 0.0003802272129032496, "-8": 7.359138500642493e-05, "-9": 1.2726775421720377e-05, "0": 0.25443208246980575, "1": 0.17028908541268326, "10": 1.8229985529134065e-07, "11": 2.0449004936754692e-08, "12": 2.1073491634960393e-09, "13": 2.0075468431330853e-10, "14": 1.766212454702191e-11, "15": 1.3017069720606442e-12, "2": 0.0846693119003615, "3": 0.030686593534014563, "4": 0.008784547656370321, "5": 0.0020688267404024483, "6": 0.0004128701802982583, "7": 7.138945356257589e-05, "8": 1.0880406070023763e-05, "9": 1.4817119178216396e-06} |
| Unadjusted home-win probability | 29.7% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 57.2% |
| P home draw | 61.6% |
| P draw away | 64.4% |
| P home away | 73.9% |
| Raw p home draw | 55.1% |
| Raw p draw away | 70.3% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.32 |
| Reference draw odds | 3.52 |
| Reference away odds | 2.98 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:30Z |
| Market reference home last update utc | 2026-10-23T16:22:30Z |
| Market reference draw last update utc | 2026-10-23T16:22:30Z |
| Market reference away last update utc | 2026-10-23T16:22:30Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:30Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:30Z |
| Home probability edge | -5.9% |
| Draw probability edge | -0.7% |
| Away probability edge | +6.5% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | -0.1170 |
| Raw ev home | -0.3318 |
| Raw edge prob draw | -0.0131 |
| Raw ev draw | -0.0993 |
| Raw edge prob away | 0.1301 |
| Raw ev away | 0.3861 |
| Elo home rating | 1,435.7664 |
| Elo away rating | 1,541.0294 |
| Elo rating diff | -45.2630 |
| Elo home expectancy | 0.4352 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **50.7%**. Expected goals are 1.56 for Frosinone and 0.97 for Lecce (2.53 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 46.6%; Under 3.5 goals: 75.0%; Double Chance 1X: 76.3%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 50.7% | 1.97 |
| Draw | 25.7% | 3.90 |
| Lecce win | 23.7% | 4.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.56 |
| Lecce expected goals | 0.97 |
| Expected total goals | 2.53 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 72.4% |
| Under 1.5 | 27.6% |
| Over 2.5 | 46.6% |
| Under 2.5 | 53.4% |
| Over 3.5 | 25.0% |
| Under 3.5 | 75.0% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.19% |
| 2 | 1-0 | 12.00% |
| 3 | 2-0 | 9.69% |
| 4 | 2-1 | 9.41% |
| 5 | 0-0 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 50.7% | 50.7% | 1.88 | -4.7% |
| Draw | 25.7% | 25.1% | 3.68 | -5.6% |
| Lecce win | 23.7% | 24.2% | 4.05 | -4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T17:30:00+00:00 |
| Fixture id | 667cf69986b200753742c90cb9c5126c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T16:22:25Z |
| Market best draw last update utc | 2026-10-23T16:22:25Z |
| Market best away last update utc | 2026-10-23T16:22:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Frosinone |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5623 |
| Dc lambda away | 0.9711 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:22:31.141591+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.24 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.62 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.87 |
| Fair Over 3.5 odds | 4.01 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.79 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.151914071413543, "-10": 1.9160051594569573e-08, "-11": 1.6723725526397024e-09, "-12": 1.3403739621058098e-10, "-13": 9.928437707107979e-12, "-14": 6.807941891694348e-13, "-15": 4.00245759039509e-14, "-2": 0.061796249248993414, "-3": 0.01789300252361894, "-4": 0.004050818511932426, "-5": 0.0007500734299157541, "-6": 0.00011726768559265361, "-7": 1.58470669464277e-05, "-8": 1.8844930662830837e-06, "-9": 2.0000186837930873e-07, "0": 0.256546826536011, "1": 0.24108423875537632, "10": 2.1739166911337983e-06, "11": 3.052855075820409e-07, "12": 3.936643378246849e-08, "13": 4.691459163480187e-09, "14": 5.17570839107515e-10, "15": 4.895619231313075e-11, "2": 0.15616829408288607, "3": 0.07275132499011935, "4": 0.026498873032408176, "5": 0.007894331037152463, "6": 0.001985714652230936, "7": 0.00043173207294245686, "8": 8.260130305890907e-05, "9": 1.410435860748646e-05} |
| Raw goal margin distribution | {"-1": 0.14832381677722262, "-10": 1.8707233343900215e-08, "-11": 1.6328486082486345e-09, "-12": 1.3086962920448618e-10, "-13": 9.693794403971645e-12, "-14": 6.647046691447108e-13, "-15": 3.907865682042678e-14, "-2": 0.060335790265115305, "-3": 0.01747012902236679, "-4": 0.0039550836678325174, "-5": 0.0007323466019512468, "-6": 0.0001144962448171413, "-7": 1.5472545975150388e-05, "-8": 1.8399559809072436e-06, "-9": 1.95275132873242e-07, "0": 0.26209504114330784, "1": 0.2411042278531346, "10": 2.174096937812228e-06, "11": 3.0531081982097756e-07, "12": 3.9369697784699965e-08, "13": 4.691848147995857e-09, "14": 5.17613752630826e-10, "15": 4.896025143420425e-11, "2": 0.1561812425166505, "3": 0.07275735704495123, "4": 0.02650107014229086, "5": 0.007894985582450208, "6": 0.0019858792944510515, "7": 0.0004317678692875682, "8": 8.260815180825216e-05, "9": 1.4105528046867811e-05} |
| Unadjusted home-win probability | 50.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.0% |
| Raw p btts yes | 49.5% |
| P home draw | 76.3% |
| P draw away | 49.3% |
| P home away | 74.3% |
| Raw p home draw | 76.9% |
| Raw p draw away | 49.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:22:25Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:22:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.91 |
| Reference draw odds | 3.73 |
| Reference away odds | 3.86 |
| Market reference 1x2 last update utc | 2026-10-23T16:22:30Z |
| Market reference home last update utc | 2026-10-23T16:22:30Z |
| Market reference draw last update utc | 2026-10-23T16:22:30Z |
| Market reference away last update utc | 2026-10-23T16:22:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-23T16:22:27Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:22:27Z |
| Home probability edge | +0.0% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -15.5% |
| Under 2.5 probability edge | +15.5% |
| Raw edge prob home | 0.0001 |
| Raw ev home | -0.0469 |
| Raw edge prob draw | 0.0111 |
| Raw ev draw | -0.0355 |
| Raw edge prob away | -0.0112 |
| Raw ev away | -0.0647 |
| Elo home rating | 1,459.6529 |
| Elo away rating | 1,423.2697 |
| Elo rating diff | 96.3832 |
| Elo home expectancy | 0.6353 |

</details>


---
