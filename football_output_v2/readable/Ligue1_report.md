# Ligue 1 — football model report

Fixtures in this report: **13**.

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
| Training sha256 | cb2f91190f3074680dd31b05e2b082dfb3251451e49ba3e50c937f2e3b49b566 |
| Training as of utc | 2026-10-22T10:57:29.078366+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 36, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T10:57:29.078366+00:00', 'observations': 145, 'observations_sha256': '83d72dab448935c06c471883514413dcf4dd8991baca1c8af1f2f211d0dd9caa', 'eligible_training_matches': 63, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 76, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 63, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '6dcf96a6a5eacbb7a83319034dd0c9898dbea66bda85c589a633a4c388882349', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5079.453 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.187 |
| Dixon-Coles low-score adjustment | -0.057 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 13.00 |
| Additional event odds calls used before this league | 4.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261022T105729078366Z_51a81d7da256ddae31710e20d95b25a8e11a7db2d5c1b00fc2c49cac3b9e2b76.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

The model's most likely 1X2 outcome is **Brest win** at **39.1%**. Expected goals are 1.22 for Brest and 1.24 for Nice (2.46 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.6%; Double Chance 1X: 67.4%; Double Chance X2: 60.9%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 39.1% | 2.56 |
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
| 1 | 1-1 | 13.48% |
| 2 | 1-0 | 10.78% |
| 3 | 0-0 | 9.17% |
| 4 | 0-1 | 8.90% |
| 5 | 2-1 | 8.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 39.1% | 43.0% | 2.30 | -10.2% |
| Draw | 28.4% | 28.0% | 3.36 | -4.7% |
| Nice win | 32.6% | 29.0% | 3.32 | +8.2% |
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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
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
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.91 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.64 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.1819766693657527, "-10": 2.0907085506860746e-07, "-11": 2.3298767777655067e-08, "-12": 2.3836889261738215e-09, "-13": 2.243684503149907e-10, "-14": 1.7933194112999368e-11, "-2": 0.0954125429278494, "-3": 0.035284989154875025, "-4": 0.010201197466025066, "-5": 0.00241200838228217, "-6": 0.0004815025431837771, "-7": 8.30807244933025e-05, "-8": 1.261442364986412e-05, "-9": 1.709312575736097e-06, "0": 0.2835662860151793, "1": 0.22043875306367305, "10": 2.171637542405231e-07, "11": 2.378901937332456e-08, "12": 2.3924502079202705e-09, "13": 2.213629119370603e-10, "14": 1.7392037452741353e-11, "2": 0.11368453302902497, "3": 0.04132716759943963, "4": 0.011744824978393334, "5": 0.0027297567555967283, "6": 0.0005356652380462379, "7": 9.085417629328595e-05, "8": 1.3560065098794631e-05, "9": 1.8061989754027758e-06} |
| Raw goal margin distribution | {"-1": 0.20179437465754754, "-10": 2.3183918358727946e-07, "-11": 2.5836060690470785e-08, "-12": 2.643278492302665e-09, "-13": 2.488027244481341e-10, "-14": 1.9886162903507718e-11, "-2": 0.10580320269470353, "-3": 0.03912761095212333, "-4": 0.011312132871699304, "-5": 0.0026746820065880043, "-6": 0.0005339393502279093, "-7": 9.212841900917395e-05, "-8": 1.3988165301418387e-05, "-9": 1.895460904505718e-06, "0": 0.2874149431703225, "1": 0.19823706592371382, "10": 1.952919115505291e-07, "11": 2.1393086906130713e-08, "12": 2.1514924349517685e-09, "13": 1.9906814730555567e-10, "14": 1.56403827691355e-11, "2": 0.10223469310803007, "3": 0.03716486477077868, "4": 0.010561934374722803, "5": 0.0024548268505158234, "6": 0.0004817152321531308, "7": 8.170371627031715e-05, "8": 1.2194350954902884e-05, "9": 1.6242860222260523e-06} |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 50.8% |
| P home draw | 67.4% |
| P draw away | 60.9% |
| P home away | 71.6% |
| Raw p home draw | 63.9% |
| Raw p draw away | 64.9% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.41, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.17, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:33Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.17, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.25 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | -3.9% |
| Draw probability edge | +0.4% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -11.6% |
| Under 2.5 probability edge | +11.6% |
| Raw edge prob home | -0.0787 |
| Raw ev home | -0.1922 |
| Raw edge prob draw | 0.0077 |
| Raw ev draw | -0.0343 |
| Raw edge prob away | 0.0710 |
| Raw ev away | 0.1997 |
| Market p home draw | 70.0% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:57:09Z |
| Market reference home draw last update utc | 2026-10-22T10:57:32Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.3% |
| Market draw away odds | 1.67 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:57:09Z |
| Market reference draw away last update utc | 2026-10-22T10:57:32Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.7% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:57:09Z |
| Market reference home away last update utc | 2026-10-22T10:57:32Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.35 |
| Market reference dc draw away odds | 1.65 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.0% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.8% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:33Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.81 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:33Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.3% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:57:09Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-22T10:57:32Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **46.6%**. Expected goals are 1.68 for RC Lens and 1.03 for Paris FC (2.70 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.8%; Double Chance 1X: 72.2%; Double Chance X2: 53.4%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 53.0%; BTTS No (at least one team does not score): 47.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 46.6% | 2.14 |
| Draw | 25.6% | 3.91 |
| Paris FC win | 27.8% | 3.60 |

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
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.21% |
| 2 | 1-0 | 9.50% |
| 3 | 2-1 | 8.68% |
| 4 | 2-0 | 8.46% |
| 5 | 0-1 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 46.6% | 41.3% | 2.40 | +11.9% |
| Draw | 25.6% | 25.6% | 3.67 | -6.0% |
| Paris FC win | 27.8% | 33.0% | 2.90 | -19.5% |
| Over 2.5 | 50.4% | 58.1% | 1.71 | -13.8% |
| Under 2.5 | 49.6% | 41.9% | 2.32 | +15.0% |

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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
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
| Dc lambda home | 1.6769 |
| Dc lambda away | 1.0254 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.0% |
| P btts no | 47.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.56 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.38 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.17402576457063987, "-10": 3.4265483591990885e-08, "-11": 3.1536278140920897e-09, "-12": 2.665729467989948e-10, "-13": 2.0827269178505593e-11, "-14": 1.50493582348365e-12, "-15": 9.229963903010642e-14, "-2": 0.07452045682289309, "-3": 0.022491735923314802, "-4": 0.005331495468968008, "-5": 0.0010362895015136847, "-6": 0.00017033668408810145, "-7": 2.4225826794319247e-05, "-8": 3.0341183330270405e-06, "-9": 3.3931365086018275e-07, "0": 0.2560352173618009, "1": 0.21052027437390688, "10": 3.4056394978059824e-06, "11": 5.125747381147355e-07, "12": 7.085455692448449e-08, "13": 9.052926540687065e-09, "14": 1.0697433591912458e-09, "15": 1.072918105317097e-10, "2": 0.14480304569158928, "3": 0.07147104242403952, "4": 0.02770519030681558, "5": 0.008806394652999244, "6": 0.0023671740268919263, "7": 0.0005505611453644533, "8": 0.00011276242788650615, "9": 2.062235164671429e-05} |
| Raw goal margin distribution | {"-1": 0.14089753798062962, "-10": 2.7742571841237023e-08, "-11": 2.553290863620634e-09, "-12": 2.158270758866497e-10, "-13": 1.686250859090536e-11, "-14": 1.218450341941331e-12, "-15": 7.472911800116798e-14, "-2": 0.060334450599557235, "-3": 0.018210120922750945, "-4": 0.00431657109615831, "-5": 0.0008390173705525312, "-6": 0.00013791072531708825, "-7": 1.9614103459256535e-05, "-8": 2.456531675755822e-06, "-9": 2.7472057443547375e-07, "0": 0.2555813346387206, "1": 0.2345802789101504, "10": 3.794864250669872e-06, "11": 5.71156034195988e-07, "12": 7.895240387099177e-08, "13": 1.0087570136335958e-08, "14": 1.1920025104834592e-09, "15": 1.1955400929509244e-10, "2": 0.16135233979907093, "3": 0.07963934645103436, "4": 0.030871569442706037, "5": 0.009812862538001078, "6": 0.002637714325181395, "7": 0.0006134838434007523, "8": 0.00012564985421414088, "9": 2.297924518413528e-05} |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 52.8% |
| P home draw | 72.2% |
| P draw away | 53.4% |
| P home away | 74.4% |
| Raw p home draw | 77.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.34 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +5.3% |
| Draw probability edge | -0.0% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.1066 |
| Raw ev home | 0.2472 |
| Raw edge prob draw | -0.0009 |
| Raw ev draw | -0.0620 |
| Raw edge prob away | -0.1057 |
| Raw ev away | -0.3482 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **59.8%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.8%; Double Chance 1X: 82.4%; Double Chance X2: 40.2%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 59.8% | 1.67 |
| Draw | 22.6% | 4.42 |
| Troyes win | 17.6% | 5.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.79% |
| 2 | 1-1 | 10.79% |
| 3 | 1-0 | 10.73% |
| 4 | 2-1 | 9.83% |
| 5 | 3-0 | 6.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 59.8% | 59.4% | 1.65 | -1.4% |
| Draw | 22.6% | 22.3% | 4.23 | -4.3% |
| Troyes win | 17.6% | 18.4% | 5.09 | -10.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T15:15:00+00:00 |
| Fixture id | 0bbce95e5764e706e6c428bb52dc5536 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 0.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9080 |
| Dc lambda away | 0.9103 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.49 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.44 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.11656528531106072, "-10": 7.866760755073348e-09, "-11": 6.426763234459286e-10, "-12": 4.822275141410193e-11, "-13": 3.3451795005100447e-12, "-14": 2.1570598064287387e-13, "-15": 1.2933326517034065e-14, "-16": 6.637982429125366e-16, "-2": 0.04450152337437951, "-3": 0.011910877567651123, "-4": 0.0025046886981465438, "-5": 0.0004319793089151696, "-6": 6.301224329166535e-05, "-7": 7.95368351789547e-06, "-8": 8.84140807325873e-07, "-9": 8.776236966166964e-08, "0": 0.22632210986252058, "1": 0.2384955787760406, "10": 1.2225587994682076e-05, "11": 2.093368207911187e-06, "12": 3.2921894589143025e-07, "13": 4.786651081298825e-08, "14": 6.469251589787445e-09, "15": 8.129832672754983e-10, "16": 8.745546916414017e-11, "2": 0.18570030132810636, "3": 0.10417439845852196, "4": 0.045914568508184365, "5": 0.016597367369857615, "6": 0.005074353434564114, "7": 0.0013424669058575854, "8": 0.0003127780216772892, "9": 6.507327194598512e-05} |
| Raw goal margin distribution | {"-1": 0.11147854110313644, "-10": 7.523466440653664e-09, "-11": 6.146308375438885e-10, "-12": 4.611837873752616e-11, "-13": 3.19920059775801e-12, "-14": 2.062928766923991e-13, "-15": 1.2368934437744282e-14, "-16": 6.348310263149442e-16, "-2": 0.04255953982701069, "-3": 0.011391103714596477, "-4": 0.0023953876254133462, "-5": 0.0004131283427659977, "-6": 6.026247810439841e-05, "-7": 7.606596017029735e-06, "-8": 8.455581528189773e-07, "-9": 8.393254396048512e-08, "0": 0.22993742172400056, "1": 0.24011741998447803, "10": 1.2308725646578644e-05, "11": 2.1076037373136473e-06, "12": 3.314577331083054e-07, "13": 4.8192017391093496e-08, "14": 6.513244433889261e-09, "15": 8.185117964474192e-10, "16": 8.805019248992066e-11, "2": 0.18696311887239286, "3": 0.10488281549984109, "4": 0.046226801295292434, "5": 0.016710234427981523, "6": 0.005108860554354709, "7": 0.0013515960820044014, "8": 0.0003149050056962514, "9": 6.551578964191675e-05} |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.4% |
| P draw away | 40.2% |
| P home away | 77.4% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.65 |
| Reference draw odds | 4.23 |
| Reference away odds | 5.09 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:29Z |
| Market reference home last update utc | 2026-10-21T17:28:29Z |
| Market reference draw last update utc | 2026-10-21T17:28:29Z |
| Market reference away last update utc | 2026-10-21T17:28:29Z |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Home probability edge | +0.4% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.8% |
| Raw edge prob home | 0.0081 |
| Raw ev home | -0.0071 |
| Raw edge prob draw | 0.0072 |
| Raw ev draw | -0.0274 |
| Raw edge prob away | -0.0154 |
| Raw ev away | -0.1433 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **44.2%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 53.2%; Under 3.5 goals: 68.7%; Double Chance 1X: 71.5%; Double Chance X2: 55.8%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 44.2% | 2.26 |
| Draw | 27.3% | 3.66 |
| Lille win | 28.5% | 3.51 |

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
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.92% |
| 2 | 2-1 | 9.27% |
| 3 | 1-0 | 8.73% |
| 4 | 2-0 | 7.33% |
| 5 | 1-2 | 6.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 44.2% | 44.9% | 2.16 | -4.6% |
| Draw | 27.3% | 28.5% | 3.22 | -12.0% |
| Lille win | 28.5% | 26.7% | 3.83 | +9.0% |
| Over 2.5 | 53.2% | 53.2% | 1.86 | -1.1% |
| Under 2.5 | 46.8% | 46.8% | 2.03 | -5.0% |

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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
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
| Dc lambda home | 1.5580 |
| Dc lambda away | 1.2640 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.48 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.48 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.1610261190036519, "-10": 1.9163457121055946e-07, "-11": 2.1700558969238786e-08, "-12": 2.2575440422963355e-09, "-13": 2.1710133409030435e-10, "-14": 1.9283696510444087e-11, "-15": 1.4363762678592705e-12, "-2": 0.08225460879203332, "-3": 0.030130751689385643, "-4": 0.008713891616782434, "-5": 0.0020726897815371457, "-6": 0.00041770505999474955, "-7": 7.292710525604672e-05, "-8": 1.1221886348832542e-05, "-9": 1.5428606873662739e-06, "0": 0.2734177957399941, "1": 0.2159035140999122, "10": 1.675552384356918e-06, "11": 2.338773625034632e-07, "12": 2.999070083010216e-08, "13": 3.555052274576753e-09, "14": 3.892305346564796e-10, "15": 3.5736988462704534e-11, "2": 0.13495204308100334, "3": 0.06093436716438252, "4": 0.021721889926143417, "5": 0.00636873057989273, "6": 0.0015820544367717486, "7": 0.00034046602316120173, "8": 6.45778801747312e-05, "9": 1.094404192333977e-05} |
| Raw goal margin distribution | {"-1": 0.17127002738412403, "-10": 2.0382568034340454e-07, "-11": 2.3081071269115258e-08, "-12": 2.4011609566035093e-09, "-13": 2.3091254800678025e-10, "-14": 2.0510456625586264e-11, "-15": 1.5277534120075506e-12, "-2": 0.08748735414757436, "-3": 0.03204756283561851, "-4": 0.009268238376873314, "-5": 0.0022045469259220607, "-6": 0.00044427796873229894, "-7": 7.75664680458749e-05, "-8": 1.1935782804418754e-05, "-9": 1.6410119911609943e-06, "0": 0.26193848588306445, "1": 0.21266291462676015, "10": 1.6504032143833666e-06, "11": 2.303669849124797e-07, "12": 2.95405560063152e-08, "13": 3.5016927886228088e-09, "14": 3.833883867377626e-10, "15": 3.5200594849719196e-11, "2": 0.1329264830917077, "3": 0.06001977400014909, "4": 0.02139585565410302, "5": 0.006273139245736412, "6": 0.0015583086223709328, "7": 0.00033535580520165624, "8": 6.360859977490097e-05, "9": 1.077977754515778e-05} |
| Unadjusted home-win probability | 43.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 71.5% |
| P draw away | 55.8% |
| P home away | 72.7% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.59, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.6, "price": 1.59, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.16 |
| Reference draw odds | 3.34 |
| Reference away odds | 3.56 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:29Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:29Z |
| Home probability edge | -0.7% |
| Draw probability edge | -1.1% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0133 |
| Raw ev home | -0.0599 |
| Raw edge prob draw | -0.0230 |
| Raw ev draw | -0.1566 |
| Raw edge prob away | 0.0362 |
| Raw ev away | 0.1598 |

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
| Angers win | 32.4% | 31.7% | 3.04 | -1.4% |
| Draw | 28.7% | 28.9% | 3.35 | -3.9% |
| Lorient win | 38.9% | 39.4% | 2.47 | -4.0% |
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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
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
| Goal margin distribution | {"-1": 0.21109270064829314, "-10": 3.648181779146932e-07, "-11": 4.2590781988655586e-08, "-12": 4.565029747783349e-09, "-13": 4.500817049282851e-10, "-14": 3.7610157947598846e-11, "-2": 0.1153711550917549, "-3": 0.04460581191515174, "-4": 0.013493062801317594, "-5": 0.00333959027418659, "-6": 0.0006980540802418408, "-7": 0.00012613807145348417, "-8": 2.0059649106830442e-05, "-9": 2.8472558335968004e-06, "0": 0.28694222187010604, "1": 0.1860131692481826, "10": 1.4684885434077683e-07, "11": 1.570892730992789e-08, "12": 1.542806114255877e-09, "13": 1.3937854376730014e-10, "14": 1.0672017859259549e-11, "2": 0.09345375300905476, "3": 0.03310760600329009, "4": 0.009176639996561662, "5": 0.002081148947401932, "6": 0.0003985986921388351, "7": 6.599785328528386e-05, "8": 9.617092161308819e-06, "9": 1.2507881579692578e-06} |
| Raw goal margin distribution | {"-1": 0.20826254364988575, "-10": 3.5992699638070095e-07, "-11": 4.2019759876840984e-08, "-12": 4.5038255903257555e-09, "-13": 4.4404738027780736e-10, "-14": 3.710591193909308e-11, "-2": 0.11382435370547063, "-3": 0.044007773942386204, "-4": 0.013312158933017931, "-5": 0.0032948157994782024, "-6": 0.0006886951463024107, "-7": 0.00012444691612412733, "-8": 1.979070585994915e-05, "-9": 2.8090821734040863e-06, "0": 0.28482008548134535, "1": 0.19021982817960212, "10": 1.501698183734747e-07, "11": 1.6064182261168245e-08, "12": 1.5776964349047547e-09, "13": 1.4253056788664988e-10, "14": 1.0913363885593978e-11, "2": 0.09556719511833729, "3": 0.03385632937085897, "4": 0.009384168284789754, "5": 0.002128213807608265, "6": 0.00040761293965214305, "7": 6.749038448669913e-05, "8": 9.83458120683267e-06, "9": 1.2790745378922567e-06} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.02 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | 0.0147 |
| Raw ev home | 0.0082 |
| Raw edge prob draw | -0.0042 |
| Raw ev draw | -0.0459 |
| Raw edge prob away | -0.0104 |
| Raw ev away | -0.0527 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **43.5%**. Expected goals are 1.73 for Auxerre and 1.52 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 62.5%; Under 3.5 goals: 59.4%; Double Chance 1X: 68.8%; Double Chance X2: 56.5%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 43.5% | 2.30 |
| Draw | 25.3% | 3.95 |
| Le Mans FC win | 31.2% | 3.20 |

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
| Over 3.5 | 40.6% |
| Under 3.5 | 59.4% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.27% |
| 2 | 2-1 | 9.07% |
| 3 | 1-2 | 7.24% |
| 4 | 2-2 | 6.97% |
| 5 | 1-0 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 43.5% | 44.6% | 2.13 | -7.4% |
| Draw | 25.3% | 26.3% | 3.77 | -4.5% |
| Le Mans FC win | 31.2% | 29.0% | 3.35 | +4.5% |
| Over 2.5 | 62.5% | 55.6% | 1.78 | +11.3% |
| Under 2.5 | 37.5% | 44.4% | 2.20 | -17.6% |

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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7258 |
| Dc lambda away | 1.5150 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.35 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.24 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.46 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.44 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.1618517756455429, "-10": 8.126990550639297e-07, "-11": 1.0979497780708247e-07, "-12": 1.3636688584130955e-08, "-13": 1.5669682324308032e-09, "-14": 1.6740868491019427e-10, "-15": 1.655121166043814e-11, "-16": 1.3471014614613605e-12, "-2": 0.09285060459848983, "-3": 0.039258842670125194, "-4": 0.013267118263613977, "-5": 0.003714522448318342, "-6": 0.000885216525619851, "-7": 0.00018332471007812673, "-8": 3.353406844855589e-05, "-9": 5.489244429674232e-06, "0": 0.2531837330975614, "1": 0.20344936915506348, "10": 3.2856563135672008e-06, "11": 5.05644326919889e-07, "12": 7.15388363686021e-08, "13": 9.364043578070758e-09, "14": 1.1395975427348412e-09, "15": 1.2834341681397806e-10, "16": 1.1899107744482522e-11, "2": 0.1324081851886771, "3": 0.06377315087605963, "4": 0.02454976096891822, "5": 0.007829678687484031, "6": 0.002125498245272847, "7": 0.0005014210129151856, "8": 0.0001044811765926694, "9": 1.948205043166519e-05} |
| Raw goal margin distribution | {"-1": 0.1731540380724204, "-10": 8.694505979974093e-07, "-11": 1.1746206485249426e-07, "-12": 1.4588951433251557e-08, "-13": 1.676391104727855e-09, "-14": 1.7909899156173934e-10, "-15": 1.7706998409906643e-11, "-16": 1.4411708293897674e-12, "-2": 0.09933445005202765, "-3": 0.04200032474941353, "-4": 0.014193573668046322, "-5": 0.003973911060732232, "-6": 0.0009470320320439217, "-7": 0.00019612644780618165, "-8": 3.587578413461973e-05, "-9": 5.872563554978882e-06, "0": 0.24292422516675805, "1": 0.19805325142287508, "10": 3.1985103648274744e-06, "11": 4.9223304759273e-07, "12": 6.964140122259035e-08, "13": 9.115679664206271e-09, "14": 1.1093718284283843e-09, "15": 1.2493934537273556e-10, "16": 1.1583505948498165e-11, "2": 0.12889630329417515, "3": 0.06208168615582476, "4": 0.023898624024942746, "5": 0.007622010960725592, "6": 0.0020691233407023123, "7": 0.00048812174917049793, "8": 0.00010171000688084836, "9": 1.896532512437966e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.7% |
| P home draw | 68.8% |
| P draw away | 56.5% |
| P home away | 74.7% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.7% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.65, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.45, "price": 1.65, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | -1.2% |
| Draw probability edge | -1.0% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +7.0% |
| Under 2.5 probability edge | -7.0% |
| Raw edge prob home | -0.0231 |
| Raw ev home | -0.0985 |
| Raw edge prob draw | -0.0205 |
| Raw ev draw | -0.0842 |
| Raw edge prob away | 0.0436 |
| Raw ev away | 0.1184 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **64.6%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.6%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 55.7%; Under 3.5 goals: 66.8%; Double Chance 1X: 84.9%; Double Chance X2: 35.4%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 64.6% | 1.55 |
| Draw | 20.3% | 4.92 |
| Le Havre win | 15.1% | 6.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.59% |
| 2 | 1-0 | 10.47% |
| 3 | 1-1 | 9.68% |
| 4 | 2-1 | 9.39% |
| 5 | 3-0 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 64.6% | 62.3% | 1.58 | +2.1% |
| Draw | 20.3% | 20.2% | 4.91 | -0.3% |
| Le Havre win | 15.1% | 17.4% | 4.95 | -25.5% |
| Over 2.5 | 55.7% | 60.5% | 1.65 | -8.0% |
| Under 2.5 | 44.3% | 39.5% | 2.45 | +8.5% |

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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1128 |
| Dc lambda away | 0.8100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.02 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.79 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.87 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.10437166516224526, "-10": 2.4971018780182813e-09, "-11": 1.815457564073966e-10, "-12": 1.2122358854303632e-11, "-13": 7.48322281422118e-13, "-14": 4.2947280916089787e-14, "-15": 2.3024412722122044e-15, "-16": 1.153355402560793e-16, "-17": 4.992705928649201e-18, "-2": 0.03577349871857241, "-3": 0.008533074444067739, "-4": 0.001598272593370444, "-5": 0.0002454470405294071, "-6": 3.1873687247130045e-05, "-7": 3.5812287000456043e-06, "-8": 3.543258214315808e-07, "-9": 3.1302533857437323e-08, "0": 0.2031184348139726, "1": 0.22955931591307357, "10": 2.9610724772561702e-05, "11": 5.6152998822329955e-06, "12": 9.78020741270874e-07, "13": 1.5747937479223496e-07, "14": 2.3574622905400402e-08, "15": 3.296641485459055e-09, "16": 4.307451424863722e-10, "17": 4.863705803842827e-11, "2": 0.19796188602338122, "3": 0.1231685351968676, "4": 0.06017542562295338, "5": 0.024104614742045446, "6": 0.008164860667136063, "7": 0.0023928892774320396, "8": 0.0006175433171582831, "9": 0.00014230435591079392} |
| Raw goal margin distribution | {"-1": 0.08789266537995546, "-10": 2.1028402626627e-09, "-11": 1.5288191861518978e-10, "-12": 1.0208387772110248e-11, "-13": 6.301714145803533e-13, "-14": 3.616643448841211e-14, "-15": 1.938914167757759e-15, "-16": 9.712547970165861e-17, "-17": 4.204419186425137e-18, "-2": 0.030125304099096854, "-3": 0.007185807140365463, "-4": 0.0013459250460045086, "-5": 0.00020669397741442978, "-6": 2.68412248025601e-05, "-7": 3.0157968189249685e-06, "-8": 2.9838214049907804e-07, "-9": 2.636024949491454e-08, "0": 0.20402543683795582, "1": 0.2376801601077155, "10": 3.0658227817306154e-05, "11": 5.813945601612437e-06, "12": 1.0126190063310319e-06, "13": 1.6305033348528845e-07, "14": 2.4408594024371183e-08, "15": 3.4132628116837044e-09, "16": 4.4598309602276993e-10, "17": 5.035763282253068e-11, "2": 0.20496494589258768, "3": 0.12752572052841296, "4": 0.062304179378324005, "5": 0.024957334745646362, "6": 0.00845369913611756, "7": 0.002477539647292931, "8": 0.0006393894053561748, "9": 0.00014733848618764153} |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 84.9% |
| P draw away | 35.4% |
| P home away | 79.7% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.57 |
| Reference draw odds | 4.60 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +2.3% |
| Draw probability edge | +0.1% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | 0.0457 |
| Raw ev home | 0.0573 |
| Raw edge prob draw | 0.0018 |
| Raw ev draw | 0.0018 |
| Raw edge prob away | -0.0475 |
| Raw ev away | -0.3724 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

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
| Paris Saint Germain win | 67.4% | 68.6% | 1.46 | -1.6% |
| Draw | 18.3% | 17.8% | 5.35 | -2.1% |
| Lyon win | 14.3% | 13.5% | 6.06 | -13.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4238 |
| Dc lambda away | 1.0958 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
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
| Goal margin distribution | {"-1": 0.09013467407130357, "-10": 2.4552165142771936e-08, "-11": 2.398359659613241e-09, "-12": 2.1539320803611614e-10, "-13": 1.7897868349305698e-11, "-14": 1.383569404723911e-12, "-15": 9.997578622887357e-14, "-16": 6.778286675878163e-15, "-17": 4.293564621864972e-16, "-18": 2.27771977354786e-17, "-2": 0.037751634208950585, "-3": 0.011518300988604417, "-4": 0.0028108926506425994, "-5": 0.0005685640036368029, "-6": 9.791694129839557e-05, "-7": 1.4656975816405712e-05, "-8": 1.938130437814815e-06, "-9": 2.2936392785597445e-07, "0": 0.18301594169881344, "1": 0.21952288056002325, "10": 7.387416847042132e-05, "11": 1.5961792701630782e-05, "12": 3.1707639129925013e-06, "13": 5.827707662829739e-07, "14": 9.964647615369292e-08, "15": 1.592650088928501e-08, "16": 2.388416271546753e-09, "17": 3.3463598356190333e-10, "18": 3.926625421147727e-11, "2": 0.198254106723363, "3": 0.1337948526546676, "4": 0.07222038332329847, "5": 0.03231167235752359, "6": 0.012308424359489659, "7": 0.0040752432835189974, "8": 0.0011919463765642177, "9": 0.0003120063116657172} |
| Raw goal margin distribution | {"-1": 0.09497662697344254, "-10": 2.587108517539774e-08, "-11": 2.5271973642356684e-09, "-12": 2.2696393572218357e-10, "-13": 1.8859325596352116e-11, "-14": 1.4578934976830097e-12, "-15": 1.0534639474620816e-13, "-16": 7.142410085431238e-15, "-17": 4.524211017334427e-16, "-18": 2.400076812960516e-17, "-2": 0.03977961774250078, "-3": 0.012137053665907761, "-4": 0.0029618912532071717, "-5": 0.0005991067459923493, "-6": 0.0001031769505342783, "-7": 1.544433525739825e-05, "-8": 2.0422450462581492e-06, "-9": 2.4168514993361445e-07, "0": 0.18769249993090134, "1": 0.21550001232329108, "10": 7.252038682772189e-05, "11": 1.566928474666553e-05, "12": 3.112658054508806e-06, "13": 5.720911961215628e-07, "14": 9.782040388824919e-08, "15": 1.5634639674698438e-08, "16": 2.344647330785826e-09, "17": 3.2850360927041936e-10, "18": 3.8546680167806636e-11, "2": 0.1946209995652185, "3": 0.13134299405291447, "4": 0.070896908133037, "5": 0.03171954455712679, "6": 0.012082866234187669, "7": 0.004000562381371569, "8": 0.001170103354069544, "9": 0.0003062886376006815} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.43 |
| Reference draw odds | 5.15 |
| Reference away odds | 6.70 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.05 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:31Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:31Z |
| Home probability edge | -1.2% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | -0.0247 |
| Raw ev home | -0.0339 |
| Raw edge prob draw | 0.0094 |
| Raw ev draw | 0.0042 |
| Raw edge prob away | 0.0154 |
| Raw ev away | -0.0875 |

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
| Rennes win | 54.1% | 56.1% | 1.77 | -4.3% |
| Draw | 22.7% | 21.8% | 4.45 | +0.8% |
| Strasbourg win | 23.3% | 22.1% | 4.06 | -5.5% |

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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9037 |
| Dc lambda away | 1.2515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
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
| Goal margin distribution | {"-1": 0.1351374841476082, "-10": 1.3055196718934538e-07, "-11": 1.4593250531378128e-08, "-12": 1.4992948975880898e-09, "-13": 1.4248359457861687e-10, "-14": 1.2589182126682087e-11, "-15": 1.0308045147890351e-12, "-16": 7.01761003944829e-14, "-2": 0.0658252258889415, "-3": 0.023295418490456857, "-4": 0.00656143374755166, "-5": 0.0015272499899233192, "-6": 0.00030209007324826436, "-7": 5.1869723746545504e-05, "-8": 7.860554879591918e-06, "-9": 1.065400202022583e-06, "0": 0.22653321789180297, "1": 0.22754698671505663, "10": 9.456778766014546e-06, "11": 1.6080444786809009e-06, "12": 2.5131550989939077e-07, "13": 3.633149774618984e-08, "14": 4.883173614065268e-09, "15": 6.08229066610552e-10, "16": 6.298923008254968e-11, "2": 0.16628860396537734, "3": 0.08952139804342424, "4": 0.03835670541699497, "5": 0.0135812233049621, "6": 0.004086499249893478, "7": 0.00106737029946035, "8": 0.0002460597583243897, "9": 5.073251281501804e-05} |
| Raw goal margin distribution | {"-1": 0.14201737162250194, "-10": 1.3719840470114374e-07, "-11": 1.5336197036428865e-08, "-12": 1.57562442415987e-09, "-13": 1.4973747460977482e-10, "-14": 1.3230100943388127e-11, "-15": 1.0832830636912386e-12, "-16": 7.374878548023994e-14, "-2": 0.06917640672512401, "-3": 0.024481394823417456, "-4": 0.006895478192302592, "-5": 0.0016050027181391858, "-6": 0.0003174695641744113, "-7": 5.45104260282327e-05, "-8": 8.26073794799024e-06, "-9": 1.1196400271301615e-06, "0": 0.2348837446829826, "1": 0.21904786308390461, "10": 9.103557951952709e-06, "11": 1.547982295366583e-06, "12": 2.419286064738769e-07, "13": 3.4974477398403544e-08, "14": 4.700781850247751e-09, "15": 5.8551105962742e-10, "16": 6.063651488455383e-11, "2": 0.1600775465307947, "3": 0.08617767795910859, "4": 0.03692404139393345, "5": 0.013073950070552271, "6": 0.003933864126726818, "7": 0.0010275028757414269, "8": 0.00023686916284852355, "9": 4.883759913253633e-05} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.74 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.86 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:31Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:31Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0404 |
| Raw ev home | -0.0786 |
| Raw edge prob draw | 0.0167 |
| Raw ev draw | 0.0452 |
| Raw edge prob away | 0.0237 |
| Raw ev away | -0.0071 |

</details>


---

## 2026-10-25 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **59.7%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.8%; Double Chance 1X: 82.1%; Double Chance X2: 40.3%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 59.7% | 1.68 |
| Draw | 22.5% | 4.45 |
| Troyes win | 17.9% | 5.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.78% |
| 2 | 1-1 | 10.71% |
| 3 | 1-0 | 10.71% |
| 4 | 2-1 | 9.81% |
| 5 | 3-0 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 59.7% | 59.2% | 1.71 | +2.0% |
| Draw | 22.5% | 22.0% | 4.26 | -4.3% |
| Troyes win | 17.9% | 18.9% | 5.13 | -8.4% |
| Over 2.5 | 53.6% | 60.0% | 1.67 | -10.4% |
| Under 2.5 | 46.4% | 40.0% | 2.40 | +11.3% |

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
| Market best home last update utc | 2026-10-21T17:28:09Z |
| Market best draw last update utc | 2026-10-21T17:28:09Z |
| Market best away last update utc | 2026-10-21T17:28:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9080 |
| Dc lambda away | 0.9103 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.60 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.1182543262858119, "-10": 7.980750792659798e-09, "-11": 6.51988758455253e-10, "-12": 4.892150321517464e-11, "-13": 3.3936514381815506e-12, "-14": 2.188315787901477e-13, "-15": 1.312073152675726e-14, "-16": 6.734167363452526e-16, "-2": 0.04514635426221711, "-3": 0.012083467204465563, "-4": 0.0025409818520548996, "-5": 0.00043823872612549396, "-6": 6.392529609762382e-05, "-7": 8.068933073765203e-06, "-8": 8.969520834020898e-07, "-9": 8.903405392001677e-08, "0": 0.22474471797544054, "1": 0.23810745849302323, "10": 1.220569245323472e-05, "11": 2.0899615256343764e-06, "12": 3.2868318522404256e-07, "13": 4.778861434287701e-08, "14": 6.458723731070632e-09, "15": 8.116602436060336e-10, "16": 8.731314685520009e-11, "2": 0.18539809843664076, "3": 0.10400486828433432, "4": 0.04583984856823632, "5": 0.01657035733070305, "6": 0.005066095589696463, "7": 0.001340282216992002, "8": 0.00031226901645833296, "9": 6.496737372827327e-05} |
| Raw goal margin distribution | {"-1": 0.11147854110313644, "-10": 7.523466440653664e-09, "-11": 6.146308375438885e-10, "-12": 4.611837873752616e-11, "-13": 3.19920059775801e-12, "-14": 2.062928766923991e-13, "-15": 1.2368934437744282e-14, "-16": 6.348310263149442e-16, "-2": 0.04255953982701069, "-3": 0.011391103714596477, "-4": 0.0023953876254133462, "-5": 0.0004131283427659977, "-6": 6.026247810439841e-05, "-7": 7.606596017029735e-06, "-8": 8.455581528189773e-07, "-9": 8.393254396048512e-08, "0": 0.22993742172400056, "1": 0.24011741998447803, "10": 1.2308725646578644e-05, "11": 2.1076037373136473e-06, "12": 3.314577331083054e-07, "13": 4.8192017391093496e-08, "14": 6.513244433889261e-09, "15": 8.185117964474192e-10, "16": 8.805019248992066e-11, "2": 0.18696311887239286, "3": 0.10488281549984109, "4": 0.046226801295292434, "5": 0.016710234427981523, "6": 0.005108860554354709, "7": 0.0013515960820044014, "8": 0.0003149050056962514, "9": 6.551578964191675e-05} |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.1% |
| P draw away | 40.3% |
| P home away | 77.5% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.67 |
| Reference draw odds | 4.40 |
| Reference away odds | 5.10 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +0.5% |
| Draw probability edge | +0.5% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0101 |
| Raw ev home | 0.0290 |
| Raw edge prob draw | 0.0104 |
| Raw ev draw | -0.0205 |
| Raw edge prob away | -0.0205 |
| Raw ev away | -0.1366 |

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
| Le Havre win | 9.7% | 8.1% | 9.70 | -6.1% |
| Draw | 15.8% | 13.0% | 6.87 | +8.3% |
| Paris Saint Germain win | 74.6% | 78.8% | 1.23 | -8.3% |

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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
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
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
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
| Goal margin distribution | {"-1": 0.2412925037995467, "-10": 6.491052834208239e-05, "-11": 1.3424217040593951e-05, "-12": 2.5503557215667683e-06, "-13": 4.480040157609365e-07, "-14": 7.317550527157542e-08, "-15": 1.1167679521350312e-08, "-16": 1.5990191115671757e-09, "-17": 2.1467209228201243e-10, "-18": 2.489593707081131e-11, "-2": 0.22271240574075465, "-3": 0.1495998509418685, "-4": 0.07921376578804988, "-5": 0.03446679608641774, "-6": 0.012699049458435046, "-7": 0.004051951873552105, "-8": 0.0011392087758034706, "-9": 0.00028611849178849646, "0": 0.1576155845829243, "1": 0.0672060739499038, "10": 1.7194247501135635e-09, "11": 1.2654471286994426e-10, "12": 8.555449046601783e-12, "13": 5.348240964651781e-13, "14": 3.1087213724497214e-14, "15": 1.6883637592021173e-15, "16": 8.602877587019189e-17, "17": 4.11010283137055e-18, "18": 1.6962606443632745e-19, "2": 0.02293593030745848, "3": 0.005482644942168678, "4": 0.0010331101555700168, "5": 0.00015996828741851826, "6": 2.0974480119105324e-05, "7": 2.3816134742457e-06, "8": 2.382853442971031e-07, "9": 2.1297417619005185e-08} |
| Raw goal margin distribution | {"-1": 0.22749522261582747, "-10": 6.11988970347812e-05, "-11": 1.2656610528730575e-05, "-12": 2.404524523104853e-06, "-13": 4.22386819704054e-07, "-14": 6.899127656121566e-08, "-15": 1.0529103469050992e-08, "-16": 1.5075860336512477e-09, "-17": 2.0239698562568283e-10, "-18": 2.3472369248814143e-11, "-2": 0.20997754810232377, "-3": 0.1410456224599005, "-4": 0.07468426494161264, "-5": 0.03249595957215422, "-6": 0.011972908557308901, "-7": 0.003820258312989858, "-8": 0.001074067987924794, "-9": 0.0002697580279493584, "0": 0.18481048795822025, "1": 0.07791822399527161, "10": 1.9934883106284224e-09, "11": 1.467150021316155e-10, "12": 9.919124210263507e-12, "13": 6.200710932393655e-13, "14": 3.604228516874586e-14, "15": 1.9574764279947596e-15, "16": 9.974112508475466e-17, "17": 4.7652227579467004e-18, "18": 1.9666320181176202e-19, "2": 0.026591747593656987, "3": 0.006356537907702812, "4": 0.0011977802567889723, "5": 0.00018546604672231318, "6": 2.431765678386512e-05, "7": 2.7612250091377207e-06, "8": 2.7626626196870204e-07, "9": 2.469206812758425e-08} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.8, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.26, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.75, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 2.0, "market_key": "spreads", "opposite_price": 2.05, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 10.50 |
| Reference draw odds | 6.75 |
| Reference away odds | 1.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:31Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:31Z |
| Home probability edge | +1.5% |
| Draw probability edge | +2.7% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | 0.0309 |
| Raw ev home | 0.0891 |
| Raw edge prob draw | 0.0544 |
| Raw ev draw | 0.2696 |
| Raw edge prob away | -0.0853 |
| Raw ev away | -0.1354 |

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
| Draw | 28.0% | 26.7% | 3.50 | -2.1% |
| RC Lens win | 32.6% | 32.8% | 3.02 | -1.6% |
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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2461 |
| Dc lambda away | 1.1238 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
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
| Goal margin distribution | {"-1": 0.19169632941566198, "-10": 9.452598355289929e-08, "-11": 9.556431291683198e-09, "-12": 8.869101701173359e-10, "-13": 7.576769473950627e-11, "-14": 5.528874924973274e-12, "-2": 0.09246970227449652, "-3": 0.031223772999925483, "-4": 0.008221444855077146, "-5": 0.0017679020589919507, "-6": 0.00032068671182377043, "-7": 5.0250189115977844e-05, "-8": 6.926111959029359e-06, "-9": 8.51738733511713e-07, "0": 0.2798107965822696, "1": 0.218182921182507, "10": 2.715172785275384e-07, "11": 3.0436716306556826e-08, "12": 3.132113397897955e-09, "13": 2.966864443901951e-10, "14": 2.4005247222352458e-11, "2": 0.11625173017392806, "3": 0.04352523598437781, "4": 0.012707487445267177, "5": 0.003029880711976571, "6": 0.0006094022888615525, "7": 0.00010588065143729351, "8": 1.618170201069735e-05, "9": 2.2064641572833654e-06} |
| Raw goal margin distribution | {"-1": 0.19050457824561345, "-10": 9.393832779630475e-08, "-11": 9.497020200150734e-09, "-12": 8.813963648390231e-10, "-13": 7.529665682692374e-11, "-14": 5.4945026280129e-12, "-2": 0.0918948301514069, "-3": 0.03102965886054984, "-4": 0.008170333200746602, "-5": 0.0017569112416207617, "-6": 0.0003186930442079117, "-7": 4.9937790219991296e-05, "-8": 6.883053220991856e-06, "-9": 8.464435844844344e-07, "0": 0.29293570855469797, "1": 0.21204302027795766, "10": 2.6387649172811003e-07, "11": 2.9580194535882484e-08, "12": 3.043972374848683e-09, "13": 2.883373703269913e-10, "14": 2.3329713874757557e-11, "2": 0.1129802820725743, "3": 0.04230038926244917, "4": 0.01234988514882308, "5": 0.002944616626120005, "6": 0.0005922530562619684, "7": 0.00010290105659086498, "8": 1.5726331598228075e-05, "9": 2.1443718945080055e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.38 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.92 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | -1.1% |
| Draw probability edge | +1.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -13.9% |
| Under 2.5 probability edge | +13.9% |
| Raw edge prob home | -0.0222 |
| Raw ev home | -0.1145 |
| Raw edge prob draw | 0.0262 |
| Raw ev draw | 0.0253 |
| Raw edge prob away | -0.0041 |
| Raw ev away | -0.0223 |

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
| Market best home last update utc | 2026-10-21T17:28:29Z |
| Market best draw last update utc | 2026-10-21T17:28:29Z |
| Market best away last update utc | 2026-10-21T17:28:29Z |
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
| Dc lambda away | 1.2984 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:29.078366+00:00 |
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
| Fair Over 4.5 odds | 7.70 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.2043228749508321, "-10": 3.3081660330485124e-07, "-11": 3.854373225680286e-08, "-12": 4.123531742883893e-09, "-13": 4.053733628610119e-10, "-14": 3.3430608690800485e-11, "-2": 0.10944855549433001, "-3": 0.041762398884864355, "-4": 0.012521797964397442, "-5": 0.0030795290265872685, "-6": 0.0006405864706340374, "-7": 0.00011531021183263556, "-8": 1.8280077388483772e-05, "-9": 2.5877933484605124e-06, "0": 0.2645366467861519, "1": 0.19530484482890775, "10": 4.2848414040357416e-07, "11": 5.16441652281395e-08, "12": 5.7155348940032685e-09, "13": 5.812497625639049e-10, "14": 4.958746502952372e-11, "2": 0.10809289515862151, "3": 0.04266704781143077, "4": 0.013234084155463392, "5": 0.003366910282724335, "6": 0.000724511104737234, "7": 0.00013491340293626006, "8": 2.212510798611664e-05, "9": 3.2400894767221524e-06} |
| Raw goal margin distribution | {"-1": 0.19328081635914016, "-10": 3.1293854477774947e-07, "-11": 3.6460743996068373e-08, "-12": 3.900686997181376e-09, "-13": 3.834660926872754e-10, "-14": 3.162394489944294e-11, "-2": 0.10353371427630557, "-3": 0.03950546678400561, "-4": 0.011845092398124073, "-5": 0.0029131044891752183, "-6": 0.0006059677655894442, "-7": 0.00010907859378408001, "-8": 1.7292181708017874e-05, "-9": 2.4479432911247022e-06, "0": 0.27554608861071694, "1": 0.20018786456574322, "10": 4.3919711844743445e-07, "11": 5.2935374764299796e-08, "12": 5.858434931728593e-09, "13": 5.957821929555669e-10, "14": 5.082725286300486e-11, "2": 0.11079543815459081, "3": 0.04373381108992616, "4": 0.01356496327004286, "5": 0.003451089911637789, "6": 0.0007426253610788396, "7": 0.000138286513367179, "8": 2.2678280842993113e-05, "9": 3.321098326644985e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:28:09Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:28:29Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.71 |
| Reference draw odds | 3.74 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:34Z |
| Market reference home last update utc | 2026-10-21T17:28:34Z |
| Market reference draw last update utc | 2026-10-21T17:28:34Z |
| Market reference away last update utc | 2026-10-21T17:28:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:34Z |
| Market best over 2 5 last update utc | 2026-10-21T17:28:09Z |
| Market best under 2 5 last update utc | 2026-10-21T17:28:09Z |
| Home probability edge | +0.9% |
| Draw probability edge | +1.1% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.0182 |
| Raw ev home | 0.0359 |
| Raw edge prob draw | 0.0220 |
| Raw ev draw | 0.0443 |
| Raw edge prob away | -0.0402 |
| Raw ev away | -0.1732 |

</details>


---
