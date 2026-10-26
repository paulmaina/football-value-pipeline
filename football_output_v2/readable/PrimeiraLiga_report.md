# Primeira Liga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,602 |
| Training data through | 2026-10-19 |
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
| Training sha256 | 9aa0490d3c785bbac1db1df68144a198798f6e850afaca727c2a89dab1ac3be4 |
| Training as of utc | 2026-10-26T11:45:49.757538+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1602, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1304, 'tuning_matches': 197, 'audit_matches': 95, 'audit_matchdays': 39, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8842989647630213, 'audit_candidate_poisson_score': 0.8712722566731389, 'audit_gain': 0.013026708089882377, 'audit_gain_lower95': 0.0016952519471041152, 'audit_baseline_briers': [0.6014046160164832, 0.17871464745604035, 0.23959646082409236, 0.25147632394995034], 'audit_candidate_briers': [0.596003028732249, 0.17800083852090984, 0.2385408793338746, 0.24933758220041838], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1441.399 |
| Base scoring parameter | 0.092 |
| Home-advantage parameter | 0.178 |
| Dixon-Coles low-score adjustment | 0.043 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1602, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-19'} |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 7, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Additional event odds calls used before this league | 2.00 |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE': 1} |
| Shot features applied fixtures | 1 |
| Goal rate features used | {'shot_features': 1} |
| Legacy comparison status | {'AVAILABLE': 1} |
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

## 2026-10-26 — Santa Clara vs Benfica

The model's most likely 1X2 outcome is **Benfica win** at **69.4%**. Expected goals are 0.80 for Santa Clara and 1.69 for Benfica (2.49 combined). The most likely exact score is 0-1 at 17.1%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 47.4%; Under 3.5 goals: 75.0%; Double Chance 1X: 30.6%; Double Chance X2: 88.4%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 88.5%; BTTS Yes (both teams score): 43.1%; BTTS No (at least one team does not score): 56.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Santa Clara win | 11.6% | 8.64 |
| Draw | 19.0% | 5.26 |
| Benfica win | 69.4% | 1.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Santa Clara expected goals | 0.80 |
| Benfica expected goals | 1.69 |
| Expected total goals | 2.49 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 71.9% |
| Under 1.5 | 28.1% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.0% |
| Under 3.5 | 75.0% |
| Over 4.5 | 11.5% |
| Under 4.5 | 88.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.08% |
| 2 | 0-2 | 13.92% |
| 3 | 1-2 | 11.16% |
| 4 | 1-1 | 8.89% |
| 5 | 0-3 | 7.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Santa Clara win | 11.6% | 8.8% | 8.89 | +2.9% |
| Draw | 19.0% | 17.3% | 5.39 | +2.5% |
| Benfica win | 69.4% | 73.9% | 1.35 | -6.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T18:45:00+00:00 |
| Fixture id | 7f4d1fc269584543a305935a2d3552fd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T11:45:35Z |
| Market best draw last update utc | 2026-10-26T11:45:35Z |
| Market best away last update utc | 2026-10-26T11:45:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santa Clara |
| Matched away-team name | Benfica |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7110 |
| Dc lambda away | 1.7675 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.0142 |
| Shot lambda away | 1.4934 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 43.1% |
| P btts no | 56.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.45 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.56 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.99 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.71 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.3106024629413727, "-10": 5.640104350987932e-06, "-11": 8.55423895552323e-07, "-12": 1.1911139365872933e-07, "-13": 1.532648591654661e-08, "-14": 1.826890433933029e-09, "-15": 1.8829076352507038e-10, "-2": 0.2134660951401523, "-3": 0.10844625559815546, "-4": 0.042912320680042575, "-5": 0.013858606178227885, "-6": 0.003773988423789873, "-7": 0.0008875752597887096, "-8": 0.00018358160731082702, "-9": 3.3873817176202186e-05, "0": 0.19007481392891748, "1": 0.08179106770189748, "10": 1.8208636458841434e-09, "11": 1.3141084791041555e-10, "12": 8.706882822055135e-12, "13": 5.331035050042592e-13, "14": 3.023716034609304e-14, "15": 1.4829177773943349e-15, "2": 0.026220608201684804, "3": 0.006338521541818534, "4": 0.0011934795027555222, "5": 0.00018340537971560885, "6": 2.3765810745406154e-05, "7": 2.6596029913294194e-06, "8": 2.6175823055715267e-07, "9": 2.2982373131029998e-08} |
| Raw goal margin distribution | {"-1": 0.2635086868172425, "-10": 4.784947540231108e-06, "-11": 7.25723889161915e-07, "-12": 1.010516356848972e-07, "-13": 1.3002672738478793e-08, "-14": 1.5498959494585234e-09, "-15": 1.597419781106902e-10, "-2": 0.18110020724788484, "-3": 0.09200355377835781, "-4": 0.036405922746378216, "-5": 0.011757354016318455, "-6": 0.003201773495930247, "-7": 0.0007530004396730817, "-8": 0.00015574682765926977, "-9": 2.8737843856934287e-05, "0": 0.23005773582372716, "1": 0.12790901993428697, "10": 2.8475589196106082e-09, "11": 2.0550694882987755e-10, "12": 1.3616264950969877e-11, "13": 8.336942989563897e-13, "14": 4.7286404911118685e-14, "15": 2.3190620305992182e-15, "2": 0.04100511695705159, "3": 0.009912501462889762, "4": 0.0018664237770498924, "5": 0.0002868186347144977, "6": 3.716618019302522e-05, "7": 4.159222047022525e-06, "8": 4.0935079674380867e-07, "9": 3.594100071744068e-08} |
| Unadjusted home-win probability | 18.1% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 58.9% |
| Raw p over 1 5 | 70.5% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 44.4% |
| P home draw | 30.6% |
| P draw away | 88.4% |
| P home away | 81.0% |
| Raw p home draw | 41.1% |
| Raw p draw away | 81.9% |
| Raw p home away | 77.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4736 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:45:35Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 8.80 |
| Reference draw odds | 4.80 |
| Reference away odds | 1.31 |
| Market reference 1x2 last update utc | 2026-10-26T11:45:52Z |
| Market reference home last update utc | 2026-10-26T11:45:52Z |
| Market reference draw last update utc | 2026-10-26T11:45:52Z |
| Market reference away last update utc | 2026-10-26T11:45:52Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-26T11:45:52Z |
| Market reference under 2 5 last update utc | 2026-10-26T11:45:52Z |
| Home probability edge | +2.8% |
| Draw probability edge | +1.7% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | 0.0932 |
| Raw ev home | 0.6093 |
| Raw edge prob draw | 0.0571 |
| Raw ev draw | 0.2400 |
| Raw edge prob away | -0.1504 |
| Raw ev away | -0.2050 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.0682360503425486, 0.16046469422099108, 0.14308458515650896, 0.08773048237339041, 0.04034311695272248, 0.014841519539664163, 0.004549943891386419, 0.0011956028025358132, 0.00027490070946159013, 5.6183950725073396e-05, 1.0334541124808063e-05, 1.728134084265297e-06, 2.6489582482392794e-07, 3.748095812064946e-08, 4.924493536679738e-09, 6.038780389166236e-10, 6.942376723037222e-11], [0.04866419643679823, 0.08849205964073267, 0.09954526620457023, 0.06103490611907633, 0.028067078729606836, 0.010325382093676864, 0.0031654379497868344, 0.0008317919021337963, 0.00019125096021522318, 3.908769295612322e-05, 7.18983562237556e-06, 1.202278828758617e-06, 1.8429046965285612e-07, 2.607584841959946e-08, 3.4260155941694764e-09, 4.201235239512071e-10, 4.829875546909778e-11], [0.01562966725118042, 0.02874939139911812, 0.029649787772764655, 0.021231273692930083, 0.00976326283039947, 0.0035917317999513707, 0.0011011121953525308, 0.00028934265083183195, 6.652752889376501e-05, 1.3596834335381894e-05, 2.50101749330165e-06, 4.1821823758997407e-07, 6.410629013772664e-08, 9.070604180037247e-09, 1.19175533118948e-09, 1.461419061486603e-10, 1.68009449280011e-11], [0.003624567909733897, 0.006667072293669803, 0.006131745090173089, 0.004215855982859766, 0.0022641306804974393, 0.0008329336519618676, 0.00025535130493517093, 6.709945069644349e-05, 1.5427938577772597e-05, 3.153147703913607e-06, 5.799936493990068e-07, 9.698609566493506e-08, 1.48664458629307e-08, 2.1035010089788147e-09, 2.763717269385532e-10, 3.389075754340016e-11, 3.896190805638561e-12], [0.0006304113351140221, 0.001159585928757686, 0.001066477909958282, 0.0006538972830571829, 0.00033718827989568506, 0.0001448699068886336, 4.441256477357798e-05, 1.1670426752210574e-05, 2.683339807415773e-06, 5.48418488310742e-07, 1.0087673344272516e-07, 1.6868530423014408e-08, 2.585680891695178e-09, 3.658562654938316e-10, 4.806859016193532e-11, 5.894528187369251e-12, 6.776539738834436e-13], [8.77165965902781e-05, 0.00016134692614022206, 0.0001483917045738615, 9.098447473034658e-05, 4.183947478261817e-05, 1.7259934731927868e-05, 6.179646225870795e-06, 1.6238447160454215e-06, 3.733648529006098e-07, 7.63079605684798e-08, 1.4036174858975374e-08, 2.3471184538881496e-09, 3.59776411137966e-10, 5.090591596761773e-11, 6.688352345592376e-12, 8.201755303273117e-13, 9.429002453482493e-14], [1.0170874275272359e-05, 1.870842422374303e-05, 1.7206246359099856e-05, 1.0549789771330618e-05, 4.8513514465813425e-06, 1.7847264348114804e-06, 6.13540640333074e-07, 1.8828729215987204e-07, 4.329222889706306e-08, 8.848025383037585e-09, 1.6275160613356475e-09, 2.721519943959368e-10, 4.1716628176822307e-11, 5.9026192453938e-12, 7.755247405857812e-13, 9.510061410132821e-14, 1.0933073354813002e-14], [1.0108530121314006e-06, 1.8593747663148928e-06, 1.710077766063555e-06, 1.0485122988522068e-06, 4.821614238814741e-07, 1.7737866417697019e-07, 5.43787290362959e-08, 1.60233729859886e-08, 4.30268616031107e-09, 8.793789862886813e-10, 1.6175399167927647e-10, 2.704837911147357e-11, 4.146091880324345e-12, 5.866438107663384e-13, 7.707710259574193e-14, 9.451767824285617e-15, 1.0866057168197894e-15], [8.790747102163862e-08, 1.616980227852804e-07, 1.487146101964024e-07, 9.11824601806703e-08, 4.1930518966592354e-08, 1.542549667841031e-08, 4.728972946197573e-09, 1.2426468199516694e-09, 3.203912560841035e-10, 7.647400940242879e-11, 1.4066718074271315e-11, 2.352225867053235e-12, 3.605592973939576e-13, 5.1016689049804124e-14, 6.70290643798001e-15, 8.219602614278386e-16, 9.449520297899234e-17], [6.795337639424787e-09, 1.2499422946462794e-08, 1.1495791841756492e-08, 7.048497659186908e-09, 3.2412721064875512e-09, 1.1924067086382403e-09, 3.655544572452529e-10, 9.605787323867543e-11, 2.2086245905978786e-11, 5.061769016396194e-12, 1.0873717294147116e-12, 1.818294712047957e-13, 2.7871603361477805e-14, 3.943642369755232e-15, 5.181415399873855e-16, 6.353837094479885e-17, 7.304576073974088e-18], [4.727579099639324e-10, 8.69596388212017e-10, 7.997728461582763e-10, 4.903704861418689e-10, 2.2549829132804603e-10, 8.295683501173373e-11, 2.5431960905461974e-11, 6.6828348784948095e-12, 1.5365605077342174e-12, 3.1404080412057033e-13, 6.477523690778979e-14, 1.2650044094630555e-14, 1.9390531643445063e-15, 2.7436283865484426e-16, 3.6047585051368347e-17, 4.420423096580501e-18, 5.081860977546439e-19], [2.9900185484500014e-11, 5.4998748315335995e-11, 5.058266808782396e-11, 3.1014115645119364e-11, 1.4261931096321143e-11, 5.246712327345597e-12, 1.6084772613659284e-12, 4.226645355220507e-13, 9.718175671120075e-14, 1.986191683947279e-14, 3.653424042739052e-15, 6.850627075089491e-16, 1.2263792536571349e-16, 1.7352432593797648e-17, 2.2798761408062604e-18, 2.79575376153534e-19, 3.2140887044422717e-20], [1.7334862454289482e-12, 3.188594725269067e-12, 2.932569078302053e-12, 1.798067203055552e-12, 8.268464221248462e-13, 3.041821816754587e-13, 9.32527060779765e-14, 2.4504301457859055e-14, 5.634187073950383e-15, 1.1515099017338229e-15, 2.118100682047816e-16, 3.541871804801962e-17, 6.087998285645949e-18, 1.0060206229046472e-18, 1.3217757239058047e-19, 1.6208597414019673e-20, 1.8633926413692247e-21], [9.276941358978242e-14, 1.7064113639130062e-13, 1.5693964369373537e-13, 9.622553421599724e-14, 4.4249591199006545e-14, 1.6278642356063385e-14, 4.990520623585072e-15, 1.3113745105663203e-15, 3.0151968744128856e-16, 6.162431262916719e-17, 1.1335247609597948e-17, 1.895471459367458e-18, 2.905460173669466e-19, 4.609931835563716e-20, 7.073627444537898e-21, 8.674208296584378e-22, 9.972149654095664e-23], [4.610038361642395e-15, 8.479758084024265e-15, 7.79888273402102e-15, 4.781785148140015e-15, 2.1989177792634175e-15, 8.089429784341592e-16, 2.4799651769954313e-16, 6.516681054946976e-17, 1.4983573487284182e-17, 3.0623287809765156e-18, 5.632883112750132e-19, 9.419264176576294e-20, 1.443825323513272e-20, 2.0429146635325077e-21, 3.0098518494683465e-22, 4.3105191093430635e-23, 4.9555118087415925e-24], [2.1381641515099207e-16, 3.932963963943599e-16, 3.6171697880996796e-16, 2.2178213676150396e-16, 1.0198715930129075e-16, 3.751927297384499e-17, 1.1502231049885375e-17, 3.022476761678697e-18, 6.949473557224747e-19, 1.42032692701679e-19, 2.6125658392649646e-20, 4.368712669189565e-21, 6.696550669653111e-22, 9.475163882590692e-23, 1.2449090321704572e-23, 1.711864115096091e-24, 2.2983968615090835e-25], [9.297128313049478e-18, 1.7101245756815176e-17, 1.572811499355675e-17, 9.64349243980122e-18, 4.434587988195061e-18, 1.63140652603233e-18, 5.001380173809821e-19, 1.3142281081035486e-19, 3.0217580499624754e-20, 6.175840932338769e-21, 1.1359913511216438e-21, 1.8995960726222952e-22, 2.911782558258532e-23, 4.119974340670215e-24, 5.413091881645122e-25, 6.637936034671539e-26, 8.557285263229775e-27]] |
| Legacy trial inputs | {"lambda_home": 0.6957092274872623, "lambda_away": 1.8394116097991045, "rho": 0.045162625721741304, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1136 |
| Legacy p draw | 0.1909 |
| Legacy p away | 0.6955 |
| Legacy p over 1 5 | 0.7226 |
| Legacy p under 3 5 | 0.7442 |
| Legacy p btts yes | 0.4106 |
| Legacy p over 2 5 | 0.4754 |
| Legacy goal margin distribution | {"-1": 0.2836566070196558, "-10": 1.160307864441215e-05, "-11": 1.9217775186433414e-06, "-12": 2.921979969862342e-07, "-13": 4.105701181177323e-08, "-14": 5.361418005558946e-09, "-15": 6.521767943857214e-10, "-16": 6.942376723037222e-11, "-2": 0.21476176835329466, "-3": 0.11965669701164865, "-4": 0.051839471995145284, "-5": 0.018312290809873396, "-6": 0.005451519736279831, "-7": 0.001401047825023177, "-8": 0.00031658904337855865, "-9": 6.380724367170691e-05, "0": 0.1909488318430651, "1": 0.08424291005414389, "10": 5.307876898289766e-10, "11": 3.325060525717678e-11, "12": 1.9121524812790197e-12, "13": 1.0162053214505646e-13, "14": 5.0190628730303116e-15, "15": 2.3091766090780727e-16, "16": 9.297128313049478e-18, "2": 0.023459235486237066, "3": 0.004943593292092972, "4": 0.0008100561686981933, "5": 0.00010822960690249303, "6": 1.2186242989025707e-05, "7": 1.184551768414246e-06, "8": 1.0123852430601849e-07, "9": 7.717359833095516e-09} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1394 |
| Legacy raw p draw | 0.2090 |
| Legacy raw p away | 0.6517 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.6957 |
| Legacy lambda away | 1.8394 |
| Legacy model home team | Santa Clara |
| Legacy model away team | Benfica |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 29.4% |
| Market reference home draw last update utc | 2026-10-26T11:44:53Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.3% |
| Market reference draw away last update utc | 2026-10-26T11:44:53Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.2% |
| Market reference home away last update utc | 2026-10-26T11:44:53Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.03 |
| Market reference dc home draw odds | 3.16 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 80.5% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-26T11:45:35Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.47 |
| Market reference over 1 5 last update utc | 2026-10-26T11:45:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.5% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-26T11:45:35Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.72 |
| Market reference under 3 5 last update utc | 2026-10-26T11:45:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 47.4% |
| Market reference btts yes odds | 2.08 |
| Market reference btts yes opposite odds | 1.88 |
| Market reference btts yes last update utc | 2026-10-26T11:45:35Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,479.7454 |
| Elo away rating | 1,690.3969 |
| Elo rating diff | -150.6514 |
| Elo home expectancy | 0.2958 |

</details>


---
