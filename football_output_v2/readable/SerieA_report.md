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
| Training sha256 | 54fabd01f258eaa52feb07ff670b6fdbf8ffeaee99a112c5a2aaa9405e14cd1e |
| Training as of utc | 2026-10-22T10:56:43.751998+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 48, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T10:56:43.751998+00:00', 'observations': 172, 'observations_sha256': '943c549b5ca943465e3c153c71035645a7162c59d0d04c84f3ab792219315459', 'eligible_training_matches': 77, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 87, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 77, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'c98c6ae22a37b1aad953e39e2daf1ca0e6d7c8881df8003146fbe908751c263c', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2439.490 |
| Base scoring parameter | 0.132 |
| Home-advantage parameter | 0.126 |
| Dixon-Coles low-score adjustment | -0.034 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 3.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261022T105643751998Z_cd045a73db4473a6cc5d6e8dfad5a1f2b7faea32159b8013bd7c15fa35f398a9.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

The model's most likely 1X2 outcome is **Torino win** at **47.1%**. Expected goals are 1.51 for Torino and 1.00 for Monza (2.51 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 45.8%; Under 3.5 goals: 75.7%; Double Chance 1X: 73.8%; Double Chance X2: 52.9%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 89.0%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 47.1% | 2.12 |
| Draw | 26.7% | 3.75 |
| Monza win | 26.2% | 3.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.51 |
| Monza expected goals | 1.00 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.8% |
| Under 2.5 | 54.2% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 11.0% |
| Under 4.5 | 89.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 11.46% |
| 3 | 2-0 | 8.98% |
| 4 | 2-1 | 8.94% |
| 5 | 0-0 | 8.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 47.1% | 45.3% | 2.19 | +3.1% |
| Draw | 26.7% | 26.7% | 3.45 | -7.9% |
| Monza win | 26.2% | 28.0% | 3.49 | -8.5% |
| Over 2.5 | 45.8% | 48.5% | 1.98 | -9.3% |
| Under 2.5 | 54.2% | 51.5% | 1.91 | +3.5% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.71 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.18 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.12 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.16638689813296625, "-10": 2.639260059713393e-08, "-11": 2.362671674349149e-09, "-12": 1.942122861747072e-10, "-13": 1.475399353567852e-11, "-14": 1.0376249199726141e-12, "-15": 6.259696552932783e-14, "-2": 0.06943181412550997, "-3": 0.020630039993559977, "-4": 0.004791680022538765, "-5": 0.0009101748339653111, "-6": 0.00014596320051645073, "-7": 2.023191204725784e-05, "-8": 2.467693211363893e-06, "-9": 2.686141808734952e-07, "0": 0.2668418810020499, "1": 0.22959062434871322, "10": 1.5655239483727745e-06, "11": 2.1305894591803375e-07, "12": 2.6625144254894913e-08, "13": 3.0749901371845917e-09, "14": 3.287709231618971e-10, "15": 3.01526271775904e-11, "2": 0.14433946365826567, "3": 0.06519968744588975, "4": 0.023022480961964742, "5": 0.00664826016140785, "6": 0.0016208597200468554, "7": 0.0003415528000522298, "8": 6.333313080753718e-05, "9": 1.0480635015081628e-05} |
| Raw goal margin distribution | {"-1": 0.15525798717860737, "-10": 2.4627311952443057e-08, "-11": 2.2046426289539684e-09, "-12": 1.8122225352590124e-10, "-13": 1.3767161747105014e-11, "-14": 9.682226084446307e-13, "-15": 5.841012111305502e-14, "-2": 0.06478781579707849, "-3": 0.0192501844842054, "-4": 0.004471184954171066, "-5": 0.0008492971158651537, "-6": 0.00013620034370868283, "-7": 1.887868562055675e-05, "-8": 2.3026397226571193e-06, "-9": 2.5064772237488046e-07, "0": 0.26677824260222277, "1": 0.23817717482143747, "10": 1.624073597066374e-06, "11": 2.210272216173584e-07, "12": 2.7620908544646496e-08, "13": 3.1899929082731955e-09, "14": 3.410667568166985e-10, "15": 3.128031719489867e-11, "2": 0.14973767228905546, "3": 0.06763811631748717, "4": 0.02388350782378899, "5": 0.00689690106995395, "6": 0.0016814788931288072, "7": 0.000354326668171053, "8": 6.570175158992852e-05, "9": 1.0872604424975797e-05} |
| Unadjusted home-win probability | 48.8% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 71.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 49.6% |
| P home draw | 73.8% |
| P draw away | 52.9% |
| P home away | 73.3% |
| Raw p home draw | 75.5% |
| Raw p draw away | 51.2% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.48, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:56:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.48, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +1.8% |
| Draw probability edge | -0.0% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | 0.0352 |
| Raw ev home | 0.0697 |
| Raw edge prob draw | -0.0001 |
| Raw ev draw | -0.0796 |
| Raw edge prob away | -0.0351 |
| Raw ev away | -0.1457 |
| Market p home draw | 72.0% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:56:00Z |
| Market reference home draw last update utc | 2026-10-22T10:56:20Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.5% |
| Market draw away odds | 1.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:56:00Z |
| Market reference draw away last update utc | 2026-10-22T10:56:20Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.5% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:56:00Z |
| Market reference home away last update utc | 2026-10-22T10:56:20Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.74 |
| Market reference dc home draw odds | 1.34 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 74.6% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:56:14Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-22T10:56:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.5% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:56:14Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.35 |
| Market reference under 3 5 last update utc | 2026-10-22T10:56:14Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.4% |
| Market btts yes odds | 1.74 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:56:00Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.22 |
| Market reference btts yes last update utc | 2026-10-22T10:56:16Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **42.4%**. Expected goals are 1.04 for Cagliari and 1.43 for Bologna (2.47 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 44.1%; Under 3.5 goals: 76.6%; Double Chance 1X: 57.6%; Double Chance X2: 71.5%; Double Chance 12 (either team wins): 70.8%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 28.5% | 3.51 |
| Draw | 29.2% | 3.43 |
| Bologna win | 42.4% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.04 |
| Bologna expected goals | 1.43 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.84% |
| 2 | 0-1 | 10.88% |
| 3 | 0-0 | 9.47% |
| 4 | 1-0 | 8.83% |
| 5 | 1-2 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 28.5% | 29.8% | 3.30 | -6.1% |
| Draw | 29.2% | 30.9% | 2.97 | -13.3% |
| Bologna win | 42.4% | 39.2% | 2.54 | +7.6% |
| Over 2.5 | 44.1% | 43.3% | 2.24 | -1.2% |
| Under 2.5 | 55.9% | 56.7% | 1.76 | -1.6% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0400 |
| Dc lambda away | 1.4267 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.56 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.78 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.21591322981260508, "-10": 8.700317206878134e-07, "-11": 1.1159680383015522e-07, "-12": 1.3141246084630255e-08, "-13": 1.4238803196940888e-09, "-14": 1.3119534423216517e-10, "-2": 0.12837172720412549, "-3": 0.05472820651000416, "-4": 0.018229006556200324, "-5": 0.004963987577659907, "-6": 0.0011410325861044394, "-7": 0.0002266662428600735, "-8": 3.961863415023497e-05, "-9": 6.179727504319192e-06, "0": 0.29177840773251745, "1": 0.17646955339099055, "10": 4.1624443712838154e-08, "11": 3.892093779667604e-09, "12": 3.341075361062532e-10, "13": 2.6390121828771728e-11, "14": 1.7725745727971134e-12, "2": 0.07700825235394883, "3": 0.023933007846839167, "4": 0.005811219130843781, "5": 0.0011535943522602901, "6": 0.00019330303222753957, "7": 2.7992755397343804e-05, "8": 3.566781345226855e-06, "9": 4.055687616334642e-07} |
| Raw goal margin distribution | {"-1": 0.2318373074464513, "-10": 9.341984819194716e-07, "-11": 1.1982731462110052e-07, "-12": 1.4110442011340038e-08, "-13": 1.5288946385100017e-09, "-14": 1.40871290669377e-10, "-2": 0.13783942564837376, "-3": 0.058764532630376023, "-4": 0.019573436056146965, "-5": 0.005330092626566409, "-6": 0.0012251862597799494, "-7": 0.0002433833789587219, "-8": 4.2540595933229226e-05, "-9": 6.635496058289701e-06, "0": 0.274423529926943, "1": 0.16785811508863513, "10": 3.959323593781315e-08, "11": 3.702165688353582e-09, "12": 3.178036107081065e-10, "13": 2.510232514343308e-11, "14": 1.6860757049944276e-12, "2": 0.07325037003841449, "3": 0.022765114482218886, "4": 0.005527640722868485, "5": 0.0010973007514688557, "6": 0.0001838701464764349, "7": 2.662675269951265e-05, "8": 3.3927279921004954e-06, "9": 3.857776401563721e-07} |
| Unadjusted home-win probability | 27.1% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 49.6% |
| P home draw | 57.6% |
| P draw away | 71.5% |
| P home away | 70.8% |
| Raw p home draw | 54.5% |
| Raw p draw away | 72.9% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:06Z |
| Market reference home last update utc | 2026-10-21T17:24:06Z |
| Market reference draw last update utc | 2026-10-21T17:24:06Z |
| Market reference away last update utc | 2026-10-21T17:24:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -1.4% |
| Draw probability edge | -1.7% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.0278 |
| Raw ev home | -0.1066 |
| Raw edge prob draw | -0.0347 |
| Raw ev draw | -0.1850 |
| Raw edge prob away | 0.0625 |
| Raw ev away | 0.1554 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **64.0%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 59.8%; Under 3.5 goals: 62.9%; Double Chance 1X: 83.7%; Double Chance X2: 36.0%; Double Chance 12 (either team wins): 80.3%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 64.0% | 1.56 |
| Draw | 19.7% | 5.08 |
| Sassuolo win | 16.3% | 6.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 59.8% |
| Under 2.5 | 40.2% |
| Over 3.5 | 37.1% |
| Under 3.5 | 62.9% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.38% |
| 2 | 2-1 | 9.99% |
| 3 | 1-0 | 9.49% |
| 4 | 1-1 | 9.25% |
| 5 | 3-0 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 64.0% | 64.5% | 1.56 | -0.1% |
| Draw | 19.7% | 18.7% | 4.58 | -9.9% |
| Sassuolo win | 16.3% | 16.8% | 5.66 | -7.6% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1169 |
| Dc lambda away | 0.9623 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.31 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.43 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.10750407488859347, "-10": 1.0683397816706927e-08, "-11": 9.205839278941642e-10, "-12": 7.288239808794707e-11, "-13": 5.3358618516200414e-12, "-14": 3.6326932168382797e-13, "-15": 2.310457529726712e-14, "-16": 1.371096162016489e-15, "-17": 6.930768265362038e-17, "-2": 0.04118146551157513, "-3": 0.011437631462825521, "-4": 0.002511412711742122, "-5": 0.00045390767199145394, "-6": 6.954213327246748e-05, "-7": 9.23329616149022e-06, "-8": 1.0807456136339053e-06, "-9": 1.1304371867435999e-07, "0": 0.19666452527372083, "1": 0.2351000387425315, "10": 2.7723581750456227e-05, "11": 5.255107128535214e-06, "12": 9.152064810871362e-07, "13": 1.4739381416976877e-07, "14": 2.2074031147297984e-08, "15": 3.088368864417052e-09, "16": 4.031599088381052e-10, "17": 4.4830032004029915e-11, "2": 0.19490175733506204, "3": 0.1190771149130988, "4": 0.05751598219145863, "5": 0.02286737023495917, "6": 0.0077068153995792955, "7": 0.0022509298530540003, "8": 0.0005795713705799246, "9": 0.00013335463830967776} |
| Raw goal margin distribution | {"-1": 0.10438549599791032, "-10": 1.037348380696842e-08, "-11": 8.938787671120445e-10, "-12": 7.07681572239149e-11, "-13": 5.18107417355939e-12, "-14": 3.5273126496914087e-13, "-15": 2.243433613772897e-14, "-16": 1.3313221204055788e-15, "-17": 6.729714048291908e-17, "-2": 0.039986834990221556, "-3": 0.011105837937079215, "-4": 0.0024385592996575235, "-5": 0.000440740293120852, "-6": 6.752478993863259e-05, "-7": 8.965448058704452e-06, "-8": 1.0493943326673947e-06, "-9": 1.097644406084121e-07, "0": 0.20601292203643928, "1": 0.23340516989333077, "10": 2.752371859710058e-05, "11": 5.217222330986877e-06, "12": 9.08608630386312e-07, "13": 1.463312316813209e-07, "14": 2.1914896389311772e-08, "15": 3.0661043841084192e-09, "16": 4.0025347303149684e-10, "17": 4.45068460736545e-11, "2": 0.1934966834825501, "3": 0.11821867144452954, "4": 0.05710134148332058, "5": 0.02270251618524625, "6": 0.007651255896411402, "7": 0.0022347025869502496, "8": 0.0005753931600311794, "9": 0.0001323932661909134} |
| Unadjusted home-win probability | 63.6% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 54.7% |
| P home draw | 83.7% |
| P draw away | 36.0% |
| P home away | 80.3% |
| Raw p home draw | 84.2% |
| Raw p draw away | 36.4% |
| Raw p home away | 79.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.50 |
| Reference draw odds | 4.70 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:06Z |
| Market reference home last update utc | 2026-10-21T17:24:06Z |
| Market reference draw last update utc | 2026-10-21T17:24:06Z |
| Market reference away last update utc | 2026-10-21T17:24:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.68 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0092 |
| Raw ev home | -0.0085 |
| Raw edge prob draw | 0.0187 |
| Raw ev draw | -0.0565 |
| Raw edge prob away | -0.0095 |
| Raw ev away | -0.1033 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **63.8%**. Expected goals are 1.60 for Lazio and 0.71 for Parma (2.31 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 42.0%; Under 3.5 goals: 79.2%; Double Chance 1X: 86.2%; Double Chance X2: 36.2%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 63.8% | 1.57 |
| Draw | 22.4% | 4.47 |
| Parma win | 13.8% | 7.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.60 |
| Parma expected goals | 0.71 |
| Expected total goals | 2.31 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 42.0% |
| Under 2.5 | 58.0% |
| Over 3.5 | 20.8% |
| Under 3.5 | 79.2% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.93% |
| 2 | 2-0 | 13.90% |
| 3 | 1-1 | 10.19% |
| 4 | 2-1 | 9.82% |
| 5 | 0-0 | 9.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 63.8% | 69.0% | 1.43 | -8.8% |
| Draw | 22.4% | 19.2% | 4.67 | +4.6% |
| Parma win | 13.8% | 11.8% | 7.97 | +10.3% |
| Over 2.5 | 42.0% | 50.7% | 1.90 | -20.2% |
| Under 2.5 | 58.0% | 49.3% | 1.98 | +14.8% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Dc lambda away | 0.7068 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.07 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.81 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.25 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.09949076335770408, "-10": 8.20149647325635e-10, "-11": 5.225179181638083e-11, "-12": 3.055496646395717e-12, "-13": 1.6508773918369147e-13, "-14": 8.269391531210035e-15, "-15": 3.6228245724925873e-16, "-2": 0.030956885017476694, "-3": 0.0066940355904522315, "-4": 0.0011215326267300751, "-5": 0.00015291035923577613, "-6": 1.754829881441443e-05, "-7": 1.737226246461375e-06, "-8": 1.511314015136173e-07, "-9": 1.1722490393377542e-08, "0": 0.2239410556080045, "1": 0.28787994832394104, "10": 3.697308146496641e-06, "11": 5.342037469000904e-07, "12": 7.08436208619879e-08, "13": 8.680544256248975e-09, "14": 9.860952964600176e-10, "15": 9.79728707813438e-11, "2": 0.19945467727591346, "3": 0.09781110940849543, "4": 0.03716424178100964, "5": 0.011491149370093951, "6": 0.002990713279730978, "7": 0.0006714432883889116, "8": 0.00013247101424933283, "9": 2.3302323864008055e-05} |
| Raw goal margin distribution | {"-1": 0.11440661585979685, "-10": 9.431081085565518e-10, "-11": 6.008548404468399e-11, "-12": 3.5135827617310504e-12, "-13": 1.898380203601925e-13, "-14": 9.509155105222584e-15, "-15": 4.1659656153447057e-16, "-2": 0.035598002597254236, "-3": 0.0076976186783813, "-4": 0.0012896750217828224, "-5": 0.00017583498346649616, "-6": 2.0179174565536974e-05, "-7": 1.997674649714838e-06, "-8": 1.7378932087550667e-07, "-9": 1.3479949395236528e-08, "0": 0.2555186479820181, "1": 0.2642525670501036, "10": 3.3938562743786125e-06, "11": 4.90359652584365e-07, "12": 6.502922062094767e-08, "13": 7.968099607009202e-09, "14": 9.05162776923849e-10, "15": 8.993187179575829e-11, "2": 0.18308468786093238, "3": 0.08978338678221842, "4": 0.03411403381958224, "5": 0.010548027874406065, "6": 0.0027452542842283864, "7": 0.0006163354329412223, "8": 0.00012159862393655246, "9": 2.1389815216890268e-05} |
| Unadjusted home-win probability | 58.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 15.9% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 79.7% |
| Raw p btts yes | 40.9% |
| P home draw | 86.2% |
| P draw away | 36.2% |
| P home away | 77.6% |
| Raw p home draw | 84.1% |
| Raw p draw away | 41.5% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.41 |
| Reference draw odds | 4.60 |
| Reference away odds | 7.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.90 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | -5.2% |
| Draw probability edge | +3.2% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.1047 |
| Raw ev home | -0.1630 |
| Raw edge prob draw | 0.0632 |
| Raw ev draw | 0.1933 |
| Raw edge prob away | 0.0415 |
| Raw ev away | 0.2687 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.7%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.26 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 39.8%; Under 3.5 goals: 80.7%; Double Chance 1X: 64.9%; Double Chance X2: 63.3%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.7% | 2.73 |
| Draw | 28.2% | 3.54 |
| AS Roma win | 35.1% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.20 |
| AS Roma expected goals | 1.06 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 39.8% |
| Under 2.5 | 60.2% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.15% |
| 2 | 0-1 | 11.69% |
| 3 | 1-0 | 11.41% |
| 4 | 0-0 | 10.40% |
| 5 | 1-2 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 36.7% | 34.6% | 2.83 | +3.8% |
| Draw | 28.2% | 27.0% | 3.45 | -2.6% |
| AS Roma win | 35.1% | 38.4% | 2.56 | -10.2% |
| Over 2.5 | 39.8% | 50.7% | 1.92 | -23.6% |
| Under 2.5 | 60.2% | 49.3% | 1.97 | +18.6% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.61 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.51 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.17 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.45 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.21299570972566492, "-10": 6.421598052790662e-08, "-11": 6.134419992721191e-09, "-12": 5.35865037328513e-10, "-13": 3.982783395916658e-11, "-2": 0.09688681256448671, "-3": 0.03114665275911992, "-4": 0.007785023025238674, "-5": 0.001586513527657422, "-6": 0.0002724622649716127, "-7": 4.039431398585769e-05, "-8": 5.265448641411353e-06, "-9": 6.121772506182787e-07, "0": 0.28238623259375484, "1": 0.20735142942614562, "10": 1.920275346031765e-07, "11": 2.07863691984027e-08, "12": 2.057525823973326e-09, "13": 1.7328513245042188e-10, "2": 0.10658770666163889, "3": 0.03882742352431844, "4": 0.010996939493625443, "5": 0.002539454617400316, "6": 0.0004941829770028559, "7": 8.302070135060642e-05, "8": 1.2262705103091654e-05, "9": 1.6155218347170708e-06} |
| Raw goal margin distribution | {"-1": 0.19293704912842974, "-10": 5.81685039848956e-08, "-11": 5.556717048594418e-09, "-12": 4.854004766876362e-10, "-13": 3.6077087032203025e-11, "-2": 0.0877625926819263, "-3": 0.028213447497662747, "-4": 0.007051876170750145, "-5": 0.0014371051831175699, "-6": 0.0002468034002665035, "-7": 3.659021936186707e-05, "-8": 4.769580216050684e-06, "-9": 5.545260626609421e-07, "0": 0.2944154549707418, "1": 0.219219329373181, "10": 2.0301836101828012e-07, "11": 2.1976091162661686e-08, "12": 2.1752897124834576e-09, "13": 1.8320322474388675e-10, "2": 0.11268832647287025, "3": 0.041049737490819964, "4": 0.011626356797355361, "5": 0.0026848020278462054, "6": 0.0005224678754616194, "7": 8.777244760038398e-05, "8": 1.2964569361497107e-05, "9": 1.7079873245848519e-06} |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.8% |
| Raw p over 1 5 | 66.5% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 46.2% |
| P home draw | 64.9% |
| P draw away | 63.3% |
| P home away | 71.8% |
| Raw p home draw | 68.2% |
| Raw p draw away | 61.2% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.09, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.90 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +2.1% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0420 |
| Raw ev home | 0.0977 |
| Raw edge prob draw | 0.0241 |
| Raw ev draw | 0.0157 |
| Raw edge prob away | -0.0661 |
| Raw ev away | -0.1867 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **58.5%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.35 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.6%; Under 3.5 goals: 57.4%; Double Chance 1X: 79.4%; Double Chance X2: 41.5%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 58.5% | 1.71 |
| Draw | 20.8% | 4.80 |
| Frosinone win | 20.6% | 4.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.35 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.6% |
| Under 2.5 | 35.4% |
| Over 3.5 | 42.6% |
| Under 3.5 | 57.4% |
| Over 4.5 | 24.3% |
| Under 4.5 | 75.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.39% |
| 2 | 2-1 | 9.10% |
| 3 | 2-0 | 8.22% |
| 4 | 1-0 | 7.04% |
| 5 | 3-1 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 58.5% | 54.3% | 1.84 | +7.7% |
| Draw | 20.8% | 21.8% | 4.20 | -12.5% |
| Frosinone win | 20.6% | 24.0% | 3.95 | -18.5% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2476 |
| Dc lambda away | 1.1074 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.27 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.55 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.11 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.12946424952665048, "-10": 3.982551777851166e-08, "-11": 3.9361384222314376e-09, "-12": 3.5759825032658734e-10, "-13": 3.005456294915509e-11, "-14": 2.3496264230523854e-12, "-15": 1.7161806882213425e-13, "-16": 1.1668664377029624e-14, "-17": 6.630142081296651e-16, "-2": 0.05453660016963522, "-3": 0.01697417449023619, "-4": 0.004213008585286372, "-5": 0.0008651477035903106, "-6": 0.00015108758758031085, "-7": 2.2915901212368332e-05, "-8": 3.068737756336224e-06, "-9": 3.676323516488211e-07, "0": 0.20841281552387173, "1": 0.20809809901423723, "10": 3.6921890120380345e-05, "11": 7.406719904446275e-06, "12": 1.3657902491410824e-06, "13": 2.3298722218121442e-07, "14": 3.6970350507968264e-08, "15": 5.4808867090334474e-09, "16": 7.563834662662557e-10, "17": 8.723219040955788e-11, "2": 0.17552785399566306, "3": 0.11088676384718961, "4": 0.05586199670928101, "5": 0.02328345548065837, "6": 0.008253136453409336, "7": 0.0025407401121307774, "8": 0.0006905834138150147, "9": 0.00016792028125320885} |
| Raw goal margin distribution | {"-1": 0.108500712849367, "-10": 3.337675910038892e-08, "-11": 3.2987780506770687e-09, "-12": 2.9969404848041945e-10, "-13": 2.5187969005205793e-11, "-14": 1.9691624735245003e-12, "-15": 1.438287625588884e-13, "-16": 9.779212466273233e-15, "-17": 5.556554374999003e-16, "-2": 0.04570574514911355, "-3": 0.014225626294161211, "-4": 0.003530815931157711, "-5": 0.0007250584072649214, "-6": 0.00012662268552972485, "-7": 1.920523716947673e-05, "-8": 2.571831492691014e-06, "-9": 3.081033749952349e-07, "0": 0.1992331429697186, "1": 0.2232333062036137, "10": 3.960726043102945e-05, "11": 7.945418916491571e-06, "12": 1.4651256995651934e-06, "13": 2.4993264309997405e-07, "14": 3.965924539673747e-08, "15": 5.8795177215976036e-09, "16": 8.113960806571989e-10, "17": 9.357668505744735e-11, "2": 0.18829419088348456, "3": 0.11895168204364012, "4": 0.059924902128466954, "5": 0.024976887205665523, "6": 0.00885339628651814, "7": 0.00272553097852321, "8": 0.0007408103168917319, "9": 0.0001801333108777217} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 60.2% |
| P home draw | 79.4% |
| P draw away | 41.5% |
| P home away | 79.2% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.76 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:06Z |
| Market reference home last update utc | 2026-10-21T17:24:06Z |
| Market reference draw last update utc | 2026-10-21T17:24:06Z |
| Market reference away last update utc | 2026-10-21T17:24:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.92 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Home probability edge | +4.3% |
| Draw probability edge | -0.9% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0851 |
| Raw ev home | 0.1554 |
| Raw edge prob draw | -0.0184 |
| Raw ev draw | -0.1632 |
| Raw edge prob away | -0.0668 |
| Raw ev away | -0.3173 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **47.6%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 39.1%; Under 3.5 goals: 80.9%; Double Chance 1X: 76.1%; Double Chance X2: 52.4%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 47.6% | 2.10 |
| Draw | 28.6% | 3.50 |
| Venezia win | 23.9% | 4.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.76% |
| 2 | 1-1 | 13.16% |
| 3 | 0-0 | 11.03% |
| 4 | 2-0 | 9.90% |
| 5 | 0-1 | 9.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 47.6% | 46.0% | 2.16 | +2.8% |
| Draw | 28.6% | 28.9% | 3.22 | -8.0% |
| Venezia win | 23.9% | 25.0% | 3.83 | -8.6% |
| Over 2.5 | 39.1% | 48.5% | 2.02 | -21.1% |
| Under 2.5 | 60.9% | 51.5% | 1.87 | +14.0% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Dc lambda away | 0.8590 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.06 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.24 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.79 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.15960590932707147, "-10": 7.407642006740598e-09, "-11": 5.733199870250348e-10, "-12": 4.0726739726742445e-11, "-13": 2.6653076952198625e-12, "-14": 1.506253737895106e-13, "-2": 0.05957366705702543, "-3": 0.015584579650814369, "-4": 0.0031641110337255413, "-5": 0.0005232485074886825, "-6": 7.287499495764314e-05, "-7": 8.758477455981894e-06, "-8": 9.252571466021665e-07, "-9": 8.716440933051706e-08, "0": 0.28565787981832796, "1": 0.24150746112374188, "10": 8.861315154037943e-07, "11": 1.1158677806622679e-07, "12": 1.2897120563884279e-08, "13": 1.3732763047965864e-09, "14": 1.2627174143281852e-10, "2": 0.14510850232706077, "3": 0.061763383256103824, "4": 0.020402583256825937, "5": 0.005489577247125771, "6": 0.0012439613844838712, "7": 0.00024325088927457797, "8": 4.1810535245089e-05, "9": 6.408552248375025e-06} |
| Raw goal margin distribution | {"-1": 0.15165158220184438, "-10": 7.0384651510927206e-09, "-11": 5.447472684868836e-10, "-12": 3.869702909825544e-11, "-13": 2.5324759636972008e-12, "-14": 1.4311861228216487e-13, "-2": 0.05660467651138171, "-3": 0.014807886324267789, "-4": 0.0030064202920173674, "-5": 0.0004971712161534182, "-6": 6.924310218132693e-05, "-7": 8.321978612690068e-06, "-8": 8.791448312746315e-07, "-9": 8.282037076443039e-08, "0": 0.2820092666514041, "1": 0.2493933811224532, "10": 9.15066282910752e-07, "11": 1.1523041044366852e-07, "12": 1.3318249006489265e-08, "13": 1.418117764457342e-09, "14": 1.3039488051267892e-10, "2": 0.14984671635638916, "3": 0.0637801370944369, "4": 0.0210687868539394, "5": 0.005668827887234978, "6": 0.0012845803364362489, "7": 0.000251193737265729, "8": 4.3175770648218586e-05, "9": 6.6178100911890525e-06} |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 66.3% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.8% |
| P home draw | 76.1% |
| P draw away | 52.4% |
| P home away | 71.4% |
| Raw p home draw | 77.3% |
| Raw p draw away | 50.9% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.53, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.75, "price": 1.53, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.15 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:06Z |
| Market reference home last update utc | 2026-10-21T17:24:06Z |
| Market reference draw last update utc | 2026-10-21T17:24:06Z |
| Market reference away last update utc | 2026-10-21T17:24:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | 0.0311 |
| Raw ev home | 0.0613 |
| Raw edge prob draw | -0.0073 |
| Raw ev draw | -0.0919 |
| Raw edge prob away | -0.0238 |
| Raw ev away | -0.1319 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **71.5%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.34 combined). The most likely exact score is 2-0 at 10.5%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.6%; Under 3.5 goals: 56.8%; Double Chance 1X: 87.8%; Double Chance X2: 28.5%; Double Chance 12 (either team wins): 83.6%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 71.5% | 1.40 |
| Draw | 16.4% | 6.11 |
| Fiorentina win | 12.2% | 8.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.50% |
| 2 | 2-1 | 9.85% |
| 3 | 1-0 | 8.46% |
| 4 | 3-0 | 8.42% |
| 5 | 3-1 | 7.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 71.5% | 73.4% | 1.35 | -3.5% |
| Draw | 16.4% | 14.9% | 5.75 | -5.9% |
| Fiorentina win | 12.2% | 11.7% | 8.05 | -2.1% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4052 |
| Dc lambda away | 0.9383 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.69 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.72 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.01 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.08169085357350879, "-10": 6.071657976434994e-09, "-11": 5.093214713058048e-10, "-12": 3.9263126423725715e-11, "-13": 2.799511600335971e-12, "-14": 1.8564843588491355e-13, "-15": 1.150537644619707e-14, "-16": 6.690069938077002e-16, "-17": 3.6416878934322185e-17, "-18": 1.6868213704405915e-18, "-2": 0.029918189966796994, "-3": 0.007996690548198198, "-4": 0.001697087688250736, "-5": 0.00029721302666377297, "-6": 4.4193363016956896e-05, "-7": 5.700816283384909e-06, "-8": 6.487793067638932e-07, "-9": 6.601545901106585e-08, "0": 0.16361886432576678, "1": 0.22795885563204565, "10": 7.944151992444695e-05, "11": 1.7082364424366355e-05, "12": 3.37564391501428e-06, "13": 6.169781348121431e-07, "14": 1.0488045156624637e-07, "15": 1.6661720276028722e-08, "16": 2.483507158335949e-09, "17": 3.4653988958679785e-10, "18": 4.114673285400148e-11, "2": 0.20996627522163308, "3": 0.14386007119776595, "4": 0.07826183302643233, "5": 0.03513413981847845, "6": 0.01339165612005587, "7": 0.004428228621532125, "8": 0.001291831084787177, "9": 0.0003369536310137697} |
| Raw goal margin distribution | {"-1": 0.08487180266793379, "-10": 6.308081444876538e-09, "-11": 5.291538711651543e-10, "-12": 4.0791987991189434e-11, "-13": 2.9085214037640593e-12, "-14": 1.9287737521137247e-13, "-15": 1.1953382742943826e-14, "-16": 6.950573666221017e-16, "-17": 3.783491085589684e-17, "-18": 1.752504279555153e-18, "-2": 0.031083170317945875, "-3": 0.00830807259949233, "-4": 0.0017631703561254615, "-5": 0.0003087861644957423, "-6": 4.591420240005732e-05, "-7": 5.9227995973161165e-06, "-8": 6.740420364093271e-07, "-9": 6.858602603752423e-08, "0": 0.1783486801937012, "1": 0.22175005514656881, "10": 7.727781127576838e-05, "11": 1.6617100672111452e-05, "12": 3.283703202642185e-06, "13": 6.001738122411725e-07, "14": 1.0202387555477248e-07, "15": 1.6207913396485214e-08, "16": 2.4158651252699003e-09, "17": 3.3710135723086883e-10, "18": 4.0026040024537225e-11, "2": 0.20424752958257758, "3": 0.13994182692768958, "4": 0.07613025491536676, "5": 0.034177208955858726, "6": 0.013026914330187656, "7": 0.00430761918989175, "8": 0.0012566461324669774, "9": 0.00032777619475220866} |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 55.6% |
| P home draw | 87.8% |
| P draw away | 28.5% |
| P home away | 83.6% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.9, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.80 |
| Reference away odds | 7.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:04Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:04Z |
| Home probability edge | -1.9% |
| Draw probability edge | +1.5% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | -0.0389 |
| Raw ev home | -0.0614 |
| Raw edge prob draw | 0.0295 |
| Raw ev draw | 0.0255 |
| Raw edge prob away | 0.0095 |
| Raw ev away | 0.0174 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **63.0%**. Expected goals are 0.62 for Lecce and 1.48 for Juventus (2.11 combined). The most likely exact score is 0-1 at 19.3%. Goal-market probabilities: at least one goal: 89.1%; Over 2.5 goals: 36.6%; Under 3.5 goals: 83.2%; Double Chance 1X: 37.0%; Double Chance X2: 86.6%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 35.3%; BTTS No (at least one team does not score): 64.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.4% | 7.45 |
| Draw | 23.5% | 4.25 |
| Juventus win | 63.0% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.11 |
| Over 0.5 | 89.1% |
| Under 0.5 | 10.9% |
| Over 1.5 | 63.5% |
| Under 1.5 | 36.5% |
| Over 2.5 | 36.6% |
| Under 2.5 | 63.4% |
| Over 3.5 | 16.8% |
| Under 3.5 | 83.2% |
| Over 4.5 | 6.6% |
| Under 4.5 | 93.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.28% |
| 2 | 0-2 | 14.60% |
| 3 | 0-0 | 10.91% |
| 4 | 1-1 | 10.12% |
| 5 | 1-2 | 9.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.4% | 11.6% | 8.19 | +10.0% |
| Draw | 23.5% | 20.0% | 4.35 | +2.4% |
| Juventus win | 63.0% | 68.3% | 1.46 | -8.0% |
| Over 2.5 | 36.6% | 52.5% | 1.92 | -29.6% |
| Under 2.5 | 63.4% | 47.5% | 2.02 | +28.0% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.3% |
| P btts no | 64.7% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.17 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.74 |
| Fair Over 2.5 odds | 2.73 |
| Fair Under 2.5 odds | 1.58 |
| Fair Over 3.5 odds | 5.96 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.10 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.2990631226698067, "-10": 2.049861936859294e-06, "-11": 2.744845035631325e-07, "-12": 3.3727389489518316e-08, "-13": 3.828534620117089e-09, "-14": 4.031606315487747e-10, "-15": 3.754845269620226e-11, "-2": 0.1966124311658901, "-3": 0.09052533247887658, "-4": 0.03212426702595781, "-5": 0.009250135485599009, "-6": 0.002238127934469493, "-7": 0.00046661649194982446, "-8": 8.542438157301409e-05, "-9": 1.3935918095621074e-05, "0": 0.23536596404394264, "1": 0.09976209834022759, "10": 2.872357131238236e-10, "11": 1.6177707211323043e-11, "12": 8.361172503455347e-13, "13": 3.992108622212538e-14, "14": 1.7682073972196032e-15, "15": 6.926796785341996e-17, "2": 0.02812174568481993, "3": 0.005446114237767497, "4": 0.0008128963261907655, "5": 9.845444824998779e-05, "6": 1.001976352384513e-05, "7": 8.786541481207984e-07, "8": 6.765891640843103e-08, "9": 4.642630232129743e-09} |
| Raw goal margin distribution | {"-1": 0.27391281438839, "-10": 1.8774747191170569e-06, "-11": 2.5140118315419535e-07, "-12": 3.089101757038554e-08, "-13": 3.5065663844401908e-09, "-14": 3.692560361581306e-10, "-15": 3.439074086476949e-11, "-2": 0.1800779176102333, "-3": 0.0829124245456065, "-4": 0.02942271287978036, "-5": 0.0084722269389657, "-6": 0.0020499081131065394, "-7": 0.0004273754497345045, "-8": 7.824044825441911e-05, "-9": 1.2763949338120938e-05, "0": 0.2705380114720154, "1": 0.11301976222626939, "10": 3.2540726929615026e-10, "11": 1.8327607907307396e-11, "12": 9.472312070367674e-13, "13": 4.522631087060509e-14, "14": 2.0031894168760353e-15, "15": 7.847318156833123e-17, "2": 0.03185892301349438, "3": 0.006169863569934395, "4": 0.0009209243894145484, "5": 0.0001115383348632438, "6": 1.135131788393616e-05, "7": 9.954209519638234e-07, "8": 7.665029878270368e-08, "9": 5.259602330639955e-09} |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 57.7% |
| Raw p over 1 5 | 62.6% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 37.0% |
| P draw away | 86.6% |
| P home away | 76.5% |
| Raw p home draw | 42.3% |
| Raw p draw away | 84.8% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 7.25 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.42 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | +1.8% |
| Draw probability edge | +3.5% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -15.9% |
| Under 2.5 probability edge | +15.9% |
| Raw edge prob home | 0.0357 |
| Raw ev home | 0.2456 |
| Raw edge prob draw | 0.0703 |
| Raw ev draw | 0.1768 |
| Raw edge prob away | -0.1060 |
| Raw ev away | -0.1570 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **55.5%**. Expected goals are 1.04 for Udinese and 1.69 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 52.1%; Under 3.5 goals: 70.3%; Double Chance 1X: 44.5%; Double Chance X2: 79.4%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 20.6% | 4.84 |
| Draw | 23.8% | 4.20 |
| AC Milan win | 55.5% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.69 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 52.1% |
| Under 2.5 | 47.9% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.33% |
| 2 | 0-1 | 11.26% |
| 3 | 1-2 | 10.32% |
| 4 | 0-2 | 9.88% |
| 5 | 0-0 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 20.6% | 18.3% | 5.21 | +7.6% |
| Draw | 23.8% | 22.7% | 4.02 | -4.3% |
| AC Milan win | 55.5% | 58.9% | 1.68 | -6.7% |
| Over 2.5 | 52.1% | 51.4% | 1.91 | -0.6% |
| Under 2.5 | 47.9% | 48.6% | 1.98 | -5.1% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.23 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.24 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.90 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.2511580276520476, "-10": 4.298252126811827e-06, "-11": 6.526553248982058e-07, "-12": 9.102291059099443e-08, "-13": 1.173380421675581e-08, "-14": 1.398591631908073e-09, "-15": 1.4115759238237456e-10, "-2": 0.17150600485079406, "-3": 0.08517062927822282, "-4": 0.03325308200068999, "-5": 0.010652216257656881, "-6": 0.0028867179814959444, "-7": 0.0006770462073778257, "-8": 0.0001398585943511277, "-9": 2.5800470910727236e-05, "0": 0.23804976817915197, "1": 0.12942343196489564, "10": 2.9146153413671897e-08, "11": 2.7321664214820027e-09, "12": 2.3523822105447634e-10, "13": 1.8721037339538537e-11, "14": 1.377577057734327e-12, "15": 8.583474521143685e-14, "2": 0.05511850858567437, "3": 0.016898256089639154, "4": 0.004073032155978564, "5": 0.0008054893716131736, "6": 0.00013475909975562146, "7": 1.9512187349585626e-05, "8": 2.488345671458993e-06, "9": 2.8338906513284997e-07} |
| Raw goal margin distribution | {"-1": 0.23577465457342706, "-10": 4.03498514438304e-06, "-11": 6.126803320679275e-07, "-12": 8.544777765412063e-08, "-13": 1.1015111330108695e-08, "-14": 1.3129282069345125e-09, "-15": 1.3251172138713696e-10, "-2": 0.16100130037247015, "-3": 0.07995394726420832, "-4": 0.031216338157728826, "-5": 0.00999977039185042, "-6": 0.0027099071500952593, "-7": 0.0006355772784452119, "-8": 0.0001312922866950749, "-9": 2.4220197831924137e-05, "0": 0.24868534889825356, "1": 0.14408296799819278, "10": 3.2447480535916806e-08, "11": 3.041633505584235e-09, "12": 2.6188318885978196e-10, "13": 2.0841532193469663e-11, "14": 1.53361248509015e-12, "15": 9.555707695023073e-14, "2": 0.06136167298369815, "3": 0.01881228811834581, "4": 0.0045343764484984915, "5": 0.0008967255588192426, "6": 0.00015002299632126066, "7": 2.1722294199613205e-05, "8": 2.770195661682913e-06, "9": 3.1548798376517464e-07} |
| Unadjusted home-win probability | 23.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 53.3% |
| P home draw | 44.5% |
| P draw away | 79.4% |
| P home away | 76.2% |
| Raw p home draw | 47.9% |
| Raw p draw away | 77.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.90 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.64 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +2.3% |
| Draw probability edge | +1.1% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0468 |
| Raw ev home | 0.1976 |
| Raw edge prob draw | 0.0213 |
| Raw ev draw | -0.0003 |
| Raw edge prob away | -0.0680 |
| Raw ev away | -0.1240 |

</details>


---

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **69.3%**. Expected goals are 1.92 for AS Roma and 0.71 for Cagliari (2.63 combined). The most likely exact score is 1-0 at 14.2%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 50.1%; Under 3.5 goals: 72.4%; Double Chance 1X: 88.2%; Double Chance X2: 30.7%; Double Chance 12 (either team wins): 81.1%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 69.3% | 1.44 |
| Draw | 18.9% | 5.29 |
| Cagliari win | 11.8% | 8.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.92 |
| Cagliari expected goals | 0.71 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 50.1% |
| Under 2.5 | 49.9% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.21% |
| 2 | 2-0 | 13.99% |
| 3 | 2-1 | 9.94% |
| 4 | 3-0 | 8.96% |
| 5 | 1-1 | 8.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 69.3% | 72.8% | 1.34 | -7.2% |
| Draw | 18.9% | 16.3% | 4.80 | -9.2% |
| Cagliari win | 11.8% | 11.0% | 9.84 | +16.4% |
| Over 2.5 | 50.1% | 55.6% | 1.78 | -10.7% |
| Under 2.5 | 49.9% | 44.4% | 2.21 | +10.2% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 42.9% |
| P btts no | 57.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.16 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.61 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.08549627146357616, "-10": 6.847633023096876e-10, "-11": 4.376936707991746e-11, "-12": 2.5685341432671587e-12, "-13": 1.3930562227490324e-13, "-14": 7.021881769167872e-15, "-15": 3.2961130908669856e-16, "-16": 1.3482936430522989e-17, "-2": 0.02609624655440058, "-3": 0.0055828660556292665, "-4": 0.0009305797094748511, "-5": 0.00012661809850013055, "-6": 1.452873019531726e-05, "-7": 1.439836760032744e-06, "-8": 1.2549859488077523e-07, "-9": 9.758660559175084e-09, "0": 0.18919081908748536, "1": 0.2668812301127192, "10": 1.6201638109402184e-05, "11": 2.801206543407248e-06, "12": 4.4464828812717277e-07, "13": 6.523134631741961e-08, "14": 8.894010262053981e-09, "15": 1.1292825919929612e-09, "16": 1.249514879845568e-10, "2": 0.21544934034807672, "3": 0.12467539308747125, "4": 0.05621258181125583, "5": 0.020688650210561373, "6": 0.006421262801090396, "7": 0.0017213233453518511, "8": 0.00040583031112647206, "9": 8.535957529027881e-05} |
| Raw goal margin distribution | {"-1": 0.09158936121344657, "-10": 7.335645445974066e-10, "-11": 4.6888692371507254e-11, "-12": 2.751586676349853e-12, "-13": 1.4923356000425962e-13, "-14": 7.522312432401488e-15, "-15": 3.5310182223373265e-16, "-16": 1.444382911457382e-17, "-2": 0.027956055990165863, "-3": 0.005980741932040395, "-4": 0.0009968996271996168, "-5": 0.00013564183047010196, "-6": 1.556415379351984e-05, "-7": 1.5424500606347438e-06, "-8": 1.344425428331367e-07, "-9": 1.0454134099806691e-08, "0": 0.21581568667905943, "1": 0.25337373622143916, "10": 1.538163466555171e-05, "11": 2.659430816964043e-06, "12": 4.22143580572021e-07, "13": 6.192983271329551e-08, "14": 8.44386324634615e-09, "15": 1.0721269137669906e-09, "16": 1.1862739595326293e-10, "2": 0.20454493673976437, "3": 0.11836527487567089, "4": 0.05336752933188916, "5": 0.019641548410933282, "6": 0.006096267416351653, "7": 0.001634203076300192, "8": 0.00038529027372435936, "9": 8.103932413845099e-05} |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 43.7% |
| P home draw | 88.2% |
| P draw away | 30.7% |
| P home away | 81.1% |
| Raw p home draw | 87.3% |
| Raw p draw away | 34.2% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.10 |
| Reference away odds | 7.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:08Z |
| Market reference home last update utc | 2026-10-21T17:24:08Z |
| Market reference draw last update utc | 2026-10-21T17:24:08Z |
| Market reference away last update utc | 2026-10-21T17:24:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -3.5% |
| Draw probability edge | +2.7% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.0701 |
| Raw ev home | -0.1189 |
| Raw edge prob draw | 0.0532 |
| Raw ev draw | 0.0359 |
| Raw edge prob away | 0.0169 |
| Raw ev away | 0.2465 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **44.1%**. Expected goals are 1.17 for Sassuolo and 1.67 for Lazio (2.84 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.6%; Double Chance 1X: 55.9%; Double Chance X2: 69.6%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 30.4% | 3.28 |
| Draw | 25.5% | 3.93 |
| Lazio win | 44.1% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.17 |
| Lazio expected goals | 1.67 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 1-2 | 8.63% |
| 3 | 0-1 | 8.49% |
| 4 | 2-1 | 7.72% |
| 5 | 1-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 30.4% | 34.6% | 2.95 | -10.2% |
| Draw | 25.5% | 26.0% | 3.25 | -17.2% |
| Lazio win | 44.1% | 39.4% | 2.48 | +9.3% |
| Over 2.5 | 53.6% | 54.6% | 1.82 | -2.4% |
| Under 2.5 | 46.4% | 45.4% | 2.15 | -0.3% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sassuolo |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1681 |
| Dc lambda away | 1.6709 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.73 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.39 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.20430176277249826, "-10": 2.949418462895648e-06, "-11": 4.415659376864889e-07, "-12": 6.073162224897975e-08, "-13": 7.721327606686854e-09, "-14": 9.06802314181118e-10, "-15": 8.938125611212113e-11, "-2": 0.13528298292520335, "-3": 0.06557902143499302, "-4": 0.02508900912457437, "-5": 0.007892806064845426, "-6": 0.002103468120160799, "-7": 0.0004856089443759179, "-8": 9.880274431197316e-05, "-9": 1.7960421409363904e-05, "0": 0.25464613164247635, "1": 0.18146737121523482, "10": 1.0525637587739256e-07, "11": 1.1016421064479128e-08, "12": 1.0592361368144753e-09, "13": 9.414620759033936e-11, "14": 7.729589230527736e-12, "15": 5.326270187428345e-13, "2": 0.08462362677861913, "3": 0.028677833554178203, "4": 0.007670044111808242, "5": 0.0016868587892692665, "6": 0.0003142795879867472, "7": 5.072240792882641e-05, "8": 7.214647835955982e-06, "9": 9.168443143639342e-07} |
| Raw goal margin distribution | {"-1": 0.22584037709198385, "-10": 3.2603623621405103e-06, "-11": 4.88118244917641e-07, "-12": 6.7134283542089e-08, "-13": 8.535352386003207e-09, "-14": 1.002402396354238e-09, "-15": 9.880431921576113e-11, "-2": 0.14954525826572598, "-3": 0.0724927221831871, "-4": 0.02773403031214978, "-5": 0.008724909045368932, "-6": 0.0023252272863992585, "-7": 0.0005368045073562164, "-8": 0.0001092190724657937, "-9": 1.9853907713652386e-05, "0": 0.24968169934853682, "1": 0.15672758780241022, "10": 9.090657886106299e-08, "11": 9.514531940861234e-09, "12": 9.148285089729633e-10, "13": 8.131108043042006e-11, "14": 6.675799989229114e-12, "15": 4.60012989040012e-13, "2": 0.07308673072898388, "3": 0.02476813129680711, "4": 0.006624372767024824, "5": 0.001456886200725825, "6": 0.000271433268641316, "7": 4.3807327945396576e-05, "8": 6.231061510402984e-06, "9": 7.918492278712772e-07} |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 48.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 56.3% |
| P home draw | 55.9% |
| P draw away | 69.6% |
| P home away | 74.5% |
| Raw p home draw | 51.3% |
| Raw p draw away | 73.7% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.13, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:08Z |
| Market reference home last update utc | 2026-10-21T17:24:08Z |
| Market reference draw last update utc | 2026-10-21T17:24:08Z |
| Market reference away last update utc | 2026-10-21T17:24:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -4.2% |
| Draw probability edge | -0.5% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0830 |
| Raw ev home | -0.2242 |
| Raw edge prob draw | -0.0099 |
| Raw ev draw | -0.1885 |
| Raw edge prob away | 0.0930 |
| Raw ev away | 0.2086 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **52.4%**. Expected goals are 0.94 for Torino and 1.48 for Como (2.41 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.1%; Under 3.5 goals: 77.4%; Double Chance 1X: 47.6%; Double Chance X2: 77.8%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 46.8%; BTTS No (at least one team does not score): 53.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 22.2% | 4.50 |
| Draw | 25.4% | 3.93 |
| Como win | 52.4% | 1.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 0.94 |
| Como expected goals | 1.48 |
| Expected total goals | 2.41 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 22.6% |
| Under 3.5 | 77.4% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.59% |
| 2 | 1-1 | 11.98% |
| 3 | 0-2 | 10.37% |
| 4 | 1-2 | 9.70% |
| 5 | 0-0 | 8.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 22.2% | 20.9% | 4.89 | +8.6% |
| Draw | 25.4% | 23.7% | 3.55 | -9.8% |
| Como win | 52.4% | 55.4% | 1.76 | -7.8% |
| Over 2.5 | 44.1% | 54.6% | 1.82 | -19.8% |
| Under 2.5 | 55.9% | 45.4% | 2.15 | +20.2% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 46.8% |
| P btts no | 53.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.41 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.35 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.42 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.02 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.25800910207343264, "-10": 1.475386375983804e-06, "-11": 1.962154133925517e-07, "-12": 2.395815732210349e-08, "-13": 2.7033356923086776e-09, "-14": 2.82534717311251e-10, "-15": 2.5490420920192023e-11, "-2": 0.16054295011501457, "-3": 0.07138234575863585, "-4": 0.02473980810369612, "-5": 0.007000891162314219, "-6": 0.0016709540112857994, "-7": 0.00034448590350869896, "-8": 6.246651489705192e-05, "-9": 1.0105771056653204e-05, "0": 0.25418288902814457, "1": 0.144216972051866, "10": 1.3624390450059707e-08, "11": 1.147273652763522e-09, "12": 8.869719806522432e-11, "13": 6.336932115287003e-12, "14": 4.1934694639967885e-13, "15": 2.3955280425217192e-14, "2": 0.057388100224532994, "3": 0.016156378255813023, "4": 0.003545456092862906, "5": 0.0006352602757062054, "6": 9.600314442296557e-05, "7": 1.253184468355987e-05, "8": 1.4388430163092831e-06, "9": 1.4738666084078786e-07} |
| Raw goal margin distribution | {"-1": 0.24321537530258183, "-10": 1.3907906669474302e-06, "-11": 1.8496481335312835e-07, "-12": 2.258444441621004e-08, "-13": 2.5483318212029178e-09, "-14": 2.663347407306086e-10, "-15": 2.4028851078908005e-11, "-2": 0.15133773789613758, "-3": 0.06728942457512233, "-4": 0.02332127690263333, "-5": 0.006599474041075359, "-6": 0.001575144844512359, "-7": 0.0003247337696034893, "-8": 5.888480965375686e-05, "-9": 9.526326321488982e-06, "0": 0.2715058760958914, "1": 0.15247089123381202, "10": 1.4404150391473723e-08, "11": 1.2129351617714942e-09, "12": 9.377357357137575e-11, "13": 6.699611519776553e-12, "14": 4.4334728252886886e-13, "15": 2.5326304555022705e-14, "2": 0.06067257315805402, "3": 0.017081050563788475, "4": 0.0037483719330533654, "5": 0.0006716179033874604, "6": 0.0001014976585845503, "7": 1.3249075337810487e-05, "8": 1.5211918120380763e-06, "9": 1.558219897051274e-07} |
| Unadjusted home-win probability | 23.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.6% |
| Raw p btts yes | 47.3% |
| P home draw | 47.6% |
| P draw away | 77.8% |
| P home away | 74.6% |
| Raw p home draw | 50.6% |
| Raw p draw away | 76.5% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.20 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.72 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:08Z |
| Market reference home last update utc | 2026-10-21T17:24:08Z |
| Market reference draw last update utc | 2026-10-21T17:24:08Z |
| Market reference away last update utc | 2026-10-21T17:24:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | +1.3% |
| Draw probability edge | +1.7% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | 0.0254 |
| Raw ev home | 0.1480 |
| Raw edge prob draw | 0.0346 |
| Raw ev draw | -0.0362 |
| Raw edge prob away | -0.0601 |
| Raw ev away | -0.1310 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **55.4%**. Expected goals are 1.62 for AC Milan and 1.04 for Bologna (2.66 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.9%; Double Chance 1X: 79.2%; Double Chance X2: 44.6%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 55.4% | 1.80 |
| Draw | 23.7% | 4.21 |
| Bologna win | 20.8% | 4.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.62 |
| Bologna expected goals | 1.04 |
| Expected total goals | 2.66 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.03% |
| 2 | 1-1 | 11.31% |
| 3 | 2-1 | 10.51% |
| 4 | 2-0 | 10.07% |
| 5 | 0-0 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 55.4% | 60.6% | 1.60 | -11.3% |
| Draw | 23.7% | 21.9% | 4.07 | -3.4% |
| Bologna win | 20.8% | 17.5% | 5.39 | +12.1% |
| Over 2.5 | 50.5% | 52.5% | 1.83 | -7.6% |
| Under 2.5 | 49.5% | 47.5% | 2.01 | -0.5% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
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
| Dc lambda away | 1.0433 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.58 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.56 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.43 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.13002878612538504, "-10": 2.963405879437701e-08, "-11": 2.7755722113682257e-09, "-12": 2.387539201840559e-10, "-13": 1.8982423255373252e-11, "-14": 1.396021794482686e-12, "-15": 8.728400747124422e-14, "-2": 0.05575088302092474, "-3": 0.01715572543123709, "-4": 0.0041431922746201074, "-5": 0.0008201430473230463, "-6": 0.00013725535070458313, "-7": 1.9871927139081278e-05, "-8": 2.533286187925185e-06, "-9": 2.8834180193485573e-07, "0": 0.2374655158204214, "1": 0.2594110520232462, "10": 3.0157605142604907e-06, "11": 4.376701186519603e-07, "12": 5.8335581412053215e-08, "13": 7.1865975635872175e-09, "14": 8.189408315629226e-10, "15": 7.933844021018009e-11, "2": 0.17074509417881018, "3": 0.08141308737753053, "4": 0.03046553992848074, "5": 0.009344413587484413, "6": 0.0024231504630050048, "7": 0.0005436003628312297, "8": 0.00010737734478944057, "9": 1.8937588135563378e-05} |
| Raw goal margin distribution | {"-1": 0.15051529524533233, "-10": 3.4303012753284555e-08, "-11": 3.2128737283295263e-09, "-12": 2.7637047040361484e-10, "-13": 2.197317321719254e-11, "-14": 1.6159701157469984e-12, "-15": 1.010359209387814e-13, "-2": 0.06453463781466663, "-3": 0.019858672493800925, "-4": 0.0047959673165854436, "-5": 0.0009493595732886363, "-6": 0.0001588804314098629, "-7": 2.3002821679411365e-05, "-8": 2.9324146589263763e-06, "-9": 3.337711036381287e-07, "0": 0.2560027154260881, "1": 0.23540214975952073, "10": 2.736647119233688e-06, "11": 3.971630584457266e-07, "12": 5.2936531287951026e-08, "13": 6.521466617287244e-09, "14": 7.431465651605551e-10, "15": 7.199554235788677e-11, "2": 0.1549423662449891, "3": 0.07387817765571915, "4": 0.027645906127801444, "5": 0.008479573362737022, "6": 0.0021988840634709745, "7": 0.0004932892913485421, "8": 9.743940206772101e-05, "9": 1.718488446657442e-05} |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.3% |
| Raw p btts yes | 52.3% |
| P home draw | 79.2% |
| P draw away | 44.6% |
| P home away | 76.3% |
| Raw p home draw | 75.9% |
| Raw p draw away | 49.7% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.76, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | -5.1% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.1026 |
| Raw ev home | -0.1949 |
| Raw edge prob draw | 0.0371 |
| Raw ev draw | 0.0419 |
| Raw edge prob away | 0.0656 |
| Raw ev away | 0.2981 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **55.5%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.21 combined). The most likely exact score is 0-1 at 16.2%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.4%; Double Chance 1X: 44.5%; Double Chance X2: 81.2%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 41.1%; BTTS No (at least one team does not score): 58.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.8% | 5.32 |
| Draw | 25.7% | 3.89 |
| Juventus win | 55.5% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.21 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.6% |
| Under 3.5 | 81.4% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.23% |
| 2 | 0-2 | 11.94% |
| 3 | 1-1 | 11.66% |
| 4 | 0-0 | 10.44% |
| 5 | 1-2 | 9.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.8% | 17.5% | 5.59 | +5.1% |
| Draw | 25.7% | 23.5% | 3.88 | -0.3% |
| Juventus win | 55.5% | 59.0% | 1.62 | -10.1% |
| Over 2.5 | 39.0% | 46.1% | 2.05 | -20.1% |
| Under 2.5 | 61.0% | 53.9% | 1.80 | +9.8% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.1% |
| P btts no | 58.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.58 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.37 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.09 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.2749321227816978, "-10": 1.290521918867517e-06, "-11": 1.6664132790253477e-07, "-12": 1.9748501129661074e-08, "-13": 2.1567537945098468e-09, "-14": 2.043043443120841e-10, "-2": 0.17074215556560407, "-3": 0.07488575554602128, "-4": 0.025440338383139367, "-5": 0.0070319749803711695, "-6": 0.0016359212241833898, "-7": 0.00032827907839488076, "-8": 5.788715635311255e-05, "-9": 9.100698114857961e-06, "0": 0.2568549750989286, "1": 0.1302302863221379, "10": 2.6881613465493437e-09, "11": 1.8965433499062462e-10, "12": 1.2280167905579151e-11, "13": 7.327584680449953e-13, "14": 3.792520930036014e-14, "2": 0.04478265430132992, "3": 0.01073144975105502, "4": 0.0019919212904545352, "5": 0.00030082693320632344, "6": 3.823771182185956e-05, "7": 4.192401077244353e-06, "8": 4.0391682477871397e-07, "9": 3.4695611457386304e-08} |
| Raw goal margin distribution | {"-1": 0.2578612177160114, "-10": 1.2103916782129267e-06, "-11": 1.5629434385475636e-07, "-12": 1.8522290148699316e-08, "-13": 2.0228380523127422e-09, "-14": 1.9161881294902775e-10, "-2": 0.1601405456159168, "-3": 0.07023599832316896, "-4": 0.02386071357617439, "-5": 0.00659535020149979, "-6": 0.0015343446763779866, "-7": 0.00030789578914650235, "-8": 5.4292865003566714e-05, "-9": 8.535623535800611e-06, "0": 0.2786225467625606, "1": 0.13902204967019957, "10": 2.869637399990617e-09, "11": 2.024577778629462e-10, "12": 1.3109194187785524e-11, "13": 7.822265236277361e-13, "14": 4.0485515927266424e-14, "2": 0.047805902654953616, "3": 0.01145592306104614, "4": 0.0021263946229505026, "5": 0.0003211355670899268, "6": 4.081911529414865e-05, "7": 4.475427392951879e-06, "8": 4.311849913169554e-07, "9": 3.703788999922334e-08} |
| Unadjusted home-win probability | 20.1% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 41.7% |
| P home draw | 44.5% |
| P draw away | 81.2% |
| P home away | 74.3% |
| Raw p home draw | 47.9% |
| Raw p draw away | 79.9% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.90 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:24:01Z |
| Market best under 2 5 last update utc | 2026-10-21T17:24:01Z |
| Home probability edge | +1.3% |
| Draw probability edge | +2.2% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | 0.0254 |
| Raw ev home | 0.1223 |
| Raw edge prob draw | 0.0435 |
| Raw ev draw | 0.0811 |
| Raw edge prob away | -0.0689 |
| Raw ev away | -0.1566 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **56.5%**. Expected goals are 0.81 for Monza and 1.88 for Napoli (2.69 combined). The most likely exact score is 0-1 at 11.2%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.3%; Double Chance 1X: 43.5%; Double Chance X2: 80.0%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 20.0% | 4.99 |
| Draw | 23.5% | 4.26 |
| Napoli win | 56.5% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.81 |
| Napoli expected goals | 1.88 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 27.7% |
| Under 3.5 | 72.3% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 11.24% |
| 2 | 1-1 | 11.15% |
| 3 | 0-2 | 10.85% |
| 4 | 1-2 | 8.84% |
| 5 | 0-0 | 7.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 20.0% | 24.8% | 3.72 | -25.4% |
| Draw | 23.5% | 24.4% | 3.86 | -9.5% |
| Napoli win | 56.5% | 50.8% | 1.91 | +7.9% |
| Over 2.5 | 49.7% | 55.6% | 1.80 | -10.6% |
| Under 2.5 | 50.3% | 44.4% | 2.17 | +9.2% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8150 |
| Dc lambda away | 1.8784 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.50 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.61 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.58 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.22646159541747415, "-10": 1.0642527280478885e-05, "-11": 1.7966869497392479e-06, "-12": 2.785255622381411e-07, "-13": 3.991062188416276e-08, "-14": 5.315555585784779e-09, "-15": 6.588655184694383e-10, "-16": 7.059517164858229e-11, "-2": 0.17561768817378118, "-3": 0.09827387122547147, "-4": 0.043011081531346584, "-5": 0.015399262376044772, "-6": 0.0046556427387268624, "-7": 0.0012167065597749672, "-8": 0.000279826060121869, "-9": 5.743800566664131e-05, "0": 0.2345776131869034, "1": 0.13875519606573164, "10": 3.6183748527765158e-09, "11": 2.6503224883263516e-10, "12": 1.7825794347457504e-11, "13": 1.108229869308242e-12, "14": 6.403944275167502e-14, "15": 3.4439210235810404e-15, "16": 1.60099113301697e-16, "2": 0.047552882605659035, "3": 0.01154527231347714, "4": 0.002192320292804308, "5": 0.000340550155749159, "6": 4.4670245048588643e-05, "7": 5.065030466593808e-06, "8": 5.054077465582145e-07, "9": 4.50101657831015e-08} |
| Raw goal margin distribution | {"-1": 0.24910400536948687, "-10": 1.1706603797143254e-05, "-11": 1.976325896450865e-06, "-12": 3.063735068341554e-07, "-13": 4.390102326093968e-08, "-14": 5.8470231331813975e-09, "-15": 7.247411612905934e-10, "-16": 7.765351994889004e-11, "-2": 0.1931765492386126, "-3": 0.10809963119928265, "-4": 0.047311477537640215, "-5": 0.01693893364363537, "-6": 0.005121129927784398, "-7": 0.0013383570703921954, "-8": 0.00030780403297353884, "-9": 6.318085521573432e-05, "0": 0.22525055728734678, "1": 0.10610646810095534, "10": 2.7669808899376437e-09, "11": 2.026708667772165e-10, "12": 1.3631432428711884e-11, "13": 8.47466333589234e-13, "14": 4.8971132485118675e-14, "15": 2.633575581974616e-15, "16": 1.2242821847543886e-16, "2": 0.03636381601821659, "3": 0.008828700496855484, "4": 0.0016764731686539516, "5": 0.0002604196113899454, "6": 3.415945539844556e-05, "7": 3.873242291981687e-06, "8": 3.8648665029272494e-07, "9": 3.4419393689739215e-08} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 62.1% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.6% |
| Raw p btts yes | 47.6% |
| P home draw | 43.5% |
| P draw away | 80.0% |
| P home away | 76.5% |
| Raw p home draw | 37.9% |
| Raw p draw away | 84.7% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.60 |
| Reference draw odds | 3.65 |
| Reference away odds | 1.86 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -4.7% |
| Draw probability edge | -0.9% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0943 |
| Raw ev home | -0.4298 |
| Raw edge prob draw | -0.0187 |
| Raw ev draw | -0.1305 |
| Raw edge prob away | 0.1130 |
| Raw ev away | 0.1870 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **38.8%**. Expected goals are 1.05 for Parma and 1.17 for Udinese (2.22 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 38.4%; Under 3.5 goals: 81.6%; Double Chance 1X: 61.2%; Double Chance X2: 67.9%; Double Chance 12 (either team wins): 70.9%; Under 4.5 goals: 92.5%; BTTS Yes (both teams score): 45.0%; BTTS No (at least one team does not score): 55.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 32.1% | 3.12 |
| Draw | 29.1% | 3.44 |
| Udinese win | 38.8% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.05 |
| Udinese expected goals | 1.17 |
| Expected total goals | 2.22 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 38.4% |
| Under 2.5 | 61.6% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.45% |
| 2 | 0-1 | 12.53% |
| 3 | 0-0 | 11.06% |
| 4 | 1-0 | 10.98% |
| 5 | 1-2 | 7.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 32.1% | 32.1% | 3.00 | -3.7% |
| Draw | 29.1% | 28.3% | 3.26 | -5.2% |
| Udinese win | 38.8% | 39.6% | 2.45 | -4.8% |
| Over 2.5 | 38.4% | 43.4% | 2.22 | -14.7% |
| Under 2.5 | 61.6% | 56.6% | 1.77 | +9.0% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.0% |
| P btts no | 55.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.04 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.60 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.43 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.36 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.22272205282224983, "-10": 1.6176780423008226e-07, "-11": 1.701853580338577e-08, "-12": 1.637587081893395e-09, "-13": 1.344736499726856e-10, "-2": 0.11192008136627117, "-3": 0.03974661838983209, "-4": 0.010961105263220309, "-5": 0.0024628862979719944, "-6": 0.00046615591580435975, "-7": 7.614671313316423e-05, "-8": 1.093431349911846e-05, "-9": 1.4002348327731248e-06, "0": 0.2907489483308481, "1": 0.19564660966046488, "10": 5.364372340375472e-08, "11": 5.063211936506509e-09, "12": 4.3710463076498994e-10, "13": 3.220292248329535e-11, "2": 0.08841340608461222, "3": 0.028170034554894603, "4": 0.006969772987682566, "5": 0.0014050304518001548, "6": 0.00023858858656969676, "7": 3.496606141269488e-05, "8": 4.504682284454816e-06, "9": 5.175479720149085e-07} |
| Raw goal margin distribution | {"-1": 0.2184644649109726, "-10": 1.5867542680720744e-07, "-11": 1.6693206939961718e-08, "-12": 1.6062827235005718e-09, "-13": 1.3190303166500521e-10, "-2": 0.1097806004329013, "-3": 0.03898681611688091, "-4": 0.010751571143578512, "-5": 0.002415805396928645, "-6": 0.0004572448099360829, "-7": 7.46910812313786e-05, "-8": 1.0725291534826868e-05, "-9": 1.373467735301542e-06, "0": 0.2983490926020697, "1": 0.1955392684969218, "10": 5.3614291870558536e-08, "11": 5.06043401430549e-09, "12": 4.3686481408869887e-10, "13": 3.218525440729422e-11, "2": 0.08836489822700917, "3": 0.028154579115664557, "4": 0.006965949034160308, "5": 0.0014042595843480102, "6": 0.00023845768536708996, "7": 3.494687734544694e-05, "8": 4.502210798551511e-06, "9": 5.17264020242875e-07} |
| Unadjusted home-win probability | 32.1% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 45.2% |
| P home draw | 61.2% |
| P draw away | 67.9% |
| P home away | 70.9% |
| Raw p home draw | 61.9% |
| Raw p draw away | 67.9% |
| Raw p home away | 70.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.18 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -0.0% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | -0.0004 |
| Raw ev home | -0.0379 |
| Raw edge prob draw | 0.0152 |
| Raw ev draw | -0.0274 |
| Raw edge prob away | -0.0148 |
| Raw ev away | -0.0667 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **76.5%**. Expected goals are 0.69 for Venezia and 2.67 for Inter Milan (3.36 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 64.9%; Under 3.5 goals: 57.3%; Double Chance 1X: 23.5%; Double Chance X2: 90.4%; Double Chance 12 (either team wins): 86.1%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 46.9%; BTTS No (at least one team does not score): 53.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 9.6% | 10.42 |
| Draw | 13.9% | 7.20 |
| Inter Milan win | 76.5% | 1.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.69 |
| Inter Milan expected goals | 2.67 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 84.6% |
| Under 1.5 | 15.4% |
| Over 2.5 | 64.9% |
| Under 2.5 | 35.1% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 11.97% |
| 2 | 0-3 | 10.67% |
| 3 | 0-1 | 8.74% |
| 4 | 1-2 | 8.24% |
| 5 | 1-3 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 9.6% | 12.2% | 7.76 | -25.5% |
| Draw | 13.9% | 13.9% | 5.92 | -17.8% |
| Inter Milan win | 76.5% | 73.9% | 1.32 | +1.0% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6888 |
| Dc lambda away | 2.6747 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.9% |
| P btts no | 53.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.18 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.49 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.08 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.19940645445862853, "-10": 0.0002040235241449586, "-11": 4.893422272040872e-05, "-12": 1.0780986660063854e-05, "-13": 2.1961103543527754e-06, "-14": 4.159458615693133e-07, "-15": 7.360750631090153e-08, "-16": 1.222254860169149e-08, "-17": 1.9113309025075944e-09, "-18": 2.8135904214510046e-10, "-19": 3.610695641278057e-11, "-2": 0.2123230789179298, "-3": 0.1658728129801195, "-4": 0.10203872379555219, "-5": 0.05154813966266396, "-6": 0.022042512924083678, "-7": 0.008160554418506718, "-8": 0.0026616222579347757, "-9": 0.0007753910514773265, "0": 0.13893324699354434, "1": 0.0710969822155742, "10": 3.7348520918554384e-10, "11": 2.306817846024673e-11, "12": 1.3087797374075897e-12, "13": 6.865460285562819e-14, "14": 3.348572860325338e-15, "15": 1.525992840107656e-16, "16": 6.5252868759292276e-18, "17": 2.6277325698605643e-19, "18": 9.96124461332729e-21, "19": 3.291933515860949e-22, "2": 0.020096979995345925, "3": 0.004043116471362878, "4": 0.0006404917005139504, "5": 8.332377365787182e-05, "6": 9.175388960860043e-06, "7": 8.747631718359245e-07, "8": 7.347247855943208e-08, "9": 5.5119656380653875e-09} |
| Raw goal margin distribution | {"-1": 0.20632137041103732, "-10": 0.00021109854849964585, "-11": 5.063113889208801e-05, "-12": 1.1154844250786167e-05, "-13": 2.2722659560547992e-06, "-14": 4.3036982132183376e-07, "-15": 7.616003010451766e-08, "-16": 1.2646395946725466e-08, "-17": 1.9776110667277746e-09, "-18": 2.911158683931057e-10, "-19": 3.735905514533923e-11, "-2": 0.219685911026149, "-3": 0.17162486631089627, "-4": 0.10557717093786217, "-5": 0.053335699921122415, "-6": 0.022806892014337988, "-7": 0.008443541988203162, "-8": 0.0027539206454701604, "-9": 0.0008022796693296037, "0": 0.13880196064737355, "1": 0.05153917515635732, "10": 2.7074453815995963e-10, "11": 1.6722438184448384e-11, "12": 9.487523383596589e-13, "13": 4.976866094171946e-14, "14": 2.427426281594366e-15, "15": 1.1062130884147045e-16, "16": 4.730269735278948e-18, "17": 1.9048792925059148e-19, "18": 7.221042509862454e-21, "19": 2.386367645853116e-22, "2": 0.014568575765330433, "3": 0.0029309104479750773, "4": 0.000464301196904396, "5": 6.040254355973223e-05, "6": 6.651364995318796e-06, "7": 6.341277917659123e-07, "8": 5.3261204957540064e-08, "9": 3.995699305699154e-09} |
| Unadjusted home-win probability | 7.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 79.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 46.6% |
| P home draw | 23.5% |
| P draw away | 90.4% |
| P home away | 86.1% |
| Raw p home draw | 20.8% |
| Raw p draw away | 93.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 6.50 |
| Reference draw odds | 5.80 |
| Reference away odds | 1.31 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:08Z |
| Market reference home last update utc | 2026-10-21T17:24:08Z |
| Market reference draw last update utc | 2026-10-21T17:24:08Z |
| Market reference away last update utc | 2026-10-21T17:24:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Home probability edge | -2.6% |
| Draw probability edge | -0.0% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.0528 |
| Raw ev home | -0.4601 |
| Raw edge prob draw | -0.0003 |
| Raw ev draw | -0.1783 |
| Raw edge prob away | 0.0531 |
| Raw ev away | 0.0449 |

</details>


---

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Atalanta BC win** at **38.4%**. Expected goals are 1.25 for Fiorentina and 1.59 for Atalanta BC (2.84 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 53.9%; Under 3.5 goals: 68.5%; Double Chance 1X: 61.6%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 36.1% | 2.77 |
| Draw | 25.5% | 3.92 |
| Atalanta BC win | 38.4% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.25 |
| Atalanta BC expected goals | 1.59 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 2-1 | 8.82% |
| 3 | 1-0 | 8.38% |
| 4 | 1-2 | 7.91% |
| 5 | 0-1 | 7.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 36.1% | 42.4% | 2.30 | -17.1% |
| Draw | 25.5% | 25.6% | 3.54 | -9.7% |
| Atalanta BC win | 38.4% | 32.0% | 3.01 | +15.7% |
| Over 2.5 | 53.9% | 55.6% | 1.78 | -4.1% |
| Under 2.5 | 46.1% | 44.4% | 2.21 | +1.9% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2523 |
| Dc lambda away | 1.5904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.04 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.34 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.18616126306189035, "-10": 1.7040251626621997e-06, "-11": 2.427463070829197e-07, "-12": 3.176931079638913e-08, "-13": 3.843508542908529e-09, "-14": 4.294331893062905e-10, "-15": 4.0193262985467595e-11, "-2": 0.11697656706855414, "-3": 0.053840460154675265, "-4": 0.019573480798468004, "-5": 0.005854127019566217, "-6": 0.0014836839053423707, "-7": 0.00032580076451510753, "-8": 6.305993854809858e-05, "-9": 1.0905931691021482e-05, "0": 0.2551645250828205, "1": 0.20672451592567434, "10": 2.213600728370956e-07, "11": 2.4831289305105723e-08, "12": 2.559044182586944e-09, "13": 2.437929789892974e-10, "14": 2.1449259454005152e-11, "15": 1.580859645852601e-12, "2": 0.10278632439974256, "3": 0.03725362854202006, "4": 0.010664763613950568, "5": 0.002511705192906682, "6": 0.0005012694768090365, "7": 8.667729042565341e-05, "8": 1.3210830589553484e-05, "9": 1.799130665529561e-06} |
| Raw goal margin distribution | {"-1": 0.21730530663029593, "-10": 1.9891018377703154e-06, "-11": 2.833568048820595e-07, "-12": 3.708419093475616e-08, "-13": 4.4865123319196e-09, "-14": 5.012756646822129e-10, "-15": 4.691743703213607e-11, "-2": 0.13654628442728514, "-3": 0.06284775635164372, "-4": 0.02284804677823455, "-5": 0.006833499333406485, "-6": 0.0017318983589280387, "-7": 0.0003803059447969205, "-8": 7.360961704329678e-05, "-9": 1.2730450960781204e-05, "0": 0.25442286204439574, "1": 0.17028768437134145, "10": 1.823436085793196e-07, "11": 2.0454578097750197e-08, "12": 2.107992398024823e-09, "13": 2.0082253753108229e-10, "14": 1.7668657766821788e-11, "15": 1.3022206253714328e-12, "2": 0.08466942146990822, "3": 0.030687381757524928, "4": 0.008785014646450219, "5": 0.00206899727982593, "6": 0.0004129167654335443, "7": 7.139973218983662e-05, "8": 1.0882317172898746e-05, "9": 1.4820196508509489e-06} |
| Unadjusted home-win probability | 29.7% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 57.2% |
| P home draw | 61.6% |
| P draw away | 63.9% |
| P home away | 74.5% |
| Raw p home draw | 55.1% |
| Raw p draw away | 70.3% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | -6.4% |
| Draw probability edge | -0.1% |
| Away probability edge | +6.4% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.1271 |
| Raw ev home | -0.3169 |
| Raw edge prob draw | -0.0015 |
| Raw ev draw | -0.0993 |
| Raw edge prob away | 0.1286 |
| Raw ev away | 0.3502 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **50.0%**. Expected goals are 1.56 for Frosinone and 0.97 for Lecce (2.53 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 46.8%; Under 3.5 goals: 75.1%; Double Chance 1X: 75.2%; Double Chance X2: 50.0%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.3%; BTTS No (at least one team does not score): 50.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 50.0% | 2.00 |
| Draw | 25.2% | 3.97 |
| Lecce win | 24.8% | 4.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.56 |
| Lecce expected goals | 0.97 |
| Expected total goals | 2.53 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 72.3% |
| Under 1.5 | 27.7% |
| Over 2.5 | 46.8% |
| Under 2.5 | 53.2% |
| Over 3.5 | 24.9% |
| Under 3.5 | 75.1% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.97% |
| 2 | 1-0 | 11.83% |
| 3 | 2-0 | 9.55% |
| 4 | 2-1 | 9.28% |
| 5 | 0-0 | 8.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 50.0% | 49.3% | 1.96 | -2.0% |
| Draw | 25.2% | 24.2% | 3.58 | -9.8% |
| Lecce win | 24.8% | 26.5% | 3.81 | -5.5% |
| Over 2.5 | 46.8% | 60.9% | 1.69 | -21.0% |
| Under 2.5 | 53.2% | 39.1% | 2.37 | +26.2% |

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
| Market best home last update utc | 2026-10-21T17:24:01Z |
| Market best draw last update utc | 2026-10-21T17:24:01Z |
| Market best away last update utc | 2026-10-21T17:24:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Frosinone |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5624 |
| Dc lambda away | 0.9710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:56:43.751998+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.3% |
| P btts no | 50.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.46 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.61 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.01 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.77 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.1593146019895326, "-10": 2.0091191020106533e-08, "-11": 1.7536310435696638e-09, "-12": 1.4054888525077386e-10, "-13": 1.0410667849379287e-11, "-14": 7.138543193107688e-13, "-15": 4.196763962480911e-14, "-2": 0.06480486851528483, "-3": 0.018763878594805463, "-4": 0.004247926127786518, "-5": 0.0007865625077408073, "-6": 0.0001229712020995374, "-7": 1.6617656119005772e-05, "-8": 1.976111159904903e-06, "-9": 2.0972342089247483e-07, "0": 0.252014343061071, "1": 0.23774971286559915, "10": 2.1451003365461304e-06, "11": 3.0125935309952025e-07, "12": 3.884991792652245e-08, "13": 4.630220536697868e-09, "14": 5.108496073996631e-10, "15": 4.832350225355757e-11, "2": 0.15401622478176033, "3": 0.07175329354386836, "4": 0.0261370499452925, "5": 0.007787054954734453, "6": 0.001958861824896677, "7": 0.0004259224556393799, "8": 8.149529327522261e-05, "9": 1.3916450374558721e-05} |
| Raw goal margin distribution | {"-1": 0.14831480861723617, "-10": 1.8704005243883525e-08, "-11": 1.6325525053213105e-09, "-12": 1.308447609761723e-10, "-13": 9.691868732533077e-12, "-14": 6.645666211821585e-13, "-15": 3.9070005896130366e-14, "-2": 0.060330450261810456, "-3": 0.017468336410798525, "-4": 0.003954630289973102, "-5": 0.0007322547107686716, "-6": 0.00011448071976492574, "-7": 1.5470298743358867e-05, "-8": 1.8396715983820297e-06, "-9": 1.9524317698300606e-07, "0": 0.26208076439065464, "1": 0.24110758102411395, "10": 2.175396752176206e-06, "11": 3.055142023568965e-07, "12": 3.9398616390945527e-08, "13": 4.695615652930324e-09, "14": 5.180646135075645e-10, "15": 4.900600128823302e-11, "2": 0.1561914794681106, "3": 0.07276670423007063, "4": 0.026506197679314877, "5": 0.007897035755829633, "6": 0.001986527893004482, "7": 0.00043193798951552965, "8": 8.26462955080303e-05, "9": 1.4112999951965353e-05} |
| Unadjusted home-win probability | 50.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.0% |
| Raw p btts yes | 49.5% |
| P home draw | 75.2% |
| P draw away | 50.0% |
| P home away | 74.8% |
| Raw p home draw | 76.9% |
| Raw p draw away | 49.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.51, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:24:01Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:23:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.84, "price": 1.51, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.92 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-21T17:24:07Z |
| Market reference home last update utc | 2026-10-21T17:24:07Z |
| Market reference draw last update utc | 2026-10-21T17:24:07Z |
| Market reference away last update utc | 2026-10-21T17:24:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:24:05Z |
| Market best over 2 5 last update utc | 2026-10-21T17:23:35Z |
| Market best under 2 5 last update utc | 2026-10-21T17:23:35Z |
| Home probability edge | +0.7% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -14.1% |
| Under 2.5 probability edge | +14.1% |
| Raw edge prob home | 0.0141 |
| Raw ev home | -0.0063 |
| Raw edge prob draw | 0.0201 |
| Raw ev draw | -0.0618 |
| Raw edge prob away | -0.0343 |
| Raw ev away | -0.1201 |

</details>


---
