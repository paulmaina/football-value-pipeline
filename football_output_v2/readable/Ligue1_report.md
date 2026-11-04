# Ligue 1 — football model report

Fixtures in this report: **2**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,761 |
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
| Training sha256 | dc4ceaad59efa379db06d13591bef36328dc2144617d5b5cda3aeecde57892a5 |
| Training as of utc | 2026-11-04T19:40:11.047826+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 81, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 81, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 142, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_CHRONOLOGICAL_PARTITIONS', 'cutoff_utc': '2026-11-04T19:40:11.047826+00:00', 'observations': 508, 'observations_sha256': '12497e4ec4abbe4d77cc117bee61429cab3670855a67ce58bae6003d9677c369', 'eligible_training_matches': 186, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 183, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 23, 'retrospective_eligible_training_matches': 186, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'f99177162bf25726d3e4c3e5e3b1d6a557c14c372c55c20100d580d3e9d778f5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 126, 'tuning_matches': 17, 'audit_matches': 43, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1759, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1471, 'tuning_matches': 187, 'audit_matches': 96, 'audit_matchdays': 34, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8547715623172535, 'audit_candidate_poisson_score': 0.8530350185434455, 'audit_gain': 0.0017365437738079414, 'audit_gain_lower95': -0.004922528465493255, 'audit_baseline_briers': [0.5824611765258155, 0.17370333581411498, 0.21287609805690424, 0.24660314645935366], 'audit_candidate_briers': [0.5816251545925518, 0.17326144719684378, 0.2118685084312232, 0.2457311201596737], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1599.004 |
| Base scoring parameter | 0.200 |
| Home-advantage parameter | 0.202 |
| Dixon-Coles low-score adjustment | -0.054 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1761, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 2.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261104T194011047826Z_42e145ee25c55d2f0312a3234f4c3170e0b7244694ff1a11ed765c54d53fd8e9.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 2} |
| Legacy comparison status | {'None': 2} |
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

## 2026-11-06 — Toulouse vs Strasbourg

The model's most likely 1X2 outcome is **Toulouse win** at **44.8%**. Expected goals are 1.50 for Toulouse and 1.39 for Strasbourg (2.89 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.5%; Under 3.5 goals: 67.0%; Double Chance 1X: 70.2%; Double Chance X2: 55.2%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 83.2%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 44.8% | 2.23 |
| Draw | 25.4% | 3.94 |
| Strasbourg win | 29.8% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.50 |
| Strasbourg expected goals | 1.39 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.5% |
| Under 2.5 | 44.5% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.90% |
| 2 | 2-1 | 9.85% |
| 3 | 1-0 | 8.72% |
| 4 | 2-0 | 7.09% |
| 5 | 1-2 | 6.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 44.8% | 47.0% | 2.08 | -6.9% |
| Draw | 25.4% | 25.1% | 3.98 | +1.0% |
| Strasbourg win | 29.8% | 27.9% | 3.51 | +4.8% |
| Over 2.5 | 55.5% | 59.5% | 1.66 | -7.9% |
| Under 2.5 | 44.5% | 40.5% | 2.42 | +7.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:45:00+00:00 |
| Fixture id | 5e7d141f719835de18877ed95bedcb32 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:18Z |
| Market best draw last update utc | 2026-11-04T19:40:19Z |
| Market best away last update utc | 2026-11-04T19:40:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5044 |
| Dc lambda away | 1.3886 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:40:11.047826+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.62 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.79 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.94 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.16000739889878327, "-10": 4.2640350726857914e-07, "-11": 5.300164485283664e-08, "-12": 6.05314683603487e-09, "-13": 6.390783653824025e-10, "-14": 6.227786557202966e-11, "-15": 5.06066905142286e-12, "-2": 0.08832157662114483, "-3": 0.0352874306772064, "-4": 0.011157628721573528, "-5": 0.0029057313694244575, "-6": 0.0006417059499910641, "-7": 0.00012284436297306124, "-8": 2.0735237894605782e-05, "-9": 3.128054709034118e-06, "0": 0.2538232236987744, "1": 0.2266366144363045, "10": 1.2381691469183783e-06, "11": 1.667305984152812e-07, "12": 2.0628797930764325e-08, "13": 2.359465219529432e-09, "14": 2.490920893030041e-10, "15": 2.1928095005707282e-11, "2": 0.1351736406503391, "3": 0.0585075600874317, "4": 0.02004151770267836, "5": 0.005654326913034859, "6": 0.0013527834141513738, "7": 0.0002805525289307422, "8": 5.130205112391458e-05, "9": 8.384299786362756e-06} |
| Raw goal margin distribution | {"-1": 0.1844551637888261, "-10": 4.915543238291698e-07, "-11": 6.109984381779433e-08, "-12": 6.978016009027922e-09, "-13": 7.367240850848097e-10, "-14": 7.179339189042076e-11, "-15": 5.8338960897160425e-12, "-2": 0.10181635970500427, "-3": 0.040679048906784296, "-4": 0.012862419159970514, "-5": 0.0033497023222817607, "-6": 0.0007397531421952642, "-7": 0.00014161393315982666, "-8": 2.39034052698351e-05, "-9": 3.6059947706560988e-06, "0": 0.26014770966139905, "1": 0.2003499006733534, "10": 1.0945586449872882e-06, "11": 1.4739215424124947e-07, "12": 1.8236142587635027e-08, "13": 2.0857998763823304e-09, "14": 2.2020085092826326e-10, "15": 1.9384739166159903e-11, "2": 0.11949536726583215, "3": 0.051721492051548586, "4": 0.017716978746182943, "5": 0.004998503168690712, "6": 0.0011958792418952226, "7": 0.00024801231453591796, "8": 4.5351722503356974e-05, "9": 7.411836933725013e-06} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 34.4% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.1% |
| Raw p btts yes | 59.0% |
| P home draw | 70.2% |
| P draw away | 55.2% |
| P home away | 74.6% |
| Raw p home draw | 65.6% |
| Raw p draw away | 60.4% |
| Raw p home away | 74.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5550 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.45, "draw": 3.82, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.51, "draw": 3.98, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.42}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.82 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:18Z |
| Market reference home last update utc | 2026-11-04T19:40:18Z |
| Market reference draw last update utc | 2026-11-04T19:40:18Z |
| Market reference away last update utc | 2026-11-04T19:40:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:19Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:19Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:19Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:19Z |
| Home probability edge | -2.2% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.0742 |
| Raw ev home | -0.1768 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | 0.0354 |
| Raw edge prob away | 0.0651 |
| Raw ev away | 0.2077 |
| Count model | {"corners": {"alpha": 0.015416351116715491, "mu": 9.118242101605375, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,453.8748 |
| Elo away rating | 1,507.0944 |
| Elo rating diff | 6.7804 |
| Elo home expectancy | 0.5098 |

</details>


---

## 2026-11-07 — Auxerre vs Paris FC

The model's most likely 1X2 outcome is **Paris FC win** at **51.3%**. Expected goals are 1.22 for Auxerre and 1.51 for Paris FC (2.73 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.3%; Under 3.5 goals: 70.4%; Double Chance 1X: 48.7%; Double Chance X2: 75.6%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 24.4% | 4.09 |
| Draw | 24.2% | 4.12 |
| Paris FC win | 51.3% | 1.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.22 |
| Paris FC expected goals | 1.51 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 52.3% |
| Under 2.5 | 47.7% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 0-1 | 10.92% |
| 3 | 1-2 | 10.76% |
| 4 | 0-2 | 8.82% |
| 5 | 0-0 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 24.4% | 22.0% | 4.33 | +5.7% |
| Draw | 24.2% | 23.2% | 4.11 | -0.4% |
| Paris FC win | 51.3% | 54.8% | 1.87 | -4.0% |
| Over 2.5 | 52.3% | 55.8% | 1.77 | -7.4% |
| Under 2.5 | 47.7% | 44.2% | 2.22 | +5.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T18:00:00+00:00 |
| Fixture id | 8553a80cf1ae5cbe3e7a69b76ce8167f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:18Z |
| Market best draw last update utc | 2026-11-04T19:40:18Z |
| Market best away last update utc | 2026-11-04T19:40:19Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2203 |
| Dc lambda away | 1.5085 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:40:11.047826+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.31 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.28 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.38 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.87 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.255316820863338, "-10": 1.5384119125257086e-06, "-11": 2.081033756982801e-07, "-12": 2.5857961532473273e-08, "-13": 2.9699276662980012e-09, "-14": 3.152822216718628e-10, "-15": 2.8241162775718197e-11, "-2": 0.15635093720468918, "-3": 0.06889522210328852, "-4": 0.023904274811950118, "-5": 0.00681101993156912, "-6": 0.00164264546853251, "-7": 0.00034299095492619757, "-8": 6.309390293544369e-05, "-9": 1.0366641493778641e-05, "0": 0.24244326558076892, "1": 0.140284333032022, "10": 1.2626390184636023e-07, "11": 1.3816350592798133e-08, "12": 1.3887246782626741e-09, "13": 1.2902545176702042e-10, "14": 1.1079920561824736e-11, "15": 8.028370134894372e-13, "2": 0.0699915925031979, "3": 0.024948367853651874, "4": 0.007002228125571678, "5": 0.0016139143457359656, "6": 0.0003148616876455431, "7": 5.318219945796272e-05, "8": 7.913683346660965e-06, "9": 1.0518092922349103e-06} |
| Raw goal margin distribution | {"-1": 0.21517128794747534, "-10": 1.2965149397229874e-06, "-11": 1.7538159539901312e-07, "-12": 2.1792104679294507e-08, "-13": 2.5029418700549995e-09, "-14": 2.6570784280753785e-10, "-15": 2.3800575876817043e-11, "-2": 0.13176661222855854, "-3": 0.058062267982440775, "-4": 0.020145611955159192, "-5": 0.005740068068982034, "-6": 0.0013843590089758064, "-7": 0.0002890597073716026, "-8": 5.317313724315547e-05, "-9": 8.736610437038346e-06, "0": 0.26652613444861245, "1": 0.17281600975361597, "10": 1.5554426657201524e-07, "11": 1.702033667764849e-08, "12": 1.7107673562446014e-09, "13": 1.5894621479894214e-10, "14": 1.3649333596250658e-11, "15": 9.89013428335467e-13, "2": 0.0862225130296107, "3": 0.030733848100837752, "4": 0.008626031844693705, "5": 0.0019881780900689876, "6": 0.0003878775292089925, "7": 6.551505290436183e-05, "8": 9.748851841576719e-06, "9": 1.2957219168894685e-06} |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 43.3% |
| Raw p over 1 5 | 76.3% |
| Raw p under 3 5 | 70.8% |
| Raw p btts yes | 55.5% |
| P home draw | 48.7% |
| P draw away | 75.6% |
| P home away | 75.8% |
| Raw p home draw | 56.7% |
| Raw p draw away | 69.9% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5232 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.36, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.09, "price": 1.36, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.79, "draw": 4.11, "home": 4.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.87, "draw": 4.04, "home": 4.3}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:19Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.77, "under": 2.22}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.33 |
| Reference draw odds | 4.11 |
| Reference away odds | 1.79 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:18Z |
| Market reference home last update utc | 2026-11-04T19:40:18Z |
| Market reference draw last update utc | 2026-11-04T19:40:18Z |
| Market reference away last update utc | 2026-11-04T19:40:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:19Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:19Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:19Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:19Z |
| Home probability edge | +2.4% |
| Draw probability edge | +1.0% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0809 |
| Raw ev home | 0.3027 |
| Raw edge prob draw | 0.0344 |
| Raw ev draw | 0.0954 |
| Raw edge prob away | -0.1153 |
| Raw ev away | -0.1910 |
| Count model | {"corners": {"alpha": 0.015416351116715491, "mu": 9.292618797632045, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,456.4699 |
| Elo away rating | 1,497.8028 |
| Elo rating diff | 18.6671 |
| Elo home expectancy | 0.5268 |

</details>


---
