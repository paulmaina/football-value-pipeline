# Eredivisie — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Eredivisie |
| Training matches | 1,629 |
| Training data through | 2026-11-01 |
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
| Training sha256 | 615de97a97f0d322c268f8b3f3257e878336d0e9922ced304f9c92ec61ef9060 |
| Training as of utc | 2026-11-03T13:22:54.974525+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1629, 'tune_start_date': '2025-11-04', 'audit_start_date': '2026-05-05', 'training_shot_matches': 1323, 'tuning_matches': 189, 'audit_matches': 114, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6640276255247738, 'audit_candidate_poisson_score': 0.6541627035388013, 'audit_gain': 0.009864921985972441, 'audit_gain_lower95': -0.0021659948572718187, 'audit_baseline_briers': [0.6216764809503332, 0.0984760918312214, 0.2796799781023385, 0.2302570571451794], 'audit_candidate_briers': [0.6176748823631296, 0.09759280650048496, 0.27680113308105514, 0.22438463488066576], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1641.383 |
| Base scoring parameter | 0.290 |
| Home-advantage parameter | 0.183 |
| Dixon-Coles low-score adjustment | -0.081 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1629, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 19.00 |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
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

## 2026-11-06 — Willem II Tilburg vs PEC Zwolle

The model's most likely 1X2 outcome is **PEC Zwolle win** at **46.4%**. Expected goals are 1.22 for Willem II Tilburg and 1.64 for PEC Zwolle (2.86 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 54.5%; Under 3.5 goals: 67.8%; Double Chance 1X: 53.6%; Double Chance X2: 72.6%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Willem II Tilburg win | 27.4% | 3.65 |
| Draw | 26.2% | 3.82 |
| PEC Zwolle win | 46.4% | 2.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Willem II Tilburg expected goals | 1.22 |
| PEC Zwolle expected goals | 1.64 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 78.9% |
| Under 1.5 | 21.1% |
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.37% |
| 2 | 1-2 | 9.41% |
| 3 | 0-1 | 8.47% |
| 4 | 0-2 | 7.72% |
| 5 | 2-1 | 6.97% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:00:00+00:00 |
| Fixture id | fdorg:558845 |
| Matched home-team name | Willem II |
| Matched away-team name | Zwolle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.2181 |
| Dc lambda away | 1.6438 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.06 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.73 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.17 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.21596482458115823, "-10": 2.717860045360891e-06, "-11": 4.001481768720594e-07, "-12": 5.4125019343982336e-08, "-13": 6.767714747944977e-09, "-14": 7.814616726139412e-10, "-15": 7.555141165768844e-11, "-2": 0.14353948290028867, "-3": 0.06824164528112653, "-4": 0.025631338508681954, "-5": 0.007921052191235711, "-6": 0.002074503162506915, "-7": 0.00047076011431860815, "-8": 9.41655010373915e-05, "-9": 1.683073982188906e-05, "0": 0.26188564495980815, "1": 0.1576465043544168, "10": 1.3575043509472647e-07, "11": 1.4811068742339102e-08, "12": 1.4846190665329601e-09, "13": 1.3756578433680907e-10, "14": 1.1771382718018928e-11, "15": 8.433615458545495e-13, "2": 0.07882685607857988, "3": 0.02777178096065149, "4": 0.0077299545912824005, "5": 0.0017702717760471325, "6": 0.0003435758153685125, "7": 5.777760804012334e-05, "8": 8.564522099635814e-06, "9": 1.1343992570176529e-06} |
| Raw goal margin distribution | {"-1": 0.21596482458115823, "-10": 2.717860045360891e-06, "-11": 4.001481768720594e-07, "-12": 5.4125019343982336e-08, "-13": 6.767714747944977e-09, "-14": 7.814616726139412e-10, "-15": 7.555141165768844e-11, "-2": 0.14353948290028867, "-3": 0.06824164528112653, "-4": 0.025631338508681954, "-5": 0.007921052191235711, "-6": 0.002074503162506915, "-7": 0.00047076011431860815, "-8": 9.41655010373915e-05, "-9": 1.683073982188906e-05, "0": 0.26188564495980815, "1": 0.1576465043544168, "10": 1.3575043509472647e-07, "11": 1.4811068742339102e-08, "12": 1.4846190665329601e-09, "13": 1.3756578433680907e-10, "14": 1.1771382718018928e-11, "15": 8.433615458545495e-13, "2": 0.07882685607857988, "3": 0.02777178096065149, "4": 0.0077299545912824005, "5": 0.0017702717760471325, "6": 0.0003435758153685125, "7": 5.777760804012334e-05, "8": 8.564522099635814e-06, "9": 1.1343992570176529e-06} |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 46.4% |
| Raw p over 1 5 | 78.9% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 57.7% |
| P home draw | 53.6% |
| P draw away | 72.6% |
| P home away | 73.8% |
| Raw p home draw | 53.6% |
| Raw p draw away | 72.6% |
| Raw p home away | 73.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5452 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,319.6939 |
| Elo away rating | 1,410.7310 |
| Elo rating diff | -31.0371 |
| Elo home expectancy | 0.4555 |

</details>


---
