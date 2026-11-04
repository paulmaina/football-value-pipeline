# Primeira Liga — football model report

Fixtures in this report: **3**.

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
| Training as of utc | 2026-11-04T19:40:46.372187+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1314, 'tuning_matches': 198, 'audit_matches': 105, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.871133946106074, 'audit_candidate_poisson_score': 0.864686880155924, 'audit_gain': 0.006447065950149988, 'audit_gain_lower95': -0.0029276060876474914, 'audit_baseline_briers': [0.5561718035340527, 0.18693031458144618, 0.22413462273999446, 0.24642668920158067], 'audit_candidate_briers': [0.5573847307845401, 0.18683181103592617, 0.22226561114095394, 0.2465786491177637], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1470.845 |
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
| Live odds matched | 3.00 |
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
| Totals anchor fixtures | {'ANCHORED_MAIN': 3} |
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

## 2026-11-06 — Famalicão vs Arouca

The model's most likely 1X2 outcome is **Famalicão win** at **46.9%**. Expected goals are 1.47 for Famalicão and 1.00 for Arouca (2.47 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 48.9%; Under 3.5 goals: 72.4%; Double Chance 1X: 73.2%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 52.5%; BTTS No (at least one team does not score): 47.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Famalicão win | 46.9% | 2.13 |
| Draw | 26.3% | 3.81 |
| Arouca win | 26.8% | 3.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Famalicão expected goals | 1.47 |
| Arouca expected goals | 1.00 |
| Expected total goals | 2.47 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.45% |
| 2 | 1-0 | 11.01% |
| 3 | 2-1 | 8.92% |
| 4 | 2-0 | 8.28% |
| 5 | 0-1 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Famalicão win | 46.9% | 46.2% | 2.09 | -1.9% |
| Draw | 26.3% | 26.8% | 3.52 | -7.6% |
| Arouca win | 26.8% | 27.0% | 3.49 | -6.5% |
| Over 2.5 | 48.9% | 48.9% | 1.96 | -4.2% |
| Under 2.5 | 51.1% | 51.1% | 1.88 | -3.9% |

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
| Market best home last update utc | 2026-11-04T19:40:37Z |
| Market best draw last update utc | 2026-11-04T19:40:37Z |
| Market best away last update utc | 2026-11-04T19:40:37Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
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
| P btts yes | 52.5% |
| P btts no | 47.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.24 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.81 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.79 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.16883408916739498, "-10": 4.7877479310206973e-08, "-11": 4.629086615931359e-09, "-12": 4.110602921047713e-10, "-13": 3.373832798985297e-11, "-14": 2.561165884690801e-12, "-15": 1.6512614425100548e-13, "-2": 0.07006019792530403, "-3": 0.022229689721246938, "-4": 0.005538046613101706, "-5": 0.0011311455963365377, "-6": 0.00019535915488264494, "-7": 2.919207201459193e-05, "-8": 3.841144259891319e-06, "-9": 4.512919914640687e-07, "0": 0.26251965701358615, "1": 0.22860263517650609, "10": 2.118162887955106e-06, "11": 3.013089538262101e-07, "12": 3.9365059321180624e-08, "13": 4.753544817381941e-09, "14": 5.309093800147515e-10, "15": 5.036016953616601e-11, "2": 0.14118553746031207, "3": 0.06590842077370819, "4": 0.02415754319746371, "5": 0.007259443345971313, "6": 0.0018446213556408617, "7": 0.0004055337833627609, "8": 7.850754357001413e-05, "9": 1.3570537539765169e-05} |
| Raw goal margin distribution | {"-1": 0.17011940003325715, "-10": 2.6457268333667556e-08, "-11": 2.377419771919352e-09, "-12": 1.961555720124916e-10, "-13": 1.4957016418991885e-11, "-14": 1.0559888364315661e-12, "-15": 6.407668435840213e-14, "-2": 0.06714352486626916, "-3": 0.020070178440087905, "-4": 0.004685604379260995, "-5": 0.0008941604513829336, "-6": 0.0001440176232966582, "-7": 2.00449510280914e-05, "-8": 2.45468652020373e-06, "-9": 2.682429919839353e-07, "0": 0.2503625011901234, "1": 0.24735990155446871, "10": 1.2572786309181312e-06, "11": 1.6621914943005403e-07, "12": 2.0177366747207908e-08, "13": 2.2635884133898e-09, "14": 2.351259006198221e-10, "15": 2.0990840537981436e-11, "2": 0.14533875757519452, "3": 0.0639171192989961, "4": 0.02195433211858271, "5": 0.006163944550650209, "6": 0.001460654694515136, "7": 0.00029910630794318445, "8": 5.388963765224035e-05, "9": 8.664156005785066e-06} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.0% |
| P home draw | 73.2% |
| P draw away | 53.1% |
| P home away | 73.7% |
| Raw p home draw | 73.7% |
| Raw p draw away | 51.3% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0779 |
| Totals anchor target over 2 5 | 0.4889 |
| Totals anchor reference over odds | 1.96 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-04T19:40:37Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4441 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.82, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.05, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.49, "draw": 3.52, "home": 2.09}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.96, "under": 1.88}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.09 |
| Reference draw odds | 3.52 |
| Reference away odds | 3.49 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:37Z |
| Market reference home last update utc | 2026-11-04T19:40:37Z |
| Market reference draw last update utc | 2026-11-04T19:40:37Z |
| Market reference away last update utc | 2026-11-04T19:40:37Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:37Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:37Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:37Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:37Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0244 |
| Raw ev home | 0.0169 |
| Raw edge prob draw | -0.0174 |
| Raw ev draw | -0.1187 |
| Raw edge prob away | -0.0071 |
| Raw ev away | -0.0819 |
| Elo home rating | 1,482.5254 |
| Elo away rating | 1,488.7246 |
| Elo rating diff | 53.8007 |
| Elo home expectancy | 0.5768 |

</details>


---

## 2026-11-07 — Alverca vs Casa Pia

The model's most likely 1X2 outcome is **Alverca win** at **53.6%**. Expected goals are 1.43 for Alverca and 0.91 for Casa Pia (2.33 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.0%; Double Chance 1X: 79.0%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alverca win | 53.6% | 1.87 |
| Draw | 25.4% | 3.93 |
| Casa Pia win | 21.0% | 4.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alverca expected goals | 1.43 |
| Casa Pia expected goals | 0.91 |
| Expected total goals | 2.33 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.35% |
| 2 | 1-1 | 12.07% |
| 3 | 2-1 | 9.89% |
| 4 | 2-0 | 9.56% |
| 5 | 0-0 | 6.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alverca win | 53.6% | 55.2% | 1.76 | -5.7% |
| Draw | 25.4% | 25.3% | 3.69 | -6.1% |
| Casa Pia win | 21.0% | 19.5% | 4.74 | -0.5% |
| Over 2.5 | 49.3% | 49.3% | 1.94 | -4.4% |
| Under 2.5 | 50.7% | 50.7% | 1.89 | -4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T18:00:00+00:00 |
| Fixture id | d9d924bf6388e1288f06e04041b3fe33 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:37Z |
| Market best draw last update utc | 2026-11-04T19:40:37Z |
| Market best away last update utc | 2026-11-04T19:40:37Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Alverca |
| Matched away-team name | Casa Pia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4251 |
| Dc lambda away | 0.9058 |
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
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.48 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.66 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.13485764424426203, "-10": 2.6838308834972314e-08, "-11": 2.4936602309915756e-09, "-12": 2.1279203728681152e-10, "-13": 1.6783259940143906e-11, "-14": 1.2244455707493016e-12, "-15": 7.595095302877215e-14, "-2": 0.053822613163378386, "-3": 0.01643143282932652, "-4": 0.003936789123613977, "-5": 0.0007730902170030745, "-6": 0.00012835089444788897, "-7": 1.8434684697912127e-05, "-8": 2.3313317070875057e-06, "-9": 2.63238894129295e-07, "0": 0.2544531400135949, "1": 0.25443203132532094, "10": 3.0315147348098516e-06, "11": 4.4315262821052744e-07, "12": 5.949533790525725e-08, "13": 7.3827029864083665e-09, "14": 8.474031479469292e-10, "15": 8.269806139094632e-11, "2": 0.16194860625491977, "3": 0.0777856318444025, "4": 0.029320921346461602, "5": 0.009058935158497958, "6": 0.0023662323406634317, "7": 0.0005346944952594174, "8": 0.0001063862699375747, "9": 1.8899185260989658e-05} |
| Raw goal margin distribution | {"-1": 0.164788140286806, "-10": 1.1191734673137573e-08, "-11": 9.12710085811773e-10, "-12": 6.832316505241625e-11, "-13": 4.7101037631173405e-12, "-14": 2.7901148192178813e-13, "-2": 0.06005731710203893, "-3": 0.01646509453131934, "-4": 0.0035109201858728365, "-5": 0.0006105203602677861, "-6": 8.947692046317116e-05, "-7": 1.1321595862808483e-05, "-8": 1.259589792446671e-06, "-9": 1.2499543568407686e-07, "0": 0.2569431462231614, "1": 0.25566419372645294, "10": 1.0399501772517312e-06, "11": 1.3343184467201767e-07, "12": 1.5714701278821898e-08, "13": 1.7044338106362112e-09, "14": 1.5884854987558713e-10, "2": 0.14865822840173593, "3": 0.06412077558063095, "4": 0.021511317372037354, "5": 0.005885152426867795, "6": 0.001357000804457929, "7": 0.00027013959072744685, "8": 4.7284764962834785e-05, "9": 7.382403343879381e-06} |
| Unadjusted home-win probability | 49.8% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 44.6% |
| P home draw | 79.0% |
| P draw away | 46.4% |
| P home away | 74.6% |
| Raw p home draw | 75.4% |
| Raw p draw away | 50.2% |
| Raw p home away | 74.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1426 |
| Totals anchor target over 2 5 | 0.4930 |
| Totals anchor reference over odds | 1.94 |
| Totals anchor reference under odds | 1.89 |
| Totals anchor reference last update utc | 2026-11-04T19:40:37Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4150 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.74, "draw": 3.69, "home": 1.76}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.94, "under": 1.89}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.76 |
| Reference draw odds | 3.69 |
| Reference away odds | 4.74 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:37Z |
| Market reference home last update utc | 2026-11-04T19:40:37Z |
| Market reference draw last update utc | 2026-11-04T19:40:37Z |
| Market reference away last update utc | 2026-11-04T19:40:37Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 1.89 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:37Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:37Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:37Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:37Z |
| Home probability edge | -1.6% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0544 |
| Raw ev home | -0.1244 |
| Raw edge prob draw | 0.0036 |
| Raw ev draw | -0.0519 |
| Raw edge prob away | 0.0508 |
| Raw ev away | 0.1638 |
| Elo home rating | 1,417.0742 |
| Elo away rating | 1,403.5352 |
| Elo rating diff | 73.5391 |
| Elo home expectancy | 0.6043 |

</details>


---

## 2026-11-07 — Nacional vs Académico de Viseu

The model's most likely 1X2 outcome is **Académico de Viseu win** at **44.2%**. Expected goals are 0.92 for Nacional and 1.60 for Académico de Viseu (2.51 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 49.0%; Under 3.5 goals: 72.0%; Double Chance 1X: 55.8%; Double Chance X2: 71.2%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 52.6%; BTTS No (at least one team does not score): 47.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nacional win | 28.8% | 3.47 |
| Draw | 26.9% | 3.71 |
| Académico de Viseu win | 44.2% | 2.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nacional expected goals | 0.92 |
| Académico de Viseu expected goals | 1.60 |
| Expected total goals | 2.51 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 0-1 | 9.62% |
| 3 | 1-0 | 9.26% |
| 4 | 0-2 | 7.89% |
| 5 | 1-2 | 7.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nacional win | 28.8% | 31.7% | 3.01 | -13.2% |
| Draw | 26.9% | 28.2% | 3.36 | -9.5% |
| Académico de Viseu win | 44.2% | 40.1% | 2.40 | +6.1% |
| Over 2.5 | 49.0% | 49.0% | 1.95 | -4.4% |
| Under 2.5 | 51.0% | 51.0% | 1.88 | -4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:30:00+00:00 |
| Fixture id | 406c4abcb4384570eada7fffa729be9d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:37Z |
| Market best draw last update utc | 2026-11-04T19:40:37Z |
| Market best away last update utc | 2026-11-04T19:40:37Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Nacional |
| Matched away-team name | Academico Viseu |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9186 |
| Dc lambda away | 1.5958 |
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
| P btts yes | 52.6% |
| P btts no | 47.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.89 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.66 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.20012582351978273, "-10": 3.9292569652269865e-06, "-11": 6.07449667849117e-07, "-12": 8.625007652571275e-08, "-13": 1.1321539545703234e-08, "-14": 1.3814070040499993e-09, "-15": 1.5674743116354806e-10, "-16": 1.5246075974388775e-11, "-2": 0.13458405046055094, "-3": 0.06827791502151202, "-4": 0.027197712229655047, "-5": 0.008882304525318898, "-6": 0.0024528660125644444, "-7": 0.000586055696845557, "-8": 0.00012330173685396007, "-9": 2.316334664621821e-05, "0": 0.2692773996619836, "1": 0.18939642006651633, "10": 2.5371670371679938e-08, "11": 2.257770218119912e-09, "12": 1.8452692412857697e-10, "13": 1.3942368393925219e-11, "14": 9.79227343276707e-13, "15": 6.395774200903221e-14, "16": 3.580812514512325e-15, "2": 0.07210837761697084, "3": 0.02105732464374754, "4": 0.004828209750196298, "5": 0.0009076328907701169, "6": 0.00014427437604535749, "7": 1.9841983469712598e-05, "8": 2.4029581000127908e-06, "9": 2.5984186392500536e-07} |
| Raw goal margin distribution | {"-1": 0.25585239455659303, "-10": 2.726665167714249e-06, "-11": 3.9126314428920764e-07, "-12": 5.155114679222778e-08, "-13": 6.277060944173735e-09, "-14": 7.077026726185548e-10, "-15": 6.858802239575006e-11, "-2": 0.16355133183534942, "-3": 0.07808455554861153, "-4": 0.029114479644570444, "-5": 0.008872969004386359, "-6": 0.002282271653228219, "-7": 0.0005072792576346711, "-8": 9.920263391520167e-05, "-9": 1.7311583103241047e-05, "0": 0.23889265276489918, "1": 0.1497888076336655, "10": 1.0887794971814976e-08, "11": 8.993067993063308e-10, "12": 6.820372263153281e-11, "13": 4.780319301347581e-12, "14": 3.102288686962925e-13, "15": 1.7306548619757918e-14, "2": 0.05418957061801816, "3": 0.014892156099040075, "4": 0.0031961877453876224, "5": 0.0005606902787301726, "6": 8.301416625985452e-05, "7": 1.0620935986955352e-05, "8": 1.1955553914841917e-06, "9": 1.200920051956881e-07} |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 53.8% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 75.4% |
| Raw p btts yes | 47.3% |
| P home draw | 55.8% |
| P draw away | 71.2% |
| P home away | 73.1% |
| Raw p home draw | 46.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0793 |
| Totals anchor target over 2 5 | 0.4902 |
| Totals anchor reference over odds | 1.95 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-04T19:40:37Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4447 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.4, "draw": 3.36, "home": 3.01}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:37Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.95, "under": 1.88}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.01 |
| Reference draw odds | 3.36 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:37Z |
| Market reference home last update utc | 2026-11-04T19:40:37Z |
| Market reference draw last update utc | 2026-11-04T19:40:37Z |
| Market reference away last update utc | 2026-11-04T19:40:37Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:37Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:37Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:37Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:37Z |
| Home probability edge | -2.8% |
| Draw probability edge | -1.3% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0939 |
| Raw ev home | -0.3296 |
| Raw edge prob draw | -0.0434 |
| Raw ev draw | -0.1973 |
| Raw edge prob away | 0.1373 |
| Raw ev away | 0.2921 |
| Elo home rating | 1,377.6402 |
| Elo away rating | 1,452.3265 |
| Elo rating diff | -14.6862 |
| Elo home expectancy | 0.4789 |

</details>


---
