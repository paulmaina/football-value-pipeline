# Eredivisie — football model report

Fixtures in this report: **3**.

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
| Training as of utc | 2026-11-04T19:40:44.422094+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1629, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1323, 'tuning_matches': 189, 'audit_matches': 114, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.664013504414629, 'audit_candidate_poisson_score': 0.6541573315881037, 'audit_gain': 0.009856172826525289, 'audit_gain_lower95': -0.0021770816139405416, 'audit_baseline_briers': [0.6216765281812682, 0.09847377645327035, 0.2796729197845708, 0.2302529853131095], 'audit_candidate_briers': [0.6176798109864696, 0.09759069645539366, 0.27679487113827406, 0.22438063704773317], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1638.394 |
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
| Live odds matched | 3.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 18.00 |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 3} |
| Legacy comparison status | {'None': 3} |
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

The model's most likely 1X2 outcome is **FC Zwolle win** at **43.5%**. Expected goals are 1.22 for Willem II and 1.64 for FC Zwolle (2.86 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.5%; Double Chance 1X: 56.5%; Double Chance X2: 68.2%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 77.4%; BTTS Yes (both teams score): 64.4%; BTTS No (at least one team does not score): 35.6%.

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
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.5% |
| Under 3.5 | 59.5% |
| Over 4.5 | 22.6% |
| Under 4.5 | 77.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.06% |
| 2 | 1-2 | 8.46% |
| 3 | 2-1 | 7.94% |
| 4 | 2-2 | 6.60% |
| 5 | 0-2 | 6.12% |

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
| Market best home last update utc | 2026-11-04T19:40:38Z |
| Market best draw last update utc | 2026-11-04T19:40:38Z |
| Market best away last update utc | 2026-11-04T19:40:17Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Willem II |
| Matched away-team name | Zwolle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2184 |
| Dc lambda away | 1.6441 |
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
| P btts yes | 64.4% |
| P btts no | 35.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.84 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.31 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.47 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.43 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.18807818924468758, "-10": 6.226010510959614e-06, "-11": 1.0357113730179454e-06, "-12": 1.5838876561335434e-07, "-13": 2.2408969472061486e-08, "-14": 2.9477096537226356e-09, "-15": 3.589067625548219e-10, "-16": 3.603090335950147e-11, "-2": 0.13394579238538282, "-3": 0.06986231791617437, "-4": 0.029104309979577244, "-5": 0.010041208888525773, "-6": 0.002947976412493851, "-7": 0.0007519904517293625, "-8": 0.00016941115494514432, "-9": 3.4150315045379416e-05, "0": 0.24685389725786439, "1": 0.1742197558663726, "10": 3.942604232157696e-07, "11": 4.860545613183801e-08, "12": 5.508629907868291e-09, "13": 5.775825317759288e-10, "14": 5.630536945681643e-11, "15": 5.080654865710888e-12, "16": 3.779950797881264e-13, "2": 0.09322209547199559, "3": 0.036033439556928545, "4": 0.011124819663680303, "5": 0.0028444258570487504, "6": 0.0006188787401708028, "7": 0.00011699487279740344, "8": 1.953302249366663e-05, "9": 2.9180659642978755e-06} |
| Raw goal margin distribution | {"-1": 0.21594417145465147, "-10": 2.7210985042850297e-06, "-11": 4.006891439388368e-07, "-12": 5.420691711815101e-08, "-13": 6.779048354653462e-09, "-14": 7.82893256399794e-10, "-15": 7.569896365977847e-11, "-2": 0.14354198304177312, "-3": 0.06825098144845922, "-4": 0.02563830157552894, "-5": 0.007924343783186256, "-6": 0.002075675485802786, "-7": 0.00047109832878658057, "-8": 9.424783972664889e-05, "-9": 1.6848113619552523e-05, "0": 0.2618684089509836, "1": 0.15763839003483313, "10": 1.3597958141390905e-07, "11": 1.4839181815968032e-08, "12": 1.4877502509434436e-09, "13": 1.3788499222718322e-10, "14": 1.1801134580063276e-11, "15": 8.456372173149979e-13, "2": 0.07883604505212838, "3": 0.027779711541880813, "4": 0.007733587902766067, "5": 0.0017714464425443077, "6": 0.00034387224030250625, "7": 5.783918556644566e-05, "8": 8.575411188649478e-06, "9": 1.136077020259528e-06} |
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
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1344 |
| Totals anchor target over 2 5 | 0.6270 |
| Totals anchor reference over odds | 1.54 |
| Totals anchor reference under odds | 2.49 |
| Totals anchor reference last update utc | 2026-11-04T19:40:38Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5498 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.85, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.42, "draw": 3.69, "home": 2.8}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.45, "home_away": 1.29, "home_draw": 1.58}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.28, "draw": 3.91, "home": 2.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.54, "under": 2.49}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.16, "under": 5.2}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.83 |
| Reference draw odds | 3.91 |
| Reference away odds | 2.28 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:38Z |
| Market reference home last update utc | 2026-11-04T19:40:38Z |
| Market reference draw last update utc | 2026-11-04T19:40:38Z |
| Market reference away last update utc | 2026-11-04T19:40:38Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.47 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:56Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:56Z |
| Home probability edge | -1.9% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.0629 |
| Raw ev home | -0.2241 |
| Raw edge prob draw | 0.0214 |
| Raw ev draw | 0.0239 |
| Raw edge prob away | 0.0415 |
| Raw ev away | 0.1228 |
| Market p home draw | 60.2% |
| Market home draw odds | 1.58 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T19:40:17Z |
| Market reference home draw last update utc | 2026-11-04T19:40:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.7% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:40:17Z |
| Market reference draw away last update utc | 2026-11-04T19:40:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:40:17Z |
| Market reference home away last update utc | 2026-11-04T19:40:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home draw odds | 1.55 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 84.5% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:38Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:38Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.8% |
| Market under 3 5 odds | 1.61 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:38Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.33 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:38Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,319.6939 |
| Elo away rating | 1,410.7310 |
| Elo rating diff | -31.0371 |
| Elo home expectancy | 0.4555 |

</details>


---

## 2026-11-07 — ADO Den Haag vs Sparta Rotterdam

The model's most likely 1X2 outcome is **Sparta Rotterdam win** at **37.1%**. Expected goals are 1.37 for ADO Den Haag and 1.51 for Sparta Rotterdam (2.88 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 55.1%; Under 3.5 goals: 67.4%; Double Chance 1X: 62.9%; Double Chance X2: 63.3%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ADO Den Haag win | 36.7% | 2.73 |
| Draw | 26.3% | 3.81 |
| Sparta Rotterdam win | 37.1% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ADO Den Haag expected goals | 1.37 |
| Sparta Rotterdam expected goals | 1.51 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.35% |
| 2 | 2-1 | 8.71% |
| 3 | 1-2 | 8.15% |
| 4 | 1-0 | 7.39% |
| 5 | 0-1 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ADO Den Haag win | 36.7% | 38.1% | 2.52 | -7.6% |
| Draw | 26.3% | 26.1% | 3.65 | -4.2% |
| Sparta Rotterdam win | 37.1% | 35.8% | 2.71 | +0.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:45:00+00:00 |
| Fixture id | da066424422bbd4438e5000312b822fd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:38Z |
| Market best draw last update utc | 2026-11-04T19:40:17Z |
| Market best away last update utc | 2026-11-04T19:40:17Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Den Haag |
| Matched away-team name | Sparta Rotterdam |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3676 |
| Dc lambda away | 1.5135 |
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
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.52 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.80 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.04 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.1851407762132636, "-10": 1.0903024008001732e-06, "-11": 1.477249411208966e-07, "-12": 1.8389720744241616e-08, "-13": 2.116286371786482e-09, "-14": 2.248168498213128e-10, "-15": 1.9932909705567073e-11, "-2": 0.11300896352749505, "-3": 0.04926592818460944, "-4": 0.016990747781503154, "-5": 0.004825166304135101, "-6": 0.0011618436833312545, "-7": 0.00024248274963038132, "-8": 4.461904063239592e-05, "-9": 7.337542961152098e-06, "0": 0.2625793892239201, "1": 0.19686093073159597, "10": 4.680158822825563e-07, "11": 5.7299786412025825e-08, "12": 6.445548291573721e-09, "13": 6.702621914855738e-10, "14": 6.434053972947714e-11, "15": 5.1548032748402646e-12, "2": 0.10912947782511254, "3": 0.04298940255021334, "4": 0.013397161348478818, "5": 0.0034379387555232336, "6": 0.0007480301542569749, "7": 0.0001410710201302072, "8": 2.3456474676966387e-05, "9": 3.4856094569785536e-06} |
| Raw goal margin distribution | {"-1": 0.19941530142302516, "-10": 1.1743657250705545e-06, "-11": 1.5911467081346183e-07, "-12": 1.9807585234891545e-08, "-13": 2.2794540098563538e-09, "-14": 2.42150437029875e-10, "-15": 2.1469755493489367e-11, "-2": 0.12172205921498461, "-3": 0.053064376847498484, "-4": 0.018300750161856096, "-5": 0.005197191092290517, "-6": 0.0012514229067023949, "-7": 0.000261178394065533, "-8": 4.8059209963915024e-05, "-9": 7.903274314984299e-06, "0": 0.2667303588406823, "1": 0.17929073893784658, "10": 4.262446238430798e-07, "11": 5.218567751668174e-08, "12": 5.87027152498548e-09, "13": 6.10440086547155e-10, "14": 5.859803094950201e-11, "15": 4.6947278202470066e-12, "2": 0.09938947584191964, "3": 0.03915252112788693, "4": 0.012201440625683317, "5": 0.003131096544195557, "6": 0.0006812671189052704, "7": 0.00012848017810270982, "8": 2.1362942164710625e-05, "9": 3.174512549889764e-06} |
| Unadjusted home-win probability | 33.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.9% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 59.1% |
| P home draw | 62.9% |
| P draw away | 63.3% |
| P home away | 73.7% |
| Raw p home draw | 60.1% |
| Raw p draw away | 66.6% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5509 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.71, "draw": 3.65, "home": 2.51}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.67, "draw": 3.62, "home": 2.52}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.52 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.67 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:38Z |
| Market reference home last update utc | 2026-11-04T19:40:38Z |
| Market reference draw last update utc | 2026-11-04T19:40:38Z |
| Market reference away last update utc | 2026-11-04T19:40:38Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:56Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:56Z |
| Home probability edge | -1.4% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0468 |
| Raw ev home | -0.1583 |
| Raw edge prob draw | 0.0059 |
| Raw ev draw | -0.0264 |
| Raw edge prob away | 0.0408 |
| Raw ev away | 0.0820 |
| Elo home rating | 1,353.4514 |
| Elo away rating | 1,463.4189 |
| Elo rating diff | -49.9676 |
| Elo home expectancy | 0.4286 |

</details>


---

## 2026-11-07 — Fortuna Sittard vs SC Telstar

The model's most likely 1X2 outcome is **Fortuna Sittard win** at **44.6%**. Expected goals are 1.54 for Fortuna Sittard and 1.44 for SC Telstar (2.98 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.5%; Under 3.5 goals: 65.1%; Double Chance 1X: 70.0%; Double Chance X2: 55.4%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 81.7%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fortuna Sittard win | 44.6% | 2.24 |
| Draw | 25.5% | 3.93 |
| SC Telstar win | 30.0% | 3.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fortuna Sittard expected goals | 1.54 |
| SC Telstar expected goals | 1.44 |
| Expected total goals | 2.98 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.8% |
| Under 1.5 | 19.2% |
| Over 2.5 | 57.5% |
| Under 2.5 | 42.5% |
| Over 3.5 | 34.9% |
| Under 3.5 | 65.1% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.84% |
| 2 | 2-1 | 9.90% |
| 3 | 1-0 | 7.89% |
| 4 | 1-2 | 6.99% |
| 5 | 2-0 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fortuna Sittard win | 44.6% | 47.0% | 2.08 | -7.3% |
| Draw | 25.5% | 25.2% | 3.74 | -4.7% |
| SC Telstar win | 30.0% | 27.9% | 3.46 | +3.7% |
| Over 2.5 | 57.5% | 59.2% | 1.64 | -5.7% |
| Under 2.5 | 42.5% | 40.8% | 2.33 | -1.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:30:00+00:00 |
| Fixture id | 33c5cad848eb423e163a9bf5631ccefe |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:17Z |
| Market best draw last update utc | 2026-11-04T19:40:38Z |
| Market best away last update utc | 2026-11-04T19:40:17Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | For Sittard |
| Matched away-team name | Telstar |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5366 |
| Dc lambda away | 1.4427 |
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
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.15 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.20 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.86 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.48 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.1563602183073526, "-10": 5.747383465344522e-07, "-11": 7.414917614824495e-08, "-12": 8.790710622891852e-09, "-13": 9.634764619835547e-10, "-14": 9.739462942640436e-11, "-15": 8.161026407129212e-12, "-2": 0.08996892252146772, "-3": 0.03706077826260345, "-4": 0.012112166439796727, "-5": 0.003265134316544133, "-6": 0.0007471037727504661, "-7": 0.00014827507879430115, "-8": 2.5958355245439393e-05, "-9": 4.062869196046103e-06, "0": 0.2546981836079996, "1": 0.22198058601704151, "10": 1.4354254545016625e-06, "11": 1.9725250850873309e-07, "12": 2.4908405347944793e-08, "13": 2.907828478505958e-09, "14": 3.130894413518899e-10, "15": 2.794370134897706e-11, "2": 0.13563041865864778, "3": 0.059509301657294664, "4": 0.020715617553221582, "5": 0.0059481627327773795, "6": 0.001449667676835556, "7": 0.0003064512698611146, "8": 5.714472790069124e-05, "9": 9.526592173911086e-06} |
| Raw goal margin distribution | {"-1": 0.18173477686209819, "-10": 6.680084377742158e-07, "-11": 8.61823047299752e-08, "-12": 1.0217290886421096e-08, "-13": 1.1198320245772605e-09, "-14": 1.132000929519169e-10, "-15": 9.485419815351942e-12, "-2": 0.10456932227366605, "-3": 0.04307510145995505, "-4": 0.014077761524521637, "-5": 0.0037950091325372887, "-6": 0.0008683457909143445, "-7": 0.0001723375590709649, "-8": 3.017094724800067e-05, "-9": 4.722202582961026e-06, "0": 0.2618983150814474, "1": 0.19416621114428365, "10": 1.2555653036218777e-06, "11": 1.7253658485659635e-07, "12": 2.1787358880497608e-08, "13": 2.54347485273151e-09, "14": 2.7385904176282284e-10, "15": 2.4442329456062204e-11, "2": 0.11863580045167037, "3": 0.05205273054713031, "4": 0.018119931314688302, "5": 0.005202852383696057, "6": 0.0012680229621877235, "7": 0.0002680526393633316, "8": 4.99844400919657e-05, "9": 8.332901271749478e-06} |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 34.8% |
| Raw p over 1 5 | 80.7% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 60.9% |
| P home draw | 70.0% |
| P draw away | 55.4% |
| P home away | 74.5% |
| Raw p home draw | 65.2% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5750 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.53, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.46, "draw": 3.66, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:17Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.64, "under": 2.33}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.74, "home": 2.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 3.74 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:38Z |
| Market reference home last update utc | 2026-11-04T19:40:38Z |
| Market reference draw last update utc | 2026-11-04T19:40:38Z |
| Market reference away last update utc | 2026-11-04T19:40:38Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:17Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:17Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:17Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:17Z |
| Home probability edge | -2.4% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0798 |
| Raw ev home | -0.1893 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | -0.0205 |
| Raw edge prob away | 0.0695 |
| Raw ev away | 0.2052 |
| Elo home rating | 1,444.9830 |
| Elo away rating | 1,422.9487 |
| Elo rating diff | 82.0343 |
| Elo home expectancy | 0.6159 |

</details>


---
