# Super Lig — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,831 |
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
| Training sha256 | 36930ef41a7cb5e7e2f4d6e9884819c8b34ead9559d248ba647b034c279b2986 |
| Training as of utc | 2026-10-29T12:08:03.532144+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-29', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1800, 'tune_start_date': '2025-10-30', 'audit_start_date': '2026-04-30', 'training_shot_matches': 1503, 'tuning_matches': 189, 'audit_matches': 94, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8834269290076148, 'audit_candidate_poisson_score': 0.8730025498190247, 'audit_gain': 0.010424379188590072, 'audit_gain_lower95': 0.0029519965878100065, 'audit_baseline_briers': [0.6143663322631336, 0.17437378698225448, 0.2059347184072143, 0.24831204298872858], 'audit_candidate_briers': [0.6098513843205008, 0.17317189145574685, 0.20307008736569596, 0.24810792752303473], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1657.916 |
| Base scoring parameter | 0.124 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1831, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 8.00 |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'ANCHORED_MAIN': 2, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 5 |
| Goal rate features used | {'shot_features': 5} |
| Legacy comparison status | {'AVAILABLE': 5} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Torku Konyaspor vs Galatasaray

The model's most likely 1X2 outcome is **Galatasaray win** at **59.7%**. Expected goals are 0.95 for Torku Konyaspor and 1.80 for Galatasaray (2.75 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 59.3%; Under 3.5 goals: 63.3%; Double Chance 1X: 40.3%; Double Chance X2: 82.0%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 80.4%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torku Konyaspor win | 18.0% | 5.55 |
| Draw | 22.3% | 4.49 |
| Galatasaray win | 59.7% | 1.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torku Konyaspor expected goals | 0.95 |
| Galatasaray expected goals | 1.80 |
| Expected total goals | 2.75 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 59.3% |
| Under 2.5 | 40.7% |
| Over 3.5 | 36.7% |
| Under 3.5 | 63.3% |
| Over 4.5 | 19.6% |
| Under 4.5 | 80.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.45% |
| 2 | 1-2 | 10.19% |
| 3 | 0-2 | 9.65% |
| 4 | 0-1 | 8.68% |
| 5 | 1-3 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torku Konyaspor win | 18.0% | 17.8% | 5.11 | -7.9% |
| Draw | 22.3% | 21.1% | 4.35 | -3.2% |
| Galatasaray win | 59.7% | 61.2% | 1.59 | -5.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T17:00:00+00:00 |
| Fixture id | feb03ec355aa5c94e0d7ae612a59b813 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:07:57Z |
| Market best draw last update utc | 2026-10-29T12:07:57Z |
| Market best away last update utc | 2026-10-29T12:07:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Konyaspor |
| Matched away-team name | Galatasaray |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9032 |
| Dc lambda away | 1.8386 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.1490 |
| Shot lambda away | 1.6581 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.41 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.55 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.10 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.2315574034868943, "-10": 1.6398963402812348e-05, "-11": 2.9336931508990047e-06, "-12": 4.822286706035824e-07, "-13": 7.33063527774887e-08, "-14": 1.0363206885714456e-08, "-15": 1.3686702714136649e-09, "-16": 1.6859719418875107e-10, "-17": 1.7634212098595635e-11, "-2": 0.1850826642710019, "-3": 0.10630271505709675, "-4": 0.04834051042922304, "-5": 0.018110112918034674, "-6": 0.005754375429369512, "-7": 0.00158511357035731, "-8": 0.00038502560238645327, "-9": 8.358988885885042e-05, "0": 0.22262239835145717, "1": 0.1117844703660742, "10": 2.6399341748678476e-08, "11": 2.4952738253106665e-09, "12": 2.16712206582042e-10, "13": 1.7405992088296368e-11, "14": 1.300104196537259e-12, "15": 9.072138015982008e-14, "16": 5.9045659783184644e-15, "17": 3.263025890276466e-16, "2": 0.049060036080410444, "3": 0.014887895103545476, "4": 0.003577066365628285, "5": 0.0007080497058189195, "6": 0.0001188687248783086, "7": 1.7300418851094345e-05, "8": 2.2203051449349433e-06, "9": 2.5468515205404256e-07} |
| Raw goal margin distribution | {"-1": 0.2351614409177999, "-10": 7.411834021428895e-06, "-11": 1.1991099383230314e-06, "-12": 1.7817468268083423e-07, "-13": 2.4475591498996803e-08, "-14": 3.1253033590058766e-09, "-15": 3.711043659360853e-10, "-16": 3.775651421977594e-11, "-2": 0.17673478611175303, "-3": 0.09378209620062777, "-4": 0.03908131015230012, "-5": 0.013353915373720484, "-6": 0.0038586328743109885, "-7": 0.0009647065852102931, "-8": 0.00021239099678961492, "-9": 4.175309829531557e-05, "0": 0.25063576567987794, "1": 0.11930261480290485, "10": 1.2565909026906374e-08, "11": 1.074123086225585e-09, "12": 8.432723590372963e-11, "13": 6.120429361094504e-12, "14": 4.1292168896481967e-13, "15": 2.5905883172588424e-14, "16": 1.392582886469766e-15, "2": 0.04933733464152104, "3": 0.013832491231061448, "4": 0.0030456248326038, "5": 0.0005498481050513237, "6": 8.394491536969811e-05, "7": 1.1088760442896535e-05, "8": 1.2898840837707084e-06, "9": 1.339769575460425e-07} |
| Unadjusted home-win probability | 18.6% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 56.3% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 70.2% |
| Raw p btts yes | 52.3% |
| P home draw | 40.3% |
| P draw away | 82.0% |
| P home away | 77.7% |
| Raw p home draw | 43.7% |
| Raw p draw away | 81.4% |
| Raw p home away | 74.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1090 |
| Totals anchor target over 2 5 | 0.5932 |
| Totals anchor reference over odds | 1.63 |
| Totals anchor reference under odds | 2.32 |
| Totals anchor reference last update utc | 2026-10-29T12:07:57Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5314 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.22, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.06, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:58Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:58Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.11 |
| Reference draw odds | 4.35 |
| Reference away odds | 1.59 |
| Market reference 1x2 last update utc | 2026-10-29T12:07:57Z |
| Market reference home last update utc | 2026-10-29T12:07:57Z |
| Market reference draw last update utc | 2026-10-29T12:07:57Z |
| Market reference away last update utc | 2026-10-29T12:07:57Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-29T12:07:58Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:07:58Z |
| Home probability edge | +0.3% |
| Draw probability edge | +1.2% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0086 |
| Raw ev home | -0.0487 |
| Raw edge prob draw | 0.0400 |
| Raw ev draw | 0.0903 |
| Raw edge prob away | -0.0486 |
| Raw ev away | -0.1045 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.06962251047204433, 0.11140537307597739, 0.11170114651417806, 0.06828301530797298, 0.03130610332829298, 0.011482470142027497, 0.0035096223671342813, 0.0009194723291268345, 0.00021077786044833492, 4.2949567725187836e-05, 7.87653327285475e-06, 1.3131633148598946e-06, 2.0068449055504015e-07, 2.8310450012814164e-08, 3.708472406557777e-09, 4.533985299318987e-10, 5.196805224156086e-11], [0.049236312185414494, 0.10900627679493462, 0.10076468891653347, 0.06159754855262345, 0.028240979269303138, 0.010358242220082537, 0.0031660015771987258, 0.0008294484533340576, 0.0001901409806556743, 3.87444530874069e-05, 7.105356119860362e-06, 1.1845938653965913e-06, 1.8103583438675703e-07, 2.5538624961796625e-08, 3.3453825682524353e-09, 4.0900709840075307e-10, 4.6879954066132815e-11], [0.026878490413128352, 0.04929253896517232, 0.04118149615188891, 0.027783321888904436, 0.012737977986682537, 0.0046720427121857665, 0.0014280120392282235, 0.0003741193263486225, 8.576231025355566e-05, 1.747552681609335e-05, 3.204841764842763e-06, 5.343062093099046e-07, 8.165547133578981e-08, 1.1519092148731066e-08, 1.508921100259089e-09, 1.8448097589479406e-10, 2.1145011198679424e-11], [0.008082288647118263, 0.014822131821482678, 0.01359117456240206, 0.00756983936705811, 0.0038302751860916054, 0.0014048704816066234, 0.00042939931950066536, 0.00011249665950503338, 2.5788492428666553e-05, 5.254843178214154e-06, 9.636871644825521e-07, 1.6066441765200387e-07, 2.455357718415602e-08, 3.4637595440748696e-09, 4.5372845314499235e-10, 5.5472925531395326e-11, 6.358247108654657e-12], [0.0018227415892215798, 0.0033427309134243747, 0.0030651217993919967, 0.0018737118219473224, 0.0007826971160867919, 0.0003168305372522379, 9.68394018340799e-05, 2.5370578666654622e-05, 5.815896922936083e-06, 1.1850877423418124e-06, 2.1733357349562899e-07, 3.623351364304326e-08, 5.537395192348218e-09, 7.811572750868692e-10, 1.0232617985691832e-10, 1.2510417884904121e-11, 1.4339306532469504e-12], [0.0003288560501746106, 0.0006030900328854434, 0.0005530042515146741, 0.0003380520160261533, 0.00015498863511402067, 5.1794158016849055e-05, 1.747160616553864e-05, 4.577318222339655e-06, 1.049294590966251e-06, 2.1381158819298698e-07, 3.921096713474815e-08, 6.537191147148703e-09, 9.990477651794803e-10, 1.4093511530613418e-10, 1.8461521663953352e-11, 2.2571090910480375e-12, 2.587074183414416e-13], [4.944305799934723e-05, 9.067376275714132e-05, 8.314343393411161e-05, 5.082565890547752e-05, 2.3302329609302778e-05, 8.546841527118029e-06, 2.380155488362388e-06, 6.881935431275859e-07, 1.577600086481581e-07, 3.214628026562175e-08, 5.8953153552275114e-09, 9.82857760621023e-10, 1.5020546701713349e-10, 2.1189402100177224e-11, 2.775664567832614e-12, 3.393532691288098e-13, 3.889630701069837e-14], [6.371739635960512e-06, 1.1685151191679633e-05, 1.0714715774150489e-05, 6.549915771312448e-06, 3.0029772265253295e-06, 1.1014336718681563e-06, 3.366537167429339e-07, 8.035932896957889e-08, 2.0330573001496255e-08, 4.142699428499377e-09, 7.597308102562283e-10, 1.2666113309462052e-10, 1.9357017273156217e-11, 2.730683713490914e-12, 3.577006087128302e-13, 4.373254331334764e-14, 5.01257711599933e-15], [7.184867639129528e-07, 1.317634891758706e-06, 1.2082071620391872e-06, 7.38578167863772e-07, 3.386201434555682e-07, 1.2419928618850696e-07, 3.796156988850909e-08, 9.945404214869788e-09, 2.0772242311002648e-09, 4.671369007999125e-10, 8.56683672737167e-11, 1.4282496277326814e-11, 2.1827258322209535e-12, 3.0791592511142127e-13, 4.0334848485225757e-14, 4.931346118657527e-15, 5.6522559249167675e-16], [7.201566910719642e-08, 1.3206973758599096e-07, 1.211015311131055e-07, 7.402947920293328e-08, 3.3940717392369416e-08, 1.2448795366514417e-08, 3.804980123769956e-09, 9.968519603266517e-10, 2.2851620078758925e-10, 4.24253480273826e-11, 8.586748010413186e-12, 1.431569205716567e-12, 2.1877989850345833e-13, 3.0863159197107966e-14, 4.0428595875328325e-15, 4.94280769210278e-16, 5.665393057224252e-17], [6.496474495704114e-09, 1.1913902800855709e-08, 1.092446988301871e-08, 6.67813865418985e-09, 3.0617643026716702e-09, 1.1229956286376978e-09, 3.4324413891007605e-10, 8.992519845389596e-11, 2.0614259211589072e-11, 4.200505310327605e-12, 7.018631902709115e-13, 1.2914068492413305e-13, 1.9735955361114928e-14, 2.7841402998341636e-15, 3.6470305040178193e-16, 4.458866314373665e-17, 5.110704650901958e-18], [5.327651278288588e-10, 9.770394623785163e-10, 8.958977053689127e-10, 5.476631049827097e-10, 2.510902261177757e-10, 9.20950140015238e-11, 2.8148884085338534e-11, 7.37461678345784e-12, 1.6905413007042283e-12, 3.444764926087708e-13, 6.317364060821688e-14, 9.596086371560197e-15, 1.6185130546948185e-15, 2.283227408520535e-16, 2.990869392242891e-17, 3.6566425120577785e-18, 4.1912043500421925e-19], [4.0050254665051155e-11, 7.344827437473399e-11, 6.734849820235612e-11, 4.117019992392612e-11, 1.8875536281632495e-11, 6.9231797868859794e-12, 2.1160731385500166e-12, 5.543817806512376e-13, 1.270852878282617e-13, 2.589578509263227e-14, 4.749035292133946e-15, 7.917517403370263e-16, 1.1024495096840148e-16, 1.716400612444869e-17, 2.248365641298381e-18, 2.7488560376273474e-19, 3.150709248867761e-20], [2.7791543488283136e-12, 5.096698956089308e-12, 4.673425256131136e-12, 2.8568692288629727e-12, 1.30980512314549e-12, 4.804110578910816e-13, 1.468378644436404e-13, 3.84694816423361e-14, 8.818661286771134e-15, 1.7969519634369212e-15, 3.295435246355715e-16, 5.494098129343871e-17, 8.396368309027972e-18, 1.079192842964874e-18, 1.560178631079517e-19, 1.907477311983592e-20, 2.1863299956805013e-21], [1.7907516884488744e-13, 3.284064544662817e-13, 3.011327590273917e-13, 1.8408273716142734e-13, 8.439746201216372e-14, 3.095534846528634e-14, 9.461516730495202e-15, 2.4787860103491535e-15, 5.682315771990864e-16, 1.157868314850107e-16, 2.1234179505263567e-17, 3.540129214404468e-18, 5.4102107472258715e-19, 7.632154358042953e-20, 9.108986063458468e-21, 1.22908546571105e-21, 1.4087645520378917e-22], [1.0769482823550924e-14, 1.97501847594592e-14, 1.81099596156912e-14, 1.107063524641669e-14, 5.075617258127958e-15, 1.8616377454469868e-15, 5.690104472388825e-16, 1.4907283647369668e-16, 3.417313662144579e-17, 6.96335678985908e-18, 1.2770119549752517e-18, 2.1290143694184332e-19, 3.253671186791294e-20, 4.589935935608615e-21, 6.012497419634088e-22, 6.697528525222248e-23, 8.472233053562543e-24], [6.071913876737349e-16, 1.1135299890802576e-15, 1.0210528852620574e-15, 6.241705834751616e-16, 2.861670459721588e-16, 1.0496050966642912e-16, 3.208122885012518e-17, 8.404836511274432e-18, 1.926706656791734e-18, 3.925991936080519e-19, 7.199887624331711e-20, 1.2003540100528834e-20, 1.834443821779045e-21, 2.5878397465671576e-22, 3.389890407391586e-23, 4.1444863513713325e-24, 4.328143576940363e-25]] |
| Legacy trial inputs | {"lambda_home": 0.9020918053311436, "lambda_away": 1.8339028050881978, "rho": -0.09475376269082486, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1743 |
| Legacy p draw | 0.2282 |
| Legacy p away | 0.5974 |
| Legacy p over 1 5 | 0.7697 |
| Legacy p under 3 5 | 0.7043 |
| Legacy p btts yes | 0.5051 |
| Legacy p over 2 5 | 0.5221 |
| Legacy goal margin distribution | {"-1": 0.2441186702108952, "-10": 9.14635099131646e-06, "-11": 1.5061847389738306e-06, "-12": 2.277889434732805e-07, "-13": 3.184667180407005e-08, "-14": 4.13862451615721e-09, "-15": 5.002784839980315e-10, "-16": 5.196805224156086e-11, "-2": 0.18754312224497507, "-3": 0.10165188940273534, "-4": 0.04321088997981035, "-5": 0.01504960483923977, "-6": 0.004430311997641736, "-7": 0.0011280897778765838, "-8": 0.0002528935008685066, "-9": 5.0614583594704856e-05, "0": 0.2282170766952081, "1": 0.11415761984347898, "10": 7.543805616694836e-09, "11": 6.110760907746531e-10, "12": 4.545944318246025e-11, "13": 3.1262949334937616e-12, "14": 1.9984640648960868e-13, "15": 1.1883012812631182e-14, "16": 6.071913876737349e-16, "2": 0.045128238792695737, "3": 0.012031980544097596, "4": 0.0025158763914989286, "5": 0.00043101819929898885, "6": 6.241360184670354e-05, "7": 7.817412360243633e-06, "8": 8.620480000468009e-07, "9": 8.486798115123186e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1711 |
| Legacy raw p draw | 0.2458 |
| Legacy raw p away | 0.5831 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9021 |
| Legacy lambda away | 1.8339 |
| Legacy model home team | Konyaspor |
| Legacy model away team | Galatasaray |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 41.6% |
| Market reference home draw last update utc | 2026-10-29T12:07:58Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.8% |
| Market reference draw away last update utc | 2026-10-29T12:07:58Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.6% |
| Market reference home away last update utc | 2026-10-29T12:07:58Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.19 |
| Market reference dc home draw odds | 2.31 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 81.8% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-29T12:07:57Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.67 |
| Market reference over 1 5 last update utc | 2026-10-29T12:07:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.8% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T12:07:57Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.57 |
| Market reference under 3 5 last update utc | 2026-10-29T12:07:57Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.3% |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.13 |
| Market reference btts yes last update utc | 2026-10-29T12:07:58Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,456.7365 |
| Elo away rating | 1,677.5170 |
| Elo rating diff | -160.7805 |
| Elo home expectancy | 0.2838 |

</details>


---

## 2026-10-31 — Erzurum BB vs Çorum FK

The model's most likely 1X2 outcome is **Çorum FK win** at **37.1%**. Expected goals are 1.26 for Erzurum BB and 1.48 for Çorum FK (2.74 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.3%; Double Chance 1X: 62.9%; Double Chance X2: 65.9%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Erzurum BB win | 34.1% | 2.93 |
| Draw | 28.8% | 3.47 |
| Çorum FK win | 37.1% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Erzurum BB expected goals | 1.26 |
| Çorum FK expected goals | 1.48 |
| Expected total goals | 2.74 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.7% |
| Under 3.5 | 74.3% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.75% |
| 2 | 0-0 | 8.85% |
| 3 | 1-0 | 8.69% |
| 4 | 0-1 | 8.64% |
| 5 | 2-1 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Erzurum BB win | 34.1% | 35.4% | 2.70 | -7.8% |
| Draw | 28.8% | 29.2% | 3.24 | -6.7% |
| Çorum FK win | 37.1% | 35.4% | 2.70 | +0.1% |
| Over 2.5 | 47.4% | 47.4% | 2.02 | -4.3% |
| Under 2.5 | 52.6% | 52.6% | 1.83 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T10:30:00+00:00 |
| Fixture id | 7ef8c62daf5d4e448691625fb8c2de1b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:07:57Z |
| Market best draw last update utc | 2026-10-29T12:07:57Z |
| Market best away last update utc | 2026-10-29T12:07:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Erzurumspor |
| Matched away-team name | Corum |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2394 |
| Dc lambda away | 1.5081 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.3508 |
| Shot lambda away | 1.3443 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.3% |
| P btts no | 46.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.30 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.89 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.46 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.19155686705310318, "-10": 5.863913454469768e-07, "-11": 7.296286854715396e-08, "-12": 8.335567394851582e-09, "-13": 8.755425182235782e-10, "-14": 7.755610393471662e-11, "-2": 0.11296260286748623, "-3": 0.04629626543715187, "-4": 0.01487649450043733, "-5": 0.003915983798691509, "-6": 0.0008711966235425287, "-7": 0.00016763465975225492, "-8": 2.8397292118081314e-05, "-9": 4.294575899223827e-06, "0": 0.2879500023014591, "1": 0.19502433632765973, "10": 1.4748738952911423e-07, "11": 1.569366553024476e-08, "12": 1.5332494419689025e-09, "13": 1.3772413229432428e-10, "14": 1.043287354039804e-11, "2": 0.09932550528212761, "3": 0.03481185831147683, "4": 0.009566146101834682, "5": 0.0021534383616918914, "6": 0.0004096971078465308, "7": 6.741642014324149e-05, "8": 9.766387567217375e-06, "9": 1.263084669211968e-06} |
| Raw goal margin distribution | {"-1": 0.2051877440165845, "-10": 1.0317209495884675e-06, "-11": 1.364779755445974e-07, "-12": 1.658369147456306e-08, "-13": 1.8626893543887673e-09, "-14": 1.9335453072778302e-10, "-15": 1.6918522703560332e-11, "-2": 0.12575791232664946, "-3": 0.05412836316275192, "-4": 0.018352737573491117, "-5": 0.005111353625339562, "-6": 0.0012051303187161088, "-7": 0.0002460277501358972, "-8": 4.425181988651149e-05, "-9": 7.109621383791346e-06, "0": 0.27761907653757695, "1": 0.17379491820114007, "10": 2.1583099108344136e-07, "11": 2.441570579404546e-08, "12": 2.537132078796253e-09, "13": 2.437010806783635e-10, "14": 2.1633487207889378e-11, "15": 1.6187872391795442e-12, "2": 0.09196988221950655, "3": 0.033852469930634496, "4": 0.009815704532086127, "5": 0.002337823426597717, "6": 0.00047137326410339446, "7": 8.229438123914143e-05, "8": 1.2658212458456545e-05, "9": 1.7391733567491627e-06} |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 41.0% |
| Raw p over 1 5 | 77.0% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 56.4% |
| P home draw | 62.9% |
| P draw away | 65.9% |
| P home away | 71.2% |
| Raw p home draw | 59.0% |
| Raw p draw away | 68.8% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9391 |
| Totals anchor target over 2 5 | 0.4738 |
| Totals anchor reference over odds | 2.02 |
| Totals anchor reference under odds | 1.83 |
| Totals anchor reference last update utc | 2026-10-29T12:07:57Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5112 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.68, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.69, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:58Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:58Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.70 |
| Reference draw odds | 3.24 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-29T12:07:57Z |
| Market reference home last update utc | 2026-10-29T12:07:57Z |
| Market reference draw last update utc | 2026-10-29T12:07:57Z |
| Market reference away last update utc | 2026-10-29T12:07:57Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-29T12:07:57Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:07:57Z |
| Market best over 2 5 last update utc | 2026-10-29T12:07:57Z |
| Market best under 2 5 last update utc | 2026-10-29T12:07:57Z |
| Home probability edge | -1.2% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0415 |
| Raw ev home | -0.1567 |
| Raw edge prob draw | -0.0148 |
| Raw ev draw | -0.1005 |
| Raw edge prob away | 0.0562 |
| Raw ev away | 0.1071 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.07824916123048668, 0.07871706543772615, 0.06686483263025425, 0.033418574142388795, 0.012526776637795167, 0.003756477036144283, 0.0009387304312922755, 0.00020107323525783575, 3.7685622001431415e-05, 6.278336475822496e-06, 9.413605542169772e-07, 1.2831419979541614e-07, 1.6032634161728998e-08, 1.849153395987261e-09, 1.980415481510079e-10, 1.9795955212376845e-11], [0.0745853640202302, 0.13534261673077871, 0.08286190450688635, 0.04141379841112439, 0.015523744376657857, 0.004655195103419127, 0.0011633169230465326, 0.0002491789863732756, 4.670171581574107e-05, 7.780396615938214e-06, 1.1665762895334445e-06, 1.590127209189259e-07, 1.9868360521430963e-08, 2.291553961769012e-09, 2.4542198351154915e-10, 2.453203703509116e-11], [0.05386787235428, 0.08076835379752588, 0.057428396352452726, 0.02566091975572617, 0.00961886071891485, 0.0028844634537072487, 0.0007208172966031703, 0.00015439689715638933, 2.8937432159822086e-05, 4.820908510910322e-06, 7.228368732921966e-07, 9.852785371515631e-08, 1.2310882473444567e-08, 1.419898308894929e-09, 1.5206897379133763e-10, 1.520060119945143e-11], [0.022251829147578228, 0.03336392418496734, 0.025012582777748826, 0.011856397132636157, 0.003973374777157663, 0.0011915188989124314, 0.00029775639225443747, 6.377852375242753e-05, 1.1953521983476585e-05, 1.9914288022247998e-06, 2.985906423087015e-07, 4.070004756690641e-08, 5.085399543040208e-09, 5.865339245008225e-10, 6.281690134701485e-11, 6.279089298461798e-12], [0.006893866586513751, 0.010336518432182785, 0.007749179067946365, 0.0038729853203526695, 0.001376896554076217, 0.00036914593716921715, 9.224827450677926e-05, 1.9759302973161938e-05, 3.7033353638712202e-06, 6.169670092300168e-07, 9.250673454328886e-08, 1.2609331849986518e-08, 1.5755138939961135e-09, 1.8171479733894473e-10, 1.946138155171156e-11, 1.945332386893373e-12], [0.0017086378363757372, 0.0025618956021245145, 0.0019206261667793327, 0.0009599154806720564, 0.00035981926596587887, 0.0001023363357036507, 2.2863641206953898e-05, 4.897323186729867e-06, 9.178679111483343e-07, 1.5291464703251297e-07, 2.2927700264672718e-08, 3.125210100881847e-09, 3.9048951952213155e-10, 4.5037828084758903e-11, 4.823483664805731e-12, 4.82148657630758e-13], [0.00035290346126970955, 0.0005291360206087416, 0.00039668770504304256, 0.0001982617313298518, 7.431736655219487e-05, 2.2285978980237822e-05, 5.281969871466885e-06, 1.0114971509815712e-06, 1.89577191805446e-07, 3.158311671891526e-08, 4.735506032993017e-09, 6.454834595818524e-10, 8.065202589754783e-11, 9.302149982172342e-12, 9.962462755117867e-13, 9.958337952140576e-14], [6.247626049146182e-05, 9.367558974918087e-05, 7.022760361958662e-05, 3.509926348550442e-05, 1.3156774192718591e-05, 3.945398050410362e-06, 9.859411299058363e-07, 2.002942111650659e-07, 3.356179612368531e-08, 5.5913167305411074e-09, 8.383502599030889e-10, 1.1427315736341054e-10, 1.4278230542171835e-11, 1.6468060226042578e-12, 1.7637044873004016e-13, 1.7629742528494336e-14], [9.677923594413655e-06, 1.4510874900685008e-05, 1.0878650173724965e-05, 5.437073018788114e-06, 2.038058206180334e-06, 6.111643139499093e-07, 1.5272781771441923e-07, 3.271383924289318e-08, 5.815097243906067e-09, 8.661263603915405e-10, 1.2986516313356717e-10, 1.7701553792686337e-11, 2.211778092407549e-12, 2.5509950077377537e-13, 2.7320772941508716e-14, 2.7309461199789716e-15], [1.3325908555776256e-06, 1.9980586755454e-06, 1.4979235577868946e-06, 7.486516829009791e-07, 2.8062814323710277e-07, 8.415358605384456e-08, 2.1029685892130893e-08, 4.504495473706735e-09, 8.442432107465453e-10, 1.3339529777318706e-10, 1.788163826275516e-11, 2.4373956338387896e-12, 3.04548308503958e-13, 3.512564019308588e-14, 3.761903246496225e-15, 3.760345688882927e-16], [1.6514064550527415e-07, 2.47608407378689e-07, 1.8562941672240446e-07, 9.277627987270523e-08, 3.4776700235597646e-08, 1.0428690444894014e-08, 2.606093151895678e-09, 5.582173156074038e-10, 1.046224114495346e-10, 1.7429849027493113e-11, 2.4786150299003643e-12, 3.0205301697751854e-13, 3.774099457712609e-14, 4.3529271351316925e-15, 4.661919507060466e-16, 4.6599893116925845e-17], [1.8604518806867325e-08, 2.78952238422016e-08, 2.091275569350666e-08, 1.0452048545903288e-08, 3.917895389074885e-09, 1.1748819736012949e-09, 2.9359888299178776e-10, 6.288799777160407e-11, 1.1786617494906869e-11, 1.9636229048317325e-12, 2.9442148458973583e-13, 3.8062057987087956e-14, 4.2518487271965714e-15, 4.903948056076495e-16, 5.252054627728707e-17, 5.249880096079469e-18], [1.9212962929954375e-09, 2.8807512151572997e-09, 2.159668863643086e-09, 1.079387343145894e-09, 4.046026648426379e-10, 1.2133054361793625e-10, 3.032007714768227e-11, 6.494469340851137e-12, 1.217208826253586e-12, 2.0278414330724616e-13, 3.0405027552320874e-14, 4.144423475847478e-15, 4.911321139052994e-16, 5.064327284672428e-17, 5.4238183699435346e-18, 5.421572722184487e-19], [1.8315051390544385e-10, 2.746120249194923e-10, 2.0587374455666861e-10, 1.0289425286507415e-10, 3.8569369161645057e-11, 1.1566020034008705e-11, 2.8903078257612077e-12, 6.190952440061048e-13, 1.160322969816482e-13, 1.9330709268529e-14, 2.8984058532870813e-15, 3.9507352000343133e-16, 4.936374324354252e-17, 5.399831225096461e-18, 5.170337992149054e-19, 5.168197294003642e-20], [1.621202463519689e-11, 2.4307968447277086e-11, 1.8223428082850376e-11, 9.107941477739848e-12, 3.414063928509716e-12, 1.0237951165091247e-12, 2.5584280751040965e-13, 5.480075995059424e-14, 1.0270888227570784e-14, 1.7111059543027904e-15, 2.565596246186256e-16, 3.4970918194181517e-17, 4.369554878579341e-18, 5.039706614129044e-19, 5.119088909886258e-20, 4.574758763341615e-21], [1.3393779503528785e-12, 2.008235102571506e-12, 1.5055527180128039e-12, 7.52464683646282e-13, 2.820574264989392e-13, 8.458219350063455e-14, 2.1136793389264227e-14, 4.527437577479083e-15, 8.485430741747816e-16, 1.4136529134893238e-16, 2.1196014186837878e-17, 2.889168859957889e-18, 3.6099658055786933e-19, 4.1636205638112304e-20, 4.459175015766129e-21, 4.2274522659759335e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2392449251326463, "lambda_away": 1.4993789482964148, "rho": -0.09475376269082486, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-29T12:07:57Z", "over": 2.02, "under": 1.83, "bookmaker": "pinnacle", "event_id": "7ef8c62daf5d4e448691625fb8c2de1b", "kickoff_utc": "2026-10-31T10:30:00Z", "home_team": "Erzurum BB", "away_team": "\u00c7orum FK"}} |
| Legacy p home | 0.3281 |
| Legacy p draw | 0.2844 |
| Legacy p away | 0.3875 |
| Legacy p over 1 5 | 0.7684 |
| Legacy p under 3 5 | 0.7069 |
| Legacy p btts yes | 0.5655 |
| Legacy p over 2 5 | 0.5124 |
| Legacy goal margin distribution | {"-1": 0.191606319999134, "-10": 1.113290635064058e-06, "-11": 1.4966722085947593e-07, "-12": 1.8482536186587808e-08, "-13": 2.1097759806982616e-09, "-14": 2.2257358518609908e-10, "-15": 1.9795955212376845e-11, "-2": 0.11918635155774876, "-3": 0.05214524797537014, "-4": 0.017970428663607364, "-5": 0.005086784933060775, "-6": 0.0012189339928987707, "-7": 0.0002529074595294167, "-8": 4.6231177103826835e-05, "-9": 7.548712656478519e-06, "0": 0.2843612925512265, "1": 0.18462241067774451, "10": 1.9530193111010592e-07, "11": 2.1700533765485532e-08, "12": 2.214884210681426e-09, "13": 2.0896403507073374e-10, "14": 1.8220259737768395e-11, "15": 1.3393779503528785e-12, "2": 0.0960193111913984, "3": 0.03472102501627241, "4": 0.009889674039176996, "5": 0.0023137298906676525, "6": 0.0004582423354073102, "7": 7.858187740169625e-05, "8": 1.1872480164282485e-05, "9": 1.6022310202940388e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3024 |
| Legacy raw p draw | 0.2763 |
| Legacy raw p away | 0.4212 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2392 |
| Legacy lambda away | 1.4994 |
| Legacy model home team | Erzurumspor |
| Legacy model away team | Corum |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 63.8% |
| Market reference home draw last update utc | 2026-10-29T12:07:58Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.3% |
| Market reference draw away last update utc | 2026-10-29T12:07:58Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market reference home away last update utc | 2026-10-29T12:07:58Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home draw odds | 1.51 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 74.4% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-29T12:07:57Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.46 |
| Market reference over 1 5 last update utc | 2026-10-29T12:07:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 74.8% |
| Market under 3 5 odds | 1.30 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T12:07:57Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.46 |
| Market reference under 3 5 last update utc | 2026-10-29T12:07:57Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.6% |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 1.98 |
| Market reference btts yes last update utc | 2026-10-29T12:07:58Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,438.6446 |
| Elo away rating | 1,451.6385 |
| Elo rating diff | 47.0060 |
| Elo home expectancy | 0.5672 |

</details>


---

## 2026-10-31 — Fenerbahce vs Goztepe

The model's most likely 1X2 outcome is **Fenerbahce win** at **72.2%**. Expected goals are 2.45 for Fenerbahce and 1.04 for Goztepe (3.49 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 69.0%; Under 3.5 goals: 53.1%; Double Chance 1X: 88.6%; Double Chance X2: 27.8%; Double Chance 12 (either team wins): 83.6%; Under 4.5 goals: 71.9%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 72.2% | 1.39 |
| Draw | 16.4% | 6.08 |
| Goztepe win | 11.4% | 8.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 2.45 |
| Goztepe expected goals | 1.04 |
| Expected total goals | 3.49 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 87.5% |
| Under 1.5 | 12.5% |
| Over 2.5 | 69.0% |
| Under 2.5 | 31.0% |
| Over 3.5 | 46.9% |
| Under 3.5 | 53.1% |
| Over 4.5 | 28.1% |
| Under 4.5 | 71.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.17% |
| 2 | 2-0 | 9.76% |
| 3 | 3-1 | 8.31% |
| 4 | 3-0 | 7.97% |
| 5 | 1-1 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 72.2% | 74.2% | 1.32 | -4.7% |
| Draw | 16.4% | 15.4% | 5.69 | -6.5% |
| Goztepe win | 11.4% | 10.5% | 8.12 | -7.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T16:00:00+00:00 |
| Fixture id | dc20aff5555a04cd21c2355e222a3297 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:07:57Z |
| Market best draw last update utc | 2026-10-29T12:07:57Z |
| Market best away last update utc | 2026-10-29T12:07:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Fenerbahce |
| Matched away-team name | Goztep |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5517 |
| Dc lambda away | 1.0229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 2.0453 |
| Shot lambda away | 1.1229 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.41 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.01 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.88 |
| Fair Over 4.5 odds | 3.56 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.07245622762873657, "-10": 1.3494869242312112e-08, "-11": 1.2555488331831385e-09, "-12": 1.0738545403537831e-10, "-13": 8.497126843424465e-12, "-14": 6.254597475926251e-13, "-15": 4.3032595968658e-14, "-16": 2.777960955615585e-15, "-17": 1.6763183913716087e-16, "-18": 8.50512487130064e-18, "-2": 0.030235509104321795, "-3": 0.008829603478570083, "-4": 0.0020586974901933633, "-5": 0.0003974237585427326, "-6": 6.527660556345106e-05, "-7": 9.314651637167492e-06, "-8": 1.1737766339275304e-06, "-9": 1.3234404969399834e-07, "0": 0.16435455167025548, "1": 0.2272413187103601, "10": 8.79757013442038e-05, "11": 1.9231422931597017e-05, "12": 3.864621992161698e-06, "13": 7.184845237148813e-07, "14": 1.2425916613185814e-07, "15": 2.0086782116396554e-08, "16": 3.0466510394190505e-09, "17": 4.3195334249256447e-10, "18": 5.1492594725570495e-11, "2": 0.21224688106221123, "3": 0.1456293748672527, "4": 0.07977817052867761, "5": 0.036185045016312846, "6": 0.013964217572804614, "7": 0.004681762885931847, "8": 0.0013861556847775507, "9": 0.00036721018935830066} |
| Raw goal margin distribution | {"-1": 0.08619762396699969, "-10": 1.605418474714115e-08, "-11": 1.4936649303558637e-09, "-12": 1.277512132414128e-10, "-13": 1.0108615483024598e-11, "-14": 7.440788168786939e-13, "-15": 5.119377101215626e-14, "-16": 3.3048040407804864e-15, "-17": 1.9942338578376156e-16, "-18": 1.0118130344919985e-17, "-2": 0.03596970377176358, "-3": 0.010504146645935008, "-4": 0.0024491315367778537, "-5": 0.00047279557348679335, "-6": 7.765637936647061e-05, "-7": 1.1081184674948859e-05, "-8": 1.396384551386838e-06, "-9": 1.574432316328433e-07, "0": 0.1892369680805948, "1": 0.21259368085023486, "10": 8.230491831454309e-05, "11": 1.7991793975755637e-05, "12": 3.615514199051186e-06, "13": 6.721720785521504e-07, "14": 1.162496048573943e-07, "15": 1.8792017978052367e-08, "16": 2.850268438909393e-09, "17": 4.0411027165839903e-10, "18": 4.8173458556590123e-11, "2": 0.1985657623801685, "3": 0.1362423216809842, "4": 0.07463578815878465, "5": 0.03385261076377779, "6": 0.013064104850491346, "7": 0.004379983404588879, "8": 0.0012968061483305518, "9": 0.0003435403660057785} |
| Unadjusted home-win probability | 67.5% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.8% |
| Raw p btts yes | 59.9% |
| P home draw | 88.6% |
| P draw away | 27.8% |
| P home away | 83.6% |
| Raw p home draw | 86.4% |
| Raw p draw away | 32.5% |
| Raw p home away | 81.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6897 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:59Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:59Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.32 |
| Reference draw odds | 5.69 |
| Reference away odds | 8.12 |
| Market reference 1x2 last update utc | 2026-10-29T12:07:57Z |
| Market reference home last update utc | 2026-10-29T12:07:57Z |
| Market reference draw last update utc | 2026-10-29T12:07:57Z |
| Market reference away last update utc | 2026-10-29T12:07:57Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.71 |
| Market reference over 2 5 last update utc | 2026-10-29T12:07:12Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:07:12Z |
| Home probability edge | -2.0% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | -0.0664 |
| Raw ev home | -0.1089 |
| Raw edge prob draw | 0.0355 |
| Raw ev draw | 0.0768 |
| Raw edge prob away | 0.0309 |
| Raw ev away | 0.1018 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.031769449017471495, 0.019739816437929308, 0.01357877559239972, 0.004718330903927164, 0.0012296384733363724, 0.0002563636685761956, 4.454041573395774e-05, 6.632927729263159e-06, 8.642996106921153e-07, 1.0010847530964381e-07, 1.0435659156107594e-08, 9.889543380146229e-10, 8.591006206478233e-11, 6.8888974455350455e-12, 5.129449078727663e-13, 3.564745281132409e-14, 2.322509821045167e-15, 1.4241563701523598e-16, 8.24772573392129e-18], [0.06516121696601289, 0.07401424568927827, 0.03472196177767754, 0.0120651309233133, 0.003144279083266144, 0.0006555413955342302, 0.00011389323007458555, 1.6960900599791967e-05, 2.2100798295621315e-06, 2.5598498404146144e-07, 2.6684774034122065e-08, 2.528831446602001e-09, 2.196785616665538e-10, 1.7615434629326265e-11, 1.3116391359454636e-12, 9.115324762264641e-14, 5.9388342259480155e-15, 3.6416761373937123e-16, 2.109006189381853e-17], [0.09244202191243384, 0.09636481121061058, 0.045053814039113384, 0.015425728627419078, 0.004020080360140332, 0.0008381345992699462, 0.00014561682511343114, 2.1685156306382706e-05, 2.82567109403532e-06, 3.2728653519106527e-07, 3.4117498214542765e-08, 3.2332071560358593e-09, 2.808673937372749e-10, 2.252200294991954e-11, 1.676980506618558e-12, 1.1654289292608318e-13, 7.593025364994927e-15, 4.65602140593733e-16, 2.6964446020298593e-17], [0.07879375990501243, 0.08213738341869194, 0.04281144701688508, 0.013343867942476472, 0.003426550394968676, 0.0007143913018855912, 0.00012411776504614309, 1.848353123567891e-05, 2.4084852878364624e-06, 2.7896551958173457e-07, 2.9080345791471623e-08, 2.75585218827404e-09, 2.393997613795676e-10, 1.91968247373141e-11, 1.4293888933871963e-12, 9.933634654326224e-14, 6.47198108809007e-15, 3.9686002662245895e-16, 2.2983379655062515e-17], [0.05037040897252656, 0.05250788386948828, 0.027368031396721983, 0.009509799130274998, 0.0022230766406438804, 0.00045668822106944277, 7.934464091657695e-05, 1.1815948734011223e-05, 1.5396700081184788e-06, 1.7833401182409437e-07, 1.8590163895526138e-08, 1.7617309030377306e-09, 1.5304084870618016e-10, 1.2271935165400246e-11, 9.137640243021336e-13, 6.35026480174662e-14, 4.137336949811125e-15, 2.5370031674994844e-16, 1.4692562383010485e-17], [0.025760193224622942, 0.026853330395467584, 0.013996427492610507, 0.004863455908345931, 0.0012674593240799897, 0.00023703206999258917, 4.057805610560289e-05, 6.042855889583625e-06, 7.874106587643884e-07, 9.120272590235502e-08, 9.50729255121515e-09, 9.009759777172805e-10, 7.826741760389046e-11, 6.276054285625916e-12, 4.673128193295136e-13, 3.2476219998479294e-14, 2.1158970402769147e-15, 1.2974620047638068e-16, 7.513999859671817e-18], [0.01097846216502248, 0.011444334643798236, 0.005964988241090883, 0.002072704432589223, 0.0005401649791126828, 0.00011261739013905276, 1.755081510616982e-05, 2.5753403390260527e-06, 3.3557815541994223e-07, 3.886871759598673e-08, 4.051811671410448e-09, 3.839773481787648e-10, 3.335595643347132e-11, 2.6747246777058996e-12, 1.9915906924701044e-13, 1.38406940276928e-14, 9.017516056346725e-16, 5.5295150178603376e-17, 3.2023115062871853e-18], [0.004010394657852765, 0.004180576280017976, 0.0021789897907961184, 0.0007571518359144012, 0.00019732041829086344, 4.113874721305769e-05, 7.1474125558442135e-06, 9.547592917443717e-07, 1.2258555174293537e-07, 1.4198609519388344e-08, 1.4801129372582454e-09, 1.4026561122364956e-10, 1.2184816732762225e-11, 9.770677711924086e-13, 7.275212642402945e-14, 5.055958162016421e-15, 3.2940677551991535e-16, 2.019912912647755e-17, 1.1697934341397144e-18], [0.0012818605134518337, 0.0013362564321032823, 0.0006964803243408776, 0.00024201185268531386, 6.307041433181139e-05, 1.3149363123660776e-05, 2.284559678122062e-06, 3.4021503815060723e-07, 3.976551416846336e-08, 4.538365532974796e-09, 4.730951668323842e-10, 4.483372928664614e-11, 3.894687871377201e-12, 3.1230457391655587e-13, 2.3254089955962365e-14, 1.6160586871077217e-15, 1.0528977181227185e-16, 6.4563386505231585e-18, 3.7390634589608764e-19], [0.0003642016456697405, 0.00037965659016851993, 0.0001978836836298832, 6.876030121422884e-05, 1.7919538398809736e-05, 3.7359912711955173e-06, 6.49088091622577e-07, 9.666174710568505e-08, 1.259545012433659e-08, 1.3086221470074562e-09, 1.3441559086235876e-10, 1.2738139459291267e-11, 1.1065570061955529e-12, 8.873183827490655e-14, 6.606941817489654e-15, 4.591538838797598e-16, 2.99148836896143e-17, 1.8343720996520433e-18, 1.0623410665409445e-19], [9.312913034213511e-05, 9.708107717645135e-05, 5.0600362695945824e-05, 1.7582531903085323e-05, 4.582162236375367e-06, 9.553213781130203e-07, 1.6597676097010864e-07, 2.471714379200503e-08, 3.2207523779584677e-09, 3.7304726962579585e-10, 3.4882447446063114e-11, 3.2572391259768355e-12, 2.8295504121482476e-13, 2.2689405801571845e-14, 1.6894452647307706e-15, 1.1740913970968491e-16, 7.649463244947029e-18, 4.690628952275071e-19, 2.716486892083102e-20], [2.164893347458491e-05, 2.2567608799876765e-05, 1.176263411641437e-05, 4.087261011525239e-06, 1.0651761168671002e-06, 2.2207540095819385e-07, 3.858319994365131e-08, 5.745783297546451e-09, 7.487007954694433e-10, 8.671911241235411e-11, 9.039904929691083e-12, 7.684476041277015e-13, 6.57761415902183e-14, 5.274412366694805e-15, 3.9273091041161777e-16, 2.7293099866231822e-17, 1.7782053831894938e-18, 1.0903904478513229e-19, 6.314785051169061e-21], [4.6131640976326276e-06, 4.808924319862172e-06, 2.506495826371044e-06, 8.709531016000026e-07, 2.269780276130327e-07, 4.732197398409499e-08, 8.221681357226592e-09, 1.2243670688043778e-09, 1.595404057009718e-10, 1.8478947077410725e-11, 1.926310361506744e-12, 1.8255032670932595e-13, 1.422474374379619e-14, 1.1239227925343579e-15, 8.368690023775818e-17, 5.815877653456396e-18, 3.789171989270074e-19, 2.3235094109067796e-20, 1.3456154649151319e-21], [9.074008770989566e-07, 9.459065520744754e-07, 4.930231102034996e-07, 1.7131487013641357e-07, 4.4646159767858934e-08, 9.308145080132235e-09, 1.6171895724680675e-09, 2.408307462321375e-10, 3.138130380839398e-11, 3.6347748380580168e-12, 3.789016984011101e-13, 3.590731286921907e-14, 3.11925369918197e-15, 2.2436258205149105e-16, 1.6461059062781686e-17, 1.1439724172298064e-18, 7.453231477950072e-20, 4.570300194797865e-21, 2.646800823167134e-22], [1.6573521752630222e-07, 1.7276821317257903e-07, 9.00498274547734e-08, 3.1290367889353855e-08, 8.154544686464082e-09, 1.7001167714915684e-09, 2.953769081986829e-10, 4.398732370792293e-11, 5.7317414432870985e-12, 6.638854046192194e-13, 6.920574686500438e-14, 6.55840925368206e-15, 5.69726350724332e-16, 4.5684827921545257e-17, 3.0513149765066207e-18, 2.089446045278566e-19, 1.3613199760410044e-20, 8.347575102274458e-22, 4.8343364134588745e-23], [2.825317029509057e-08, 2.9452097274188147e-08, 1.5350950438276473e-08, 5.334123343058629e-09, 1.390119391305788e-09, 2.898218579214638e-10, 5.0353414398785323e-11, 7.498595446969451e-12, 9.770999157672611e-13, 1.1317369761894568e-13, 1.1797623828898018e-14, 1.1180234127352604e-15, 9.712224021463948e-17, 7.787971937614805e-18, 5.798896818597142e-19, 3.614907635749294e-20, 2.320665799536013e-21, 1.4230256214445772e-22, 8.241177221825823e-24], [4.515344058494483e-09, 4.706953274561031e-09, 2.4533467263940804e-09, 8.524849386032164e-10, 2.2216506213539018e-10, 4.631853312457864e-11, 8.04734435660743e-12, 1.1984049239391294e-12, 1.561574242159226e-13, 1.8087109438842512e-14, 1.8854638295024944e-15, 1.7867943035154167e-16, 1.5521809613594033e-17, 1.244652279689168e-18, 9.267637586223391e-20, 6.4406073333960846e-21, 3.7640026666942083e-22, 2.2742404543506086e-23, 1.317082303150858e-24], [6.791810660916453e-10, 7.080022035188678e-10, 3.690231848423862e-10, 1.2822757732899147e-10, 3.3417232838673464e-11, 6.967059497530634e-12, 1.210451263186703e-12, 1.8025956013678367e-13, 2.3488612270325675e-14, 2.7205949562313576e-15, 2.8360437592561035e-16, 2.6876287703150278e-17, 2.334732207438324e-18, 1.8721591340141256e-19, 1.3940031799173465e-20, 9.687719248645973e-22, 6.311761801774818e-23, 3.471720567166466e-24, 1.9811056504134884e-25], [9.648431298980046e-11, 1.0057863743887891e-10, 5.2423352540898754e-11, 1.821598145562091e-11, 4.747244753175356e-12, 9.897389411141253e-13, 1.719564404353495e-13, 2.5607633498567483e-14, 3.3367870971838443e-15, 3.864871215948753e-16, 4.028877531811427e-17, 3.8180395246836465e-18, 3.3167154429986848e-19, 2.6595851514588428e-20, 1.9803178538810105e-21, 1.376235267455979e-22, 8.966474944655405e-24, 5.49821675436273e-25, 2.8562251220797603e-26]] |
| Legacy trial inputs | {"lambda_home": 2.5570760442577782, "lambda_away": 1.0424351308747077, "rho": -0.09475376269082486, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7177 |
| Legacy p draw | 0.1667 |
| Legacy p away | 0.1156 |
| Legacy p over 1 5 | 0.8833 |
| Legacy p under 3 5 | 0.5113 |
| Legacy p btts yes | 0.5994 |
| Legacy p over 2 5 | 0.7033 |
| Legacy goal margin distribution | {"-1": 0.0738140261171657, "-10": 1.3265501983753127e-08, "-11": 1.2326499665344848e-09, "-12": 1.0530608383273221e-10, "-13": 8.323812669811293e-12, "-14": 6.121027334494131e-13, "-15": 4.20748725575209e-14, "-16": 2.7136418808048366e-15, "-17": 1.635056989090545e-16, "-18": 8.24772573392129e-18, "-2": 0.030464115937431663, "-3": 0.00883750610569608, "-4": 0.002050915294016153, "-5": 0.00039453877803057133, "-6": 6.462547844398522e-05, "-7": 9.201217187251723e-06, "-8": 1.157317466361564e-06, "-9": 1.302786096858294e-07, "0": 0.16666003208317565, "1": 0.2152348516433196, "10": 0.00011838300243600442, "11": 2.698360894652326e-05, "12": 5.654683904583008e-06, "13": 1.0964069326201951e-06, "14": 1.977736363489666e-07, "15": 3.334736273594961e-08, "16": 5.27576961455425e-09, "17": 7.797597035305242e-10, "18": 9.648431298980046e-11, "2": 0.20739458089337895, "3": 0.14758192005391566, "4": 0.08401285773639224, "5": 0.03964444421130371, "6": 0.01592909177659183, "7": 0.005563231465752237, "8": 0.0017164413165349397, "9": 0.00047396270791643996} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6939 |
| Legacy raw p draw | 0.1796 |
| Legacy raw p away | 0.1265 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.5571 |
| Legacy lambda away | 1.0424 |
| Legacy model home team | Fenerbahce |
| Legacy model away team | Goztep |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,643.4256 |
| Elo away rating | 1,515.6231 |
| Elo rating diff | 187.8026 |
| Elo home expectancy | 0.7467 |

</details>


---

## 2026-10-31 — Kocaelispor vs Çaykur Rizespor

The model's most likely 1X2 outcome is **Kocaelispor win** at **38.8%**. Expected goals are 1.18 for Kocaelispor and 0.89 for Çaykur Rizespor (2.07 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.2%; Double Chance 1X: 66.9%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Kocaelispor win | 38.8% | 2.58 |
| Draw | 28.2% | 3.55 |
| Çaykur Rizespor win | 33.1% | 3.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Kocaelispor expected goals | 1.18 |
| Çaykur Rizespor expected goals | 0.89 |
| Expected total goals | 2.07 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 27.8% |
| Under 3.5 | 72.2% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.45% |
| 2 | 1-2 | 8.35% |
| 3 | 0-0 | 8.18% |
| 4 | 0-1 | 8.13% |
| 5 | 1-0 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Kocaelispor win | 38.8% | 37.7% | 2.54 | -1.6% |
| Draw | 28.2% | 26.4% | 3.57 | +0.6% |
| Çaykur Rizespor win | 33.1% | 35.9% | 2.66 | -12.1% |
| Over 2.5 | 49.7% | 49.7% | 1.93 | -4.0% |
| Under 2.5 | 50.3% | 50.3% | 1.91 | -4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T13:00:00+00:00 |
| Fixture id | 7d597f0fe7ec1c85b6e7f9f2ce731746 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:07:57Z |
| Market best draw last update utc | 2026-10-29T12:07:57Z |
| Market best away last update utc | 2026-10-29T12:07:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Kocaelispor |
| Matched away-team name | Rizespor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1503 |
| Dc lambda away | 0.8781 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.2856 |
| Shot lambda away | 0.9314 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.23 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.10 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.60 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.59 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.19309196673494672, "-10": 1.0863645250265927e-07, "-11": 1.1215642337149177e-08, "-12": 1.0635080555955036e-09, "-13": 9.321280293488874e-11, "-14": 7.554504756007445e-12, "-15": 5.188064846594072e-13, "-2": 0.09470995629983732, "-3": 0.032004570166105514, "-4": 0.008500127828099741, "-5": 0.0018519432439245093, "-6": 0.00034130153867941994, "-7": 5.443356577135719e-05, "-8": 7.645931009929229e-06, "-9": 9.590602688489203e-07, "0": 0.2818592853255185, "1": 0.1878867140281043, "10": 1.3053727990245393e-06, "11": 1.7853424009566324e-07, "12": 2.2427276455522568e-08, "13": 2.6040523149263387e-09, "14": 2.7958799583934123e-10, "15": 2.5436438456059578e-11, "2": 0.11996306197514159, "3": 0.05370346275624787, "4": 0.018895314821386594, "5": 0.005453743807692118, "6": 0.0013315077265178827, "7": 0.00028132648104511735, "8": 5.234950615385905e-05, "9": 8.69894326740013e-06} |
| Raw goal margin distribution | {"-1": 0.16997288406538869, "-10": 1.1798721033221123e-08, "-11": 9.457494598578259e-10, "-12": 6.938770222116457e-11, "-13": 4.390289101195243e-12, "-2": 0.06992704097920391, "-3": 0.0191280593146882, "-4": 0.00404529330388577, "-5": 0.0006953683844720118, "-6": 0.00010054079239601374, "-7": 1.2534066887938114e-05, "-8": 1.3727189193791626e-06, "-9": 1.3401102945761177e-07, "0": 0.3236699874813781, "1": 0.22930793307814307, "10": 1.9643495852103954e-07, "11": 2.085923290175425e-08, "12": 2.0274171784119793e-09, "13": 1.699386328864499e-10, "2": 0.12272185759849802, "3": 0.04447193884427038, "4": 0.012459584340964617, "5": 0.0028373104952913292, "6": 0.0005434662909457884, "7": 8.975542353815835e-05, "8": 1.3022329999920517e-05, "9": 1.6841703037576475e-06} |
| Unadjusted home-win probability | 41.2% |
| Unadjusted draw probability | 32.4% |
| Unadjusted away-win probability | 26.4% |
| Raw p over 1 5 | 62.4% |
| Raw p under 3 5 | 84.5% |
| Raw p btts yes | 42.0% |
| P home draw | 66.9% |
| P draw away | 61.2% |
| P home away | 71.8% |
| Raw p home draw | 73.6% |
| Raw p draw away | 58.8% |
| Raw p home away | 67.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.2946 |
| Totals anchor target over 2 5 | 0.4972 |
| Totals anchor reference over odds | 1.93 |
| Totals anchor reference under odds | 1.91 |
| Totals anchor reference last update utc | 2026-10-29T12:07:57Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3536 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:58Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:58Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.54 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.66 |
| Market reference 1x2 last update utc | 2026-10-29T12:07:57Z |
| Market reference home last update utc | 2026-10-29T12:07:57Z |
| Market reference draw last update utc | 2026-10-29T12:07:57Z |
| Market reference away last update utc | 2026-10-29T12:07:57Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-29T12:07:57Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:07:57Z |
| Market best over 2 5 last update utc | 2026-10-29T12:07:57Z |
| Market best under 2 5 last update utc | 2026-10-29T12:07:57Z |
| Home probability edge | +1.1% |
| Draw probability edge | +1.8% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0355 |
| Raw ev home | 0.0476 |
| Raw edge prob draw | 0.0597 |
| Raw ev draw | 0.1555 |
| Raw edge prob away | -0.0953 |
| Raw ev away | -0.2981 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.12854237921964382, 0.11967724501339246, 0.05934748746952753, 0.017459045225233626, 0.0038521208711649055, 0.0006799379926969961, 0.00010001323283438688, 1.2609528073888171e-05, 1.3910676569747673e-06, 1.364096677047053e-07, 1.2038837661855756e-08, 9.65898030057946e-10, 7.103778992499271e-11, 4.822647245971627e-12], [0.13231810116892498, 0.13157872651641112, 0.06898829443114958, 0.020295210527718106, 0.004477885419846174, 0.000790391715558142, 0.00011626005831051449, 1.4657905035085204e-05, 1.6170420886360166e-06, 1.5856897604468047e-07, 1.3994507815539191e-08, 1.1228050340348373e-09, 8.257764862581406e-11, 5.606070658231218e-12], [0.0839245611401396, 0.07406763643730949, 0.030826322592541575, 0.01179605084501086, 0.0026026516955070605, 0.00045939414382845, 6.757306396017716e-05, 8.519517096856959e-06, 9.398626671066946e-07, 9.216399609699778e-08, 8.133935123143704e-09, 6.526005360929978e-10, 4.799605998278185e-11, 3.2583793321534088e-12], [0.03251927801725272, 0.02869989462755335, 0.0126645485670941, 0.0035139185245329743, 0.001008481342272855, 0.00017800707778154847, 2.618336305303134e-05, 3.3011616776024095e-06, 3.6418010358902197e-07, 3.571191283627462e-08, 3.1517555057824024e-09, 2.528711259148452e-10, 1.859762144846438e-11, 1.2625641641548974e-12], [0.009450482329578647, 0.008340524869419464, 0.003680465857265198, 0.0010827319334270867, 0.00022531192749291693, 5.173093763711347e-05, 7.6091913765839386e-06, 9.59356172812701e-07, 1.0583499522733042e-07, 1.0378299328650906e-08, 9.159369927815247e-10, 7.348730515637663e-11, 5.404686191915451e-12, 3.669159049894894e-13], [0.0021971365099629843, 0.0019390832196469281, 0.0008556691210733283, 0.00025172364525668904, 5.553968703039585e-05, 9.246058826445106e-06, 1.7690559700283012e-06, 2.2304009465717106e-07, 2.4605509426532468e-08, 2.4128440825643977e-09, 2.1294559764080484e-10, 1.7085015933262426e-11, 1.2565319888471442e-12, 8.530404087581209e-14], [0.0004256757023133822, 0.00037568016717413996, 0.00016577829934968398, 4.8769222575674654e-05, 1.0760321525642254e-05, 1.8993047372127149e-06, 2.634915119345763e-07, 4.321203917312997e-08, 4.767099112150392e-09, 4.674671304040147e-10, 4.1256319950652334e-11, 3.310070231616757e-12, 2.4344192288750877e-13, 1.6526900966473187e-14], [7.068933432934908e-05, 6.238688464940288e-05, 2.7529778100074366e-05, 8.098803527893832e-06, 1.7869001253386888e-06, 3.1540580501187156e-07, 4.6393574932982117e-08, 5.516746491627565e-09, 7.916427014475342e-10, 7.762937863148966e-11, 6.851182198891914e-12, 5.496829158553243e-13, 4.0426896304515066e-14, 2.7445203508162228e-15], [1.0271573443524269e-05, 9.065178978817514e-06, 4.000237664162535e-06, 1.1768034885412245e-06, 2.596470322969028e-07, 4.583030695407547e-08, 6.741257599223459e-09, 8.499282999028686e-10, 8.843323890695487e-11, 1.128000244384027e-11, 9.955168173321853e-13, 7.98721404639732e-14, 5.874264320426088e-15, 3.98794848163559e-16], [1.3266841392904149e-06, 1.170865324300269e-06, 5.166737006375991e-07, 1.5199682228758854e-07, 3.3536205670543924e-08, 5.919476861952057e-09, 8.707058937887653e-10, 1.0977737745973977e-10, 1.2110505512730668e-11, 1.120064391746611e-12, 1.285816996990022e-13, 1.0316345641429967e-14, 7.587243908402538e-16, 5.150864205939929e-17], [1.5421996772061834e-07, 1.3610686008152492e-07, 6.00605668482937e-08, 1.7668821336302398e-08, 3.898405357246189e-09, 6.881076689900466e-10, 1.0121492437987245e-10, 1.2761035657930035e-11, 1.407781787647386e-12, 1.3804867426171441e-13, 1.149093766443096e-14, 1.1992202549937922e-15, 8.819767086897828e-17, 5.9876053994149345e-18], [1.6297500142292146e-08, 1.4383361664061797e-08, 6.347019203955837e-09, 1.867187644366395e-09, 4.1197169733253717e-10, 7.271713902568982e-11, 1.0696087341111047e-11, 1.3485476850032117e-12, 1.487701250597018e-13, 1.4588566718541346e-14, 1.28751421654268e-15, 9.742772832239393e-17, 9.320463327686437e-18, 6.327520443120143e-19], [1.5787480176048682e-09, 1.3933243451678053e-09, 6.148393249552691e-10, 1.8087551871775326e-10, 3.990793034480569e-11, 7.044150212018907e-12, 1.0361360048150682e-12, 1.3063457375402246e-13, 1.441144580249713e-14, 1.413202674367594e-15, 1.247222272899431e-16, 1.000669309010563e-17, 6.9411681025094755e-19, 6.129504690113309e-20], [1.4117003965194997e-10, 1.245896437316038e-10, 5.497830617402376e-11, 1.6173704647427147e-11, 3.568526481984484e-12, 6.298807369232034e-13, 9.265022616241554e-14, 1.168121052322775e-14, 1.2886568044385899e-15, 1.2636714368096623e-16, 1.1152534524611834e-17, 8.947883034926888e-19, 6.580796476729633e-20, 4.213648806275771e-21]] |
| Legacy trial inputs | {"lambda_home": 1.1624467584507634, "lambda_away": 0.8825501787686354, "rho": -0.09475376269082486, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-29T12:07:57Z", "over": 1.93, "under": 1.91, "bookmaker": "pinnacle", "event_id": "7d597f0fe7ec1c85b6e7f9f2ce731746", "kickoff_utc": "2026-10-31T13:00:00Z", "home_team": "Kocaelispor", "away_team": "\u00c7aykur Rizespor"}} |
| Legacy p home | 0.3933 |
| Legacy p draw | 0.2947 |
| Legacy p away | 0.3120 |
| Legacy p over 1 5 | 0.6195 |
| Legacy p under 3 5 | 0.8484 |
| Legacy p btts yes | 0.4094 |
| Legacy p over 2 5 | 0.3446 |
| Legacy goal margin distribution | {"-1": 0.20152361564052457, "-10": 1.3210901320037532e-08, "-11": 1.0517340580159134e-09, "-12": 7.664386058322393e-11, "-13": 4.822647245971627e-12, "-2": 0.08243119384773989, "-3": 0.022423492588042476, "-4": 0.004713495102012065, "-5": 0.0008050923428037788, "-6": 0.00011564764571761021, "-7": 1.4321960674491013e-05, "-8": 1.558028929258739e-06, "-9": 1.5107574059369098e-07, "0": 0.2946961739372722, "1": 0.22019050435427634, "10": 1.6923434241428285e-07, "11": 1.7745802793633974e-08, "12": 1.703337661336472e-09, "13": 1.4117003965194997e-10, "2": 0.11656772785000295, "3": 0.04176607484437061, "4": 0.011563708321190323, "5": 0.00260155749386709, "6": 0.0004922187936195487, "7": 8.028927493863825e-05, "8": 1.150440706012828e-05, "9": 1.4693224626210954e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4096 |
| Legacy raw p draw | 0.3255 |
| Legacy raw p away | 0.2649 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1624 |
| Legacy lambda away | 0.8826 |
| Legacy model home team | Kocaelispor |
| Legacy model away team | Rizespor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,459.3997 |
| Elo away rating | 1,449.0338 |
| Elo rating diff | 70.3660 |
| Elo home expectancy | 0.5999 |

</details>


---

## 2026-11-01 — Amed SK vs Eyüpspor

The model's most likely 1X2 outcome is **Amed SK win** at **77.5%**. Expected goals are 2.79 for Amed SK and 0.80 for Eyüpspor (3.59 combined). The most likely exact score is 2-0 at 10.7%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 69.5%; Under 3.5 goals: 51.9%; Double Chance 1X: 92.1%; Double Chance X2: 22.5%; Double Chance 12 (either team wins): 85.4%; Under 4.5 goals: 70.9%; BTTS Yes (both teams score): 52.4%; BTTS No (at least one team does not score): 47.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Amed SK win | 77.5% | 1.29 |
| Draw | 14.6% | 6.84 |
| Eyüpspor win | 7.9% | 12.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Amed SK expected goals | 2.79 |
| Eyüpspor expected goals | 0.80 |
| Expected total goals | 3.59 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 87.9% |
| Under 1.5 | 12.1% |
| Over 2.5 | 69.5% |
| Under 2.5 | 30.5% |
| Over 3.5 | 48.1% |
| Under 3.5 | 51.9% |
| Over 4.5 | 29.1% |
| Under 4.5 | 70.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.66% |
| 2 | 3-0 | 9.92% |
| 3 | 2-1 | 8.52% |
| 4 | 3-1 | 7.93% |
| 5 | 1-0 | 7.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Amed SK win | 77.5% | 77.2% | 1.27 | -1.6% |
| Draw | 14.6% | 14.7% | 5.91 | -13.6% |
| Eyüpspor win | 7.9% | 8.1% | 10.23 | -19.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T10:30:00+00:00 |
| Fixture id | 5706f8b2f4d8a94519bbea0efc91e36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:07:57Z |
| Market best draw last update utc | 2026-10-29T12:07:57Z |
| Market best away last update utc | 2026-10-29T12:07:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Amedspor |
| Matched away-team name | Eyupspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.0104 |
| Dc lambda away | 0.7473 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9191 |
| Shot lambda away | 1.0061 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 52.4% |
| P btts no | 47.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.64 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.23 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.27 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.44 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.05515798913513255, "-10": 1.050772282692248e-09, "-11": 7.507667509705847e-11, "-12": 4.929440433520252e-12, "-13": 2.9935406045529586e-13, "-14": 1.6907395687867543e-14, "-15": 8.924144778558885e-16, "-16": 4.4206735281485167e-17, "-17": 2.0623818323692488e-18, "-18": 9.043431823998683e-20, "-19": 3.4035357337655755e-21, "-2": 0.018625184800605862, "-3": 0.004245848049670598, "-4": 0.0007681256600098126, "-5": 0.00011464160531965, "-6": 1.4524369818531777e-05, "-7": 1.5962073854387608e-06, "-8": 1.547475418915701e-07, "-9": 1.3412810512183909e-08, "0": 0.146121133383237, "1": 0.19398561932522496, "10": 0.0002654111570759729, "11": 6.62642807568316e-05, "12": 1.5203233694204414e-05, "13": 3.2261710680305226e-06, "14": 6.367117231563692e-07, "15": 1.1743474997664551e-07, "16": 2.0327424362589685e-08, "17": 3.313804442038799e-09, "18": 5.077558795570381e-10, "19": 6.677530761848548e-11, "2": 0.21164111078355183, "3": 0.16858843530358777, "4": 0.1065760196494704, "5": 0.055581897945142365, "6": 0.02460663927260845, "7": 0.009449486542186353, "8": 0.003201153831922349, "9": 0.0009695416388500153} |
| Raw goal margin distribution | {"-1": 0.051731118701063505, "-10": 9.854896187489438e-10, "-11": 7.041229116623738e-11, "-12": 4.623182827994611e-12, "-13": 2.80755710602847e-13, "-14": 1.5856968445896976e-14, "-15": 8.369703103463154e-16, "-16": 4.1460247302169997e-17, "-17": 1.93424961732797e-18, "-18": 8.481579051152748e-20, "-19": 3.1920799472109898e-21, "-2": 0.017468034293071956, "-3": 0.003982060856244825, "-4": 0.000720403341716291, "-5": 0.0001075191207268625, "-6": 1.3621995850860998e-05, "-7": 1.4970377822394544e-06, "-8": 1.451333448483478e-07, "-9": 1.2579495801066258e-08, "0": 0.14498480224858942, "1": 0.1954975506757871, "10": 0.0002674797818047955, "11": 6.678074710030182e-05, "12": 1.5321728280205932e-05, "13": 3.2513159689618343e-06, "14": 6.416742787254839e-07, "15": 1.1835004091807065e-07, "16": 2.048585708701991e-08, "17": 3.3396323608452476e-09, "18": 5.117133483395434e-10, "19": 6.729575692489801e-11, "2": 0.21329064971109973, "3": 0.16990242002866357, "4": 0.10740667723061828, "5": 0.0560151053876287, "6": 0.024798424362027154, "7": 0.009523136202401083, "8": 0.0032261037475567723, "9": 0.0009770982835361102} |
| Unadjusted home-win probability | 78.1% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 7.4% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 51.7% |
| Raw p btts yes | 52.2% |
| P home draw | 92.1% |
| P draw away | 22.5% |
| P home away | 85.4% |
| Raw p home draw | 92.6% |
| Raw p draw away | 21.9% |
| Raw p home away | 85.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6946 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:59Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:07:59Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:07:57Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.27 |
| Reference draw odds | 5.91 |
| Reference away odds | 10.23 |
| Market reference 1x2 last update utc | 2026-10-29T12:07:57Z |
| Market reference home last update utc | 2026-10-29T12:07:57Z |
| Market reference draw last update utc | 2026-10-29T12:07:57Z |
| Market reference away last update utc | 2026-10-29T12:07:57Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-29T12:07:59Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:07:59Z |
| Home probability edge | +0.3% |
| Draw probability edge | -0.0% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +10.3% |
| Under 2.5 probability edge | -10.3% |
| Raw edge prob home | 0.0086 |
| Raw ev home | -0.0081 |
| Raw edge prob draw | -0.0016 |
| Raw ev draw | -0.1431 |
| Raw edge prob away | -0.0070 |
| Raw ev away | -0.2427 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.030365000193854054, 0.014580524226339736, 0.007420162470557536, 0.0017803692184256313, 0.0003203819222114013, 4.612282666654514e-05, 5.533279169406642e-06, 5.689871510374349e-07, 5.119533501151031e-08, 4.0945463994506724e-09, 2.9472957237483753e-10, 1.9286301240265433e-11, 1.1568728178694696e-12, 6.405605401003387e-14, 3.2934423297656855e-15, 1.5804352990492476e-16, 7.11008275418156e-18, 3.010534796135855e-19, 1.2038962541379605e-20, 4.560929710558069e-22, 1.6415015634025028e-23], [0.0614615520753261, 0.061067943579696915, 0.02292846572755693, 0.00550138016101987, 0.0009899872074635274, 0.00014252055189870643, 1.709795470114715e-05, 1.758182848926465e-06, 1.5819471458743012e-07, 1.2652238702617287e-08, 9.107208805612867e-10, 5.959509630057175e-11, 3.5747625285715993e-12, 1.9793462000856183e-13, 1.0176809454422074e-14, 4.883579939476593e-16, 2.1970312563398124e-17, 9.3026189343846e-19, 3.7200659840083434e-20, 1.4093373422653542e-21, 5.072276043489036e-23], [0.1019094828668554, 0.07335547183033217, 0.0310181830709916, 0.008499693030759738, 0.0015295411554069197, 0.00022019582473080637, 2.6416528609185347e-05, 2.716411894910965e-06, 2.444125789759158e-07, 1.9547848353786285e-08, 1.4070738060100008e-09, 9.207508113737051e-11, 5.523047537418008e-12, 3.05811171195441e-13, 1.572328286054774e-14, 7.545184873941188e-16, 3.3944375250029856e-17, 1.43726488644886e-18, 5.747542978811399e-20, 2.1774417392419537e-21, 7.836722436018836e-23], [0.10496751674900434, 0.07555667540813125, 0.02719322784581286, 0.007665726891862959, 0.0015754386376214708, 0.00022680331869301477, 2.720921872263817e-05, 2.797924227020068e-06, 2.517467536445113e-07, 2.0134427550415976e-08, 1.449296367173269e-09, 9.483801064990232e-11, 5.68877957752864e-12, 3.1498775512803847e-13, 1.6195096968259246e-14, 7.77159590402889e-16, 3.496295611907997e-17, 1.4803934020368147e-18, 5.920011533001548e-20, 2.2427810033387674e-21, 8.07188173680395e-23], [0.08108798560125953, 0.058367948459938215, 0.02100691848589396, 0.00504033047721822, 0.001065645749251432, 0.0001752068145469537, 2.1019271526433753e-05, 2.1614118963728894e-06, 1.9447575561402036e-07, 1.5553956327286557e-08, 1.119589436742758e-09, 7.326288627385599e-11, 4.394613598170666e-12, 2.4332977804428926e-13, 1.2510801726531881e-14, 6.003600697457481e-16, 2.7009076428287677e-17, 1.143612067679971e-18, 4.5732415590547285e-20, 1.7325606943753615e-21, 6.235573159400639e-23], [0.05011273287215263, 0.03607164967510333, 0.012982368309496362, 0.0031149464735042427, 0.0005605424585184726, 9.480960677401162e-05, 1.299000254305315e-05, 1.3357620883844599e-06, 1.2018687502139728e-07, 9.612413636309798e-09, 6.919112116789615e-10, 4.5276786962477146e-11, 2.715890593267314e-12, 1.5037887643350526e-13, 7.73173066625569e-15, 3.7102517196836457e-16, 1.6691728400184984e-17, 7.067573035890823e-19, 2.8262834612230974e-20, 1.0707301534035784e-21, 3.85361172465672e-23], [0.02580824168231976, 0.018577032209958745, 0.006685967412616559, 0.0016042088868068927, 0.0002886814271245913, 4.155915955936099e-05, 5.8577298885551656e-06, 6.879223868124571e-07, 6.189668253591973e-08, 4.950428365365915e-09, 3.563368180153748e-10, 2.3317711758159803e-11, 1.3986936412468449e-12, 7.744567427230179e-14, 3.981869720943011e-15, 1.9107932773917547e-16, 8.596301497797558e-18, 3.6398260993480225e-19, 1.4555463741336295e-20, 5.514299658349452e-22, 1.9846242070551347e-23], [0.011392576592100113, 0.0082004913357136, 0.002951398114529476, 0.0007081486928726114, 0.0001274331397588671, 1.8345531408584225e-05, 2.2008830362611884e-06, 2.6589658445068957e-07, 2.732315921663315e-08, 2.1852761226570644e-09, 1.5729837552654625e-10, 1.0293177676623157e-11, 6.174277439328364e-13, 3.4186977428937714e-14, 1.7577236114727075e-15, 8.434847686376315e-17, 3.7946801811583486e-18, 1.6067347062684552e-19, 6.425243437653857e-21, 2.434186799040038e-22, 8.760760831258338e-24], [0.004400414124640243, 0.003167462391930431, 0.0011399856604534786, 0.000273524385398732, 4.9221401638942355e-05, 7.086012095836504e-06, 8.500971418669687e-07, 8.741549740166487e-08, 9.240857682430747e-09, 8.440689284500627e-10, 6.075693130998584e-11, 3.9757682618567854e-12, 2.3848316870046784e-13, 1.3204814305253057e-14, 6.789255919948428e-16, 3.257983178630295e-17, 1.465705684106658e-18, 6.206057109957125e-20, 2.4817679959167226e-21, 9.402113635940941e-23, 3.383868029572552e-24], [0.0015108196356767674, 0.001087503185257009, 0.000391397871068299, 9.39107094450137e-05, 1.6899468546662398e-05, 2.432881522010868e-06, 2.9186876911734235e-07, 3.0012868379219664e-08, 2.7004456050175808e-09, 2.537504142792656e-10, 2.0860028676072786e-11, 1.3650235152367165e-12, 8.187980581953493e-14, 4.533685278876524e-15, 2.3309945075524945e-16, 1.118582210573573e-17, 5.032292109216944e-19, 2.130761486595581e-20, 8.520797618637099e-22, 3.2280820613003516e-23, 1.1618029846304593e-24], [0.0004668466003889522, 0.00033604088334605864, 0.00012094280560886321, 2.9018616391545934e-05, 5.22197306222811e-06, 7.51765757393736e-07, 9.018809353844735e-08, 9.274042539487785e-09, 8.344436493063053e-10, 6.673788225125274e-11, 5.643990278537511e-12, 4.217952775374017e-13, 2.5301040630329445e-14, 1.4009187527727933e-15, 7.202824451568225e-17, 3.4564437073119636e-18, 1.5549893633065697e-19, 6.58409999954274e-21, 2.6329452615838673e-22, 9.974844782974808e-24, 3.5899968526256847e-25], [0.00013114239037606532, 9.439761298330222e-05, 3.397417612791824e-05, 8.15165134719371e-06, 1.4669101783957691e-06, 2.111793431618632e-07, 2.533483624007997e-08, 2.6051814580302242e-09, 2.3440448042886884e-10, 1.874741167607052e-11, 1.349457568038451e-12, 1.0374815538026272e-13, 7.10734306407916e-15, 3.935336228393106e-16, 2.0233533140240096e-17, 9.709533915413452e-19, 4.368137669707347e-20, 1.849546749822534e-21, 7.396235402501911e-23, 2.8020445846230425e-24, 1.0084699520220066e-25], [3.3769406612260505e-05, 2.430755888251468e-05, 8.748412810611812e-06, 2.099065207789639e-06, 3.777320676850436e-07, 5.437906909347138e-08, 6.523766907046082e-09, 6.708390147736748e-10, 6.035958463650833e-11, 4.8274929715800724e-12, 3.474878045947197e-13, 2.2738656398581384e-14, 1.6024976037027996e-15, 1.0133563134809293e-16, 5.210171980669644e-18, 2.5002228330967853e-19, 1.1248034802757511e-20, 4.762616882614119e-22, 1.90454421328489e-23, 7.215316317818751e-25, 2.59682866603394e-26], [8.026785492816352e-06, 5.77776101440615e-06, 2.079445275413651e-06, 4.989352152917077e-07, 8.978464785830814e-08, 1.2925578702761689e-08, 1.550660281634354e-09, 1.5945441190682797e-10, 1.4347111392145187e-11, 1.1474661369052102e-12, 8.259576784623848e-14, 5.404842300071767e-15, 3.242049921303664e-16, 2.1090660519270907e-17, 1.2384266430768018e-18, 5.942879777527155e-20, 2.6735904368745367e-21, 1.1320454795119139e-22, 4.5269874111652796e-24, 1.715037430504373e-25, 6.172506050575095e-27], [1.7716388749163396e-06, 1.2752434996872538e-06, 4.5896655535157784e-07, 1.1012291586297244e-07, 1.9816895899212755e-08, 2.8528802384338543e-09, 3.4225531991490033e-10, 3.519411788989271e-11, 3.1666350505850056e-12, 2.532639769196155e-13, 1.8230196054313456e-14, 1.1929344243930532e-15, 7.155718413232106e-17, 3.962121661763405e-18, 2.393390742905319e-19, 1.3116878297350761e-20, 5.901038165042018e-22, 2.4986039323855416e-23, 9.991779263386359e-25, 3.7853596393443516e-26, 1.3623699904079843e-27], [3.649602137986122e-07, 2.627020364481042e-07, 9.454778540882624e-08, 2.2685482626573587e-08, 4.0823097001317815e-09, 5.87697524874996e-10, 7.050509926056625e-11, 7.250040045635908e-12, 6.523314776202669e-13, 5.2172751723137966e-14, 3.7554471985082384e-15, 2.4574624588477287e-16, 1.4740885171077418e-17, 8.162028894526086e-19, 4.1965075547413696e-20, 2.365977367356939e-21, 1.21562254071062e-22, 5.147160847915701e-24, 2.0583212232607087e-25, 7.797896528687257e-27, 2.806502216743187e-28], [7.048344449335371e-08, 5.073469299998351e-08, 1.825967141862153e-08, 4.381165110773835e-09, 7.884016894857813e-10, 1.1349989480295963e-10, 1.3616394506423352e-11, 1.4001739800962193e-12, 1.2598241604353836e-13, 1.0075934611799874e-14, 7.252759181849828e-16, 4.74600825689655e-17, 2.846853773249534e-18, 1.5763030839792492e-19, 8.10456307612119e-21, 3.889164067975154e-22, 2.0556544734079154e-23, 9.940525356076752e-25, 3.975161242349637e-26, 1.505979518764557e-27, 5.420096101857466e-29], [1.2811494023198201e-08, 9.221842388809127e-09, 3.3189875002106593e-09, 7.963468731528328e-10, 1.4330462430335535e-10, 2.0630422283616653e-11, 2.4749976124251584e-12, 2.545040286606859e-13, 2.28993202839577e-14, 1.831462366589965e-15, 1.3183050513192044e-16, 8.626629537523947e-18, 5.174612331033972e-19, 2.865183119853532e-20, 1.4731340410037758e-21, 7.069178098524866e-23, 3.1802909815287173e-24, 1.582092136578066e-25, 7.225491725565965e-27, 2.737358785796905e-28, 9.85189207384078e-30], [2.1993221756356706e-09, 1.5830942456203775e-09, 5.69763588591105e-10, 1.3670718922022604e-10, 2.4600802804951037e-11, 3.5415811098165507e-12, 4.2487762346808195e-13, 4.369017017129535e-14, 3.931078047283006e-15, 3.144032842219575e-16, 2.2631064951276142e-17, 1.4809153099955033e-18, 8.883147921197554e-20, 4.91859947117846e-21, 2.5288981583231444e-22, 1.2135509041686735e-23, 5.459538495654833e-25, 2.3116651634393013e-26, 1.0860911099408189e-27, 4.699166131110896e-29, 1.691253547067444e-30], [3.57681791640489e-10, 2.5746295489681195e-10, 9.266221358400039e-11, 2.2233064765189705e-11, 4.0008959671977135e-12, 5.759770399410281e-13, 6.909901208361728e-14, 7.105452087496024e-15, 6.393219941159291e-16, 5.113226758860847e-17, 3.680552102906483e-18, 2.4084531462241258e-19, 1.4446906865489502e-20, 7.999253091260195e-22, 4.1128163675424944e-23, 1.973631087153153e-24, 8.878997048677642e-26, 3.7595243957056516e-27, 1.5034130624033044e-28, 6.69173222526833e-30, 2.7505319845127847e-31], [5.5262231342920364e-11, 3.977831052143755e-11, 1.4316414208115568e-11, 3.435033030003879e-12, 6.181428400483588e-13, 8.89890879919997e-14, 1.0675873585340912e-14, 1.0978001850592188e-15, 9.877595328353391e-17, 7.899991742967795e-18, 5.686493596658278e-19, 3.721086676925371e-20, 2.2320630461188156e-21, 1.2358934260318988e-22, 6.354346653534114e-24, 3.0492817994342304e-25, 1.3718148378386383e-26, 5.80850666012266e-28, 2.322789764540394e-29, 8.799828732799129e-31, 3.7209862034377895e-32]] |
| Legacy trial inputs | {"lambda_home": 3.090022060640153, "lambda_away": 0.7198100683738232, "rho": -0.09475376269082486, "max_goals": 20, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8027 |
| Legacy p draw | 0.1313 |
| Legacy p away | 0.0661 |
| Legacy p over 1 5 | 0.8936 |
| Legacy p under 3 5 | 0.4798 |
| Legacy p btts yes | 0.5022 |
| Legacy p over 2 5 | 0.7232 |
| Legacy goal margin distribution | {"-1": 0.047773034550271876, "-10": 3.6017559455434317e-10, "-11": 2.3183687459301916e-11, "-12": 1.3713356109649802e-12, "-13": 7.502351734306216e-14, "-14": 3.8172719153573984e-15, "-15": 1.8151207856691338e-16, "-16": 8.100125214143065e-18, "-17": 3.405123000102789e-19, "-18": 1.3526667108005147e-20, "-19": 5.068157314906973e-22, "-2": 0.014700306283398473, "-20": 1.6415015634025028e-23, "-3": 0.0030200481798998077, "-4": 0.000492321381988649, "-5": 6.620520983236765e-05, "-6": 7.557175324654032e-06, "-7": 7.482550683591793e-07, "-8": 6.535403459096758e-08, "-9": 5.103282397172499e-09, "0": 0.13128344221926144, "1": 0.16765497491385686, "10": 0.0005705119798664634, "11": 0.00015764371577878654, "12": 4.0029629128838434e-05, "13": 9.401104859425432e-06, "14": 2.053422117111937e-06, "15": 4.191546913730818e-07, "16": 8.02979016783592e-08, "17": 1.4490685515432582e-08, "18": 2.471101544740598e-09, "19": 3.9746010216192656e-10, "2": 0.2018959311564723, "20": 5.5262231342920364e-11, "3": 0.17805686293922796, "4": 0.1246054985198135, "5": 0.07193236483662308, "6": 0.0352480692267781, "7": 0.014981978347254819, "8": 0.005617402774132894, "9": 0.0018830264698151214} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8330 |
| Legacy raw p draw | 0.1160 |
| Legacy raw p away | 0.0511 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 3.0900 |
| Legacy lambda away | 0.7198 |
| Legacy model home team | Amedspor |
| Legacy model away team | Eyupspor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,486.7305 |
| Elo away rating | 1,373.7821 |
| Elo rating diff | 172.9484 |
| Elo home expectancy | 0.7302 |

</details>


---
