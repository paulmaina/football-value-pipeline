# Primeira Liga — football model report

Fixtures in this report: **1**.

> Each match shows the two models the shortlists use, side by side, and the master's verdict on them: **Research** (the value shortlist's model, independent of bookmaker odds) and **Cagey** (the cagey tier's market view, built from Pinnacle's prices). Probabilities are model estimates, not guarantees. No probability here is blended or averaged. The production model (70% Pinnacle blend) is kept only as a benchmark at the end of this report.

## Quick reference

- **Research:** The value shortlist's model: team form, goal rates and xG, never bookmaker odds. Live research v5 (C6 grid) for domestic leagues and v6 (CE3n) for UCL/UEL, exactly as the forecast carries it.
- **Cagey:** The cagey tier's market view: Pinnacle's 1X2, O/U 2.5 and main AH line with the margin removed, plus the narrow-margin correction (D_pow2 for domestic leagues, D for UCL/UEL, D where D_pow2's power fit fails). Blank without Pinnacle 1X2 and O/U 2.5.
- **No-loss:** The chance a bet does not lose: a win, a half win or a refund (push) on that exact line.
- **Gap:** Research minus cagey no-loss on the same Pinnacle offer, in percentage points (the master's g). +4 or more: research too optimistic; -4 or less: research too pessimistic; -8 or less with cagey no-loss of 85% or more: flagged for inspection.
- **Cagey tier:** The master's market classes from the cagey no-loss: safe (75% or more), risky (below 50%), in between otherwise; fair price when the Pinnacle price is within its 2.70% margin of the cagey fair odds.
- **Best offer:** The fixture's master pick, or else the Pinnacle offer the master's own rule would choose for it (safe first, then chance of profit), shown with both views and the master's labels.
- **Expected goals:** A view's average goal expectation for each team, from its score grid. It is not a prediction that the team will score exactly that many goals.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-27 — CS Marítimo vs CD Nacional

Research leans **CD Nacional win** at **38.6%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote). Only one view is available.

**Fixture source:** football-data.org

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| CS Marítimo win | 33.1% | — |
| Draw | 28.3% | — |
| CD Nacional win | 38.6% | — |
| CS Marítimo expected goals | 1.21 | — |
| CD Nacional expected goals | 1.32 | — |
| Expected total goals | 2.53 | — |
| Most likely score | 1-1 | — |
| Most likely score probability | 13.4% | — |
| Over 1.5 | 72.2% | — |
| Under 1.5 | 27.8% | — |
| Over 2.5 | 46.2% | — |
| Under 2.5 | 53.8% | — |
| Over 3.5 | 25.0% | — |
| Under 3.5 | 75.0% | — |
| BTTS Yes | 52.1% | — |
| BTTS No | 47.9% | — |
| Double Chance 1X | 61.4% | — |
| Double Chance X2 | 66.9% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 1-1 (13.45%) | — |
| 2 | 0-1 (10.17%) | — |
| 3 | 1-0 (9.18%) | — |
| 4 | 0-0 (8.46%) | — |
| 5 | 1-2 (8.33%) | — |

### No-loss on the quoted Pinnacle Asian handicap lines

_No Pinnacle Asian handicap quotes in this forecast._

### On the lists

- **Value shortlist:** no
- **Cagey tier:** no
- **Master shortlist:** no

### The master's verdict on every Pinnacle offer

_No Pinnacle offer of this match in the run's decision rows._

### Safest Asian handicap (cagey tier)

_no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)._


---

## Benchmark (70% Pinnacle blend), display only

The production forecasting model blends 70% of Pinnacle's prices into its score grid, so it is neither independent research nor the cagey tier's market view. It is shown for comparison only: no list, probability or stake reads it, and its EV is not a recommendation.

- **Benchmark EV:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Probability edge:** Model probability minus the de-vigged market probability.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,628 |
| Training data through | 2026-11-08 |
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
| Training sha256 | 7c73b44b6e1c6ee16fc6ee45d20634ecf277c8dff8e4ce224e38cad97bc36515 |
| Training as of utc | 2026-11-24T15:49:50.493998+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1628, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1323, 'tuning_matches': 207, 'audit_matches': 92, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8715376387746687, 'audit_candidate_poisson_score': 0.8661166852387249, 'audit_gain': 0.005420953535943851, 'audit_gain_lower95': -0.003731446012881781, 'audit_baseline_briers': [0.5256825537437794, 0.20162598269824156, 0.221887119731087, 0.2543680014638883], 'audit_candidate_briers': [0.5292164683524547, 0.20093844348497894, 0.21876001119885946, 0.2532888353919278], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1448.818 |
| Base scoring parameter | 0.083 |
| Home-advantage parameter | 0.174 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1628, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-08'} |
| Training data health | {'training_end': '2026-11-08', 'days_since_latest_result': 16, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
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

### 2026-11-27 — CS Marítimo vs CD Nacional

The model's most likely 1X2 outcome is **CD Nacional win** at **41.0%**. Expected goals are 1.21 for CS Marítimo and 1.36 for CD Nacional (2.57 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.3%; Double Chance 1X: 59.0%; Double Chance X2: 66.2%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| CS Marítimo win | 33.8% | 2.96 |
| Draw | 25.2% | 3.97 |
| CD Nacional win | 41.0% | 2.44 |

| Measure | Benchmark estimate |
| --- | --- |
| CS Marítimo expected goals | 1.21 |
| CD Nacional expected goals | 1.36 |
| Expected total goals | 2.57 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 72.0% |
| Under 1.5 | 28.0% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.7% |
| Under 3.5 | 74.3% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 1-1 | 11.96% |
| 2 | 0-1 | 11.05% |
| 3 | 1-0 | 9.88% |
| 4 | 1-2 | 8.57% |
| 5 | 2-1 | 7.61% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T20:15:00+00:00 |
| Fixture id | fdorg:567361 |
| Matched home-team name | Maritimo |
| Matched away-team name | Nacional |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2090 |
| Dc lambda away | 1.3610 |
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
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.24 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.58 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.88 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.45 |
| Fair Under 4.5 odds | 1.13 |
| Score matrix json | [[0.07023918752892773,0.11046253311836686,0.07088502237831537,0.032158271959385414,0.010941886107065913,0.002978390673011528,0.0006756003881385662,0.00013135642736450412,2.234708179389605e-05,3.3793858924165956e-06,4.5993585219190825e-07,5.690678582815852e-08,6.4541980576289235e-09,6.757069930987995e-10,6.568857723958644e-11],[0.09882800645957703,0.11963863443190496,0.08569930974113245,0.038879041254701256,0.013228634980702125,0.003600845654731681,0.0008167943661682212,0.00015880865629299586,2.7017406783684417e-05,4.085645015153707e-06,5.560580181195509e-07,6.879975630157297e-08,7.803063325836843e-09,8.169232505390015e-10,7.941685758755925e-11],[0.05593468696227034,0.07612734601517357,0.05180482028283379,0.023502193320490382,0.007996646178744663,0.002176693868049499,0.000493748263261294,9.599906841102939e-05,1.6331892370717837e-05,2.4697527481706955e-06,3.3613439574398397e-07,4.158912156319372e-08,4.716914225699192e-09,4.938261732431329e-10,4.8007108192334274e-11],[0.022541499376598446,0.030679076185777893,0.02087717635566605,0.009471308500213459,0.0032226227524012,0.0008772006447945248,0.00019897896587869407,3.86873165519083e-05,6.581700223718679e-06,9.953024331895243e-07,1.3546108298107057e-07,1.676028254922331e-08,1.900901298505291e-09,1.9901036335139713e-10,1.9346710568340926e-11],[0.006813113942444115,0.00927267695065678,0.0063100763144140525,0.0028626802023198577,0.0009740299719554619,0.00026513178398305837,6.0140913611480214e-05,1.1693148330194632e-05,1.9893030543371073e-06,3.008277653238958e-07,4.0942786355863975e-08,5.065755068359059e-09,5.745428431216834e-10,6.015040342204947e-11,5.847496713126146e-12],[0.0016473978351561108,0.0022421154355645426,0.0015257643051110367,0.0006921905618907346,0.00023551857208496365,6.41083549540755e-05,1.4541957132206857e-05,2.8273807554158538e-06,4.810096488726484e-07,7.2739574522902e-08,9.899886920680648e-09,1.2248898232945207e-09,1.389233533974266e-10,1.4544251750133389e-11,1.4139134480452736e-12],[0.0003319480209054327,0.0004517826632973837,0.00030743905973493456,0.0001394752877572376,4.745661443865421e-05,1.2917730675839912e-05,2.9301810328470386e-06,5.697126863211288e-07,9.692267257627061e-08,1.4656907572112025e-08,1.9948113323798975e-09,2.4681333433419934e-10,2.799283283837252e-11,2.9306433946780375e-12,2.8490129147567364e-13],[5.733170886571042e-05,7.802869874654213e-05,5.309869484563796e-05,2.408918290836016e-05,8.196370007954652e-06,2.2310588636523175e-06,5.060800948316896e-07,9.839673627266442e-08,1.6739796885887623e-08,2.531437167493595e-09,3.44529671356605e-10,4.262784935312136e-11,4.834723636063726e-12,5.061599506892819e-13,4.920613129066227e-14],[8.664185520476713e-06,1.179199321347584e-05,8.024476369880957e-06,3.6404487827774946e-06,1.2386665555309071e-06,3.371660863461358e-07,7.648074541285301e-08,1.4870088377666931e-08,2.529781662956393e-09,3.8256039609718345e-10,5.206663204361313e-11,6.442082443408084e-12,7.306417923318393e-13,7.649281353324859e-14,7.436217386190924e-15],[1.1638796550954602e-06,1.5840451432800265e-06,1.07794607671153e-06,4.890297263000703e-07,1.663928825187797e-07,4.5292283661169256e-08,1.0273831669714455e-08,1.997532634929746e-09,3.398312977474777e-10,5.1390204054434214e-11,6.994228551741404e-12,8.653795183182762e-13,9.814876600319162e-14,1.0275452807647208e-14,9.989239157218043e-16],[1.4071192999149153e-07,1.9150953307651016e-07,1.303226430815093e-07,5.91232231868937e-08,2.011673933259419e-08,5.4757934978788716e-09,1.242096359640085e-09,2.4149977280847e-10,4.108527678803594e-11,6.213026203781279e-12,8.455954995075561e-13,1.0462355078084475e-13,1.1866091335241739e-14,1.2422923536557048e-15,1.2076893988179946e-16],[1.54653971742047e-08,2.1048471098746296e-08,1.4323529185972595e-08,6.498127975785341e-09,2.210994928769202e-09,6.018346937160556e-10,1.3651659480208441e-10,2.6542809157610356e-11,4.51560946948514e-12,6.82862625088213e-13,9.293789268184389e-14,1.1498987802236647e-14,1.3041809277720734e-15,1.365381361546585e-16,1.3273498712530031e-17],[1.5581263599290939e-09,2.1206165794347814e-09,1.4430840760496215e-09,6.546811811695029e-10,2.2275596555198078e-10,6.063436263783257e-11,1.3753937421256389e-11,2.674166731651805e-12,4.549440319118118e-13,6.879786172805082e-14,9.363418138744887e-15,1.1585137973082418e-15,1.3139518234086014e-16,1.3756107695249103e-17,1.3372943481188987e-18],[1.4490459778299262e-10,1.972157717098929e-10,1.3420575056347032e-10,6.088486510027238e-11,2.0716139860146408e-11,5.638950829548305e-12,1.2791059962879417e-12,2.486955259984811e-13,4.2309458111570644e-14,6.398150200402754e-15,8.707909539060422e-16,1.0774092534615594e-16,1.2219654668182211e-17,1.2793078301623187e-18,1.2436738419627066e-19],[1.2513447422788018e-11,1.7030854976266047e-11,1.1589532900997411e-11,5.257801132140619e-12,1.7889724060466699e-12,4.86959805312137e-13,1.1045905980631807e-13,2.147646407690359e-14,3.653694828639393e-15,5.525215718533772e-16,7.519842009610555e-17,9.304124404808157e-18,1.0552460622672613e-18,1.1047648946427092e-19,1.073992645547627e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.22316691951564993, "-10": 5.33657380579245e-07, "-11": 6.522302203780683e-08, "-12": 7.31912841636026e-09, "-13": 7.551238506863588e-10, "-14": 6.568857723958644e-11, "-2": 0.11870097825797647, "-3": 0.04777476893997353, "-4": 0.015077231422419875, "-5": 0.0038980767871922913, "-6": 0.0008517784354180775, "-7": 0.00016098425563761156, "-8": 2.678621085933912e-05, "-9": 3.978995497714715e-06, "0": 0.25219512023058765, "1": 0.19894416663181894, "10": 1.6326615900379378e-07, "11": 1.7725477305335093e-08, "12": 1.7669316645399843e-09, "13": 1.6193545275925866e-10, "14": 1.2513447422788018e-11, "2": 0.09366579621771097, "3": 0.033487959976134525, "4": 0.009388042848591729, "5": 0.00215609164999155, "6": 0.0004185109583284688, "7": 7.026304430895855e-05, "8": 1.0385279940189476e-05, "9": 1.3703886016387777e-06} |
| Raw goal margin distribution | {"-1": 0.22316691951564993, "-10": 5.33657380579245e-07, "-11": 6.522302203780683e-08, "-12": 7.31912841636026e-09, "-13": 7.551238506863588e-10, "-14": 6.568857723958644e-11, "-2": 0.11870097825797647, "-3": 0.04777476893997353, "-4": 0.015077231422419875, "-5": 0.0038980767871922913, "-6": 0.0008517784354180775, "-7": 0.00016098425563761156, "-8": 2.678621085933912e-05, "-9": 3.978995497714715e-06, "0": 0.25219512023058765, "1": 0.19894416663181894, "10": 1.6326615900379378e-07, "11": 1.7725477305335093e-08, "12": 1.7669316645399843e-09, "13": 1.6193545275925866e-10, "14": 1.2513447422788018e-11, "2": 0.09366579621771097, "3": 0.033487959976134525, "4": 0.009388042848591729, "5": 0.00215609164999155, "6": 0.0004185109583284688, "7": 7.026304430895855e-05, "8": 1.0385279940189476e-05, "9": 1.3703886016387777e-06} |
| Research history json | {"away": [{"away": "Academico Viseu", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-11-08T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 1.67, "date": "2026-10-25T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.08, "date": "2026-09-05T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 3.0, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-08-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}], "h2h": [], "home": [{"away": "Santa Clara", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-11-01T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 2.06, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 0.0, "away_xg": 0.52, "date": "2026-10-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 5.0, "home_xg": 1.78, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 2.13, "date": "2026-10-10T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 0.19, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-09-14T00:00:00+00:00", "home": "Moreirense", "home_goals": 3.0, "home_xg": 1.99, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": 1.31, "date": "2026-09-05T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 0.13, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.84, "date": "2026-08-22T00:00:00+00:00", "home": "Maritimo", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-08T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}], "teams": {"away": "Nacional", "home": "Maritimo"}} |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 41.0% |
| Raw p over 1 5 | 72.0% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.5% |
| P home draw | 59.0% |
| P draw away | 66.2% |
| P home away | 74.8% |
| Raw p home draw | 59.0% |
| Raw p draw away | 66.2% |
| Raw p home away | 74.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4740 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-08 |
| Elo home rating | 1,397.7708 |
| Elo away rating | 1,372.3069 |
| Elo rating diff | 85.4639 |
| Elo home expectancy | 0.6206 |
| Research p home | 0.3314 |
| Research p draw | 0.2826 |
| Research p away | 0.3860 |
| Research p over 1 5 | 0.7219 |
| Research v4 p home | 0.3422 |
| Research v4 p draw | 0.2674 |
| Research v4 p away | 0.3904 |
| Research v4 p over 1 5 | 0.7201 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.2089903743523251, 1.3610042381487502], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:50:27.223173+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 4.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-08", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:50:26.894746+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:50:26.947464+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:50:27.131448+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22CS+Mar%C3%ADtimo%22+%22CD+Nacional%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T15:50:01.200490+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T15:50:01.389360+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T15:50:27.222665+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=CS+Mar%C3%ADtimo_vs_CD+Nacional&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 1.5507048527234875, "goals_for": 0.8473887254235924, "last_match": "2026-11-08T00:00:00+00:00", "matches": 10, "points_per_game": 1.0589134132875462, "results": "WLWLLLLLLW", "xg_against": 1.4473966787066475, "xg_for": 0.943443703024997, "xg_matches": 10}, "venue": {"goals_against": 1.7599865214626136, "goals_for": 0.5295057548750894, "last_match": "2026-11-01T00:00:00+00:00", "matches": 4, "points_per_game": 0.0, "results": "LLLL", "xg_against": 1.9738427187746768, "xg_for": 0.5203791930565782, "xg_matches": 4}}, "home": {"all": {"goals_against": 2.3662591888570916, "goals_for": 0.7131841570421359, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.49878383320263503, "results": "LLLDLLLDWW", "xg_against": 1.4454419451949967, "xg_for": 0.932195130990825, "xg_matches": 10}, "venue": {"goals_against": 1.8988119457434338, "goals_for": 0.7157020266306037, "last_match": "2026-11-01T00:00:00+00:00", "matches": 5, "points_per_game": 0.6169046207669643, "results": "LLLDW", "xg_against": 1.3603430415604811, "xg_for": 1.0106319966707003, "xg_matches": 5}}}, "goal_rates": [1.217234345693549, 1.3190484130517532], "h2h": [], "margin_distribution": {"-1": 0.21054968194047746, "-10": 3.99685145933116e-07, "-11": 4.735707693746992e-08, "-12": 5.151805998374461e-09, "-13": 5.153760519377678e-10, "-14": 4.3561692859914796e-11, "-2": 0.11327383371987867, "-3": 0.044297909013864434, "-4": 0.013571703448351367, "-5": 0.0034046630441421357, "-6": 0.0007216512402511817, "-7": 0.00013227357937544608, "-8": 2.134171426156946e-05, "-9": 3.0738048424277462e-06, "0": 0.28264656102992136, "1": 0.19029632072994784, "10": 1.7545831256872042e-07, "11": 1.9184668113342977e-08, "12": 1.925938278429753e-09, "13": 1.77795416571276e-10, "14": 1.3868022499992662e-11, "2": 0.09455355054813246, "3": 0.034122821256727914, "4": 0.009647383172868338, "5": 0.002233380734951207, "6": 0.00043684709645500417, "7": 7.389050917155263e-05, "8": 1.1001662466091215e-05, "9": 1.4622403645796103e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:50:27.223173+00:00", "p_over_1_5": 0.72188240231137, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.21392774332199294, "-10": 4.021254884927521e-07, "-11": 4.7646223260585494e-08, "-12": 5.183261186451244e-09, "-13": 5.185227641099821e-10, "-14": 4.382766584924785e-11, "-2": 0.11396544550513635, "-3": 0.0445683770904727, "-4": 0.013654567687537568, "-5": 0.0034254507672096097, "-6": 0.0007260573990807469, "-7": 0.00013308119719299523, "-8": 2.1472019563475325e-05, "-9": 3.092572457019677e-06, "0": 0.26735212621742876, "1": 0.19741519271895494, "10": 1.8009274752601612e-07, "11": 1.969139871645287e-08, "12": 1.976808684923905e-09, "13": 1.8249158218316258e-10, "14": 1.4234322889649932e-11, "2": 0.0970510228740735, "3": 0.03502411794286693, "4": 0.009902202503843358, "5": 0.0022923717146288145, "6": 0.0004483856746230307, "7": 7.584220216177732e-05, "8": 1.129225279706372e-05, "9": 1.5008629739183522e-06}, "p_over_1_5": 0.7200674650464436, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
