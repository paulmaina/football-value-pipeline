# Primeira Liga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,620 |
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
| Training sha256 | b3df8a6ba2e5ca811847821ea9d38323a7d64bb77cbc57ee92f21ada8c933425 |
| Training as of utc | 2026-11-04T09:31:00.482336+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1314, 'tuning_matches': 198, 'audit_matches': 105, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.871133946106074, 'audit_candidate_poisson_score': 0.864686880155924, 'audit_gain': 0.006447065950149988, 'audit_gain_lower95': -0.0029276060876474914, 'audit_baseline_briers': [0.5561718035340527, 0.18693031458144618, 0.22413462273999446, 0.24642668920158067], 'audit_candidate_briers': [0.5573847307845401, 0.18683181103592617, 0.22226561114095394, 0.2465786491177637], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1471.745 |
| Base scoring parameter | 0.087 |
| Home-advantage parameter | 0.174 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 9.00 |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
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

## 2026-11-06 — FC Famalicão vs FC Arouca

The model's most likely 1X2 outcome is **FC Famalicão win** at **48.7%**. Expected goals are 1.47 for FC Famalicão and 1.00 for FC Arouca (2.47 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 44.8%; Under 3.5 goals: 76.4%; Double Chance 1X: 73.7%; Double Chance X2: 51.3%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Famalicão win | 48.7% | 2.06 |
| Draw | 25.0% | 3.99 |
| FC Arouca win | 26.3% | 3.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Famalicão expected goals | 1.47 |
| FC Arouca expected goals | 1.00 |
| Expected total goals | 2.47 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 44.8% |
| Under 2.5 | 55.2% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.06% |
| 2 | 1-1 | 11.81% |
| 3 | 2-0 | 9.15% |
| 4 | 2-1 | 9.14% |
| 5 | 0-1 | 9.08% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:45:00+00:00 |
| Fixture id | fdorg:567353 |
| Matched home-team name | Famalicao |
| Matched away-team name | Arouca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4703 |
| Dc lambda away | 0.9993 |
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
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.76 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.54 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.17011672584290727, "-10": 2.6454477131805612e-08, "-11": 2.3771455314199498e-09, "-12": 1.9613101280775501e-10, "-13": 1.4954996452512397e-11, "-14": 1.055835811028706e-12, "-15": 6.406675802145749e-14, "-2": 0.06714176247272613, "-3": 0.020069450614050927, "-4": 0.004685387827340297, "-5": 0.0008941102595004602, "-6": 0.00014400811417344353, "-7": 2.0043429463970233e-05, "-8": 2.4544759626969864e-06, "-9": 2.682173370161998e-07, "0": 0.2503610778520413, "1": 0.2473611820050017, "10": 1.2574170428225922e-06, "11": 1.6623939388173867e-07, "12": 2.018006046938938e-08, "13": 2.26391711454329e-09, "14": 2.351627944449948e-10, "15": 2.0994376833773568e-11, "2": 0.14534120928617147, "3": 0.06391893528901493, "4": 0.0219552106847118, "5": 0.006164262980213969, "6": 0.0014607471893325955, "7": 0.0002991287417750447, "8": 5.389430942620282e-05, "9": 8.665008448934917e-06} |
| Raw goal margin distribution | {"-1": 0.17011672584290727, "-10": 2.6454477131805612e-08, "-11": 2.3771455314199498e-09, "-12": 1.9613101280775501e-10, "-13": 1.4954996452512397e-11, "-14": 1.055835811028706e-12, "-15": 6.406675802145749e-14, "-2": 0.06714176247272613, "-3": 0.020069450614050927, "-4": 0.004685387827340297, "-5": 0.0008941102595004602, "-6": 0.00014400811417344353, "-7": 2.0043429463970233e-05, "-8": 2.4544759626969864e-06, "-9": 2.682173370161998e-07, "0": 0.2503610778520413, "1": 0.2473611820050017, "10": 1.2574170428225922e-06, "11": 1.6623939388173867e-07, "12": 2.018006046938938e-08, "13": 2.26391711454329e-09, "14": 2.351627944449948e-10, "15": 2.0994376833773568e-11, "2": 0.14534120928617147, "3": 0.06391893528901493, "4": 0.0219552106847118, "5": 0.006164262980213969, "6": 0.0014607471893325955, "7": 0.0002991287417750447, "8": 5.389430942620282e-05, "9": 8.665008448934917e-06} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.0% |
| P home draw | 73.7% |
| P draw away | 51.3% |
| P home away | 75.0% |
| Raw p home draw | 73.7% |
| Raw p draw away | 51.3% |
| Raw p home away | 75.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4484 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,482.5254 |
| Elo away rating | 1,488.7246 |
| Elo rating diff | 53.8007 |
| Elo home expectancy | 0.5768 |

</details>


---
