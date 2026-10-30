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
| Training as of utc | 2026-10-30T12:02:44.805088+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1314, 'tuning_matches': 189, 'audit_matches': 111, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.697527130180536, 'audit_candidate_poisson_score': 0.6897609882876101, 'audit_gain': 0.007766141892925904, 'audit_gain_lower95': -0.0040409684446989, 'audit_baseline_briers': [0.6185431327072937, 0.0906978089419721, 0.2827167334442277, 0.222891032722524], 'audit_candidate_briers': [0.6176465875952819, 0.08929765884844829, 0.27915634412666435, 0.21726144428100155], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1614.747 |
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
| Additional event odds calls used before this league | 28.00 |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 5, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 4} |
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

The model's most likely 1X2 outcome is **Ajax win** at **56.5%**. Expected goals are 1.87 for Ajax and 1.25 for AZ Alkmaar (3.12 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 70.5%; Under 3.5 goals: 50.7%; Double Chance 1X: 78.0%; Double Chance X2: 43.5%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 68.5%; BTTS No (at least one team does not score): 31.5%.

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
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 49.3% |
| Under 3.5 | 50.7% |
| Over 4.5 | 30.2% |
| Under 4.5 | 69.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.71% |
| 2 | 1-1 | 8.92% |
| 3 | 3-1 | 7.03% |
| 4 | 2-0 | 6.66% |
| 5 | 2-2 | 6.44% |

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
| Market best home last update utc | 2026-10-30T12:02:36Z |
| Market best draw last update utc | 2026-10-30T12:02:36Z |
| Market best away last update utc | 2026-10-30T12:02:36Z |
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
| P btts yes | 68.5% |
| P btts no | 31.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.85 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.80 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.11943365414203676, "-10": 3.7477334028072536e-07, "-11": 4.8522966652348035e-08, "-12": 5.778973651329454e-09, "-13": 6.370733305708901e-10, "-14": 6.535656417159108e-11, "-15": 6.264015381839207e-12, "-16": 5.565868479738849e-13, "-17": 4.0236740583121766e-14, "-2": 0.06457941682409386, "-3": 0.02550161698954693, "-4": 0.008123388586434467, "-5": 0.0021560389095973227, "-6": 0.0004888672757038135, "-7": 9.656775591324962e-05, "-8": 1.6878356565764443e-05, "-9": 2.6432943757798588e-06, "0": 0.2147465256082813, "1": 0.21709271356413382, "10": 2.402454202063126e-05, "11": 4.631289709110644e-06, "12": 8.21246428063861e-07, "13": 1.3479704750037116e-07, "14": 2.0589620582945117e-08, "15": 2.938191661092621e-09, "16": 3.8871242408674643e-10, "17": 4.183949661048064e-11, "2": 0.1714095999791033, "3": 0.10078059474755269, "4": 0.047798536805175026, "5": 0.018888703253461463, "6": 0.006376827840898848, "7": 0.0018754869219770424, "8": 0.0004880678873384696, "9": 0.0001138056396693127} |
| Raw goal margin distribution | {"-1": 0.14099983175325548, "-10": 1.4486697105087724e-07, "-11": 1.623902847266856e-08, "-12": 1.673012295264183e-09, "-13": 1.5942894776201582e-10, "-14": 1.4124959774532609e-11, "-15": 1.1599819670743e-12, "-16": 7.933786021218581e-14, "-2": 0.07104207483295685, "-3": 0.02526198546773359, "-4": 0.0071442150247747575, "-5": 0.0016689250593918026, "-6": 0.0003312185907084879, "-7": 5.705106922832396e-05, "-8": 8.671990355481712e-06, "-9": 1.1788366496523989e-06, "0": 0.24573969771840892, "1": 0.21475693786099473, "10": 7.75623817160494e-06, "11": 1.294523610157594e-06, "12": 1.9857164829511245e-07, "13": 2.8174321335440546e-08, "14": 3.716564541873844e-09, "15": 4.544371975441653e-10, "16": 4.6277649656224766e-11, "2": 0.15748963924535112, "3": 0.08338194242080232, "4": 0.03510970820390549, "5": 0.012211744639026802, "6": 0.003608475483864284, "7": 0.0009254245531930415, "8": 0.00020944220024403487, "9": 4.2390370319173945e-05} |
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
| Totals anchor scale | 1.1618 |
| Totals anchor target over 2 5 | 0.7054 |
| Totals anchor reference over odds | 1.38 |
| Totals anchor reference under odds | 3.09 |
| Totals anchor reference last update utc | 2026-10-30T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6165 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.65, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.94, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.65 |
| Reference draw odds | 4.56 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:36Z |
| Market reference home last update utc | 2026-10-30T12:02:36Z |
| Market reference draw last update utc | 2026-10-30T12:02:36Z |
| Market reference away last update utc | 2026-10-30T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 2.94 |
| Market reference over 2 5 last update utc | 2026-10-30T12:01:56Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:01:56Z |
| Home probability edge | -2.4% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.0816 |
| Raw ev home | -0.1622 |
| Raw edge prob draw | 0.0443 |
| Raw ev draw | 0.1206 |
| Raw edge prob away | 0.0373 |
| Raw ev away | 0.0847 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05060446982706753, 0.042020399668492754, 0.03236598508133505, 0.013426941169377213, 0.004177597608558876, 0.0010398390256652224, 0.0002156872004381082, 3.834739302466347e-05, 5.9656170148294445e-06, 8.249400154293788e-07, 1.0266723871620685e-07, 1.1615788816006241e-08, 1.204694625209848e-09, 1.1533022294696978e-10, 1.0252377929673605e-11, 8.506342381485801e-13, 6.616562019264133e-14], [0.07887353163068965, 0.10398725648490878, 0.05999979700122171, 0.024890753131273115, 0.0077443960947405415, 0.0019276450352762758, 0.00039983915859589545, 7.10880818619894e-05, 1.1059011767363658e-05, 1.529267017196122e-06, 1.9032368290872023e-07, 2.1533253791535394e-08, 2.2332529901194736e-09, 2.1379821894913877e-10, 1.9005773901655903e-11, 1.5768987559917163e-12, 1.2265728263923e-13], [0.08393274700493754, 0.10445781767996466, 0.054345829663121896, 0.02307113674017532, 0.007178248899481976, 0.0017867262577725114, 0.00037060927218198327, 6.589125080245602e-05, 1.0250552538544453e-05, 1.4174713107271563e-06, 1.7641023918090913e-07, 1.995908440637857e-08, 2.0699930146234365e-09, 1.9816869012228361e-10, 1.7616373688068117e-11, 1.4616209735810607e-12, 1.1369053097845204e-13], [0.051864612075464625, 0.06454768115598876, 0.0401661458158883, 0.013931381216624574, 0.004435659594590206, 0.0011040728148569534, 0.00022901080709485295, 4.071621963993971e-05, 6.334130002196904e-06, 8.758988866960301e-07, 1.0900928359606227e-07, 1.2333328850268457e-08, 1.2791120097147596e-09, 1.2245449607518e-10, 1.088569622836634e-11, 9.031803140159963e-13, 7.025285715364626e-14], [0.024036547846874846, 0.029914490139312327, 0.01861491770773072, 0.00772234814748882, 0.0020088368029502097, 0.0005116802763728223, 0.00010613458776434018, 1.8869848290685565e-05, 2.9355395282741527e-06, 4.059335384300169e-07, 5.052012838923421e-08, 5.7158559016960305e-09, 5.928018313968199e-10, 5.6751284472990885e-11, 5.044953539013404e-12, 4.1857705983828005e-13, 3.255854222714062e-14], [0.008911750949637127, 0.011091047167224073, 0.006901636275562546, 0.002863125099129396, 0.0008908197642518342, 0.00018538522149446818, 3.935028521249068e-05, 6.996153919244677e-06, 1.0883758077679133e-06, 1.5050325111738574e-07, 1.8730759717106557e-08, 2.1192013339199798e-09, 2.197862320975558e-10, 2.1041012899074022e-11, 1.870458677285614e-12, 1.5519094232140767e-13, 1.2071351570947232e-14], [0.00275342177165304, 0.003426748672987659, 0.0021323660960182117, 0.0008846062942580487, 0.0002752323923066659, 6.850764708916036e-05, 1.1880728514852239e-05, 2.1615687677928665e-06, 3.362703538041152e-07, 4.6500281557806354e-08, 5.787154723705886e-09, 6.547596678034443e-10, 6.790631829670235e-11, 6.500942782327401e-12, 5.779068192233607e-13, 4.794861545906579e-14, 3.729628713432304e-15], [0.0007291815198790186, 0.0009074969303058943, 0.0005647089620779611, 0.00023426798203690237, 7.288907794958868e-05, 1.814270183453179e-05, 3.7632253363159838e-06, 5.593935500300989e-07, 8.905360239449651e-08, 1.2314548512038202e-08, 1.5325971199368614e-09, 1.7339829830638786e-10, 1.7983453495847992e-11, 1.7216277533165975e-12, 1.530455584858505e-13, 1.2698107008700565e-14, 9.877078629374952e-16], [0.00016896883819478485, 0.00021028879339202348, 0.00013085660379369887, 5.428550734195739e-05, 1.6890146667834506e-05, 4.204098934383095e-06, 8.720295229752801e-07, 1.5503960725865392e-07, 2.0165451170277042e-08, 2.853576096275234e-09, 3.5513949231649493e-10, 4.0180542445239406e-11, 4.167197276787172e-12, 3.9894242153869696e-13, 3.5464324730166876e-14, 2.942455794668482e-15, 2.2887558931017894e-16], [3.4803671425563875e-05, 4.331462622271949e-05, 2.6953432898976148e-05, 1.1181558569524652e-05, 3.4789794451876525e-06, 8.659471149595e-07, 1.7961790656355235e-07, 3.1934572117719657e-08, 4.967989001605364e-09, 5.743721672027684e-10, 7.31505189529459e-11, 8.276262131559104e-12, 8.583462272470173e-13, 8.217290895345787e-14, 7.304830396095625e-15, 6.060778174010614e-16, 4.714307616000183e-17], [6.451875990127945e-06, 8.02962979194378e-06, 4.996605227248992e-06, 2.072828133124368e-06, 6.449303488156694e-07, 1.6052856411074e-07, 3.3297419820577225e-08, 5.9200047196741e-09, 9.209617159853427e-10, 1.2735282374082082e-10, 1.3251463643134696e-11, 1.5342466684532029e-12, 1.5911951779674094e-13, 1.5233146291754902e-14, 1.3541634521324808e-15, 1.1235420741752116e-16, 8.739344693217549e-18], [1.0873122415735103e-06, 1.3532056073989569e-06, 8.420605166948169e-07, 3.4932652259167126e-07, 1.0868787067552506e-07, 2.7053321103334526e-08, 5.611498460156872e-09, 9.976778245154954e-10, 1.5520647782809473e-10, 2.1462328858184087e-11, 2.671076683244681e-12, 2.5266724304923983e-13, 2.6815859424204386e-14, 2.5671892122614666e-15, 2.282124611272778e-16, 1.893466416655932e-17, 1.4728113935862391e-18], [1.6797087437992676e-07, 2.0904678564244375e-07, 1.3008373847180568e-07, 5.39648862583465e-08, 1.679039007731624e-08, 4.17926868369651e-09, 8.668791418830334e-10, 1.5412391227272058e-10, 2.3976707695745416e-11, 3.3155573962099907e-12, 4.126349992814927e-13, 4.6685593863060417e-14, 4.048152942107353e-15, 3.9658618766053935e-16, 3.525486532228314e-17, 2.9250770611619313e-18, 2.27523804219649e-19], [2.3952540439712007e-08, 2.9809939403940044e-08, 1.854985882402004e-08, 7.69535864595091e-09, 2.394299004575033e-09, 5.95961070776122e-10, 1.2361641730417515e-10, 2.1977972401863826e-11, 3.4190633513909237e-12, 4.727963875051222e-13, 5.884148989291461e-14, 6.657336154764696e-15, 6.904444640736588e-16, 5.5263790567895775e-17, 5.027321495145483e-18, 4.1711413871837263e-19, 3.2444750565753626e-20], [3.1716444648265935e-09, 3.947244324471304e-09, 2.4562554110116464e-09, 1.01897089854487e-09, 3.1703798618412977e-10, 7.891340946221333e-11, 1.6368506993707238e-11, 2.9101846082645064e-12, 4.52730823297208e-13, 6.260471824251556e-14, 7.791419293946778e-15, 8.815225015022783e-16, 9.142430500268527e-17, 8.752413481461977e-18, 6.505116238294787e-19, 5.523162574745851e-20, 4.296129414896804e-21], [3.919712285834015e-10, 4.878246047248765e-10, 3.035590722245414e-10, 1.2593065818781878e-10, 3.918149412090398e-11, 9.752601970883245e-12, 2.022920244545825e-12, 3.596584197744594e-13, 5.595124516426016e-14, 7.737074125670694e-15, 9.629112679323315e-16, 1.089439443070278e-16, 1.129877498934782e-17, 1.0816768094421793e-18, 9.615657686939494e-20, 6.670263734009096e-21, 5.309419588435675e-22], [4.541456502525498e-11, 5.652032755634597e-11, 3.5170956996947545e-11, 1.4590576164513e-11, 4.539645725966406e-12, 1.129955833678918e-12, 2.343795571905949e-13, 4.167073882120977e-14, 6.48262238771848e-15, 8.96432774556885e-16, 1.115648119100633e-16, 1.2622461757512743e-17, 1.309098510403246e-18, 1.2532522342585631e-19, 1.1140891969605108e-20, 9.243537663035e-22, 6.011370600080794e-23]] |
| Legacy trial inputs | {"lambda_home": 1.8537917770907781, "lambda_away": 1.2445418672382986, "rho": -0.10363221309641538, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5476 |
| Legacy p draw | 0.2251 |
| Legacy p away | 0.2273 |
| Legacy p over 1 5 | 0.8285 |
| Legacy p under 3 5 | 0.6215 |
| Legacy p btts yes | 0.6048 |
| Legacy p over 2 5 | 0.6082 |
| Legacy goal margin distribution | {"-1": 0.13008027711672357, "-10": 1.2639814389255092e-07, "-11": 1.4058526840887774e-08, "-12": 1.437044956703298e-09, "-13": 1.358678706793604e-10, "-14": 1.1942967216643772e-11, "-15": 9.7329152078781e-13, "-16": 6.616562019264133e-14, "-2": 0.06565253961711048, "-3": 0.023207080627016603, "-4": 0.006519660143240232, "-5": 0.0015123289025134005, "-6": 0.0002979544427190864, "-7": 5.0938827685462085e-05, "-8": 7.68424203373484e-06, "-9": 1.0365605654336658e-06, "0": 0.2250756200915639, "1": 0.2321830940483763, "10": 7.94318771961237e-06, "11": 1.3159681683884736e-06, "12": 2.0036753949879225e-07, "13": 2.8217934412572365e-08, "14": 3.6946400265484176e-09, "15": 4.4849155613974747e-10, "16": 4.541456502525498e-11, "2": 0.17025275096886613, "3": 0.08964262365797457, "4": 0.037512019505491885, "5": 0.01296113936915902, "6": 0.0038036297373097703, "7": 0.0009686095680259514, "8": 0.00021764679925314112, "9": 4.373180189746584e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5059 |
| Legacy raw p draw | 0.2487 |
| Legacy raw p away | 0.2455 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8538 |
| Legacy lambda away | 1.2445 |
| Legacy model home team | Ajax |
| Legacy model away team | AZ Alkmaar |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 77.9% |
| Market reference home draw last update utc | 2026-10-30T12:02:41Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.9% |
| Market reference draw away last update utc | 2026-10-30T12:02:41Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.2% |
| Market reference home away last update utc | 2026-10-30T12:02:41Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.16 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 88.9% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.94 |
| Market reference over 1 5 last update utc | 2026-10-30T12:02:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.6% |
| Market under 3 5 odds | 1.87 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market reference under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.2% |
| Market reference btts yes odds | 1.38 |
| Market reference btts yes opposite odds | 2.81 |
| Market reference btts yes last update utc | 2026-10-30T12:02:36Z |
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
| Market best home last update utc | 2026-10-30T12:02:36Z |
| Market best draw last update utc | 2026-10-30T12:02:36Z |
| Market best away last update utc | 2026-10-30T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Feyenoord |
| Matched away-team name | For Sittard |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7316 |
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
| Goal margin distribution | {"-1": 0.0422314226930881, "-10": 3.0440461257762474e-09, "-11": 2.569918232996388e-10, "-12": 1.995340446771711e-11, "-13": 1.4337552585626242e-12, "-14": 9.586312611497135e-14, "-15": 5.992421212709999e-15, "-16": 3.5166876341252987e-16, "-17": 1.9446359290634595e-17, "-18": 1.016152741120932e-18, "-19": 4.9920409231077447e-20, "-2": 0.015629597550975104, "-20": 2.064041509805681e-21, "-3": 0.004063404298843296, "-4": 0.0008492751871296631, "-5": 0.00014758407220399878, "-6": 2.1880031489054298e-05, "-7": 2.823294283449573e-06, "-8": 3.2213152894712664e-07, "-9": 3.2916776906450414e-08, "0": 0.11288443893156057, "1": 0.18486043391504664, "10": 0.0005483720800646866, "11": 0.00015182954130199346, "12": 3.866044500910151e-05, "13": 9.110406069889996e-06, "14": 1.997685727122005e-06, "15": 4.0953477064131885e-07, "16": 7.881976041243899e-08, "17": 1.4293957614540899e-08, "18": 2.449548517576442e-09, "19": 3.946554077211297e-10, "2": 0.2104112491398487, "20": 5.351446852543853e-11, "3": 0.17940067107626137, "4": 0.12296891230147577, "5": 0.07008083272931345, "6": 0.03407380041911019, "7": 0.01441921607024087, "8": 0.005395498836270233, "9": 0.001808125377646427} |
| Raw goal margin distribution | {"-1": 0.05659059048545416, "-10": 1.5390196069136006e-09, "-11": 1.1458580378743212e-10, "-12": 7.840328242133055e-12, "-13": 4.96191109908552e-13, "-14": 2.920659693206155e-14, "-15": 1.606652921471555e-15, "-16": 8.29476009595295e-17, "-17": 4.0331668395092904e-18, "-18": 1.842848543588335e-19, "-19": 7.214627955972602e-21, "-2": 0.01974017631191244, "-3": 0.004678629520605293, "-4": 0.000880760036937762, "-5": 0.00013685367280078325, "-6": 1.805669121166979e-05, "-7": 2.0670399771711938e-06, "-8": 2.0876908553946202e-07, "-9": 1.8853478640072603e-08, "0": 0.15237822146882815, "1": 0.19961899263839847, "10": 0.00022149954387664145, "11": 5.4084443749898114e-05, "12": 1.2136366007654474e-05, "13": 2.518930978235818e-06, "14": 4.862516791999507e-07, "15": 8.772332678740112e-08, "16": 1.4852847545894278e-08, "17": 2.3684539752485364e-09, "18": 3.549124825328986e-10, "19": 4.556783960913067e-11, "2": 0.21231308654251868, "3": 0.1650278576494745, "4": 0.10188472425706747, "5": 0.051918340097500786, "6": 0.02246546340095341, "7": 0.008434104050597331, "8": 0.0027936316074830387, "9": 0.0008273843623414728} |
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
| Totals anchor scale | 1.1395 |
| Totals anchor target over 2 5 | 0.7794 |
| Totals anchor reference over odds | 1.25 |
| Totals anchor reference under odds | 3.87 |
| Totals anchor reference last update utc | 2026-10-30T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7109 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:53:24Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 4.4, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:53:24Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:53:24Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:53:24Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.76, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:53:24Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:53:24Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:53:24Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:53:24Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.39, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.41 |
| Reference away odds | 14.00 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:36Z |
| Market reference home last update utc | 2026-10-30T12:02:36Z |
| Market reference draw last update utc | 2026-10-30T12:02:36Z |
| Market reference away last update utc | 2026-10-30T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.24 |
| Reference Under 2.5 odds | 3.89 |
| Market reference over 2 5 last update utc | 2026-10-30T12:01:56Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:01:56Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.0837 |
| Raw ev home | -0.1119 |
| Raw edge prob draw | 0.0564 |
| Raw ev draw | 0.2815 |
| Raw edge prob away | 0.0273 |
| Raw ev away | 0.1487 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.02826567231386846, 0.014313136577105975, 0.008582059587346891, 0.0024707051700670027, 0.0005334719459180797, 9.214934117741133e-05, 1.3264523005699772e-05, 1.6366064197277388e-06, 1.766871300573881e-07, 1.695559600326836e-08, 1.4644134644068552e-09, 1.1497983504693508e-10, 8.27543988749373e-12, 5.497919657910917e-13, 3.3917279209429084e-14, 1.9529017771187166e-15, 1.0541710154738374e-16, 5.355657588520098e-18, 2.569750450224938e-19, 1.168121461042497e-20], [0.0740685860341384, 0.058581890525644824, 0.023169495912208977, 0.006670309470064873, 0.001440245892542008, 0.0002487810486506801, 3.581102047008431e-05, 4.418443540951856e-06, 4.770127375531491e-07, 4.577602943540524e-08, 3.953563993820703e-09, 3.1041788873549376e-10, 2.2341696499953116e-11, 1.4843060193549718e-12, 9.15684928539466e-14, 5.272364900449953e-15, 2.8460080922534163e-16, 1.445898683660488e-17, 6.937707894695517e-19, 3.1536468770842785e-20], [0.1098123963219843, 0.09484228788047214, 0.030942452714403976, 0.009004115295802478, 0.001944158682434874, 0.00033582448543269516, 4.8340569297431084e-05, 5.964367208038602e-06, 6.439098074490315e-07, 6.179213253450866e-08, 5.3368357479444965e-09, 4.190268041681712e-10, 3.015860239951477e-11, 2.0036345528651778e-12, 1.2360644896911837e-13, 7.117058310149413e-15, 3.8417685281980464e-16, 1.951789270371207e-17, 9.365070998996691e-19, 4.257043876442228e-20], [0.09882234918073811, 0.08535045226171552, 0.036857551766737745, 0.008016558001695635, 0.0017495868828415631, 0.0003022151020688318, 4.350263520977393e-05, 5.3674521148477584e-06, 5.794671818840077e-07, 5.560796323980374e-08, 4.802724131956969e-09, 3.77090515684391e-10, 2.7140323287264732e-11, 1.8031103959635068e-12, 1.1123589021043754e-13, 6.4047816550967534e-15, 3.457283546130498e-16, 1.7564537999725543e-17, 8.427812773082843e-19, 3.830998052369021e-20], [0.06669914115819604, 0.057606421123508805, 0.024876630321133155, 0.007161779584808295, 0.001168271195825623, 0.0002039770145127922, 2.9361661918231156e-05, 3.6227073049369348e-06, 3.911054906247556e-07, 3.753203015714571e-08, 3.2415498870139263e-09, 2.5451341466341653e-10, 1.831808562560651e-11, 1.2169910533519504e-12, 7.507753463170764e-14, 4.322842345302079e-15, 2.3334584249310027e-16, 1.1855006576291166e-17, 5.6882666569544275e-19, 2.5856932362982192e-20], [0.03601432646054194, 0.031104695211065243, 0.013432183234542521, 0.0038670163292505336, 0.0008349619173728961, 0.00010896308060049855, 1.585388446365774e-05, 1.9560876090074908e-06, 2.111781437554469e-07, 2.0265490129781886e-08, 1.7502809457795692e-09, 1.3742499596112447e-10, 9.890884716012378e-12, 6.571166035110212e-13, 4.0538255742543526e-14, 2.334126838183931e-15, 1.2599552563690013e-16, 6.401133052340025e-18, 3.0713902581187733e-19, 1.3961499162034767e-20], [0.016205002641765755, 0.013995865468118101, 0.006043943791061192, 0.001740002271038258, 0.00037569937873545826, 6.489647768010571e-05, 7.0575275959839e-06, 8.801609799983653e-07, 9.502169591286342e-08, 9.118657861048656e-09, 7.875562349129485e-10, 6.183573709297574e-11, 4.450501472740002e-12, 2.9567611954401113e-13, 1.824058939767295e-14, 1.0502634727995902e-15, 5.669293379771034e-17, 2.8802531719457095e-18, 1.3820024456444986e-19, 6.28211473152674e-21], [0.006249943994784121, 0.005397924163790188, 0.002331027710196019, 0.0006710839229830156, 0.00014489970337431215, 2.5029267808574874e-05, 3.602861338134515e-06, 3.35839842522204e-07, 3.664795932918727e-08, 3.516883162503583e-09, 3.0374461947095604e-10, 2.38488016479078e-11, 1.716469016897266e-12, 1.1403633980178136e-13, 7.0350289159154885e-15, 4.050655238924212e-16, 2.186532572493828e-17, 1.1108557902400013e-18, 5.330105817860969e-20, 2.422885457584362e-21], [0.002109168119331548, 0.0018216370524819269, 0.00078665174211592, 0.0002264706398862082, 4.889929175569411e-05, 8.446625082738993e-06, 1.2158573387389205e-06, 1.5001518902701202e-07, 1.2235675658627915e-08, 1.186842290420025e-09, 1.0250467337647903e-10, 8.0482532582704e-12, 5.792566671447631e-13, 3.8483834824104586e-14, 2.374110667296795e-15, 1.3669743120053929e-16, 7.378889791064876e-18, 3.7488041811324934e-19, 1.7987504004960725e-20, 8.176509690636799e-22], [0.0006326940471526565, 0.0005464424142459053, 0.00023597449148659948, 6.793513726931749e-05, 1.4668480203282141e-05, 2.5337617041513866e-06, 3.6472469565431647e-07, 4.500054604938356e-08, 4.858234231907523e-09, 3.522237609304729e-10, 3.0748661548696126e-11, 2.414260807288549e-12, 1.7376151370623348e-13, 1.1544121581229743e-14, 7.121697282985458e-16, 4.100557475193172e-17, 2.2134696625709738e-18, 1.124541029993958e-19, 5.3957703052519265e-21, 2.452734308060492e-22], [0.00017081216915337512, 0.00014752630361358432, 6.370743479741536e-05, 1.8340852440333714e-05, 3.960136709017309e-06, 6.840546939734762e-07, 9.846689199762101e-08, 1.2149064651981647e-08, 1.3116063461350698e-09, 1.2586693390268965e-10, 8.212858921116083e-12, 6.517923271932337e-13, 4.691142773526731e-14, 3.1166350578676587e-15, 1.9226869075740382e-16, 1.1070518526734836e-17, 5.975835494587991e-19, 3.0359901993655437e-20, 1.4567281520053111e-21, 6.621792466709098e-23], [4.192288697426936e-05, 3.6207774790159535e-05, 1.563588590713653e-05, 4.501444409253144e-06, 9.719469314022657e-07, 1.6788937089089016e-07, 2.4166992342432224e-08, 2.981777391930357e-09, 3.219110492905327e-10, 3.089185782227407e-11, 2.6680544008456103e-12, 1.5826493546205822e-13, 1.1513597025873005e-14, 7.649240678731208e-16, 4.718901838940859e-17, 2.7170669352376708e-18, 1.4666652689802765e-19, 7.45131184820366e-21, 3.5752868177629043e-22, 1.62520421422462e-23], [9.431808962369534e-06, 8.146023316163476e-06, 3.517760809841938e-06, 1.0127347324353009e-06, 2.1866857080176606e-07, 3.7771742056485086e-08, 5.437088698322898e-09, 6.708401247810234e-10, 7.242353136719165e-11, 6.950048589239551e-12, 6.002587423292234e-13, 4.712989388311151e-14, 2.562700924350929e-15, 1.7209257757763477e-16, 1.0616582938188779e-17, 6.112855798042096e-19, 3.29970277029219e-20, 1.6763957576307262e-21, 8.043678449796339e-23, 3.6563836080307676e-24], [1.958739597091508e-06, 1.691715607457713e-06, 7.305467507691163e-07, 2.1031846909593683e-07, 4.5411732783996336e-08, 7.844201161446854e-09, 1.129140864577928e-09, 1.3931591712352545e-10, 1.504046988399543e-11, 1.4433429926080084e-12, 1.2465801330280724e-13, 9.787644101347365e-15, 7.044457871053606e-16, 3.535793829539812e-17, 2.2047861094095093e-18, 1.2694799853036236e-19, 6.852618093295332e-21, 3.481434753363137e-22, 1.6704612602680947e-23, 7.593350738739844e-25], [3.777232578363208e-07, 3.26230363408345e-07, 1.4087860331817137e-07, 4.055780433908974e-08, 8.75719655467924e-09, 1.5126754073000624e-09, 2.177434747108804e-10, 2.6865675336574348e-11, 2.900403551553062e-12, 2.783341992741938e-13, 2.403904580785376e-14, 1.887448858435805e-15, 1.3584529463212622e-16, 9.02509746849071e-18, 4.206361316884355e-19, 2.4480646458513778e-20, 1.321458572007776e-21, 6.71359724864682e-23, 3.2213167603021276e-24, 1.4643014228075834e-25], [6.79841273477682e-08, 5.871623234879609e-08, 2.5355888762106657e-08, 7.299754192868261e-09, 1.576154905559811e-09, 2.7225730847182157e-10, 3.919033262258021e-11, 4.835390608001478e-12, 5.220261138755384e-13, 5.009569110752376e-14, 4.326642634825904e-15, 3.3971051793136606e-16, 2.4449973937976343e-17, 1.6243727726444865e-18, 1.0020936699339127e-19, 4.359129482608208e-21, 2.378413454304851e-22, 1.2083398118720336e-23, 5.797853436781982e-25, 2.635507672307716e-26], [1.1471299114212419e-08, 9.907481207887369e-09, 4.2784249154059545e-09, 1.2317237430770234e-09, 2.659524373905695e-10, 4.593932647740593e-11, 6.6127792683044984e-12, 8.158994483329103e-13, 8.808405625423978e-14, 8.452894512978719e-15, 7.300558786391692e-16, 5.732104118216135e-17, 4.125565412386398e-18, 2.7408847733925032e-19, 1.6908823686839807e-20, 9.735825690238892e-22, 3.970411469242968e-23, 2.0388917169869804e-24, 9.78300576742991e-26, 4.447022857584128e-27], [1.8217498494070186e-09, 1.5734009041844133e-09, 6.794539892768857e-10, 1.9560927852378425e-10, 4.223574051568644e-11, 7.295595752392688e-12, 1.0501713464406224e-12, 1.2957248192492956e-13, 1.3988573972193715e-14, 1.3423988994405752e-15, 1.1593971822440157e-16, 9.103118757672233e-18, 6.55178467051047e-19, 4.352781993962154e-20, 2.685279731480972e-21, 1.5461403986119833e-22, 8.346023405614613e-24, 3.2034163408701204e-25, 1.5536330372104546e-26, 7.062289231980913e-28], [2.73238125153903e-10, 2.359891031772238e-10, 1.0190901578434957e-10, 2.9338776969814917e-11, 6.3347964907197965e-12, 1.0942418389184557e-12, 1.5751166379137457e-13, 1.9434140227446602e-14, 2.098099103443335e-15, 2.0134189038698007e-16, 1.7389407908456186e-17, 1.3653461276307017e-18, 9.826801195373085e-20, 6.528591132426989e-21, 4.0275606422169528e-22, 2.319003917464075e-23, 1.2517919453008423e-24, 6.359659801579109e-26, 2.3053883228176693e-27, 1.059248979583655e-28], [3.882511540425013e-11, 3.353230505384445e-11, 1.4480516934934775e-11, 4.16882307705422e-12, 9.001276987832591e-13, 1.5548366704770254e-13, 2.2381241712777173e-14, 2.7614474981776394e-15, 2.9812435499203853e-16, 2.8609192533367524e-17, 2.470906168299579e-18, 1.9400558008568529e-19, 1.3963157236937048e-20, 9.276644831348906e-22, 5.722865600970303e-23, 3.2951329419252082e-24, 1.778703711681567e-25, 9.036605912480309e-27, 4.335942268205832e-28, 1.489061379293832e-29]] |
| Legacy trial inputs | {"lambda_home": 2.6997593848415278, "lambda_away": 0.8636756054606272, "rho": -0.10363221309641538, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8016 |
| Legacy p draw | 0.1271 |
| Legacy p away | 0.0713 |
| Legacy p over 1 5 | 0.8834 |
| Legacy p under 3 5 | 0.5129 |
| Legacy p btts yes | 0.5349 |
| Legacy p over 2 5 | 0.7064 |
| Legacy goal margin distribution | {"-1": 0.048457083594129195, "-10": 1.8068705354213195e-09, "-11": 1.3944085376220662e-10, "-12": 9.889997025071593e-12, "-13": 6.488354137375176e-13, "-14": 3.959196828886342e-14, "-15": 2.2578891172574417e-15, "-16": 1.2085090546441197e-16, "-17": 6.091998816754072e-18, "-18": 2.885115137933366e-19, "-19": 1.168121461042497e-20, "-2": 0.017530159234988407, "-3": 0.004294121499327832, "-4": 0.0008363731989578256, "-5": 0.00013454354193993446, "-6": 1.8385867859176973e-05, "-7": 2.1804787210968234e-06, "-8": 2.2819607961179907e-07, "-9": 2.1356585726362735e-08, "0": 0.12709121379575067, "1": 0.2138338215245538, "10": 0.0002107570594208141, "11": 5.084163800967668e-05, "12": 1.1271976335644541e-05, "13": 2.311600925368633e-06, "14": 4.409200146592044e-07, "15": 7.860130144960106e-08, "16": 1.3150777857258235e-08, "17": 2.0722194695191773e-09, "18": 3.0677043020774746e-10, "19": 3.882511540425013e-11, "2": 0.22430848608162074, "3": 0.1717546793410327, "4": 0.10457039865932596, "5": 0.05258306766679518, "6": 0.022461647290376942, "7": 0.00832690726640358, "8": 0.002724046148224394, "9": 0.0007969159358344284} |
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
| Market reference home draw last update utc | 2026-10-30T12:00:49Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 17.4% |
| Market reference draw away last update utc | 2026-10-30T12:00:49Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 89.6% |
| Market reference home away last update utc | 2026-10-30T12:00:49Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.03 |
| Market reference dc draw away odds | 5.50 |
| Market reference dc home away odds | 1.07 |
| Market p over 1 5 | 91.5% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.60 |
| Market reference over 1 5 last update utc | 2026-10-30T12:02:15Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 42.9% |
| Market under 3 5 odds | 2.19 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference under 3 5 odds | 2.19 |
| Market reference under 3 5 opposite odds | 1.68 |
| Market reference under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.1% |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-30T12:02:36Z |
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
| Market best home last update utc | 2026-10-30T12:02:36Z |
| Market best draw last update utc | 2026-10-30T12:02:36Z |
| Market best away last update utc | 2026-10-30T12:02:36Z |
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
| Goal margin distribution | {"-1": 0.14764740820673128, "-10": 3.446452933480858e-06, "-11": 5.606943902846441e-07, "-12": 8.392407546256554e-08, "-13": 1.1628405109678447e-08, "-14": 1.4979300564450849e-09, "-15": 1.7766738843788138e-10, "-16": 1.684100424439461e-11, "-2": 0.09777829100857854, "-3": 0.04811777515450923, "-4": 0.019156641345810733, "-5": 0.006366029522073548, "-6": 0.0018094567906787949, "-7": 0.00044842227983743753, "-8": 9.83859920261349e-05, "-9": 1.9349956621140135e-05, "0": 0.24300690826560034, "1": 0.20085441027804343, "10": 4.500960862007418e-06, "11": 7.289196193671265e-07, "12": 1.0860768041055126e-07, "13": 1.4980098536383495e-08, "14": 1.9209081358661667e-09, "15": 2.268001427293833e-10, "16": 2.140051054375477e-11, "2": 0.13243750013493602, "3": 0.06487757593978177, "4": 0.02571159322767307, "5": 0.008505479705525397, "6": 0.002406572364028526, "7": 0.0005936882242614309, "8": 0.00012966568703476998, "9": 2.538588663668296e-05} |
| Raw goal margin distribution | {"-1": 0.182825862489229, "-10": 1.743950982308886e-06, "-11": 2.5254277072460206e-07, "-12": 3.3620148009884153e-08, "-13": 4.138097463755298e-09, "-14": 4.685153218287688e-10, "-15": 4.317058020872091e-11, "-2": 0.11450641194219713, "-3": 0.05186794249647719, "-4": 0.018781878515931903, "-5": 0.005635305160216146, "-6": 0.0014392915972255157, "-7": 0.00031946789131552923, "-8": 6.263468635668142e-05, "-9": 1.0989424699828498e-05, "0": 0.2522337888994178, "1": 0.181949823435606, "10": 1.6662482813858516e-06, "11": 2.4019332023805047e-07, "12": 3.1830697086924965e-08, "13": 3.900028565517991e-09, "14": 4.395531684239165e-10, "15": 4.031772760885235e-11, "2": 0.11346734535636896, "3": 0.051163547918814146, "4": 0.01844255992826976, "5": 0.005508332642695994, "6": 0.0014004643380285272, "7": 0.0003094361318892555, "8": 6.0391978738543904e-05, "9": 1.0547750639469762e-05} |
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
| Totals anchor scale | 1.1293 |
| Totals anchor target over 2 5 | 0.7046 |
| Totals anchor reference over odds | 1.38 |
| Totals anchor reference under odds | 3.07 |
| Totals anchor reference last update utc | 2026-10-30T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6318 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.8, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.56, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.82, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.6, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.89, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.35, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:55:14Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.89, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.09 |
| Reference draw odds | 3.93 |
| Reference away odds | 3.18 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:36Z |
| Market reference home last update utc | 2026-10-30T12:02:36Z |
| Market reference draw last update utc | 2026-10-30T12:02:36Z |
| Market reference away last update utc | 2026-10-30T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.14 |
| Market reference over 2 5 last update utc | 2026-10-30T12:01:56Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:01:56Z |
| Home probability edge | -2.7% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0903 |
| Raw ev home | -0.2219 |
| Raw edge prob draw | 0.0132 |
| Raw ev draw | -0.0087 |
| Raw edge prob away | 0.0772 |
| Raw ev away | 0.1939 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.04739201537783506, 0.046426341301477256, 0.04537733414616653, 0.024529626111098043, 0.009944985230050609, 0.003225576477292585, 0.0008718249591952287, 0.00020197818409734087, 4.09437561042096e-05, 7.377655590381684e-06, 1.1964418136084156e-06, 1.7638924548640652e-07, 2.3837684183160452e-08, 2.9736778268598984e-09, 3.444602274945829e-10, 3.724097393367781e-11], [0.05800666884665025, 0.10927268016092655, 0.07461292228593153, 0.04033350837303282, 0.01635231386035905, 0.005303742310033703, 0.0014335220248469448, 0.0003321081512846342, 6.732289037644154e-05, 1.2130911909553428e-05, 1.9672821627390647e-06, 2.9003283937214677e-07, 3.919576394033245e-08, 4.8895510671518665e-09, 5.663881465989304e-10, 6.12344895584979e-11], [0.05732337169702336, 0.09296188735721082, 0.0660047989609002, 0.033159736930142035, 0.013443869568538819, 0.004360411648781077, 0.0011785538909199252, 0.00027303895379250903, 5.534875155448149e-05, 9.973291783178232e-06, 1.6173787407842857e-06, 2.384472128170427e-07, 3.222435323544459e-08, 4.019889011233554e-09, 4.6564959754724706e-10, 5.034324180360504e-11], [0.031418507044512343, 0.050951708288215644, 0.041314448420630194, 0.01955605635605427, 0.007368483364466423, 0.002389908689047261, 0.0006459564856009314, 0.0001496505882190053, 3.0336232659352456e-05, 5.466285894746724e-06, 8.864730712205174e-07, 1.3069111627335787e-07, 1.766192460701406e-08, 2.2032708034889984e-09, 2.5521902720827246e-10, 2.7592750573188756e-11], [0.012915184797442716, 0.020944684843089513, 0.016983102838110564, 0.009180556122651238, 0.0032591892142659544, 0.000982418175514505, 0.00026553290297413504, 6.151676778136534e-05, 1.2470294985648808e-05, 2.2470225076668414e-06, 3.644018958809596e-07, 5.37231102567397e-08, 7.260275603004162e-09, 9.056970640124884e-10, 1.049127157935445e-10, 1.1342533628908386e-11], [0.004247229140857083, 0.006887774136166556, 0.005584986231902635, 0.003019076080205904, 0.0012240164970334633, 0.0003476304757069987, 8.732194707670227e-05, 2.0230125458529027e-05, 4.100924693591592e-06, 7.389456383631505e-07, 1.198355560096696e-07, 1.766713856584404e-08, 2.38758133122793e-09, 2.978434318511813e-10, 3.450112025133611e-11, 3.730054204829491e-12], [0.0011639371056797554, 0.0018875684891839334, 0.0015305443842171028, 0.0008273663977340107, 0.00033543709830873524, 0.0001087963419640424, 2.5749192789887787e-05, 5.543989479453176e-06, 1.1238429244498944e-06, 2.0250526144146795e-07, 3.284048154540399e-08, 4.8416126010620745e-09, 6.54307646722272e-10, 8.162286764321644e-11, 9.45490170562018e-12, 1.0222072676591507e-12], [0.0002734050582926868, 0.0004433837277791565, 0.0003595199212607246, 0.00019434568852392582, 7.879308853468456e-05, 2.5555908537977515e-05, 6.907378905807367e-06, 1.4012506138216208e-06, 2.6398706491241236e-07, 4.756783037400103e-08, 7.714122805662566e-09, 1.1372791269945053e-09, 1.53694748127287e-10, 1.917294738445247e-11, 2.2209258037761606e-12, 2.4011317814147686e-13], [5.6194217748841064e-05, 9.113072706373278e-05, 7.389380747573297e-05, 3.994477647070677e-05, 1.6194711253227065e-05, 5.252625163998249e-06, 1.4197058266974769e-06, 3.2890731310728434e-07, 5.838269234733922e-08, 9.776838199588092e-09, 1.585519665911383e-09, 2.3375028722082187e-10, 3.158959895274574e-11, 3.940705365646902e-12, 4.564772466199677e-13, 4.935158223153231e-14], [1.0266542098130531e-05, 1.6649354387575783e-05, 1.3500212577590531e-05, 7.297810089106235e-06, 2.958732971271815e-06, 9.596413925167588e-07, 2.593766800330885e-07, 6.00905379890011e-08, 1.2181178589102852e-08, 1.9219734183252054e-09, 2.896704509749809e-10, 4.2705588943840466e-11, 5.771340193059507e-12, 7.199569484811838e-13, 8.339724364895644e-14, 9.016409817357526e-15], [1.6881042532062706e-06, 2.7376156145040354e-06, 2.2198093626450166e-06, 1.1999623761105662e-06, 4.864977579758885e-07, 1.577916596236736e-07, 4.264871975015903e-08, 9.880550996343466e-09, 2.00292359284964e-09, 3.609068109013878e-10, 5.125021054193983e-11, 7.021983219150601e-12, 9.489683900851212e-13, 1.1838088961596949e-13, 1.3712819795003684e-14, 1.482547835079115e-15], [2.523374155542338e-07, 4.0921812004963546e-07, 3.3181656673694217e-07, 1.7937008580776256e-07, 7.272156721801974e-08, 2.3586659123585484e-08, 6.375120314999252e-09, 1.4769423736322227e-09, 2.993965343149467e-10, 5.3948262819552776e-11, 8.748843940749732e-12, 1.1294280266424657e-12, 1.4185156547169817e-13, 1.7695546753091857e-14, 2.049788986942003e-15, 2.2161089187995575e-16], [3.45760578690647e-08, 5.6072340159420564e-08, 4.546653847671297e-08, 2.4577847297224732e-08, 9.964535425460576e-09, 3.2319174269252014e-09, 8.735388228080224e-10, 2.0237523978684773e-10, 4.102424475392993e-11, 7.392158840524637e-12, 1.1987938202440836e-12, 1.7673599755669171e-13, 2.0914348735660882e-14, 2.4246988787445325e-15, 2.808684652500359e-16, 3.0365813984527943e-17], [4.373279112343489e-09, 7.09219064035672e-09, 5.7507383804060325e-09, 3.1086767212837367e-09, 1.260343061820317e-09, 4.0878219921758913e-10, 1.1048769938071552e-10, 2.559700161212355e-11, 5.1888643107156464e-12, 9.349814827015196e-13, 1.5162688568873924e-13, 2.2354076611070223e-14, 3.020985871283924e-15, 3.2999390439457455e-16, 3.5525050225373825e-17, 3.840755372712942e-18], [5.136345532786185e-10, 8.329663114903215e-10, 6.754149147958753e-10, 3.6510904929838416e-10, 1.480252526550928e-10, 4.801080765477712e-11, 1.297660145999362e-11, 3.006326408759642e-12, 6.094237147442483e-13, 1.0981206180865783e-13, 1.7808332305145303e-14, 2.625450116292796e-15, 3.5480990089984073e-16, 4.4261444482159755e-17, 4.489501524023349e-18, 4.51090501986904e-19], [5.6303843799638804e-11, 9.130850873086046e-11, 7.40379626329091e-11, 4.0022702425901206e-11, 1.622630457918875e-11, 5.262872206774494e-12, 1.422475448721063e-12, 3.295489593701722e-13, 6.680410697397715e-14, 1.2037432326008452e-14, 1.95212248483031e-15, 2.8779787556719794e-16, 3.889372533703636e-17, 4.851872679831347e-18, 5.620236166721091e-19, 5.3206400865731495e-20]] |
| Legacy trial inputs | {"lambda_home": 1.6442773399951887, "lambda_away": 1.6217100391189667, "rho": -0.10363221309641538, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4205 |
| Legacy p draw | 0.2459 |
| Legacy p away | 0.3336 |
| Legacy p over 1 5 | 0.8482 |
| Legacy p under 3 5 | 0.5873 |
| Legacy p btts yes | 0.6566 |
| Legacy p over 2 5 | 0.6362 |
| Legacy goal margin distribution | {"-1": 0.16264304205482777, "-10": 1.5210109197894942e-06, "-11": 2.1987145999880973e-07, "-12": 2.9220477598432757e-08, "-13": 3.5904092152624335e-09, "-14": 4.0569471705308077e-10, "-15": 3.724097393367781e-11, "-2": 0.10183155684516511, "-3": 0.04595413625734039, "-4": 0.016590175269931413, "-5": 0.004964845545988002, "-6": 0.0012651308909096257, "-7": 0.0002802170339129141, "-8": 5.483030568487041e-05, "-9": 9.601988110936336e-06, "0": 0.2458595813461594, "1": 0.202803622423373, "10": 2.1460508765787642e-06, "11": 3.1454182944793794e-07, "12": 4.2383686126643195e-08, "13": 5.280283386466719e-09, "14": 6.049430620094789e-10, "15": 5.6303843799638804e-11, "2": 0.1286397337648602, "3": 0.0588598597951112, "4": 0.02154504752663549, "5": 0.006537385435199527, "6": 0.001689023435198136, "7": 0.00037931202735559547, "8": 7.525313820864473e-05, "9": 1.336186190301366e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3784 |
| Legacy raw p draw | 0.2527 |
| Legacy raw p away | 0.3689 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6443 |
| Legacy lambda away | 1.6217 |
| Legacy model home team | Heerenveen |
| Legacy model away team | Nijmegen |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Market p home draw | 68.6% |
| Market reference home draw last update utc | 2026-10-30T12:02:41Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.3% |
| Market reference draw away last update utc | 2026-10-30T12:02:41Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.1% |
| Market reference home away last update utc | 2026-10-30T12:02:41Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 88.9% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.96 |
| Market reference over 1 5 last update utc | 2026-10-30T12:02:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 50.4% |
| Market under 3 5 odds | 1.91 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference under 3 5 odds | 1.91 |
| Market reference under 3 5 opposite odds | 1.94 |
| Market reference under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 72.1% |
| Market reference btts yes odds | 1.33 |
| Market reference btts yes opposite odds | 3.04 |
| Market reference btts yes last update utc | 2026-10-30T12:02:36Z |
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
| Willem II win | 2.6% | 37.89 |

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
| 3 | 5-0 | 8.52% |
| 4 | 4-1 | 6.51% |
| 5 | 6-0 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 92.8% | 92.5% | 1.07 | -0.7% |
| Draw | 4.5% | 4.5% | 14.59 | -34.1% |
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
| Market best home last update utc | 2026-10-30T12:02:36Z |
| Market best draw last update utc | 2026-10-30T12:02:36Z |
| Market best away last update utc | 2026-10-30T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | PSV Eindhoven |
| Matched away-team name | Willem II |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.4599 |
| Dc lambda away | 0.6807 |
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
| Fair Under 0.5 odds | 135.05 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 28.36 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.76 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.01 |
| Fair Over 4.5 odds | 1.72 |
| Fair Under 4.5 odds | 2.39 |
| Goal margin distribution | {"-1": 0.019793057309746877, "-10": 7.282051680272287e-11, "-11": 4.40669852964033e-12, "-12": 2.4526734370206235e-13, "-13": 1.263444231910751e-14, "-14": 6.056405876004499e-16, "-15": 2.7143618811615467e-17, "-16": 1.1421360933589676e-18, "-17": 4.52858511165607e-20, "-18": 1.6975624567160364e-21, "-19": 6.033712845622717e-23, "-2": 0.005421723433296465, "-20": 2.038875056969076e-24, "-21": 6.565730214380147e-26, "-22": 2.0187955780749617e-27, "-23": 5.902040923919806e-29, "-24": 1.485961079536061e-30, "-3": 0.0010065307586506233, "-4": 0.00015042403721501278, "-5": 1.8706868586966627e-05, "-6": 1.985807090617676e-06, "-7": 1.8354070530542854e-07, "-8": 1.5004081684166027e-08, "-9": 1.0986915175822367e-09, "0": 0.045136520180807924, "1": 0.08915005094565141, "10": 0.006534792413778773, "11": 0.0025910165728560927, "12": 0.000944877241494992, "13": 0.0003189117706544606, "14": 0.00010016321472687748, "15": 2.941303509151384e-05, "16": 8.10902725881809e-06, "17": 2.1066493290973906e-06, "18": 5.174093679171938e-07, "19": 1.204958179352329e-07, "2": 0.14324679478993357, "20": 2.6678214505772936e-08, "21": 5.628957785956827e-09, "22": 1.134007987778843e-09, "23": 2.1722249425800826e-10, "24": 3.583346661929316e-11, "3": 0.17424222772238745, "4": 0.1706170447122105, "5": 0.1390224957956138, "6": 0.09669407281224159, "7": 0.05855635072484595, "8": 0.03136388391050296, "9": 0.015047868945641156} |
| Raw goal margin distribution | {"-1": 0.012300798668943229, "-10": 4.525579359170496e-11, "-11": 2.7386325699739548e-12, "-12": 1.5242638707764914e-13, "-13": 7.851931555070367e-15, "-14": 3.7638768065128604e-16, "-15": 1.6868954852356353e-17, "-16": 7.098037416394302e-19, "-17": 2.814381469315692e-20, "-18": 1.0549847697221497e-21, "-19": 3.7497737605030327e-23, "-2": 0.0033694404733941707, "-20": 1.2671004380185613e-24, "-21": 4.0804067920278513e-26, "-22": 1.2546216368213276e-27, "-23": 3.667943562475829e-29, "-24": 9.23480783348087e-31, "-3": 0.0006255290439725576, "-4": 9.348408221100428e-05, "-5": 1.1625764560452222e-05, "-6": 1.2341202692834684e-06, "-7": 1.1406511021448608e-07, "-8": 9.324592210341316e-09, "-9": 6.828042250147775e-10, "0": 0.04603841039965343, "1": 0.09002271201518522, "10": 0.006598759387173614, "11": 0.0026163791976629674, "12": 0.0009541263397893251, "13": 0.00032203349502718016, "14": 0.00010114368010142657, "15": 2.9700949796989925e-05, "16": 8.18840390892088e-06, "17": 2.1272706393172073e-06, "18": 5.224741211910722e-07, "19": 1.2167531259887376e-07, "2": 0.1446489914215976, "20": 2.693935893538243e-08, "21": 5.684057836598954e-09, "22": 1.1451084258938837e-09, "23": 2.1934881513113433e-10, "24": 3.61842288563687e-11, "3": 0.17594782864116726, "4": 0.17228715988477525, "5": 0.14038334212809894, "6": 0.0976405798764871, "7": 0.059129539939092056, "8": 0.031670894845300494, "9": 0.01519516767703855} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 2.88, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.07 |
| Reference draw odds | 14.59 |
| Reference away odds | 20.21 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:36Z |
| Market reference home last update utc | 2026-10-30T12:02:36Z |
| Market reference draw last update utc | 2026-10-30T12:02:36Z |
| Market reference away last update utc | 2026-10-30T12:02:36Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.10 |
| Reference Under 2.5 odds | 6.50 |
| Market reference over 2 5 last update utc | 2026-10-30T12:00:49Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:00:49Z |
| Home probability edge | +0.4% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Raw edge prob home | 0.0130 |
| Raw ev home | 0.0032 |
| Raw edge prob draw | 0.0013 |
| Raw ev draw | -0.3283 |
| Raw edge prob away | -0.0143 |
| Raw ev away | -0.6685 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.006548456735861319, 0.0026292665959829977, 0.0017639380097091055, 0.00040633338315144865, 7.020094414649957e-05, 9.702717548507441e-06, 1.1175387189196437e-06, 1.1032780532501496e-07, 9.530494441974614e-09, 7.318016144177042e-10, 5.057242785381232e-11, 3.177178087414905e-12, 1.8297036432516875e-13, 9.726527987615034e-15, 4.801204952179648e-16, 2.211970988418548e-17, 9.553882246106923e-19, 3.883751223539208e-20, 1.491074483431453e-21, 5.42333182657486e-23, 1.8739440589030515e-24, 6.166770237142005e-26, 1.9371155488328916e-27, 5.820337002232906e-29, 1.675935614078705e-30], [0.019981727691334356, 0.01750521534409718, 0.008254554234732302, 0.0019014845930776356, 0.00032851352915868996, 4.540500164268901e-05, 5.229653147650429e-06, 5.162918694657017e-07, 4.459906347166238e-08, 3.4245512495486043e-09, 2.3665959132556093e-10, 1.4867976477412826e-11, 8.56231220914564e-13, 4.551642537747139e-14, 2.246780014472729e-15, 1.0351176962599961e-16, 4.4708509436644605e-18, 1.8174468111948657e-19, 6.977657448143621e-21, 2.5379115620278868e-22, 8.76934040874859e-24, 2.8858122618501955e-25, 9.06495878470314e-27, 2.7236947775321093e-28, 7.842736731215096e-30], [0.0503600436157161, 0.03480218712686455, 0.012823714632738096, 0.0044491097798430215, 0.0007686587420753282, 0.00010623900798234242, 1.2236386794351681e-05, 1.2080240955176142e-06, 1.0435326701356617e-07, 8.012794061759853e-09, 5.537381192008511e-10, 3.478821747646555e-11, 2.0034170735047235e-12, 1.0649971818211565e-13, 5.257034935722106e-15, 2.4219771658864525e-16, 1.0460934961078493e-17, 4.252477464960162e-19, 1.6326382083739962e-20, 5.938227000156362e-22, 2.051857707255321e-23, 6.752248008598194e-25, 2.121026745613498e-26, 6.372924143661838e-28, 1.835050192813133e-29], [0.07855523814731767, 0.0542869684279856, 0.018757978529543397, 0.004607889783344666, 0.001199009496467181, 0.00016571928801871076, 1.9087201076073196e-05, 1.8843633503420829e-06, 1.6277777287593707e-07, 1.2498935675078005e-08, 8.637607655187912e-10, 5.4265177556986717e-11, 3.1250748414453677e-12, 1.661259626432782e-13, 8.20030328956153e-15, 3.7779751444496516e-16, 1.6317722903136472e-17, 6.633321895531428e-19, 2.5467071523187683e-20, 9.26287593652001e-22, 3.2006360452704104e-23, 1.053264477673428e-24, 3.308530913712341e-26, 9.940947978923379e-28, 2.862444004391815e-29], [0.09190210627303741, 0.06351055460303658, 0.021945038637099665, 0.005055167326584499, 0.0009313498456368648, 0.0001938756978933262, 2.233019749056683e-05, 2.20452467543144e-06, 1.9043440685239044e-07, 1.4622557856125598e-08, 1.0105173829187689e-09, 6.348506137063664e-11, 3.6560383109158e-12, 1.9435146826137546e-13, 9.5935695971683e-15, 4.419869144448152e-16, 1.909017323027785e-17, 7.760351418490495e-19, 2.979403498462893e-20, 1.0836677843374225e-21, 3.744437683737062e-23, 1.2322185794820079e-24, 3.8706643479255186e-26, 1.162995720158667e-27, 3.348785380790268e-29], [0.08601333111950156, 0.05944101375026757, 0.020538875018981904, 0.004731249356072318, 0.000817403111732516, 0.00012047684482080751, 2.089935419993185e-05, 2.0632662140043587e-06, 1.7823201618988502e-07, 1.3685593961865477e-08, 9.457668576253787e-10, 5.941715403770334e-11, 3.421771780595672e-12, 1.8189808559405588e-13, 8.97884620759027e-15, 4.1366589259317327e-16, 1.7866939701100976e-17, 7.263094429840597e-19, 2.788493431157357e-20, 1.014230029514542e-21, 3.504506821538495e-23, 1.153262193727139e-24, 3.622645309362655e-26, 1.0884749003616546e-27, 3.134206575748153e-29], [0.06708490724805398, 0.04636019605643322, 0.016019011328761087, 0.00369007245840249, 0.0006375222447629849, 8.811417491646524e-05, 1.0822605584230519e-05, 1.6092159295891248e-06, 1.39009594432754e-07, 1.0673889612422132e-08, 7.376377719162293e-10, 4.6341587003818896e-11, 2.6687635455758334e-12, 1.418688945289454e-13, 7.002926839257904e-15, 3.2263298810903324e-16, 1.3935072355117477e-17, 5.664749984892079e-19, 2.1748468610185726e-20, 7.9103467535333805e-22, 2.733291595769611e-23, 8.994708877323237e-25, 2.825432074401908e-26, 8.489409348784159e-28, 2.44448104373712e-29], [0.04484738143234474, 0.03099256570681861, 0.010708976738591823, 0.002466875096704664, 0.0004261942731286941, 5.890579825150898e-05, 6.78464667097898e-06, 7.142767245011973e-07, 9.293023662132452e-08, 7.135673558360982e-09, 4.931231758838227e-10, 3.098012524420303e-11, 1.7841130231964073e-12, 9.484172651232613e-14, 4.681573605546186e-15, 2.156855434990959e-16, 9.315828713699309e-18, 3.786980018500268e-19, 1.4539214666033088e-20, 5.2881989805257195e-22, 1.8272511029648606e-23, 6.013113179133362e-25, 1.8888485525268302e-26, 5.675312001139881e-28, 1.6341764231297342e-29], [0.026233570871069468, 0.01812916703225219, 0.006264238652423701, 0.0014430038190101455, 0.0002493032438433938, 3.445707160136167e-05, 3.968693457538777e-06, 3.918049833667397e-07, 3.609252545008389e-08, 4.174027379691591e-09, 2.884534474377397e-10, 1.8121889957264273e-11, 1.0436206962635575e-12, 5.5477869042344544e-14, 2.738496408190471e-15, 1.2616571604708835e-16, 5.449313760988464e-18, 2.215201992395493e-19, 8.504744450385857e-21, 3.0933432076791307e-22, 1.0688544075016318e-23, 3.5173833053893318e-25, 1.1048859662448951e-26, 3.319785789989436e-28, 9.559149641028063e-30], [0.013640340365579574, 0.00942639528868236, 0.0032571374964629586, 0.0007503005723798037, 0.00012962707657984728, 1.7916210757340883e-05, 2.0635516923537617e-06, 2.037219163307408e-07, 1.7598198256358542e-08, 1.4409967439194421e-09, 1.4998351623623947e-10, 9.422611519397238e-12, 5.426383460932831e-13, 2.884613079225e-14, 1.4239015832506964e-15, 6.560080279605458e-17, 2.8334112357037633e-18, 1.151810758180353e-19, 4.422105156620935e-21, 1.6084068168862634e-22, 5.557588020032204e-24, 1.828889620765603e-25, 5.7449367906498165e-27, 1.7261473224069827e-28, 4.9703509808085446e-30], [0.006383156817764408, 0.004411191930791566, 0.001524215588447322, 0.00035111192870554056, 6.066050666341741e-05, 8.384100380134853e-06, 9.656631506861614e-07, 9.533405357215554e-08, 8.235282710679763e-09, 6.323484284633836e-10, 4.6600840145562294e-11, 4.409421271697889e-12, 2.539339610019012e-13, 1.349888430183984e-14, 6.663314004896555e-16, 3.069866296556026e-17, 1.3259279286279219e-18, 5.390033163986168e-20, 2.069375831015542e-21, 7.526727826274497e-23, 2.6007383180784026e-24, 8.558502895710178e-26, 2.6884103666062603e-27, 8.077708293329488e-29, 2.3259338769793243e-30], [0.0027155208120085207, 0.0018766080539478075, 0.0006484313750364894, 0.0001493699398220765, 2.580617600574375e-05, 3.56676167016034e-06, 4.1081215109429174e-07, 4.05569867636422e-08, 3.5034516982863544e-09, 2.690134939430492e-10, 1.8590647036167156e-11, 1.245486782774057e-12, 1.080285156174387e-13, 5.742691634729335e-15, 2.8347052052501006e-16, 1.3059816727643937e-17, 5.640758935127514e-19, 2.293026421266405e-20, 8.803532949952248e-22, 3.202018474885356e-23, 1.1064053776143021e-24, 3.640955940210767e-26, 1.1437027963062966e-27, 3.436416433139187e-29, 9.894981481130421e-31], [0.001058966438299291, 0.0007318172404294716, 0.0002528675385831469, 5.8249508699352774e-05, 1.0063584918988033e-05, 1.3909232016964098e-06, 1.6020362596028868e-07, 1.5815930274339915e-08, 1.3662343334956043e-09, 1.0490667583011876e-10, 7.249758937773677e-12, 4.554611319574708e-13, 2.7970960374967986e-14, 2.239466433027425e-15, 1.1054445473433334e-16, 5.092911659434267e-18, 2.1997159338354367e-19, 8.942071117689653e-21, 3.4330968450821554e-22, 1.2486849980022299e-23, 4.314627812337766e-25, 1.4198565987633993e-26, 4.460075840043381e-28, 1.340092719828192e-29, 3.8587269336226494e-31], [0.0003811967161234072, 0.00026343264409987426, 9.102486333458439e-05, 2.096810685299504e-05, 3.622594054735352e-06, 5.006913700853988e-07, 5.766858506413305e-08, 5.693268894052722e-09, 4.918041049723841e-10, 3.776331230108528e-11, 2.6096996088034537e-12, 1.6395258767867407e-13, 9.441858112533208e-15, 5.352435227332409e-16, 3.979274659360913e-17, 1.8332981385140606e-18, 7.918329231746756e-20, 3.2188821308441494e-21, 1.2358137105654701e-22, 4.494898076991604e-24, 1.5531388851183177e-25, 5.1110654052833005e-27, 1.6054958895735777e-28, 4.823938942954637e-30, 1.3890280015637048e-31], [0.00012741818711569812, 8.805456216845875e-05, 3.0425821047189083e-05, 7.008764896054199e-06, 1.2108823281705636e-06, 1.6736027353421153e-07, 1.9276206356458843e-08, 1.9030226929015483e-09, 1.643896309205162e-10, 1.2622702634538164e-11, 8.723138972756335e-13, 5.48025221921932e-14, 3.1560199571948914e-15, 1.6777097513220139e-16, 8.83132964730417e-18, 6.127952192967536e-19, 2.6467677002961907e-20, 1.075938244752608e-21, 4.1308105750312693e-23, 1.5024572353731765e-24, 5.191496482267853e-26, 1.7084163126949087e-27, 5.366504143885222e-29, 1.6124418938307694e-30, 4.642942143155586e-32], [3.975122066832157e-05, 2.7470774862245744e-05, 9.492079222281357e-06, 2.1865556738965056e-06, 3.7776436566918363e-07, 5.221213168202005e-08, 6.013684151917233e-09, 5.936944851810179e-10, 5.128536704396647e-11, 3.93796089250992e-12, 2.721396608096555e-13, 1.7096987503552948e-14, 9.845976354864068e-16, 5.234026009304275e-17, 2.5836178775927845e-18, 1.2693293580090503e-19, 8.257239354435736e-21, 3.3566525753353924e-22, 1.2887074162968844e-23, 4.687282911489278e-25, 1.6196143340044406e-26, 5.329822639654302e-28, 1.6742122554870475e-29, 5.030406960531655e-31, 1.4484793879169012e-32], [1.1626280412682435e-05, 8.034544004749481e-06, 2.7762059348679444e-06, 6.39515189100128e-07, 1.1048703338785996e-07, 1.5270798573559794e-08, 1.7588586485650237e-09, 1.7364142404005061e-10, 1.4999742103408284e-11, 1.1517592874068256e-12, 7.959433584153463e-14, 5.000459547820646e-15, 2.8797123739527146e-16, 1.5308273066426587e-17, 7.556463781262154e-19, 3.48135079124237e-20, 1.6034857565348052e-21, 9.817405209873699e-23, 3.769160679815592e-24, 1.3709180394044455e-25, 4.736984195944845e-27, 1.5588455276762349e-28, 4.8966700456959354e-30, 1.471273609458192e-31, 4.236455447853186e-33], [3.200384650255959e-06, 2.211681672201607e-06, 7.642106111778288e-07, 1.7604036047238e-07, 3.0413940929990114e-08, 4.203616945163241e-09, 4.841638100090091e-10, 4.779855021733022e-11, 4.129002800687664e-12, 3.1704660591065936e-13, 2.1910059075875397e-14, 1.3764844312213452e-15, 7.927029928417184e-17, 4.213932608254954e-18, 2.0800797707739806e-19, 9.583169542594832e-21, 4.1391353608976493e-22, 1.7943122029840376e-23, 1.0375428387974857e-24, 3.7737478319230547e-26, 1.3039571531983348e-27, 4.291058809705867e-29, 1.3479141303454702e-30, 4.0499982014026554e-32, 1.1661758107960842e-33], [8.320319056985481e-07, 5.749901707512817e-07, 1.986784966996038e-07, 4.5766747628907455e-08, 7.90697744090195e-09, 1.0928509538474245e-09, 1.2587228772011747e-10, 1.2426605915564653e-11, 1.073452864053713e-12, 8.242537086596919e-14, 5.6961491192661466e-15, 3.578566608803981e-16, 2.0608590962161e-17, 1.0955328067365937e-18, 5.407764768349511e-20, 2.491420153674266e-21, 1.0760871140900157e-22, 4.374404601527157e-24, 1.790951180217921e-25, 9.810941319099202e-27, 3.390011119563687e-28, 1.1155839778879619e-29, 3.504289906213765e-31, 1.0529133494373062e-32, 3.0318089488356146e-34], [2.0492582215752262e-07, 1.4161756618548662e-07, 4.893364545558435e-08, 1.1272149927298242e-08, 1.9474539879542547e-09, 2.6916441386318226e-10, 3.1001794367773746e-11, 3.060618729202014e-12, 2.643867491221597e-13, 2.030100862197852e-14, 1.4029366342838073e-15, 8.813853163947159e-17, 5.07580588857736e-18, 2.698249425093249e-19, 1.33190882897466e-20, 6.13625895635424e-22, 2.650355533936793e-23, 1.0773967359640964e-24, 4.1364101072993987e-26, 1.6043801961919e-27, 8.349449234359384e-29, 2.7476345833458704e-30, 8.630912891570576e-32, 2.5932795643565832e-33, 7.467212942309608e-35], [4.7948717692617194e-08, 3.3135798260327544e-08, 1.1449535870676531e-08, 2.6374672013633214e-09, 4.556669359901471e-10, 6.297931786899866e-11, 7.25382614281919e-12, 7.161261663668629e-13, 6.186143582033633e-14, 4.750047217292098e-15, 3.282603037024607e-16, 2.0622728394737325e-17, 1.1876413672594146e-18, 6.313386892190323e-20, 3.1164115756832157e-21, 1.435767075565799e-22, 6.201324359412165e-24, 2.520902021609546e-25, 9.678407455324517e-27, 3.5202275785865443e-28, 1.2971137056855352e-29, 6.428938704369462e-31, 2.0194683193676593e-32, 6.067777521652977e-34, 1.7471848181545406e-35], [1.0684839654526042e-08, 7.383944936880699e-09, 2.5514020141514534e-09, 5.877302980508639e-10, 1.015403201840694e-10, 1.4034242110405582e-11, 1.6164346607702079e-12, 1.5958076937724913e-13, 1.3785134500913259e-14, 1.0584953114608183e-15, 7.314916600046761e-17, 4.595546173918589e-18, 2.64652699527829e-19, 1.4068682097504084e-20, 6.944577370587545e-22, 3.199447601917919e-23, 1.3818963178701996e-24, 5.617550412576698e-26, 2.1567257008675862e-27, 7.844436521902877e-29, 2.710517387785566e-30, 9.51196417116517e-32, 4.5001610508472496e-33, 1.352136887034667e-34, 3.8934074834868695e-36], [2.2727707686963316e-09, 1.5706379087398808e-09, 5.427083704059187e-10, 1.250160306075682e-10, 2.1598627496544858e-11, 2.9852217029598274e-12, 3.438315936683153e-13, 3.3944403436419254e-14, 2.9322340577148056e-15, 2.251523916572036e-16, 1.555954900735971e-17, 9.77517992593567e-19, 5.629423920167424e-20, 2.992547427863766e-21, 1.4771800943344644e-22, 6.805540579670195e-24, 2.9394297510998075e-25, 1.194908373189684e-26, 4.587568262619277e-28, 1.6685890102546065e-29, 5.765537795780274e-31, 1.8973216789058132e-32, 6.355585873774569e-34, 2.8761285068294845e-35, 8.281661686279203e-37], [4.6242159329702874e-10, 3.195645131729739e-10, 1.1042031726001582e-10, 2.5435962507728775e-11, 4.3944914628193004e-12, 6.07378005402354e-13, 6.995652863889965e-14, 6.906382877138887e-15, 5.96597053941369e-16, 4.580986746168053e-17, 3.1657708476660824e-18, 1.988873817973792e-19, 1.1453716381619122e-20, 6.08868509164895e-22, 3.005494360527239e-23, 1.3846662239077553e-24, 5.980611012820862e-26, 2.431179780138054e-27, 9.333940116521845e-29, 3.394938017098991e-30, 1.173065586050388e-31, 3.860321180828446e-33, 1.212610150096554e-34, 3.885354643377144e-36, 1.6850001966158988e-37], [9.016483053286614e-11, 6.230997988031067e-11, 2.1530199578590082e-11, 4.959606735917621e-12, 8.568557000077601e-13, 1.1842901741683304e-13, 1.3640406591788182e-14, 1.346634436494247e-15, 1.1632690394386126e-16, 8.932193038317667e-18, 6.17274790198545e-19, 3.8779865245971354e-20, 2.2332918952961807e-21, 1.1871964186237401e-22, 5.8602343318850515e-24, 2.6998781465430465e-25, 1.1661236980938598e-26, 4.740412559633098e-28, 1.8199693548253702e-29, 6.619587307738339e-31, 2.2872906737776722e-32, 7.527010202749262e-34, 2.3643962624310196e-35, 7.104162197479534e-37, 2.1814181867619978e-38]] |
| Legacy trial inputs | {"lambda_home": 4.679616964597059, "lambda_away": 0.6910674540401642, "rho": -0.10363221309641538, "max_goals": 24, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.9351 |
| Legacy p draw | 0.0425 |
| Legacy p away | 0.0224 |
| Legacy p over 1 5 | 0.9708 |
| Legacy p under 3 5 | 0.2208 |
| Legacy p btts yes | 0.4992 |
| Legacy p over 2 5 | 0.9012 |
| Legacy goal margin distribution | {"-1": 0.016748421633815597, "-10": 6.761996892530149e-11, "-11": 4.148569764984484e-12, "-12": 2.341414609236431e-13, "-13": 1.2232628171320459e-14, "-14": 5.947873682050614e-16, "-15": 2.704239527741802e-17, "-16": 1.1544242018780129e-18, "-17": 4.6442268054319315e-20, "-18": 1.7664773007476587e-21, "-19": 6.371216312228006e-23, "-2": 0.004624340539989191, "-20": 2.1847631351959062e-24, "-21": 7.13985780105333e-26, "-22": 2.2278355285142336e-27, "-23": 6.604610675354415e-29, "-24": 1.675935614078705e-30, "-3": 0.0008625670637512796, "-4": 0.00012993158562574022, "-5": 1.631878907189824e-05, "-6": 1.7517554920216646e-06, "-7": 1.6387047713662925e-07, "-8": 1.3566894148856545e-08, "-9": 1.0065781605504803e-09, "0": 0.0425486776502047, "1": 0.07950977266223254, "10": 0.008534865419359496, "11": 0.0035457652126925, "12": 0.0013551262787664259, "13": 0.00047941441122706526, "14": 0.0001578493918315245, "15": 4.859775411616821e-05, "16": 1.4048382783543347e-05, "17": 3.827050530509239e-06, "18": 9.857089576986708e-07, "19": 2.407425513830894e-07, "2": 0.13202390900697517, "20": 5.590166381811155e-08, "21": 1.2370857487261857e-08, "22": 2.6138654814478956e-09, "23": 5.247315731773394e-10, "24": 9.016483053286614e-11, "3": 0.1667575540692385, "4": 0.17009723352839626, "5": 0.14466394604328214, "6": 0.1051564055133131, "7": 0.06661205461304001, "8": 0.037344135849533715, "9": 0.018762009325973678} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.9456 |
| Legacy raw p draw | 0.0403 |
| Legacy raw p away | 0.0141 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 4.6796 |
| Legacy lambda away | 0.6911 |
| Legacy model home team | PSV Eindhoven |
| Legacy model away team | Willem II |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 95.1% |
| Market reference home draw last update utc | 2026-10-30T12:00:49Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 10.8% |
| Market reference draw away last update utc | 2026-10-30T12:00:49Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 94.2% |
| Market reference home away last update utc | 2026-10-30T12:00:49Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.02 |
| Market reference dc draw away odds | 9.00 |
| Market reference dc home away odds | 1.03 |
| Market p over 1 5 | 97.5% |
| Market reference over 1 5 odds | 1.02 |
| Market reference over 1 5 opposite odds | 17.00 |
| Market reference over 1 5 last update utc | 2026-10-30T12:00:49Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 23.9% |
| Market under 3 5 odds | 3.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference under 3 5 odds | 3.51 |
| Market reference under 3 5 opposite odds | 1.27 |
| Market reference under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-30T12:02:36Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,679.0337 |
| Elo away rating | 1,344.0120 |
| Elo rating diff | 395.0217 |
| Elo home expectancy | 0.9067 |

</details>


---

## 2026-10-31 — SC Cambuur vs Go Ahead Eagles

The model's most likely 1X2 outcome is **Go Ahead Eagles win** at **42.7%**. Expected goals are 1.77 for SC Cambuur and 2.02 for Go Ahead Eagles (3.79 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 66.4%; Under 3.5 goals: 55.5%; Double Chance 1X: 57.3%; Double Chance X2: 66.6%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 74.1%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

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
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 86.4% |
| Under 1.5 | 13.6% |
| Over 2.5 | 66.4% |
| Under 2.5 | 33.6% |
| Over 3.5 | 44.5% |
| Under 3.5 | 55.5% |
| Over 4.5 | 25.9% |
| Under 4.5 | 74.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.32% |
| 2 | 1-2 | 8.72% |
| 3 | 2-1 | 7.65% |
| 4 | 2-2 | 6.83% |
| 5 | 0-2 | 5.47% |

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
| Market best home last update utc | 2026-10-30T12:02:36Z |
| Market best draw last update utc | 2026-10-30T12:02:36Z |
| Market best away last update utc | 2026-10-30T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Cambuur |
| Matched away-team name | Go Ahead Eagles |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7685 |
| Dc lambda away | 2.0173 |
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
| P btts yes | 67.6% |
| P btts no | 32.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.11 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.35 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.98 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.86 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.1920854924741905, "-10": 4.6836122325489e-06, "-11": 7.58057212211316e-07, "-12": 1.1283071306707196e-07, "-13": 1.5540900646692256e-08, "-14": 1.9901808582990974e-09, "-15": 2.3541547059520953e-10, "-16": 2.265453290071554e-11, "-2": 0.1308741032362938, "-3": 0.06539475668676552, "-4": 0.02624568274600468, "-5": 0.008753165140977338, "-6": 0.002489624638835724, "-7": 0.0006161642889889366, "-8": 0.00013481969346723513, "-9": 2.6415731175353347e-05, "0": 0.23945434237438085, "1": 0.16753584890546622, "10": 1.2581129401053014e-06, "11": 1.785194289847939e-07, "12": 2.3294620800590765e-08, "13": 2.8128676851310556e-09, "14": 3.157987975618461e-10, "15": 3.274897669720481e-11, "16": 2.7628840175955916e-12, "2": 0.10074742557843179, "3": 0.044133459721383474, "4": 0.015528436415762984, "5": 0.004540250164021655, "6": 0.001132122290657029, "7": 0.00024564096778465367, "8": 4.711968930960479e-05, "9": 8.093875624928874e-06} |
| Raw goal margin distribution | {"-1": 0.18558226591585386, "-10": 9.610728621815232e-06, "-11": 1.7171123759024028e-06, "-12": 2.823236032066456e-07, "-13": 4.298087303248265e-08, "-14": 6.090755334152081e-09, "-15": 8.062830878141821e-10, "-16": 9.867812393668327e-11, "-17": 9.678394048651832e-12, "-2": 0.13234162371837546, "-3": 0.07084394788764642, "-4": 0.030781761177762938, "-5": 0.011187320525462993, "-6": 0.0034824709640634294, "-7": 0.0009460623938482962, "-8": 0.00022769432363096411, "-9": 4.914738246563078e-05, "0": 0.22731967468192102, "1": 0.1617439868345194, "10": 2.5775339137473266e-06, "11": 4.0373053726465864e-07, "12": 5.8194893385532533e-08, "13": 7.767079113969342e-09, "14": 9.649358851658724e-10, "15": 1.1198495021847906e-10, "16": 1.2015388079059045e-11, "17": 1.0331539152038637e-12, "2": 0.10171525063000951, "3": 0.04773502750066687, "4": 0.018183299575891397, "5": 0.0057936214863367405, "6": 0.0015810891137730343, "7": 0.0003765593462419647, "8": 7.945306641437367e-05, "9": 1.503500785389907e-05} |
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
| Totals anchor scale | 0.9016 |
| Totals anchor target over 2 5 | 0.6640 |
| Totals anchor reference over odds | 1.46 |
| Totals anchor reference under odds | 2.74 |
| Totals anchor reference last update utc | 2026-10-30T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7248 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.7, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.7, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.87 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.28 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:36Z |
| Market reference home last update utc | 2026-10-30T12:02:36Z |
| Market reference draw last update utc | 2026-10-30T12:02:36Z |
| Market reference away last update utc | 2026-10-30T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-30T12:01:56Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:01:56Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.5% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | 0.0047 |
| Raw ev home | -0.0322 |
| Raw edge prob draw | -0.0173 |
| Raw ev draw | -0.1248 |
| Raw edge prob away | 0.0126 |
| Raw ev away | -0.0072 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.026991289868189525, 0.030327547757114513, 0.039599743539211266, 0.027610287347887, 0.014438123191594144, 0.006040050178951927, 0.002105664155013876, 0.0006292031266080342, 0.00016451317836788543, 3.8234726804512516e-05, 7.997565383436616e-06, 1.5207748511728507e-06, 2.650839808517033e-07, 4.265205293209145e-08, 6.3725274035797905e-09, 8.886285466515754e-10, 1.1617163076269676e-10, 1.4293907665104333e-11], [0.02629808219865412, 0.08449229916155387, 0.07605403212832797, 0.05302745657807838, 0.02772940900485764, 0.011600331954469838, 0.004044072889975175, 0.0012084278969864506, 0.00031595887838857745, 7.343242356933092e-05, 1.535987459156173e-05, 2.920752738626369e-06, 5.091120243351473e-07, 8.191620233157294e-08, 1.2238877340470803e-08, 1.7066722659521146e-09, 2.2311561007150833e-10, 2.745243316348132e-11], [0.0322428458701101, 0.0674424246085738, 0.07688868739038801, 0.05092143945678967, 0.02662811895822943, 0.011139617839834259, 0.0038834601188631602, 0.0011604344610359797, 0.0003034103827516096, 7.051601099225348e-05, 1.4749847994810922e-05, 2.804753298495935e-06, 4.888923361001468e-07, 7.866285141199363e-08, 1.175280301430673e-08, 1.6388907571929405e-09, 2.1425444030852892e-10, 2.6362143377883216e-11], [0.0206415346544348, 0.0431759389461185, 0.045155598531973526, 0.03432018465727376, 0.01704704486920739, 0.007131467507688515, 0.002486150786613418, 0.000742898075379869, 0.0001942401720776297, 4.514361698879826e-05, 9.44269931255593e-06, 1.7955738969590674e-06, 3.1298378990961907e-07, 5.035913951201659e-08, 7.524022280286695e-09, 1.0492008210352014e-09, 1.3716346479808829e-10, 1.6876770068370436e-11], [0.009910871886278178, 0.020730590366875308, 0.02168110847816488, 0.015116805857848357, 0.008617063863667247, 0.003424118507325768, 0.001193705911338402, 0.0003566967172215865, 9.326290379365823e-05, 2.1675355633650263e-05, 4.533838433727221e-06, 8.621308034033792e-07, 1.5027672584458693e-07, 2.4179548098647512e-08, 3.612600619954528e-09, 5.037655917712331e-10, 6.585796792002636e-11, 8.103249530715357e-12], [0.003806902275073453, 0.007962905033667018, 0.008328012120297481, 0.005806573152435092, 0.0030364051427475254, 0.0013846786035127273, 0.000458518867137664, 0.00013701211758999186, 3.58235647383959e-05, 8.325802373554497e-06, 1.741509732566345e-06, 3.311563053732232e-07, 5.772335835562734e-08, 9.287697159564068e-09, 1.3876496111384249e-09, 1.93503296119976e-10, 2.52969517498842e-11, 3.1125696536021536e-12], [0.0012185696255463173, 0.0025488845008371746, 0.0026657533810164028, 0.0018586538767753384, 0.0009719374994288165, 0.0004066007187674461, 0.00015451696139071305, 4.3856866492251365e-05, 1.1466936820215344e-05, 2.6650460525728065e-06, 5.574482110018683e-07, 1.0600141161442459e-07, 1.847694689649881e-08, 2.9729435725268807e-09, 4.4417942590917094e-10, 6.193939903286529e-11, 8.09742273216742e-12, 9.963173633616914e-13], [0.0003343352585104359, 0.0006993297228449986, 0.0007313946836378872, 0.0005099532364385911, 0.0002666675488336046, 0.00011155780808068077, 3.8890948043111675e-05, 1.2668049668218087e-05, 3.14614873515392e-06, 7.312006160745048e-07, 1.5294537778088212e-07, 2.9083286347869577e-08, 5.06946397449796e-09, 8.156775263556192e-10, 1.218681641763235e-10, 1.6994125369200687e-11, 2.2216653572123464e-12, 2.7335657828220314e-13], [8.02642334893136e-05, 0.00016788885626520267, 0.00017558672669434184, 0.00012242503474057194, 6.401917195022757e-05, 2.6781805769564996e-05, 9.33659270117227e-06, 2.789909922460846e-06, 7.951690390745645e-07, 1.7554013668080446e-07, 3.6717765179806234e-08, 6.982056563409409e-09, 1.2170317959512105e-09, 1.9582060150963588e-10, 2.925702430531152e-11, 4.079798381592516e-12, 5.333576475328432e-13, 6.562501461208504e-14], [1.7128109222074892e-05, 3.582690000599687e-05, 3.7469598873920794e-05, 2.6125078075180433e-05, 1.3661469396780365e-05, 5.715144522579652e-06, 1.992396520786528e-06, 5.953571073225547e-07, 1.556637051655317e-07, 3.943702279377862e-08, 7.835443821611433e-09, 1.4899466700657326e-09, 2.5971036689169485e-10, 4.178743762669839e-11, 6.243347578731871e-12, 8.706148336078579e-13, 1.1381667330801525e-13, 1.4004150654795792e-14], [3.2895712260947125e-06, 6.880802653220287e-06, 7.196294273398445e-06, 5.0175009979986924e-06, 2.623779195423539e-06, 1.097632828626565e-06, 3.82653460505935e-07, 1.1434242881725442e-07, 2.989628562152479e-08, 6.948235542884724e-09, 1.5842867858689904e-09, 2.8615450956764305e-10, 4.9879162899331765e-11, 8.025564914768934e-12, 1.1990778598629518e-12, 1.6720756906177102e-13, 2.1859275224689004e-14, 2.689593488844593e-15], [5.743498071581269e-07, 1.2013686299359721e-06, 1.2564525721141903e-06, 8.760414450844562e-07, 4.5810440672720897e-07, 1.9164357909359526e-07, 6.681020903471572e-08, 1.9963863807000336e-08, 5.219806686433082e-09, 1.2131422212379804e-09, 2.537531988488855e-10, 5.259907514740582e-11, 8.708760389556976e-12, 1.4012408743630755e-12, 2.0935559385879594e-13, 2.919396737307258e-14, 3.8165674633594565e-15, 4.695953957153107e-16], [9.192319356658241e-08, 1.9227592616570738e-07, 2.0109196791613964e-07, 1.4020815594472095e-07, 7.331841941699479e-08, 3.067205664084628e-08, 1.069280027742951e-08, 3.195164504621378e-09, 8.354164908512409e-10, 1.9416025884718482e-10, 4.06125398236682e-11, 7.72266636719269e-12, 1.4673891188758174e-12, 2.2426495930209623e-13, 3.3506818560192506e-14, 4.67241858596569e-15, 6.108317010328914e-16, 7.515752233277924e-17], [1.3580370617083628e-08, 2.8406088134676996e-08, 2.9708535424651014e-08, 2.0713800809019894e-08, 1.083177455122209e-08, 4.531368859254917e-09, 1.5797122039364994e-09, 4.720410211148625e-10, 1.234211424254492e-10, 2.8684472024394785e-11, 5.999936698315338e-12, 1.1409163166486226e-12, 1.9887141005957122e-13, 3.4880947068104816e-14, 4.9501654217136904e-15, 6.902847215550997e-16, 9.024187000946357e-17, 1.1103476373474614e-17], [1.863002583416023e-09, 3.896846196014282e-09, 4.075520455679361e-09, 2.841591404804835e-09, 1.4859405932943707e-09, 6.216289767956073e-10, 2.1671042712820497e-10, 6.47562328460355e-11, 1.6931342573045835e-11, 3.935035868472354e-12, 8.23092232492733e-13, 1.5651487763552162e-13, 2.7281873312241937e-14, 4.38965757516418e-15, 7.149272901113902e-16, 9.469566448591729e-17, 1.2379694317652379e-17, 1.5232135964433814e-18], [2.3853497635909573e-10, 4.989440828025556e-10, 5.218211634274463e-10, 3.638314539126802e-10, 1.902567433065884e-10, 7.959208140880871e-11, 2.7747152404378847e-11, 8.291253382327609e-12, 2.167853891530198e-12, 5.038338090423572e-13, 1.0538701769216277e-13, 2.0039839433920353e-14, 3.4931143217391118e-15, 5.620426269062723e-16, 8.397326261511246e-17, 1.2764653655000253e-17, 1.5850703148137376e-18, 1.9502910111442318e-19], [2.8632677156389025e-11, 5.989102755509362e-11, 6.263709051747899e-11, 4.3672708791932975e-11, 2.2837572883746205e-11, 9.553879292539037e-12, 3.3306447085046465e-12, 9.95245162540091e-13, 2.602195348700647e-13, 6.047796853517278e-14, 1.2650188664624707e-14, 2.405493154653819e-15, 4.1929789991949336e-16, 6.746509602059228e-17, 1.007977678966284e-17, 1.4055926058691632e-18, 2.003082093692551e-19, 2.341042547950472e-20], [3.2347662676977096e-12, 6.766167013123384e-12, 7.076402475604967e-12, 4.9339083609793405e-12, 2.5800664742921534e-12, 1.0793460315416213e-12, 3.762783722217414e-13, 1.1243745956027885e-13, 2.9398207125240725e-14, 6.832476456460429e-15, 1.429150454525663e-15, 2.717597125602921e-16, 4.737002744688926e-17, 7.621844637943775e-18, 1.138759109636666e-18, 1.5879631243550474e-19, 2.0759660089975106e-20, 2.784393327306833e-21]] |
| Legacy trial inputs | {"lambda_home": 1.920568805023195, "lambda_away": 2.091701981899017, "rho": -0.10363221309641538, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3445 |
| Legacy p draw | 0.2329 |
| Legacy p away | 0.4226 |
| Legacy p over 1 5 | 0.9164 |
| Legacy p under 3 5 | 0.4317 |
| Legacy p btts yes | 0.7575 |
| Legacy p over 2 5 | 0.7600 |
| Legacy goal margin distribution | {"-1": 0.17827988827180344, "-10": 1.1461384072370534e-05, "-11": 2.116603808061163e-06, "-12": 3.598711575561918e-07, "-13": 5.667508774408399e-08, "-14": 8.310330879908805e-09, "-15": 1.1381063001009669e-09, "-16": 1.4362406392617807e-10, "-17": 1.4293907665104333e-11, "-2": 0.12772974100859874, "-3": 0.06936081050258927, "-4": 0.0307669898380197, "-5": 0.011462325840517564, "-6": 0.0036675303692542257, "-7": 0.0010260436684712214, "-8": 0.0002546510499729036, "-9": 5.673796990887899e-05, "0": 0.2328622248000948, "1": 0.15749776079015027, "10": 4.714314600512715e-06, "11": 7.993760470542614e-07, "12": 1.2479255052976673e-07, "13": 1.804529075179158e-08, "14": 2.429517665097037e-09, "15": 3.055024063897943e-10, "16": 3.539884416951241e-11, "17": 3.2347662676977096e-12, "2": 0.10399992485535572, "3": 0.05185435253206265, "4": 0.02111962133614183, "5": 0.007224435729352051, "6": 0.0021224377582247525, "7": 0.0005452016378091239, "8": 0.00012424154427080215, "9": 2.541705477867788e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3565 |
| Legacy raw p draw | 0.2211 |
| Legacy raw p away | 0.4224 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9206 |
| Legacy lambda away | 2.0917 |
| Legacy model home team | Cambuur |
| Legacy model away team | Go Ahead Eagles |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 56.9% |
| Market reference home draw last update utc | 2026-10-30T12:02:41Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.2% |
| Market reference draw away last update utc | 2026-10-30T12:02:41Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.9% |
| Market reference home away last update utc | 2026-10-30T12:02:41Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.64 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 86.4% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.96 |
| Market reference over 1 5 last update utc | 2026-10-30T12:02:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.8% |
| Market under 3 5 odds | 1.73 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference under 3 5 odds | 1.73 |
| Market reference under 3 5 opposite odds | 2.15 |
| Market reference under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.8% |
| Market reference btts yes odds | 1.37 |
| Market reference btts yes opposite odds | 2.86 |
| Market reference btts yes last update utc | 2026-10-30T12:02:36Z |
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
| Market best home last update utc | 2026-10-30T12:02:36Z |
| Market best draw last update utc | 2026-10-30T12:02:36Z |
| Market best away last update utc | 2026-10-30T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Excelsior |
| Matched away-team name | Twente |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.0885 |
| Dc lambda away | 1.8371 |
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
| Goal margin distribution | {"-1": 0.25071783101123823, "-10": 8.610757667254956e-06, "-11": 1.4168825742289886e-06, "-12": 2.141972807159243e-07, "-13": 2.9943230483859385e-08, "-14": 3.891338277745167e-09, "-15": 4.696302583137879e-10, "-16": 4.7931736188592485e-11, "-2": 0.18674083687723242, "-3": 0.09923746175384485, "-4": 0.04166132541886572, "-5": 0.014390209554835671, "-6": 0.0042122343559357865, "-7": 0.0010683333420758838, "-8": 0.00023883822553615, "-9": 4.771087364005568e-05, "0": 0.215523182724771, "1": 0.11326721365349081, "10": 3.6153424766111664e-08, "11": 3.5249634432627273e-09, "12": 3.1575293269098867e-10, "13": 2.6154400798714576e-11, "14": 2.013992222828144e-12, "15": 1.4402157482054366e-13, "16": 8.709782833937432e-15, "2": 0.051599551243535394, "3": 0.016247814534449963, "4": 0.004041709262163858, "5": 0.0008272024022790057, "6": 0.0001434728998503398, "7": 2.156139295121671e-05, "8": 2.856186416362334e-06, "9": 3.3807477224542113e-07} |
| Raw goal margin distribution | {"-1": 0.22568069035441576, "-10": 7.750871675072728e-06, "-11": 1.2753900917753505e-06, "-12": 1.9280714893326264e-07, "-13": 2.695304478258616e-08, "-14": 3.502742128000972e-09, "-15": 4.2273212272176804e-10, "-16": 4.314518544332178e-11, "-2": 0.16809255573819193, "-3": 0.0893274275199986, "-4": 0.03750094934886439, "-5": 0.012953176938318572, "-6": 0.00379159293755842, "-7": 0.0009616476227313826, "-8": 0.00021498740398566196, "-9": 4.294637863238943e-05, "0": 0.24851526358520176, "1": 0.12954842461639163, "10": 4.1350176029448536e-08, "11": 4.0316473423815344e-09, "12": 3.6113976568066174e-10, "13": 2.9913876319272774e-11, "14": 2.3034866952340693e-12, "15": 1.647234669853485e-13, "16": 9.9617409883439e-15, "2": 0.05901655350119726, "3": 0.01858330145594107, "4": 0.004622671034114113, "5": 0.0009461058023549002, "6": 0.00016409592459489292, "7": 2.4660662156926035e-05, "8": 3.2667392329649145e-06, "9": 3.8667018225525076e-07} |
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
| Unanchored p over 2 5 | 0.5742 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.57, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.47, "price": 1.57, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.18 |
| Reference draw odds | 4.53 |
| Reference away odds | 1.56 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:36Z |
| Market reference home last update utc | 2026-10-30T12:02:36Z |
| Market reference draw last update utc | 2026-10-30T12:02:36Z |
| Market reference away last update utc | 2026-10-30T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-30T12:01:56Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:01:56Z |
| Home probability edge | +1.1% |
| Draw probability edge | +1.4% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.0382 |
| Raw ev home | 0.1029 |
| Raw edge prob draw | 0.0471 |
| Raw ev draw | 0.1258 |
| Raw edge prob away | -0.0854 |
| Raw ev away | -0.1598 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.059894169206570674, 0.09662936296773242, 0.09808138229395096, 0.05886770444854457, 0.02649896350860451, 0.00954268658658681, 0.00286372418743393, 0.0007366224068736121, 0.0001657932007220205, 3.316927538953218e-05, 5.9723845282422815e-06, 9.77612743729495e-07, 1.4668894523356466e-07, 2.0317291475982147e-08, 2.6130610297357707e-09, 3.1366789661157065e-10, 3.5298956465153264e-11], [0.044392720751087744, 0.10786900233127095, 0.10698470899946748, 0.06421141385445804, 0.028904404010733496, 0.010408922913416926, 0.0031236784360272087, 0.0008034892249547859, 0.00018084306030859837, 3.618021272005619e-05, 6.514527077850218e-06, 1.0663554331709434e-06, 1.6000461812638637e-07, 2.2161591378279007e-08, 2.8502613577191763e-09, 3.4214106547653705e-10, 3.850321536141524e-11], [0.029765389067081923, 0.05359488474006706, 0.047990935062641356, 0.035020098947398506, 0.015764099055127597, 0.005676895873838425, 0.0017036150014929639, 0.00043821293555166863, 9.862953462311553e-05, 1.973223377803457e-05, 3.552941278927816e-06, 5.815768652499426e-07, 8.726450988180094e-08, 1.2086653700824275e-08, 1.5544967597118556e-09, 1.8659944155901513e-10, 2.0999170253531815e-11], [0.010822446330177407, 0.019486651505351324, 0.017543611458352513, 0.010472819341439673, 0.005731694471831888, 0.0020640718244320615, 0.0006194201553821724, 0.00015933055554923954, 3.586087326536958e-05, 7.17447504401892e-06, 1.2918197111017233e-06, 2.1145648043959422e-07, 3.172864539403828e-08, 4.39460612101566e-09, 5.65202010781764e-10, 6.78459951241449e-11, 7.635122542323476e-12], [0.002951213176794186, 0.005313887538885708, 0.0047840327154201456, 0.002871340282700014, 0.0012855546356533706, 0.0005628594293997909, 0.00016891198798911516, 4.34484423075116e-05, 9.779035024364052e-06, 1.956434307042907e-06, 3.522711258743077e-07, 5.766285480684133e-08, 8.652202423736206e-09, 1.1983815022485036e-09, 1.5412704030867378e-10, 1.8501176970013984e-11, 2.0820499881355384e-12], [0.000643821845757556, 0.001159251019321422, 0.0010436605519470172, 0.0006263971763009198, 0.0002819691386335579, 0.00010099443398347772, 3.68489910294658e-05, 9.478493977212143e-06, 2.1333451709350788e-06, 4.26805883278154e-07, 7.684969972716608e-08, 1.2579438823771411e-08, 1.8875210296969747e-09, 2.61432890299524e-10, 3.362358109300342e-11, 4.03612385549886e-12, 4.5420956942765857e-13], [0.00011704411718260784, 0.00021074698388008487, 0.0001897331206542369, 0.00011387638519713757, 5.126080937075414e-05, 1.8459810242805965e-05, 5.509876293404849e-06, 1.7231505378294173e-06, 3.8783322408712395e-07, 7.759152340948414e-08, 1.3970953796590846e-08, 2.286889333567892e-09, 3.4314342397707704e-10, 4.752740536724205e-11, 6.112626328977318e-12, 7.337504258661347e-13, 8.257339886781683e-14], [1.8238397723568107e-05, 3.283964545651284e-05, 2.9565160549050724e-05, 1.774478593663363e-05, 7.987714815920236e-06, 2.876499641452463e-06, 8.632266734979088e-07, 2.2084759678677514e-07, 6.043410605830738e-08, 1.2090697917878785e-08, 2.1770236561507495e-09, 3.5635449452212714e-10, 5.347031865733831e-11, 7.40595719564974e-12, 9.524999018063286e-13, 1.1433664859811168e-13, 1.2866998583008296e-14], [2.4867482842266517e-06, 4.477582583258765e-06, 4.0311168438459695e-06, 2.4194458663916043e-06, 1.0890998438812103e-06, 3.922016975601447e-07, 1.1769824749712961e-07, 3.027497087065127e-08, 6.77734530134454e-09, 1.6485287116825575e-09, 2.968303424295862e-10, 4.858781682802281e-11, 7.290510120105827e-12, 1.0097790183366512e-12, 1.2987037197254137e-13, 1.5589443164635355e-14, 1.7543748707758104e-15], [3.013869540677022e-07, 5.426705167204432e-07, 4.88560114734561e-07, 2.9323008879856423e-07, 1.31995862510486e-07, 4.7533751508988905e-08, 1.4264699220772974e-08, 3.6692420029281725e-09, 8.25844245589879e-10, 1.6433175895704937e-10, 3.5975009351437935e-11, 5.888707840468566e-12, 8.835894861718082e-13, 1.2238239975808486e-13, 1.573992674719636e-14, 1.889397017302928e-15, 2.1262533966539912e-16], [3.287453217220562e-08, 5.919313732745763e-08, 5.329091054913373e-08, 3.198480179039756e-08, 1.4397777243285188e-08, 5.1848622581615005e-09, 1.5559575725855598e-09, 4.0023170427534105e-10, 9.008101662813404e-11, 1.8021981811650693e-11, 3.227516069929886e-12, 6.42325464793398e-13, 9.637972247349706e-14, 1.3349164865494216e-14, 1.7168716868966744e-15, 2.0609068240373021e-16, 2.319263815210169e-17], [3.259883110868023e-09, 5.869671624292028e-09, 5.284398827393086e-09, 3.171656241822737e-09, 1.4277030810223204e-09, 5.141379600178117e-10, 1.5429085912246968e-10, 3.968751757033974e-11, 8.932555547182833e-12, 1.787084111932753e-12, 3.2177831367829915e-13, 5.238777486524109e-14, 9.557143745064005e-15, 1.3237212581844565e-15, 1.7024732051925233e-16, 2.0436231042192544e-17, 2.2998133939205242e-18], [2.963165535188466e-10, 5.335408684437332e-10, 4.803407958806248e-10, 2.88296915736099e-10, 1.297752226165326e-10, 4.673406473924835e-11, 1.402471624280366e-11, 3.607512301577689e-12, 8.119506079934503e-13, 1.6244220632659382e-13, 2.924897539681143e-14, 4.787731090276733e-15, 7.145199676089235e-16, 1.2032349250105652e-16, 1.547512519510262e-17, 1.857610639212432e-18, 2.0904822518055024e-19], [2.486266585540443e-11, 4.476715247525018e-11, 4.030335991316604e-11, 2.418977204604408e-11, 1.0888888784339736e-11, 3.9212572563984955e-12, 1.176754486109102e-12, 3.0269106419558293e-13, 6.812733348138668e-14, 1.3629836904997245e-14, 2.454157532773866e-15, 4.0171821955100653e-16, 6.027705989412503e-17, 8.303755913606097e-18, 1.2984521526972855e-18, 1.558642339205171e-19, 1.754035037397527e-20], [1.9371122584126903e-12, 3.4879204160316106e-12, 3.140135213056484e-12, 1.8846854247697242e-12, 8.483804619870218e-13, 3.0551492522705915e-13, 9.168387466738884e-14, 2.358341516454043e-14, 5.30797033541264e-15, 1.061934560935134e-15, 1.912095295194872e-16, 3.129886762930624e-17, 4.696335956130165e-18, 6.504704655003481e-19, 8.320806312924637e-20, 1.2143770902584312e-20, 1.3666124109090803e-21], [1.4086356072788464e-13, 2.536357339147169e-13, 2.2834537614283947e-13, 1.3705116914729128e-13, 6.169280701645307e-14, 2.2216533934002096e-14, 6.6670978880492134e-15, 1.7149464723966522e-15, 3.859867173092431e-16, 7.722210360482727e-17, 1.3904436904079676e-17, 2.276001260054758e-18, 3.4150968911681517e-19, 4.730112337102507e-20, 6.083523598096857e-21, 7.263230122657586e-22, 9.937776682767746e-23], [9.603152186375113e-15, 1.7291218112760724e-14, 1.556708766144851e-14, 9.343248373399541e-15, 4.20581029985558e-15, 1.5145773351145713e-15, 4.545189354121062e-16, 1.1691378437981015e-16, 2.63140386987694e-17, 5.264495723643765e-18, 9.479131648082448e-19, 1.5516281402902735e-19, 2.3281887102412438e-20, 3.2246798531235716e-21, 4.147346740352823e-22, 4.9784123438436037e-23, 5.5723289794165014e-24]] |
| Legacy trial inputs | {"lambda_home": 1.0907748901706251, "lambda_away": 1.8005773288997116, "rho": -0.10363221309641538, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1961 |
| Legacy p draw | 0.2276 |
| Legacy p away | 0.5763 |
| Legacy p over 1 5 | 0.7991 |
| Legacy p under 3 5 | 0.6669 |
| Legacy p btts yes | 0.5580 |
| Legacy p over 2 5 | 0.5634 |
| Legacy goal margin distribution | {"-1": 0.24496735907665917, "-10": 7.130557323153605e-06, "-11": 1.1502881729540269e-06, "-12": 1.7047496141666783e-07, "-13": 2.336178739780266e-08, "-14": 2.9762012654658394e-09, "-15": 3.521711119729859e-10, "-16": 3.5298956465153264e-11, "-2": 0.18029975773667375, "-3": 0.09411408609400908, "-4": 0.03878105215469419, "-5": 0.013142474456823205, "-6": 0.003773382623301713, "-7": 0.0009385491195428907, "-8": 0.00020574673106547552, "-9": 4.029834072972715e-05, "0": 0.22761921268040738, "1": 0.11870388052692092, "10": 3.924960541593918e-08, "11": 3.8356752320340435e-09, "12": 3.443650981866004e-10, "13": 2.858827489595228e-11, "14": 2.2063150799888557e-12, "15": 1.5815477884064537e-13, "16": 9.603152186375113e-15, "2": 0.05471672923255378, "3": 0.01730226539674916, "4": 0.0043190803327727316, "5": 0.0008866907747454266, "6": 0.00015422303581976197, "7": 2.3238000861226746e-05, "8": 3.0860151576430594e-06, "9": 3.6616398832601023e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2175 |
| Legacy raw p draw | 0.2539 |
| Legacy raw p away | 0.5286 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0908 |
| Legacy lambda away | 1.8006 |
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

The model's most likely 1X2 outcome is **FC Zwolle win** at **43.0%**. Expected goals are 1.76 for FC Zwolle and 1.48 for ADO Den Haag (3.24 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.4%; Under 3.5 goals: 63.1%; Double Chance 1X: 68.3%; Double Chance X2: 57.0%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

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
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 36.9% |
| Under 3.5 | 63.1% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.64% |
| 2 | 2-1 | 9.09% |
| 3 | 1-2 | 7.70% |
| 4 | 1-0 | 6.73% |
| 5 | 2-0 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Zwolle win | 43.0% | 42.9% | 2.25 | -3.2% |
| Draw | 25.3% | 25.4% | 3.71 | -6.2% |
| ADO Den Haag win | 31.7% | 31.7% | 3.00 | -4.9% |

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
| Market best home last update utc | 2026-10-30T12:02:36Z |
| Market best draw last update utc | 2026-10-30T12:02:36Z |
| Market best away last update utc | 2026-10-30T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Zwolle |
| Matched away-team name | Den Haag |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.7578 |
| Dc lambda away | 1.4784 |
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
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.00 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.61 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.71 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.06 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.16892218892500177, "-10": 4.712935969849459e-07, "-11": 5.9075192255096624e-08, "-12": 6.80543496696209e-09, "-13": 7.248044260295971e-10, "-14": 7.114262791558067e-11, "-15": 5.755816799567118e-12, "-2": 0.09450112701946786, "-3": 0.03758304966015132, "-4": 0.01188646381803186, "-5": 0.003105210103137416, "-6": 0.0006891498583481329, "-7": 0.00013273946980512478, "-8": 2.256249742653483e-05, "-9": 3.4296540832588007e-06, "0": 0.2528973973729176, "1": 0.20143652775904886, "10": 2.6426278181079893e-06, "11": 3.9384247987694145e-07, "12": 5.3944385799015646e-08, "13": 6.830997901847858e-09, "14": 7.971979430125322e-10, "15": 7.668601659811934e-11, "2": 0.13267767259443833, "3": 0.06273730015554989, "4": 0.023591710539048627, "5": 0.007327750934579402, "6": 0.001933598635865719, "7": 0.00044281843140367715, "8": 8.949231261808225e-05, "9": 1.6174163583664343e-05} |
| Raw goal margin distribution | {"-1": 0.1646780464237622, "-10": 6.829440331198767e-07, "-11": 9.004556445747993e-08, "-12": 1.0914552884221475e-08, "-13": 1.2239645246628685e-09, "-14": 1.2761382959090908e-10, "-15": 1.2314134325897772e-11, "-16": 9.788590683191031e-13, "-2": 0.09460843911681364, "-3": 0.03907009988037293, "-4": 0.012892071117789398, "-5": 0.003523820945514072, "-6": 0.0008197425151093069, "-7": 0.00016570436617521274, "-8": 2.958432427580748e-05, "-9": 4.726439154108903e-06, "0": 0.2499958183416452, "1": 0.19764260148936272, "10": 3.8558010985688995e-06, "11": 6.044561259912319e-07, "12": 8.711267677586309e-08, "13": 1.1614945879971632e-08, "14": 1.439855973890088e-09, "15": 1.6519547550068308e-10, "16": 1.5613036716173917e-11, "2": 0.13374445302686216, "3": 0.0656694492204145, "4": 0.0257640714982094, "5": 0.008372951711726579, "6": 0.0023158752669439064, "7": 0.0005566018010972534, "8": 0.00011815313798888917, "9": 2.2443502249022674e-05} |
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
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9489 |
| Totals anchor target over 2 5 | 0.5945 |
| Totals anchor reference over odds | 1.62 |
| Totals anchor reference under odds | 2.31 |
| Totals anchor reference last update utc | 2026-10-30T12:02:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6265 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.5, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.86, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.6, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.88, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.26, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:56:00Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.77, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.25 |
| Reference draw odds | 3.71 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:36Z |
| Market reference home last update utc | 2026-10-30T12:02:36Z |
| Market reference draw last update utc | 2026-10-30T12:02:36Z |
| Market reference away last update utc | 2026-10-30T12:02:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:02:36Z |
| Home probability edge | +0.2% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0057 |
| Raw ev home | -0.0230 |
| Raw edge prob draw | -0.0041 |
| Raw ev draw | -0.0725 |
| Raw edge prob away | -0.0015 |
| Raw ev away | -0.0526 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05022358250503002, 0.04806920717310243, 0.044066092838737726, 0.022109807316912373, 0.008320063365612114, 0.0025047148865870008, 0.0006283602647607336, 0.0001351177303177535, 2.5422837520648047e-05, 4.251901351058536e-06, 6.400071815746426e-07, 8.757775931448186e-08, 1.0985358917434693e-08, 1.271957399189443e-09, 1.3675593960798247e-10, 1.372323834219206e-11, 1.2910358167289131e-12], [0.05805115872193149, 0.11353091579224248, 0.07612098635985179, 0.03819309207532291, 0.014372307349430164, 0.004326713702867701, 0.0010854468835702384, 0.0002334061007889092, 4.391611199159385e-05, 7.34485187810523e-06, 1.1055660894905443e-06, 1.5128424130091356e-07, 1.8976412530430186e-08, 2.1972143568148857e-09, 2.3623598878221175e-10, 2.3705901099102758e-11, 2.2301709424283236e-12], [0.0594063826382515, 0.08942002266912122, 0.0668699981137637, 0.032987901282122145, 0.012413560418315834, 0.0037370424008802408, 0.0009375154693310964, 0.00020159607387337954, 3.7930952650187324e-05, 6.3438500399210264e-06, 9.548927054413553e-07, 1.306662892790433e-07, 1.6390189671160943e-08, 1.8977643955960876e-09, 2.0404028722951276e-10, 2.0475114288173033e-11, 1.9262294539021244e-12], [0.03420674227569369, 0.05148887264109884, 0.03875119098574748, 0.01931925304702376, 0.0071478424218960335, 0.002151823433833177, 0.0005398300420708584, 0.00011608087610333863, 2.1840991892696854e-05, 3.652847281960251e-06, 5.498360146732832e-07, 7.523885284695776e-08, 9.437622171765358e-09, 1.0927502180269705e-09, 1.1748827666581997e-10, 1.1789759389758438e-11, 1.1091406607722633e-12], [0.014772417943383243, 0.022235825322319977, 0.016734969510735682, 0.0083966362230214, 0.003139582342050189, 0.0009292798141592434, 0.00023312933267928863, 5.013032820290198e-05, 9.4321832209735e-06, 1.5775073316704498e-06, 2.374504810664033e-07, 3.249241833314659e-08, 4.075702327611694e-09, 4.719117301002968e-10, 5.073812385778081e-11, 5.09148903317794e-12, 4.789900560209327e-13], [0.005103656586416419, 0.00768215581197351, 0.005781689747357855, 0.0029009162838207216, 0.0010916335431499803, 0.000326537752026619, 8.05428101733642e-05, 1.7319302817759435e-05, 3.258682783313056e-06, 5.450059505665592e-07, 8.20357043976749e-08, 1.1225660245338418e-08, 1.408096163289584e-09, 1.6303867239366417e-10, 1.7529287419407336e-11, 1.7590357677691259e-12, 1.6548413154897034e-13], [0.001469366234418573, 0.0022117280358751913, 0.0016645751039093368, 0.0008351871573150133, 0.00031428632422730504, 9.461437976499412e-05, 2.3584812467304707e-05, 4.986307039509294e-06, 9.381897800932211e-07, 1.5690972301135937e-07, 2.361845708418351e-08, 3.2319192806695153e-09, 4.053973699286124e-10, 4.6939584602398476e-11, 5.046762573337816e-12, 5.064344981936476e-13, 4.764364355495815e-14], [0.00036260340477046164, 0.0005458000173469164, 0.000410776146909696, 0.00020610362465748455, 7.755812578795813e-05, 2.3348499127998397e-05, 5.857460732317658e-06, 1.2515202377975608e-06, 2.3152213560784997e-07, 3.872145587177091e-08, 5.828453624115564e-09, 7.975580952272184e-10, 1.0004208833563701e-10, 1.1583533632835795e-11, 1.2454167308972823e-12, 1.249755636387691e-13, 1.1757278045479304e-14], [7.829639256190168e-05, 0.0001178537538706755, 8.869825829094631e-05, 4.450363701032687e-05, 1.6747006186837654e-05, 5.041605317010809e-06, 1.2647924395629596e-06, 2.7197118172625877e-07, 5.0846308986995146e-08, 8.361064098181076e-09, 1.2585289795374964e-09, 1.7221548637791452e-10, 2.1601933456741682e-11, 2.501214507747458e-12, 2.6892090913272463e-13, 2.698578022867784e-14, 2.5387308701389933e-15], [1.5027927991006762e-05, 2.2620425650365737e-05, 1.7024424688151736e-05, 8.541868027959774e-06, 3.2143601359636927e-06, 9.676675921335073e-07, 2.4275971195345554e-07, 5.2201170461076985e-08, 9.821818882678794e-09, 1.6322096564403865e-09, 2.415575259630499e-10, 3.305442107281482e-11, 4.146197415133489e-12, 4.800741168601455e-13, 5.161571210994885e-14, 5.179553601234966e-15, 4.872748725278958e-16], [2.595965804834511e-06, 3.907514829342549e-06, 2.940846160819381e-06, 1.4755458851854168e-06, 5.552574514848966e-07, 1.6715757362747688e-07, 4.193498341220276e-08, 9.017374422501135e-09, 1.6966481324618012e-09, 2.837598470598017e-10, 4.2440204936792764e-11, 5.7099120287892754e-12, 7.162255978482841e-13, 8.29293294392193e-14, 8.916240729247284e-15, 8.947304007019426e-16, 8.417320786967455e-17], [4.076675509456891e-07, 6.136317349771827e-07, 4.618271742472727e-07, 2.3171806662525535e-07, 8.719700581942863e-08, 2.625023740136721e-08, 6.585422641070041e-09, 1.4160783396820131e-09, 2.6643971491811407e-10, 4.456132730722432e-11, 6.7074861673405635e-12, 9.119974657899654e-13, 1.124752625229728e-13, 1.302312864487441e-14, 1.4001964182136685e-15, 1.4050745604257623e-16, 1.3218465914908359e-17], [5.868468264714425e-08, 8.833370118817716e-08, 6.648108512845369e-08, 3.3356349240866e-08, 1.2552209766079915e-08, 3.778782117286201e-09, 9.479867526665126e-10, 2.0384773763562314e-10, 3.835461046211202e-11, 6.414705672044941e-12, 9.655580783345968e-13, 1.3212572518403645e-13, 1.646768946914919e-14, 1.874709355268763e-15, 2.0156149847080713e-16, 2.02263718274567e-17, 1.9028286050704947e-18], [7.797964793934592e-09, 1.1737698167766502e-08, 8.833943337673958e-09, 4.432359949843193e-09, 1.667925690771991e-09, 5.021209723791758e-10, 1.2596757772140013e-10, 2.7087093423741282e-11, 5.096524145269094e-12, 8.523799863556591e-13, 1.2830243875773477e-13, 1.7556740649910134e-14, 2.2022383190578614e-15, 2.5336550919296974e-16, 2.678330013878914e-17, 2.6876610438177625e-18, 2.5284605457355154e-19], [9.621728464720473e-10, 1.448287438524227e-09, 1.089999843727664e-09, 5.468986462783839e-10, 2.05801494621034e-10, 6.195554584231637e-11, 1.5542848169007143e-11, 3.342213830260854e-12, 6.288483307569308e-13, 1.0517319575301849e-13, 1.5830941273914997e-14, 2.1662856363541097e-15, 2.7172909445626983e-16, 3.146258896649784e-17, 3.3611891418944204e-18, 3.31624282132385e-19, 3.1198090075693836e-20], [1.1080559738625623e-10, 1.6678744926247505e-10, 1.2552638985606476e-10, 6.298185552918914e-11, 2.3700479220633e-11, 7.134914785447428e-12, 1.7899430261054959e-12, 3.848955012735545e-13, 7.241933215052134e-14, 1.211193895895652e-14, 1.823120358753392e-15, 2.494734443251166e-16, 3.1292823060693325e-17, 3.6232897015685085e-18, 3.8956209376641865e-19, 3.884292831035773e-20, 3.5928295220789275e-21], [1.1963040662155804e-11, 1.8007078022501795e-11, 1.3552359641066155e-11, 6.799787343298659e-12, 2.558803917104092e-12, 7.703155590758205e-13, 1.9324981507566183e-13, 4.155494524672357e-14, 7.818697210961583e-15, 1.3076561264180143e-15, 1.9683178014684045e-16, 2.6934207557998417e-17, 3.378505450439947e-18, 3.911856716004746e-19, 4.205877029764802e-20, 4.220529878472946e-21, 3.945240906179452e-22]] |
| Legacy trial inputs | {"lambda_home": 1.7274276310001135, "lambda_away": 1.5052258477617535, "rho": -0.10363221309641538, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4247 |
| Legacy p draw | 0.2534 |
| Legacy p away | 0.3219 |
| Legacy p over 1 5 | 0.8437 |
| Legacy p under 3 5 | 0.5952 |
| Legacy p btts yes | 0.6504 |
| Legacy p over 2 5 | 0.6267 |
| Legacy goal margin distribution | {"-1": 0.16534098629892602, "-10": 8.088269075680132e-07, "-11": 1.0857468149033868e-07, "-12": 1.339888231092487e-08, "-13": 1.5297776429206e-09, "-14": 1.6238807016098734e-10, "-15": 1.5953409284620384e-11, "-16": 1.2910358167289131e-12, "-2": 0.09707599560525551, "-3": 0.04081253903490252, "-4": 0.013710375041192036, "-5": 0.0038152617134744908, "-6": 0.0009035992588781902, "-7": 0.00018596147709091252, "-8": 3.380206487231846e-05, "-9": 5.498061311209185e-06, "0": 0.25343475840672947, "1": 0.1958113960670712, "10": 3.280724114549212e-06, "11": 5.054065649125983e-07, "12": 7.157792131808472e-08, "13": 9.378578409658181e-09, "14": 1.1425126553755883e-09, "15": 1.28812675408758e-10, "16": 1.1963040662155804e-11, "2": 0.13087009463306495, "3": 0.0631422962838628, "4": 0.024343010547987372, "5": 0.00777405271839515, "6": 0.002112988861488285, "7": 0.0004990482343859295, "8": 0.00010410245270601288, "9": 1.9432358056572035e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4208 |
| Legacy raw p draw | 0.2527 |
| Legacy raw p away | 0.3265 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7274 |
| Legacy lambda away | 1.5052 |
| Legacy model home team | Zwolle |
| Legacy model away team | Den Haag |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Market p home draw | 68.6% |
| Market reference home draw last update utc | 2026-10-30T12:02:41Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.9% |
| Market reference draw away last update utc | 2026-10-30T12:02:41Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market reference home away last update utc | 2026-10-30T12:02:41Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.64 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.9% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.77 |
| Market reference over 1 5 last update utc | 2026-10-30T12:02:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.2% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.52 |
| Market reference under 3 5 last update utc | 2026-10-30T12:02:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.2% |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.42 |
| Market reference btts yes last update utc | 2026-10-30T12:02:36Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,408.9706 |
| Elo away rating | 1,360.6524 |
| Elo rating diff | 108.3181 |
| Elo home expectancy | 0.6510 |

</details>


---

## 2026-11-01 — Groningen vs Sparta Rotterdam

The model's most likely 1X2 outcome is **Groningen win** at **53.0%**. Expected goals are 1.67 for Groningen and 1.21 for Sparta Rotterdam (2.89 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 56.4%; Under 3.5 goals: 66.8%; Double Chance 1X: 76.2%; Double Chance X2: 47.0%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Groningen win | 53.0% | 1.89 |
| Draw | 23.2% | 4.30 |
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
| Over 2.5 | 56.4% |
| Under 2.5 | 43.6% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.97% |
| 2 | 2-1 | 10.66% |
| 3 | 1-0 | 9.28% |
| 4 | 2-0 | 8.78% |
| 5 | 1-2 | 6.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Groningen win | 53.0% | 55.5% | 1.75 | -7.3% |
| Draw | 23.2% | 21.9% | 4.23 | -1.7% |
| Sparta Rotterdam win | 23.8% | 22.6% | 4.12 | -2.0% |

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
| Market best home last update utc | 2026-10-30T12:02:36Z |
| Market best draw last update utc | 2026-10-30T12:02:36Z |
| Market best away last update utc | 2026-10-30T12:02:36Z |
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
| Fair Under 0.5 odds | 17.00 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.94 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.82 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.13662541039969797, "-10": 1.147190221610031e-07, "-11": 1.2475474471428187e-08, "-12": 1.246452794997938e-09, "-13": 1.1512414294786718e-10, "-14": 9.817612030434103e-12, "-15": 7.000106592801277e-13, "-2": 0.06867164363486328, "-3": 0.024076629867248085, "-4": 0.00667294850788436, "-5": 0.0015222347742829437, "-6": 0.0002943475696533162, "-7": 4.932383677749998e-05, "-8": 7.286245193494718e-06, "-9": 9.618372585677513e-07, "0": 0.23240390870199443, "1": 0.24232088601575438, "10": 3.57257608227727e-06, "11": 5.353089356412156e-07, "12": 7.369272702324409e-08, "13": 9.378137014972638e-09, "14": 1.1019386103938735e-09, "15": 1.0825739165331112e-10, "2": 0.164631343595448, "3": 0.0795302134220996, "4": 0.030370755557674937, "5": 0.009545986871863872, "6": 0.002543320075957885, "7": 0.0005872172274974503, "8": 0.00011952179018254229, "9": 2.173933599834742e-05} |
| Raw goal margin distribution | {"-1": 0.1532160036697895, "-10": 1.286494955000975e-07, "-11": 1.3990386830713093e-08, "-12": 1.3978111059569456e-09, "-13": 1.2910381060726006e-10, "-14": 1.1009776852512104e-11, "-15": 7.850138230318019e-13, "-2": 0.07701052660986513, "-3": 0.027000284934584912, "-4": 0.007483252932827687, "-5": 0.001707081633500676, "-6": 0.0003300905606084518, "-7": 5.531329153633225e-05, "-8": 8.171022996670467e-06, "-9": 1.0786343514528436e-06, "0": 0.2628068775800391, "1": 0.21519449698872015, "10": 3.1726473339553845e-06, "11": 4.753842684917766e-07, "12": 6.544326237922e-08, "13": 8.328310080118835e-09, "14": 9.785831047214885e-10, "15": 9.613861737295957e-11, "2": 0.14620183904121364, "3": 0.07062727672455602, "4": 0.02697092922058862, "5": 0.008477370138940959, "6": 0.002258610445950118, "7": 0.0005214817342909891, "8": 0.00010614203315454756, "9": 1.9305745996360374e-05} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 58.2% |
| P home draw | 76.2% |
| P draw away | 47.0% |
| P home away | 76.8% |
| Raw p home draw | 73.3% |
| Raw p draw away | 53.0% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5636 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.81, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.75 |
| Reference draw odds | 4.23 |
| Reference away odds | 4.12 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:36Z |
| Market reference home last update utc | 2026-10-30T12:02:36Z |
| Market reference draw last update utc | 2026-10-30T12:02:36Z |
| Market reference away last update utc | 2026-10-30T12:02:36Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-30T12:01:56Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:01:56Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | -0.0847 |
| Raw ev home | -0.1768 |
| Raw edge prob draw | 0.0434 |
| Raw ev draw | 0.1117 |
| Raw edge prob away | 0.0413 |
| Raw ev away | 0.0993 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05656400527199108, 0.046765431046738415, 0.034754736970429426, 0.014016547733964291, 0.004239643876725158, 0.0010259062669417762, 0.00020687344250939436, 3.575650073200797e-05, 5.40770923978086e-06, 7.269744241893257e-07, 8.79563990948108e-08, 9.674378285356722e-09, 9.754165680242724e-10, 9.078102558316997e-11, 7.845404824182888e-12, 6.328086516896687e-13, 4.785207057037603e-14], [0.08209375091721169, 0.11065298798622955, 0.06237506013360848, 0.02515579411564783, 0.007608978366914952, 0.0018412156347603753, 0.0003712801344907039, 6.417294670433111e-05, 9.705329932532468e-06, 1.3047163459469084e-06, 1.5785720626636935e-07, 1.736281094050086e-08, 1.7506007062461239e-09, 1.6292662305454103e-10, 1.4080313659035105e-11, 1.1357150461473654e-12, 8.5881121237788e-14], [0.08422864123564522, 0.10190795903167388, 0.05442821184407414, 0.022573817376423385, 0.006827997052537931, 0.0016522342844204746, 0.0003331721476553842, 5.7586271089308256e-05, 8.709180257547252e-06, 1.1708009846971776e-06, 1.41654830271998e-07, 1.5580701666994016e-08, 1.5709200218512011e-09, 1.4620392493603723e-10, 1.2635118083754156e-11, 1.0191458844640274e-12, 7.706633064302198e-14], [0.05038897351379372, 0.06096545513687646, 0.03688095292345104, 0.01313187794033511, 0.004084783484397376, 0.0009884332499597807, 0.00019931702895185994, 3.445043213458969e-05, 5.2101832213658646e-06, 7.004204145093469e-07, 8.474363810176184e-08, 9.32100473315286e-09, 9.397877754182443e-10, 8.746509017762657e-11, 7.558837719876546e-12, 6.096942112039801e-13, 4.610419017341467e-14], [0.022608538626460315, 0.02735399733762172, 0.01654775619753898, 0.006673692130950478, 0.0017821823365759184, 0.0004434905050263829, 8.942961988967422e-05, 1.5457229455168564e-05, 2.3377064543483885e-06, 3.1426482605090244e-07, 3.802279907222124e-08, 4.1821509916096705e-09, 4.2166424000287025e-10, 3.924386094522021e-11, 3.3915014068344274e-12, 2.735577679620931e-13, 2.0686040847646562e-14], [0.008115204310470421, 0.009818559296135223, 0.0059397214761026185, 0.002395483230590438, 0.0007245718420207694, 0.000154795170420399, 3.2100245345492296e-05, 5.548283202864999e-06, 8.391062247932979e-07, 1.128035435254848e-07, 1.3648064035678472e-08, 1.5011589344579667e-09, 1.513539426222646e-10, 1.4086357139838463e-11, 1.2173598342839162e-12, 9.819198022513737e-14, 7.425134840733014e-15], [0.0024274214154499903, 0.0029369292740483864, 0.0017766905873579826, 0.0007165373873315927, 0.00021673406350151487, 5.244516767708107e-05, 9.336845795786351e-06, 1.6596034986129943e-06, 2.5099360927643393e-07, 3.3741816818969786e-08, 4.0824114405713944e-09, 4.490269383354718e-10, 4.5273019332371775e-11, 4.213513755014583e-12, 3.641368989609741e-13, 2.9371203300009536e-14, 2.2210077079321694e-15], [0.0006223634940843876, 0.000752995566917925, 0.00045552344344378115, 0.0001837121107951994, 5.55681713069608e-05, 1.3446349939735961e-05, 2.7114491750902198e-06, 4.137608415295094e-07, 6.435193274142521e-08, 8.651021564921192e-09, 1.046684284925901e-09, 1.151254464930531e-10, 1.1607491933666437e-11, 1.08029744083698e-12, 9.336059710109878e-14, 7.530445515109786e-15, 5.694413457420944e-16], [0.0001396211126612244, 0.0001689271300154292, 0.00010219219253928364, 4.121400043925121e-05, 1.2466171265140754e-05, 3.0165560121422585e-06, 6.082868843510987e-07, 1.0513776037048933e-07, 1.4038305615751535e-08, 1.940771378834708e-09, 2.348132977840712e-10, 2.5827258648305022e-11, 2.6040263517849383e-12, 2.4235407784743996e-13, 2.09445293142535e-14, 1.6893811922583502e-15, 1.2774855055530586e-16], [2.7842328708473857e-05, 3.3686342932109354e-05, 2.0378498365230215e-05, 8.218626293324912e-06, 2.485922304188695e-06, 6.015418618054959e-07, 1.2130059029289068e-07, 2.0965884228488067e-08, 3.17081939064242e-09, 3.7633529783597006e-10, 4.6824931397646215e-11, 5.150302924957199e-12, 5.192778962293683e-13, 4.832866441653461e-14, 4.176620990169659e-15, 3.368853432854313e-16, 2.547478005867315e-17], [4.996921510090453e-06, 6.045759079861369e-06, 3.6573721218071075e-06, 1.4750142108627267e-06, 4.461537238597958e-07, 1.0795998782820575e-07, 2.1770073012489722e-08, 3.7627915026918286e-09, 5.690736498233626e-10, 7.650226196673652e-11, 8.171847146074664e-12, 9.2433573853209e-13, 9.319590026222628e-14, 8.67364742746628e-15, 7.495869861963867e-16, 6.046152374405506e-17, 4.5720125558773615e-18], [8.15280047462582e-07, 9.86404677284493e-07, 5.967239051151812e-07, 2.406581038769166e-07, 7.279286425242204e-08, 1.7614369932147708e-08, 3.551928146769153e-09, 6.139237586004956e-10, 9.28480448013476e-11, 1.2481838596281418e-11, 1.5101735913691877e-12, 1.466493507446101e-13, 1.5205513601859742e-14, 1.4151616494393177e-15, 1.2229996257685097e-16, 9.8646884583186e-18, 7.45953404716926e-19], [1.2193335935155535e-07, 1.475267748250704e-07, 8.924608247500648e-08, 3.5992848288409485e-08, 1.0886907514472111e-08, 2.6344067972378185e-09, 5.312267023568788e-10, 9.181849415409298e-11, 1.3886362173448903e-11, 1.8667849356369125e-12, 2.2586170208967285e-13, 2.4842667147329295e-14, 2.211377735875049e-15, 2.1165170726141643e-16, 1.8291193721687833e-17, 1.4753637187895334e-18, 1.1156486024642917e-19], [1.683356723943138e-08, 2.0366878242681647e-08, 1.232090986575198e-08, 4.969009588710762e-09, 1.502997134245685e-09, 3.636942686821186e-10, 7.333875209427543e-11, 1.2676045369257232e-11, 1.9170882570690597e-12, 2.5771987176207244e-13, 3.118144344712855e-14, 3.4296660901932763e-15, 3.457951538063304e-16, 2.841328898813256e-17, 2.525199346929743e-18, 2.03682031684665e-19, 1.540213922181317e-20], [2.1579684636453646e-09, 2.6109190242018208e-09, 1.57947121697587e-09, 6.369990291108054e-10, 1.926757632840932e-10, 4.6623555843003066e-11, 9.401614757674962e-12, 1.6249975873514836e-12, 2.457599118438329e-13, 3.303823531916258e-14, 3.99728534378776e-15, 4.3966386673731495e-16, 4.4328990176693276e-17, 4.125653923900073e-18, 3.147825994849443e-19, 2.6110888722215377e-20, 1.974467457823925e-21], [2.5819677051186053e-10, 3.123914327172825e-10, 1.8898068911104675e-10, 7.621570699775961e-11, 2.3053283990917527e-11, 5.578418661460606e-12, 1.1248850986115463e-12, 1.9442783164447069e-13, 2.940470012808543e-14, 3.952961225581898e-15, 4.782674927681437e-16, 5.2604934879617077e-17, 5.303878298730846e-18, 4.936265461456907e-19, 4.2659796599545185e-20, 3.0379000405303403e-21, 2.3624122858112357e-22], [2.896194967013333e-11, 3.5040968691446794e-11, 2.1197977015013946e-11, 8.549121144183116e-12, 2.585888465423598e-12, 6.257316084622875e-13, 1.2617843959118784e-13, 2.1808983371082294e-14, 3.2983272543908667e-15, 4.4340393505437934e-16, 5.3647297861053415e-17, 5.900699196832619e-18, 5.949363969186396e-19, 5.537012394450736e-20, 4.785152345650265e-21, 3.8596935044661387e-22, 2.5767886251282253e-23]] |
| Legacy trial inputs | {"lambda_home": 1.7947211105835568, "lambda_away": 1.2098967469576944, "rho": -0.10363221309641538, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5274 |
| Legacy p draw | 0.2367 |
| Legacy p away | 0.2358 |
| Legacy p over 1 5 | 0.8146 |
| Legacy p under 3 5 | 0.6437 |
| Legacy p btts yes | 0.5917 |
| Legacy p over 2 5 | 0.5849 |
| Legacy goal margin distribution | {"-1": 0.13627640873550695, "-10": 1.0698108706173525e-07, "-11": 1.1579022737161563e-08, "-12": 1.151608689414619e-09, "-13": 1.0592658931684252e-10, "-14": 9.058186200973275e-12, "-15": 7.186897729274567e-13, "-16": 4.785207057037603e-14, "-2": 0.06782219917635655, "-3": 0.023493408564787974, "-4": 0.006450936801463382, "-5": 0.0014603112295142628, "-6": 0.00028049556021839144, "-7": 4.672171310086282e-05, "-8": 6.863837543125156e-06, "-9": 9.013926110595314e-07, "0": 0.23672382557922517, "1": 0.22833619184877743, "10": 6.077739659799049e-06, "11": 9.757884101981146e-07, "12": 1.4395851040667602e-07, "13": 1.964201607388843e-08, "14": 2.491557873377661e-09, "15": 2.9323773920330733e-10, "16": 2.896194967013333e-11, "2": 0.1643681460486458, "3": 0.084457939600297, "4": 0.03440059073202057, "5": 0.011551468556391106, "6": 0.0032912921134468304, "7": 0.0008132196389405572, "8": 0.00017721674602014188, "9": 3.4522355309122984e-05} |
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
| 4 | 0-1 | 6.61% |
| 5 | 2-2 | 6.32% |

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
| Market best home last update utc | 2026-10-30T12:02:36Z |
| Market best draw last update utc | 2026-10-30T12:02:36Z |
| Market best away last update utc | 2026-10-30T12:02:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Telstar |
| Matched away-team name | Utrecht |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4645 |
| Dc lambda away | 1.5984 |
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
| Goal margin distribution | {"-1": 0.19899412539235828, "-10": 1.7823547089694535e-06, "-11": 2.5454449477260374e-07, "-12": 3.340955965062253e-08, "-13": 4.054077787593958e-09, "-14": 4.5337282718148954e-10, "-15": 4.1789996991686806e-11, "-2": 0.12587385963695857, "-3": 0.05703353017874779, "-4": 0.02055117304313567, "-5": 0.006116799368542492, "-6": 0.0015466729882056371, "-7": 0.00033942046179783614, "-8": 6.573236980494876e-05, "-9": 1.1384065620489507e-05, "0": 0.25685098437706183, "1": 0.1721540456077875, "10": 7.049602540825831e-07, "11": 9.224176239924155e-08, "12": 1.109246390876726e-08, "13": 1.233226191018476e-09, "14": 1.2635706763954109e-10, "15": 1.0671114520919146e-11, "2": 0.10026720950779816, "3": 0.04162430761775217, "4": 0.013741899693096873, "5": 0.00374738041985408, "6": 0.0008681513354465742, "7": 0.00017455341349033947, "8": 3.097155461858358e-05, "9": 4.914445183579583e-06} |
| Raw goal margin distribution | {"-1": 0.19336310280162392, "-10": 1.7319186490550231e-06, "-11": 2.4734153942110557e-07, "-12": 3.246415493192442e-08, "-13": 3.939357799948471e-09, "-14": 4.405435407548155e-10, "-15": 4.060744742313585e-11, "-2": 0.12231195274246566, "-3": 0.05541962777719382, "-4": 0.019969627635984515, "-5": 0.005943709658686289, "-6": 0.001502906115591221, "-7": 0.0003298157346011282, "-8": 6.387231258675521e-05, "-9": 1.1061925805773954e-05, "0": 0.26048783679629334, "1": 0.17628444112462413, "10": 7.218739702995372e-07, "11": 9.445486729918067e-08, "12": 1.135859917754756e-08, "13": 1.2628142957455241e-09, "14": 1.2938868193507742e-10, "15": 1.0927140590020488e-11, "2": 0.10267286446161934, "3": 0.04262297629828659, "4": 0.014071601389532744, "5": 0.003837289217706616, "6": 0.0008889804038033744, "7": 0.00017874137569583764, "8": 3.171463776771565e-05, "9": 5.0323547121203315e-06} |
| Unadjusted home-win probability | 34.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 39.9% |
| Raw p over 1 5 | 82.1% |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T12:02:36Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:36Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.90 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.32 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:36Z |
| Market reference home last update utc | 2026-10-30T12:02:36Z |
| Market reference draw last update utc | 2026-10-30T12:02:36Z |
| Market reference away last update utc | 2026-10-30T12:02:36Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-30T12:02:18Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:02:18Z |
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
| Legacy trial matrix | [[0.055994390142717454, 0.06323956870718302, 0.06015523496605706, 0.03228480737838055, 0.012995237921278963, 0.004184660770037226, 0.0011229360751458196, 0.00025828728126564435, 5.1982727243016165e-05, 9.299563797956175e-06, 1.4972992429805216e-06, 2.1916033050171542e-07, 2.9405375356037297e-08, 3.6419116172234083e-09, 4.188392692345574e-10, 4.49575008305407e-11], [0.05499253024340082, 0.11828585460237888, 0.08920990640395632, 0.04787820455061331, 0.01927187150559023, 0.006205830562177552, 0.0016653084676322863, 0.0003830387197397188, 7.709011916566408e-05, 1.3791205644552879e-05, 2.2204871346671133e-06, 3.250136514727286e-07, 4.360802155897945e-08, 5.400936338912234e-09, 6.211364983911961e-10, 6.667174425486591e-11], [0.04894328169595429, 0.07880233979193814, 0.06397851204233995, 0.03550156648178453, 0.014290043536633754, 0.004601607523626624, 0.0012348219786276217, 0.000284022233113649, 5.716212661557413e-05, 1.0226143788171445e-05, 1.6464855433331398e-06, 2.4099679308251786e-07, 3.233523669164764e-08, 4.004780511288461e-09, 4.6057112832179965e-10, 4.943692820850229e-11], [0.02419421231121015, 0.03895448922673842, 0.0313598188566152, 0.016973730760287357, 0.00706402054135925, 0.002274720156508985, 0.0006104115637986496, 0.0001404011739904165, 2.825704733264334e-05, 5.055106346831545e-06, 8.139098855325229e-07, 1.19132338006693e-07, 1.5984330321593924e-08, 1.979689685538985e-09, 2.276748774684706e-10, 2.443823739733881e-11], [0.008969973340717452, 0.014442327171908305, 0.011626612823564862, 0.006239905067008738, 0.0025330456083330582, 0.0008433495953089635, 0.00022630930834654925, 5.205355609432012e-05, 1.0476264240425857e-05, 1.8741742273858104e-06, 3.017560514499739e-07, 4.416816229401463e-08, 5.926170069504013e-09, 7.339674246782619e-10, 8.441017029089404e-11, 9.060445330004995e-12], [0.002660484935759659, 0.004283579495577541, 0.003448441494312212, 0.0018507494727982427, 0.00074496122742242, 0.00024192941978911975, 6.712310982520985e-05, 1.543903159812316e-05, 3.1072492788993397e-06, 5.558781625710083e-07, 8.950053680903804e-08, 1.3100231846844589e-08, 1.7576959928182058e-09, 2.1769398888075659e-10, 2.503597033721719e-11, 2.6873188354230073e-12], [0.0006575809299672096, 0.0010587544212070715, 0.0008523368556942621, 0.0004574420035614641, 0.00018412894962627322, 5.929227281537862e-05, 1.6046187631620265e-05, 3.816000842413379e-06, 7.680058033762732e-07, 1.3739407962012567e-07, 2.212147320828447e-08, 3.2379294935471604e-09, 4.3444236425529906e-10, 5.380651238891707e-11, 6.188036036474666e-12, 6.642133526725964e-13], [0.0001393127375210441, 0.00022430391463484299, 0.00018057302948667903, 9.691202233683472e-05, 3.900889892076047e-05, 1.2561448277046101e-05, 3.3708116861878594e-06, 7.819184652444008e-07, 1.6270695518152048e-07, 2.910781696789542e-08, 4.686575979017849e-09, 6.859761302212279e-10, 9.203940123771277e-11, 1.1399254746839747e-11, 1.3109751223520797e-12, 1.4071785880935488e-13], [2.5825009831114195e-05, 4.158019506096636e-05, 3.347361012860104e-05, 1.7965004307117703e-05, 7.2312497482680215e-06, 2.328570459673477e-06, 6.248620656204279e-07, 1.4372494362528785e-07, 2.9172065387885294e-08, 5.395842998524247e-09, 8.68771031895896e-10, 1.271623874607795e-10, 1.7061745279786404e-11, 2.113129575535351e-12, 2.430211768537995e-13, 2.6085483293413742e-14], [4.255373084533169e-06, 6.851468559709795e-06, 5.515688106797526e-06, 2.960223298731378e-06, 1.1915451629080516e-06, 3.836953451067101e-07, 1.0296302820312409e-07, 2.3682595308917645e-08, 4.766343454148051e-09, 8.599393900803862e-10, 1.4315366731430213e-10, 2.0953463503182447e-11, 2.8113867957289167e-12, 3.4819559716218607e-13, 4.004435164664625e-14, 4.298293175094731e-15], [6.310696563637772e-07, 1.016069290205988e-06, 8.17973730862271e-07, 4.389996042134095e-07, 1.7670553945819217e-07, 5.690182382949294e-08, 1.5269364527046544e-08, 3.512116795991959e-09, 7.068463013627688e-10, 1.264528166085313e-10, 2.0533052880250595e-11, 3.1073879422337226e-12, 4.1692722678884506e-13, 5.163722932947646e-14, 5.9385569093365646e-15, 6.374346838863307e-16], [8.50793708377329e-08, 1.369841428224773e-07, 1.1027735160734571e-07, 5.918492475093831e-08, 2.382303755067396e-08, 7.671374026803323e-09, 2.0585808776460205e-09, 4.734955710489484e-10, 9.52954051783099e-11, 1.7048080143329477e-11, 2.744868259142275e-12, 4.0518544692925446e-13, 5.6209177200350296e-14, 6.961613411219237e-15, 8.00622689485134e-16, 8.593748932199661e-17], [1.051435605677035e-08, 1.6928898716399913e-08, 1.3628395795365355e-08, 7.314245108974618e-09, 2.944120257298683e-09, 9.480507103926251e-10, 2.544054111602528e-10, 5.851595958328913e-11, 1.1776883288546503e-11, 2.1068513194954778e-12, 3.3921880147178474e-13, 4.9651601035317736e-14, 6.718572830761986e-15, 8.603364295529522e-16, 9.894328015696102e-17, 1.0620404834442355e-17], [1.1994412587464053e-09, 1.931190029703653e-09, 1.5546801077714608e-09, 8.343837048051254e-10, 3.3585502414494194e-10, 1.0815033572089641e-10, 2.9021686629821084e-11, 6.6752976445133775e-12, 1.3434659849309544e-12, 2.4034228867682095e-13, 3.8696903931246724e-14, 5.664082376802143e-15, 7.599663130462347e-16, 9.492399501251962e-17, 1.1287106110463694e-17, 1.2115389353604213e-18], [1.2705466174329352e-10, 2.045674969047365e-10, 1.6468447601875696e-10, 8.838476966260935e-11, 3.557652046430336e-11, 1.1456171131551303e-11, 3.074215224033231e-12, 7.071023095752689e-13, 1.4231094272796922e-13, 2.5459027666230014e-14, 4.099093643515214e-15, 5.999860895421303e-16, 8.050186879622929e-17, 9.970309429054384e-18, 1.156393440595105e-18, 1.283361469338897e-19], [1.2561427655965019e-11, 2.0224836915646147e-11, 1.628174915572758e-11, 8.738277484451314e-12, 3.517319883675143e-12, 1.132629554152763e-12, 3.039363657004744e-13, 6.990860772225359e-14, 1.4069760111135203e-14, 2.5170405385573413e-15, 4.0526233002041205e-16, 5.931842055190582e-17, 7.958924034577572e-18, 9.857278661187208e-19, 1.1336396445119393e-19, 1.2271814574639721e-20]] |
| Legacy trial inputs | {"lambda_home": 1.48299489569434, "lambda_away": 1.6100747040518133, "rho": -0.10363221309641538, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3356 |
| Legacy p draw | 0.2580 |
| Legacy p away | 0.4063 |
| Legacy p over 1 5 | 0.8258 |
| Legacy p under 3 5 | 0.6261 |
| Legacy p btts yes | 0.6291 |
| Legacy p over 2 5 | 0.5984 |
| Legacy goal margin distribution | {"-1": 0.19592951908937595, "-10": 1.8567149183195631e-06, "-11": 2.670098678947818e-07, "-12": 3.529132106066866e-08, "-13": 4.3124850438231065e-09, "-14": 4.855110134894233e-10, "-15": 4.49575008305407e-11, "-2": 0.12484074955352661, "-3": 0.0568240009874511, "-4": 0.020587346603342854, "-5": 0.006164215525002705, "-6": 0.0015685073302201793, "-7": 0.0003464634351068722, "-8": 6.754570096172115e-05, "-9": 1.1777791723635768e-05, "0": 0.2580243207348925, "1": 0.17220236689142204, "10": 7.825532878364434e-07, "11": 1.0365485175145056e-07, "12": 1.2618968839977211e-08, "13": 1.4202905048068694e-09, "14": 1.4727949865893966e-10, "15": 1.2561427655965019e-11, "2": 0.10157247288585942, "3": 0.042583867022959125, "4": 0.014210432414300948, "5": 0.003919027956213432, "6": 0.000918503316168407, "7": 0.00018687242112414118, "8": 3.3556692461154045e-05, "9": 5.3893815865871195e-06} |
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
