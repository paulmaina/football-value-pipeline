# Bundesliga — football model report

Fixtures in this report: **2**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,602 |
| Training data through | 2026-10-31 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 480 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 70.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 42e1c02dabf9ac4d449e156a41a109c7298d50521993b971575ec7e2ca7daddf |
| Training as of utc | 2026-11-01T09:08:05.465726+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 7, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 64, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-01T09:08:05.465726+00:00', 'observations': 363, 'observations_sha256': 'a7d1b621253d8d4a3fc289448d3bcba403d71404007d411b27fd14028a609736', 'eligible_training_matches': 75, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 111, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 21, 'retrospective_eligible_training_matches': 75, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '878a9c1d69aa8c24cb7e65f8d509fa0b0aab63a7bace976f1a6ec9057fe87afc', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1592, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1302, 'tuning_matches': 206, 'audit_matches': 78, 'audit_matchdays': 26, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7307058747259999, 'audit_candidate_poisson_score': 0.7195187152220802, 'audit_gain': 0.011187159503919686, 'audit_gain_lower95': 0.0018529305887372996, 'audit_baseline_briers': [0.5975304647116524, 0.16609585680719302, 0.2894000422491477, 0.2556310978277841], 'audit_candidate_briers': [0.593708908876311, 0.16323459442926103, 0.2868872229847938, 0.253789216550467], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1591.379 |
| Base scoring parameter | 0.218 |
| Home-advantage parameter | 0.225 |
| Dixon-Coles low-score adjustment | -0.075 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1602, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-31'} |
| Training data health | {'training_end': '2026-10-31', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 2.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 7.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261101T090805465726Z_35bc8ca22b2fef37dda9ef6bbfa726eb2946d3c9004920971c154481a8e6a7de.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 2} |
| Shot features applied fixtures | 2 |
| Goal rate features used | {'shot_features': 2} |
| Legacy comparison status | {'AVAILABLE': 2} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-01 — Eintracht Frankfurt vs Hamburger SV

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **60.6%**. Expected goals are 2.01 for Eintracht Frankfurt and 1.16 for Hamburger SV (3.16 combined). The most likely exact score is 2-1 at 10.6%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.0%; Under 3.5 goals: 60.6%; Double Chance 1X: 82.0%; Double Chance X2: 39.4%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 78.3%; BTTS Yes (both teams score): 59.5%; BTTS No (at least one team does not score): 40.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 60.6% | 1.65 |
| Draw | 21.4% | 4.68 |
| Hamburger SV win | 18.0% | 5.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.01 |
| Hamburger SV expected goals | 1.16 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 39.4% |
| Under 3.5 | 60.6% |
| Over 4.5 | 21.7% |
| Under 4.5 | 78.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.59% |
| 2 | 1-1 | 9.85% |
| 3 | 2-0 | 9.16% |
| 4 | 1-0 | 8.33% |
| 5 | 3-1 | 7.09% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0306 |
| Dc lambda away | 1.1068 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:08:05.465726+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9213 |
| Shot lambda away | 1.3486 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 59.5% |
| P btts no | 40.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.57 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.04 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.60 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.10847635280242603, "-10": 5.279795648189517e-08, "-11": 5.449968118910081e-09, "-12": 5.170215529140011e-10, "-13": 4.5368163099070013e-11, "-14": 3.7027009965315704e-12, "-15": 2.8232793659495085e-13, "-16": 2.0057518900813253e-14, "-17": 1.1991978441502282e-15, "-2": 0.04992199322882997, "-3": 0.016366106292296314, "-4": 0.0042652358938654366, "-5": 0.0009179569226871499, "-6": 0.00016781273365105507, "-7": 2.6622598312123194e-05, "-8": 3.7269034711244535e-06, "-9": 4.665533119552644e-07, "0": 0.21382536936606128, "1": 0.239008898681901, "10": 1.6503918782202057e-05, "11": 2.96252149235117e-06, "12": 4.887353805878157e-07, "13": 7.457854589505131e-08, "14": 1.0584709488251594e-08, "15": 1.4034978050172403e-09, "16": 1.733934459681075e-10, "17": 1.802784812080842e-11, "2": 0.18658692594560228, "3": 0.10637320484713533, "4": 0.048208932599931135, "5": 0.018042817062157285, "6": 0.00573593921540855, "7": 0.0015824414556811098, "8": 0.0003852325190952507, "9": 8.386363002525906e-05} |
| Raw goal margin distribution | {"-1": 0.1247416456035229, "-10": 6.071465168127866e-08, "-11": 6.2671538457584935e-09, "-12": 5.945454254020514e-10, "-13": 5.21708112116805e-11, "-14": 4.25789587825101e-12, "-15": 3.246610943386511e-13, "-16": 2.3065007716181742e-14, "-17": 1.3790094211219734e-15, "-2": 0.05740745725950426, "-3": 0.01882009284310631, "-4": 0.004904779065139148, "-5": 0.0010555983324559192, "-6": 0.0001929751140046638, "-7": 3.0614476223628595e-05, "-8": 4.2857273496306985e-06, "-9": 5.365098142732899e-07, "0": 0.2289769021992816, "1": 0.2223803144774603, "10": 1.5355690391181572e-05, "11": 2.7564097602579197e-06, "12": 4.547325569498131e-07, "13": 6.938988707481584e-08, "14": 9.848298693609233e-09, "15": 1.3058521459636087e-09, "16": 1.6132993062336626e-10, "17": 1.6773595278529492e-11, "2": 0.17360549961944874, "3": 0.0989724938123091, "4": 0.04485488888203979, "5": 0.01678752278458853, "6": 0.005336872282081027, "7": 0.0014723461364712076, "8": 0.00035843070787654034, "9": 7.802897934381696e-05} |
| Unadjusted home-win probability | 56.4% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 20.7% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.0% |
| P home draw | 82.0% |
| P draw away | 39.4% |
| P home away | 78.6% |
| Raw p home draw | 79.3% |
| Raw p draw away | 43.6% |
| Raw p home away | 77.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6197 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 6.83, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.09, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:08:18Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.43, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:08:18Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.65, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:07:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.60 |
| Reference draw odds | 4.80 |
| Reference away odds | 5.90 |
| Market reference 1x2 last update utc | 2026-11-01T09:08:18Z |
| Market reference home last update utc | 2026-11-01T09:08:18Z |
| Market reference draw last update utc | 2026-11-01T09:08:18Z |
| Market reference away last update utc | 2026-11-01T09:08:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.95 |
| Market reference over 2 5 last update utc | 2026-11-01T09:07:33Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:07:33Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | -0.0602 |
| Raw edge prob draw | 0.0216 |
| Raw edge prob away | 0.0386 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.057458423322380416, 0.038828151852793265, 0.02558121956181093, 0.008774865366568026, 0.002257464563466578, 0.00046461305489413183, 7.968574356658372e-05, 1.1714481227283191e-05, 1.506862222111182e-06, 1.722945367928232e-07, 1.773013237425022e-08, 1.658669138536867e-09, 1.4223909793642448e-10, 1.125942230247105e-11, 8.276153631053157e-13, 5.677769481634794e-14, 3.651726513422169e-15], [0.0905185994204787, 0.10531519272259138, 0.05023029548405162, 0.017229986988324824, 0.004432670295241958, 0.000912296263932619, 0.000156467850781877, 2.300210324480539e-05, 2.9588165055036606e-06, 3.383109031404855e-07, 3.481420367696075e-08, 3.2568987079631687e-09, 2.792952033216423e-10, 2.2108567101982395e-11, 1.6250735871084398e-12, 1.1148649033863999e-13, 7.17038925188585e-15], [0.1003932901869361, 0.10331066542413073, 0.047861754307621136, 0.016916068749551302, 0.0043519101615814414, 0.0008956748679555092, 0.00015361711664171727, 2.2583021109479985e-05, 2.904908950791569e-06, 3.321471165431013e-07, 3.417991338353338e-08, 3.1975603052725373e-09, 2.7420664124762375e-10, 2.1705764566428345e-11, 1.5954658898601407e-12, 1.0945528493390799e-13, 7.0397498052746665e-15], [0.06570946338870785, 0.06761894519752806, 0.0347919577624496, 0.010745609710099017, 0.002848414280485379, 0.0005862375347447955, 0.00010054554724775125, 1.4781049570510938e-05, 1.9013223691956162e-06, 2.1739708653351666e-07, 2.237145294194921e-08, 2.0928686710163466e-09, 1.7947385946263078e-10, 1.420686720642245e-11, 1.044265082681186e-12, 7.164072444157351e-14, 4.607660344969479e-15], [0.0322561416016361, 0.033193487798586434, 0.017079036386965465, 0.005858448011996544, 0.0013570505921291676, 0.0002877783496885445, 4.9356839063683496e-05, 7.255874624128152e-06, 9.333408067622635e-07, 1.0671813229589278e-07, 1.0981930405687374e-08, 1.0273690382553392e-09, 8.810198601642538e-11, 6.974014041404489e-12, 5.126196538442153e-13, 3.516774042669029e-14, 2.2618560078687254e-15], [0.012667382959680073, 0.013035490323208245, 0.0067071473447719715, 0.0023006844846431506, 0.0005918852858514699, 0.0001096834214102442, 1.9383036874666485e-05, 2.849471077675143e-06, 3.6653439760924984e-07, 4.1909521207747555e-08, 4.3127389445221385e-09, 4.0346043892114133e-10, 3.459873193022665e-11, 2.738780965178299e-12, 2.0131203378565105e-13, 1.381080357698184e-14, 8.88258633198492e-16], [0.004145530718586575, 0.004265997620716333, 0.0021949826132469604, 0.0007529225440820321, 0.00019370051747757646, 3.986587015196944e-05, 6.156352056004389e-06, 9.325185732384799e-07, 1.1995213293418474e-07, 1.3715319740547333e-08, 1.4113879585600457e-09, 1.320365578751127e-10, 1.1322789126801549e-11, 8.962941010598116e-13, 6.588142339549448e-14, 4.5197268180001054e-15, 2.906917286462991e-16], [0.0011628577331321132, 0.0011966497559725137, 0.0006157118784479843, 0.00021120137860992927, 5.43346943855936e-05, 1.1182726300015045e-05, 1.9179483893782103e-06, 2.538705513960729e-07, 3.364762556524159e-08, 3.847267504536263e-09, 3.9590670374303246e-10, 3.7037412771499177e-11, 3.1761416789632727e-12, 2.5141835806573365e-13, 1.8480317205639283e-14, 1.2678230216438956e-15, 8.154157997148882e-17], [0.00028541782087443575, 0.00029371190986507114, 0.000151123510319524, 5.183835952671448e-05, 1.3336188621839506e-05, 2.744746223932897e-06, 4.707511798296397e-07, 6.920442242253585e-08, 8.015254401349017e-09, 9.442932494486108e-10, 9.717339054671726e-11, 9.090654293191425e-12, 7.79568653128764e-13, 6.170942312407332e-14, 4.53590470753025e-15, 3.111810445783329e-16, 2.0013987440608752e-17], [6.227060200375163e-05, 6.408015234275015e-05, 3.297114362265742e-05, 1.1309755798449338e-05, 2.909602810971186e-06, 5.988308620260166e-07, 1.0270542768548476e-07, 1.5098570342841612e-08, 1.9421658386824525e-09, 1.999480860611719e-10, 2.120065772190096e-11, 1.9833397708339167e-12, 1.700812135165803e-13, 1.3463360190570562e-14, 9.896141590045277e-16, 6.789145442524349e-17, 4.366521482800159e-18], [1.2227215090588095e-05, 1.258253141161625e-05, 6.474086517304198e-06, 2.2207400012181444e-06, 5.713183790286957e-07, 1.1758411701934816e-07, 2.016684141267183e-08, 2.964697003108728e-09, 3.813561887474937e-10, 4.3604243924351216e-11, 4.0401939159118315e-12, 3.894409431635648e-13, 3.339649069733058e-14, 2.64361344832108e-15, 1.9431681707703423e-16, 1.333090397970295e-17, 8.573933067911338e-19], [2.1826261519111806e-06, 2.246052098762633e-06, 1.1556605848277491e-06, 3.964144874645252e-07, 1.0198352003273373e-07, 2.098942129948824e-08, 3.599893773245618e-09, 5.292149654305773e-10, 6.807420860651777e-11, 7.783600960521392e-12, 8.009788235150467e-13, 6.746861561027756e-14, 5.961460024871964e-15, 4.718997584569491e-16, 3.4686636618909506e-17, 2.3796407799445223e-18, 1.5304949164723712e-19], [3.571433732104812e-07, 3.6752176833223004e-07, 1.891008770285163e-07, 6.486534907437775e-08, 1.668757534334327e-08, 3.434501468825158e-09, 5.890510403032442e-10, 8.659550685849014e-11, 1.1138990737867366e-11, 1.2736315380125046e-12, 1.3106425882867715e-13, 1.2261174180518663e-14, 9.467259160218684e-16, 7.721701281960286e-17, 5.675778417919214e-18, 3.8938089990098855e-19, 2.5043506267521336e-20], [5.394407265541362e-08, 5.5511658511652546e-08, 2.856239878659843e-08, 9.797468931965361e-09, 2.520544532779195e-09, 5.18758041354558e-10, 8.897214536062025e-11, 1.3079661178127861e-11, 1.6824686407309267e-12, 1.9237336424630165e-13, 1.9796363116656044e-14, 1.851966802264524e-15, 1.5881533046106979e-16, 1.1319376883016705e-17, 8.572876506148125e-19, 5.881333136905264e-20, 3.782650954705802e-21], [7.565892801462078e-09, 7.78575359360421e-09, 4.00600171129881e-09, 1.3741379917384864e-09, 3.5351742643044404e-10, 7.275809069620057e-11, 1.24787336398302e-11, 1.8344798507390677e-12, 2.3597360657036595e-13, 2.6981208130900545e-14, 2.7765267586707934e-15, 2.5974646718472664e-16, 2.227454669899943e-17, 1.7632179303628923e-18, 1.1669477413774105e-19, 8.248827693777456e-21, 5.305333880047743e-22], [9.904063411306626e-10, 1.0191870188930405e-09, 5.244020238674157e-10, 1.7988028859506865e-10, 4.6276878357203764e-11, 9.52433193081345e-12, 1.6335173191695251e-12, 2.401409224959279e-13, 3.0889911134030224e-14, 3.5319506006014394e-15, 3.6345871931665666e-16, 3.400187591031258e-17, 2.9158293509309213e-18, 2.3081244538506096e-19, 1.6965695100952023e-20, 1.047982061027506e-21, 6.944899239914195e-23], [1.215452293137996e-10, 1.250772685719906e-10, 6.435597349954441e-11, 2.207537453906068e-11, 5.679218274624396e-12, 1.1688506631226624e-12, 2.0046947288307927e-13, 2.947071548337776e-14, 3.79088983616803e-15, 4.334501182464446e-16, 4.4604594650525176e-17, 4.1727982071482655e-18, 3.5783812399081787e-19, 2.8325900630623025e-20, 2.0820740092991497e-21, 1.4283853098313494e-22, 8.271777467880268e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9635614073317362, "lambda_away": 1.0290594643502804, "rho": -0.11154584965395063, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6019 |
| Legacy p draw | 0.2229 |
| Legacy p away | 0.1753 |
| Legacy p over 1 5 | 0.8132 |
| Legacy p under 3 5 | 0.6461 |
| Legacy p btts yes | 0.5593 |
| Legacy p over 2 5 | 0.5819 |
| Legacy goal margin distribution | {"-1": 0.10913105888553297, "-10": 2.1275971311816587e-08, "-11": 1.9607504275066786e-09, "-12": 1.6601703350871644e-10, "-13": 1.2998558834858367e-11, "-14": 9.461416032492304e-13, "-15": 6.394808406823379e-14, "-16": 3.651726513422169e-15, "-2": 0.047801684455194386, "-3": 0.014211392606524839, "-4": 0.0033391356931579946, "-5": 0.0006456764153013369, "-6": 0.00010582154981837094, "-7": 1.5028879185132055e-05, "-8": 1.8815368152424593e-06, "-9": 2.1049295456186268e-07, "0": 0.22285413251814987, "1": 0.2351134109144543, "10": 1.4672528777539044e-05, "11": 2.5801319027507685e-06, "12": 4.168465929403023e-07, "13": 6.227630364742431e-08, "14": 8.649435793854664e-09, "15": 1.115483609702653e-09, "16": 1.215452293137996e-10, "2": 0.18759732573887328, "3": 0.1064202062562504, "4": 0.047711771643575644, "5": 0.017603961693498194, "6": 0.005505206650847642, "7": 0.0014918670354805103, "8": 0.0003563856932780048, "9": 7.60762543148815e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5797 |
| Legacy raw p draw | 0.2384 |
| Legacy raw p away | 0.1819 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9636 |
| Legacy lambda away | 1.0291 |
| Legacy model home team | Ein Frankfurt |
| Legacy model away team | Hamburg |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 81.9% |
| Market reference home draw last update utc | 2026-11-01T09:08:23Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 38.2% |
| Market reference draw away last update utc | 2026-11-01T09:08:23Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.9% |
| Market reference home away last update utc | 2026-11-01T09:08:23Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.53 |
| Market reference dc home draw odds | 1.18 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-11-01T09:07:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.5% |
| Market reference under 3 5 odds | 1.84 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market reference under 3 5 last update utc | 2026-11-01T09:07:50Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 64.3% |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-11-01T09:08:18Z |
| Market btts yes bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.303752938389106, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.7389 |
| Elo away rating | 1,410.7728 |
| Elo rating diff | 123.9661 |
| Elo home expectancy | 0.6712 |

</details>


---

## 2026-11-01 — Union Berlin vs 1. FC Köln

The model's most likely 1X2 outcome is **Union Berlin win** at **37.3%**. Expected goals are 1.44 for Union Berlin and 1.19 for 1. FC Köln (2.63 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 48.9%; Under 3.5 goals: 73.1%; Double Chance 1X: 64.7%; Double Chance X2: 62.7%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 54.0%; BTTS No (at least one team does not score): 46.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 37.3% | 2.68 |
| Draw | 27.4% | 3.65 |
| 1. FC Köln win | 35.3% | 2.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 1.44 |
| 1. FC Köln expected goals | 1.19 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.09% |
| 2 | 0-1 | 8.93% |
| 3 | 1-2 | 8.57% |
| 4 | 1-0 | 8.42% |
| 5 | 0-0 | 8.03% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 14.00 |
| Matched home-team name | Union Berlin |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4286 |
| Dc lambda away | 1.1544 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:08:05.465726+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.4865 |
| Shot lambda away | 1.3222 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.0% |
| P btts no | 46.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.45 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.91 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.2031906920484307, "-10": 1.517444754490265e-07, "-11": 1.6179778924984243e-08, "-12": 1.5840608199678995e-09, "-13": 1.42534492449979e-10, "-14": 1.077729790087741e-11, "-2": 0.10155407234272808, "-3": 0.03552766401360978, "-4": 0.009759617796303847, "-5": 0.002198153940076171, "-6": 0.0004186483766033218, "-7": 6.898663241715252e-05, "-8": 1.001038484765297e-05, "-9": 1.297006166007779e-06, "0": 0.2742717752942128, "1": 0.18938631667771255, "10": 7.928552098054451e-07, "11": 1.0249082400383797e-07, "12": 1.2165099341300746e-08, "13": 1.3270741419483744e-09, "14": 1.2165123072408973e-10, "2": 0.11369126305062517, "3": 0.048220066713417796, "4": 0.016059254108451416, "5": 0.0043851259247183125, "6": 0.0010125227341586808, "7": 0.000202279430879339, "8": 3.558516286422458e-05, "9": 5.589740291696355e-06} |
| Raw goal margin distribution | {"-1": 0.17404419128971058, "-10": 1.2997762961460973e-07, "-11": 1.3858885512206383e-08, "-12": 1.3568366817674717e-09, "-13": 1.2208876410260516e-10, "-14": 9.231358378362248e-12, "-2": 0.08698674242840827, "-3": 0.030431431131635944, "-4": 0.008359658454480317, "-5": 0.0018828417826327437, "-6": 0.0003585957476994482, "-7": 5.909090878031966e-05, "-8": 8.574454458244902e-06, "-9": 1.110958316962607e-06, "0": 0.27840201468864356, "1": 0.21297929519417078, "10": 8.916258932410094e-07, "11": 1.1525871479592504e-07, "12": 1.3680578032922954e-08, "13": 1.4923956512843226e-09, "14": 1.368060472035631e-10, "2": 0.12785445907089005, "3": 0.054227126874833, "4": 0.018059850792613165, "5": 0.0049314071109663295, "6": 0.0011386587060361179, "7": 0.00022747858122333675, "8": 4.001821799559945e-05, "9": 6.286087445640942e-06} |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 30.2% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 54.0% |
| P home draw | 64.7% |
| P draw away | 62.7% |
| P home away | 72.6% |
| Raw p home draw | 69.8% |
| Raw p draw away | 58.1% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4892 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.35, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.19, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.88, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.39, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:08:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:08:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:06:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 2.82 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.66 |
| Market reference 1x2 last update utc | 2026-11-01T09:08:18Z |
| Market reference home last update utc | 2026-11-01T09:08:18Z |
| Market reference draw last update utc | 2026-11-01T09:08:18Z |
| Market reference away last update utc | 2026-11-01T09:08:18Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.26 |
| Market reference over 2 5 last update utc | 2026-11-01T09:08:18Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:08:18Z |
| Home probability edge | +2.0% |
| Draw probability edge | +0.2% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | 0.0664 |
| Raw edge prob draw | 0.0059 |
| Raw edge prob away | -0.0723 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0935302723899333, 0.0889979369774156, 0.0561415908722359, 0.01984559005089057, 0.005261439491859576, 0.0011159253196508427, 0.0001972352054611241, 2.9880437533321387e-05, 3.960933226694495e-06, 4.667190925340898e-07, 4.9494406742590685e-08, 4.7715996000548986e-09, 4.2168029119973437e-10, 3.439857932968094e-11, 2.60563168348289e-12], [0.09408837024806382, 0.1348007158275827, 0.08024981795640508, 0.02836764979542135, 0.007520797947661642, 0.0015951240847221957, 0.00028193161410174685, 4.2711644526849804e-05, 5.6618304797077814e-06, 6.671368165871079e-07, 7.074821125023429e-08, 6.820611837250751e-09, 6.027575292904212e-10, 4.916995913863591e-11, 3.724537638001841e-12], [0.07626764241461473, 0.08087995060308546, 0.04595838111419874, 0.020274619017426422, 0.00537518314684262, 0.00114004978686967, 0.0002014991057103221, 3.052640337266839e-05, 4.046562078465017e-06, 4.7680879051832625e-07, 5.05643942874118e-08, 4.874753723458883e-09, 4.307963244886434e-10, 3.5142219952220784e-11, 2.6619611483902633e-12], [0.03633945484768837, 0.03853709410664674, 0.020433818124255904, 0.0077407333871191255, 0.002561128403587741, 0.000543202679962851, 9.600883706360239e-05, 1.4544999975124887e-05, 1.928076642769925e-06, 2.271864052100469e-07, 2.409255701282838e-08, 2.3226874100056015e-09, 2.0526271806331995e-10, 1.6744310886900405e-11, 1.2683520021813606e-12], [0.012986070535472571, 0.013771406984463698, 0.007302118443515526, 0.0025812387372998727, 0.0007333681137970123, 0.00019411596422184743, 3.4309197409876504e-05, 5.197722321567347e-06, 6.89007014159986e-07, 8.118610185881186e-08, 8.609585533405046e-09, 8.30022978181951e-10, 7.33515719001672e-11, 5.9836561433447566e-12, 4.532513939235046e-13], [0.003712505400184809, 0.0039370202601555285, 0.0020875563612787634, 0.0007379339828176336, 0.00019564018956481926, 4.446741782718668e-05, 9.808438997173364e-06, 1.4859438915543887e-06, 1.9697584837899344e-07, 2.3209780106113108e-08, 2.461339840932574e-09, 2.3729000857963034e-10, 2.097001599117721e-11, 1.7106295306448543e-12, 1.2957716831938246e-13], [0.0008844538659553671, 0.0009379414745809727, 0.00049733188106361, 0.00017580272445944664, 4.660861152908536e-05, 9.885456213940755e-06, 1.8724029081799882e-06, 3.540059010857247e-07, 4.692681405661161e-08, 5.5294141098902726e-09, 5.863807060413745e-10, 5.653111384845093e-11, 4.995820803821398e-12, 4.075341955114572e-13, 3.086999616321693e-14], [0.00018060779293168456, 0.0001915301025228462, 0.00010155647100534512, 3.589937618928336e-05, 9.517600390366962e-06, 2.0186360166950115e-06, 3.567856042809748e-07, 5.792461068300256e-08, 9.582578178823712e-09, 1.1291208247632816e-09, 1.197404739946039e-10, 1.1543801318692796e-11, 1.0201596759213097e-12, 8.321954872796976e-14, 6.303733964490955e-15], [3.227051077261926e-05, 3.422207943752614e-05, 1.8145834896763432e-05, 6.414403206204856e-06, 1.7005790333919765e-06, 3.606844104860631e-07, 6.374948444677435e-08, 9.657821905272083e-09, 1.3719650437033606e-09, 2.0174824766777782e-10, 2.1394903249955583e-11, 2.0626151217780555e-12, 1.8227936501091565e-13, 1.4869443339769255e-14, 1.126334093932355e-15], [5.125339886423992e-06, 5.435296329004669e-06, 2.8819987394732296e-06, 1.0187628213267133e-06, 2.7009320091876596e-07, 5.7285433394629165e-08, 1.0124964481542932e-08, 1.5338963853361e-09, 2.033324027537757e-10, 2.5675441713149756e-11, 3.3980296055995555e-12, 3.275933135511476e-13, 2.895038465753591e-14, 2.3616282858126955e-15, 1.7888917525187866e-16], [7.326254679641316e-07, 7.769312094029893e-07, 4.119581768169873e-07, 1.456238230553124e-07, 3.860761668532042e-08, 8.188484740189666e-09, 1.4472809620019346e-09, 2.1925795791455669e-10, 2.9064705955275065e-11, 3.424711403059055e-12, 3.892044708096688e-13, 4.682678806883634e-14, 4.138220991674988e-15, 3.375754713621595e-16, 2.5570746260120978e-17], [9.520256894773897e-08, 1.0095997240770175e-07, 5.353277827071693e-08, 1.892339627966014e-08, 5.01694856391758e-09, 1.0640700018547288e-09, 1.8806999155328974e-10, 2.8491939972694198e-11, 3.7768748066349015e-12, 4.4503138060687804e-13, 4.7194478471790085e-14, 4.875872567179689e-15, 5.377498961040856e-16, 4.3866959985337156e-17, 3.322844809967064e-18], [1.1340357935980218e-08, 1.2026169429719113e-08, 6.376727787993288e-09, 2.254120761106196e-09, 5.976098448820114e-10, 1.2675009533194268e-10, 2.240255746041751e-11, 3.3939083908353755e-12, 4.4989450032737883e-13, 5.301133367100492e-14, 5.621720972317556e-15, 5.419723825085817e-16, 5.1327457387916056e-17, 5.2253529846461095e-18, 3.958112677760427e-19], [1.2469319444528077e-09, 1.3223405218754571e-09, 7.011547276388005e-10, 2.4785242225554503e-10, 6.571034266375267e-11, 1.3936839006676099e-11, 2.4632789099367698e-12, 3.7317806130722073e-13, 4.9468264340401786e-14, 5.828874692102845e-15, 6.181377609733397e-16, 5.959271132148198e-17, 5.266383177485201e-18, 4.603868846254e-19, 4.352152873397387e-20], [1.2731338235509478e-10, 1.3501269673465905e-10, 7.158881471204414e-11, 2.5306056471352886e-11, 6.709111926638319e-12, 1.4229694901729312e-12, 2.515039983562553e-13, 3.8101968128331415e-14, 5.050774487276625e-15, 5.951357294814342e-16, 6.311267383999514e-17, 6.084493765518222e-18, 5.377046101724825e-19, 4.386326578443833e-20, 3.560629357466659e-21]] |
| Legacy trial inputs | {"lambda_home": 1.4294183101977538, "lambda_away": 1.0604752951900203, "rho": -0.11154584965395063, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3970 |
| Legacy p draw | 0.2828 |
| Legacy p away | 0.3201 |
| Legacy p over 1 5 | 0.7234 |
| Legacy p under 3 5 | 0.7611 |
| Legacy p btts yes | 0.5104 |
| Legacy p over 2 5 | 0.4562 |
| Legacy goal margin distribution | {"-1": 0.19228779055172676, "-10": 5.6763012466610903e-08, "-11": 5.410767701299722e-09, "-12": 4.735122114867605e-10, "-13": 3.8123116967682786e-11, "-14": 2.60563168348289e-12, "-2": 0.09046346971342571, "-3": 0.028607846971901916, "-4": 0.007073320497170658, "-5": 0.0014303951187760494, "-6": 0.0002442294504273576, "-7": 3.6044020767392427e-05, "-8": 4.681032218050447e-06, "-9": 5.42553433459158e-07, "0": 0.2828098699760116, "1": 0.19818927000871484, "10": 8.402167296940088e-07, "11": 1.0795519916156825e-07, "12": 1.273428727256772e-08, "13": 1.3819446411874667e-09, "14": 1.2731338235509478e-10, "2": 0.12289348150803665, "3": 0.05238410955074408, "4": 0.017458081393576467, "5": 0.004758696222176954, "6": 0.0010951882606637772, "7": 0.00021786264113177938, "8": 3.813730047290847e-05, "9": 5.958125128170959e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4410 |
| Legacy raw p draw | 0.2931 |
| Legacy raw p away | 0.2659 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4294 |
| Legacy lambda away | 1.0605 |
| Legacy model home team | Union Berlin |
| Legacy model away team | FC Koln |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 62.1% |
| Market reference home draw last update utc | 2026-11-01T09:08:23Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.8% |
| Market reference draw away last update utc | 2026-11-01T09:08:23Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market reference home away last update utc | 2026-11-01T09:08:23Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.51 |
| Market reference dc home draw odds | 1.55 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-11-01T09:07:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.5% |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market reference under 3 5 last update utc | 2026-11-01T09:07:33Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 60.7% |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-11-01T09:08:18Z |
| Market btts yes bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.176507153371874, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,423.6013 |
| Elo away rating | 1,399.6261 |
| Elo rating diff | 83.9752 |
| Elo home expectancy | 0.6186 |

</details>


---
