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
| Training as of utc | 2026-11-04T10:20:26.740559+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1629, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1323, 'tuning_matches': 189, 'audit_matches': 114, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.664013504414629, 'audit_candidate_poisson_score': 0.6541573315881037, 'audit_gain': 0.009856172826525289, 'audit_gain_lower95': -0.0021770816139405416, 'audit_baseline_briers': [0.6216765281812682, 0.09847377645327035, 0.2796729197845708, 0.2302529853131095], 'audit_candidate_briers': [0.6176798109864696, 0.09759069645539366, 0.27679487113827406, 0.22438063704773317], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1639.315 |
| Base scoring parameter | 0.290 |
| Home-advantage parameter | 0.183 |
| Dixon-Coles low-score adjustment | -0.081 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1629, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
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
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
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

## 2026-11-06 — Willem II vs FC Zwolle

The model's most likely 1X2 outcome is **FC Zwolle win** at **43.5%**. Expected goals are 1.22 for Willem II and 1.64 for FC Zwolle (2.86 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 55.0%; Under 3.5 goals: 67.9%; Double Chance 1X: 56.5%; Double Chance X2: 68.2%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Willem II win | 31.8% | 3.14 |
| Draw | 24.7% | 4.05 |
| FC Zwolle win | 43.5% | 2.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Willem II expected goals | 1.22 |
| FC Zwolle expected goals | 1.64 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.8% |
| Under 1.5 | 21.2% |
| Over 2.5 | 55.0% |
| Under 2.5 | 45.0% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.66% |
| 2 | 1-2 | 8.82% |
| 3 | 2-1 | 8.09% |
| 4 | 0-1 | 7.94% |
| 5 | 0-2 | 7.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Willem II win | 31.8% | 33.7% | 2.83 | -9.9% |
| Draw | 24.7% | 24.0% | 3.91 | -3.5% |
| FC Zwolle win | 43.5% | 42.3% | 2.42 | +5.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:00:00+00:00 |
| Fixture id | 926c11a6b5d1773d9024296a215d0f71 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T10:20:25Z |
| Market best draw last update utc | 2026-11-04T10:20:25Z |
| Market best away last update utc | 2026-11-04T10:19:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Willem II |
| Matched away-team name | Zwolle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2183 |
| Dc lambda away | 1.6440 |
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
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.98 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.72 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.12 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.20243978319464886, "-10": 2.550077853641865e-06, "-11": 3.7548931299340625e-07, "-12": 5.0795525680399336e-08, "-13": 6.352141985063483e-09, "-14": 7.335592050532946e-10, "-15": 7.092631786889914e-11, "-2": 0.134564475426251, "-3": 0.0639801704087665, "-4": 0.024033065527858718, "-5": 0.0074278945606344295, "-6": 0.001945556296083438, "-7": 0.00044154751895810244, "-8": 8.83321014135484e-05, "-9": 1.5789905143420916e-05, "0": 0.24685870877559637, "1": 0.18295560949038658, "10": 1.577681532090879e-07, "11": 1.7216181922571592e-08, "12": 1.7259892309184927e-09, "13": 1.5995807891050032e-10, "14": 1.3689718376185254e-11, "15": 9.809347434867193e-13, "2": 0.0914975454960659, "3": 0.032240203452834106, "4": 0.008975009398129494, "5": 0.0020557241214604173, "6": 0.0003990398454921942, "7": 6.711556810308199e-05, "8": 9.950335959390571e-06, "9": 1.3181719417187018e-06} |
| Raw goal margin distribution | {"-1": 0.2159425715885417, "-10": 2.7201687374706143e-06, "-11": 4.0053455191585214e-07, "-12": 5.41836010072707e-08, "-13": 6.775831576697769e-09, "-14": 7.82487802801806e-10, "-15": 7.565712248955452e-11, "-2": 0.1435399623999195, "-3": 0.0682476651116437, "-4": 0.02563607751077124, "-5": 0.007923337140554387, "-6": 0.002075325428216725, "-7": 0.0004709988581180883, "-8": 9.42238765130514e-05, "-9": 1.684309609505441e-05, "0": 0.2618844473434234, "1": 0.1576361553634267, "10": 1.3593442245330816e-07, "11": 1.4833613114519536e-08, "12": 1.487127436641757e-09, "13": 1.3782128161583277e-10, "14": 1.1795181240088123e-11, "15": 8.451819654853529e-13, "2": 0.07883508648554403, "3": 0.027778441637267694, "4": 0.007732946695717989, "5": 0.0017712299059729336, "6": 0.0003438162254517293, "7": 5.7827361239547024e-05, "8": 8.573296602284295e-06, "9": 1.135748488823446e-06} |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 46.4% |
| Raw p over 1 5 | 78.9% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 57.7% |
| P home draw | 56.5% |
| P draw away | 68.2% |
| P home away | 75.3% |
| Raw p home draw | 53.6% |
| Raw p draw away | 72.6% |
| Raw p home away | 73.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5498 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:25Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:25Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:41Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.42, "draw": 3.69, "home": 2.8}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.28, "draw": 3.91, "home": 2.83}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.83 |
| Reference draw odds | 3.91 |
| Reference away odds | 2.28 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:25Z |
| Market reference home last update utc | 2026-11-04T10:20:25Z |
| Market reference draw last update utc | 2026-11-04T10:20:25Z |
| Market reference away last update utc | 2026-11-04T10:20:25Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.47 |
| Market reference over 2 5 last update utc | 2026-11-04T10:20:26Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:20:26Z |
| Home probability edge | -1.9% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | -0.0629 |
| Raw ev home | -0.2241 |
| Raw edge prob draw | 0.0215 |
| Raw ev draw | 0.0240 |
| Raw edge prob away | 0.0414 |
| Raw ev away | 0.1228 |
| Elo home rating | 1,319.6939 |
| Elo away rating | 1,410.7310 |
| Elo rating diff | -31.0371 |
| Elo home expectancy | 0.4555 |

</details>


---
