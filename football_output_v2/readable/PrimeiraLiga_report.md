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
| Training as of utc | 2026-11-04T10:20:29.086436+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1314, 'tuning_matches': 198, 'audit_matches': 105, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.871133946106074, 'audit_candidate_poisson_score': 0.864686880155924, 'audit_gain': 0.006447065950149988, 'audit_gain_lower95': -0.0029276060876474914, 'audit_baseline_briers': [0.5561718035340527, 0.18693031458144618, 0.22413462273999446, 0.24642668920158067], 'audit_candidate_briers': [0.5573847307845401, 0.18683181103592617, 0.22226561114095394, 0.2465786491177637], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1471.672 |
| Base scoring parameter | 0.087 |
| Home-advantage parameter | 0.174 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
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

## 2026-11-06 — Famalicão vs Arouca

The model's most likely 1X2 outcome is **Famalicão win** at **47.3%**. Expected goals are 1.47 for Famalicão and 1.00 for Arouca (2.47 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.4%; Under 3.5 goals: 70.1%; Double Chance 1X: 73.1%; Double Chance X2: 52.7%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 85.6%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Famalicão win | 47.3% | 2.11 |
| Draw | 25.8% | 3.88 |
| Arouca win | 26.9% | 3.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Famalicão expected goals | 1.47 |
| Arouca expected goals | 1.00 |
| Expected total goals | 2.47 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 51.4% |
| Under 2.5 | 48.6% |
| Over 3.5 | 29.9% |
| Under 3.5 | 70.1% |
| Over 4.5 | 14.4% |
| Under 4.5 | 85.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.20% |
| 2 | 1-0 | 10.30% |
| 3 | 2-1 | 8.99% |
| 4 | 2-0 | 8.03% |
| 5 | 0-1 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Famalicão win | 47.3% | 46.7% | 2.07 | -2.1% |
| Draw | 25.8% | 26.1% | 3.61 | -6.9% |
| Arouca win | 26.9% | 27.1% | 3.48 | -6.4% |
| Over 2.5 | 51.4% | 51.4% | 1.87 | -3.9% |
| Under 2.5 | 48.6% | 48.6% | 1.97 | -4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:45:00+00:00 |
| Fixture id | d98d64a216d4db8db11c9b5017f76ca6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T10:20:24Z |
| Market best draw last update utc | 2026-11-04T10:20:24Z |
| Market best away last update utc | 2026-11-04T10:20:24Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
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
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.81 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.10 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.34 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.97 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.16711237168118315, "-10": 6.413128010044245e-08, "-11": 6.435526262816145e-09, "-12": 5.932090239443874e-10, "-13": 5.0543839473791904e-11, "-14": 3.98039855507774e-12, "-15": 2.644696100766583e-13, "-2": 0.0710806361409515, "-3": 0.023232924314229405, "-4": 0.005979584854239772, "-5": 0.0012638570811655462, "-6": 0.00022611325880293493, "-7": 3.50239566768813e-05, "-8": 4.7793962214496806e-06, "-9": 5.825440948917593e-07, "0": 0.2579777483025831, "1": 0.22521189007534437, "10": 2.824958102002761e-06, "11": 4.1709983475977985e-07, "12": 5.6568875841374216e-08, "13": 7.091724851703103e-09, "14": 8.217203766437991e-10, "15": 8.033173004557712e-11, "2": 0.1425550541247541, "3": 0.0685565634768488, "4": 0.025961515683443345, "5": 0.008073666858818888, "6": 0.0021252632722833474, "7": 0.00048435720391891505, "8": 9.72495142869416e-05, "9": 1.7440424759128456e-05} |
| Raw goal margin distribution | {"-1": 0.17011468515100486, "-10": 2.6438724120387384e-08, "-11": 2.375565989792102e-09, "-12": 1.959871260418521e-10, "-13": 1.4942989540390754e-11, "-14": 1.0549156957979068e-12, "-15": 6.400702886537441e-14, "-2": 0.06713731116009497, "-3": 0.020066912709693106, "-4": 0.004684497153724774, "-5": 0.0008938816394166603, "-6": 0.00014396167230775692, "-7": 2.003561099385338e-05, "-8": 2.453351335382738e-06, "-9": 2.6807606835683034e-07, "0": 0.2503673000714643, "1": 0.24736692444981342, "10": 1.2571264936457668e-06, "11": 1.6619556627315113e-07, "12": 2.017407948764552e-08, "13": 2.263171806534338e-09, "14": 2.350778091212527e-10, "15": 2.0986276822993136e-11, "2": 0.145342170328282, "3": 0.06391784250745877, "4": 0.021954238295466545, "5": 0.006163810237732578, "6": 0.0014605955546429057, "7": 0.00029908837362111905, "8": 5.388532854791681e-05, "9": 8.66328661638614e-06} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.0% |
| P home draw | 73.1% |
| P draw away | 52.7% |
| P home away | 74.2% |
| Raw p home draw | 73.7% |
| Raw p draw away | 51.3% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1199 |
| Totals anchor target over 2 5 | 0.5139 |
| Totals anchor reference over odds | 1.87 |
| Totals anchor reference under odds | 1.97 |
| Totals anchor reference last update utc | 2026-11-04T10:20:24Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4456 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:24Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:24Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:24Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.48, "draw": 3.61, "home": 2.07}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:24Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.87, "under": 1.97}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.07 |
| Reference draw odds | 3.61 |
| Reference away odds | 3.48 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:24Z |
| Market reference home last update utc | 2026-11-04T10:20:24Z |
| Market reference draw last update utc | 2026-11-04T10:20:24Z |
| Market reference away last update utc | 2026-11-04T10:20:24Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-11-04T10:20:24Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:20:24Z |
| Market best over 2 5 last update utc | 2026-11-04T10:20:24Z |
| Market best under 2 5 last update utc | 2026-11-04T10:20:24Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0193 |
| Raw ev home | 0.0072 |
| Raw edge prob draw | -0.0109 |
| Raw ev draw | -0.0962 |
| Raw edge prob away | -0.0084 |
| Raw ev away | -0.0845 |
| Elo home rating | 1,482.5254 |
| Elo away rating | 1,488.7246 |
| Elo rating diff | 53.8007 |
| Elo home expectancy | 0.5768 |

</details>


---
