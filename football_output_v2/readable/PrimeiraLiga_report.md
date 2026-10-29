# Primeira Liga — football model report

Fixtures in this report: **3**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,611 |
| Training data through | 2026-10-26 |
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
| Training sha256 | 84c0a9d8af08458f9d90e4a3ffe4465c5e09f0dc593fdcb0fb4ebd37c58b23a7 |
| Training as of utc | 2026-10-29T12:07:44.956402+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-29', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1611, 'tune_start_date': '2025-10-30', 'audit_start_date': '2026-04-30', 'training_shot_matches': 1305, 'tuning_matches': 198, 'audit_matches': 102, 'audit_matchdays': 41, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.883738573006896, 'audit_candidate_poisson_score': 0.8736508102296558, 'audit_gain': 0.010087762777240106, 'audit_gain_lower95': 0.00023527464656370386, 'audit_baseline_briers': [0.595476367672287, 0.18598397156743018, 0.24306305301985578, 0.24914845801147523], 'audit_candidate_briers': [0.5923603451480663, 0.18512676084672974, 0.2410781373860159, 0.24810745496845585], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1462.838 |
| Base scoring parameter | 0.094 |
| Home-advantage parameter | 0.170 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 3.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 7.00 |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'ANCHORED_MAIN': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
| Shot features applied fixtures | 3 |
| Goal rate features used | {'shot_features': 3} |
| Legacy comparison status | {'AVAILABLE': 3} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Casa Pia vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **75.9%**. Expected goals are 0.73 for Casa Pia and 2.38 for Sporting Lisbon (3.11 combined). The most likely exact score is 0-2 at 13.0%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 60.1%; Under 3.5 goals: 62.3%; Double Chance 1X: 24.1%; Double Chance X2: 91.2%; Double Chance 12 (either team wins): 84.7%; Under 4.5 goals: 79.7%; BTTS Yes (both teams score): 46.2%; BTTS No (at least one team does not score): 53.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Casa Pia win | 8.8% | 11.39 |
| Draw | 15.3% | 6.55 |
| Sporting Lisbon win | 75.9% | 1.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Casa Pia expected goals | 0.73 |
| Sporting Lisbon expected goals | 2.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 60.1% |
| Under 2.5 | 39.9% |
| Over 3.5 | 37.7% |
| Under 3.5 | 62.3% |
| Over 4.5 | 20.3% |
| Under 4.5 | 79.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.97% |
| 2 | 0-1 | 11.37% |
| 3 | 0-3 | 10.23% |
| 4 | 1-2 | 9.43% |
| 5 | 1-3 | 7.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Casa Pia win | 8.8% | 8.2% | 10.08 | -11.5% |
| Draw | 15.3% | 15.2% | 5.74 | -12.3% |
| Sporting Lisbon win | 75.9% | 76.6% | 1.28 | -2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:15:00+00:00 |
| Fixture id | 75daf3f21fd7945dcc4215b1fe8a5da3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:07:30Z |
| Market best draw last update utc | 2026-10-29T12:07:30Z |
| Market best away last update utc | 2026-10-29T12:07:30Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Casa Pia |
| Matched away-team name | Sp Lisbon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6959 |
| Dc lambda away | 2.5772 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 0.8099 |
| Shot lambda away | 1.9041 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 46.2% |
| P btts no | 53.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.68 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.36 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.51 |
| Fair Over 3.5 odds | 2.65 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.93 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.2392964675117225, "-10": 8.19064856541098e-05, "-11": 1.739001451990478e-05, "-12": 3.3910717152633273e-06, "-13": 6.113330410905441e-07, "-14": 1.0246338155733719e-07, "-15": 1.604465649203203e-08, "-16": 2.357043430833372e-09, "-17": 3.2488543016998165e-10, "-18": 3.897246200458999e-11, "-2": 0.22209912456920627, "-3": 0.15463555617570676, "-4": 0.08455814994785858, "-5": 0.03791494528206352, "-6": 0.014376799149743056, "-7": 0.004716919608927427, "-8": 0.0013628216934147253, "-9": 0.00035158884810084905, "0": 0.1527666991860114, "1": 0.06527993268363388, "10": 5.275635379965299e-10, "11": 3.442998001137067e-11, "12": 2.0637360298555114e-12, "13": 1.1436032658840315e-13, "14": 5.891780362224355e-15, "15": 2.8358851171706735e-16, "16": 1.280578307619796e-17, "17": 5.425617051058111e-19, "18": 2.0005853776637164e-20, "2": 0.017949839049442997, "3": 0.0038415228317197157, "4": 0.0006456986471109677, "5": 8.899491314848546e-05, "6": 1.037283098334425e-05, "7": 1.0461017209434252e-06, "8": 9.290408834897347e-08, "9": 7.3673486946430785e-09} |
| Raw goal margin distribution | {"-1": 0.2334842603158997, "-10": 8.255320254905098e-05, "-11": 1.7597299029707647e-05, "-12": 3.445245654133987e-06, "-13": 6.235963421671633e-07, "-14": 1.0494001723418433e-07, "-15": 1.6498827501417302e-08, "-16": 2.4335598899717623e-09, "-17": 3.3677012976487197e-10, "-18": 4.0534574794640424e-11, "-2": 0.21727698020840688, "-3": 0.15176253447786875, "-4": 0.08327813629194229, "-5": 0.037478479373629435, "-6": 0.014265159976855084, "-7": 0.004698364602271684, "-8": 0.0013627695327950965, "-9": 0.0003529627889730303, "0": 0.15567919955193454, "1": 0.07446019694214509, "10": 6.216377584506915e-10, "11": 4.073144522861668e-11, "12": 2.4512315931475825e-12, "13": 1.3637917438551577e-13, "14": 7.054495732378326e-15, "15": 3.40924546763124e-16, "16": 1.5457084267652912e-17, "17": 6.575055849289035e-19, "18": 2.4326064252474106e-20, "2": 0.0205293126414999, "3": 0.004407634855095311, "4": 0.0007434510537742355, "5": 0.00010284512059528004, "6": 1.2032579018067374e-05, "7": 1.2181734722756698e-06, "8": 1.086088420678484e-07, "9": 8.646732753099515e-09} |
| Unadjusted home-win probability | 10.0% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 74.4% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 62.4% |
| Raw p btts yes | 46.6% |
| P home draw | 24.1% |
| P draw away | 91.2% |
| P home away | 84.7% |
| Raw p home draw | 25.6% |
| Raw p draw away | 90.0% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9959 |
| Totals anchor target over 2 5 | 0.6009 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.36 |
| Totals anchor reference last update utc | 2026-10-29T12:07:30Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6033 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.82, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.08 |
| Reference draw odds | 5.74 |
| Reference away odds | 1.28 |
| Market reference 1x2 last update utc | 2026-10-29T12:07:30Z |
| Market reference home last update utc | 2026-10-29T12:07:30Z |
| Market reference draw last update utc | 2026-10-29T12:07:30Z |
| Market reference away last update utc | 2026-10-29T12:07:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.32 |
| Market reference over 2 5 last update utc | 2026-10-29T12:07:06Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:07:06Z |
| Home probability edge | +0.5% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.0178 |
| Raw ev home | 0.0106 |
| Raw edge prob draw | 0.0042 |
| Raw ev draw | -0.1064 |
| Raw edge prob away | -0.0219 |
| Raw ev away | -0.0476 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03806785521173214, 0.10483905327844284, 0.12651675124422074, 0.10537399101369375, 0.06582336650851928, 0.032894003818849826, 0.013698472450185604, 0.0048896835467180004, 0.0015272052861909217, 0.0004239958069333767, 0.00010594201141807059, 2.4064795838610716e-05, 5.010805991115705e-06, 9.630989030546847e-07, 1.71889562038898e-07, 2.8632871121818304e-08, 4.471482839151739e-09, 6.572177730154899e-10, 9.123121250309235e-11], [0.03122964624140294, 0.06989216239544752, 0.08923337599596236, 0.07432120148397832, 0.0464257986014563, 0.023200429839634613, 0.009661652948692681, 0.0034487367572639065, 0.0010771513035663803, 0.00029904796707721143, 7.472183126476753e-05, 1.697311189399445e-05, 3.534165481256565e-06, 6.792821163395414e-07, 1.212352180114879e-07, 2.019501551794595e-08, 3.1537761246754026e-09, 4.635414684140427e-10, 6.434617556801875e-11], [0.009790159371144459, 0.024462250779887854, 0.03241386551869083, 0.02620969812799575, 0.016372261782630196, 0.008181733481093592, 0.0034072243471102203, 0.001216212164577233, 0.00037986213813749994, 0.00010546057903240679, 2.6350981979789157e-05, 5.985642456684299e-06, 1.2463389793030437e-06, 2.3955182178861164e-07, 4.2754132106540885e-08, 7.121860920529619e-09, 1.1121930020041697e-09, 1.634699347474758e-10, 2.2691961427619686e-11], [0.002301695134265561, 0.005751146785128367, 0.007185071743796848, 0.006347084230342823, 0.003849166683953248, 0.0019235494979576958, 0.00080104842054047, 0.00028593504102627934, 8.930670093275391e-05, 2.479409092472655e-05, 6.195193020530988e-06, 1.4072420678472657e-06, 2.930179433812399e-07, 5.631933472303048e-08, 1.005162164462993e-08, 1.6743703556056444e-09, 2.614798313316888e-10, 3.84322603078309e-11, 5.334946574908353e-12], [0.0004058514491640845, 0.0010140835866364623, 0.0012669235539303273, 0.0010552024919545152, 0.0006991014845069357, 0.00033917408941913613, 0.00014124662188621595, 5.041812403376195e-05, 1.5747200163060267e-05, 4.371872531119209e-06, 1.0923810142371488e-06, 2.481350479731173e-07, 5.166703234583765e-08, 9.930630374553275e-09, 1.7723742602531223e-09, 2.952370299365332e-10, 4.6106005479743226e-11, 6.7766526975613275e-12, 9.406961705770855e-13], [5.725011843191681e-05, 0.0001430484123054798, 0.00017871446228930895, 0.00014884871732865484, 9.298047441112656e-05, 4.928175449667514e-05, 1.9924496629861077e-05, 7.11206915237837e-06, 2.221327720187133e-06, 6.167040198854311e-07, 1.5409318499826238e-07, 3.500236579869148e-08, 7.288242353001909e-09, 1.4008321670841455e-09, 2.5001422691520007e-10, 4.164665412472217e-11, 6.503794133480434e-12, 9.55926534958612e-13, 1.3269625446677991e-13], [6.729835237373967e-06, 1.6815550293204617e-05, 2.1008146684853313e-05, 1.7497384640480283e-05, 1.0929990892925344e-05, 5.4620597706036085e-06, 2.412512684032587e-06, 8.360341411212314e-07, 2.611203255910965e-07, 7.249446040868551e-08, 1.8113879493083366e-08, 4.114579344034388e-09, 8.567435587767987e-10, 1.6466987209644064e-10, 2.9389538401386154e-11, 4.89562516417483e-12, 7.645305221189085e-13, 1.1237056368635831e-13, 1.559863898342994e-14], [6.780874155529775e-07, 1.6943079046121699e-06, 2.1167471993933513e-06, 1.7630084409658384e-06, 1.1012883696530656e-06, 5.503483908306978e-07, 2.2918864822038256e-07, 8.67679767219578e-08, 2.631006562316817e-08, 7.304425675600176e-09, 1.8251254745273402e-09, 4.14578422067379e-10, 8.63241082539949e-11, 1.65918724680228e-11, 2.9612427995588264e-12, 4.932753474640471e-13, 7.703287042986658e-14, 1.1322277949860575e-14, 1.571693870851027e-15], [5.978262632725211e-08, 1.4937628102438257e-07, 1.866200491973346e-07, 1.554331674952277e-07, 9.70935451262244e-08, 4.852069430016667e-08, 2.020609585245531e-08, 7.212586278685322e-09, 2.389271165017594e-09, 6.439844490307823e-10, 1.609096286723405e-10, 3.6550725350925724e-11, 7.61064397954255e-12, 1.4627991746703248e-12, 2.6107381982000543e-13, 4.348892944700968e-14, 6.7914950229076255e-15, 9.982127618425296e-16, 1.385661866402511e-16], [4.6850234987532174e-09, 1.170626701685363e-08, 1.4624973333254725e-08, 1.2180930931581214e-08, 7.608992251420313e-09, 3.802452433717809e-09, 1.5835040998133475e-09, 5.652333843189148e-10, 1.765405479139519e-10, 5.1983601910359674e-11, 1.2610108284284557e-11, 2.864394184159507e-12, 5.964282279874953e-13, 1.1463612303970005e-13, 2.0459739825923605e-14, 3.4081248836333333e-15, 5.32233455248574e-16, 7.822758104315224e-17, 1.0859105402772628e-17], [3.3043882276676857e-10, 8.256532956711903e-10, 1.0315122160053513e-09, 8.591317585293145e-10, 5.366689073533786e-10, 2.681903102852573e-10, 1.1168593513520738e-10, 3.986640710607393e-11, 1.2451559920416824e-11, 3.4569086708729634e-12, 9.161198924523995e-13, 2.0202823793851436e-13, 4.206660683206941e-14, 8.085386456197207e-15, 1.4430434220856582e-15, 2.4037804179416126e-16, 3.753889312107638e-17, 5.517460007334068e-18, 7.659022428697224e-19], [2.1187400393178566e-11, 5.294004746433876e-11, 6.613951153792266e-11, 5.508665236743119e-11, 3.4410663140182326e-11, 1.7196089242804287e-11, 7.161188283455491e-12, 2.5561933749837627e-12, 7.983813262152113e-13, 2.2165345923693954e-13, 5.538359796332732e-14, 1.334298163750541e-14, 2.6972679380429912e-15, 5.18426735535088e-16, 9.252647286560362e-17, 1.541279494515042e-17, 2.406955551449714e-18, 3.5377390994776664e-19, 4.9108870882184545e-20], [1.245304967569047e-12, 3.1115900425380975e-12, 3.887398205646928e-12, 3.237758317060805e-12, 2.0225119151290776e-12, 1.0107127330127455e-12, 4.2090408344553433e-13, 1.5024213678235081e-13, 4.692544687408963e-14, 1.3027844319942745e-14, 3.2552115118277406e-15, 7.394233826135199e-16, 1.6329629886385059e-16, 3.0470910876367114e-17, 5.438311173289381e-18, 9.058983052729037e-19, 1.4147057446005767e-19, 2.0793320524405573e-20, 2.886409834449572e-21], [6.756342558344689e-14, 1.688178299775077e-13, 2.1090893092088195e-13, 1.7566302938544646e-13, 1.0973041690840404e-13, 5.48357360658827e-14, 2.283594979561866e-14, 8.151315294122589e-15, 2.5459176831491735e-15, 7.068194644251904e-16, 1.7660994412242945e-16, 4.0117062074675435e-17, 8.353231680745033e-18, 1.7028468179082554e-18, 2.9505297242443736e-19, 4.914907940498751e-20, 7.675418374374729e-21, 1.1281316629017147e-21, 1.56600785455672e-22], [3.403791253711444e-15, 8.504907029000154e-15, 1.062542297402417e-14, 8.849762691267835e-15, 5.528130495361439e-15, 2.7625804523684483e-15, 1.1504568561065393e-15, 4.10656734243156e-16, 1.282612932624243e-16, 3.560899836246477e-17, 8.897467497113897e-18, 2.02106544828352e-18, 4.208291200396346e-19, 8.08852038179583e-20, 1.5311066967153638e-20, 2.476091245551835e-21, 3.8668142868223064e-22, 5.683436939527513e-23, 7.889422113448216e-24], [1.600482580460271e-16, 3.999057090679868e-16, 4.996136105998033e-16, 4.1612102425897237e-16, 2.5993593322416044e-16, 1.2989815066698524e-16, 5.4095155093952764e-17, 1.9309320129083108e-17, 6.030921120382519e-18, 1.6743559560128839e-18, 4.1836413216629804e-19, 9.503168093580519e-20, 1.9787631666291306e-20, 3.803269650759713e-21, 6.787904674290758e-22, 1.199247669376629e-22, 1.8181987221413374e-23, 2.6723853317796185e-24, 3.709652479041938e-25], [7.055215143087777e-18, 1.7628563090092007e-17, 2.2023866765127778e-17, 1.8343363355225056e-17, 1.1458443563867785e-17, 5.726144169474521e-18, 2.3846117542671447e-18, 8.511895689502533e-19, 2.6585385267394885e-19, 7.380862272417929e-20, 1.844224358715356e-20, 4.1891674585959145e-21, 8.72274401997636e-22, 1.6765496832567467e-22, 2.992230495512177e-23, 4.984371891376772e-24, 8.255718251152381e-25, 1.1780355307281794e-25, 1.6352815497812577e-26], [2.927120714447077e-19, 7.313870823273276e-19, 9.137427465070005e-19, 7.61043253263704e-19, 4.75396523435301e-19, 2.375705754175425e-19, 9.893456571154915e-20, 3.531479293918631e-20, 1.1029944564339636e-20, 3.0622276443606752e-21, 7.651456706848201e-22, 1.7380332981563852e-22, 3.618957634864929e-23, 6.955795404011896e-24, 1.241439089833432e-24, 2.067953693240788e-25, 3.2294419278269826e-26, 5.034344900538335e-27, 6.7845790684462555e-28], [1.1469577512204812e-20, 2.8658540765932183e-20, 3.5803932531893005e-20, 2.9820582869597915e-20, 1.862785244100824e-20, 9.308922983332838e-21, 3.8766343474129035e-21, 1.3837685372670816e-21, 4.321953772238352e-22, 1.199897809258804e-22, 2.9981331260898206e-23, 6.810278624181442e-24, 1.41804589409663e-24, 2.7255464440393817e-25, 4.864432750329944e-26, 8.103032805996112e-27, 1.2654187553509394e-27, 1.8599102942806915e-28, 2.738318122077908e-29]] |
| Legacy trial inputs | {"lambda_home": 0.7053087841602202, "lambda_away": 2.4986570547552023, "rho": 0.05, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0852 |
| Legacy p draw | 0.1475 |
| Legacy p away | 0.7674 |
| Legacy p over 1 5 | 0.8259 |
| Legacy p under 3 5 | 0.6017 |
| Legacy p btts yes | 0.4620 |
| Legacy p over 2 5 | 0.6197 |
| Legacy goal margin distribution | {"-1": 0.22449125567340927, "-10": 0.00012421959642299686, "-11": 2.7848866618066847e-05, "-12": 5.734563687448046e-06, "-13": 1.0917243711669858e-06, "-14": 1.9323614351532652e-07, "-15": 3.195545212781609e-08, "-16": 4.957716268993401e-09, "-17": 7.215639485835087e-10, "-18": 9.123121250309235e-11, "-2": 0.2192823912883934, "-3": 0.16083528532527927, "-4": 0.09273333817665798, "-5": 0.04386570580115557, "-6": 0.017552993693491722, "-7": 0.006078746213302786, "-8": 0.0018540645750699668, "-9": 0.0005050064842164783, "0": 0.1474718523180621, "1": 0.06403085037251198, "10": 3.874475919151445e-10, "11": 2.4519014891724542e-11, "12": 1.4251760414356114e-12, "13": 7.658677429184849e-14, "14": 3.826500500650264e-15, "15": 1.7862038446549572e-16, "16": 7.822406157946998e-18, "17": 3.213706122106399e-19, "18": 1.1469577512204812e-20, "2": 0.016968579550821306, "3": 0.003513142001077861, "4": 0.0005717720268827132, "5": 7.634573358858407e-05, "6": 8.623498416297e-06, "7": 8.429832462977291e-07, "8": 7.257757073016483e-08, "9": 5.580166612234246e-09} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0879 |
| Legacy raw p draw | 0.1434 |
| Legacy raw p away | 0.7687 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.7053 |
| Legacy lambda away | 2.4987 |
| Legacy model home team | Casa Pia |
| Legacy model away team | Sp Lisbon |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 27.2% |
| Market reference home draw last update utc | 2026-10-29T12:07:10Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.6% |
| Market reference draw away last update utc | 2026-10-29T12:07:10Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.2% |
| Market reference home away last update utc | 2026-10-29T12:07:10Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.42 |
| Market reference dc draw away odds | 1.04 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 82.2% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-29T12:07:30Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-29T12:07:31Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T12:07:30Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-10-29T12:07:31Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.6% |
| Market reference btts yes odds | 2.12 |
| Market reference btts yes opposite odds | 1.79 |
| Market reference btts yes last update utc | 2026-10-29T12:07:30Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,356.0841 |
| Elo away rating | 1,692.9144 |
| Elo rating diff | -276.8303 |
| Elo home expectancy | 0.1689 |

</details>


---

## 2026-10-31 — FC Porto vs Estoril

The model's most likely 1X2 outcome is **FC Porto win** at **80.5%**. Expected goals are 2.34 for FC Porto and 0.69 for Estoril (3.04 combined). The most likely exact score is 2-0 at 14.2%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 59.9%; Under 3.5 goals: 62.8%; Double Chance 1X: 94.3%; Double Chance X2: 19.5%; Double Chance 12 (either team wins): 86.3%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 43.8%; BTTS No (at least one team does not score): 56.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Porto win | 80.5% | 1.24 |
| Draw | 13.7% | 7.28 |
| Estoril win | 5.7% | 17.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Porto expected goals | 2.34 |
| Estoril expected goals | 0.69 |
| Expected total goals | 3.04 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 59.9% |
| Under 2.5 | 40.1% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.22% |
| 2 | 1-0 | 12.55% |
| 3 | 3-0 | 11.11% |
| 4 | 2-1 | 9.83% |
| 5 | 3-1 | 7.68% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:30:00+00:00 |
| Fixture id | 60352ce6c1b34bca7b294edae8aa388b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 10.00 |
| Matched home-team name | Porto |
| Matched away-team name | Estoril |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5377 |
| Dc lambda away | 0.6307 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.8905 |
| Shot lambda away | 0.8334 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.71 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.36 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.03 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.043131710349880545, "-10": 2.2844940493347142e-10, "-11": 1.418937423958153e-11, "-12": 8.09365036239986e-13, "-13": 4.267680991483981e-14, "-14": 2.091987771757828e-15, "-15": 9.580162000848937e-17, "-16": 4.1157620766406536e-18, "-17": 1.6596245721405329e-19, "-18": 5.849365551733769e-21, "-2": 0.011379984859123952, "-3": 0.0023309208635696006, "-4": 0.00037415807260507536, "-5": 4.91873521770152e-05, "-6": 5.46406501419811e-06, "-7": 5.249331846994463e-07, "-8": 4.43941311010106e-08, "-9": 3.351616426511917e-09, "0": 0.13737117586126898, "1": 0.25428881005853543, "10": 8.253582901973941e-05, "11": 1.737301185777368e-05, "12": 3.358270684572318e-06, "13": 6.000985724826249e-07, "14": 9.968944379761446e-08, "15": 1.5471138375157415e-08, "16": 2.252470255792409e-09, "17": 3.078066838248601e-10, "18": 3.6765149727186184e-11, "2": 0.2363301234347773, "3": 0.16404549671196167, "4": 0.08923830025722833, "5": 0.039756578417222334, "6": 0.014966863584440868, "7": 0.004872797421841719, "8": 0.0013965589573135622, "9": 0.00035731184285553284} |
| Raw goal margin distribution | {"-1": 0.07241808772278747, "-10": 3.8356626510955305e-10, "-11": 2.382394159837258e-11, "-12": 1.358922883389592e-12, "-13": 7.165431046140175e-14, "-14": 3.5124448518554204e-15, "-15": 1.6085080015332968e-16, "-16": 6.910359378157844e-18, "-17": 2.786507580553193e-19, "-18": 9.821077444226148e-21, "-2": 0.019106980342928, "-3": 0.0039136132141193046, "-4": 0.0006282109358591311, "-5": 8.258550277537495e-05, "-6": 9.174158323686986e-06, "-7": 8.813621604567783e-07, "-8": 7.453769058473745e-08, "-9": 5.6273597874828484e-09, "0": 0.15604963208078979, "1": 0.23611250935892217, "10": 7.663625346858038e-05, "11": 1.6131206968631478e-05, "12": 3.1182249752096785e-06, "13": 5.572041482240738e-07, "14": 9.256374563328889e-08, "15": 1.4365277432210477e-08, "16": 2.091466015469002e-09, "17": 2.858049809529816e-10, "18": 3.4137214913405686e-11, "2": 0.21943749104981936, "3": 0.1523196945582308, "4": 0.08285963900577813, "5": 0.036914819379800096, "6": 0.013897047681105341, "7": 0.004524494910349737, "8": 0.0012967343698807672, "9": 0.00033177156250351845} |
| Unadjusted home-win probability | 74.8% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 9.6% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 44.7% |
| P home draw | 94.3% |
| P draw away | 19.5% |
| P home away | 86.3% |
| Raw p home draw | 90.4% |
| Raw p draw away | 25.2% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5993 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 1.75, "market_key": "spreads", "opposite_price": 1.79, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.91, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.20 |
| Reference draw odds | 7.40 |
| Reference away odds | 23.00 |
| Market reference 1x2 last update utc | 2026-10-29T12:07:30Z |
| Market reference home last update utc | 2026-10-29T12:07:30Z |
| Market reference draw last update utc | 2026-10-29T12:07:30Z |
| Market reference away last update utc | 2026-10-29T12:07:30Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.19 |
| Market reference over 2 5 last update utc | 2026-10-29T12:07:32Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:07:32Z |
| Home probability edge | -2.5% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0822 |
| Raw edge prob draw | 0.0267 |
| Raw edge prob away | 0.0556 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03727386948304492, 0.022826933051749838, 0.0064148428811618445, 0.0013553169239136113, 0.00021476176403801005, 2.7224696735600047e-05, 2.875993451260606e-06, 2.6041496949909247e-07, 2.0632509358045412e-08, 1.4530669799091646e-09, 9.210044451287821e-11, 5.3069516826715536e-12, 2.8031089627458957e-13, 1.3666985076631031e-14, 6.187579287281399e-16, 2.6146021286778312e-17, 1.0357661656562088e-18, 3.8617921139262016e-20, 1.3598546126023454e-21], [0.11125891430942109, 0.0623902319191664, 0.01638819199941016, 0.003462468899179551, 0.0005486583363596699, 6.955175138255611e-05, 7.3473869495254985e-06, 6.652899531186496e-07, 5.271049206555682e-08, 3.712193906523469e-09, 2.3529177500832223e-10, 1.3557829040929236e-11, 7.161186755119247e-13, 3.491545773422535e-14, 1.580759486242866e-15, 6.679602677825549e-17, 2.6461029683384014e-18, 9.865836435477597e-20, 3.474061468918541e-21], [0.13775262639545946, 0.08731241091605683, 0.026586068267314945, 0.004422836705664061, 0.0007008369748808798, 8.884297532055276e-05, 9.385295185980915e-06, 8.498181240732353e-07, 6.733053952813851e-08, 4.741826698343743e-09, 3.0055348635600636e-10, 1.731829676377708e-11, 9.147449568185793e-13, 4.4599784881413905e-14, 2.019206896049887e-15, 8.532290906566437e-17, 3.380039410059932e-18, 1.2602274501078616e-19, 4.4376446489113565e-21], [0.11730692560017558, 0.07435321386830154, 0.02356382789959127, 0.004783356154488273, 0.0005968164311741453, 7.565660683744203e-05, 7.992298607482944e-06, 7.23685305049296e-07, 5.7337117975322804e-08, 4.038029083486647e-09, 2.5594434302560453e-10, 1.4747857831457816e-11, 7.789754823592232e-13, 3.798013717610183e-14, 1.7195095246045565e-15, 7.265900046814898e-17, 2.87836277228781e-18, 1.0731803203860709e-19, 3.778994740727647e-21], [0.07492188254687265, 0.0474880978077142, 0.015049804921707502, 0.0031796967891276275, 0.0004840986236560499, 4.832055211036296e-05, 5.104541394173874e-06, 4.6220515241019937e-07, 3.662021484703275e-08, 2.5790185802413493e-09, 1.6346717730936878e-10, 9.419198965562225e-12, 4.975180220401569e-13, 2.4257249621566705e-14, 1.0982206718105194e-15, 4.64060333283483e-17, 1.8383599812994788e-18, 6.854215086126172e-20, 2.413577874123593e-21], [0.038281037240713335, 0.024263854282231007, 0.007689637834619571, 0.0016246533997943727, 0.00025744047309810605, 3.135558814948463e-05, 2.608145078106949e-06, 2.3616188022497823e-07, 1.871095280401093e-08, 1.3177392633313078e-09, 8.3522902648626e-11, 4.812702165522762e-12, 2.54204850201542e-13, 1.2394145002156455e-14, 5.611314746369058e-16, 2.3710977749723374e-17, 9.393027045460957e-19, 3.502133876624107e-20, 1.2332079940047324e-21], [0.016299619488205724, 0.010331266355996647, 0.003274158166568886, 0.0006917584821527315, 0.000109615152953588, 1.3895580110152545e-05, 1.410371628143573e-06, 1.0055497611210052e-07, 7.966905626130597e-09, 5.610780199582857e-10, 3.5563078480934205e-11, 2.0491924896082813e-12, 1.082374624357033e-13, 5.2772824870570944e-15, 2.3892324186320535e-16, 1.0095857972280002e-17, 3.9994414393925627e-19, 1.491167786985075e-20, 5.250855906984838e-22], [0.005948732575341227, 0.003770513830762405, 0.0011949414743320425, 0.00025246517073777093, 4.000530390282139e-05, 5.0713509057276466e-06, 5.357331299431935e-07, 4.660779907231368e-08, 2.907613337668746e-09, 2.047718412720582e-10, 1.2979152279722212e-11, 7.478762387611583e-13, 3.95024999896129e-14, 1.926004607822295e-15, 8.719777004035063e-17, 3.6845988484073294e-18, 1.459641900898335e-19, 5.4421874057589306e-21, 1.9163599251446141e-22], [0.0018996757481802246, 0.0012040806325987164, 0.0003815941144661546, 8.062254539711133e-05, 1.2775344102337662e-05, 1.6194915814601078e-06, 1.7108169203444014e-07, 1.549107616829715e-08, 1.1792332963422535e-09, 6.539209753473005e-11, 4.144778825649605e-12, 2.388277394253718e-13, 1.2614778067822737e-14, 6.150527356919396e-16, 2.784584563906851e-17, 1.1766444339936873e-18, 4.6612388185985894e-20, 1.7379149761458338e-21, 6.119727905860471e-23], [0.0005392398617903499, 0.000341788999795859, 0.0001083188842842555, 2.2885426778107194e-05, 3.626395080669924e-06, 4.5970709337830294e-07, 4.8563060330629877e-08, 4.397279788394625e-09, 3.4839362943884927e-10, 2.357413827473159e-11, 1.1765323441307743e-12, 6.779337859253503e-14, 3.580816983279886e-15, 1.7458819090890086e-16, 7.904291018207058e-18, 3.3400099073273273e-19, 1.323134107871159e-20, 4.933226275263002e-22, 1.7371392108953077e-23], [0.00013776122895710075, 8.731786351915132e-05, 2.7672551077209827e-05, 5.8466087942614515e-06, 9.26446055635447e-07, 1.1744275346008002e-07, 1.240655104919976e-08, 1.1233862899271e-09, 8.900516811381531e-11, 6.268286061725117e-12, 3.817305682150981e-13, 1.7319378280110605e-14, 9.148020820443047e-16, 4.4602570108880486e-17, 2.0193329942031086e-18, 8.532823742566635e-20, 3.380250491315773e-21, 1.260306150489882e-22, 4.437921776924326e-24], [3.199479582031142e-05, 2.0279415593998783e-05, 6.4268998487098014e-06, 1.3578642991917826e-06, 2.1516541782462926e-07, 2.7275866700496316e-08, 2.8813990021606633e-09, 2.6090443040942487e-10, 2.067128902893859e-11, 1.4557980805372444e-12, 9.227355117990281e-14, 5.108491565357702e-15, 2.124611260554138e-16, 1.0358866093878593e-17, 4.689864291415818e-19, 1.981732853872405e-20, 7.850570520449835e-22, 2.9270381994460305e-23, 1.03069929176825e-24], [6.811505579050437e-06, 4.317369400767146e-06, 1.3682495247459632e-06, 2.8908139628341005e-07, 4.5807463568833466e-08, 5.806873069210862e-09, 6.134330560793272e-10, 5.554503280200886e-11, 4.400796971405983e-12, 3.099309276183979e-13, 1.964450131798298e-14, 1.1319426293337367e-15, 5.744487658820805e-17, 2.2053422246344452e-18, 9.984447772499438e-20, 4.218993759531997e-21, 1.671340714255336e-22, 6.2314937521693226e-24, 2.1942987277155354e-25], [1.3385813939340035e-06, 8.484394945489491e-07, 2.688852464155674e-07, 5.680961043143994e-08, 9.001977275793135e-09, 1.1411533261146796e-09, 1.2055045184391258e-10, 1.0915581962216934e-11, 8.648344886515348e-13, 6.090691232650047e-14, 3.86049217051802e-15, 2.224467593900292e-16, 1.1749541775855688e-17, 5.50409230284021e-19, 1.9621206885712794e-20, 8.29106940028447e-22, 3.2844802915634446e-23, 1.2245988051048004e-24, 4.312185339298424e-26], [2.442652955365831e-07, 1.548238492033949e-07, 4.906637316099118e-08, 1.0366658571707294e-08, 1.6426872879376257e-09, 2.0823847972124137e-10, 2.199813315810494e-11, 1.991883247471892e-12, 1.5781561951929549e-13, 1.1114337168492646e-14, 7.044653879260042e-16, 4.059224464779886e-17, 2.1440648340883188e-18, 1.0453714957305702e-19, 4.5472700777438046e-21, 1.5129603074959944e-22, 5.9935432595918994e-24, 2.2346567074532236e-25, 7.868906822442975e-27], [4.1602126362302645e-08, 2.636887620203529e-08, 8.35675592760468e-09, 1.7656009582025271e-09, 2.7977484061502436e-10, 3.546620705092925e-11, 3.7466194834099075e-12, 3.3924826847892786e-13, 2.687842057449995e-14, 1.892942091102821e-15, 1.199812606288841e-16, 6.913481865926036e-18, 3.651671268354728e-19, 1.7804279959376852e-20, 8.060694680201972e-22, 3.272573002340062e-23, 1.020792345862025e-24, 3.805963123644504e-26, 1.3401955248752455e-27], [6.642637698221137e-09, 4.210335058211937e-09, 1.3343284782154901e-09, 2.8191461616247827e-10, 4.4671824874970344e-11, 5.6629116001843525e-12, 5.982250908198761e-13, 5.416798453110709e-14, 4.291694328840882e-15, 3.0224725499375127e-16, 1.9157483393822574e-17, 1.1038800004747322e-18, 5.830646495671459e-20, 2.8428205860892386e-21, 1.2870561925190156e-22, 5.438540185828835e-24, 2.070000689735721e-25, 6.077005272035605e-27, 2.1398986289773934e-28], [9.982438981306048e-10, 6.327217397497013e-10, 2.0052053446136416e-10, 4.236563217250102e-11, 6.713203192120498e-12, 8.510123850425988e-13, 8.990021340159621e-14, 8.140269346119998e-15, 6.449482676970935e-16, 4.542118533802244e-17, 2.8789528753830774e-18, 1.6588914295858768e-19, 8.76219289819058e-21, 4.27214072551873e-22, 1.934165385954103e-23, 8.172942439259593e-25, 3.237684678518018e-26, 1.1598284554620114e-27, 3.2158019841527364e-29], [1.4168020573423144e-10, 8.98018474524449e-11, 2.8459768829668455e-11, 6.012930801281392e-12, 9.528012254084332e-13, 1.2078371830872885e-13, 1.275948769047523e-14, 1.1553439373384938e-15, 9.153715181868829e-17, 6.4466037763265334e-18, 4.0860819329552807e-19, 2.3544554539689262e-20, 1.243613203970961e-21, 6.063425762487267e-23, 2.7451502615661714e-24, 1.1599812114221724e-25, 4.595228002034689e-27, 1.7133032385458896e-28, 5.7965536736537645e-30]] |
| Legacy trial inputs | {"lambda_home": 2.5547300694669484, "lambda_away": 0.6338348182589337, "rho": 0.05, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8112 |
| Legacy p draw | 0.1316 |
| Legacy p away | 0.0573 |
| Legacy p over 1 5 | 0.8286 |
| Legacy p under 3 5 | 0.6003 |
| Legacy p btts yes | 0.4275 |
| Legacy p over 2 5 | 0.6221 |
| Legacy goal margin distribution | {"-1": 0.04428581041436228, "-10": 1.0661212098489922e-10, "-11": 6.069437013028843e-12, "-12": 3.1732009381173866e-13, "-13": 1.53360156100707e-14, "-14": 6.89043726526368e-16, "-15": 2.892192599486823e-17, "-16": 1.1388621746598962e-18, "-17": 4.2091982608180556e-20, "-18": 1.3598546126023454e-21, "-2": 0.010659154241225082, "-3": 0.002001292024606157, "-4": 0.0002944604701894529, "-5": 3.5481903557975024e-05, "-6": 3.612820363062006e-06, "-7": 3.1813291137550466e-07, "-8": 2.4660514763578337e-08, "-9": 1.7064808557882968e-09, "0": 0.13155043821844162, "1": 0.22558673754636654, "10": 0.00015946738244622882, "11": 3.659170265487362e-05, "12": 7.710822583315327e-06, "13": 1.502050747668076e-06, "14": 2.720118186502318e-07, "15": 4.601899488577723e-08, "16": 7.303819206800507e-09, "17": 1.0880457455830496e-09, "18": 1.4168020573423144e-10, "2": 0.22889516065857488, "3": 0.1732180942275781, "4": 0.10272560788952394, "5": 0.04989161439209337, "6": 0.020475567206643095, "7": 0.007267199795878872, "8": 0.002270542134311099, "9": 0.0006332829205716889} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7923 |
| Legacy raw p draw | 0.1337 |
| Legacy raw p away | 0.0740 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.5547 |
| Legacy lambda away | 0.6338 |
| Legacy model home team | Porto |
| Legacy model away team | Estoril |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,693.7612 |
| Elo away rating | 1,387.3773 |
| Elo rating diff | 366.3839 |
| Elo home expectancy | 0.8918 |

</details>


---

## 2026-10-31 — Moreirense FC vs CF Estrela

The model's most likely 1X2 outcome is **Moreirense FC win** at **36.2%**. Expected goals are 1.42 for Moreirense FC and 1.07 for CF Estrela (2.49 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 47.9%; Under 3.5 goals: 73.0%; Double Chance 1X: 64.3%; Double Chance X2: 63.8%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 53.5%; BTTS No (at least one team does not score): 46.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Moreirense FC win | 36.2% | 2.76 |
| Draw | 28.1% | 3.56 |
| CF Estrela win | 35.7% | 2.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Moreirense FC expected goals | 1.42 |
| CF Estrela expected goals | 1.07 |
| Expected total goals | 2.49 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.31% |
| 2 | 0-1 | 10.60% |
| 3 | 1-0 | 8.80% |
| 4 | 1-2 | 8.47% |
| 5 | 0-0 | 7.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Moreirense FC win | 36.2% | 32.1% | 2.97 | +7.6% |
| Draw | 28.1% | 29.3% | 3.25 | -8.8% |
| CF Estrela win | 35.7% | 38.6% | 2.49 | -11.1% |
| Over 2.5 | 47.9% | 47.9% | 2.00 | -4.1% |
| Under 2.5 | 52.1% | 52.1% | 1.85 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:30:00+00:00 |
| Fixture id | 853df01a49c2a57a62c1ac2d356b395b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:07:30Z |
| Market best draw last update utc | 2026-10-29T12:07:30Z |
| Market best away last update utc | 2026-10-29T12:07:30Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Moreirense |
| Matched away-team name | Estrela |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4765 |
| Dc lambda away | 1.0418 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.2893 |
| Shot lambda away | 1.1237 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.5% |
| P btts no | 46.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.42 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.72 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.08 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.2187300481046046, "-10": 9.98169908626142e-08, "-11": 1.0175972782016434e-08, "-12": 9.527939135086675e-10, "-13": 8.24579246233069e-11, "-14": 6.599901500153691e-12, "-15": 4.4839542959590174e-13, "-2": 0.09576652901670367, "-3": 0.03201875498211868, "-4": 0.008407443483364838, "-5": 0.0018101887108662408, "-6": 0.00032959097486977865, "-7": 5.1923960694116677e-05, "-8": 7.203477807668677e-06, "-9": 8.923401000145824e-07, "0": 0.28068762263212566, "1": 0.18328935348871955, "10": 1.1136438828562152e-06, "11": 1.5122714467195738e-07, "12": 1.8861001204104467e-08, "13": 2.174253217776227e-09, "14": 2.3180731071554888e-10, "15": 2.0977938353973774e-11, "2": 0.10781023326627351, "3": 0.04801341895625256, "4": 0.016793224784385035, "5": 0.004816215929372624, "6": 0.0011680713224867987, "7": 0.0002451172164471678, "8": 4.529603412167753e-05, "9": 7.474124354950689e-06} |
| Raw goal margin distribution | {"-1": 0.18144096654628142, "-10": 4.9960233854384125e-08, "-11": 4.788614444567909e-09, "-12": 4.2137978089305733e-10, "-13": 3.411341320941981e-11, "-14": 2.344627557990409e-12, "-2": 0.07617502099355415, "-3": 0.02422417087102472, "-4": 0.0060228047004343855, "-5": 0.0012247176450403399, "-6": 0.00021027037319736928, "-7": 3.120401607930286e-05, "-8": 4.074873328191219e-06, "-9": 4.749072467387985e-07, "0": 0.253116230800496, "1": 0.2395920960447644, "10": 8.785045041416141e-07, "11": 1.121608660765241e-07, "12": 1.3146711387975256e-08, "13": 1.417687674962088e-09, "14": 1.2978999244158858e-10, "2": 0.1351563605072181, "3": 0.057251224543173475, "4": 0.01896036059469256, "5": 0.005135653801639627, "6": 0.0011744912982775155, "7": 0.00023216361845501265, "8": 4.038403751991703e-05, "9": 6.26926133137622e-06} |
| Unadjusted home-win probability | 45.8% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 28.9% |
| Raw p over 1 5 | 70.4% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 49.1% |
| P home draw | 64.3% |
| P draw away | 63.8% |
| P home away | 71.9% |
| Raw p home draw | 71.1% |
| Raw p draw away | 54.2% |
| Raw p home away | 74.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0652 |
| Totals anchor target over 2 5 | 0.4793 |
| Totals anchor reference over odds | 2.00 |
| Totals anchor reference under odds | 1.85 |
| Totals anchor reference last update utc | 2026-10-29T12:07:30Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4414 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.12, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.12, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.97 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.49 |
| Market reference 1x2 last update utc | 2026-10-29T12:07:30Z |
| Market reference home last update utc | 2026-10-29T12:07:30Z |
| Market reference draw last update utc | 2026-10-29T12:07:30Z |
| Market reference away last update utc | 2026-10-29T12:07:30Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-29T12:07:30Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:07:30Z |
| Market best over 2 5 last update utc | 2026-10-29T12:07:30Z |
| Market best under 2 5 last update utc | 2026-10-29T12:07:30Z |
| Home probability edge | +4.1% |
| Draw probability edge | -1.2% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.1362 |
| Raw ev home | 0.3589 |
| Raw edge prob draw | -0.0394 |
| Raw ev draw | -0.1774 |
| Raw edge prob away | -0.0968 |
| Raw ev away | -0.2796 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.0855757139410667, 0.11250272424688139, 0.05225263307274364, 0.017364687489798768, 0.0043279977565713465, 0.0008629727240131841, 0.00014339231138694514, 2.04224514297228e-05, 2.545059449628829e-06, 2.819262200256899e-07, 2.8107066101976066e-08, 2.547433621556163e-09, 2.11641912273333e-10, 1.6230741879568406e-11, 1.1558204707690837e-12, 7.682086084073924e-14], [0.10893555919625339, 0.12811160665783014, 0.07656047079346402, 0.025442711136672735, 0.006341375091564547, 0.0012644261953342808, 0.0002100981753907828, 2.992294175949998e-05, 3.7290168591059385e-06, 4.1307782718125917e-07, 4.1182426355329145e-08, 3.732495491852508e-09, 3.100973767334896e-10, 2.3781255920577538e-11, 1.693506225257825e-12, 1.1255779712647815e-13], [0.07601679443915572, 0.07578610694553285, 0.049247177300577566, 0.01863930895285212, 0.0046456861017150995, 0.0009263175758398016, 0.00015391774801446878, 2.1921522169451445e-05, 2.7318746400058174e-06, 3.026204715780633e-07, 3.01702111910014e-08, 2.734423083453864e-09, 2.2717707949265224e-10, 1.74221282476289e-11, 1.240661247796841e-12, 8.245974827222136e-14], [0.037126560125493764, 0.0370138924819108, 0.018450783374914567, 0.007993100906581811, 0.002268950508266288, 0.0004524129888460997, 7.517334252516582e-05, 1.0706459235372127e-05, 1.334246054780287e-06, 1.4779967000898734e-07, 1.4735114365788014e-08, 1.3354907131429341e-09, 1.1095315927415083e-10, 8.508957746401407e-12, 6.059382634000358e-13, 4.027329519415747e-14], [0.01359944348733851, 0.013558173376491216, 0.006758514253842108, 0.0022460014168077694, 0.0007297460870392444, 0.0001657186890989572, 2.753596400985553e-05, 3.921771551923445e-06, 4.887337733109623e-07, 5.413895747250494e-08, 5.3974662457188515e-09, 4.891896911500147e-10, 4.064209596014696e-11, 3.1168276731589133e-12, 2.2195493312795116e-13, 1.475209123039007e-14], [0.003985176381332838, 0.003973082601822171, 0.0019805127615986, 0.0006581675056803458, 0.00016404254264328866, 4.26391195325427e-05, 8.069129704570227e-06, 1.149234626862442e-06, 1.4321838183833637e-07, 1.5864862031323734e-08, 1.581671707486141e-09, 1.4335198384975043e-10, 1.1909746237707117e-11, 9.133541412427581e-13, 6.504159953643278e-14, 4.322947891312814e-15], [0.0009731789640950717, 0.0009702256665016916, 0.0004836406656271963, 0.0001607243218592038, 4.005914329536524e-05, 7.987515233515796e-06, 1.7301437547945492e-06, 2.8064277629240744e-07, 3.4973889017727765e-08, 3.874194896234728e-09, 3.862437911255124e-10, 3.500651459176207e-11, 2.908356719300494e-12, 2.2304082729941645e-13, 1.588314051956277e-14, 1.0556626729022595e-15], [0.0002037000277743739, 0.0002030818611020632, 0.00010123278518734218, 3.364185831655404e-05, 8.384941416681049e-06, 1.6718991418277845e-06, 2.778042407153455e-07, 5.157777121035607e-08, 7.32052626200523e-09, 8.109234139685496e-10, 8.084625118577899e-11, 7.327355252953594e-12, 6.087599160655737e-13, 4.668557828719364e-14, 3.324564426839737e-15, 2.2096502670556348e-16], [3.730761760210391e-05, 3.7194400504998364e-05, 1.8540763493407923e-05, 6.161499334150078e-06, 1.5357002716566837e-06, 3.0620797912548736e-07, 5.087978874666991e-08, 7.246483471693484e-09, 1.1772238696489399e-09, 1.4852045413779395e-10, 1.480697404294673e-11, 1.3420035863458552e-12, 1.1149425166116968e-13, 8.550453926304375e-15, 6.088932813866717e-16, 4.04696985554703e-17], [6.073673229109417e-06, 6.055241506690115e-06, 3.0184328594278923e-06, 1.0030909493103737e-06, 2.500117195200171e-07, 4.985060223328991e-08, 8.283220175280354e-09, 1.1797261657556642e-09, 1.4701825764957115e-10, 2.1230024847265816e-11, 2.410572629105428e-12, 2.1847793506112245e-13, 1.815124350035811e-14, 1.3920123140213517e-15, 9.912771332614544e-17, 6.588459422094711e-18], [8.899135881227645e-07, 8.872129752292637e-07, 4.4226027893091006e-07, 1.4697271852492404e-07, 3.66316754290425e-08, 7.304101921534005e-09, 1.2136560380077403e-09, 1.7285328096649585e-10, 2.154109058048074e-11, 2.3861911137170543e-12, 3.1011799282615936e-13, 3.201135059160971e-14, 2.6595171690957453e-15, 2.0395741198995236e-16, 1.4524176016859875e-17, 9.653399752257095e-19], [1.185363549523806e-07, 1.1817663372460581e-07, 5.890900206982936e-08, 1.9576743814123436e-08, 4.879333610712742e-09, 9.729052680335989e-10, 1.6165880017053912e-10, 2.3024030805675928e-11, 2.8692699978832137e-12, 3.1784029440031613e-13, 3.168757472705861e-14, 3.743846689545733e-15, 3.5424728351759333e-16, 2.7167096340004156e-17, 1.9346180423619436e-18, 1.2858313827352366e-19], [1.4473272457966174e-08, 1.4429350546071802e-08, 7.192780961807452e-09, 2.3903176976838705e-09, 5.957659554279985e-10, 1.1879159795066813e-10, 1.9738517023204046e-11, 2.8112309600292948e-12, 3.5033746778795957e-13, 3.8808255752625286e-14, 3.869048468219934e-15, 3.5066428191453596e-16, 3.797799438542695e-17, 3.3170986857040958e-18, 2.362165939761692e-19, 1.5699983304536993e-20], [1.6312472812633985e-09, 1.626296949569328e-09, 8.106808203015284e-10, 2.6940688479587466e-10, 6.714732952645454e-11, 1.3388711623908196e-11, 2.224680169863776e-12, 3.1684699323318694e-13, 3.948568255821527e-14, 4.373983967406121e-15, 4.360710276953478e-16, 3.952251698228933e-17, 3.283548195802352e-18, 3.282628859461566e-19, 2.6623396873928074e-20, 1.7695068724634223e-21], [1.7072148533810845e-10, 1.7020339835679345e-10, 8.484344180472875e-11, 2.8195322720809352e-11, 7.027439656092662e-12, 1.4012227094269256e-12, 2.3282840521102613e-13, 3.31602632727692e-14, 4.132454014394811e-15, 4.577681436393272e-16, 4.563789587033448e-17, 4.1363089955872565e-18, 3.436463812724221e-19, 2.6354116972242174e-20, 2.4464828401198993e-21, 1.8519132264789177e-22], [1.6676055697644796e-11, 1.6625449018939284e-11, 8.287497957936977e-12, 2.7541159870656976e-12, 6.864395239108188e-13, 1.36871278392001e-13, 2.2742652722376448e-14, 3.2390908279066355e-15, 4.0365764845311433e-16, 4.471474135091112e-17, 4.4579045920890145e-18, 4.0403420258718403e-19, 3.356734029723083e-20, 2.574267214351931e-21, 1.8331822202921908e-22, 1.5883130996886494e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4651983314770025, "lambda_away": 0.9969653088462243, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-29T12:07:30Z", "over": 2.0, "under": 1.85, "bookmaker": "pinnacle", "event_id": "853df01a49c2a57a62c1ac2d356b395b", "kickoff_utc": "2026-10-31T15:30:00Z", "home_team": "Moreirense FC", "away_team": "CF Estrela"}} |
| Legacy p home | 0.4036 |
| Legacy p draw | 0.2717 |
| Legacy p away | 0.3247 |
| Legacy p over 1 5 | 0.6930 |
| Legacy p under 3 5 | 0.7702 |
| Legacy p btts yes | 0.4861 |
| Legacy p over 2 5 | 0.4366 |
| Legacy goal margin distribution | {"-1": 0.21014553043453327, "-10": 3.207547390894864e-08, "-11": 2.875573816891912e-09, "-12": 2.367041027369015e-10, "-13": 1.8006707853098453e-11, "-14": 1.268378267895562e-12, "-15": 7.682086084073924e-14, "-2": 0.08282216429845486, "-3": 0.024711622446063557, "-4": 0.005757553151474858, "-5": 0.0010963824238813035, "-6": 0.00017620047123034728, "-7": 2.4469325200615845e-05, "-8": 2.9896845502684396e-06, "-9": 3.2595720554868244e-07, "0": 0.2717017669329218, "1": 0.2055907661915461, "10": 1.015559574004908e-06, "11": 1.3380526808099868e-07, "12": 1.6187166965327297e-08, "13": 1.8097381775781289e-09, "14": 1.8734693435704773e-10, "15": 1.6676055697644796e-11, "2": 0.12048915180440392, "3": 0.052834670193820564, "4": 0.01809139540101315, "5": 0.005063053812687442, "6": 0.0011958423042800915, "7": 0.00024406483424077783, "8": 4.382530552227361e-05, "9": 7.0222540954010825e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4858 |
| Legacy raw p draw | 0.2509 |
| Legacy raw p away | 0.2633 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4652 |
| Legacy lambda away | 0.9970 |
| Legacy model home team | Moreirense |
| Legacy model away team | Estrela |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,438.8922 |
| Elo away rating | 1,379.1640 |
| Elo rating diff | 119.7282 |
| Elo home expectancy | 0.6658 |

</details>


---
