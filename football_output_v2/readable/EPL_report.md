# Premier League — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,990 |
| Training data through | 2026-11-02 |
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
| Training sha256 | 30ae885ed8569d2286ab5399b119765e818638a76668dfc7f09da6d64d922b7f |
| Training as of utc | 2026-11-04T19:38:02.402368+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 90, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 90, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 231, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-04T19:38:02.402368+00:00', 'observations': 638, 'observations_sha256': 'e608fe91556dbb265b5a33edd09ce2c48a9e680f58ec5639ac3d91e0e5e53fd4', 'eligible_training_matches': 297, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 266, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 28, 'retrospective_eligible_training_matches': 297, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '2ec7ecb858efb4c86e98b5308bc6c6491a23bd208b7991e91edc452cd7d52587', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 236, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-04T00:00:00+00:00', 'audit_origin_utc': '2025-11-02T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 12, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1619, 'tuning_matches': 249, 'audit_matches': 112, 'audit_matchdays': 37, 'selected_shrinkage': 15.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9372149208477853, 'audit_candidate_poisson_score': 0.9280257670321073, 'audit_gain': 0.009189153815678086, 'audit_gain_lower95': 0.0003474802310925464, 'audit_baseline_briers': [0.6265738347139245, 0.167832988720583, 0.21447736421684555, 0.2603646763863064], 'audit_candidate_briers': [0.6266934513464083, 0.16714356098353306, 0.2120711078558599, 0.25712093059759306], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'market_brier_worse']} |
| Optimizer objective | 1879.930 |
| Base scoring parameter | 0.214 |
| Home-advantage parameter | 0.178 |
| Dixon-Coles low-score adjustment | -0.061 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1990, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261104T193802402368Z_de7c3963f4b39e6cc2d00338b871cdc60b307414824654c53e672a8d0c5e7bef.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 4, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 5} |
| Legacy comparison status | {'None': 5} |
| Bbs statistics applied fixtures | 0 |
| Goal market validation | SKIPPED: not required by 48h-ah-price-edge-cagey-v28 |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-06 — Everton vs Coventry City

The model's most likely 1X2 outcome is **Everton win** at **54.6%**. Expected goals are 1.44 for Everton and 0.90 for Coventry City (2.33 combined). The most likely exact score is 1-0 at 14.7%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 42.7%; Under 3.5 goals: 78.8%; Double Chance 1X: 79.5%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 90.8%; BTTS Yes (both teams score): 44.9%; BTTS No (at least one team does not score): 55.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 54.6% | 1.83 |
| Draw | 24.9% | 4.02 |
| Coventry City win | 20.5% | 4.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.44 |
| Coventry City expected goals | 0.90 |
| Expected total goals | 2.33 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 69.0% |
| Under 1.5 | 31.0% |
| Over 2.5 | 42.7% |
| Under 2.5 | 57.3% |
| Over 3.5 | 21.2% |
| Under 3.5 | 78.8% |
| Over 4.5 | 9.2% |
| Under 4.5 | 90.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.69% |
| 2 | 1-1 | 11.62% |
| 3 | 2-0 | 11.18% |
| 4 | 2-1 | 10.01% |
| 5 | 0-0 | 9.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 54.6% | 57.0% | 1.75 | -4.4% |
| Draw | 24.9% | 23.4% | 4.16 | +3.4% |
| Coventry City win | 20.5% | 19.6% | 4.93 | +1.1% |
| Over 2.5 | 42.7% | 55.8% | 1.81 | -22.8% |
| Under 2.5 | 57.3% | 44.2% | 2.15 | +23.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:00:00+00:00 |
| Fixture id | 586bec023ee8ac2f0645d963bd2c9d25 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:37:33Z |
| Market best draw last update utc | 2026-11-04T19:37:33Z |
| Market best away last update utc | 2026-11-04T19:37:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4394 |
| Dc lambda away | 0.8952 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:38:02.402368+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.9% |
| P btts no | 55.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.91 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.22 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.72 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.89 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.13423663921029577, "-10": 8.971941548615147e-09, "-11": 7.231539480594255e-10, "-12": 5.3502482986415453e-11, "-13": 3.645428131768542e-12, "-14": 2.1345454855199877e-13, "-2": 0.052860913448371315, "-3": 0.014325178810956156, "-4": 0.0030192613130103703, "-5": 0.000518932570720987, "-6": 7.517007749304932e-05, "-7": 9.400689505267824e-06, "-8": 1.0337030332216008e-06, "-9": 1.0138481612014184e-07, "0": 0.24866452773286046, "1": 0.2709574766421869, "10": 1.2760105788037921e-06, "11": 1.6536858513974853e-07, "12": 1.9672094246528727e-08, "13": 2.1551604531459994e-09, "14": 2.0290413233170142e-10, "2": 0.16829345458080294, "3": 0.07333090134256309, "4": 0.024850897806788747, "5": 0.006867627339558908, "6": 0.0015995403443916458, "7": 0.0003216357530240586, "8": 5.686627889051534e-05, "9": 8.967808950797232e-06} |
| Raw goal margin distribution | {"-1": 0.14831328263300875, "-10": 9.912778735334523e-09, "-11": 7.989870464329045e-10, "-12": 5.911298828258627e-11, "-13": 4.0277037327960775e-12, "-14": 2.3583832979532563e-13, "-2": 0.058404140945641246, "-3": 0.015827379963150718, "-4": 0.003335874311914914, "-5": 0.0005733501187275886, "-6": 8.305274189192228e-05, "-7": 1.0386487085360585e-05, "-8": 1.1421016722909348e-06, "-9": 1.1201647312076712e-07, "0": 0.2833254770926832, "1": 0.24310079193498124, "10": 1.1448260666903443e-06, "11": 1.4836731765747886e-07, "12": 1.764963915967521e-08, "13": 1.933592013770523e-09, "14": 1.8204389806100295e-10, "2": 0.150991486166273, "3": 0.06579187409995063, "4": 0.022296018592996573, "5": 0.006161578066235806, "6": 0.0014350942785279085, "7": 0.0002885689195356895, "8": 5.101995192749523e-05, "9": 8.045843520824226e-06} |
| Unadjusted home-win probability | 49.0% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.2% |
| Raw p btts yes | 45.9% |
| P home draw | 79.5% |
| P draw away | 45.4% |
| P home away | 75.1% |
| Raw p home draw | 77.3% |
| Raw p draw away | 51.0% |
| Raw p home away | 71.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4267 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.93, "draw": 4.16, "home": 1.75}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.15}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.83, "draw": 4.07, "home": 1.72}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.72 |
| Reference draw odds | 4.07 |
| Reference away odds | 4.83 |
| Market reference 1x2 last update utc | 2026-11-04T19:38:18Z |
| Market reference home last update utc | 2026-11-04T19:38:18Z |
| Market reference draw last update utc | 2026-11-04T19:38:18Z |
| Market reference away last update utc | 2026-11-04T19:38:18Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:21Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:21Z |
| Market best over 2 5 last update utc | 2026-11-04T19:37:33Z |
| Market best under 2 5 last update utc | 2026-11-04T19:37:33Z |
| Home probability edge | -2.4% |
| Draw probability edge | +1.5% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -13.1% |
| Under 2.5 probability edge | +13.1% |
| Raw edge prob home | -0.0802 |
| Raw ev home | -0.1423 |
| Raw edge prob draw | 0.0495 |
| Raw ev draw | 0.1786 |
| Raw edge prob away | 0.0307 |
| Raw ev away | 0.1169 |
| Count model | {"corners": {"alpha": 0.00930322941348174, "mu": 9.757177087800525, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,448.4574 |
| Elo away rating | 1,377.6232 |
| Elo rating diff | 130.8342 |
| Elo home expectancy | 0.6799 |

</details>


---

## 2026-11-07 — Arsenal vs Hull City

The model's most likely 1X2 outcome is **Arsenal win** at **78.5%**. Expected goals are 1.67 for Arsenal and 0.60 for Hull City (2.27 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 44.1%; Under 3.5 goals: 78.6%; Double Chance 1X: 93.1%; Double Chance X2: 21.5%; Double Chance 12 (either team wins): 85.4%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 34.2%; BTTS No (at least one team does not score): 65.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 78.5% | 1.27 |
| Draw | 14.6% | 6.84 |
| Hull City win | 6.9% | 14.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.67 |
| Hull City expected goals | 0.60 |
| Expected total goals | 2.27 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 69.7% |
| Under 1.5 | 30.3% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 21.4% |
| Under 3.5 | 78.6% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.79% |
| 2 | 2-0 | 18.03% |
| 3 | 2-1 | 10.79% |
| 4 | 3-0 | 10.04% |
| 5 | 1-1 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 78.5% | 85.3% | 1.19 | -6.5% |
| Draw | 14.6% | 10.2% | 8.40 | +22.8% |
| Hull City win | 6.9% | 4.5% | 19.00 | +30.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:00:00+00:00 |
| Fixture id | 842fcc5b9feb8c63054a661ad1fc8926 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:37:33Z |
| Market best draw last update utc | 2026-11-04T19:37:33Z |
| Market best away last update utc | 2026-11-04T19:37:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6704 |
| Dc lambda away | 0.5987 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:38:02.402368+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 34.2% |
| P btts no | 65.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.49 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.30 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.68 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.77 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.05127757668772254, "-10": 1.0275962758183225e-10, "-11": 5.551511145287936e-12, "-12": 2.7523778987102536e-13, "-13": 1.2607087583433261e-14, "-14": 5.355827093156811e-16, "-15": 2.004201391914283e-17, "-2": 0.014208306314477994, "-3": 0.0026268721556965283, "-4": 0.0003750407372268207, "-5": 4.349359262948418e-05, "-6": 4.240989083686607e-06, "-7": 3.564702779864187e-07, "-8": 2.631757040567912e-08, "-9": 1.7317502852111036e-09, "0": 0.14613565833207545, "1": 0.33544662251180524, "10": 6.593780865885345e-06, "11": 9.938275704845763e-07, "12": 1.3746613517462636e-07, "13": 1.7566703340682272e-08, "14": 2.0820438951324937e-09, "15": 2.1736645833005275e-10, "2": 0.24840001016734592, "3": 0.12812564694124087, "4": 0.05103444711549634, "5": 0.0165119395207904, "6": 0.004491876401131668, "7": 0.0010533478282744963, "8": 0.00021696121742901958, "9": 3.982991869022709e-05} |
| Raw goal margin distribution | {"-1": 0.09216885042801766, "-10": 1.8470523289951817e-10, "-11": 9.978560482988427e-12, "-12": 4.947260055063145e-13, "-13": 2.2660602252847758e-14, "-14": 9.626828297166542e-16, "-15": 3.602450627570341e-17, "-2": 0.025538711930747915, "-3": 0.00472166983019476, "-4": 0.0006741167552512042, "-5": 7.817753280458514e-05, "-6": 7.622963364701226e-06, "-7": 6.407372940779149e-07, "-8": 4.7304501636689906e-08, "-9": 3.1127335441051687e-09, "0": 0.248354891755473, "1": 0.2684395340048914, "10": 5.276641182775181e-06, "11": 7.953056969375338e-07, "12": 1.1000660847742311e-07, "13": 1.40576692156409e-08, "14": 1.666145536962222e-09, "15": 1.7394645486513888e-10, "2": 0.19878090432639842, "3": 0.10253192803505282, "4": 0.0408400689781844, "5": 0.013213599580427842, "6": 0.00359460232122301, "7": 0.0008429364947835156, "8": 0.00017362216279798818, "9": 3.187369940587492e-05} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 12.3% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 37.2% |
| P home draw | 93.1% |
| P draw away | 21.5% |
| P home away | 85.4% |
| Raw p home draw | 87.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 75.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4414 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.44, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.65, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": -2.0, "market_key": "spreads", "opposite_price": 2.03, "price": 1.86, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 19.0, "draw": 8.4, "home": 1.19}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 17.87, "draw": 8.34, "home": 1.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.34 |
| Reference away odds | 17.87 |
| Market reference 1x2 last update utc | 2026-11-04T19:38:18Z |
| Market reference home last update utc | 2026-11-04T19:38:18Z |
| Market reference draw last update utc | 2026-11-04T19:38:18Z |
| Market reference away last update utc | 2026-11-04T19:38:18Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-11-04T19:37:34Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:37:34Z |
| Home probability edge | -6.7% |
| Draw probability edge | +4.4% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -20.7% |
| Under 2.5 probability edge | +20.7% |
| Raw edge prob home | -0.2241 |
| Raw ev home | -0.2521 |
| Raw edge prob draw | 0.1460 |
| Raw ev draw | 1.0862 |
| Raw edge prob away | 0.0781 |
| Raw ev away | 1.3406 |
| Count model | {"corners": {"alpha": 0.00930322941348174, "mu": 9.887447394780748, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,656.9795 |
| Elo away rating | 1,392.5184 |
| Elo rating diff | 324.4611 |
| Elo home expectancy | 0.8662 |

</details>


---

## 2026-11-07 — Fulham vs Newcastle United

The model's most likely 1X2 outcome is **Fulham win** at **43.9%**. Expected goals are 1.41 for Fulham and 1.41 for Newcastle United (2.82 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.7%; Double Chance 1X: 69.7%; Double Chance X2: 56.1%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 43.9% | 2.28 |
| Draw | 25.9% | 3.87 |
| Newcastle United win | 30.3% | 3.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 1.41 |
| Newcastle United expected goals | 1.41 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.21% |
| 2 | 2-1 | 10.00% |
| 3 | 1-0 | 9.19% |
| 4 | 2-0 | 7.08% |
| 5 | 1-2 | 6.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 43.9% | 47.0% | 2.16 | -5.2% |
| Draw | 25.9% | 25.5% | 3.88 | +0.3% |
| Newcastle United win | 30.3% | 27.5% | 3.50 | +5.9% |
| Over 2.5 | 53.8% | 58.4% | 1.71 | -8.0% |
| Under 2.5 | 46.2% | 41.6% | 2.32 | +7.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:00:00+00:00 |
| Fixture id | 3903e98a54db0f2cc23095407fe9dad8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:37:33Z |
| Market best draw last update utc | 2026-11-04T19:37:33Z |
| Market best away last update utc | 2026-11-04T19:38:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fulham |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4091 |
| Dc lambda away | 1.4114 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:38:02.402368+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.41 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.39 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.159165544911251, "-10": 5.076313724120082e-07, "-11": 6.417966826632898e-08, "-12": 7.451761915923225e-09, "-13": 7.939058885467923e-10, "-14": 7.008311517627618e-11, "-2": 0.09048351944410091, "-3": 0.03696764407671054, "-4": 0.01192887870579151, "-5": 0.003166637383302444, "-6": 0.0007123173105115125, "-7": 0.0001388271322929191, "-8": 2.3848547060193935e-05, "-9": 3.660617786491555e-06, "0": 0.258527132139832, "1": 0.23111923234864418, "10": 7.264080060692939e-07, "11": 9.168970804343648e-08, "12": 1.0628526182649283e-08, "13": 1.1305090760457345e-09, "14": 9.963441658850121e-11, "2": 0.1311819309674126, "3": 0.05350782069262212, "4": 0.01723796782166038, "5": 0.0045685221155807145, "6": 0.0010259869807389208, "7": 0.00019963360899978954, "8": 3.423829936584152e-05, "9": 5.246813160480978e-06} |
| Raw goal margin distribution | {"-1": 0.19326502423804928, "-10": 6.163858487583136e-07, "-11": 7.792946111545806e-08, "-12": 9.048220505889604e-09, "-13": 9.63991552809241e-10, "-14": 8.509765703860935e-11, "-2": 0.10986862507371736, "-3": 0.04488755799813813, "-4": 0.014484510661481612, "-5": 0.003845054851402069, "-6": 0.000864923513175861, "-7": 0.00016856932888616212, "-8": 2.895783775439978e-05, "-9": 4.444865159900038e-06, "0": 0.2662041535134795, "1": 0.19293795230263092, "10": 6.064042001308976e-07, "11": 7.654241638549855e-08, "12": 8.872676050523759e-09, "13": 9.437471039310626e-10, "14": 8.317464591806167e-11, "2": 0.10951045866134365, "3": 0.0446682400754842, "4": 0.01439022698185813, "5": 0.003813794694072749, "6": 0.0008564922319156685, "7": 0.00016665380608871434, "8": 2.858207559293445e-05, "9": 4.380030934728196e-06} |
| Unadjusted home-win probability | 36.6% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.9% |
| P home draw | 69.7% |
| P draw away | 56.1% |
| P home away | 74.1% |
| Raw p home draw | 63.3% |
| Raw p draw away | 63.4% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5381 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.88, "home": 2.16}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.32}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.5, "draw": 3.76, "home": 2.08}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.76 |
| Reference away odds | 3.50 |
| Market reference 1x2 last update utc | 2026-11-04T19:38:18Z |
| Market reference home last update utc | 2026-11-04T19:38:18Z |
| Market reference draw last update utc | 2026-11-04T19:38:18Z |
| Market reference away last update utc | 2026-11-04T19:38:18Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:21Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:21Z |
| Market best over 2 5 last update utc | 2026-11-04T19:37:33Z |
| Market best under 2 5 last update utc | 2026-11-04T19:37:33Z |
| Home probability edge | -3.1% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.1036 |
| Raw ev home | -0.2086 |
| Raw edge prob draw | 0.0110 |
| Raw ev draw | 0.0329 |
| Raw edge prob away | 0.0926 |
| Raw ev away | 0.2860 |
| Count model | {"corners": {"alpha": 0.00930322941348174, "mu": 10.271788422563715, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,459.2088 |
| Elo away rating | 1,451.5742 |
| Elo rating diff | 67.6346 |
| Elo home expectancy | 0.5961 |

</details>


---

## 2026-11-07 — Leeds United vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Leeds United win** at **37.1%**. Expected goals are 1.46 for Leeds United and 1.36 for Tottenham Hotspur (2.82 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 47.9%; Under 3.5 goals: 73.8%; Double Chance 1X: 65.1%; Double Chance X2: 62.9%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.5%; BTTS No (at least one team does not score): 46.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 37.1% | 2.70 |
| Draw | 28.0% | 3.57 |
| Tottenham Hotspur win | 34.9% | 2.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.46 |
| Tottenham Hotspur expected goals | 1.36 |
| Expected total goals | 2.82 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 26.2% |
| Under 3.5 | 73.8% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.37% |
| 2 | 1-0 | 9.03% |
| 3 | 0-1 | 8.86% |
| 4 | 0-0 | 8.30% |
| 5 | 2-1 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 37.1% | 36.3% | 2.68 | -0.6% |
| Draw | 28.0% | 28.7% | 3.57 | +0.1% |
| Tottenham Hotspur win | 34.9% | 35.1% | 2.77 | -3.4% |
| Over 2.5 | 47.9% | 47.9% | 2.03 | -2.8% |
| Under 2.5 | 52.1% | 52.1% | 1.92 | +0.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T12:30:00+00:00 |
| Fixture id | 5c87852253fd11eea5d34ad723356607 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:37:33Z |
| Market best draw last update utc | 2026-11-04T19:37:33Z |
| Market best away last update utc | 2026-11-04T19:38:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4599 |
| Dc lambda away | 1.3603 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:38:02.402368+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.5% |
| P btts no | 46.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.06 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.82 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.26 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.19540339863304088, "-10": 2.2914831120950044e-07, "-11": 2.569960350151426e-08, "-12": 2.6464585509612595e-09, "-13": 2.5051680513848535e-10, "-14": 1.9964590358142123e-11, "-2": 0.10181402503669602, "-3": 0.03754098445807593, "-4": 0.010860770721612326, "-5": 0.0025750180245637847, "-6": 0.0005161138862709108, "-7": 8.948615665429624e-05, "-8": 1.366097828536182e-05, "-9": 1.8619754927532022e-06, "0": 0.2803763595271547, "1": 0.1984086932432827, "10": 4.3840850134596064e-07, "11": 5.277060521684948e-08, "12": 5.8322226381853855e-09, "13": 5.925284507202304e-10, "14": 5.067994012422352e-11, "2": 0.11064789252073515, "3": 0.04378693460955704, "4": 0.01359574081703241, "5": 0.0034595996973631605, "6": 0.000744208227548514, "7": 0.00013848671852814798, "8": 2.2690152541850812e-05, "9": 3.3191961716948284e-06} |
| Raw goal margin distribution | {"-1": 0.18585192472111284, "-10": 4.261522048034895e-07, "-11": 5.192750200232526e-08, "-12": 5.813076399763964e-09, "-13": 6.015594131502411e-10, "-14": 5.7492675574428726e-11, "-15": 4.604196440614057e-12, "-2": 0.10199731172951282, "-3": 0.04016864466791728, "-4": 0.012493520343566721, "-5": 0.0031965975855224615, "-6": 0.0006930394052206538, "-7": 0.0001301808776465423, "-8": 2.1553546868244e-05, "-9": 3.1885409837113804e-06, "0": 0.26585381852239265, "1": 0.19999587828317789, "10": 8.641680349426607e-07, "11": 1.1301451750850624e-07, "12": 1.357832441667991e-08, "13": 1.5080718129986041e-09, "14": 1.5468897499676169e-10, "15": 1.329548033992745e-11, "2": 0.11748851570829044, "3": 0.049658913800215775, "4": 0.016576705107254484, "5": 0.004552025604289323, "6": 0.001059200076911607, "7": 0.00021353576041918863, "8": 3.794420996475539e-05, "9": 6.024515359843355e-06} |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 34.5% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.8% |
| P home draw | 65.1% |
| P draw away | 62.9% |
| P home away | 72.0% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9183 |
| Totals anchor target over 2 5 | 0.4787 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.87 |
| Totals anchor reference last update utc | 2026-11-04T19:38:18Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5302 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.76, "draw": 3.57, "home": 2.68}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.02, "under": 1.92}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.77, "draw": 3.37, "home": 2.68}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.03, "under": 1.87}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.68 |
| Reference draw odds | 3.37 |
| Reference away odds | 2.77 |
| Market reference 1x2 last update utc | 2026-11-04T19:38:18Z |
| Market reference home last update utc | 2026-11-04T19:38:18Z |
| Market reference draw last update utc | 2026-11-04T19:38:18Z |
| Market reference away last update utc | 2026-11-04T19:38:18Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:18Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:18Z |
| Market best over 2 5 last update utc | 2026-11-04T19:38:18Z |
| Market best under 2 5 last update utc | 2026-11-04T19:37:33Z |
| Home probability edge | +0.8% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0268 |
| Raw ev home | 0.0441 |
| Raw edge prob draw | -0.0207 |
| Raw ev draw | -0.0509 |
| Raw edge prob away | -0.0061 |
| Raw ev away | -0.0456 |
| Count model | {"corners": {"alpha": 0.00930322941348174, "mu": 9.49812326939887, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,475.4318 |
| Elo away rating | 1,472.6402 |
| Elo rating diff | 62.7916 |
| Elo home expectancy | 0.5894 |

</details>


---

## 2026-11-07 — Nottingham Forest vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **56.4%**. Expected goals are 0.94 for Nottingham Forest and 1.84 for Manchester City (2.78 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.8%; Double Chance 1X: 43.6%; Double Chance X2: 79.8%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 52.0%; BTTS No (at least one team does not score): 48.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 20.2% | 4.96 |
| Draw | 23.4% | 4.27 |
| Manchester City win | 56.4% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.94 |
| Manchester City expected goals | 1.84 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.17% |
| 2 | 0-1 | 10.48% |
| 3 | 0-2 | 10.23% |
| 4 | 1-2 | 9.63% |
| 5 | 0-0 | 6.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 20.2% | 21.0% | 4.58 | -7.6% |
| Draw | 23.4% | 23.2% | 4.26 | -0.2% |
| Manchester City win | 56.4% | 55.8% | 1.78 | +0.4% |
| Over 2.5 | 52.7% | 58.2% | 1.70 | -10.5% |
| Under 2.5 | 47.3% | 41.8% | 2.34 | +10.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:30:00+00:00 |
| Fixture id | 59c5f635cfe11613c07e9a5520ced5c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:37:33Z |
| Market best draw last update utc | 2026-11-04T19:37:33Z |
| Market best away last update utc | 2026-11-04T19:37:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9416 |
| Dc lambda away | 1.8396 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:38:02.402368+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 52.0% |
| P btts no | 48.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.88 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.36 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.70 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.23325673304900899, "-10": 8.64518965023283e-06, "-11": 1.4272917121512213e-06, "-12": 2.1642731388047225e-07, "-13": 3.034012838900529e-08, "-14": 3.953641337559312e-09, "-15": 4.790618328098191e-10, "-16": 4.970028807278783e-11, "-2": 0.17568012607843395, "-3": 0.09504876817839446, "-4": 0.04039874268925713, "-5": 0.014081968638224598, "-6": 0.0041514153618729625, "-7": 0.0010590102276114885, "-8": 0.0002379067839838602, "-9": 4.7724589913658604e-05, "0": 0.23434689044248933, "1": 0.13144539955985052, "10": 1.2066416369779342e-08, "11": 1.0196982566886738e-09, "12": 7.914548644140111e-11, "13": 5.679193263759165e-12, "14": 3.788101901223665e-13, "15": 2.349476505336498e-14, "16": 1.2476523566019533e-15, "2": 0.05203376041404902, "3": 0.014410007996264334, "4": 0.003135022978895411, "5": 0.0005593599949724666, "6": 8.440717563029773e-05, "7": 1.102144366967393e-05, "8": 1.2673609095916005e-06, "9": 1.3013401738606131e-07} |
| Raw goal margin distribution | {"-1": 0.2391513643126143, "-10": 8.863662251327488e-06, "-11": 1.4633608032284923e-06, "-12": 2.218966488660991e-07, "-13": 3.110685382070399e-08, "-14": 4.0535538139488495e-09, "-15": 4.91168205131717e-10, "-16": 5.095626412996125e-11, "-2": 0.1801197388177519, "-3": 0.09745074574683539, "-4": 0.041419659378579055, "-5": 0.014437834089579214, "-6": 0.0042563257859384775, "-7": 0.0010857724767202627, "-8": 0.0002439189266918712, "-9": 4.893063809958037e-05, "0": 0.23885981009719773, "1": 0.11921524275405772, "10": 1.0943713218656946e-08, "11": 9.248218318335181e-10, "12": 7.178150327508005e-11, "13": 5.150780520682896e-12, "14": 3.4356431586322783e-13, "15": 2.1308726883295137e-14, "16": 1.1315662553655915e-15, "2": 0.04719235058768904, "3": 0.013069248578611256, "4": 0.0028433290683436267, "5": 0.0005073151119084092, "6": 7.655362581456153e-05, "7": 9.99596856930764e-06, "8": 1.1494410530904232e-06, "9": 1.1802587633488197e-07} |
| Unadjusted home-win probability | 18.3% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 57.8% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 52.0% |
| P home draw | 43.6% |
| P draw away | 79.8% |
| P home away | 76.6% |
| Raw p home draw | 42.2% |
| Raw p draw away | 81.7% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5266 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.08, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.78, "draw": 4.26, "home": 4.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:37:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.7, "under": 2.34}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.76, "draw": 4.11, "home": 4.54}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.54 |
| Reference draw odds | 4.11 |
| Reference away odds | 1.76 |
| Market reference 1x2 last update utc | 2026-11-04T19:38:18Z |
| Market reference home last update utc | 2026-11-04T19:38:18Z |
| Market reference draw last update utc | 2026-11-04T19:38:18Z |
| Market reference away last update utc | 2026-11-04T19:38:18Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:21Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:21Z |
| Market best over 2 5 last update utc | 2026-11-04T19:37:33Z |
| Market best under 2 5 last update utc | 2026-11-04T19:37:33Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | -0.0268 |
| Raw ev home | -0.1622 |
| Raw edge prob draw | 0.0064 |
| Raw ev draw | 0.0175 |
| Raw edge prob away | 0.0204 |
| Raw ev away | 0.0292 |
| Count model | {"corners": {"alpha": 0.00930322941348174, "mu": 9.724577865121287, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,415.6922 |
| Elo away rating | 1,636.6871 |
| Elo rating diff | -160.9950 |
| Elo home expectancy | 0.2836 |

</details>


---
