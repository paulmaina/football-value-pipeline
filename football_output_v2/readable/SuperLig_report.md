# Super Lig — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,840 |
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
| Training sha256 | 428b36b889bc8107b0a0c389334f72426054f163962dc5b037f54c55da735d9c |
| Training as of utc | 2026-11-04T10:20:31.558511+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1512, 'tuning_matches': 189, 'audit_matches': 91, 'audit_matchdays': 37, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8325808781597445, 'audit_candidate_poisson_score': 0.8249955374677742, 'audit_gain': 0.007585340691970255, 'audit_gain_lower95': -0.0033625185473820135, 'audit_baseline_briers': [0.5922711615757454, 0.16649579451704555, 0.22016577620350214, 0.2497311353345134], 'audit_candidate_briers': [0.5911122360258325, 0.16508071200426702, 0.21632094488190387, 0.24937852775967387], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1674.812 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 27.00 |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 1} |
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

## 2026-11-06 — Gazişehir Gaziantep vs Kasimpasa SK

The model's most likely 1X2 outcome is **Gazişehir Gaziantep win** at **36.9%**. Expected goals are 1.39 for Gazişehir Gaziantep and 1.41 for Kasimpasa SK (2.81 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.2%; Double Chance 1X: 64.7%; Double Chance X2: 63.1%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gazişehir Gaziantep win | 36.9% | 2.71 |
| Draw | 27.8% | 3.59 |
| Kasimpasa SK win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gazişehir Gaziantep expected goals | 1.39 |
| Kasimpasa SK expected goals | 1.41 |
| Expected total goals | 2.81 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.27% |
| 2 | 2-1 | 8.54% |
| 3 | 1-2 | 8.08% |
| 4 | 1-0 | 8.08% |
| 5 | 0-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gazişehir Gaziantep win | 36.9% | 37.4% | 2.61 | -3.8% |
| Draw | 27.8% | 28.0% | 3.46 | -3.6% |
| Kasimpasa SK win | 35.3% | 34.7% | 2.79 | -1.5% |
| Over 2.5 | 51.0% | 51.0% | 1.93 | -1.6% |
| Under 2.5 | 49.0% | 49.0% | 1.95 | -4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T17:00:00+00:00 |
| Fixture id | 51baab3ec98943f452377895491bfd6a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T10:20:05Z |
| Market best draw last update utc | 2026-11-04T10:20:05Z |
| Market best away last update utc | 2026-11-04T10:20:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Gaziantep |
| Matched away-team name | Kasimpasa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3919 |
| Dc lambda away | 1.4143 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.89 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.26 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.47 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.18627529451539387, "-10": 4.7320122655038706e-07, "-11": 5.7952902834811835e-08, "-12": 6.517467635871071e-09, "-13": 6.731752588174772e-10, "-14": 5.8056290455859735e-11, "-2": 0.1064458499812725, "-3": 0.04247833269216317, "-4": 0.013346190232435013, "-5": 0.0034432636141727294, "-6": 0.0007519025171511644, "-7": 0.00014215064752410894, "-8": 2.367523838475556e-05, "-9": 3.5219266721682367e-06, "0": 0.27847040635733256, "1": 0.1966660613774384, "10": 4.3321473399690893e-07, "11": 5.221620900171027e-08, "12": 5.779387483867449e-09, "13": 5.874945769950827e-10, "14": 4.986522526047119e-11, "2": 0.11071432107446819, "3": 0.04348258106441494, "4": 0.013445530754403967, "5": 0.003414001433570934, "6": 0.0007337155963842454, "7": 0.00013651734727700038, "8": 2.2377220703579797e-05, "9": 3.2761583177509285e-06} |
| Raw goal margin distribution | {"-1": 0.1907271386377898, "-10": 6.369660868695188e-07, "-11": 8.070725057771706e-08, "-12": 9.391101514724548e-09, "-13": 1.0028202974705809e-09, "-14": 8.881813992500041e-11, "-2": 0.11125317244637284, "-3": 0.04560203960999687, "-4": 0.014757148983254344, "-5": 0.0039276886101017846, "-6": 0.0008856919121996255, "-7": 0.00017302570834450053, "-8": 2.979169522975935e-05, "-9": 4.583138751316778e-06, "0": 0.27541808779322285, "1": 0.18752745719892053, "10": 5.430554458541525e-07, "11": 6.77194156211343e-08, "12": 7.755145861024511e-09, "13": 8.150220102999479e-10, "14": 7.104290007909864e-11, "2": 0.10776009772038685, "3": 0.04347129984608057, "4": 0.013845020621077855, "5": 0.003626611052106095, "6": 0.00080485824360379, "7": 0.00015474625227472307, "8": 2.622270605584121e-05, "9": 3.970252080144702e-06} |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 58.0% |
| P home draw | 64.7% |
| P draw away | 63.1% |
| P home away | 72.2% |
| Raw p home draw | 63.3% |
| Raw p draw away | 64.3% |
| Raw p home away | 72.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9656 |
| Totals anchor target over 2 5 | 0.5098 |
| Totals anchor reference over odds | 1.88 |
| Totals anchor reference under odds | 1.95 |
| Totals anchor reference last update utc | 2026-11-04T10:20:29Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5309 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.88, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:29Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:29Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.86, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.79, "draw": 3.46, "home": 2.61}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:20:05Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.93, "under": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.76, "draw": 3.39, "home": 2.57}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:29Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.88, "under": 1.95}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.57 |
| Reference draw odds | 3.39 |
| Reference away odds | 2.76 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:29Z |
| Market reference home last update utc | 2026-11-04T10:20:29Z |
| Market reference draw last update utc | 2026-11-04T10:20:29Z |
| Market reference away last update utc | 2026-11-04T10:20:29Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-11-04T10:20:29Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:20:29Z |
| Market best over 2 5 last update utc | 2026-11-04T10:20:05Z |
| Market best under 2 5 last update utc | 2026-11-04T10:20:05Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0163 |
| Raw ev home | -0.0677 |
| Raw edge prob draw | -0.0044 |
| Raw ev draw | -0.0471 |
| Raw edge prob away | 0.0206 |
| Raw ev away | 0.0249 |
| Elo home rating | 1,396.7846 |
| Elo away rating | 1,500.7901 |
| Elo rating diff | -44.0056 |
| Elo home expectancy | 0.4370 |

</details>


---
