# Bundesliga — football model report

Fixtures in this report: **15**.

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
| Training sha256 | 59a6af4527b312c54e5a945372880e0a496386c1332e248f6d495827a2d618c4 |
| Training as of utc | 2026-10-22T10:56:00.959120+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 16, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T10:56:00.959120+00:00', 'observations': 117, 'observations_sha256': '1fbd2433f0e808c63f12c4f1a128a1d8257dee0aafd7de3572c17ad4415ad7b7', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 57, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '36344966bf586cd1ed7bbeef1405ff77e3fdb372d754b3dbe98de225b222158b', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
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
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 2.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261022T105600959120Z_5d7c832d5a9b79934b74ea6878ec44b56d915c707b07ba69ddede03c19b95ab7.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **64.5%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.46 combined). The most likely exact score is 2-1 at 10.9%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.8%; Under 3.5 goals: 53.8%; Double Chance 1X: 82.8%; Double Chance X2: 35.5%; Double Chance 12 (either team wins): 81.8%; Under 4.5 goals: 72.3%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 64.5% | 1.55 |
| Draw | 18.2% | 5.48 |
| Borussia Monchengladbach win | 17.2% | 5.80 |

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
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.7% |
| Under 4.5 | 72.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.91% |
| 2 | 2-0 | 8.47% |
| 3 | 1-1 | 7.99% |
| 4 | 3-1 | 7.88% |
| 5 | 1-0 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 64.5% | 72.6% | 1.38 | -11.0% |
| Draw | 18.2% | 14.1% | 5.81 | +6.0% |
| Borussia Monchengladbach win | 17.2% | 13.3% | 7.00 | +20.7% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.63 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.94 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.21 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.60 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.09868491252210053, "-10": 1.1424441075363521e-07, "-11": 1.3101264034186651e-08, "-12": 1.3814867091270819e-09, "-13": 1.3479718956038738e-10, "-14": 1.2236966136079201e-11, "-15": 1.0378774856010138e-12, "-16": 8.180006977513352e-14, "-17": 5.322106092433833e-15, "-2": 0.04956107359531113, "-3": 0.0176368830387812, "-4": 0.005031843835184516, "-5": 0.0011916081283074996, "-6": 0.0002404825116747301, "-7": 4.220968412852372e-05, "-8": 6.547614110584366e-06, "-9": 9.092764608843264e-07, "0": 0.18239162587173385, "1": 0.24049657411031541, "10": 2.9267282200026496e-05, "11": 5.650047835339494e-06, "12": 1.0029450262456415e-06, "13": 1.6474139828597425e-07, "14": 2.5176024987008306e-08, "15": 3.594603444825098e-09, "16": 4.76924970690186e-10, "17": 5.2236179746237406e-11, "2": 0.1968594191525713, "3": 0.11793122807498133, "4": 0.05664031146012903, "5": 0.022579973508589767, "6": 0.007671229269061836, "7": 0.002266653097144719, "8": 0.0005918988882593613, "9": 0.00013837316958352467} |
| Raw goal margin distribution | {"-1": 0.12109102337107787, "-10": 1.4018325860587188e-07, "-11": 1.6075866399527612e-08, "-12": 1.6951490871948355e-09, "-13": 1.6540248366493716e-10, "-14": 1.501533227830757e-11, "-15": 1.27352442894533e-12, "-16": 1.0037252815802221e-13, "-17": 6.5304741804167306e-15, "-2": 0.060813765424187954, "-3": 0.0216412839780725, "-4": 0.0061743087557531865, "-5": 0.0014621591490161716, "-6": 0.00029508333844870924, "-7": 5.1793265218208733e-05, "-8": 8.034230086711681e-06, "-9": 1.1157249306073696e-06, "0": 0.22361409490480375, "1": 0.2105414328639974, "10": 2.5621884857295536e-05, "11": 4.946304002055558e-06, "12": 8.780228312637725e-07, "13": 1.4422197145826114e-07, "14": 2.2040215725289934e-08, "15": 3.1468762607162467e-09, "16": 4.175214015800187e-10, "17": 4.572988273034373e-11, "2": 0.17233952015526385, "3": 0.10324225960461389, "4": 0.049585456162084936, "5": 0.019767516415219, "6": 0.006715736422073377, "7": 0.0019843292680733348, "8": 0.0005181746996012109, "9": 0.00012113804739973052} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 65.1% |
| P home draw | 82.8% |
| P draw away | 35.5% |
| P home away | 81.8% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:41Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.75, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:41Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.16, "price": 5.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:55:47Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.25, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.70 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -8.0% |
| Draw probability edge | +4.1% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.1607 |
| Raw ev home | -0.2205 |
| Raw edge prob draw | 0.0824 |
| Raw ev draw | 0.2992 |
| Raw edge prob away | 0.0783 |
| Raw ev away | 0.4808 |
| Market p home draw | 86.3% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:55:41Z |
| Market reference home draw last update utc | 2026-10-22T10:55:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 31.2% |
| Market draw away odds | 3.25 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:55:41Z |
| Market reference draw away last update utc | 2026-10-22T10:55:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.6% |
| Market home away odds | 1.18 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:55:41Z |
| Market reference home away last update utc | 2026-10-22T10:55:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.10 |
| Market reference dc home draw odds | 1.12 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 92.4% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 9.00 |
| Market reference over 1 5 last update utc | 2026-10-22T10:55:27Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 44.0% |
| Market under 3 5 odds | 2.17 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:55:47Z |
| Market reference under 3 5 odds | 2.17 |
| Market reference under 3 5 opposite odds | 1.73 |
| Market reference under 3 5 last update utc | 2026-10-22T10:55:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.8% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:55:41Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.66 |
| Market reference btts yes last update utc | 2026-10-22T10:55:47Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.2%**. Expected goals are 1.76 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 50.5%; Under 3.5 goals: 72.1%; Double Chance 1X: 76.0%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.2% | 1.95 |
| Draw | 24.7% | 4.04 |
| FC Schalke 04 win | 24.0% | 4.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.76 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.82% |
| 2 | 1-0 | 9.87% |
| 3 | 2-0 | 9.67% |
| 4 | 2-1 | 9.01% |
| 5 | 0-0 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.2% | 46.9% | 2.09 | +7.1% |
| Draw | 24.7% | 23.6% | 3.92 | -3.1% |
| FC Schalke 04 win | 24.0% | 29.6% | 3.33 | -19.9% |
| Over 2.5 | 50.5% | 60.1% | 1.64 | -17.2% |
| Under 2.5 | 49.5% | 39.9% | 2.46 | +21.7% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.02 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.43 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.15436648801120897, "-10": 1.3823863817671104e-08, "-11": 1.1561069604419644e-09, "-12": 8.879361794480457e-11, "-13": 6.30428118072029e-12, "-14": 4.160509443318982e-13, "-15": 2.554206206148458e-14, "-16": 1.3487039334440144e-15, "-2": 0.06388363135996605, "-3": 0.017603450370753684, "-4": 0.0038027050424813786, "-5": 0.0006728848702266587, "-6": 0.00010062454416942163, "-7": 1.301446450308175e-05, "-8": 1.4818529517655662e-06, "-9": 1.5062868065063822e-07, "0": 0.2472474596957999, "1": 0.2170010901924327, "10": 5.602290577046648e-06, "11": 8.837896872103025e-07, "12": 1.280405099535657e-07, "13": 1.7148097651084667e-08, "14": 2.1347234189432654e-09, "15": 2.4720985953725843e-10, "16": 2.462301251100307e-11, "2": 0.1615131704121885, "3": 0.08395196717679233, "4": 0.03420900535568256, "5": 0.011418348641440099, "6": 0.0032209292969506923, "7": 0.0007858113520387077, "8": 0.00016877644479918353, "9": 3.236153599382169e-05} |
| Raw goal margin distribution | {"-1": 0.11901446396764057, "-10": 1.0658011096957276e-08, "-11": 8.913427516487102e-10, "-12": 6.845867247223397e-11, "-13": 4.860515096840371e-12, "-14": 3.20769622738946e-13, "-15": 1.9692582658582365e-14, "-16": 1.03983239988094e-15, "-2": 0.04925341141440384, "-3": 0.013572020953823117, "-4": 0.002931833897944885, "-5": 0.0005187850884846596, "-6": 7.758015577475788e-05, "-7": 1.003397522749685e-05, "-8": 1.142488483124904e-06, "-9": 1.1613266530030076e-07, "0": 0.2587303581675913, "1": 0.23546141465198012, "10": 6.07887851343552e-06, "11": 9.589738458034056e-07, "12": 1.3893294075016992e-07, "13": 1.8606889614859162e-08, "14": 2.31632475057778e-09, "15": 2.682400498123859e-10, "16": 2.6717696918908704e-11, "2": 0.17525312686888264, "3": 0.09109377716367555, "4": 0.037119172017722295, "5": 0.012389709755461673, "6": 0.003494934371442457, "7": 0.0008526604748231426, "8": 0.00018313428940429081, "9": 3.5114538082085415e-05} |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 76.0% |
| P draw away | 48.8% |
| P home away | 75.3% |
| Raw p home draw | 81.5% |
| Raw p draw away | 44.4% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market best over 2 5 last update utc | 2026-10-21T17:19:22Z |
| Market best under 2 5 last update utc | 2026-10-21T17:19:22Z |
| Home probability edge | +4.4% |
| Draw probability edge | +1.1% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | 0.0872 |
| Raw ev home | 0.1618 |
| Raw edge prob draw | 0.0230 |
| Raw ev draw | 0.0142 |
| Raw edge prob away | -0.1101 |
| Raw ev away | -0.3827 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **46.6%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 47.1%; Under 3.5 goals: 75.4%; Double Chance 1X: 72.5%; Double Chance X2: 53.4%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 46.6% | 2.15 |
| Draw | 25.8% | 3.87 |
| Union Berlin win | 27.5% | 3.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.34 |
| Union Berlin expected goals | 1.16 |
| Expected total goals | 2.50 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 47.1% |
| Under 2.5 | 52.9% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.34% |
| 2 | 1-0 | 11.31% |
| 3 | 2-1 | 10.08% |
| 4 | 2-0 | 8.72% |
| 5 | 0-0 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 46.6% | 53.6% | 1.85 | -13.8% |
| Draw | 25.8% | 22.0% | 4.18 | +8.1% |
| Union Berlin win | 27.5% | 24.4% | 3.94 | +8.5% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.93 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.82 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.1581157034637423, "-10": 9.997119714368352e-08, "-11": 1.0389766561849968e-08, "-12": 9.913518199928204e-10, "-13": 8.70070580690846e-11, "-14": 6.469742826260407e-12, "-2": 0.08024421150988523, "-3": 0.02760739191695709, "-4": 0.007432416315288199, "-5": 0.0016373322612462861, "-6": 0.000304635553380682, "-7": 4.9000571640251666e-05, "-8": 6.936692501495152e-06, "-9": 8.76470741781784e-07, "0": 0.2584963621019209, "1": 0.2437595819723098, "10": 5.858083775356438e-07, "11": 7.0705834419301e-08, "12": 7.835127115704162e-09, "13": 7.986224223760719e-10, "14": 6.896723414028849e-11, "2": 0.14208367667374017, "3": 0.05677074976216677, "4": 0.01774998759690842, "5": 0.004541231289765322, "6": 0.000981264679248189, "7": 0.00018330550262435225, "8": 3.013669169492446e-05, "9": 4.4223115168197405e-06} |
| Raw goal margin distribution | {"-1": 0.17631546894875316, "-10": 1.1147829165367342e-07, "-11": 1.1585671274205352e-08, "-12": 1.1054604773985363e-09, "-13": 9.702192703977588e-11, "-14": 7.214436740949729e-12, "-2": 0.08948064912497897, "-3": 0.030785115871849525, "-4": 0.008287917893954808, "-5": 0.0018257959149058228, "-6": 0.0003397003540833918, "-7": 5.464073825841776e-05, "-8": 7.735134237535585e-06, "-9": 9.773561162604787e-07, "0": 0.2969829378029667, "1": 0.20705426885518452, "10": 4.975973634286229e-07, "11": 6.005895124626177e-08, "12": 6.655313826858479e-09, "13": 6.783658735319705e-10, "14": 5.858214936348186e-11, "2": 0.12068871940090377, "3": 0.04822221136603921, "4": 0.015077194809449407, "5": 0.0038574127703888904, "6": 0.0008335058629130357, "7": 0.00015570336360081556, "8": 2.5598709245060693e-05, "9": 3.756399934542836e-06} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 52.1% |
| P home draw | 72.5% |
| P draw away | 53.4% |
| P home away | 74.2% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -7.0% |
| Draw probability edge | +3.8% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -16.7% |
| Under 2.5 probability edge | +16.7% |
| Raw edge prob home | -0.1404 |
| Raw ev home | -0.2675 |
| Raw edge prob draw | 0.0770 |
| Raw ev draw | 0.2414 |
| Raw edge prob away | 0.0634 |
| Raw ev away | 0.2100 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **65.3%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 71.2%; Under 3.5 goals: 50.3%; Double Chance 1X: 83.7%; Double Chance X2: 34.7%; Double Chance 12 (either team wins): 81.6%; Under 4.5 goals: 69.3%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 65.3% | 1.53 |
| Draw | 18.4% | 5.44 |
| Eintracht Frankfurt win | 16.3% | 6.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.42 |
| Eintracht Frankfurt expected goals | 1.22 |
| Expected total goals | 3.64 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 88.9% |
| Under 1.5 | 11.1% |
| Over 2.5 | 71.2% |
| Under 2.5 | 28.8% |
| Over 3.5 | 49.7% |
| Under 3.5 | 50.3% |
| Over 4.5 | 30.7% |
| Under 4.5 | 69.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.73% |
| 2 | 2-0 | 7.95% |
| 3 | 1-1 | 7.87% |
| 4 | 3-1 | 7.85% |
| 5 | 3-0 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 65.3% | 67.7% | 1.48 | -3.3% |
| Draw | 18.4% | 16.7% | 5.21 | -4.2% |
| Eintracht Frankfurt win | 16.3% | 15.6% | 5.89 | -3.9% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.43 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.00 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.47 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.26 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.09679560072008415, "-10": 6.760255331313982e-08, "-11": 7.354041844900418e-09, "-12": 7.357352418449716e-10, "-13": 6.812077634639103e-11, "-14": 5.868911159086526e-12, "-15": 4.727149626962545e-13, "-16": 3.572452907549929e-14, "-17": 2.5181011991863746e-15, "-18": 1.4692302676504083e-16, "-2": 0.045713725223531475, "-3": 0.015309380426959989, "-4": 0.00412220626364385, "-5": 0.0009229160271173359, "-6": 0.00017629096265798057, "-7": 2.930959986321276e-05, "-8": 4.308908213739892e-06, "-9": 5.673327852200543e-07, "0": 0.18384893469743574, "1": 0.21582986713785238, "10": 6.74152218980921e-05, "11": 1.4515160915764846e-05, "12": 2.874208083769369e-06, "13": 5.267167446726691e-07, "14": 8.981646555678805e-08, "15": 1.4318537575760474e-08, "16": 2.1417398437267247e-09, "17": 2.987956513330078e-10, "18": 3.450577994837239e-11, "2": 0.1935683596848432, "3": 0.12830579161303984, "4": 0.06837845021396205, "5": 0.03030069650360836, "6": 0.011455692880152081, "7": 0.0037696592180901664, "8": 0.0010968830713831835, "9": 0.0002858458302581878} |
| Raw goal margin distribution | {"-1": 0.10080930094807405, "-10": 7.040574252449981e-08, "-11": 7.658982557184252e-09, "-12": 7.66243040608192e-10, "-13": 7.094545405403843e-11, "-14": 6.112269843593253e-12, "-15": 4.923164336250311e-13, "-16": 3.720587274637349e-14, "-17": 2.6225161031911894e-15, "-18": 1.5301529729837978e-16, "-2": 0.047609278203078045, "-3": 0.015944195059577105, "-4": 0.004293136554867052, "-5": 0.0009611854137516374, "-6": 0.00018360099608665976, "-7": 3.0524943812505066e-05, "-8": 4.487580237584121e-06, "-9": 5.908576532145084e-07, "0": 0.20091367794030146, "1": 0.20795556604471535, "10": 6.49556561182218e-05, "11": 1.3985592191186683e-05, "12": 2.7693459525172895e-06, "13": 5.07500098277291e-07, "14": 8.653961651687368e-08, "15": 1.3796142424523502e-08, "16": 2.0636009623183386e-09, "17": 2.8789444032307225e-10, "18": 3.324687679298347e-11, "2": 0.18650624373918692, "3": 0.123624704381915, "4": 0.06588374217189615, "5": 0.029195210915514185, "6": 0.011037745280197304, "7": 0.0036321275960982846, "8": 0.001056864571244278, "9": 0.00027541707837356986} |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.2% |
| P home draw | 83.7% |
| P draw away | 34.7% |
| P home away | 81.6% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.1% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.42 |
| Reference draw odds | 5.00 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -2.4% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0477 |
| Raw ev home | -0.0687 |
| Raw edge prob draw | 0.0341 |
| Raw ev draw | 0.0468 |
| Raw edge prob away | 0.0135 |
| Raw ev away | 0.0003 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **53.2%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 56.2%; Under 3.5 goals: 66.8%; Double Chance 1X: 77.1%; Double Chance X2: 46.8%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 53.2% | 1.88 |
| Draw | 23.9% | 4.19 |
| Werder Bremen win | 22.9% | 4.36 |

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
| 2 | 2-1 | 10.38% |
| 3 | 1-0 | 9.01% |
| 4 | 2-0 | 8.94% |
| 5 | 0-0 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 53.2% | 57.0% | 1.76 | -6.3% |
| Draw | 23.9% | 21.5% | 4.22 | +0.6% |
| Werder Bremen win | 22.9% | 21.5% | 4.34 | -0.5% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.17 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.98 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.85 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.13416380796382582, "-10": 7.671111242794569e-08, "-11": 7.975057444504274e-09, "-12": 7.617295730572787e-10, "-13": 6.727836291889104e-11, "-14": 5.524166177636258e-12, "-15": 4.212080455688205e-13, "-16": 2.7150324901757482e-14, "-2": 0.06559867244787834, "-3": 0.02201528309941188, "-4": 0.005837764635544147, "-5": 0.00127375974595006, "-6": 0.0002355408147427329, "-7": 3.774080417997442e-05, "-8": 5.3305381646810975e-06, "-9": 6.727538441835476e-07, "0": 0.2385007475860474, "1": 0.23507096905688776, "10": 4.738082593356608e-06, "11": 7.340893097548833e-07, "12": 1.0449286331683732e-07, "13": 1.3754093165754503e-08, "14": 1.6830383596177707e-09, "15": 1.9124701770024542e-10, "16": 1.837146449766389e-11, "2": 0.16652273274812215, "3": 0.08328628425329132, "4": 0.032912928555356914, "5": 0.010702326576068172, "6": 0.0029493586390826406, "7": 0.000704276659872836, "8": 0.00014824291168623118, "9": 2.7882377376071105e-05} |
| Raw goal margin distribution | {"-1": 0.14247684097315846, "-10": 8.146427216211246e-08, "-11": 8.46920647615194e-09, "-12": 8.089277197192859e-10, "-13": 7.144705237580779e-11, "-14": 5.866453538741207e-12, "-15": 4.47306860441116e-13, "-16": 2.883260830253328e-14, "-2": 0.0696632852350664, "-3": 0.023379389991522153, "-4": 0.006199483126190135, "-5": 0.001352684211308833, "-6": 0.0002501353510615692, "-7": 4.007929289543694e-05, "-8": 5.66082798272539e-06, "-9": 7.144388932197317e-07, "0": 0.2620325427909855, "1": 0.218409179113876, "10": 4.402248112306575e-06, "11": 6.820571854665524e-07, "12": 9.708642709838772e-08, "13": 1.2779205402693655e-08, "14": 1.5637448895372688e-09, "15": 1.7769146190816546e-10, "16": 1.7069298247047478e-11, "2": 0.15471963003017647, "3": 0.0773829667193151, "4": 0.03058006582799052, "5": 0.009943747505128935, "6": 0.002740308604924192, "7": 0.0006543576510915887, "8": 0.00013773547954790244, "9": 2.5906079252930887e-05} |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 24.3% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.7% |
| P home draw | 77.1% |
| P draw away | 46.8% |
| P home away | 76.1% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.99, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.66 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -3.8% |
| Draw probability edge | +2.4% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | -0.0755 |
| Raw ev home | -0.1295 |
| Raw edge prob draw | 0.0471 |
| Raw ev draw | 0.1058 |
| Raw edge prob away | 0.0284 |
| Raw ev away | 0.0562 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **67.7%**. Expected goals are 2.69 for RB Leipzig and 1.32 for Elversberg (4.01 combined). The most likely exact score is 2-1 at 8.9%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 76.7%; Under 3.5 goals: 42.9%; Double Chance 1X: 84.9%; Double Chance X2: 32.3%; Double Chance 12 (either team wins): 82.8%; Under 4.5 goals: 62.4%; BTTS Yes (both teams score): 68.7%; BTTS No (at least one team does not score): 31.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 67.7% | 1.48 |
| Draw | 17.2% | 5.82 |
| Elversberg win | 15.1% | 6.60 |

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
| 1 | 2-1 | 8.93% |
| 2 | 3-1 | 8.00% |
| 3 | 2-0 | 6.76% |
| 4 | 1-1 | 6.75% |
| 5 | 3-0 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 67.7% | 69.7% | 1.42 | -3.9% |
| Draw | 17.2% | 16.1% | 5.27 | -9.4% |
| Elversberg win | 15.1% | 14.2% | 6.87 | +4.0% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6857 |
| Dc lambda away | 1.3213 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 68.7% |
| P btts no | 31.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.92 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.09 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.30 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.33 |
| Fair Over 4.5 odds | 2.66 |
| Fair Under 4.5 odds | 1.60 |
| Goal margin distribution | {"-1": 0.08824568134487963, "-10": 1.052764639919386e-07, "-11": 1.2321283987989057e-08, "-12": 1.3270223440864775e-09, "-13": 1.3233500431762887e-10, "-14": 1.2284658680720696e-11, "-15": 1.0665154251344952e-12, "-16": 8.694636750333858e-14, "-17": 6.674990985377289e-15, "-18": 4.783656992701491e-16, "-19": 2.803063587209124e-17, "-2": 0.0426591097073531, "-3": 0.01497123817927392, "-4": 0.004263489326955353, "-5": 0.001015398408202529, "-6": 0.00020710227357886542, "-7": 3.686111552941907e-05, "-8": 5.8120161408555085e-06, "-9": 8.218304530291616e-07, "0": 0.17184108260477796, "1": 0.20387621592214758, "10": 0.00013866499628333387, "11": 3.2987660704916214e-05, "12": 7.221605886579496e-06, "13": 1.4638287765316413e-06, "14": 2.762095151941016e-07, "15": 4.8741925189682e-08, "16": 8.076942232978065e-09, "17": 1.2603936728640995e-09, "18": 1.8360121838245007e-10, "19": 2.1867970219517726e-11, "2": 0.19282678920169413, "3": 0.1375540236074719, "4": 0.07962340679872754, "5": 0.038545355034119475, "6": 0.015980134679004356, "7": 0.005781280473505212, "8": 0.0018528590088003672, "9": 0.0005325468109372868} |
| Raw goal margin distribution | {"-1": 0.09366755068943594, "-10": 1.1174471517570373e-07, "-11": 1.307831131127491e-08, "-12": 1.4085554192159521e-09, "-13": 1.4046574898622463e-10, "-14": 1.3039435722432571e-11, "-15": 1.1320427937366378e-12, "-16": 9.22884062003318e-14, "-17": 7.085106567774646e-15, "-18": 5.07756784259608e-16, "-19": 2.975285550966595e-17, "-2": 0.04528011184211402, "-3": 0.01589108033015518, "-4": 0.004525440753137, "-5": 0.0010777851156089644, "-6": 0.00021982676560150332, "-7": 3.912588530907586e-05, "-8": 6.169110014050465e-06, "-9": 8.723242253225315e-07, "0": 0.18270762229707238, "1": 0.19780017816556197, "10": 0.0001345324212837269, "11": 3.200454322337023e-05, "12": 7.006383380945029e-06, "13": 1.4202028985686167e-06, "14": 2.6797775831428767e-07, "15": 4.7289289940191845e-08, "16": 7.836228495265395e-09, "17": 1.2228306863732754e-09, "18": 1.7812942791389985e-10, "19": 2.1216248231679684e-11, "2": 0.18708005289716087, "3": 0.13345455846275675, "4": 0.07725042364407751, "5": 0.03739660390849655, "6": 0.015503885395949036, "7": 0.005608983384903947, "8": 0.0017976390252226859, "9": 0.000516675540638451} |
| Unadjusted home-win probability | 65.7% |
| Unadjusted draw probability | 18.3% |
| Unadjusted away-win probability | 16.1% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 43.2% |
| Raw p btts yes | 69.0% |
| P home draw | 84.9% |
| P draw away | 32.3% |
| P home away | 82.8% |
| Raw p home draw | 83.9% |
| Raw p draw away | 34.3% |
| Raw p home away | 81.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.38 |
| Reference draw odds | 5.10 |
| Reference away odds | 5.70 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -2.0% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | -0.0403 |
| Raw ev home | -0.0677 |
| Raw edge prob draw | 0.0217 |
| Raw ev draw | -0.0371 |
| Raw edge prob away | 0.0186 |
| Raw ev away | 0.1041 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **38.8%**. Expected goals are 1.02 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 14.1%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 33.3%; Under 3.5 goals: 85.9%; Double Chance 1X: 68.0%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 94.6%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 38.8% | 2.58 |
| Draw | 29.3% | 3.42 |
| Hamburger SV win | 32.0% | 3.13 |

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
| 1 | 1-0 | 14.14% |
| 2 | 0-0 | 13.18% |
| 3 | 1-1 | 12.92% |
| 4 | 0-1 | 11.94% |
| 5 | 2-0 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 38.8% | 43.2% | 2.26 | -12.4% |
| Draw | 29.3% | 24.5% | 3.79 | +11.0% |
| Hamburger SV win | 32.0% | 32.3% | 3.05 | -2.5% |
| Over 2.5 | 33.3% | 61.5% | 1.64 | -45.4% |
| Under 2.5 | 66.7% | 38.5% | 2.47 | +64.8% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0158 |
| Dc lambda away | 0.9633 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.59 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 3.00 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 7.07 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.63 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.19693317667692636, "-10": 2.8953277783447656e-08, "-11": 2.516837672283873e-09, "-12": 2.0030120945210977e-10, "-13": 1.3803433782710555e-11, "-2": 0.0887456516334616, "-3": 0.026438174066376125, "-4": 0.00607880868393105, "-5": 0.0011349640370622676, "-6": 0.00017814034967691988, "-7": 2.409939896007e-05, "-8": 2.8633997301045777e-06, "-9": 3.032147138953192e-07, "0": 0.29279341260060543, "1": 0.23261932895421342, "10": 5.493577508143923e-08, "11": 5.035875763202942e-09, "12": 4.2263519035364233e-10, "13": 3.0713655040467084e-11, "2": 0.11010482319537698, "3": 0.03459019426333719, "4": 0.008386916147014726, "5": 0.001651308469876777, "6": 0.00027331954601931305, "7": 3.899212318370598e-05, "8": 4.88556656011791e-06, "9": 5.455637541035831e-07} |
| Raw goal margin distribution | {"-1": 0.19475054008535084, "-10": 2.863238475464187e-08, "-11": 2.4889432255924727e-09, "-12": 1.9808124450529827e-10, "-13": 1.3650448490075177e-11, "-2": 0.08776207177217604, "-3": 0.026145156266605483, "-4": 0.006011436438732865, "-5": 0.001122385079675731, "-6": 0.0001761659964866559, "-7": 2.3832302115887576e-05, "-8": 2.8316642900294575e-06, "-9": 2.99854144890038e-07, "0": 0.34037791647289223, "1": 0.20619156081959616, "10": 4.8694548556219896e-08, "11": 4.463752381956058e-09, "12": 3.746198131861055e-10, "13": 2.7224291720466074e-11, "2": 0.09759586810986391, "3": 0.030660419219137085, "4": 0.007434082707531246, "5": 0.0014637041226506584, "6": 0.0002422678461398116, "7": 3.456224714886349e-05, "8": 4.33051973388255e-06, "9": 4.835825229611842e-07} |
| Unadjusted home-win probability | 34.4% |
| Unadjusted draw probability | 34.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 86.1% |
| Raw p btts yes | 40.9% |
| P home draw | 68.0% |
| P draw away | 61.2% |
| P home away | 70.7% |
| Raw p home draw | 68.4% |
| Raw p draw away | 65.6% |
| Raw p home away | 66.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.92, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market best over 2 5 last update utc | 2026-10-21T17:19:22Z |
| Market best under 2 5 last update utc | 2026-10-21T17:19:22Z |
| Home probability edge | -4.4% |
| Draw probability edge | +4.8% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -28.3% |
| Under 2.5 probability edge | +28.3% |
| Raw edge prob home | -0.0881 |
| Raw ev home | -0.2234 |
| Raw edge prob draw | 0.0952 |
| Raw ev draw | 0.2900 |
| Raw edge prob away | -0.0071 |
| Raw ev away | -0.0362 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **67.2%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 72.4%; Under 3.5 goals: 49.2%; Double Chance 1X: 32.8%; Double Chance X2: 84.3%; Double Chance 12 (either team wins): 83.0%; Under 4.5 goals: 68.2%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 15.7% | 6.36 |
| Draw | 17.0% | 5.87 |
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
| Over 2.5 | 72.4% |
| Under 2.5 | 27.6% |
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.91% |
| 2 | 1-3 | 8.09% |
| 3 | 0-2 | 8.01% |
| 4 | 1-1 | 7.23% |
| 5 | 0-3 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 15.7% | 14.4% | 6.56 | +3.1% |
| Draw | 17.0% | 14.2% | 5.99 | +2.1% |
| Bayern Munich win | 67.2% | 71.4% | 1.39 | -6.5% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Dc lambda away | 2.4469 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.83 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.43 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.62 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.14 |
| Fair Under 4.5 odds | 1.47 |
| Goal margin distribution | {"-1": 0.22038799867349942, "-10": 7.447063190530348e-05, "-11": 1.6200748254958777e-05, "-12": 3.241520474453923e-06, "-13": 6.00274512095489e-07, "-14": 1.034406018479004e-07, "-15": 1.666523711560281e-08, "-16": 2.519150971615375e-09, "-17": 3.5502846134282094e-10, "-18": 4.131051843059543e-11, "-2": 0.19859309510105277, "-3": 0.13258142134446937, "-4": 0.07124470968746699, "-5": 0.031855605132956585, "-6": 0.012157700183435467, "-7": 0.004039828375726703, "-8": 0.00118726199751353, "-9": 0.00031254502831221234, "0": 0.1703888430696886, "1": 0.09294281083335841, "10": 7.098301159436079e-08, "11": 7.811862627719678e-09, "12": 7.90712191500344e-10, "13": 7.407466756757558e-11, "14": 6.45744905056058e-12, "15": 5.262978412022939e-13, "16": 4.02461580654557e-14, "17": 2.869350125897699e-15, "18": 1.6890058822169893e-16, "2": 0.04412984398094046, "3": 0.01490393885054804, "4": 0.004051549528914655, "5": 0.000916441046342078, "6": 0.0001769376456170103, "7": 2.9742801459600415e-05, "8": 4.421968713159411e-06, "9": 5.888868212651657e-07} |
| Raw goal margin distribution | {"-1": 0.2068058707716204, "-10": 6.988113677145068e-05, "-11": 1.5202324401439514e-05, "-12": 3.0417512222914337e-06, "-13": 5.632806410653451e-07, "-14": 9.706573800321836e-08, "-15": 1.5638187623880755e-08, "-16": 2.3639000917736273e-09, "-17": 3.3314867660050714e-10, "-18": 3.876462324395002e-11, "-2": 0.18635414908617226, "-3": 0.1244106596289857, "-4": 0.06685402251243175, "-5": 0.029892399759198645, "-6": 0.011408442329659357, "-7": 0.00379086080021889, "-8": 0.001114093111728788, "-9": 0.0002932834234372491, "0": 0.19914783501645508, "1": 0.1004437135252062, "10": 7.67116597595022e-08, "11": 8.442315062794698e-09, "12": 8.545262202834401e-10, "13": 8.005282626939887e-11, "14": 6.9785942207089675e-12, "15": 5.687724431472037e-13, "16": 4.3494203962313376e-14, "17": 3.1009195812457727e-15, "18": 1.8253162504409837e-16, "2": 0.047691320791674645, "3": 0.016106753721766533, "4": 0.004378527791085773, "5": 0.0009904019589698665, "6": 0.0001912173091046729, "7": 3.2143179256775216e-05, "8": 4.7788414688508005e-06, "9": 6.364126352922598e-07} |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 32.8% |
| P draw away | 84.3% |
| P home away | 83.0% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 5.60 |
| Reference draw odds | 5.70 |
| Reference away odds | 1.35 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.90 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +1.3% |
| Draw probability edge | +2.9% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | 0.0254 |
| Raw ev home | 0.1141 |
| Raw edge prob draw | 0.0575 |
| Raw ev draw | 0.1929 |
| Raw edge prob away | -0.0829 |
| Raw ev away | -0.1229 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.9%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.1%; Double Chance X2: 69.6%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 69.9%; BTTS No (at least one team does not score): 30.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.4% | 3.29 |
| Draw | 22.7% | 4.41 |
| Bayer Leverkusen win | 46.9% | 2.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.50 |
| Bayer Leverkusen expected goals | 2.16 |
| Expected total goals | 3.66 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 49.4% |
| Under 3.5 | 50.6% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.33% |
| 2 | 1-2 | 8.16% |
| 3 | 2-1 | 7.40% |
| 4 | 2-2 | 6.80% |
| 5 | 1-3 | 5.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.4% | 35.1% | 2.79 | -15.2% |
| Draw | 22.7% | 22.8% | 4.04 | -8.5% |
| Bayer Leverkusen win | 46.9% | 42.1% | 2.34 | +9.9% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 69.9% |
| P btts no | 30.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.39 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.94 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.40 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.18176040808651134, "-10": 1.8933815050542225e-05, "-11": 3.6289129502120118e-06, "-12": 6.398444205915607e-07, "-13": 1.0443237763444095e-07, "-14": 1.5862721303182306e-08, "-15": 2.2510127193519753e-09, "-16": 2.959877229738795e-10, "-17": 3.157244745795066e-11, "-2": 0.14283913980710508, "-3": 0.08321038280973696, "-4": 0.03914996472428166, "-5": 0.01535905686923089, "-6": 0.005150251545959129, "-7": 0.0015050348542561495, "-8": 0.00038924771221161527, "-9": 9.021929922939728e-05, "0": 0.22660866184825676, "1": 0.16137197452132473, "10": 6.50674048577778e-07, "11": 8.669657852237776e-08, "12": 1.0626734929792132e-08, "13": 1.2057594628703277e-09, "14": 1.2732194368450565e-10, "15": 1.2560402813516814e-11, "16": 1.148151952956633e-12, "17": 8.514006413936333e-14, "2": 0.08998542249140921, "3": 0.03644202540495586, "4": 0.011919455437330945, "5": 0.003250795428337656, "6": 0.0007577982285057175, "7": 0.00015394718599750178, "8": 2.7679058819395908e-05, "9": 4.459896209659476e-06} |
| Raw goal margin distribution | {"-1": 0.20043907122758145, "-10": 2.087955426309985e-05, "-11": 4.001839283723624e-06, "-12": 7.055982253983506e-07, "-13": 1.1516440241030029e-07, "-14": 1.7492858640802028e-08, "-15": 2.4823387201773446e-09, "-16": 3.2640499057095726e-10, "-17": 3.4816999540632526e-11, "-2": 0.15751804707797365, "-3": 0.09176152288861927, "-4": 0.043173222653596924, "-5": 0.016937434979431627, "-6": 0.005679518698973877, "-7": 0.0016597002148490895, "-8": 0.0004292488707222872, "-9": 9.949071271746138e-05, "0": 0.22517267924407702, "1": 0.13651688716221025, "10": 5.50454909736094e-07, "11": 7.334326212836368e-08, "12": 8.989967295228469e-09, "13": 1.020044087740177e-09, "14": 1.077113635797648e-10, "15": 1.0625804751358427e-11, "16": 9.713094920713084e-13, "17": 7.202648764492166e-14, "2": 0.07612554661330101, "3": 0.030829094611551273, "4": 0.010083578377223566, "5": 0.0027500963162544424, "6": 0.0006410794412072279, "7": 0.00013023569106160692, "8": 2.341583140946395e-05, "9": 3.7729670806549764e-06} |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.7% |
| P home draw | 53.1% |
| P draw away | 69.6% |
| P home away | 77.3% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -4.7% |
| Draw probability edge | -0.1% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0936 |
| Raw ev home | -0.2827 |
| Raw edge prob draw | -0.0029 |
| Raw ev draw | -0.0903 |
| Raw edge prob away | 0.0965 |
| Raw ev away | 0.2115 |

</details>


---

## 2026-10-30 — Elversberg vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **38.8%**. Expected goals are 1.91 for Elversberg and 1.56 for FSV Mainz 05 (3.47 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 67.5%; Under 3.5 goals: 54.6%; Double Chance 1X: 61.2%; Double Chance X2: 62.3%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 68.4%; BTTS No (at least one team does not score): 31.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 37.7% | 2.65 |
| Draw | 23.5% | 4.25 |
| FSV Mainz 05 win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 1.91 |
| FSV Mainz 05 expected goals | 1.56 |
| Expected total goals | 3.47 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 45.4% |
| Under 3.5 | 54.6% |
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.05% |
| 2 | 1-2 | 9.12% |
| 3 | 2-1 | 7.39% |
| 4 | 2-2 | 6.73% |
| 5 | 0-1 | 4.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 37.7% | 30.2% | 3.38 | +27.4% |
| Draw | 23.5% | 22.9% | 3.74 | -12.0% |
| FSV Mainz 05 win | 38.8% | 46.9% | 2.05 | -20.5% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9112 |
| Dc lambda away | 1.5582 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.4% |
| P btts no | 31.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.74 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.71 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.73 |
| Fair Under 4.5 odds | 1.37 |
| Goal margin distribution | {"-1": 0.19786023435842767, "-10": 1.1951556498377016e-06, "-11": 1.656329143122385e-07, "-12": 2.1110985231898028e-08, "-13": 2.4901204786747803e-09, "-14": 2.730846899770149e-10, "-15": 2.76483931439721e-11, "-16": 2.270110079806087e-12, "-2": 0.1167395416220226, "-3": 0.04976568604585847, "-4": 0.017062026866146107, "-5": 0.00486485932013824, "-6": 0.0011835768064106726, "-7": 0.00025065092912306017, "-8": 4.6940124855546164e-05, "-9": 7.873183086906156e-06, "0": 0.23523869422484522, "1": 0.1622920536355236, "10": 6.083261894021928e-06, "11": 1.03401601970754e-06, "12": 1.6164329868671376e-07, "13": 2.3385041306976622e-08, "14": 3.14545671428464e-09, "15": 3.9059334127231657e-10, "16": 3.9334210251900435e-11, "2": 0.11603296727805028, "3": 0.06066832281423733, "4": 0.025511217992498114, "5": 0.008921531992050424, "6": 0.002662160136505887, "7": 0.0006914736379409579, "8": 0.00015882509652063908, "9": 3.2673361447047426e-05} |
| Raw goal margin distribution | {"-1": 0.15667488591444095, "-10": 9.463795274249641e-07, "-11": 1.3115580317435828e-07, "-12": 1.671665462984017e-08, "-13": 1.971792579618799e-09, "-14": 2.1624108950372763e-10, "-15": 2.1893276613138364e-11, "-16": 1.7975781688529659e-12, "-2": 0.09243976903515413, "-3": 0.039406772204485935, "-4": 0.013510502104632253, "-5": 0.003852220641726933, "-6": 0.0009372108636010618, "-7": 0.00019847699994918853, "-8": 3.716936215303263e-05, "-9": 6.234350555200315e-06, "0": 0.24115126335853881, "1": 0.19449653408763928, "10": 7.290396096606495e-06, "11": 1.2392013503992765e-06, "12": 1.937190432235512e-07, "13": 2.8025460161579144e-08, "14": 3.769626518036405e-09, "15": 4.681008676234251e-10, "16": 4.7139508026994114e-11, "2": 0.13905800974192245, "3": 0.07270706268083355, "4": 0.0305735454616801, "5": 0.01069187931469977, "6": 0.0031904268147318355, "7": 0.0008286864512450136, "8": 0.00019034161012451112, "9": 3.915691135879758e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.3% |
| Raw p btts yes | 68.3% |
| P home draw | 61.2% |
| P draw away | 62.3% |
| P home away | 76.5% |
| Raw p home draw | 69.3% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.55 |
| Reference away odds | 1.92 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:06Z |
| Home probability edge | +7.5% |
| Draw probability edge | +0.6% |
| Away probability edge | -8.1% |
| Over 2.5 probability edge | +7.2% |
| Under 2.5 probability edge | -7.2% |
| Raw edge prob home | 0.1496 |
| Raw ev home | 0.5270 |
| Raw edge prob draw | 0.0118 |
| Raw ev draw | -0.0981 |
| Raw edge prob away | -0.1614 |
| Raw ev away | -0.3705 |

</details>


---

## 2026-10-31 — Augsburg vs SC Freiburg

The model's most likely 1X2 outcome is **SC Freiburg win** at **41.2%**. Expected goals are 1.36 for Augsburg and 1.43 for SC Freiburg (2.80 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 53.9%; Under 3.5 goals: 69.1%; Double Chance 1X: 58.8%; Double Chance X2: 66.6%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 33.4% | 3.00 |
| Draw | 25.5% | 3.93 |
| SC Freiburg win | 41.2% | 2.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.36 |
| SC Freiburg expected goals | 1.43 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 30.9% |
| Under 3.5 | 69.1% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.07% |
| 2 | 1-2 | 9.35% |
| 3 | 0-1 | 8.11% |
| 4 | 2-1 | 7.87% |
| 5 | 0-2 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 33.4% | 32.3% | 3.06 | +2.1% |
| Draw | 25.5% | 23.0% | 3.81 | -3.0% |
| SC Freiburg win | 41.2% | 44.7% | 2.17 | -10.6% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.79 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.62 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.23 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.2106378521110673, "-10": 8.05534844593372e-07, "-11": 1.0348688096198757e-07, "-12": 1.2209307547365135e-08, "-13": 1.3220029861950685e-09, "-14": 1.1879988636580899e-10, "-2": 0.1257398567576556, "-3": 0.05229272252310093, "-4": 0.017165049898440168, "-5": 0.004633410300657271, "-6": 0.0010595638201321318, "-7": 0.0002098983655863339, "-8": 3.6646209171015504e-05, "-9": 5.716351111507146e-06, "0": 0.2545508949803175, "1": 0.17665386976514108, "10": 4.331049718359563e-07, "11": 5.2938443314566324e-08, "12": 5.942291234735032e-09, "13": 6.121704560040037e-10, "14": 5.233991174753525e-11, "2": 0.10068518069666543, "3": 0.03983922453825296, "4": 0.01244204375146481, "5": 0.0031953942137476006, "6": 0.0006952289299874046, "7": 0.00013103484607090147, "8": 2.176626101608149e-05, "9": 3.230358361316208e-06} |
| Raw goal margin distribution | {"-1": 0.19242832651887554, "-10": 7.358968036571649e-07, "-11": 9.45404974490197e-08, "-12": 1.1153819675558241e-08, "-13": 1.2077165606129295e-09, "-14": 1.0852970202122597e-10, "-2": 0.11486971581841098, "-3": 0.04777204563845586, "-4": 0.01568114084655674, "-5": 0.004232854547722349, "-6": 0.000967965115028156, "-7": 0.00019175276819442645, "-8": 3.3478164695302975e-05, "-9": 5.22217572557482e-06, "0": 0.2792224920142339, "1": 0.18243880113881683, "10": 4.472879758256215e-07, "11": 5.4672032632542425e-08, "12": 6.136885030166965e-09, "13": 6.322173651471951e-10, "14": 5.405390079270184e-11, "2": 0.10398234515420447, "3": 0.04114385024637164, "4": 0.012849486675563713, "5": 0.003300034640039684, "6": 0.0007179957771236612, "7": 0.000135325879112454, "8": 2.2479046569021544e-05, "9": 3.336143767871063e-06} |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 58.0% |
| P home draw | 58.8% |
| P draw away | 66.6% |
| P home away | 74.5% |
| Raw p home draw | 62.4% |
| Raw p draw away | 65.5% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +1.1% |
| Draw probability edge | +2.5% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -12.3% |
| Under 2.5 probability edge | +12.3% |
| Raw edge prob home | 0.0219 |
| Raw ev home | 0.0545 |
| Raw edge prob draw | 0.0493 |
| Raw ev draw | 0.0638 |
| Raw edge prob away | -0.0712 |
| Raw ev away | -0.1837 |

</details>


---

## 2026-10-31 — Bayer Leverkusen vs VfB Stuttgart

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **57.8%**. Expected goals are 2.29 for Bayer Leverkusen and 1.23 for VfB Stuttgart (3.51 combined). The most likely exact score is 2-1 at 9.2%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 68.3%; Under 3.5 goals: 53.6%; Double Chance 1X: 78.4%; Double Chance X2: 42.2%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 72.3%; BTTS Yes (both teams score): 64.5%; BTTS No (at least one team does not score): 35.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 57.8% | 1.73 |
| Draw | 20.6% | 4.85 |
| VfB Stuttgart win | 21.6% | 4.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.29 |
| VfB Stuttgart expected goals | 1.23 |
| Expected total goals | 3.51 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.3% |
| Under 2.5 | 31.7% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.7% |
| Under 4.5 | 72.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.16% |
| 2 | 1-1 | 9.02% |
| 3 | 2-0 | 7.47% |
| 4 | 3-1 | 6.98% |
| 5 | 1-2 | 5.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 57.8% | 55.3% | 1.79 | +3.4% |
| Draw | 20.6% | 20.0% | 4.35 | -10.3% |
| VfB Stuttgart win | 21.6% | 24.7% | 3.79 | -18.2% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.5% |
| P btts no | 35.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.33 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.92 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.15 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.12718523160840153, "-10": 9.426376934251807e-08, "-11": 1.0285527526209266e-08, "-12": 1.0319751080332306e-09, "-13": 9.581144653340402e-11, "-14": 8.276361115747461e-12, "-15": 6.683280171102965e-13, "-16": 5.0637222266345046e-14, "-17": 3.581581016918344e-15, "-18": 2.1095207108145146e-16, "-2": 0.0609692774942863, "-3": 0.020632095639966184, "-4": 0.005598744015405948, "-5": 0.001261230218763682, "-6": 0.00024214622370627765, "-7": 4.0435596235762045e-05, "-8": 5.967734000284472e-06, "-9": 7.885139864926027e-07, "0": 0.2062830286732527, "1": 0.20231377379187818, "10": 3.9800208535643315e-05, "11": 8.109075459350472e-06, "12": 1.5192114268503168e-06, "13": 2.6337261682681387e-07, "14": 4.2481210044418086e-08, "15": 6.405474995391649e-09, "16": 9.062244434050817e-10, "17": 1.1968642719136512e-10, "18": 1.3163098837016631e-11, "2": 0.17418782285436624, "3": 0.11006628549185762, "4": 0.05577066262742235, "5": 0.0234592317956592, "6": 0.00841010357923945, "7": 0.0026223564311287566, "8": 0.0007226725385828988, "9": 0.00017829769197983796} |
| Raw goal margin distribution | {"-1": 0.10877244547124032, "-10": 8.061706993066727e-08, "-11": 8.7964771368442e-09, "-12": 8.825746098559362e-10, "-13": 8.194068770235205e-11, "-14": 7.078180593598624e-12, "-15": 5.715732233901107e-13, "-16": 4.330639987148674e-14, "-17": 3.063070459808365e-15, "-18": 1.8041224093848837e-16, "-2": 0.052142668828776946, "-3": 0.017645157928913104, "-4": 0.004788205913704122, "-5": 0.0010786401334672792, "-6": 0.00020709037190146503, "-7": 3.458167769190096e-05, "-8": 5.103776695799402e-06, "-9": 6.743596997421457e-07, "0": 0.21228393424574396, "1": 0.21115888829578816, "10": 4.15402650586332e-05, "11": 8.463602487414244e-06, "12": 1.5856310223839499e-06, "13": 2.7488721076357674e-07, "14": 4.433847937445424e-08, "15": 6.68552097903513e-09, "16": 9.458443803867615e-10, "17": 1.2491909194389227e-10, "18": 1.3738586675820269e-11, "2": 0.1818032768566162, "3": 0.11487835972659075, "4": 0.05820894395475274, "5": 0.024484864344137224, "6": 0.00877779149170279, "7": 0.0027370052880437553, "8": 0.0007542676259207124, "9": 0.00018609282857279616} |
| Unadjusted home-win probability | 60.3% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 64.4% |
| P home draw | 78.4% |
| P draw away | 42.2% |
| P home away | 79.4% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.7% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.66 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +2.5% |
| Draw probability edge | +0.6% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | 0.0505 |
| Raw ev home | 0.0794 |
| Raw edge prob draw | 0.0120 |
| Raw ev draw | -0.0766 |
| Raw edge prob away | -0.0625 |
| Raw ev away | -0.3001 |

</details>


---

## 2026-10-31 — Borussia Monchengladbach vs SC Paderborn

The model's most likely 1X2 outcome is **Borussia Monchengladbach win** at **52.6%**. Expected goals are 1.56 for Borussia Monchengladbach and 0.85 for SC Paderborn (2.40 combined). The most likely exact score is 1-0 at 12.7%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.2%; Under 3.5 goals: 77.7%; Double Chance 1X: 77.5%; Double Chance X2: 47.4%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 52.6% | 1.90 |
| Draw | 25.0% | 4.00 |
| SC Paderborn win | 22.5% | 4.45 |

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
| 1 | 1-0 | 12.70% |
| 2 | 1-1 | 11.75% |
| 3 | 2-0 | 10.91% |
| 4 | 2-1 | 9.26% |
| 5 | 0-0 | 9.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 52.6% | 52.4% | 1.85 | -2.8% |
| Draw | 25.0% | 21.8% | 4.11 | +2.6% |
| SC Paderborn win | 22.5% | 25.8% | 3.74 | -16.0% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Dc lambda away | 0.8488 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.89 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.41 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.49 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.11 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.1483335925136727, "-10": 6.383225456225493e-09, "-11": 4.876948623363151e-10, "-12": 3.420731538362619e-11, "-13": 2.2171666271121823e-12, "-14": 1.331407506163028e-13, "-15": 6.924169245676735e-15, "-2": 0.05798437074406112, "-3": 0.014866618236476397, "-4": 0.002966724480499933, "-5": 0.00048298630524095624, "-6": 6.628689183301516e-05, "-7": 7.855496231447054e-06, "-8": 8.186356024360485e-07, "-9": 7.609990627778822e-08, "0": 0.2497189209360137, "1": 0.24229962619853246, "10": 2.323423914070455e-06, "11": 3.2536271818549657e-07, "12": 4.1828273111325044e-08, "13": 4.969132901898159e-09, "14": 5.469210218548385e-10, "15": 5.213298908806996e-11, "2": 0.16570992876710147, "3": 0.07787196029545185, "4": 0.028482458262778846, "5": 0.008498972172459113, "6": 0.0021379157275784604, "7": 0.0004643739908348037, "8": 8.869849010249645e-05, "9": 1.5112665045566321e-05} |
| Raw goal margin distribution | {"-1": 0.12645916573302127, "-10": 5.441905317608044e-09, "-11": 4.1577557974702397e-10, "-12": 2.91628382490701e-11, "-13": 1.8902059688863743e-12, "-14": 1.1350677862436283e-13, "-15": 5.903077322972625e-15, "-2": 0.04943354384929555, "-3": 0.012674270929444616, "-4": 0.002529228183623822, "-5": 0.00041176138315139783, "-6": 5.6511710518070637e-05, "-7": 6.697063578205456e-06, "-8": 6.97913220930516e-07, "-9": 6.487762142862653e-08, "0": 0.2817225022392976, "1": 0.2428223352886952, "10": 2.328436199145922e-06, "11": 3.2606461794928853e-07, "12": 4.1918508572782944e-08, "13": 4.979852732460015e-09, "14": 5.481008857869867e-10, "15": 5.2245454747721294e-11, "2": 0.16606741213369078, "3": 0.07803995222409757, "4": 0.028543903012313607, "5": 0.008517306868559485, "6": 0.0021425278188240797, "7": 0.0004653757773833542, "8": 8.888983792992686e-05, "9": 1.5145267355028536e-05} |
| Unadjusted home-win probability | 52.7% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 19.2% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 77.8% |
| Raw p btts yes | 46.5% |
| P home draw | 77.5% |
| P draw away | 47.4% |
| P home away | 75.0% |
| Raw p home draw | 80.8% |
| Raw p draw away | 47.3% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.02, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.74 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +0.1% |
| Draw probability edge | +3.2% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -22.1% |
| Under 2.5 probability edge | +22.1% |
| Raw edge prob home | 0.0023 |
| Raw ev home | -0.0256 |
| Raw edge prob draw | 0.0640 |
| Raw ev draw | 0.1579 |
| Raw edge prob away | -0.0663 |
| Raw ev away | -0.2835 |

</details>


---

## 2026-10-31 — FC Schalke 04 vs RB Leipzig

The model's most likely 1X2 outcome is **RB Leipzig win** at **57.3%**. Expected goals are 0.91 for FC Schalke 04 and 2.08 for RB Leipzig (3.00 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.2%; Under 3.5 goals: 65.6%; Double Chance 1X: 42.7%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 54.0%; BTTS No (at least one team does not score): 46.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 20.4% | 4.89 |
| Draw | 22.2% | 4.49 |
| RB Leipzig win | 57.3% | 1.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.91 |
| RB Leipzig expected goals | 2.08 |
| Expected total goals | 3.00 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.2% |
| Under 2.5 | 42.8% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.58% |
| 2 | 0-2 | 9.82% |
| 3 | 1-2 | 8.95% |
| 4 | 0-1 | 8.46% |
| 5 | 0-3 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 20.4% | 26.4% | 4.04 | -17.4% |
| Draw | 22.2% | 22.3% | 3.68 | -18.1% |
| RB Leipzig win | 57.3% | 51.3% | 1.88 | +7.7% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.0% |
| P btts no | 46.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.49 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.91 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.55 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.20750455826003628, "-10": 2.2884747665799298e-05, "-11": 4.2755187871420055e-06, "-12": 7.337915069692401e-07, "-13": 1.1644701490858869e-07, "-14": 1.71824889687389e-08, "-15": 2.368504279035759e-09, "-16": 3.0481297319595126e-10, "-17": 3.3613902649346375e-11, "-2": 0.177192397067257, "-3": 0.10748331004816097, "-4": 0.051402070467555155, "-5": 0.02020162266346198, "-6": 0.006723323004928689, "-7": 0.001937845003074643, "-8": 0.0004921643799579387, "-9": 0.000111663734964889, "0": 0.2224696549230505, "1": 0.13371301267261293, "10": 9.218700467679597e-09, "11": 7.536467935600922e-10, "12": 5.6598794086835584e-11, "13": 3.930233180130119e-12, "14": 2.5376486524523514e-13, "15": 1.5306470281370578e-14, "16": 8.619653075400678e-16, "17": 4.1594004842498615e-17, "2": 0.053103723623842476, "3": 0.014095366885117182, "4": 0.002949656376302546, "5": 0.0005072622317087782, "6": 7.38729955622794e-05, "7": 9.317002923410021e-06, "8": 1.0354349824913853e-06, "9": 1.027969586149082e-07} |
| Raw goal margin distribution | {"-1": 0.2294212531614181, "-10": 2.5301841712754648e-05, "-11": 4.7271003889566985e-06, "-12": 8.112947903396054e-07, "-13": 1.287461842344498e-07, "-14": 1.8997308708275855e-08, "-15": 2.6186664253110845e-09, "-16": 3.3700741264121406e-10, "-17": 3.716421332679793e-11, "-2": 0.19590751223355118, "-3": 0.11883573012543046, "-4": 0.056831172869850205, "-5": 0.022335324227131227, "-6": 0.007433442436800672, "-7": 0.002142520784920992, "-8": 0.0005441469322802284, "-9": 0.00012345769280029892, "0": 0.22197313580274625, "1": 0.09445190246925789, "10": 6.5118852687769615e-09, "11": 5.323593569452686e-10, "12": 3.998013111899873e-11, "13": 2.776229430414473e-12, "14": 1.7925386484973394e-13, "15": 1.0812150659594863e-14, "16": 6.088731495340364e-16, "17": 2.93810812438166e-17, "2": 0.037511290967277115, "3": 0.009956654118333082, "4": 0.002083571754190351, "5": 0.00035831877450106175, "6": 5.218224339200348e-05, "7": 6.581323940268658e-06, "8": 7.314082752662802e-07, "9": 7.26134885091877e-08} |
| Unadjusted home-win probability | 14.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 63.4% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 64.8% |
| Raw p btts yes | 53.4% |
| P home draw | 42.7% |
| P draw away | 79.6% |
| P home away | 77.8% |
| Raw p home draw | 36.6% |
| Raw p draw away | 85.6% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.15 |
| Reference draw odds | 3.65 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -6.0% |
| Draw probability edge | -0.0% |
| Away probability edge | +6.1% |
| Over 2.5 probability edge | -11.4% |
| Under 2.5 probability edge | +11.4% |
| Raw edge prob home | -0.1201 |
| Raw ev home | -0.4165 |
| Raw edge prob draw | -0.0010 |
| Raw ev draw | -0.1831 |
| Raw edge prob away | 0.1211 |
| Raw ev away | 0.1912 |

</details>


---

## 2026-10-31 — Werder Bremen vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **38.8%**. Expected goals are 1.82 for Werder Bremen and 1.59 for TSG Hoffenheim (3.42 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 66.7%; Under 3.5 goals: 55.5%; Double Chance 1X: 61.2%; Double Chance X2: 62.3%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 74.0%; BTTS Yes (both teams score): 67.8%; BTTS No (at least one team does not score): 32.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 37.7% | 2.65 |
| Draw | 23.5% | 4.25 |
| TSG Hoffenheim win | 38.8% | 2.58 |

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
| Over 3.5 | 44.5% |
| Under 3.5 | 55.5% |
| Over 4.5 | 26.0% |
| Under 4.5 | 74.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.15% |
| 2 | 1-2 | 8.94% |
| 3 | 2-1 | 7.71% |
| 4 | 2-2 | 6.64% |
| 5 | 0-1 | 4.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 37.7% | 32.9% | 2.92 | +10.0% |
| Draw | 23.5% | 22.5% | 3.91 | -8.0% |
| TSG Hoffenheim win | 38.8% | 44.6% | 2.21 | -14.3% |

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
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8229 |
| Dc lambda away | 1.5937 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:00.959120+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 67.8% |
| P btts no | 32.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.03 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.44 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.00 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.84 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.1939174423100142, "-10": 1.4608605936192607e-06, "-11": 2.0717797307982175e-07, "-12": 2.70199796984938e-08, "-13": 3.2610068592008937e-09, "-14": 3.6591970296754847e-10, "-15": 3.792546365457105e-11, "-16": 3.1971479353185753e-12, "-2": 0.11755959266943256, "-3": 0.05145841988833224, "-4": 0.01809330646694024, "-5": 0.005286822343716188, "-6": 0.0013174917152969797, "-7": 0.00028569660294965293, "-8": 5.477262458274541e-05, "-9": 9.403287550053465e-06, "0": 0.23531491395011325, "1": 0.16859144412158183, "10": 4.2219606673020055e-06, "11": 6.848614645722026e-07, "12": 1.0216400517540577e-07, "13": 1.4103222121188382e-08, "14": 1.81011501136777e-09, "15": 2.1458779433440866e-10, "16": 2.0691434022208396e-11, "2": 0.11596676661770243, "3": 0.058061154039243314, "4": 0.023350753451638166, "5": 0.007804254390846348, "6": 0.002224530349191641, "7": 0.0005517587897048238, "8": 0.00012099334329998444, "9": 2.37591765142964e-05} |
| Raw goal margin distribution | {"-1": 0.1648264883881764, "-10": 1.2417063612358447e-06, "-11": 1.7609771131126185e-07, "-12": 2.296651769417731e-08, "-13": 2.7717997040851144e-09, "-14": 3.110254495609697e-10, "-15": 3.223599135905859e-11, "-16": 2.717520717881578e-12, "-2": 0.09992363041313854, "-3": 0.043738771237702576, "-4": 0.01537899908719471, "-5": 0.004493707998962645, "-6": 0.0011198452822296836, "-7": 0.00024283719529127984, "-8": 4.655578818611312e-05, "-9": 7.992632574545519e-06, "0": 0.2455627488552502, "1": 0.19005428689297155, "10": 4.759445107639002e-06, "11": 7.720490084649783e-07, "12": 1.1517018109020407e-07, "13": 1.5898658660297446e-08, "14": 2.0405550202872116e-09, "15": 2.419062867671403e-10, "16": 2.332559495159089e-11, "2": 0.13073012837422932, "3": 0.06545273566286969, "4": 0.026323463914718185, "5": 0.008797789298927848, "6": 0.002507728262191622, "7": 0.0006220014536363736, "8": 0.00013639662261325484, "9": 2.6783882023884954e-05} |
| Unadjusted home-win probability | 42.5% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 33.0% |
| Raw p over 1 5 | 86.6% |
| Raw p under 3 5 | 55.5% |
| Raw p btts yes | 67.9% |
| P home draw | 61.2% |
| P draw away | 62.3% |
| P home away | 76.5% |
| Raw p home draw | 67.0% |
| Raw p draw away | 57.5% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +4.8% |
| Draw probability edge | +1.0% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.0959 |
| Raw ev home | 0.2400 |
| Raw edge prob draw | 0.0205 |
| Raw ev draw | -0.0398 |
| Raw edge prob away | -0.1164 |
| Raw ev away | -0.2712 |

</details>


---
