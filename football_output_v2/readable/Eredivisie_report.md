# Eredivisie — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Eredivisie |
| Training matches | 1,620 |
| Training data through | 2026-10-25 |
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
| Training sha256 | 173f00460382fe819ab1795f92939756d58effd9917931edff4bdbeeab528135 |
| Training as of utc | 2026-10-30T07:26:39.353694+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1314, 'tuning_matches': 189, 'audit_matches': 111, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6975264417818999, 'audit_candidate_poisson_score': 0.6897599095674726, 'audit_gain': 0.007766532214427357, 'audit_gain_lower95': -0.004043472232242698, 'audit_baseline_briers': [0.6185436744320431, 0.09069762579431699, 0.2827207992348542, 0.22288997938438054], 'audit_candidate_briers': [0.6176465928802188, 0.08929774811962869, 0.27915947396895324, 0.21726068541197704], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1615.194 |
| Base scoring parameter | 0.292 |
| Home-advantage parameter | 0.184 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 27.00 |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 4, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 5} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 9} |
| Legacy comparison status | {'AVAILABLE': 9} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'UNRELIABLE_AUDIT', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'UNRELIABLE_AUDIT', 'draw': 'UNRELIABLE_AUDIT', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-31 — Ajax vs AZ Alkmaar

The model's most likely 1X2 outcome is **Ajax win** at **56.5%**. Expected goals are 1.87 for Ajax and 1.25 for AZ Alkmaar (3.12 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.4%; Double Chance 1X: 78.0%; Double Chance X2: 43.5%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 68.7%; BTTS No (at least one team does not score): 31.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ajax win | 56.5% | 1.77 |
| Draw | 21.5% | 4.66 |
| AZ Alkmaar win | 22.0% | 4.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ajax expected goals | 1.87 |
| AZ Alkmaar expected goals | 1.25 |
| Expected total goals | 3.12 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 88.7% |
| Under 1.5 | 11.3% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 49.6% |
| Under 3.5 | 50.4% |
| Over 4.5 | 30.4% |
| Under 4.5 | 69.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.68% |
| 2 | 1-1 | 8.89% |
| 3 | 3-1 | 7.03% |
| 4 | 2-0 | 6.62% |
| 5 | 2-2 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ajax win | 56.5% | 58.9% | 1.65 | -6.8% |
| Draw | 21.5% | 20.1% | 4.56 | -2.1% |
| AZ Alkmaar win | 22.0% | 20.9% | 4.40 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:00:00+00:00 |
| Fixture id | 43ebf45469e32887fe9caff703c94ae6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:26:45Z |
| Market best draw last update utc | 2026-10-30T07:26:45Z |
| Market best away last update utc | 2026-10-30T07:26:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ajax |
| Matched away-team name | AZ Alkmaar |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8680 |
| Dc lambda away | 1.2546 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.7% |
| P btts no | 31.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.12 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.89 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.29 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.11928071796789409, "-10": 3.84269444173494e-07, "-11": 4.9924431257314745e-08, "-12": 5.9665793397192845e-09, "-13": 6.600567133332065e-10, "-14": 6.795232380614618e-11, "-15": 6.535660524510203e-12, "-16": 5.826744372723881e-13, "-17": 4.22273606262736e-14, "-2": 0.0645967311622387, "-3": 0.02557026038153952, "-4": 0.00816794966444134, "-5": 0.002174397536772365, "-6": 0.0004945885349161816, "-7": 9.801663464252158e-05, "-8": 1.7188716765927985e-05, "-9": 2.701016380358409e-06, "0": 0.21474803897563277, "1": 0.2165896309758897, "10": 2.4600614345265084e-05, "11": 4.75853297259008e-06, "12": 8.467110609152999e-07, "13": 1.3945719383617887e-07, "14": 2.1375379746179338e-08, "15": 3.0608980739512047e-09, "16": 4.0628913058628913e-10, "17": 4.3838232124230845e-11, "2": 0.17128597011512306, "3": 0.10094766013626473, "4": 0.04800914984350427, "5": 0.019028290210479082, "6": 0.0064439879567862466, "7": 0.001901342337386408, "8": 0.0004964252273193217, "9": 0.00011614150842129107} |
| Raw goal margin distribution | {"-1": 0.14100530529028923, "-10": 1.4488764238271256e-07, "-11": 1.624151364617638e-08, "-12": 1.6732855427561949e-09, "-13": 1.5945662038876695e-10, "-14": 1.4127556097718773e-11, "-15": 1.1602074098042241e-12, "-16": 7.93542960045226e-14, "-2": 0.07104582796182733, "-3": 0.025263648267100824, "-4": 0.007144771091377752, "-5": 0.0016690740322045873, "-6": 0.0003312518185698501, "-7": 5.70574092646714e-05, "-8": 8.673046299205138e-06, "-9": 1.1789925803943561e-06, "0": 0.24574474227624657, "1": 0.21475574433227212, "10": 7.754073417528708e-06, "11": 1.2941211075109068e-06, "12": 1.9850357579475067e-07, "13": 2.8163763397853722e-08, "14": 3.7150531271912553e-09, "15": 4.5423801718723994e-10, "16": 4.6256007426758316e-11, "2": 0.15748467280247325, "3": 0.08337687914899546, "4": 0.03510651701265881, "5": 0.012210259161185026, "6": 0.0036079242359932542, "7": 0.0009252541516117635, "8": 0.00020939702889645473, "9": 4.2379885476791474e-05} |
| Unadjusted home-win probability | 50.8% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 61.4% |
| P home draw | 78.0% |
| P draw away | 43.5% |
| P home away | 78.5% |
| Raw p home draw | 75.3% |
| Raw p draw away | 49.2% |
| Raw p home away | 75.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1660 |
| Totals anchor target over 2 5 | 0.7075 |
| Totals anchor reference over odds | 1.37 |
| Totals anchor reference under odds | 3.06 |
| Totals anchor reference last update utc | 2026-10-30T07:26:45Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6165 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.65, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.92, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.65 |
| Reference draw odds | 4.56 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-30T07:26:45Z |
| Market reference home last update utc | 2026-10-30T07:26:45Z |
| Market reference draw last update utc | 2026-10-30T07:26:45Z |
| Market reference away last update utc | 2026-10-30T07:26:45Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 2.94 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:23Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:23Z |
| Home probability edge | -2.4% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | -0.0816 |
| Raw ev home | -0.1622 |
| Raw edge prob draw | 0.0443 |
| Raw ev draw | 0.1206 |
| Raw edge prob away | 0.0373 |
| Raw ev away | 0.0847 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.050601035420893295, 0.04202049997721472, 0.032363772488915366, 0.01342567428508677, 0.004177094853612371, 0.0010396868594052722, 0.0002156500318008472, 3.833978811849052e-05, 5.964278897195831e-06, 8.24733538574069e-07, 1.0263887374076859e-07, 1.1612277740239026e-08, 1.204299179752683e-09, 1.1528936846351247e-10, 1.0248479729619656e-11, 8.502887036071783e-13, 6.613702396809123e-14], [0.07887381758828074, 0.10398401444843447, 0.05999827940642993, 0.024889476566807782, 0.007743797612593917, 0.0019274459646864773, 0.00039978747429472955, 7.107704519627245e-05, 1.105700739474646e-05, 1.5289501030872866e-06, 1.9027929536858204e-07, 2.1527672172412968e-08, 2.2326160740526645e-09, 2.1373168854260757e-10, 1.8999365742033145e-11, 1.5763260983443002e-12, 1.2260955191507333e-13], [0.08393346902169516, 0.10445600095804515, 0.05434624356020494, 0.02307094715003619, 0.007178003321250418, 0.0017866186886844409, 0.0003705773267646955, 6.588385854167648e-05, 1.0249136118111318e-05, 1.4172386039813498e-06, 1.7637669299357694e-07, 1.9954770266859992e-08, 2.069491791542187e-09, 1.9811555608326413e-10, 1.7611192495032597e-11, 1.4611531105729647e-12, 1.1365118445659122e-13], [0.05186729212567732, 0.06454933865024154, 0.0401661331199595, 0.013931725213730187, 0.004435698887247758, 0.0011040538955829145, 0.00022900092998049242, 4.0713405238435346e-05, 6.333527534010339e-06, 8.757928099634164e-07, 1.0899324865619616e-07, 1.2331194108806342e-08, 1.2788573682789744e-09, 1.2242693578357396e-10, 1.0882963333557488e-11, 9.029300958219758e-13, 7.023156856671284e-14], [0.024038825248795987, 0.02991654678980883, 0.018615713591737353, 0.007722477574353522, 0.0020089207096517362, 0.0005116935466162733, 0.00010613458139040905, 1.8869356654261265e-05, 2.9353867410236254e-06, 4.0590185934229805e-07, 5.051487267537109e-08, 5.715112706719259e-09, 5.927093459921384e-10, 5.674095551230727e-11, 5.043904222540445e-12, 4.184791203818729e-13, 3.2550077988132423e-14], [0.008912979192234707, 0.011092287425918926, 0.006902228631162675, 0.0028632964057243, 0.0008908499064365968, 0.0001853961306071244, 3.9351977715992474e-05, 6.996272966321837e-06, 1.0883660359075007e-06, 1.5049798769132792e-07, 1.8729617790974156e-08, 2.1190170529991376e-09, 2.1976140735644173e-10, 2.1038089448819474e-11, 1.8701501807114913e-12, 1.5516131315672892e-13, 1.2068733176899823e-14], [0.002753919865710706, 0.0034272794808076104, 0.002132640964942079, 0.0008846973254478305, 0.0002752535602057381, 6.85111350303516e-05, 1.1881630532779853e-05, 2.161698652306369e-06, 3.362818180998115e-07, 4.6500658097993147e-08, 5.787051153072426e-09, 6.547309302728158e-10, 6.790157279428221e-11, 6.500319502616995e-12, 5.778363915637669e-13, 4.794152588893685e-14, 3.7289803255440025e-15], [0.0007293448412878518, 0.0009076765958597151, 0.0005648060807674376, 0.00023430218084795833, 7.289782345586201e-05, 1.8144407005926816e-05, 3.7634811986311728e-06, 5.594455737457529e-07, 8.906047423667554e-08, 1.2315178637744786e-08, 1.5326357013198836e-09, 1.7339815597823844e-10, 1.798297127286261e-11, 1.7215368373592863e-12, 1.5303349837547244e-13, 1.2696776339038612e-14, 9.875786864980307e-16], [0.00016901396301302043, 0.00021033948540656312, 0.00013088474565172296, 5.4295770513413037e-05, 1.6892900778653897e-05, 4.20467515637446e-06, 8.721263743807077e-07, 1.5505279608390164e-07, 2.0167670941306268e-08, 2.8538450249448627e-09, 3.551637292421446e-10, 4.018224009000073e-11, 4.167265015831182e-12, 3.9893853618162423e-13, 3.546305748665345e-14, 2.942274168638325e-15, 2.288555127057504e-16], [3.481446553280927e-05, 4.332693367063108e-05, 2.6960390638916508e-05, 1.118415424038615e-05, 3.4796965967971883e-06, 8.661031059130957e-07, 1.7964559294306353e-07, 3.193866429019739e-08, 4.968496457046832e-09, 5.744452020332491e-10, 7.315866209972302e-11, 8.276968291292167e-12, 8.58397150586664e-13, 8.217564791693914e-14, 7.304883990336453e-15, 6.060665095714179e-16, 4.714097117806737e-17], [6.454154969537101e-06, 8.032257281145834e-06, 4.998110313049045e-06, 2.073398616521371e-06, 6.450910774871711e-07, 1.6056439700022178e-07, 3.330398668209435e-08, 5.921018338043719e-09, 9.210954587010915e-10, 1.2736800711586742e-10, 1.3253374957896495e-11, 1.53444366335598e-12, 1.5913581181001542e-13, 1.5234310171391756e-14, 1.3542317133575029e-15, 1.1235695032956984e-16, 8.739330871272394e-18], [1.0877431585166709e-06, 1.3537067123813927e-06, 8.423504431162795e-07, 3.4943771425445124e-07, 1.0871964021141936e-07, 2.7060525376705076e-08, 5.612846892546279e-09, 9.978916247064837e-10, 1.5523570293428286e-10, 2.146581217961116e-11, 2.671440753889375e-12, 2.527080015177304e-13, 2.6819760509059416e-14, 2.5674959374024455e-15, 2.282337948505414e-16, 1.8935941979954104e-17, 1.4728724999799432e-18], [1.680446811566557e-07, 2.091332049120577e-07, 1.3013413187417757e-07, 5.398438851693303e-08, 1.679602131417523e-08, 4.180561673273261e-09, 8.671247978477722e-10, 1.5416358042773032e-10, 2.3982255369267934e-11, 3.3162383373759737e-12, 4.1270901701502714e-13, 4.669275447803291e-14, 4.048875099062447e-15, 3.9665065488452834e-16, 3.525967962614861e-17, 2.9254004564475048e-18, 2.275430442431439e-19], [2.3964097359061478e-08, 2.9823547219879424e-08, 1.8557844166829316e-08, 7.698471224347612e-09, 2.3952051754767792e-09, 5.961711270140575e-10, 1.2365677351435464e-10, 2.1984575918517905e-11, 3.420001743603231e-12, 4.72913857408229e-13, 5.885457960725792e-14, 6.6586440378390786e-15, 6.905621560572176e-16, 5.5274593030462146e-17, 5.028224574526352e-18, 4.171782223038498e-19, 3.2448891735743954e-20], [3.1733114319288016e-09, 3.949216276144283e-09, 2.4574186193699825e-09, 1.0194269526851045e-09, 3.171716360216443e-10, 7.894462388437223e-11, 1.637455595130749e-11, 2.911184387337664e-12, 4.5287458432432286e-13, 6.262297000156459e-14, 7.79348821241768e-15, 8.817336588907445e-16, 9.144382746572149e-17, 8.754054885742305e-18, 6.506498903112831e-19, 5.524249055381021e-20, 4.296862825902365e-21], [3.921941341494145e-10, 4.880893323003455e-10, 3.037159094973077e-10, 1.2599244656988996e-10, 3.919969969372139e-11, 9.756879863273763e-12, 2.0237549736808406e-12, 3.5979747485648164e-13, 5.5971422688064376e-14, 7.739663132496301e-15, 9.63208442360472e-16, 1.0897473390717913e-16, 1.1301674451293424e-17, 1.0819262621580555e-18, 9.617625210757596e-20, 6.6717954274934075e-21, 5.310554705118508e-22], [4.5442348482239756e-11, 5.655343514241884e-11, 3.519064411534278e-11, 1.4598363832177325e-11, 4.54195067895279e-12, 1.1305001687692784e-12, 2.344863697569609e-13, 4.1688645524793215e-14, 6.4852395111773226e-15, 8.96771365448443e-16, 1.1160404985074218e-16, 1.2626572920855543e-17, 1.309490846828537e-18, 1.2535952467443821e-19, 1.1143651532338296e-20, 9.245586921050314e-22, 6.012853666376e-23]] |
| Legacy trial inputs | {"lambda_home": 1.8538716222584808, "lambda_away": 1.2445095165915911, "rho": -0.1036082449967548, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5476 |
| Legacy p draw | 0.2251 |
| Legacy p away | 0.2273 |
| Legacy p over 1 5 | 0.8285 |
| Legacy p under 3 5 | 0.6215 |
| Legacy p btts yes | 0.6048 |
| Legacy p over 2 5 | 0.6082 |
| Legacy goal margin distribution | {"-1": 0.13007872463295275, "-10": 1.2636366743502335e-07, "-11": 1.4054322881562071e-08, "-12": 1.4365775409641332e-09, "-13": 1.3582011888468528e-10, "-14": 1.1938457012420547e-11, "-15": 9.728982555222515e-13, "-16": 6.613702396809123e-14, "-2": 0.06564878608751239, "-3": 0.023205097313385693, "-4": 0.006518923399730816, "-5": 0.0015121170243730807, "-6": 0.00029790470947411025, "-7": 5.0928968896331016e-05, "-8": 7.682551225582964e-06, "-9": 1.0363051216125875e-06, "0": 0.22506979731525462, "1": 0.23218171391468387, "10": 7.946021448019272e-06, "11": 1.3164939647481056e-06, "12": 2.0045618139315394e-07, "13": 2.8231627908535246e-08, "14": 3.6965914083444896e-09, "15": 4.4874756929183337e-10, "16": 4.5442348482239756e-11, "2": 0.1702561206446294, "3": 0.08964805309593186, "4": 0.0375158491507309, "5": 0.012963006555811039, "6": 0.0038043384026354935, "7": 0.0009688311427765634, "8": 0.00021770585364423487, "9": 4.37455338608313e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5059 |
| Legacy raw p draw | 0.2487 |
| Legacy raw p away | 0.2454 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8539 |
| Legacy lambda away | 1.2445 |
| Legacy model home team | Ajax |
| Legacy model away team | AZ Alkmaar |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 77.9% |
| Market reference home draw last update utc | 2026-10-30T07:26:44Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.0% |
| Market reference draw away last update utc | 2026-10-30T07:26:44Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.2% |
| Market reference home away last update utc | 2026-10-30T07:26:44Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.21 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 88.8% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:26:45Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.82 |
| Market reference over 1 5 last update utc | 2026-10-30T07:26:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.7% |
| Market under 3 5 odds | 1.86 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 1.98 |
| Market reference under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.2% |
| Market reference btts yes odds | 1.38 |
| Market reference btts yes opposite odds | 2.81 |
| Market reference btts yes last update utc | 2026-10-30T07:26:44Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,582.8938 |
| Elo away rating | 1,549.1473 |
| Elo rating diff | 93.7465 |
| Elo home expectancy | 0.6317 |

</details>


---

## 2026-10-31 — Feyenoord vs Fortuna Sittard

The model's most likely 1X2 outcome is **Feyenoord win** at **82.4%**. Expected goals are 2.73 for Feyenoord and 0.83 for Fortuna Sittard (3.56 combined). The most likely exact score is 3-0 at 9.0%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 77.9%; Under 3.5 goals: 41.5%; Double Chance 1X: 93.7%; Double Chance X2: 17.6%; Double Chance 12 (either team wins): 88.7%; Under 4.5 goals: 60.9%; BTTS Yes (both teams score): 58.3%; BTTS No (at least one team does not score): 41.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 82.4% | 1.21 |
| Draw | 11.3% | 8.86 |
| Fortuna Sittard win | 6.3% | 15.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 2.73 |
| Fortuna Sittard expected goals | 0.83 |
| Expected total goals | 3.56 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 92.1% |
| Under 1.5 | 7.9% |
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 58.5% |
| Under 3.5 | 41.5% |
| Over 4.5 | 39.1% |
| Under 4.5 | 60.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 8.99% |
| 2 | 2-0 | 8.66% |
| 3 | 3-1 | 8.53% |
| 4 | 2-1 | 8.22% |
| 5 | 4-0 | 6.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 82.4% | 84.9% | 1.16 | -4.4% |
| Draw | 11.3% | 9.6% | 8.41 | -5.1% |
| Fortuna Sittard win | 6.3% | 5.5% | 14.00 | -11.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:30:00+00:00 |
| Fixture id | 1836e9e3241ea98ae062bab0f288ce2c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:26:45Z |
| Market best draw last update utc | 2026-10-30T07:26:45Z |
| Market best away last update utc | 2026-10-30T07:26:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Feyenoord |
| Matched away-team name | For Sittard |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7317 |
| Dc lambda away | 0.8329 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 58.3% |
| P btts no | 41.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 52.27 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.62 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.53 |
| Fair Over 3.5 odds | 1.71 |
| Fair Under 3.5 odds | 2.41 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
| Goal margin distribution | {"-1": 0.04223010376654307, "-10": 3.0428081952789643e-09, "-11": 2.568759711592439e-10, "-12": 1.994352721220291e-11, "-13": 1.4329820340971458e-12, "-14": 9.580717658549371e-14, "-15": 5.9886578259608446e-15, "-16": 3.514322851262457e-16, "-17": 1.9432418261047964e-17, "-18": 1.0153791057333932e-18, "-19": 4.9880205278196804e-20, "-2": 0.015628590639383187, "-20": 2.062294539289759e-21, "-3": 0.004062979204885901, "-4": 0.0008491510117944182, "-5": 0.00014755622640061158, "-6": 2.1874961810202928e-05, "-7": 2.8225175661327903e-06, "-8": 3.220288380637469e-07, "-9": 3.290483943468075e-08, "0": 0.11288030458765441, "1": 0.1848548387126605, "10": 0.0005484468065798088, "11": 0.00015185275635637966, "12": 3.866699585599549e-05, "13": 9.112099864369624e-06, "14": 1.998089927727608e-06, "15": 4.096243372698971e-07, "16": 7.88382856979369e-08, "17": 1.4297550159058163e-08, "18": 2.4502041158217038e-09, "19": 3.94767633609515e-10, "2": 0.21040964454800684, "20": 5.353074178394242e-11, "3": 0.17940299537178225, "4": 0.12297286330181853, "5": 0.07008436736229418, "6": 0.03407612356013352, "7": 0.014420449493315833, "8": 0.0053960525797693, "9": 0.0018083414920809203} |
| Raw goal margin distribution | {"-1": 0.056584168068161564, "-10": 1.5387635070893341e-09, "-11": 1.1456641489422958e-10, "-12": 7.838980700299383e-12, "-13": 4.961045607686916e-13, "-14": 2.9201430533108785e-14, "-15": 1.606364876137126e-15, "-16": 8.293253640259396e-17, "-17": 4.032424993634281e-18, "-18": 1.8425042624023487e-19, "-19": 7.213222661600304e-21, "-2": 0.019737685866766892, "-3": 0.004677994991445379, "-4": 0.0008806344327563251, "-5": 0.00013683340129249096, "-6": 1.805393375100229e-05, "-7": 2.066716122912132e-06, "-8": 2.0873563957156916e-07, "-9": 1.885039756802319e-08, "0": 0.15236444032247443, "1": 0.19960902690162385, "10": 0.0002215973247540059, "11": 5.411145619467381e-05, "12": 1.2143133149648183e-05, "13": 2.5204822593585753e-06, "14": 4.86579509474728e-07, "15": 8.778759509770868e-08, "16": 1.4864597838108802e-08, "17": 2.370466254893376e-09, "18": 3.5523458724521486e-10, "19": 4.561160396006449e-11, "2": 0.21231210669968253, "3": 0.16503556448031736, "4": 0.10189496308434295, "5": 0.05192642694989786, "6": 0.022470225221487613, "7": 0.0084363710351824, "8": 0.0027945424743396835, "9": 0.0008277017732491273} |
| Unadjusted home-win probability | 76.6% |
| Unadjusted draw probability | 15.2% |
| Unadjusted away-win probability | 8.2% |
| Raw p over 1 5 | 87.7% |
| Raw p under 3 5 | 52.3% |
| Raw p btts yes | 53.5% |
| P home draw | 93.7% |
| P draw away | 17.6% |
| P home away | 88.7% |
| Raw p home draw | 91.8% |
| Raw p draw away | 23.4% |
| Raw p home away | 84.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1394 |
| Totals anchor target over 2 5 | 0.7794 |
| Totals anchor reference over odds | 1.25 |
| Totals anchor reference under odds | 3.87 |
| Totals anchor reference last update utc | 2026-10-30T07:26:45Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7110 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:23:10Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 4.4, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:23:10Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:23:10Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:23:10Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.76, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:23:10Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:23:10Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:23:10Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:23:10Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.39, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.41 |
| Reference away odds | 14.00 |
| Market reference 1x2 last update utc | 2026-10-30T07:26:45Z |
| Market reference home last update utc | 2026-10-30T07:26:45Z |
| Market reference draw last update utc | 2026-10-30T07:26:45Z |
| Market reference away last update utc | 2026-10-30T07:26:45Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.24 |
| Reference Under 2.5 odds | 3.89 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:23Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:23Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.0837 |
| Raw ev home | -0.1119 |
| Raw edge prob draw | 0.0564 |
| Raw ev draw | 0.2814 |
| Raw edge prob away | 0.0273 |
| Raw ev away | 0.1485 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.028263531650112923, 0.01431360211327666, 0.008581580744955844, 0.002470549318832086, 0.0005334344089551319, 9.214218602746337e-05, 1.3263396435420944e-05, 1.6364555004219635e-06, 1.766695499650326e-07, 1.695378545034902e-08, 1.464246425249964e-09, 1.1496588235204495e-10, 8.274375397001406e-12, 5.497172403322232e-13, 3.3912422281823086e-14, 1.95260789960056e-15, 1.0540047034326552e-16, 5.354773643213802e-18, 2.569307599985367e-19, 1.1679116488278156e-20], [0.07406731008561998, 0.058579544281491425, 0.023168728365085853, 0.006670039912426765, 0.0014401771991641573, 0.00024876737077726967, 3.580879075120759e-05, 4.418136249910936e-06, 4.769760881091453e-07, 4.577217898811512e-08, 3.953202643476259e-09, 3.103872559880753e-10, 2.2339329042211486e-11, 1.4841379225322934e-12, 9.155745583486749e-14, 5.271691005874115e-15, 2.845623597226867e-16, 1.44569281212048e-17, 6.936669553030922e-19, 3.153151913418305e-20], [0.10981041876134379, 0.09483988906040408, 0.030942361469880168, 0.009003955536171553, 0.001944110025687126, 0.00033581363451150586, 4.833865523461877e-05, 5.964087602059393e-06, 6.438749311155555e-07, 6.178833557425125e-08, 5.336468940916085e-09, 4.1899495184491706e-10, 3.015609022507278e-11, 2.0034530586736596e-12, 1.2359435208270037e-13, 7.116309953242304e-15, 3.841336585464184e-16, 1.9515556083921012e-17, 9.363881632588534e-19, 4.2564722250489816e-20], [0.09882280974995332, 0.08535022832116097, 0.03685718657922368, 0.008016657696782675, 0.0017495827569786843, 0.00030221218796092303, 4.350189885170472e-05, 5.36732216376768e-06, 5.794489315142847e-07, 5.56058068086524e-08, 4.802502903033565e-09, 3.770703989605146e-10, 2.7138677738690787e-11, 1.8029879376980007e-12, 1.1122752540068704e-13, 6.404253371980832e-15, 3.45697319847118e-16, 1.7562833361352983e-17, 8.426933468940856e-19, 3.8305704472010574e-20], [0.06670096405947781, 0.057607575883771835, 0.02487694777728608, 0.007161818808489431, 0.0011683036987365396, 0.00020397967168229802, 2.936183052443483e-05, 3.622701718833447e-06, 3.911020386187247e-07, 3.753142549606512e-08, 3.24147405180342e-09, 2.5450560647482627e-10, 1.8317390216392022e-11, 1.2169359881221468e-12, 7.507359073221842e-14, 4.322583774668326e-15, 2.3333018525706625e-16, 1.1854124769193342e-17, 5.687802116390445e-19, 2.5854632384217975e-20], [0.0360161271894284, 0.03110602386877731, 0.013432659150661724, 0.003867125172046805, 0.000834979336288451, 0.00010896778855092356, 1.5854334904957364e-05, 1.956128936285239e-06, 2.1118106710385976e-07, 2.0265623043491274e-08, 1.750279675521346e-09, 1.3742389517858063e-10, 9.890733441628925e-12, 6.571017667828158e-13, 4.053704516126059e-14, 2.3340401328621025e-15, 1.2598992754973952e-16, 6.400802018782146e-18, 3.071209049835464e-19, 1.396057375655867e-20], [0.016206180275600307, 0.013996780603953988, 0.006044294952407153, 0.0017400906920635802, 0.00037571573365233034, 6.489883000132785e-05, 7.057941114469259e-06, 8.80199528867223e-07, 9.502516542876287e-08, 9.118924383868267e-09, 7.875735168589713e-10, 6.183664356041564e-11, 4.450534294536708e-12, 2.9567614629658336e-13, 1.8240458177756858e-14, 1.0502482669694743e-15, 5.66917000276538e-17, 2.8801695107090207e-18, 1.3819522366718572e-19, 6.281840739278975e-21], [0.006250539878043805, 0.00539839948966653, 0.0023312159924297983, 0.0006711332391218488, 0.00014490929608737711, 2.503074247374799e-05, 3.603047364247435e-06, 3.358646874437175e-07, 3.6650128273868696e-08, 3.5170656833954858e-09, 3.037581706671382e-10, 2.3849691903075015e-11, 1.7165205874258865e-12, 1.1403893526938137e-13, 7.035137786632838e-15, 4.050688418184914e-16, 2.1865345550330258e-17, 1.1108487056210907e-18, 5.3300329985063726e-20, 2.4228347075405447e-21], [0.002109417030403397, 0.0018218387599484374, 0.000786733116167107, 0.00022649241695846703, 4.890363760484424e-05, 8.44731423012539e-06, 1.2159476812860908e-06, 1.5002524285196813e-07, 1.2236769095584741e-08, 1.1869307922764051e-09, 1.025115703333414e-10, 8.04873614948687e-12, 5.79287202514002e-13, 3.848558314639357e-14, 2.374201228678852e-15, 1.3670164979174894e-16, 7.379063757602434e-18, 3.7488652557353955e-19, 1.7987666024106962e-20, 8.176523778195532e-22], [0.0006327830583845282, 0.0005465153100537857, 0.0002360042515089626, 6.794321001403617e-05, 1.4670116398844131e-05, 2.5340258737987304e-06, 3.6476006475241403e-07, 4.5004582137366765e-08, 4.858634573639653e-09, 3.52260656746011e-10, 3.07514275557581e-11, 2.4144603951682454e-12, 1.7377461279893407e-13, 1.1544907742794602e-14, 7.122130394559314e-16, 4.1007769822021e-17, 2.2135720273658495e-18, 1.1245848439661483e-19, 5.395941227305424e-21, 2.4527941363642716e-22], [0.00017084007281941417, 0.00014754932852481105, 6.371691368668336e-05, 1.834344771494991e-05, 3.9606682268740895e-06, 6.84141522232384e-07, 9.84786732170203e-08, 1.215042973682595e-08, 1.3117441647104257e-09, 1.2587924256698177e-10, 8.213845595246369e-12, 6.518609881610888e-13, 4.6916027714975366e-14, 3.1169179600157774e-15, 1.9228474263236157e-16, 1.107136211965174e-17, 5.976247330509223e-19, 3.0361773136795436e-20, 1.4568073212256488e-21, 6.622104105272451e-23], [4.193068597267087e-05, 3.6214246796722465e-05, 1.563856684706637e-05, 4.5021834344726746e-06, 9.720994197803931e-07, 1.6791448783748823e-07, 2.417043175832049e-08, 2.982180031416812e-09, 3.2195217280840387e-10, 3.0895579142799134e-11, 2.668356364916702e-12, 1.582863842547436e-13, 1.151498704452789e-14, 7.650108433408922e-16, 4.719402788581088e-17, 2.7173355798059938e-18, 1.4667995978641272e-19, 7.451940015959598e-21, 3.575562179347122e-22, 1.625317544848059e-23], [9.433777435017389e-06, 8.147664087340228e-06, 3.5184437272030744e-06, 1.0129239602738607e-06, 2.1870783551919145e-07, 3.777824926132248e-08, 5.437985771682507e-09, 6.70945920271272e-10, 7.243442535078745e-11, 6.9510433850068245e-12, 6.003402873099425e-13, 4.7135953110000195e-14, 2.563087665971476e-15, 1.7211600201715545e-16, 1.0617950672853848e-17, 6.113598783681146e-19, 3.3000797928853376e-20, 1.6765750890763415e-21, 8.044480318545548e-23, 3.656721473461937e-24], [1.9591928102439863e-06, 1.6920947107515354e-06, 7.307051391733e-07, 2.1036253547026316e-07, 4.542091668420143e-08, 7.845730392329504e-09, 1.1293527645185354e-09, 1.3934104679835368e-10, 1.5043073290519703e-11, 1.4435823102047026e-12, 1.2467777438034086e-13, 9.78912435376316e-15, 7.045471930788378e-16, 3.5363818288202033e-17, 2.2051201399518935e-18, 1.2696630659574605e-19, 6.85355643377069e-21, 3.4818861086969084e-22, 1.6706656597325847e-23, 7.594224550261737e-25], [3.7781922022810127e-07, 3.2631086681490237e-07, 1.4091234127423208e-07, 4.0567221715499904e-08, 8.759166139208843e-09, 1.5130046024314962e-09, 2.1778927455317986e-10, 2.6871130483867574e-11, 2.9009713544990675e-12, 2.7838666001877535e-13, 2.404340157326795e-14, 1.887777104283126e-15, 1.358679297469421e-16, 9.026535515563909e-18, 4.207125556712878e-19, 2.4484732029652997e-20, 1.3216694824814406e-21, 6.714619855853271e-23, 3.2217839587897646e-24, 1.4645031274179051e-25], [6.800294059823957e-08, 5.8732053068070506e-08, 2.5362535996567982e-08, 7.301614689928284e-09, 1.5765451378972152e-09, 2.723227316013593e-10, 3.9199464472538284e-11, 4.836482085264967e-12, 5.221401456974418e-13, 5.010626905949832e-14, 4.327524703426803e-15, 3.397772993332061e-16, 2.4454602257156115e-17, 1.6246684276734336e-18, 1.0022687619167507e-19, 4.359988555932807e-21, 2.3788469854294233e-22, 1.2085512614251801e-23, 5.7988257727510395e-25, 2.6359304621826793e-26], [1.1474733688150685e-08, 9.910375374736208e-09, 4.2796435515361685e-09, 1.2320656036833942e-09, 2.660243137366278e-10, 4.595140731952745e-11, 6.614470074138903e-12, 8.161021189334256e-13, 8.810529466905798e-14, 8.454871046847819e-15, 7.30221267843252e-16, 5.733360923554727e-17, 4.1264399139495375e-18, 2.7414457926517626e-19, 1.6912161482682925e-20, 9.73767660592829e-22, 3.9712550331211947e-23, 2.0392947351002536e-24, 9.784868251421667e-26, 4.447837079976688e-27], [1.8223366025147003e-09, 1.5738962036819837e-09, 6.796629274049217e-10, 1.9566800479301326e-10, 4.224811287618136e-11, 7.297679734555346e-12, 1.0504636752301033e-12, 1.2960760599245524e-13, 1.399226402235081e-14, 1.3427432302087452e-15, 1.1596861247416988e-16, 9.105321090990067e-18, 6.55332201829929e-19, 4.353771640833942e-20, 2.685870690781966e-21, 1.5464693983058483e-22, 8.347738528879632e-24, 3.2041462421332016e-25, 1.553964043955384e-26, 7.0637424215201365e-28], [2.733323264496455e-10, 2.3606874292543954e-10, 1.0194266464977352e-10, 2.9348250420933575e-11, 6.336795828289204e-12, 1.0945792214116236e-12, 1.5755908091034066e-13, 1.9439849050170764e-14, 2.098700137092796e-15, 2.0139810089475922e-16, 1.7394135967505232e-17, 1.3657074074224234e-18, 9.82932983271943e-20, 6.530223504140104e-21, 4.0285383251441827e-22, 2.3195499549250325e-23, 1.252077574221695e-24, 6.361064587156076e-26, 2.3059490841650406e-27, 1.0594909561992277e-28], [3.8839381161498384e-11, 3.354438169056463e-11, 1.4485626564484597e-11, 4.1702637200936264e-12, 9.00432201761024e-13, 1.555351324304265e-13, 2.238848685927182e-14, 2.7623212987237702e-15, 2.9821651769847487e-16, 2.861782836833424e-17, 2.471634019993321e-18, 1.9406131444804839e-19, 1.3967066863033762e-20, 9.279174660440244e-22, 5.724384582180186e-23, 3.295983537427158e-24, 1.779149900804708e-25, 9.038806909616622e-27, 4.336966758083182e-28, 1.489446492576152e-29]] |
| Legacy trial inputs | {"lambda_home": 2.699820587099197, "lambda_away": 0.8636693141706719, "rho": -0.1036082449967548, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8016 |
| Legacy p draw | 0.1271 |
| Legacy p away | 0.0713 |
| Legacy p over 1 5 | 0.8834 |
| Legacy p under 3 5 | 0.5129 |
| Legacy p btts yes | 0.5349 |
| Legacy p over 2 5 | 0.7064 |
| Legacy goal margin distribution | {"-1": 0.04845662084610292, "-10": 1.8066702248524566e-09, "-11": 1.3942434348632047e-10, "-12": 9.888751796593713e-12, "-13": 6.48748870967695e-13, "-14": 3.9586392520390364e-14, "-15": 2.2575543633864455e-15, "-16": 1.208320923322012e-16, "-17": 6.091005320767384e-18, "-18": 2.8846227913271974e-19, "-19": 1.1679116488278156e-20, "-2": 0.017529359477696214, "-3": 0.004293885365053621, "-4": 0.0008363199368066861, "-5": 0.00013453385860978935, "-6": 1.8384396888192113e-05, "-7": 2.1802871261985405e-06, "-8": 2.2817426143802748e-07, "-9": 2.1354380268936133e-08, "0": 0.12708677298876106, "1": 0.21382984075986408, "10": 0.0002107921641138858, "11": 5.085124598764686e-05, "12": 1.1274359584047958e-05, "13": 2.3121416437397247e-06, "14": 4.4103307718346164e-07, "15": 7.86232275830034e-08, "16": 1.3154742820202537e-08, "17": 2.0728909720046245e-09, "18": 3.0687670814021013e-10, "19": 3.8839381161498384e-11, "2": 0.22430672880347718, "3": 0.17175686932629228, "4": 0.1045739553180184, "5": 0.052585995317395245, "6": 0.02246339025444133, "7": 0.008327737371639804, "8": 0.002724378213859472, "9": 0.0007970308516677289} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7540 |
| Legacy raw p draw | 0.1582 |
| Legacy raw p away | 0.0878 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.6998 |
| Legacy lambda away | 0.8637 |
| Legacy model home team | Feyenoord |
| Legacy model away team | For Sittard |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 93.0% |
| Market reference home draw last update utc | 2026-10-30T07:25:59Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 17.4% |
| Market reference draw away last update utc | 2026-10-30T07:25:59Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 89.6% |
| Market reference home away last update utc | 2026-10-30T07:25:59Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.03 |
| Market reference dc draw away odds | 5.50 |
| Market reference dc home away odds | 1.07 |
| Market p over 1 5 | 91.5% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.60 |
| Market reference over 1 5 last update utc | 2026-10-30T07:26:02Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 42.9% |
| Market under 3 5 odds | 2.19 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market reference under 3 5 odds | 2.19 |
| Market reference under 3 5 opposite odds | 1.68 |
| Market reference under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.1% |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-30T07:26:44Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,614.9048 |
| Elo away rating | 1,453.3704 |
| Elo rating diff | 221.5344 |
| Elo home expectancy | 0.7816 |

</details>


---

## 2026-10-31 — Heerenveen vs NEC Nijmegen

The model's most likely 1X2 outcome is **Heerenveen win** at **43.6%**. Expected goals are 1.62 for Heerenveen and 1.62 for NEC Nijmegen (3.24 combined). The most likely exact score is 1-1 at 9.8%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 70.5%; Under 3.5 goals: 50.3%; Double Chance 1X: 67.9%; Double Chance X2: 56.4%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 71.5%; BTTS No (at least one team does not score): 28.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Heerenveen win | 43.6% | 2.30 |
| Draw | 24.3% | 4.12 |
| NEC Nijmegen win | 32.1% | 3.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Heerenveen expected goals | 1.62 |
| NEC Nijmegen expected goals | 1.62 |
| Expected total goals | 3.24 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 49.7% |
| Under 3.5 | 50.3% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.81% |
| 2 | 2-1 | 8.98% |
| 3 | 2-2 | 7.50% |
| 4 | 1-2 | 6.60% |
| 5 | 3-1 | 5.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Heerenveen win | 43.6% | 46.3% | 2.09 | -9.0% |
| Draw | 24.3% | 23.9% | 3.93 | -4.5% |
| NEC Nijmegen win | 32.1% | 29.8% | 3.18 | +2.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:45:00+00:00 |
| Fixture id | c27c8af8c7ee29d153de0b9999ea0434 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:26:45Z |
| Market best draw last update utc | 2026-10-30T07:26:45Z |
| Market best away last update utc | 2026-10-30T07:26:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Heerenveen |
| Matched away-team name | Nijmegen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.6167 |
| Dc lambda away | 1.6241 |
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
| P btts yes | 71.5% |
| P btts no | 28.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.32 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.92 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.14764751237484303, "-10": 3.446664589802607e-06, "-11": 5.607325624881377e-07, "-12": 8.393034818540294e-08, "-13": 1.162935168409353e-08, "-14": 1.4980619675257816e-09, "-15": 1.776842238046197e-10, "-16": 1.6842715908132524e-11, "-2": 0.09777902365024296, "-3": 0.04811846656490931, "-4": 0.019157046941959563, "-5": 0.00636620732755464, "-6": 0.001809519502873154, "-7": 0.0004484408288583225, "-8": 9.839072020942717e-05, "-9": 1.9351015821747275e-05, "0": 0.24300555729843018, "1": 0.2008553609259055, "10": 4.5006637676127245e-06, "11": 7.28865664117773e-07, "12": 1.085987702767462e-07, "13": 1.4978749400199864e-08, "14": 1.9207197276058434e-09, "15": 2.267760863327972e-10, "16": 2.1398073643123382e-11, "2": 0.13243717236686725, "3": 0.06487690898517612, "4": 0.025711126350058747, "5": 0.008505257865376132, "6": 0.002406490454265572, "7": 0.0005936632832473686, "8": 0.00012965920383617416, "9": 2.5384414278348368e-05} |
| Raw goal margin distribution | {"-1": 0.18282581208405804, "-10": 1.7444464554824529e-06, "-11": 2.526234618371934e-07, "-12": 3.363208570941455e-08, "-13": 4.139714032211897e-09, "-14": 4.687145242233232e-10, "-15": 4.3190136458399594e-11, "-2": 0.11450883413303876, "-3": 0.051870488413497826, "-4": 0.018783376013024867, "-5": 0.0056359364396742825, "-6": 0.0014395008263597211, "-7": 0.0003195252131315188, "-8": 6.264808949447631e-05, "-9": 1.0992160111528332e-05, "0": 0.2522292856755179, "1": 0.1819469593981976, "10": 1.6664769962300218e-06, "11": 2.4023126580485585e-07, "12": 3.183639001948223e-08, "13": 3.9008075525175345e-09, "14": 4.396496812536648e-10, "15": 4.0327109586035146e-11, "2": 0.11346641379792308, "3": 0.05116380572274383, "4": 0.018442947256778162, "5": 0.005508545314255642, "6": 0.001400544544624759, "7": 0.0003094598486779859, "8": 6.0397807687987663e-05, "9": 1.0548982144028733e-05} |
| Unadjusted home-win probability | 37.2% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 37.5% |
| Raw p over 1 5 | 84.4% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 65.3% |
| P home draw | 67.9% |
| P draw away | 56.4% |
| P home away | 75.7% |
| Raw p home draw | 62.5% |
| Raw p draw away | 62.8% |
| Raw p home away | 74.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1292 |
| Totals anchor target over 2 5 | 0.7046 |
| Totals anchor reference over odds | 1.38 |
| Totals anchor reference under odds | 3.07 |
| Totals anchor reference last update utc | 2026-10-30T07:26:45Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6319 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.35, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.89, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.09 |
| Reference draw odds | 3.93 |
| Reference away odds | 3.18 |
| Market reference 1x2 last update utc | 2026-10-30T07:26:45Z |
| Market reference home last update utc | 2026-10-30T07:26:45Z |
| Market reference draw last update utc | 2026-10-30T07:26:45Z |
| Market reference away last update utc | 2026-10-30T07:26:45Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.04 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:23Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:23Z |
| Home probability edge | -2.7% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.0903 |
| Raw ev home | -0.2219 |
| Raw edge prob draw | 0.0132 |
| Raw ev draw | -0.0087 |
| Raw edge prob away | 0.0772 |
| Raw ev away | 0.1940 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.047389897427907036, 0.046427826580273245, 0.04537590797001367, 0.024528345097769425, 0.009944259081815923, 0.0032252738875651692, 0.0008717250462657676, 0.00020195083742902782, 4.0937361268750434e-05, 7.376349914258026e-06, 1.196205195795014e-06, 1.7635069415086593e-07, 2.3831978674796825e-08, 2.9729042608879952e-09, 3.4436345935826976e-10, 3.722973775327301e-11], [0.058009171989954686, 0.10927114855989536, 0.07461234938440946, 0.040332359970968706, 0.016351508238068937, 0.005303370729649168, 0.0014333917849556664, 0.0003320710728408188, 6.731397427635605e-05, 1.2129053094606603e-05, 1.966939814473461e-06, 2.899763375503774e-07, 3.9187313245187725e-08, 4.888395215063458e-09, 5.662424818439478e-10, 6.121746814571364e-11], [0.05732428792273978, 0.09296144008283304, 0.0660055024426374, 0.03315958036189992, 0.013443526534246908, 0.004360209718085725, 0.0011784748057772285, 0.0002730149545836998, 5.5342735736325975e-05, 9.972000425808423e-06, 1.6171356918365504e-06, 2.3840642290638104e-07, 3.221817081014062e-08, 4.0190341971385155e-09, 4.655408980417041e-10, 5.033044324683698e-11], [0.03141975547560344, 0.05095267332407495, 0.041314371795250854, 0.01955632260729176, 0.007368470359459398, 0.0023898547741097805, 0.0006459284811628946, 0.00014964098857650222, 3.0333655893465034e-05, 5.465707928265867e-06, 8.863609100012834e-07, 1.3067186323583348e-07, 1.765895548655009e-08, 2.2028546066263114e-09, 2.5516551029953163e-10, 2.7586390988854235e-11], [0.01291600475888907, 0.020945579020908427, 0.016983474716482462, 0.009180566239697393, 0.0032592432239603583, 0.0009824193463066045, 0.0002655276977912797, 6.151428269642978e-05, 1.246953192168257e-05, 2.2468382883181496e-06, 3.6436444391042636e-07, 5.371647175031086e-08, 7.25922750348555e-09, 9.055474860209652e-10, 1.048932079656744e-10, 1.1340188741101994e-11], [0.004247599674954279, 0.00688823179472041, 0.005585241181927989, 0.00301915111550245, 0.001224021464963822, 0.0003476372643260284, 8.732230932737799e-05, 2.022978870510068e-05, 4.100771153782585e-06, 7.389026065948795e-07, 1.1982608572931045e-07, 1.766537502932417e-08, 2.3872933588851123e-09, 2.9780131542852977e-10, 3.4495524303153964e-11, 3.729371652443405e-12], [0.0011640662970396432, 0.001887738744710501, 0.0015306506069902215, 0.0008274066127156568, 0.00033544642698297896, 0.00010879710521657797, 2.5749771761015148e-05, 5.544028870398297e-06, 1.1238275396190818e-06, 2.0249827831082032e-07, 3.283866620626735e-08, 4.841244295561659e-09, 6.542442680299521e-10, 8.16132642038953e-11, 9.45359269066374e-12, 1.0220444914670866e-12], [0.0002734418994790118, 0.0004434342523157731, 0.000359553412446108, 0.00019435975115664677, 7.879715133145e-05, 2.555669482390816e-05, 6.907447787198598e-06, 1.4012862641421848e-06, 2.639897211196389e-07, 4.7567319836813876e-08, 7.713879601733006e-09, 1.1372196234758161e-09, 1.5368351083466968e-10, 1.9171146904045763e-11, 2.2206710638474577e-12, 2.4008064472749125e-13], [5.6203124777544935e-05, 9.114327636337118e-05, 7.390244634199437e-05, 3.994861565401044e-05, 1.6195930970471114e-05, 5.252911535600258e-06, 1.4197537049661166e-06, 3.289115655092215e-07, 5.83843503319387e-08, 9.776965480475093e-09, 1.5855073366634355e-09, 2.3374360885973087e-10, 3.158803955117747e-11, 3.9404288941440405e-12, 4.564357295977674e-13, 4.934606751196999e-14], [1.0268413276267308e-05, 1.6652042617852158e-05, 1.350211156711269e-05, 7.298684850242228e-06, 2.9590260907546474e-06, 9.597165062389178e-07, 2.5939158811554947e-07, 6.00927421626589e-08, 1.218137209461772e-08, 1.9220336824709966e-09, 2.8967507856286864e-10, 4.2705383125189596e-11, 5.771192366659301e-12, 7.199235368312103e-13, 8.339163923919464e-14, 9.015616423055924e-15], [1.688452029430835e-06, 2.7381226676242432e-06, 2.220174340838393e-06, 1.2001347156575796e-06, 4.865575112389364e-07, 1.5780775851538564e-07, 4.2652184089944837e-08, 9.881148112056571e-09, 2.0030029841072026e-09, 3.60913611238449e-10, 5.125196904642119e-11, 7.022116160049913e-12, 9.489666223547091e-13, 1.1837820743026728e-13, 1.3712223955419703e-14, 1.4824525889760723e-15], [2.523953957360352e-07, 4.0930363565128384e-07, 3.318790060904432e-07, 1.7940010803686091e-07, 7.273222659389878e-08, 2.358962586229579e-08, 6.375789595880155e-09, 1.4770667123481089e-09, 2.9941551315770196e-10, 5.395056071907275e-11, 8.74903465784144e-12, 1.1294701192320505e-12, 1.4185467044050056e-13, 1.769556611031257e-14, 2.0497486048306285e-15, 2.2160191781146052e-16], [3.4584823922638726e-08, 5.608538986463959e-08, 4.547617422174545e-08, 2.4582544899694312e-08, 9.966232715600667e-09, 3.2324007118642717e-09, 8.736512799620176e-10, 2.0239708422405577e-10, 4.102781975110014e-11, 7.3926492896414e-12, 1.1988484268982618e-12, 1.7674037281260183e-13, 2.0915190031121218e-14, 2.4247591219002438e-15, 2.8086960293792907e-16, 3.0365305540057444e-17], [4.374491767100943e-09, 7.0940096953020255e-09, 5.752093755841084e-09, 3.1093447379881106e-09, 1.2605876803342371e-09, 4.088530372064601e-10, 1.105045478924461e-10, 2.5600372597062962e-11, 5.189439741684117e-12, 9.350657249821138e-13, 1.5163739405466465e-13, 2.2355160966338926e-14, 3.021069590832815e-15, 3.300081543808536e-16, 3.552603790695077e-17, 3.840782286115255e-18], [5.137891806907283e-10, 8.33199745984847e-10, 6.755901474763591e-10, 3.651961806010354e-10, 1.4805749923652973e-10, 4.8020267997540765e-11, 1.297888855369495e-11, 3.006793740233558e-12, 6.095057746309988e-13, 1.0982456438566572e-13, 1.7809989503090426e-14, 2.625639833976989e-15, 3.548281611951308e-16, 4.4262801955912284e-17, 4.489708666941702e-18, 4.511043771611431e-19], [5.632213153723115e-11, 9.13362668070542e-11, 7.405893035790729e-11, 4.003320446151449e-11, 1.623022488691306e-11, 5.26403426201884e-12, 1.4227599486340494e-12, 3.296080161031965e-13, 6.681468917916545e-14, 1.2039088781575428e-14, 1.9523505148964432e-15, 2.87825508314201e-16, 3.8896650842431124e-17, 4.8521367277835545e-18, 5.620425154087435e-19, 5.3209013099943e-20]] |
| Legacy trial inputs | {"lambda_home": 1.6443163943676118, "lambda_away": 1.621676316470326, "rho": -0.1036082449967548, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4206 |
| Legacy p draw | 0.2459 |
| Legacy p away | 0.3336 |
| Legacy p over 1 5 | 0.8482 |
| Legacy p under 3 5 | 0.5873 |
| Legacy p btts yes | 0.6566 |
| Legacy p over 2 5 | 0.6362 |
| Legacy goal margin distribution | {"-1": 0.16264378643407448, "-10": 1.5207111813417766e-06, "-11": 2.1982354729223282e-07, "-12": 2.921350117889084e-08, "-13": 3.58947718597878e-09, "-14": 4.055809275039834e-10, "-15": 3.722973775327301e-11, "-2": 0.10182857975987455, "-3": 0.045951817040730356, "-4": 0.016588988048554826, "-5": 0.004964385946325156, "-6": 0.0012649872664709841, "-7": 0.0002801793606895841, "-8": 5.482178864092167e-05, "-9": 9.60029617217923e-06, "0": 0.24585696294282983, "1": 0.20280561758848364, "10": 2.1464945055753513e-06, "11": 3.1461430576200384e-07, "12": 4.239445696987863e-08, "13": 5.2817504434436974e-09, "14": 6.051254474977825e-10, "15": 5.632213153723115e-11, "2": 0.12864207210522877, "3": 0.05886230193372125, "4": 0.021546446730464842, "5": 0.006537963865102065, "6": 0.0016892127275579514, "7": 0.00037936350033061534, "8": 7.526513023852173e-05, "9": 1.3364307525589969e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3785 |
| Legacy raw p draw | 0.2527 |
| Legacy raw p away | 0.3689 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6443 |
| Legacy lambda away | 1.6217 |
| Legacy model home team | Heerenveen |
| Legacy model away team | Nijmegen |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Market p home draw | 69.0% |
| Market reference home draw last update utc | 2026-10-30T07:26:44Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.1% |
| Market reference draw away last update utc | 2026-10-30T07:26:44Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market reference home away last update utc | 2026-10-30T07:26:44Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.38 |
| Market reference dc draw away odds | 1.76 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 88.9% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:26:45Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.96 |
| Market reference over 1 5 last update utc | 2026-10-30T07:26:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 50.4% |
| Market under 3 5 odds | 1.91 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market reference under 3 5 odds | 1.91 |
| Market reference under 3 5 opposite odds | 1.94 |
| Market reference under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 72.1% |
| Market reference btts yes odds | 1.33 |
| Market reference btts yes opposite odds | 3.04 |
| Market reference btts yes last update utc | 2026-10-30T07:26:44Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,510.9156 |
| Elo away rating | 1,535.4128 |
| Elo rating diff | 35.5028 |
| Elo home expectancy | 0.5509 |

</details>


---

## 2026-10-31 — PSV Eindhoven vs Willem II

The model's most likely 1X2 outcome is **PSV Eindhoven win** at **92.8%**. Expected goals are 4.46 for PSV Eindhoven and 0.68 for Willem II (5.14 combined). The most likely exact score is 4-0 at 9.6%. Goal-market probabilities: at least one goal: 99.3%; Over 2.5 goals: 88.6%; Under 3.5 goals: 24.9%; Double Chance 1X: 97.4%; Double Chance X2: 7.2%; Double Chance 12 (either team wins): 95.5%; Under 4.5 goals: 41.9%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PSV Eindhoven win | 92.8% | 1.08 |
| Draw | 4.5% | 22.16 |
| Willem II win | 2.6% | 37.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| PSV Eindhoven expected goals | 4.46 |
| Willem II expected goals | 0.68 |
| Expected total goals | 5.14 |
| Over 0.5 | 99.3% |
| Under 0.5 | 0.7% |
| Over 1.5 | 96.5% |
| Under 1.5 | 3.5% |
| Over 2.5 | 88.6% |
| Under 2.5 | 11.4% |
| Over 3.5 | 75.1% |
| Under 3.5 | 24.9% |
| Over 4.5 | 58.1% |
| Under 4.5 | 41.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-0 | 9.56% |
| 2 | 3-0 | 8.57% |
| 3 | 5-0 | 8.53% |
| 4 | 4-1 | 6.50% |
| 5 | 6-0 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 92.8% | 92.5% | 1.07 | -0.7% |
| Draw | 4.5% | 4.5% | 14.59 | -34.2% |
| Willem II win | 2.6% | 3.1% | 20.21 | -46.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:45:00+00:00 |
| Fixture id | 49a7de86105dbc67bec3e1390c7bcbb3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:26:45Z |
| Market best draw last update utc | 2026-10-30T07:26:45Z |
| Market best away last update utc | 2026-10-30T07:26:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | PSV Eindhoven |
| Matched away-team name | Willem II |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.4602 |
| Dc lambda away | 0.6804 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 24 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 135.01 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 28.36 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.76 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.01 |
| Fair Over 4.5 odds | 1.72 |
| Fair Under 4.5 odds | 2.39 |
| Goal margin distribution | {"-1": 0.019791166123623537, "-10": 7.254347701831122e-11, "-11": 4.387972922914448e-12, "-12": 2.4411573621856055e-13, "-13": 1.25694752287218e-14, "-14": 6.02255417686191e-16, "-15": 2.6979747452060176e-17, "-16": 1.1347289656992837e-18, "-17": 4.4971852060566317e-20, "-18": 1.6850305791798402e-21, "-19": 5.986463028807297e-23, "-2": 0.005419620691185458, "-20": 2.021993704239631e-24, "-21": 6.508421003618111e-26, "-22": 2.000269026586554e-27, "-23": 5.845257745141111e-29, "-24": 1.4710594409960568e-30, "-3": 0.0010057458485136226, "-4": 0.00015024488935393428, "-5": 1.8676678192954048e-05, "-6": 1.981747350628255e-06, "-7": 1.830855254157328e-07, "-8": 1.4960282361639526e-08, "-9": 1.0949989652061645e-09, "0": 0.04512908943029209, "1": 0.08911757815571784, "10": 0.006538285575726636, "11": 0.0025925922844491772, "12": 0.0009455202366886974, "13": 0.00031915155600958656, "14": 0.00010024559604460712, "15": 2.9439283395890573e-05, "16": 8.116826493167858e-06, "17": 2.1088207297060635e-06, "18": 5.179781529030372e-07, "19": 1.2063649980860823e-07, "2": 0.14321756061122015, "20": 2.671117480352086e-08, "21": 5.6362934413664554e-09, "22": 1.1355627426019576e-09, "23": 2.1753600983192917e-10, "24": 3.5889092847421526e-11, "3": 0.1742289807093527, "4": 0.17062262638835765, "5": 0.139040498942558, "6": 0.0967152002343953, "7": 0.05857404641084482, "8": 0.03137586979228018, "9": 0.01505478159811929} |
| Raw goal margin distribution | {"-1": 0.012289468408512931, "-10": 4.504639916068737e-11, "-11": 2.7247436698133312e-12, "-12": 1.5158544016756504e-13, "-13": 7.805106973993724e-15, "-14": 3.739748776437986e-16, "-15": 1.675327021715913e-17, "-16": 7.046181962739593e-19, "-17": 2.792559830574842e-20, "-18": 1.0463319816961587e-21, "-19": 3.717337715812575e-23, "-2": 0.0033653528475487437, "-20": 1.2555716826005489e-24, "-21": 4.041451312855862e-26, "-22": 1.2420815861587867e-27, "-23": 3.6296552689122214e-29, "-24": 9.134650487111247e-31, "-3": 0.0006245251924568359, "-4": 9.329565573459174e-05, "-5": 1.1597419030013552e-05, "-6": 1.2305804168926398e-06, "-7": 1.1368828731960975e-07, "-8": 9.289696034957066e-09, "-9": 6.79947563786691e-10, "0": 0.04601364123126735, "1": 0.08999269202398738, "10": 0.006602490017773157, "11": 0.0026180509370499665, "12": 0.0009548050252677808, "13": 0.00032228554998163744, "14": 0.00010122998445761241, "15": 2.972837030449849e-05, "16": 8.196531839492435e-06, "17": 2.1295288582756647e-06, "18": 5.230645777638435e-07, "19": 1.2182112214896788e-07, "2": 0.14462392371111968, "20": 2.697347232093644e-08, "21": 5.691640530664124e-09, "22": 1.146713704341568e-09, "23": 2.196721627996333e-10, "24": 3.6241515383136235e-11, "3": 0.17593986873423603, "4": 0.17229810085347522, "5": 0.1404058442694153, "6": 0.09766492098252534, "7": 0.059149229908821245, "8": 0.0316839735284058, "9": 0.015202616048212433} |
| Unadjusted home-win probability | 93.8% |
| Unadjusted draw probability | 4.6% |
| Unadjusted away-win probability | 1.6% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 24.6% |
| Raw p btts yes | 49.0% |
| P home draw | 97.4% |
| P draw away | 7.2% |
| P home away | 95.5% |
| Raw p home draw | 98.4% |
| Raw p draw away | 6.2% |
| Raw p home away | 95.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8858 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 7.14, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:20:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 2.88, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.07 |
| Reference draw odds | 14.59 |
| Reference away odds | 20.21 |
| Market reference 1x2 last update utc | 2026-10-30T07:26:45Z |
| Market reference home last update utc | 2026-10-30T07:26:45Z |
| Market reference draw last update utc | 2026-10-30T07:26:45Z |
| Market reference away last update utc | 2026-10-30T07:26:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.11 |
| Reference Under 2.5 odds | 6.50 |
| Market reference over 2 5 last update utc | 2026-10-30T07:25:59Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:25:59Z |
| Home probability edge | +0.4% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0130 |
| Raw ev home | 0.0032 |
| Raw edge prob draw | 0.0013 |
| Raw ev draw | -0.3287 |
| Raw edge prob away | -0.0143 |
| Raw ev away | -0.6688 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.006548425963491019, 0.0026299262635347143, 0.00176397581031577, 0.0004063440328533627, 7.02031195963413e-05, 9.703064600605044e-06, 1.1175840331225302e-06, 1.1033280625403364e-07, 9.530971992453334e-09, 7.318417810829014e-10, 5.0575445365531276e-11, 3.177382846749115e-12, 1.829830307644662e-13, 9.727247814468077e-15, 4.801583221890066e-16, 2.212155834625164e-17, 9.55472629519193e-19, 3.884112902189194e-20, 1.4912204686552254e-21, 5.423888726966553e-23, 1.874145444207321e-24, 6.167462432626912e-26, 1.9373422418494172e-27, 5.821045954947774e-29, 1.6761477644177798e-30], [0.019983329083594806, 0.017505602496184505, 0.008254586721822854, 0.0019015011648503728, 0.00032851796235616433, 4.5405831386546036e-05, 5.229773711399741e-06, 5.163062396660449e-07, 4.460051798606427e-08, 3.4246793030119247e-09, 2.366695718405903e-10, 1.4868674560921484e-11, 8.562755153637166e-13, 4.5518997584674934e-14, 2.2469177227575495e-15, 1.0351860877180071e-16, 4.471167707953113e-18, 1.817584266233921e-19, 6.978218526516169e-21, 2.538127768217418e-22, 8.770129390691134e-24, 2.88608569380495e-25, 9.065861023532966e-27, 2.723978887115863e-28, 7.843592298184233e-30], [0.0503623185956739, 0.034803925636058504, 0.012824113707123197, 0.00444907072282777, 0.0007686556680899315, 0.00010623909088345599, 1.2236454826591611e-05, 1.2080365857110862e-06, 1.043548447209951e-07, 8.012953504187584e-09, 5.537517843924174e-10, 3.4789242257159084e-11, 2.0034856651685237e-12, 1.0650387348165582e-13, 5.2572651764376316e-15, 2.422094816811336e-16, 1.046149311608361e-17, 4.25272468650318e-19, 1.6327409268908052e-20, 5.9386289911954285e-22, 2.0520064162361756e-23, 6.752769654437773e-25, 2.1212007440552793e-26, 6.373477408425254e-28, 1.835218273894396e-29], [0.07855741254668787, 0.0542887305563996, 0.018758677061020503, 0.004607974593465506, 0.0011989837264894641, 0.0001657165182985365, 1.9086973291258264e-05, 1.8843498687399576e-06, 1.6277738627976818e-07, 1.2498965728713767e-08, 8.637669707827235e-10, 5.426582676074552e-11, 3.125127164886699e-12, 1.661295381193466e-13, 8.200518976269354e-15, 3.778092571134858e-16, 1.6318308082128487e-17, 6.633591481902339e-19, 2.5468228261166726e-20, 9.263340938856898e-22, 3.2008120174705935e-23, 1.053327420914237e-24, 3.308744446078895e-26, 9.941637082881769e-28, 2.862656110275404e-29], [0.09190304236549715, 0.06351150505789173, 0.02194547193920191, 0.005055291301896765, 0.0009313551459118804, 0.000193869066051555, 2.2329540372439102e-05, 2.204470338369474e-06, 1.904306231894238e-07, 1.4622337213667682e-08, 1.0105069647321108e-09, 6.348471027896394e-11, 3.656035565853901e-12, 1.943522512387853e-13, 9.593654099124492e-15, 4.419929200435666e-16, 1.9090523865125948e-17, 7.760531046441339e-19, 2.97948670275908e-20, 1.0837032269155399e-21, 3.7445780469254385e-23, 1.2322706597736894e-24, 3.8708464439796885e-26, 1.1630559922877738e-27, 3.348974937586357e-29], [0.08601270252901655, 0.059440863448122896, 0.02053892124983781, 0.004731282618678726, 0.000817412765214782, 0.00012047599867191875, 2.08983735927476e-05, 2.0631792655364756e-06, 1.782253571069638e-07, 1.3685148050227589e-08, 9.45740562269277e-10, 5.941578602641927e-11, 3.421709352239627e-12, 1.8189563632903458e-13, 8.978768220888282e-15, 4.136642767542513e-16, 1.786695530495985e-17, 7.263135486963546e-19, 2.788522521750478e-20, 1.0142454579002708e-21, 3.504576881861763e-23, 1.153290761287584e-24, 3.622752361096173e-26, 1.0885122680856453e-27, 3.1343291546123e-29], [0.0670832434371668, 0.04635926782396626, 0.01601876715447766, 0.0036900338478701895, 0.0006375186211484553, 8.81140952234051e-05, 1.082239197345517e-05, 1.609119965481927e-06, 1.3900196908066084e-07, 1.0673355110745207e-08, 7.376043596085145e-10, 4.633970937811514e-11, 2.6686681699146204e-12, 1.418645024890663e-13, 7.0027435090131035e-15, 3.226260838555036e-16, 1.3934840749821334e-17, 5.664682909186943e-19, 2.174831503445708e-20, 7.910328702253196e-22, 2.7332984221823365e-23, 8.994774331987848e-25, 2.8254661393763334e-26, 8.489552277432298e-28, 2.4445338828893812e-29], [0.04484548462261355, 0.0309914030060665, 0.010708626167907522, 0.002466806130752808, 0.00042618439503631597, 5.890471449964836e-05, 6.784554273331669e-06, 7.142535451987027e-07, 9.292351334738997e-08, 7.135191412426934e-09, 4.930922130707487e-10, 3.0978328086940395e-11, 1.7840180534630815e-12, 9.48371312849097e-14, 4.681369150609114e-15, 2.1567715484639175e-16, 9.315510916671832e-18, 3.7868689300013637e-19, 1.453885765614513e-20, 5.2880944033211855e-22, 1.8272237011885415e-23, 6.013051744685831e-25, 1.8888382823021727e-26, 5.675308267810004e-28, 1.634183158678881e-29], [0.026232002427039408, 0.01812816977481275, 0.006263924004628958, 0.0014429382345511191, 0.00024929310451294717, 3.4455834890000736e-05, 3.96856998340193e-06, 3.9179466608955386e-07, 3.609089532253275e-08, 4.173672333419105e-09, 2.8843028989151966e-10, 1.812052170693845e-11, 1.0435468877668764e-12, 5.5474210591644204e-14, 2.738328907671618e-15, 1.2615860207550548e-16, 5.4490325398786224e-18, 2.215098260139766e-19, 8.504386841436098e-21, 3.0932279222685886e-22, 1.0688196809038817e-23, 3.517285837980976e-25, 1.1048606302863035e-26, 3.3197255310809613e-28, 9.559021815782763e-30], [0.013639286236540015, 0.009425711864390444, 0.0032569169166820166, 0.0007502533463630676, 0.00012961953700274656, 1.791525431162908e-05, 2.063451393156524e-06, 2.0371298804229924e-07, 1.7597511107075218e-08, 1.4409133406343815e-09, 1.4996885175123276e-10, 9.42173526416009e-12, 5.42590476769383e-13, 2.884372396312445e-14, 1.4237895824158178e-15, 6.559595630167733e-17, 2.833215448585683e-18, 1.1517366734064407e-19, 4.4218418597372275e-21, 1.6083187375429352e-22, 5.5573102372347925e-24, 1.828806948816884e-25, 5.744704556913874e-27, 1.7260857942926502e-28, 4.9701975687681546e-30], [0.00638255186975212, 0.00441079495220501, 0.0015240857032903967, 0.0003510836869006223, 6.065591731896613e-05, 8.383506139598384e-06, 9.655993223641553e-07, 9.532820780891554e-08, 8.234817091714542e-09, 6.323156979229575e-10, 4.6597550481844275e-11, 4.408934088168921e-12, 2.539071181552265e-13, 1.3497521873120774e-14, 6.662673327462143e-16, 3.069585800023918e-17, 1.3258131140569445e-18, 5.3895921904027394e-20, 2.069216419405059e-21, 7.526183986051515e-23, 2.600562832271305e-24, 8.557966310081573e-26, 2.6882546619393685e-27, 8.077279061862297e-29, 2.3258213982336613e-30], [0.0027152159553588857, 0.0018764063456813865, 0.0006483647768724158, 0.00014935531238789842, 2.5803772198373448e-05, 3.5664464773038737e-06, 4.1077781114353966e-07, 4.0553790414959435e-08, 3.5031923301476828e-09, 2.6899486394475347e-10, 1.8589448425472312e-11, 1.2453830266359522e-12, 1.080152065291464e-13, 5.742011580256284e-15, 2.8343830638969606e-16, 1.3058394997253193e-17, 5.640171822452066e-19, 2.2927987123162228e-20, 8.80270078757292e-22, 3.2017311036263074e-23, 1.1063113687426362e-24, 3.6406639765325934e-26, 1.1436165501071221e-27, 3.4361737173796785e-29, 9.894329883517906e-31], [0.0010588290308421173, 0.0007317257798749254, 0.00025283714430635257, 5.824278557095383e-05, 1.006247147853963e-05, 1.3907759563879014e-06, 1.6018743216580406e-07, 1.5814407144042538e-08, 1.366109289562396e-09, 1.0489757565323537e-10, 7.24916470138772e-12, 4.554259761624653e-13, 2.796827463544369e-14, 2.239162061716514e-15, 1.1052995864502621e-16, 5.092268146114223e-18, 2.1994485016056812e-19, 8.941026711656017e-21, 3.4327122766435807e-22, 1.2485510903023618e-23, 4.314185735626144e-25, 1.4197179057841454e-26, 4.459661490332097e-28, 1.3399746269896175e-29, 3.8584053326295128e-31], [0.0003811405858357475, 0.000263395113175957, 9.101233012596717e-05, 2.0965319958750954e-05, 3.6221298836468783e-06, 5.006296081269778e-07, 5.76617470439403e-08, 5.69262102563579e-09, 4.917504901857072e-10, 3.775937594516647e-11, 2.6094400518176978e-12, 1.6393706472264458e-13, 9.441009284818037e-15, 5.351853247137747e-16, 3.978683239999668e-17, 1.8330344256797165e-18, 7.917228050980269e-20, 3.2184498720660586e-21, 1.2356536608038898e-22, 4.4943374250442265e-24, 1.5529525832636131e-25, 5.110476749033861e-27, 1.6053186525330079e-28, 4.823429462730831e-30, 1.3888879375554885e-31], [0.00012739719641880758, 8.804047696849663e-05, 3.0421099532517227e-05, 7.007710760877027e-06, 1.2107059950845948e-06, 1.6733670170488937e-07, 1.9273583520108756e-08, 1.902772850470697e-09, 1.643688342711197e-10, 1.2621166080725474e-11, 8.722118797597317e-13, 5.479637490979238e-14, 3.155681024135483e-15, 1.67753759553212e-16, 8.830257129216907e-18, 6.12696352603582e-19, 2.6463533262707863e-20, 1.0757749390992032e-21, 4.1302033417897784e-23, 1.5022435526126428e-24, 5.190782945492693e-26, 1.7081896664528677e-27, 5.365817844958082e-29, 1.612243391315451e-30, 4.642392753752065e-32], [3.974397682803822e-05, 2.7465900152640996e-05, 9.490440205050826e-06, 2.1861885655811314e-06, 3.777027467388239e-07, 5.220386462176209e-08, 6.012760707058826e-09, 5.936061562102266e-10, 5.127798196631759e-11, 3.937412646084902e-12, 2.721030737941171e-13, 1.7094770653475476e-14, 9.844746746829112e-16, 5.233397374445578e-17, 2.5833199180189218e-18, 1.26915906812641e-19, 8.25580218675682e-21, 3.356084392248915e-22, 1.2884954341659705e-23, 4.686534289878017e-25, 1.6193633997002247e-26, 5.329022335641798e-28, 1.673968863431006e-29, 5.029699694093063e-31, 1.4482826562777948e-32], [1.1623958413948956e-05, 8.032977740434442e-06, 2.775678004012798e-06, 6.393966331380873e-07, 1.1046707882108777e-07, 1.5268113556836946e-08, 1.758557798941028e-09, 1.736125527625604e-10, 1.499731978273503e-11, 1.1515787927985958e-12, 7.958224280815192e-14, 4.9997237073621336e-15, 2.8793023726873343e-16, 1.5306166694750407e-17, 7.555460146050057e-19, 3.480905041729838e-20, 1.603250252774401e-21, 9.815571697315258e-23, 3.768474757347941e-24, 1.3706751069927304e-25, 4.736167418935048e-27, 1.5585841921285914e-28, 4.895872534084274e-30, 1.4710410166489472e-31, 4.235805953957826e-33], [3.1996894947958754e-06, 2.2112118413253354e-06, 7.640519205331988e-07, 1.7600464636940794e-07, 3.040791605039329e-08, 4.202804312731964e-09, 4.840725263186299e-10, 4.778976674352531e-11, 4.1282637850223786e-12, 3.16991375444503e-13, 2.190634697900912e-14, 1.37625779907567e-15, 7.925762658590459e-17, 4.213279077118561e-18, 2.0797671151898393e-19, 9.581774897817414e-21, 4.138552770008573e-22, 1.7940258626367805e-23, 1.037335876737127e-24, 3.773013103143843e-26, 1.3037095106754325e-27, 4.2902643735582355e-29, 1.347671021979097e-30, 4.0492871014895827e-32, 1.165976626052664e-33], [8.318366279690961e-07, 5.748579681887992e-07, 1.986337656211212e-07, 4.5756662257679965e-08, 7.905272806022748e-09, 1.0926205724658797e-09, 1.2584635435416176e-10, 1.2424105052699748e-11, 1.0732419604731138e-12, 8.240957045173e-14, 5.695084423591061e-15, 3.577914821613993e-16, 2.0604935868709548e-17, 1.0953437406671346e-18, 5.406857343108844e-20, 2.4910139980529093e-21, 1.0759168308285222e-22, 4.373733286746784e-24, 1.7906426093165707e-25, 9.80885958499111e-27, 3.3893080093406874e-28, 1.1153579293869268e-29, 3.5035965844750654e-31, 1.0527100625420946e-32, 3.0312380825824685e-34], [2.048741420496131e-07, 1.4158252843542675e-07, 4.8921772551740804e-08, 1.1269468796995998e-08, 1.9470000831247582e-09, 2.6910296426382e-10, 3.0994864870675486e-11, 3.0599492470301377e-12, 2.6433018031485717e-13, 2.0296761978606435e-14, 1.4026498665152328e-15, 8.812093682318521e-17, 5.074816876476856e-18, 2.6977365695770998e-19, 1.3316620380837913e-20, 6.135151284822078e-22, 2.649889776684869e-23, 1.0772125493725817e-24, 4.1357227330113946e-26, 1.6040833755024179e-27, 8.347571472668461e-29, 2.747029779384384e-30, 8.629054314243915e-32, 2.5927335204854522e-33, 7.465676319560545e-35], [4.793578695120699e-08, 3.3127020575638525e-08, 1.1446557593138103e-08, 2.636793740301573e-09, 4.5555276153907855e-10, 6.296383835381684e-11, 7.252077905772763e-12, 7.159569954495386e-13, 6.184711785286547e-14, 4.748970505854395e-15, 3.281874642439295e-16, 2.0618250850192906e-17, 1.1873891852504949e-18, 6.312076485397152e-20, 3.1157796249922242e-21, 1.4354827893870383e-22, 6.200126111990579e-24, 2.520426968054661e-25, 9.676629848723858e-27, 3.5195978498640133e-28, 1.296857242541619e-29, 6.427411138166113e-31, 2.0189981276300896e-32, 6.066393758424929e-34, 1.7467947195330365e-35], [1.0681771315995578e-08, 7.381859789418579e-09, 2.550693716361222e-09, 5.875699458114526e-10, 1.0151310181021604e-10, 1.4030547222628789e-11, 1.6160168150383986e-12, 1.5954028052702471e-13, 1.3781702804424323e-14, 1.0582368655296937e-15, 7.313165517441995e-17, 4.594468027442e-18, 2.6459187481040687e-19, 1.4065515940046076e-20, 6.94304767731937e-22, 3.198758142822916e-23, 1.3816051320077171e-24, 5.616393555577181e-26, 2.1562918589157003e-27, 7.842896038148903e-29, 2.7099980510678816e-30, 9.509962568286693e-32, 4.499034574882437e-33, 1.351804882357238e-34, 3.8924700973477405e-36], [2.2720783552216096e-09, 1.5701669089004911e-09, 5.425482171730946e-10, 1.2497973571647365e-10, 2.159246014273079e-11, 2.9843835552547928e-12, 3.437367004501064e-13, 3.393519739826517e-14, 2.931452819359575e-15, 2.250934798863442e-16, 1.5555552154024302e-17, 9.772715638722458e-19, 5.628031661977216e-20, 2.9918216161908753e-21, 1.4768288779302254e-22, 6.803955004179415e-24, 2.9387589595717287e-25, 1.1946413993083782e-26, 4.5865652008917815e-28, 1.668232150209685e-29, 5.764332274464347e-31, 1.8969340326184936e-32, 6.354167678353603e-34, 2.875371998544335e-35, 8.279522932013701e-37], [4.6227262676765866e-10, 3.194630941195199e-10, 1.1038580114296014e-10, 2.54281330525447e-11, 4.39315978941341e-12, 6.071968522561258e-13, 6.99359980558505e-14, 6.904389016832553e-15, 5.964276680584086e-16, 4.579708000659351e-17, 3.1649022748428728e-18, 1.9883376462714342e-19, 1.1450683353127582e-20, 6.087101856141408e-22, 3.004727205460093e-23, 1.384319402965394e-24, 5.979141610834592e-26, 2.430594070114325e-27, 9.331736022152182e-29, 3.394152566804734e-30, 1.1727997918532711e-31, 3.859464952202271e-33, 1.2123469846015862e-34, 3.884438271004532e-36, 1.6845355730664188e-37], [9.013420763442425e-11, 6.228911510128581e-11, 2.1523092962873054e-11, 4.957993382259636e-12, 8.565810599666137e-13, 1.1839162430815906e-13, 1.3636164905465976e-14, 1.3462221148231792e-15, 1.162918419971933e-16, 8.929543475736324e-18, 6.170946369418619e-19, 3.8768732535497426e-20, 2.2326614450947936e-21, 1.1868669499851159e-22, 5.8586360112960724e-24, 2.699154682199203e-25, 1.1658167934253618e-26, 4.739187611487017e-28, 1.8195077612351203e-29, 6.617940031155122e-31, 2.286732413547007e-32, 7.525209048002413e-34, 2.363841778803168e-35, 7.1025301195637965e-37, 2.1808759643478113e-38]] |
| Legacy trial inputs | {"lambda_home": 4.679535101076695, "lambda_away": 0.6910707569974378, "rho": -0.1036082449967548, "max_goals": 24, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.9351 |
| Legacy p draw | 0.0425 |
| Legacy p away | 0.0224 |
| Legacy p over 1 5 | 0.9708 |
| Legacy p under 3 5 | 0.2208 |
| Legacy p btts yes | 0.4992 |
| Legacy p over 2 5 | 0.9012 |
| Legacy goal margin distribution | {"-1": 0.01674904124595835, "-10": 6.762375677031201e-11, "-11": 4.1488231957682214e-12, "-12": 2.341569419081044e-13, "-13": 1.223349807498141e-14, "-14": 5.948326202830795e-16, "-15": 2.7044586418814728e-17, "-16": 1.1545234274083606e-18, "-17": 4.64464879311828e-20, "-18": 1.7666464584822893e-21, "-19": 6.371857546954507e-23, "-2": 0.004624388316464867, "-20": 2.184993674486033e-24, "-21": 7.140645965174737e-26, "-22": 2.2280923132999475e-27, "-23": 6.605405184766197e-29, "-24": 1.6761477644177798e-30, "-3": 0.0008625819402039398, "-4": 0.0001299346411052164, "-5": 1.631926854242828e-05, "-6": 1.7518167722996178e-06, "-7": 1.6387709780961766e-07, "-8": 1.3567514061807576e-08, "-9": 1.0066293855326e-09, "0": 0.042549522130046785, "1": 0.07951394454082948, "10": 0.008534025396999753, "11": 0.0035453552437467355, "12": 0.001354946230968531, "13": 0.0004793424319038878, "14": 0.00015782296101219716, "15": 4.858877476574238e-05, "16": 1.4045543423758551e-05, "17": 3.826210598044302e-06, "18": 9.854754972366325e-07, "19": 2.406813476287431e-07, "2": 0.13202840783980194, "20": 5.5886479671911174e-08, "21": 1.2367282019421287e-08, "22": 2.6130645423040024e-09, "23": 5.245617418689445e-10, "24": 9.013420763442425e-11, "3": 0.16676067532257002, "4": 0.17009769501554614, "5": 0.1446619648954509, "6": 0.10515321220646202, "7": 0.06660890916613543, "8": 0.037341738290704585, "9": 0.018760484408359104} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.9456 |
| Legacy raw p draw | 0.0403 |
| Legacy raw p away | 0.0141 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 4.6795 |
| Legacy lambda away | 0.6911 |
| Legacy model home team | PSV Eindhoven |
| Legacy model away team | Willem II |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 94.8% |
| Market reference home draw last update utc | 2026-10-30T07:25:59Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 11.4% |
| Market reference draw away last update utc | 2026-10-30T07:25:59Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 93.9% |
| Market reference home away last update utc | 2026-10-30T07:25:59Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.02 |
| Market reference dc draw away odds | 8.50 |
| Market reference dc home away odds | 1.03 |
| Market p over 1 5 | 97.5% |
| Market reference over 1 5 odds | 1.02 |
| Market reference over 1 5 opposite odds | 17.00 |
| Market reference over 1 5 last update utc | 2026-10-30T07:25:59Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 23.9% |
| Market under 3 5 odds | 3.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market reference under 3 5 odds | 3.51 |
| Market reference under 3 5 opposite odds | 1.27 |
| Market reference under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-30T07:26:44Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,679.0337 |
| Elo away rating | 1,344.0120 |
| Elo rating diff | 395.0217 |
| Elo home expectancy | 0.9067 |

</details>


---

## 2026-10-31 — SC Cambuur vs Go Ahead Eagles

The model's most likely 1X2 outcome is **Go Ahead Eagles win** at **42.7%**. Expected goals are 1.77 for SC Cambuur and 2.02 for Go Ahead Eagles (3.79 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 66.3%; Under 3.5 goals: 55.7%; Double Chance 1X: 57.3%; Double Chance X2: 66.6%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 74.2%; BTTS Yes (both teams score): 67.5%; BTTS No (at least one team does not score): 32.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Cambuur win | 33.4% | 2.99 |
| Draw | 23.9% | 4.18 |
| Go Ahead Eagles win | 42.7% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Cambuur expected goals | 1.77 |
| Go Ahead Eagles expected goals | 2.02 |
| Expected total goals | 3.79 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 86.3% |
| Under 1.5 | 13.7% |
| Over 2.5 | 66.3% |
| Under 2.5 | 33.7% |
| Over 3.5 | 44.3% |
| Under 3.5 | 55.7% |
| Over 4.5 | 25.8% |
| Under 4.5 | 74.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.33% |
| 2 | 1-2 | 8.73% |
| 3 | 2-1 | 7.66% |
| 4 | 2-2 | 6.81% |
| 5 | 0-2 | 5.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Cambuur win | 33.4% | 33.3% | 2.87 | -4.2% |
| Draw | 23.9% | 24.5% | 3.85 | -7.8% |
| Go Ahead Eagles win | 42.7% | 42.3% | 2.28 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:00:00+00:00 |
| Fixture id | 314c3b27fe569849986fdd2d013d1aca |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:26:45Z |
| Market best draw last update utc | 2026-10-30T07:26:45Z |
| Market best away last update utc | 2026-10-30T07:26:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Cambuur |
| Matched away-team name | Go Ahead Eagles |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7686 |
| Dc lambda away | 2.0171 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 67.5% |
| P btts no | 32.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.00 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.31 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.97 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.88 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.19228211241399576, "-10": 4.6202612723256365e-06, "-11": 7.463938550003793e-07, "-12": 1.1088399864149442e-07, "-13": 1.524366715633433e-08, "-14": 1.9483985055443145e-09, "-15": 2.3005111740484493e-10, "-16": 2.2107670713213384e-11, "-2": 0.13088292460324993, "-3": 0.06530949639874249, "-4": 0.026170705722672577, "-5": 0.008713601194353056, "-6": 0.0024740563216342493, "-7": 0.0006112146820459559, "-8": 0.00013349250745917982, "-9": 2.6107265184174274e-05, "0": 0.23945590832500535, "1": 0.1676725651579487, "10": 1.2424258000858637e-06, "11": 1.7598600934603634e-07, "12": 2.2923721787372705e-08, "13": 2.763197133330622e-09, "14": 3.096751538867496e-10, "15": 3.2059672635347207e-11, "16": 2.7013688379786835e-12, "2": 0.10074827533690131, "3": 0.04407954739369525, "4": 0.015487538098453978, "5": 0.004521377772349775, "6": 0.0011256123770414157, "7": 0.00024382555295166712, "8": 4.669264677618848e-05, "9": 8.006803023895978e-06} |
| Raw goal margin distribution | {"-1": 0.18557232018818198, "-10": 9.60357104151649e-06, "-11": 1.7156989825359618e-06, "-12": 2.820690745259073e-07, "-13": 4.293875099318182e-08, "-14": 6.084308173835453e-09, "-15": 8.053663537262244e-10, "-16": 9.855822620654876e-11, "-17": 9.665899790599595e-12, "-2": 0.1323251354786998, "-3": 0.07082974390516956, "-4": 0.030773226531100182, "-5": 0.011183353808919966, "-6": 0.0034809657017760465, "-7": 0.0009455797586549935, "-8": 0.0002275603856056672, "-9": 4.911462838731966e-05, "0": 0.22732489451733603, "1": 0.16175917831676445, "10": 2.5792555515536913e-06, "11": 4.040255930171919e-07, "12": 5.8241079808221005e-08, "13": 7.773731105939196e-09, "14": 9.658228412904273e-10, "15": 1.120949152029287e-10, "16": 1.2027946056331566e-11, "17": 1.0343012353339323e-12, "2": 0.10173131807215695, "3": 0.04774568821606464, "4": 0.01818853340637358, "5": 0.005795659671692229, "6": 0.0015817458968033736, "7": 0.0003767396252419074, "8": 7.949612459793677e-05, "9": 1.5044103789613885e-05} |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 43.5% |
| Raw p over 1 5 | 89.9% |
| Raw p under 3 5 | 47.6% |
| Raw p btts yes | 72.7% |
| P home draw | 57.3% |
| P draw away | 66.6% |
| P home away | 76.1% |
| Raw p home draw | 56.5% |
| Raw p draw away | 66.3% |
| Raw p home away | 77.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8999 |
| Totals anchor target over 2 5 | 0.6629 |
| Totals anchor reference over odds | 1.46 |
| Totals anchor reference under odds | 2.72 |
| Totals anchor reference last update utc | 2026-10-30T07:26:45Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7248 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.7, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.68, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.87 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.28 |
| Market reference 1x2 last update utc | 2026-10-30T07:26:45Z |
| Market reference home last update utc | 2026-10-30T07:26:45Z |
| Market reference draw last update utc | 2026-10-30T07:26:45Z |
| Market reference away last update utc | 2026-10-30T07:26:45Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:23Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:23Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.5% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | 0.0048 |
| Raw ev home | -0.0320 |
| Raw edge prob draw | -0.0173 |
| Raw ev draw | -0.1248 |
| Raw edge prob away | 0.0126 |
| Raw ev away | -0.0073 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.02699180558416735, 0.030331575750224934, 0.039600401226893726, 0.02760903699847475, 0.014436575773861276, 0.0060390290349048295, 0.0021051778630252686, 0.0006290188812080131, 0.00016445482582841614, 3.821879939094259e-05, 7.993739056147835e-06, 1.5199531766873408e-06, 2.6492435803031007e-07, 4.2623731322324924e-08, 6.367901795896345e-09, 8.87928560512449e-10, 1.1607293606728968e-10, 1.4280880201078046e-11], [0.02630230009933635, 0.08449489025450378, 0.0760562642503548, 0.05302573076526705, 0.027726790333159217, 0.01159851854688683, 0.004043190444633944, 0.001208089432566889, 0.0003158508323889831, 7.340276905666185e-05, 1.5352721466616594e-05, 2.9192118481817328e-06, 5.088119401938033e-07, 8.18628516972013e-08, 1.2230149359701108e-08, 1.7053496212535534e-09, 2.2292890032267988e-10, 2.742776246325547e-11], [0.03224581183994366, 0.06744445393625824, 0.0768889356976326, 0.05092043093255881, 0.02662594351393589, 0.011138018355677416, 0.0038826621870531723, 0.0011601242193850342, 0.000303310492161841, 7.048843227742153e-05, 1.4743166794407234e-05, 2.8033093207309922e-06, 4.886103950739078e-07, 7.861262118654461e-08, 1.1744571301098639e-08, 1.6376415063342605e-09, 2.1407787328765798e-10, 2.6338788056074336e-11], [0.02064369644652671, 0.04317778820309277, 0.04515473764449797, 0.03431860853943176, 0.017045869343664193, 0.007130534380456428, 0.002485671627428105, 0.000742708924313138, 0.00019417869707592407, 4.512653631266703e-05, 9.438542328379072e-06, 1.7946723422607032e-06, 3.128072794876442e-07, 5.032762383828563e-08, 7.51884821625546e-09, 1.0484144208495233e-09, 1.3705217452748561e-10, 1.6862033063328574e-11], [0.009912036137242843, 0.020731742403976326, 0.021680971354104947, 0.015115774631895269, 0.0086162445972958, 0.0034237140930653506, 0.0011934910523513313, 0.00035661044117334876, 9.323457489722586e-05, 2.1667430532045735e-05, 4.531900228436567e-06, 8.617089074661001e-07, 1.5019388927295612e-07, 2.4164723962049082e-08, 3.6101623283899398e-09, 5.033944213036243e-10, 6.580537115157551e-11, 8.096276822517276e-12], [0.0038073979876811553, 0.007963449004533192, 0.008328065551983926, 0.005806251018343104, 0.0030360487688505812, 0.0013844789004216823, 0.0004584421775828917, 0.00013698072296245426, 3.581313949332999e-05, 8.322864269629226e-06, 1.7407874195786352e-06, 3.309984663923926e-07, 5.769227471147276e-08, 9.282121262682214e-09, 1.386730697305307e-09, 1.9336318796094216e-10, 2.5277070647445498e-11, 3.109930962210598e-12], [0.0012187438278642472, 0.0025490910995352653, 0.002665804447648734, 0.001858574442317732, 0.0009718358075786633, 0.0004065330138573432, 0.0001544870825157538, 4.3847375868512444e-05, 1.1463745806232327e-05, 2.6641395229974953e-06, 5.572241016304439e-07, 1.0595223805167445e-07, 1.8467232463627656e-08, 2.9711966111720262e-09, 4.438909417189772e-10, 6.189533971127571e-11, 8.091161979319342e-12, 9.95485414853219e-13], [0.00033438731410262906, 0.0006993953172835757, 0.0007314180131966131, 0.000509937939062649, 0.0002666430450888701, 0.00011154065316254944, 3.8882560840159786e-05, 1.2664977498261397e-05, 3.1453132988734125e-06, 7.30961207041306e-07, 1.5288583739864417e-07, 2.9070165112014123e-08, 5.066863208852425e-09, 8.152086039456967e-10, 1.2179056530362904e-10, 1.6982253307319855e-11, 2.219975896801238e-12, 2.731317988985851e-13], [8.02777533036843e-05, 0.00016790674279410848, 0.0001755945645929843, 0.0001224229220002538, 6.401410487485712e-05, 2.677802853240645e-05, 9.334698103959266e-06, 2.7891711483841213e-06, 7.949371244093749e-07, 1.7548489723929963e-07, 3.670393887774301e-08, 6.978995449101852e-09, 1.2164229250004648e-09, 1.9571052022179261e-10, 2.9238767572265726e-11, 4.0770001852620566e-12, 5.329588470238379e-13, 6.557188699043333e-14], [1.713121256218011e-05, 3.583117343291623e-05, 3.747174885956633e-05, 2.6124960066281428e-05, 1.3660562141548347e-05, 5.714411277174161e-06, 1.9920175994183764e-06, 5.952070386737576e-07, 1.5561483574063057e-07, 3.9423582915825795e-08, 7.832593127080258e-09, 1.4893124133254039e-09, 2.5958374314313874e-10, 4.17644787577844e-11, 6.239531149331191e-12, 8.700287927286394e-13, 1.1373301966636846e-13, 1.3992991680857261e-14], [3.290209162510471e-06, 6.881711070046979e-06, 7.196798883064388e-06, 5.017542259096253e-06, 2.623638377028357e-06, 1.0975059864716838e-06, 3.825855603448526e-07, 1.143150635208686e-07, 2.988728068827528e-08, 6.945712776819076e-09, 1.5836690251085603e-09, 2.8603634041537067e-10, 4.9855479116162993e-11, 8.021257700094109e-12, 1.1983601559308663e-12, 1.670971447638965e-13, 2.1843487262097677e-14, 2.6874845707611916e-15], [5.744685080084254e-07, 1.201542545075923e-06, 1.2565566845714306e-06, 8.760598105115379e-07, 4.58085656431373e-07, 1.9162387417875803e-07, 6.679920490804828e-08, 1.9959340193926882e-08, 5.2183009338902125e-09, 1.2127172039451195e-09, 2.53648597855638e-10, 5.257598079086448e-11, 8.704736170041657e-12, 1.4005066899176175e-12, 2.0923295050004527e-13, 2.917505930587719e-14, 3.813859519977664e-15, 4.692331628190012e-16], [9.194336272474337e-08, 1.923062108906876e-07, 2.0111119308224562e-07, 1.4021288165242809e-07, 7.331635256088603e-08, 3.066929365966173e-08, 1.0691175305461764e-08, 3.1944812110916523e-09, 8.351861396804334e-10, 1.940947087794539e-10, 4.059631592010862e-11, 7.719103527293175e-12, 1.4666727460258013e-12, 2.2415031075582764e-13, 3.348761645522924e-14, 4.669451889670554e-15, 6.104060785545779e-16, 7.510050471019596e-17], [1.3583523388666798e-08, 2.841092424735258e-08, 2.9711754214752015e-08, 2.0714762880927054e-08, 1.083160720109844e-08, 4.531018394303222e-09, 1.5794922603477366e-09, 4.719460868037466e-10, 1.233886832723647e-10, 2.8675153248584226e-11, 5.9976162547522365e-12, 1.14040448592718e-12, 1.9876989039070322e-13, 3.486220467112189e-14, 4.947391610116675e-15, 6.898552225621937e-16, 9.018013915211229e-17, 1.1095194171716924e-17], [1.863458832832113e-09, 3.897559287292504e-09, 4.076013950593313e-09, 2.84175959034992e-09, 1.4859365670541145e-09, 6.215888180848358e-10, 2.1668301512924566e-10, 6.474403429148215e-11, 1.6927105371442164e-11, 3.933807604621299e-12, 8.227843885615344e-13, 1.5644665610657473e-13, 2.726829389925916e-14, 4.3872010917442265e-15, 7.145080198768606e-16, 9.463795004258133e-17, 1.2371383479873867e-17, 1.522096807263093e-18], [2.385964334005882e-10, 4.990417435205624e-10, 5.218909985924141e-10, 3.638576237334535e-10, 1.9025865176736514e-10, 7.958795355372931e-11, 2.7743996098775933e-11, 8.28979712014103e-12, 2.1673389818244014e-12, 5.036829618179793e-13, 1.0534894418359955e-13, 2.003135969885957e-14, 3.4914201240465056e-15, 5.617352606123535e-16, 8.392214533780507e-17, 1.2756540748004376e-17, 1.5840263935655187e-18, 1.9488859270985343e-19], [2.864041907671276e-11, 5.990351350812387e-11, 6.264627135878218e-11, 4.367640655586298e-11, 2.28380929334305e-11, 9.553505518708809e-12, 3.3303082690994985e-12, 9.950830370676462e-13, 2.6016104195710816e-13, 6.046063179849391e-14, 1.2645779602420804e-14, 2.4045059193676046e-15, 4.1909987546911026e-16, 6.7429060211864e-17, 1.0073769243046898e-17, 1.4046679282456095e-18, 2.0017105875280318e-19, 2.3393857523048917e-20], [3.2356821322246324e-12, 6.767663831892512e-12, 7.077529848399576e-12, 4.9343889806239935e-12, 2.5801580989738892e-12, 1.0793175555217292e-12, 3.762451566180783e-13, 1.1242057577773254e-13, 2.9391973375348254e-14, 6.830604869621657e-15, 1.4286705441706858e-15, 2.716516409654123e-16, 4.734825894274637e-17, 7.617870560337801e-18, 1.1380949090365789e-18, 1.586938691420494e-19, 2.0744983488947794e-20, 2.782350090791923e-21]] |
| Legacy trial inputs | {"lambda_home": 1.9205932741586182, "lambda_away": 2.091572520209064, "rho": -0.1036082449967548, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3445 |
| Legacy p draw | 0.2329 |
| Legacy p away | 0.4226 |
| Legacy p over 1 5 | 0.9164 |
| Legacy p under 3 5 | 0.4317 |
| Legacy p btts yes | 0.7575 |
| Legacy p over 2 5 | 0.7600 |
| Legacy goal margin distribution | {"-1": 0.178283472849079, "-10": 1.145570081305189e-05, "-11": 2.11542625326131e-06, "-12": 3.5964911075157336e-07, "-13": 5.663667063971029e-08, "-14": 8.304191323500885e-09, "-15": 1.1371962488912033e-09, "-16": 1.4350069853054514e-10, "-17": 1.4280880201078046e-11, "-2": 0.12772531461342163, "-3": 0.069354765167581, "-4": 0.030762610424963567, "-5": 0.011460041835173655, "-6": 0.0036665865353336714, "-7": 0.0010257191865655718, "-8": 0.0002545553714524284, "-9": 5.671325309332468e-05, "0": 0.23286295163192158, "1": 0.15750168264880374, "10": 4.71514663079902e-06, "11": 7.995284211066577e-07, "12": 1.248180759569117e-07, "13": 1.804923023920655e-08, "14": 2.4300812366920817e-09, "15": 3.055774767571116e-10, "16": 3.5408082908605275e-11, "17": 3.2356821322246324e-12, "2": 0.10400415992313079, "3": 0.05185761166964218, "4": 0.021121359454244523, "5": 0.007225158211657718, "6": 0.0021226851126233937, "7": 0.0005452737494310141, "8": 0.00012425985804093555, "9": 2.542117516294124e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3566 |
| Legacy raw p draw | 0.2211 |
| Legacy raw p away | 0.4224 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9206 |
| Legacy lambda away | 2.0916 |
| Legacy model home team | Cambuur |
| Legacy model away team | Go Ahead Eagles |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 56.9% |
| Market reference home draw last update utc | 2026-10-30T07:26:44Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.0% |
| Market reference draw away last update utc | 2026-10-30T07:26:44Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.1% |
| Market reference home away last update utc | 2026-10-30T07:26:44Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.67 |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 86.9% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:26:45Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 5.88 |
| Market reference over 1 5 last update utc | 2026-10-30T07:26:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.8% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.14 |
| Market reference under 3 5 last update utc | 2026-10-30T07:26:45Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.8% |
| Market reference btts yes odds | 1.37 |
| Market reference btts yes opposite odds | 2.86 |
| Market reference btts yes last update utc | 2026-10-30T07:26:44Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,402.1959 |
| Elo away rating | 1,431.3227 |
| Elo rating diff | 30.8732 |
| Elo home expectancy | 0.5443 |

</details>


---

## 2026-11-01 — Excelsior vs FC Twente Enschede

The model's most likely 1X2 outcome is **FC Twente Enschede win** at **59.8%**. Expected goals are 1.09 for Excelsior and 1.84 for FC Twente Enschede (2.93 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 57.4%; Under 3.5 goals: 65.8%; Double Chance 1X: 40.2%; Double Chance X2: 81.4%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 82.1%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Excelsior win | 18.6% | 5.37 |
| Draw | 21.6% | 4.64 |
| FC Twente Enschede win | 59.8% | 1.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Excelsior expected goals | 1.09 |
| FC Twente Enschede expected goals | 1.84 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 34.2% |
| Under 3.5 | 65.8% |
| Over 4.5 | 17.9% |
| Under 4.5 | 82.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.94% |
| 2 | 1-1 | 10.19% |
| 3 | 0-2 | 10.05% |
| 4 | 0-1 | 9.81% |
| 5 | 1-3 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Excelsior win | 18.6% | 17.5% | 5.18 | -3.6% |
| Draw | 21.6% | 20.1% | 4.53 | -2.4% |
| FC Twente Enschede win | 59.8% | 62.4% | 1.56 | -6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:30:00+00:00 |
| Fixture id | c0c32575c239ac72913af247ce084ea2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:26:45Z |
| Market best draw last update utc | 2026-10-30T07:26:45Z |
| Market best away last update utc | 2026-10-30T07:26:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Excelsior |
| Matched away-team name | Twente |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.0886 |
| Dc lambda away | 1.8372 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.05 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.11 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.58 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.2507126212081621, "-10": 8.613020203230257e-06, "-11": 1.417303013824017e-06, "-12": 2.142681402444338e-07, "-13": 2.9954158890420035e-08, "-14": 3.892891530934677e-09, "-15": 4.698335516270104e-10, "-16": 4.795390291592849e-11, "-2": 0.18674155660519026, "-3": 0.09924073196785665, "-4": 0.04166398749599495, "-5": 0.014391589866876674, "-6": 0.004212776125427084, "-7": 0.0010685061605145397, "-8": 0.00023888485220302638, "-9": 4.7721794949930785e-05, "0": 0.2155213545016627, "1": 0.11326594888571229, "10": 3.615559438985997e-08, "11": 3.5252111265518955e-09, "12": 3.157783881331821e-10, "13": 2.6156782098587893e-11, "14": 2.0141966539296315e-12, "15": 1.4403763313743792e-13, "16": 8.710804977645618e-15, "2": 0.05159908012214354, "3": 0.016247753643301634, "4": 0.004041723325119935, "5": 0.0008272121493102942, "6": 0.00014347587855617204, "7": 2.1562043831859916e-05, "8": 2.856300446603731e-06, "9": 3.380916369506532e-07} |
| Raw goal margin distribution | {"-1": 0.2256796686126945, "-10": 7.753034274271968e-06, "-11": 1.2757892799421784e-06, "-12": 1.9287406693607613e-07, "-13": 2.6963320072942187e-08, "-14": 3.5041972215553584e-09, "-15": 4.229219882244087e-10, "-16": 4.316584010250753e-11, "-2": 0.1680959355288574, "-3": 0.0893318230069942, "-4": 0.03750395510951435, "-5": 0.012954629951676332, "-6": 0.0037921422357770932, "-7": 0.0009618188149184943, "-8": 0.00021503286919492492, "-9": 4.295690746642283e-05, "0": 0.24850916950817417, "1": 0.1295446209475953, "10": 4.135190510870508e-08, "11": 4.031857267272818e-09, "12": 3.6116230867788975e-10, "13": 2.991605557985881e-11, "14": 2.3036785955019107e-12, "15": 1.6473883608043415e-13, "16": 9.96272878194086e-15, "2": 0.059014940866406074, "3": 0.018582893691158824, "4": 0.004622603008923917, "5": 0.0009460997358859834, "6": 0.00016409634568493946, "7": 2.466095788304544e-05, "8": 3.2668102135539772e-06, "9": 3.866824353232359e-07} |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 80.0% |
| Raw p under 3 5 | 66.4% |
| Raw p btts yes | 56.8% |
| P home draw | 40.2% |
| P draw away | 81.4% |
| P home away | 78.4% |
| Raw p home draw | 46.1% |
| Raw p draw away | 78.7% |
| Raw p home away | 75.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5743 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.57, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.47, "price": 1.57, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.18 |
| Reference draw odds | 4.53 |
| Reference away odds | 1.56 |
| Market reference 1x2 last update utc | 2026-10-30T07:26:45Z |
| Market reference home last update utc | 2026-10-30T07:26:45Z |
| Market reference draw last update utc | 2026-10-30T07:26:45Z |
| Market reference away last update utc | 2026-10-30T07:26:45Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:23Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:23Z |
| Home probability edge | +1.1% |
| Draw probability edge | +1.4% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.0382 |
| Raw ev home | 0.1028 |
| Raw edge prob draw | 0.0471 |
| Raw ev draw | 0.1257 |
| Raw edge prob away | -0.0853 |
| Raw ev away | -0.1598 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05989434999536613, 0.09663503134183214, 0.09808242451923269, 0.058867321324375214, 0.026498337012670358, 0.009542297473573835, 0.0028635583505559497, 0.0007365671287456828, 0.0001657779186385054, 3.3165649716939326e-05, 5.9716293771956145e-06, 9.774723854606435e-07, 1.466653717081912e-07, 2.031367833853484e-08, 2.612551569827979e-09, 3.13601368423365e-10, 3.529086495343921e-11], [0.044396298148558985, 0.10786866721300165, 0.10698465046466892, 0.06421027851370761, 0.028903397699346717, 0.010408382183089376, 0.0031234626460456185, 0.0008034199521359686, 0.00018082437059682477, 3.617585372499271e-05, 6.513630599522415e-06, 1.0661904210663895e-06, 1.5997711724993894e-07, 2.2157402688120957e-08, 2.8496738114804816e-09, 3.42064676219711e-10, 3.84939592403651e-11], [0.02976575887407956, 0.05359463229094806, 0.047990469719194774, 0.03501908846921411, 0.015763374097158354, 0.005676537540842266, 0.001703478278930164, 0.00043817025923310676, 9.861823960113091e-05, 1.9729635992381223e-05, 3.5524126588511915e-06, 5.814803726849096e-07, 8.724853639794574e-08, 1.2084234221436438e-08, 1.5541589543383425e-09, 1.8655569538098026e-10, 2.0993887511029738e-11], [0.010822459866682793, 0.01948634199088072, 0.01754303221555622, 0.010472421339424614, 0.005731366845095388, 0.002063918476843583, 0.0006193635238892481, 0.0001593132587475794, 3.585636585719841e-05, 7.173450360029125e-06, 1.2916130777297974e-06, 2.1141903430946157e-07, 3.172248312526113e-08, 4.3936773268353215e-09, 5.650728738657943e-10, 6.782933150479578e-11, 7.633116494524389e-12], [0.0029511838937513425, 0.005313743764359595, 0.004783821308637423, 0.0028711642020913964, 0.0012854693913309603, 0.000562811324034371, 0.00016889465783154556, 4.3443240175397085e-05, 9.777696633644728e-06, 1.9561330257565207e-06, 3.5221084290545274e-07, 5.765199932109235e-08, 8.650425358219846e-09, 1.1981148390501032e-09, 1.5409010379261077e-10, 1.8496426240130783e-11, 2.0814796945671456e-12], [0.0006438082640749513, 0.0011592067020679171, 0.0010436027720535262, 0.0006263517650446867, 0.0002819438660573568, 0.00010098487843398124, 3.6844798692582565e-05, 9.477253214323135e-06, 2.1330293614325004e-06, 4.2673538923769224e-07, 7.683569019180904e-08, 1.257693012012964e-08, 1.887112268800794e-09, 2.613717960187128e-10, 3.361514761716454e-11, 4.035042375523453e-12, 4.5408008348918026e-13], [0.0001170403403666847, 0.0002107365725730667, 0.00018972049671381753, 0.00011386685735610467, 5.125564222923725e-05, 1.845763321360846e-05, 5.509199024615059e-06, 1.7229057218446987e-06, 3.8777147856730217e-07, 7.757784109008367e-08, 1.396825085070907e-08, 2.286407715102913e-09, 3.4306527979715153e-10, 4.7515767776352225e-11, 6.111024878256703e-12, 7.335456212321637e-13, 8.254893652486436e-14], [1.8237605427668107e-05, 3.283765621088993e-05, 2.956286310999744e-05, 1.7743103012543197e-05, 7.986820407304923e-06, 2.876128270165487e-06, 8.631004376158736e-07, 2.2081419961807916e-07, 6.042380943234982e-08, 1.2088430803419067e-08, 2.176578150164323e-09, 3.5627546557180493e-10, 5.3457544546358475e-11, 7.404061040687875e-12, 9.522397161451986e-13, 1.1430345777628937e-13, 1.2863043016599362e-14], [2.4866124735846864e-06, 4.477261330229636e-06, 4.030758558504219e-06, 2.419189374727537e-06, 1.088965726770003e-06, 3.92146680691594e-07, 1.1767972076400211e-07, 3.0269686670748766e-08, 6.7761285948193325e-09, 1.6482011819514746e-09, 2.967662832380137e-10, 4.857649872055143e-11, 7.288686971729296e-12, 1.0095092040441712e-12, 1.298334458106625e-13, 1.5584743567770216e-14, 1.7538159458591862e-15], [3.013671269417089e-07, 5.426255188503004e-07, 4.885112332847591e-07, 2.931957267706183e-07, 1.3197813326399253e-07, 4.752655259119875e-08, 1.4262294475996109e-08, 3.668560582839296e-09, 8.256767293675202e-10, 1.6429760628699827e-10, 3.596684368902877e-11, 5.887270337382393e-12, 8.833586556738209e-13, 1.2234833198814563e-13, 1.5735275584979025e-14, 1.8888063351389084e-15, 2.125552245888137e-16], [3.287200219146094e-08, 5.9187567754328465e-08, 5.328498331603342e-08, 3.198069633784224e-08, 1.4395682534804222e-08, 5.184019095860615e-09, 1.5556778870606131e-09, 4.0015290566819477e-10, 9.00617380954666e-11, 1.8017816142850236e-11, 3.22675396041672e-12, 6.421614905251074e-13, 9.63534674794586e-14, 1.334529972810812e-14, 1.7163451726197061e-15, 2.0602395031605707e-16, 2.318473112643576e-17], [3.2595958142213437e-09, 5.869053761382002e-09, 5.283752038168062e-09, 3.1712137067754763e-09, 1.427479417286498e-09, 5.140486073008437e-10, 1.5426140152353506e-10, 3.967926044685467e-11, 8.930544078441939e-12, 1.7866510758477837e-12, 3.216948301145895e-13, 5.23739220057649e-14, 9.554433510087243e-15, 1.323323200086985e-15, 1.7019320903682265e-16, 2.042938553508656e-17, 2.299003635172811e-18], [2.9628712835990614e-10, 5.334787452981116e-10, 4.802766378348005e-10, 2.8825346949358805e-10, 1.2975344228122404e-10, 4.6725420688687154e-11, 1.402188193848226e-11, 3.6067214474723992e-12, 8.117586996979277e-13, 1.6240102970267537e-13, 2.924106019741233e-14, 4.786353448811265e-15, 7.143108069839825e-16, 1.202859658658249e-16, 1.54700337237742e-17, 1.8569676485469842e-18, 2.089722849018491e-19], [2.485991914856618e-11, 4.476143985397729e-11, 4.0297526428535953e-11, 2.4185856421004046e-11, 1.0886939646062189e-11, 3.9204881661025e-12, 1.1765035262617912e-12, 3.02621325711619e-13, 6.81104702534439e-14, 1.3626229699550906e-14, 2.453465988718247e-15, 4.0159814033288456e-16, 6.025800974570077e-17, 8.301090177898342e-18, 1.2980104459058951e-18, 1.5580854240925595e-19, 1.7533782637498148e-20], [1.9368766143999323e-12, 3.4874363654170644e-12, 3.139645631634976e-12, 1.884359294216732e-12, 8.482191223883172e-13, 3.054515905935105e-13, 9.166329758184062e-14, 2.3577718225336464e-14, 5.306597187275503e-15, 1.061641652564432e-15, 1.9115351378960779e-16, 3.128916235603e-17, 4.694799255349249e-18, 6.502464816773874e-19, 8.317899641128803e-20, 1.2139296202563613e-20, 1.3660854385562408e-21], [1.408448513927421e-13, 2.5359770104973197e-13, 2.2830722366406386e-13, 1.3702592245232553e-13, 6.168038549955699e-14, 2.2211680168459357e-14, 6.665527081126335e-15, 1.7145130438039204e-15, 3.85882552706909e-16, 7.719994122295071e-17, 1.3900208223247536e-17, 2.2752700866305523e-18, 3.4139412832101365e-19, 4.728430732221877e-20, 6.081256642158745e-21, 7.260487360148353e-22, 9.933833634666108e-23], [9.60176942368895e-15, 1.7288432113625745e-14, 1.5564312771875217e-14, 9.341422845388525e-15, 4.204916499784192e-15, 1.514229518376711e-15, 4.544067709075487e-16, 1.1688293010163016e-16, 2.6306643509349966e-17, 5.26292603396726e-18, 9.476142931822185e-19, 1.551112343292169e-19, 2.3273748882726787e-20, 3.2234974283922426e-21, 4.1457549570955874e-22, 4.9764163230612514e-23, 5.5700670630012495e-24]] |
| Legacy trial inputs | {"lambda_home": 1.0907627027887206, "lambda_away": 1.8005464775036863, "rho": -0.1036082449967548, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1961 |
| Legacy p draw | 0.2276 |
| Legacy p away | 0.5763 |
| Legacy p over 1 5 | 0.7991 |
| Legacy p under 3 5 | 0.6669 |
| Legacy p btts yes | 0.5580 |
| Legacy p over 2 5 | 0.5634 |
| Legacy goal margin distribution | {"-1": 0.24497157825788865, "-10": 7.12962021968189e-06, "-11": 1.1501177603122084e-06, "-12": 1.7044684416184987e-07, "-13": 2.3357540961890825e-08, "-14": 2.9756101335587198e-09, "-15": 3.520953276637301e-10, "-16": 3.529086495343921e-11, "-2": 0.18029876768064873, "-3": 0.0941122761618829, "-4": 0.03877972949739944, "-5": 0.013141822054316419, "-6": 0.00377313513102719, "-7": 0.0009384723360080131, "-8": 0.00020572652208089513, "-9": 4.029371564866724e-05, "0": 0.22761809949368236, "1": 0.118706422570571, "10": 3.924638933230807e-08, "11": 3.835319639857226e-09, "12": 3.4432944468447056e-10, "13": 2.8585004160492697e-11, "14": 2.2060386282215395e-12, "15": 1.5813328350636785e-13, "16": 9.60176942368895e-15, "2": 0.05471652714930117, "3": 0.017302066899082823, "4": 0.004318992284007707, "5": 0.000886664209222412, "6": 0.00015421687492387956, "7": 2.323683409283071e-05, "8": 3.0858279567923607e-06, "9": 3.661378993773457e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2175 |
| Legacy raw p draw | 0.2539 |
| Legacy raw p away | 0.5286 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0908 |
| Legacy lambda away | 1.8005 |
| Legacy model home team | Excelsior |
| Legacy model away team | Twente |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Elo home rating | 1,409.2021 |
| Elo away rating | 1,577.6366 |
| Elo rating diff | -108.4345 |
| Elo home expectancy | 0.3488 |

</details>


---

## 2026-11-01 — FC Zwolle vs ADO Den Haag

The model's most likely 1X2 outcome is **FC Zwolle win** at **43.0%**. Expected goals are 1.76 for FC Zwolle and 1.48 for ADO Den Haag (3.24 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.4%; Double Chance 1X: 68.3%; Double Chance X2: 57.0%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 77.4%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Zwolle win | 43.0% | 2.32 |
| Draw | 25.3% | 3.95 |
| ADO Den Haag win | 31.7% | 3.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Zwolle expected goals | 1.76 |
| ADO Den Haag expected goals | 1.48 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 84.3% |
| Under 1.5 | 15.7% |
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.6% |
| Under 3.5 | 59.4% |
| Over 4.5 | 22.6% |
| Under 4.5 | 77.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.32% |
| 2 | 2-1 | 8.90% |
| 3 | 1-2 | 7.58% |
| 4 | 2-2 | 6.72% |
| 5 | 2-0 | 6.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Zwolle win | 43.0% | 42.9% | 2.25 | -3.2% |
| Draw | 25.3% | 25.4% | 3.71 | -6.2% |
| ADO Den Haag win | 31.7% | 31.7% | 3.00 | -5.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T11:15:00+00:00 |
| Fixture id | 016bdfefaa570d0fcaeffc5a1cb3625f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:26:45Z |
| Market best draw last update utc | 2026-10-30T07:26:45Z |
| Market best away last update utc | 2026-10-30T07:26:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Zwolle |
| Matched away-team name | Den Haag |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.7588 |
| Dc lambda away | 1.4789 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.17 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.38 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.47 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.43 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.1652031430092644, "-10": 6.865078957880466e-07, "-11": 9.054059529827448e-08, "-12": 1.0977629534053504e-08, "-13": 1.2313848710781757e-09, "-14": 1.2842369378218471e-10, "-15": 1.2395607934384003e-11, "-16": 9.855093005105244e-13, "-2": 0.09491846792996443, "-3": 0.03920484528109371, "-4": 0.012939250724686435, "-5": 0.0035375424593013685, "-6": 0.0008231390542173204, "-7": 0.0001664339860717995, "-8": 2.9722485068506244e-05, "-9": 4.749798394916822e-06, "0": 0.2528751223849643, "1": 0.1957952584607407, "10": 3.836067945999917e-06, "11": 6.016799668342421e-07, "12": 8.675853865635975e-08, "13": 1.157387861010719e-08, "14": 1.4355281671996415e-09, "15": 1.6478430487723561e-10, "16": 1.5580815751407833e-11, "2": 0.1325378313825854, "3": 0.06510439936728864, "4": 0.025554134266356627, "5": 0.008308739767484245, "6": 0.0022992603756667794, "7": 0.0005528895910703042, "8": 0.00011742564881566474, "9": 2.2316931430823628e-05} |
| Raw goal margin distribution | {"-1": 0.16463149421139187, "-10": 6.841323876336088e-07, "-11": 9.022729967012763e-08, "-12": 1.093964388431148e-08, "-13": 1.2271239371246929e-09, "-14": 1.2797931210256486e-10, "-15": 1.2352715685208137e-11, "-16": 9.820991643795342e-13, "-2": 0.09459002364555379, "-3": 0.03906918561828416, "-4": 0.012894477320334658, "-5": 0.0035253015790284712, "-6": 0.0008202907642740784, "-7": 0.00016585807821478164, "-8": 2.9619637007932458e-05, "-9": 4.733362772124592e-06, "0": 0.249921568381801, "1": 0.1976380442219747, "10": 3.872172249268487e-06, "11": 6.073428581852307e-07, "12": 8.757509264729038e-08, "13": 1.1682809637715467e-08, "14": 1.449039070819896e-09, "15": 1.6633522175382336e-10, "16": 1.572745926893133e-11, "2": 0.1337852509085574, "3": 0.06571714893584772, "4": 0.025794644660412702, "5": 0.008386939962206472, "6": 0.0023209005538557623, "7": 0.0005580932771757219, "8": 0.00011853083550579372, "9": 2.252697392009772e-05} |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 84.3% |
| Raw p under 3 5 | 59.4% |
| Raw p btts yes | 64.9% |
| P home draw | 68.3% |
| P draw away | 57.0% |
| P home away | 74.7% |
| Raw p home draw | 68.4% |
| Raw p draw away | 56.6% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6268 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.26, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.25 |
| Reference draw odds | 3.71 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-30T07:26:45Z |
| Market reference home last update utc | 2026-10-30T07:26:45Z |
| Market reference draw last update utc | 2026-10-30T07:26:45Z |
| Market reference away last update utc | 2026-10-30T07:26:45Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:44Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:44Z |
| Home probability edge | +0.2% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | +3.3% |
| Under 2.5 probability edge | -3.3% |
| Raw edge prob home | 0.0058 |
| Raw ev home | -0.0227 |
| Raw edge prob draw | -0.0042 |
| Raw ev draw | -0.0728 |
| Raw edge prob away | -0.0016 |
| Raw ev away | -0.0528 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05022027248238647, 0.04807124845443618, 0.044068773114218994, 0.02211292927247826, 0.008321906984038323, 0.002505471256119088, 0.0006286005346369912, 0.00013518026011988238, 2.5436646970962072e-05, 4.254552870048752e-06, 6.404577667109036e-07, 8.764646068449553e-08, 1.0994860130755229e-08, 1.2731598323970276e-09, 1.3689622250878648e-10, 1.373841962044325e-11, 1.2925678997593353e-12], [0.058051028443760255, 0.11352897702496993, 0.07612157147487596, 0.03819645538511068, 0.014374728237858486, 0.004327790310989611, 0.0010858042360856177, 0.0002335017089320281, 4.393763210658857e-05, 7.349041679732145e-06, 1.106285658077311e-06, 1.513948732864099e-07, 1.899181602197824e-08, 2.199174615766223e-09, 2.3646575227620325e-10, 2.3730864673243648e-11, 2.2326988662163098e-12], [0.059401435873733456, 0.0894197630659044, 0.06687212964431521, 0.03298905328211271, 0.012414991678506761, 0.003737773668357204, 0.0009377742891853508, 0.0002016679359317134, 3.7947523455779354e-05, 6.347131562361029e-06, 9.554634363736209e-07, 1.307548957391196e-07, 1.6402622294563645e-08, 1.899356572349952e-09, 2.042278850899696e-10, 2.0495586599415357e-11, 1.9283103921007734e-12], [0.034202076489650096, 0.0514859873516763, 0.038752133870865034, 0.01932039503986307, 0.00714828671665862, 0.0021521301467845857, 0.0005399503816190958, 0.00011611608488569019, 2.1849372506519897e-05, 3.654542621615927e-06, 5.501354142916379e-07, 7.528587280232887e-08, 9.444279150793632e-09, 1.0936088970428074e-09, 1.1759004886707288e-10, 1.1800920470399287e-11, 1.1102798872843584e-12], [0.014769618179227438, 0.022233397875561906, 0.016734487482834088, 0.008397069216335528, 0.0031398534396317795, 0.0009293628867718559, 0.00023316891226342546, 5.014286892046979e-05, 9.435301083975497e-06, 1.5781556174612338e-06, 2.3756715526957518e-07, 3.251099669099818e-08, 4.078360478419225e-09, 4.722574622513384e-10, 5.077937662553687e-11, 5.096038235104527e-12, 4.794565620080985e-13], [0.005102418181566904, 0.007680909024298964, 0.005781216017602074, 0.0029009117311892003, 0.0010917195681491246, 0.0003265748420411146, 8.055220404968599e-05, 1.7322714978209004e-05, 3.2595867554074267e-06, 5.452009536171601e-07, 8.207165261018372e-08, 1.1231481992562086e-08, 1.4089396491872378e-09, 1.6314944858634914e-10, 1.7542607493210464e-11, 1.760513902879889e-12, 1.6563650119962998e-13], [0.0014689316374362272, 0.0022112515808332574, 0.0016643502764606567, 0.0008351414697344789, 0.00031429439058050615, 9.462441277813949e-05, 2.3588133770656683e-05, 4.9870244210299945e-06, 9.384001741142445e-07, 1.5695752504603809e-07, 2.3627551244487028e-08, 3.2334235742910546e-09, 4.0561866007106983e-10, 4.6968981790741336e-11, 5.050329124922742e-12, 5.068331285407185e-13, 4.768497764557241e-14], [0.00036247689602598494, 0.0005456534456238705, 0.0004106988417543973, 0.0002060813995539499, 7.755599527751775e-05, 2.3349734295303875e-05, 5.858241409001443e-06, 1.2517305716593233e-06, 2.3156175119003284e-07, 3.873119417994609e-08, 5.830388030000053e-09, 7.978869205866299e-10, 1.0009137874475361e-10, 1.1590172268822186e-11, 1.2462306471298263e-12, 1.2506729010018656e-13, 1.1766853026736565e-14], [7.826491696659686e-05, 0.00011781584449241221, 8.867685389217511e-05, 4.449647357191484e-05, 1.6745656336180862e-05, 5.041604129392708e-06, 1.26489379729435e-06, 2.7201483791454257e-07, 5.085623938857918e-08, 8.36272250657685e-09, 1.2588797797978345e-09, 1.7227733484003802e-10, 2.1611428293539484e-11, 2.502515002177944e-12, 2.69082358594938e-13, 2.7004151663853035e-14, 2.5406633779761434e-15], [1.5021088503862893e-05, 2.2611947931065732e-05, 1.701941204546326e-05, 8.540039311851478e-06, 3.2139302720834738e-06, 9.67615948041827e-07, 2.4276626633686707e-07, 5.2206775564869434e-08, 9.823662999007019e-09, 1.6325728927321225e-09, 2.416120187815097e-10, 3.306453509618228e-11, 4.147799418616808e-12, 4.802982075097965e-13, 5.164395593759853e-14, 5.182804350097181e-15, 4.876198805064976e-16], [2.5946464613699543e-06, 3.905842820174683e-06, 2.939824049835151e-06, 1.4751516026789527e-06, 5.551536964452783e-07, 1.6713977118943253e-07, 4.193388739630699e-08, 9.017863482003241e-09, 1.6968765233964012e-09, 2.8382085465022486e-10, 4.24508058111084e-11, 5.711355669203976e-12, 7.164642616424788e-13, 8.296363104425793e-14, 8.920645630320089e-15, 8.952443735015754e-16, 8.42283298660053e-17], [4.0743871268767115e-07, 6.133365737126717e-07, 4.6164213284019475e-07, 2.3164384010040655e-07, 8.717607997508803e-08, 2.6246047092049073e-08, 6.5849006225380186e-09, 1.4160798948927304e-09, 2.6646142223072676e-10, 4.4568539635085924e-11, 6.709110976431803e-12, 9.122501124446449e-13, 1.1250676375239394e-13, 1.302782307178753e-14, 1.4008137239789753e-15, 1.405806997257628e-16, 1.322641939985848e-17], [5.86486244449114e-08, 8.828652076951172e-08, 6.645091699385722e-08, 3.334389236950125e-08, 1.2548530652161584e-08, 3.77797816243597e-09, 9.478612404568926e-10, 2.038371302317008e-10, 3.835569717560553e-11, 6.41540300840293e-12, 9.657406568472305e-13, 1.321613303972736e-13, 1.6472700063291975e-14, 1.8752854819117904e-15, 2.0163964654457996e-16, 2.0235840153803345e-17, 1.903872361603068e-18], [7.792759330993563e-09, 1.1730805539587772e-08, 8.829465453931703e-09, 4.4304692710763276e-09, 1.6673482158433707e-09, 5.019874695486951e-10, 1.25944207489396e-10, 2.7084244748281685e-11, 5.0963977397750705e-12, 8.524273523716679e-13, 1.2831988109175638e-13, 1.756053872358528e-14, 2.2028917719969693e-15, 2.534495027781822e-16, 2.679226072189413e-17, 2.688776312685154e-18, 2.529713058289865e-19], [9.614794663644455e-10, 1.4473600647936205e-09, 1.089389441191325e-09, 5.466363132191617e-10, 2.0571931003140576e-10, 6.193578215917784e-11, 1.5539138867921176e-11, 3.3416847718998837e-12, 6.287993214073956e-13, 1.0517345154149296e-13, 1.583225216584749e-14, 2.16663914332284e-15, 2.7179528013580123e-16, 3.1472781753361945e-17, 3.3623949872833778e-18, 3.3174426470633413e-19, 3.1211886034591553e-20], [1.1071986314177938e-10, 1.6667179476725693e-10, 1.254494287775913e-10, 6.294829989121286e-11, 2.3689755890912496e-11, 7.132259776875891e-12, 1.7894207718266447e-12, 3.848141260954183e-13, 7.24098405066522e-14, 1.2111324857361795e-14, 1.8231744455833504e-15, 2.495008971261768e-16, 3.1298782004160654e-17, 3.624270939034777e-18, 3.8969891154052074e-19, 3.885792169616821e-20, 3.5942273039005185e-21], [1.1953149277027455e-11, 1.7993635347724184e-11, 1.3543330946645117e-11, 6.795803426628641e-12, 2.557510282846135e-12, 7.699879983266205e-13, 1.9318316513513194e-13, 4.154395212029233e-14, 7.817257067897899e-15, 1.307520347791971e-15, 1.9682716079781934e-16, 2.6935740195799643e-17, 3.378969255099283e-18, 3.912708192133604e-19, 4.207130618265052e-20, 4.222127153876021e-21, 3.9468712610081477e-22]] |
| Legacy trial inputs | {"lambda_home": 1.7273358456697079, "lambda_away": 1.505346827911355, "rho": -0.1036082449967548, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4247 |
| Legacy p draw | 0.2534 |
| Legacy p away | 0.3219 |
| Legacy p over 1 5 | 0.8437 |
| Legacy p under 3 5 | 0.5952 |
| Legacy p btts yes | 0.6505 |
| Legacy p over 2 5 | 0.6267 |
| Legacy goal margin distribution | {"-1": 0.1653453022152375, "-10": 8.094014587644259e-07, "-11": 1.086604850024271e-07, "-12": 1.3410543008643829e-08, "-13": 1.5312314511599307e-09, "-14": 1.6255539757413092e-10, "-15": 1.597111848665956e-11, "-16": 1.2925678997593353e-12, "-2": 0.09708382037590498, "-3": 0.04081894698041152, "-4": 0.01371359261867552, "-5": 0.003816456363983031, "-6": 0.0009039535257668585, "-7": 0.00018604912738216797, "-8": 3.382068464773425e-05, "-9": 5.501528021685702e-06, "0": 0.25343309486974197, "1": 0.19581247894836676, "10": 3.279077466100533e-06, "11": 5.051257949682229e-07, "12": 7.153432523586455e-08, "13": 9.372364627991401e-09, "14": 1.1416945920783473e-09, "15": 1.2871349848950357e-10, "16": 1.1953149277027455e-11, "2": 0.13086178540731036, "3": 0.06313468150909261, "4": 0.024338715541016732, "5": 0.007772252941710921, "6": 0.0021123843515942547, "7": 0.0004988783875842866, "8": 0.00010406139923749012, "9": 1.9423648464209996e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4208 |
| Legacy raw p draw | 0.2527 |
| Legacy raw p away | 0.3265 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7273 |
| Legacy lambda away | 1.5053 |
| Legacy model home team | Zwolle |
| Legacy model away team | Den Haag |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Elo home rating | 1,408.9706 |
| Elo away rating | 1,360.6524 |
| Elo rating diff | 108.3181 |
| Elo home expectancy | 0.6510 |

</details>


---

## 2026-11-01 — Groningen vs Sparta Rotterdam

The model's most likely 1X2 outcome is **Groningen win** at **52.8%**. Expected goals are 1.67 for Groningen and 1.21 for Sparta Rotterdam (2.89 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 56.3%; Under 3.5 goals: 66.8%; Double Chance 1X: 76.2%; Double Chance X2: 47.2%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Groningen win | 52.8% | 1.89 |
| Draw | 23.4% | 4.27 |
| Sparta Rotterdam win | 23.8% | 4.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Groningen expected goals | 1.67 |
| Sparta Rotterdam expected goals | 1.21 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 79.8% |
| Under 1.5 | 20.2% |
| Over 2.5 | 56.3% |
| Under 2.5 | 43.7% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.04% |
| 2 | 2-1 | 10.63% |
| 3 | 1-0 | 9.24% |
| 4 | 2-0 | 8.75% |
| 5 | 1-2 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Groningen win | 52.8% | 55.2% | 1.76 | -7.1% |
| Draw | 23.4% | 22.2% | 4.20 | -1.7% |
| Sparta Rotterdam win | 23.8% | 22.6% | 4.12 | -1.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:45:00+00:00 |
| Fixture id | 961d9c9f07b1f911e211cd6a750cddba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:26:45Z |
| Market best draw last update utc | 2026-10-30T07:26:45Z |
| Market best away last update utc | 2026-10-30T07:26:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Groningen |
| Matched away-team name | Sparta Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6733 |
| Dc lambda away | 1.2144 |
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
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.89 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.94 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.83 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.13685100847607445, "-10": 1.149025673021301e-07, "-11": 1.2495365876516914e-08, "-12": 1.2484333311183758e-09, "-13": 1.1530643498674301e-10, "-14": 9.833103093076548e-12, "-15": 7.011109889700168e-13, "-2": 0.06878463732838434, "-3": 0.024116100928480242, "-4": 0.006683849171944378, "-5": 0.0015247127305979195, "-6": 0.0002948250582418247, "-7": 4.940357331502612e-05, "-8": 7.297983513087444e-06, "-9": 9.633814694030144e-07, "0": 0.2339481550366874, "1": 0.24143309998433815, "10": 3.5598018323029613e-06, "11": 5.334002534589896e-07, "12": 7.343071317875608e-08, "13": 9.344887699111389e-09, "14": 1.098042841018803e-09, "15": 1.0787569757716104e-10, "2": 0.1640296419054717, "3": 0.07924030315625291, "4": 0.030260341663875444, "5": 0.009511376283074479, "6": 0.0025341241076591615, "7": 0.0005850998681480981, "8": 0.00011909202134430368, "9": 2.166138531537386e-05} |
| Raw goal margin distribution | {"-1": 0.15321405355468107, "-10": 1.2864127415821507e-07, "-11": 1.3989415773466526e-08, "-12": 1.3977064062838866e-09, "-13": 1.2909343162309857e-10, "-14": 1.1008830703463343e-11, "-15": 7.849416515670598e-13, "-2": 0.07700910080770709, "-3": 0.026999622584675705, "-4": 0.007483025783918374, "-5": 0.001707020069217649, "-6": 0.00033007679494464353, "-7": 5.531067554393919e-05, "-8": 8.170591136059077e-06, "-9": 1.078571372548608e-06, "0": 0.2628055826033378, "1": 0.21519532266325628, "10": 3.1729398494629816e-06, "11": 4.754329031902259e-07, "12": 6.545061972414108e-08, "13": 8.32933066672558e-09, "14": 9.787128752704102e-10, "15": 9.615229042391849e-11, "2": 0.1462036966699106, "3": 0.07062885166429239, "4": 0.02697179462418568, "5": 0.008477726079566693, "6": 0.002258727801000881, "7": 0.0005215140547196163, "8": 0.0001061496785712868, "9": 1.9307331109849435e-05} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 58.2% |
| P home draw | 76.2% |
| P draw away | 47.2% |
| P home away | 76.6% |
| Raw p home draw | 73.3% |
| Raw p draw away | 53.0% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5630 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.81, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.76 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.12 |
| Market reference 1x2 last update utc | 2026-10-30T07:26:45Z |
| Market reference home last update utc | 2026-10-30T07:26:45Z |
| Market reference draw last update utc | 2026-10-30T07:26:45Z |
| Market reference away last update utc | 2026-10-30T07:26:45Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:24Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:24Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | -0.0819 |
| Raw ev home | -0.1721 |
| Raw edge prob draw | 0.0412 |
| Raw ev draw | 0.1038 |
| Raw edge prob away | 0.0407 |
| Raw ev away | 0.0992 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05682689329472522, 0.0468242695776684, 0.034796229947771304, 0.014033147374996889, 0.00424462417790599, 0.0010271015577739905, 0.00020711248820584442, 3.579747503710423e-05, 5.413854212106582e-06, 7.277935391207088e-07, 8.805466001674367e-08, 9.685093285249233e-09, 9.764875506376587e-10, 9.087983025205471e-11, 7.853868405054446e-12, 6.334852537610603e-13, 4.790277534696145e-14], [0.08188241952461855, 0.1111679926079362, 0.06244904137615968, 0.025185389404953563, 0.007617857202063836, 0.001843346471017739, 0.0003717062556748215, 6.424598305936158e-05, 9.71628266061608e-06, 1.3061762411063126e-06, 1.5803232462261348e-07, 1.7381905804460138e-08, 1.7525091524170072e-09, 1.6310267773800705e-10, 1.4095393487350278e-11, 1.1369204906017504e-12, 8.597145162465745e-14], [0.08400825806824817, 0.10164034448197512, 0.05468177058149382, 0.022600198748332752, 0.006835911251354271, 0.0016541335111874363, 0.0003335519304139599, 5.765136137374993e-05, 8.718940799133044e-06, 1.172101895059315e-06, 1.4181086850416674e-07, 1.5597714988211916e-08, 1.5726203202999298e-09, 1.463607679037601e-10, 1.2648551472760468e-11, 1.0202196454265587e-12, 7.71467878522371e-14], [0.05025673942184408, 0.0608048830536073, 0.03678346273252118, 0.013192824696951247, 0.004089486181121191, 0.0009895617258621316, 0.0001995426739696118, 3.4489102767983815e-05, 5.215981688616054e-06, 7.011932025538545e-07, 8.483632477903992e-08, 9.331110009469864e-09, 9.407976247121186e-10, 8.755823705027405e-11, 7.566815097081096e-12, 6.103318179933536e-13, 4.6151962955503484e-14], [0.022549031923116677, 0.02728173902306967, 0.016503885547295986, 0.006655935384175714, 0.001790422560734668, 0.0004439933669206763, 8.953016405614916e-05, 1.5474459510536685e-05, 2.3402898588338177e-06, 3.1460910696858574e-07, 3.806408887025788e-08, 4.1866523754264084e-09, 4.2211404712827857e-10, 3.928534769846797e-11, 3.3950542184645e-12, 2.7384171368754076e-13, 2.0707314043254747e-14], [0.008093781594573314, 0.009792546213325577, 0.005923928155190874, 0.002389090914891242, 0.0007226314090188307, 0.00015550818968330785, 3.2136084443337446e-05, 5.554424509193759e-06, 8.400269710016729e-07, 1.1292624038804106e-07, 1.3662778205411917e-08, 1.5027629591656223e-09, 1.515142165351767e-10, 1.4101138586455308e-11, 1.2186255906541103e-12, 9.829313425195968e-14, 7.432712758924483e-15], [0.00242099456582787, 0.002929125389789979, 0.0017719526656967937, 0.0007146197429021868, 0.00021615195491611925, 5.230380837150208e-05, 9.379690267959463e-06, 1.6614275287679216e-06, 2.5126706326094146e-07, 3.377825446910047e-08, 4.086780870340188e-09, 4.4950322854111785e-10, 4.5320607010605625e-11, 4.217902285957806e-12, 3.64512669174379e-13, 2.940123119231868e-14, 2.223257075627117e-15], [0.0006207108809520655, 0.0007509888815028705, 0.0004543051503107823, 0.00018321901933343387, 5.541849298187755e-05, 1.3410002413748225e-05, 2.7040938120833083e-06, 4.156522637788328e-07, 6.442154079664556e-08, 8.660296220602546e-09, 1.0477963850445354e-09, 1.1524666305194519e-10, 1.1619602249382107e-11, 1.0814141760749187e-12, 9.345621142443498e-14, 7.538085533958609e-15, 5.700136123698913e-16], [0.0001392492791079326, 0.00016847563588211548, 0.00010191808556467496, 4.1103059643340264e-05, 1.2432495439967025e-05, 3.0083783388586685e-06, 6.066320496835314e-07, 1.0485073036093628e-07, 1.410223374418892e-08, 1.94283690295609e-09, 2.350609530890708e-10, 2.5854250734195664e-11, 2.6067228502029788e-12, 2.4260271417275236e-13, 2.0965815919080192e-14, 1.6910819653228095e-15, 1.2787593554420956e-16], [2.776796351426022e-05, 3.359604688933625e-05, 2.0323679228598078e-05, 8.196439276472459e-06, 2.479187554720666e-06, 5.999064446557662e-07, 1.2096965047220552e-07, 2.0908483503525415e-08, 3.162107980157664e-09, 3.7804249660058556e-10, 4.6873951598308275e-11, 5.155645297949575e-12, 5.198115599587422e-13, 4.8377868515843015e-14, 4.180833216640689e-15, 3.3722187011330966e-16, 2.5499983449043384e-17], [4.9835361619249075e-06, 6.029506430485977e-06, 3.647505166414757e-06, 1.4710207866826471e-06, 4.4494155377291755e-07, 1.076656363070514e-07, 2.1710509210157094e-08, 3.752460405579199e-09, 5.675057682546396e-10, 7.62907561540613e-11, 8.208775062238939e-12, 9.25287328586233e-13, 9.329095038282659e-14, 8.682410471395895e-15, 7.5033711101664805e-16, 6.052144887897788e-17, 4.576500166515e-18], [8.130897995735573e-07, 9.837452796164115e-07, 5.95109405919944e-07, 2.400046789567879e-07, 7.259452465564751e-08, 1.7566207568572474e-08, 3.5421822996280067e-09, 6.122333981221895e-10, 9.259151260754018e-11, 1.2447232971750136e-11, 1.5059722415244966e-12, 1.473094871616284e-13, 1.5220902925985853e-14, 1.4165803478941462e-15, 1.2242139544814268e-16, 9.874388614830905e-18, 7.46679763572287e-19], [1.2160483720103594e-07, 1.471278875196601e-07, 8.900392362769164e-08, 3.589484203015974e-08, 1.0857159144127207e-08, 2.627183138610525e-09, 5.297649805821808e-10, 9.156496951103444e-11, 1.3847887186314379e-11, 1.86159479546651e-12, 2.2523159109352246e-13, 2.477312353612043e-14, 2.2212935632552527e-15, 2.1186223548518453e-16, 1.830921242795428e-17, 1.4768029565689383e-18, 1.1167262353818475e-19], [1.6788082018583215e-08, 2.0311651244740927e-08, 1.2287382675141435e-08, 4.955440638024851e-09, 1.4988785182869808e-09, 3.6269417421214754e-10, 7.313638297038919e-11, 1.2640946310705e-11, 1.9117616635890932e-12, 2.5700134000420477e-13, 3.1094210653832767e-14, 3.420038539201638e-15, 3.448211553437261e-16, 2.854019829088493e-17, 2.5276672130073877e-18, 2.0387913614964581e-19, 1.541689628752236e-20], [2.1521207288804693e-09, 2.6038189254264073e-09, 1.5751609343811331e-09, 6.352546113382619e-10, 1.921462812552595e-10, 4.649498672344587e-11, 9.375599050069352e-12, 1.6204854466293112e-12, 2.45075161077651e-13, 3.2945866630915106e-14, 3.986071501331446e-15, 4.38426249385639e-16, 4.420378428877682e-17, 4.113961729506102e-18, 3.161830958540735e-19, 2.6135952553019827e-20, 1.9763438157289438e-21], [2.574950919416214e-10, 3.1153948967852964e-10, 1.884635021532044e-10, 7.600639794867651e-11, 2.2989753174210362e-11, 5.5629922246072604e-12, 1.1217636199532517e-12, 1.9388645045342583e-13, 2.9322542312542524e-14, 3.9418787447100766e-15, 4.769220582969554e-16, 5.2456447205869315e-17, 5.288856404225623e-18, 4.922237584387494e-19, 4.2538158509949923e-20, 3.0513629031272437e-21, 2.364638868582934e-22], [2.88830170591697e-11, 3.494513362231402e-11, 2.1139799235303407e-11, 8.525576437221476e-12, 2.578742096052697e-12, 6.239963570248863e-13, 1.258273217060438e-13, 2.1748086978130765e-14, 3.2890859528437283e-15, 4.4215736373900333e-16, 5.349596313396261e-17, 5.8839974311201934e-18, 5.932467628601656e-19, 5.521234251384584e-20, 4.771470976957884e-21, 3.848621273952636e-22, 2.5881630300192438e-23]] |
| Legacy trial inputs | {"lambda_home": 1.7947071125203762, "lambda_away": 1.2098851567592637, "rho": -0.1036082449967548, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5261 |
| Legacy p draw | 0.2378 |
| Legacy p away | 0.2361 |
| Legacy p over 1 5 | 0.8145 |
| Legacy p under 3 5 | 0.6439 |
| Legacy p btts yes | 0.5920 |
| Legacy p over 2 5 | 0.5845 |
| Legacy goal margin distribution | {"-1": 0.13644085317436716, "-10": 1.071002399491638e-07, "-11": 1.1591811295093528e-08, "-12": 1.1528698189804629e-09, "-13": 1.0604159534778705e-10, "-14": 9.067935683508434e-12, "-15": 7.194567053857178e-13, "-16": 4.790277534696145e-14, "-2": 0.06790243708617741, "-3": 0.023521030101133027, "-4": 0.006458469102888289, "-5": 0.0014620038897660275, "-6": 0.0002808182185420511, "-7": 4.677503839722572e-05, "-8": 6.871609019090876e-06, "-9": 9.024049103007802e-07, "0": 0.23782522176269077, "1": 0.22773990952515316, "10": 6.061438640907837e-06, "11": 9.731639381292281e-07, "12": 1.4357023452020275e-07, "13": 1.9588890022600052e-08, "14": 2.4848000177943022e-09, "15": 2.924402255639354e-10, "16": 2.88830170591697e-11, "2": 0.16393630766208747, "3": 0.08423557803092309, "4": 0.03430980456020864, "5": 0.011520905683200904, "6": 0.0032825610225882262, "7": 0.0008110565133438892, "8": 0.00017674406526873332, "9": 3.443002070971302e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4998 |
| Legacy raw p draw | 0.2541 |
| Legacy raw p away | 0.2461 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7947 |
| Legacy lambda away | 1.2099 |
| Legacy model home team | Groningen |
| Legacy model away team | Sparta Rotterdam |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,487.9195 |
| Elo away rating | 1,450.6913 |
| Elo rating diff | 97.2282 |
| Elo home expectancy | 0.6364 |

</details>


---

## 2026-11-01 — SC Telstar vs FC Utrecht

The model's most likely 1X2 outcome is **FC Utrecht win** at **41.1%**. Expected goals are 1.46 for SC Telstar and 1.60 for FC Utrecht (3.06 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.2%; Under 3.5 goals: 63.3%; Double Chance 1X: 58.9%; Double Chance X2: 66.7%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 80.4%; BTTS Yes (both teams score): 62.3%; BTTS No (at least one team does not score): 37.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Telstar win | 33.3% | 3.01 |
| Draw | 25.7% | 3.89 |
| FC Utrecht win | 41.1% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Telstar expected goals | 1.46 |
| FC Utrecht expected goals | 1.60 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 36.7% |
| Under 3.5 | 63.3% |
| Over 4.5 | 19.6% |
| Under 4.5 | 80.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.82% |
| 2 | 1-2 | 9.00% |
| 3 | 2-1 | 7.83% |
| 4 | 0-1 | 6.62% |
| 5 | 2-2 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Telstar win | 33.3% | 32.9% | 2.90 | -3.5% |
| Draw | 25.7% | 25.5% | 3.70 | -5.0% |
| FC Utrecht win | 41.1% | 41.6% | 2.32 | -4.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:30:00+00:00 |
| Fixture id | d7d5552edc5c81a14b6933537ba2043c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:26:45Z |
| Market best draw last update utc | 2026-10-30T07:26:45Z |
| Market best away last update utc | 2026-10-30T07:26:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Telstar |
| Matched away-team name | Utrecht |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4644 |
| Dc lambda away | 1.5983 |
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
| P btts yes | 62.3% |
| P btts no | 37.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.73 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.58 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.72 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.10 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.1989973309472319, "-10": 1.7817918121699667e-06, "-11": 2.5445382226394934e-07, "-12": 3.3396304379553804e-08, "-13": 4.052304864505207e-09, "-14": 4.531565546572789e-10, "-15": 4.1768657682171685e-11, "-2": 0.1258724845057806, "-3": 0.057030992620063566, "-4": 0.020549516767684958, "-5": 0.006116076353769267, "-6": 0.0015464305203463128, "-7": 0.0003393539444743556, "-8": 6.571688157075766e-05, "-9": 1.138092816150394e-05, "0": 0.2568525013128031, "1": 0.1721556910534091, "10": 7.048920985685862e-07, "11": 9.223144387978138e-08, "12": 1.1091053092697031e-08, "13": 1.233050403379889e-09, "14": 1.2633722400289368e-10, "15": 1.0669349148061662e-11, "2": 0.10026785574449792, "3": 0.04162422865411001, "4": 0.013741724166357518, "5": 0.0037472861399691095, "6": 0.000868117908868907, "7": 0.00017454425138551272, "8": 3.0969481924515175e-05, "9": 4.914043769717716e-06} |
| Raw goal margin distribution | {"-1": 0.1933623086437126, "-10": 1.7313366801638586e-06, "-11": 2.4724843434820236e-07, "-12": 3.2450618730715605e-08, "-13": 3.937555444583583e-09, "-14": 4.403244866072967e-10, "-15": 4.058589147869175e-11, "-2": 0.12230814394797916, "-3": 0.05541604173667148, "-4": 0.01996761456446821, "-5": 0.005942886962235893, "-6": 0.0015026401316435365, "-7": 0.000329744433448264, "-8": 6.385597172032781e-05, "-9": 1.1058653567570662e-05, "0": 0.2604928932487643, "1": 0.17628839439554186, "10": 7.218134673236486e-07, "11": 9.444551646744535e-08, "12": 1.1357300649797777e-08, "13": 1.2626505373742122e-09, "14": 1.2937002683780287e-10, "15": 1.0925473442372072e-11, "2": 0.10267484734615934, "3": 0.04262344388667045, "4": 0.01407160271432462, "5": 0.0038372420505743154, "6": 0.0008889576136814233, "7": 0.0001787342935888064, "8": 3.1712923402809705e-05, "9": 5.032008415476645e-06} |
| Unadjusted home-win probability | 34.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 39.9% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 63.3% |
| Raw p btts yes | 62.4% |
| P home draw | 58.9% |
| P draw away | 66.7% |
| P home away | 74.3% |
| Raw p home draw | 60.1% |
| Raw p draw away | 65.9% |
| Raw p home away | 74.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5921 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:26:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:26:45Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.90 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.32 |
| Market reference 1x2 last update utc | 2026-10-30T07:26:45Z |
| Market reference home last update utc | 2026-10-30T07:26:45Z |
| Market reference draw last update utc | 2026-10-30T07:26:45Z |
| Market reference away last update utc | 2026-10-30T07:26:45Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-30T07:26:24Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:26:24Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | 0.0114 |
| Raw ev home | -0.0123 |
| Raw edge prob draw | 0.0052 |
| Raw ev draw | -0.0362 |
| Raw edge prob away | -0.0166 |
| Raw ev away | -0.0745 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.055994890016975975, 0.06324502245848194, 0.06015706761267441, 0.032285520929643964, 0.012995416453928836, 0.004184683262297462, 0.0011229327193831699, 0.00025828434928511527, 5.1981702414009975e-05, 9.299302685716117e-06, 1.4972446799959644e-06, 2.1915051126453882e-07, 2.9403811966570838e-08, 3.6416875318034175e-09, 4.1880999556599885e-10, 4.495398267897399e-11], [0.05499714609145931, 0.11828614983874407, 0.08920996602790014, 0.04787783613175608, 0.019271562035532964, 0.0062056790080044655, 0.0016652538716279447, 0.0003830229587256151, 7.70863024155988e-05, 1.3790407504855006e-05, 2.2203400587589928e-06, 3.249894059129206e-07, 4.360440378373576e-08, 5.40044310484248e-09, 6.210745795846607e-10, 6.666454045650901e-11], [0.04894358238034492, 0.07880216486713137, 0.06397761979700349, 0.03550023550269795, 0.01428938828571031, 0.004601358040326855, 0.0012347447042486725, 0.0002840020839764038, 5.7157593385279364e-05, 1.0225247288814124e-05, 1.646327431446667e-06, 2.409716348508545e-07, 3.233159073892707e-08, 4.004295463839239e-09, 4.605114938636612e-10, 4.9430113745585454e-11], [0.0241936400532173, 0.03895324206949126, 0.031358552586273666, 0.01697284635205725, 0.0070634861600152995, 0.0022745290550769195, 0.000610355177928398, 0.00014038703053432445, 2.8253964532578578e-05, 5.054512569967741e-06, 8.138074768747189e-07, 1.1911635219734404e-07, 1.5982051796021864e-08, 1.979390931501623e-09, 2.2763861534134578e-10, 2.44341407307884e-11], [0.008969493913563147, 0.014441434479777311, 0.01162579694258648, 0.006239415008230648, 0.0025328169716235687, 0.0008432536183418153, 0.00022628166086204548, 5.204676159317235e-05, 1.0474809179253367e-05, 1.8738982489873473e-06, 3.0170909357103056e-07, 4.416091971649559e-08, 5.925148757911112e-09, 7.338347959882508e-10, 8.439421146652224e-11, 9.058656576103252e-12], [0.002660263470514774, 0.004283187098247607, 0.0034480967622061835, 0.0018505489812171414, 0.0007448742961811544, 0.0002418983518942163, 6.7112909851965e-05, 1.5436556394284347e-05, 3.106725138420976e-06, 5.557797471387451e-07, 8.948394280478327e-08, 1.309769343490862e-08, 1.7573407095133702e-09, 2.1764816610313e-10, 2.5030491134822658e-11, 2.686708237229048e-12], [0.0006575065996620198, 0.0010586258902168305, 0.0008522262559900142, 0.00045737882041911083, 0.00018410197752440668, 5.928309159106131e-05, 1.604351479682862e-05, 3.8152753732068895e-06, 7.67853374106747e-07, 1.3736566161678007e-07, 2.2116712727908338e-08, 3.2372056261539754e-09, 4.3434160832806135e-10, 5.3793583681939565e-11, 6.186497426415786e-12, 6.640426472504915e-13], [0.00013929283967247365, 0.0002242700019663703, 0.00018054421856953211, 9.689574938863453e-05, 3.9002022568099614e-05, 1.2559128952510912e-05, 3.3701611194306168e-06, 7.817583877554083e-07, 1.6266981500474402e-07, 2.9100929313751308e-08, 4.685427829430573e-09, 6.858023394783916e-10, 9.201531367597582e-11, 1.1396176146471967e-11, 1.310610105807098e-12, 1.4067750201548378e-13], [2.5820551907380986e-05, 4.157266978444296e-05, 3.346727210180764e-05, 1.7961452523881827e-05, 7.2297596242592055e-06, 2.328071147033144e-06, 6.247228524101359e-07, 1.436917213588063e-07, 2.916498021523617e-08, 5.394405467399118e-09, 8.685323148165172e-10, 1.2712638313887757e-10, 1.7056771824244665e-11, 2.1124959360978976e-12, 2.4294627309559896e-13, 2.6077225157678394e-14], [4.254511748976914e-06, 6.850024456049296e-06, 5.514479429955392e-06, 2.9595498603460077e-06, 1.191264128436271e-06, 3.836016396177538e-07, 1.0293702183312031e-07, 2.367641555241129e-08, 4.765059868638381e-09, 8.596977255911895e-10, 1.4311006794152585e-10, 2.0946906658284342e-11, 2.8104835398628e-12, 3.480808160891908e-13, 4.003081641953257e-14, 4.296804391014757e-15], [6.309231211788082e-07, 1.0158248619247713e-06, 8.177701176781192e-07, 4.3888665617689936e-07, 1.7665859830851374e-07, 5.688623231917062e-08, 1.526505294418822e-08, 3.511095721441118e-09, 7.066348907481941e-10, 1.2641393860129404e-10, 2.0526499277048915e-11, 3.106323006644406e-12, 4.167808556218716e-13, 5.161866927791875e-14, 5.936372756479235e-15, 6.37194911525569e-16], [8.5057080860044e-08, 1.3694710895828944e-07, 1.1024661593367485e-07, 5.916793433260966e-08, 2.381599940873111e-08, 7.669043501139428e-09, 2.057938279676223e-09, 4.733438079238404e-10, 9.526406470664672e-11, 1.704233089026325e-11, 2.743919638122046e-12, 4.050406659796215e-13, 5.618776955156319e-14, 6.958903833571024e-15, 8.003043803812596e-16, 8.590260412707052e-17], [1.0511288192564506e-08, 1.692381768623946e-08, 1.3624191432581817e-08, 7.311927510798779e-09, 2.943162766084482e-09, 9.477344576923766e-10, 2.54318419130567e-10, 5.849546127076917e-11, 1.1772659353009432e-11, 2.106078055457366e-12, 3.3909146424853234e-13, 4.9632547537725914e-14, 6.715915866184956e-15, 8.599759474389412e-16, 9.890099564786353e-17, 1.0615777303210781e-17], [1.1990555592872481e-09, 1.93055287889489e-09, 1.5541541796548616e-09, 8.340944678056253e-10, 3.3573579297894186e-10, 1.0811103733488998e-10, 2.901089844566921e-11, 6.672760440476072e-12, 1.3429441174304814e-12, 2.402469187815996e-13, 3.868122516150492e-14, 5.6617401175240066e-15, 7.596456921713992e-16, 9.488283505939487e-17, 1.1281946273198132e-17, 1.210974959336999e-18], [1.2701002078461245e-10, 2.0449391137470465e-10, 1.6462386011353163e-10, 8.835149870394282e-11, 3.556283085809737e-11, 1.1451667099656823e-11, 3.0729808856855646e-12, 7.068124872707213e-13, 1.422514235860834e-13, 2.5448167027413052e-14, 4.097310732337858e-15, 5.997201084086963e-16, 8.046550837809607e-17, 9.965722775464678e-18, 1.1558479095920555e-18, 1.2827258383795323e-19], [1.2556640019258431e-11, 2.0216959381628517e-11, 1.6275271331006738e-11, 8.7347278390635e-12, 3.5158616807738104e-12, 1.1321505224743418e-12, 3.038052787429384e-13, 6.98778719107995e-14, 1.4063456624627997e-14, 2.515891821284554e-15, 4.0507399018742395e-16, 5.929035730471255e-17, 7.955092176418139e-18, 9.85245043266661e-19, 1.1330748961803207e-19, 1.2265557260866611e-20]] |
| Legacy trial inputs | {"lambda_home": 1.4829507083404545, "lambda_away": 1.610061238565513, "rho": -0.1036082449967548, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3356 |
| Legacy p draw | 0.2580 |
| Legacy p away | 0.4063 |
| Legacy p over 1 5 | 0.8258 |
| Legacy p under 3 5 | 0.6261 |
| Legacy p btts yes | 0.6291 |
| Legacy p over 2 5 | 0.5984 |
| Legacy goal margin distribution | {"-1": 0.19593306016315623, "-10": 1.8566321484990175e-06, "-11": 2.6699590778403124e-07, "-12": 3.528920070600776e-08, "-13": 4.312192225133664e-09, "-14": 4.854745360225079e-10, "-15": 4.495398267897399e-11, "-2": 0.12484133714668053, "-3": 0.05682409185124252, "-4": 0.020587280605568633, "-5": 0.006164159896000285, "-6": 0.0015684830368360657, "-7": 0.0003464556798571, "-8": 6.754370282660793e-05, "-9": 1.1777355960451757e-05, "0": 0.25802307664709945, "1": 0.17220495468797611, "10": 7.823652110188657e-07, "11": 1.0362692008632304e-07, "12": 1.2615199659411993e-08, "13": 1.4198247419929595e-09, "14": 1.4722698016624098e-10, "15": 1.2556640019258431e-11, "2": 0.10157048060340673, "3": 0.04258198675486203, "4": 0.014209432128867095, "5": 0.003918645299988312, "6": 0.0009183880123683002, "7": 0.00018684366900868974, "8": 3.355056883210318e-05, "9": 5.388242645611515e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3421 |
| Legacy raw p draw | 0.2608 |
| Legacy raw p away | 0.3972 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4830 |
| Legacy lambda away | 1.6101 |
| Legacy model home team | Telstar |
| Legacy model away team | Utrecht |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,388.0800 |
| Elo away rating | 1,522.9291 |
| Elo rating diff | -74.8492 |
| Elo home expectancy | 0.3939 |

</details>


---
